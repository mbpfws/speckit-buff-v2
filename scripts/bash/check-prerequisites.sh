#!/usr/bin/env bash

# Consolidated prerequisite checking script
#
# This script provides unified prerequisite checking for Spec-Driven Development workflow.
# It replaces the functionality previously spread across multiple scripts.
#
# Usage: ./check-prerequisites.sh [OPTIONS]
#
# OPTIONS:
#   --json              Output in JSON format
#   --require-tasks     Require tasks.md to exist (for implementation phase)
#   --include-tasks     Include tasks.md in AVAILABLE_DOCS list
#   --paths-only        Only output path variables (no validation)
#   --validate-tags     Scan for missing code tags and metadata (NEW in v2.0)
#   --help, -h          Show help message
#
# OUTPUTS:
#   JSON mode: {"FEATURE_DIR":"...", "AVAILABLE_DOCS":["..."], "tag_validation": {...}}
#   Text mode: FEATURE_DIR:... \n AVAILABLE_DOCS: \n ✓/✗ file.md
#   Paths only: REPO_ROOT: ... \n BRANCH: ... \n FEATURE_DIR: ... etc.
#
# NEW in v2.0: --validate-tags flag
#   Scans source files for missing TODO/FIXME/HACK/TASK-XXX tags
#   Validates metadata completeness in YAML frontmatter
#   Outputs: {"missing_task_tags": [...], "orphaned_todos": [...], "metadata_issues": [...]}

set -e

# Parse command line arguments
JSON_MODE=false
REQUIRE_TASKS=false
INCLUDE_TASKS=false
PATHS_ONLY=false
VALIDATE_TAGS=false

for arg in "$@"; do
    case "$arg" in
        --json)
            JSON_MODE=true
            ;;
        --require-tasks)
            REQUIRE_TASKS=true
            ;;
        --include-tasks)
            INCLUDE_TASKS=true
            ;;
        --paths-only)
            PATHS_ONLY=true
            ;;
        --validate-tags)
            VALIDATE_TAGS=true
            ;;
        --help|-h)
            cat << 'EOF'
Usage: check-prerequisites.sh [OPTIONS]

Consolidated prerequisite checking for Spec-Driven Development workflow.

OPTIONS:
  --json              Output in JSON format
  --require-tasks     Require tasks.md to exist (for implementation phase)
  --include-tasks     Include tasks.md in AVAILABLE_DOCS list
  --paths-only        Only output path variables (no prerequisite validation)
  --help, -h          Show this help message

EXAMPLES:
  # Check task prerequisites (plan.md required)
  ./check-prerequisites.sh --json
  
  # Check implementation prerequisites (plan.md + tasks.md required)
  ./check-prerequisites.sh --json --require-tasks --include-tasks
  
  # Get feature paths only (no validation)
  ./check-prerequisites.sh --paths-only
  
EOF
            exit 0
            ;;
        *)
            echo "ERROR: Unknown option '$arg'. Use --help for usage information." >&2
            exit 1
            ;;
    esac
done

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Get feature paths and validate branch
eval $(get_feature_paths)
check_feature_branch "$CURRENT_BRANCH" "$HAS_GIT" || exit 1

# If paths-only mode, output paths and exit (support JSON + paths-only combined)
if $PATHS_ONLY; then
    if $JSON_MODE; then
        # Minimal JSON paths payload (no validation performed)
        printf '{"REPO_ROOT":"%s","BRANCH":"%s","FEATURE_DIR":"%s","FEATURE_SPEC":"%s","IMPL_PLAN":"%s","TASKS":"%s"}\n' \
            "$REPO_ROOT" "$CURRENT_BRANCH" "$FEATURE_DIR" "$FEATURE_SPEC" "$IMPL_PLAN" "$TASKS"
    else
        echo "REPO_ROOT: $REPO_ROOT"
        echo "BRANCH: $CURRENT_BRANCH"
        echo "FEATURE_DIR: $FEATURE_DIR"
        echo "FEATURE_SPEC: $FEATURE_SPEC"
        echo "IMPL_PLAN: $IMPL_PLAN"
        echo "TASKS: $TASKS"
    fi
    exit 0
fi

# Validate required directories and files
if [[ ! -d "$FEATURE_DIR" ]]; then
    echo "ERROR: Feature directory not found: $FEATURE_DIR" >&2
    echo "Run /specify first to create the feature structure." >&2
    exit 1
fi

if [[ ! -f "$IMPL_PLAN" ]]; then
    echo "ERROR: plan.md not found in $FEATURE_DIR" >&2
    echo "Run /plan first to create the implementation plan." >&2
    exit 1
fi

# Check for tasks.md if required
if $REQUIRE_TASKS && [[ ! -f "$TASKS" ]]; then
    echo "ERROR: tasks.md not found in $FEATURE_DIR" >&2
    echo "Run /tasks first to create the task list." >&2
    exit 1
fi

# Build list of available documents
docs=()

# Always check these optional docs
[[ -f "$RESEARCH" ]] && docs+=("research.md")
[[ -f "$DATA_MODEL" ]] && docs+=("data-model.md")

# Check contracts directory (only if it exists and has files)
if [[ -d "$CONTRACTS_DIR" ]] && [[ -n "$(ls -A "$CONTRACTS_DIR" 2>/dev/null)" ]]; then
    docs+=("contracts/")
fi

[[ -f "$QUICKSTART" ]] && docs+=("quickstart.md")

# Include tasks.md if requested and it exists
if $INCLUDE_TASKS && [[ -f "$TASKS" ]]; then
    docs+=("tasks.md")
fi

# Tag validation (if requested)
tag_validation_json=""
if $VALIDATE_TAGS; then
    missing_task_tags=()
    orphaned_todos=()
    metadata_issues=()
    
    # Scan source files for missing TASK-XXX tags
    # Look in common source directories
    for src_dir in "src" "lib" "app" "components" "services"; do
        if [[ -d "$REPO_ROOT/$src_dir" ]]; then
            while IFS= read -r file; do
                # Check if file has TODO/FIXME/HACK without TASK-XXX
                if grep -q "TODO\|FIXME\|HACK" "$file" 2>/dev/null; then
                    if ! grep -q "TASK-T[0-9]" "$file" 2>/dev/null; then
                        orphaned_todos+=("${file#$REPO_ROOT/}")
                    fi
                fi
            done < <(find "$REPO_ROOT/$src_dir" -type f \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -o -name "*.py" -o -name "*.java" \) 2>/dev/null)
        fi
    done
    
    # Check metadata completeness in spec/plan/tasks files
    for doc in "$FEATURE_SPEC" "$IMPL_PLAN" "$TASKS"; do
        if [[ -f "$doc" ]]; then
            # Check for required frontmatter fields
            if ! grep -q "^feature_id:" "$doc" 2>/dev/null; then
                metadata_issues+=("$(basename $doc): missing feature_id")
            fi
            if ! grep -q "^status:" "$doc" 2>/dev/null; then
                metadata_issues+=("$(basename $doc): missing status")
            fi
        fi
    done
    
    # Build JSON for tag validation
    orphaned_json=$(printf '"%s",' "${orphaned_todos[@]}")
    orphaned_json="[${orphaned_json%,}]"
    
    metadata_json=$(printf '"%s",' "${metadata_issues[@]}")
    metadata_json="[${metadata_json%,}]"
    
    tag_validation_json=",\"tag_validation\":{\"orphaned_todos\":$orphaned_json,\"metadata_issues\":$metadata_json}"
fi

# Output results
if $JSON_MODE; then
    # Build JSON array of documents
    if [[ ${#docs[@]} -eq 0 ]]; then
        json_docs="[]"
    else
        json_docs=$(printf '"%s",' "${docs[@]}")
        json_docs="[${json_docs%,}]"
    fi
    
    printf '{"FEATURE_DIR":"%s","AVAILABLE_DOCS":%s%s}\n' "$FEATURE_DIR" "$json_docs" "$tag_validation_json"
else
    # Text output
    echo "FEATURE_DIR:$FEATURE_DIR"
    echo "AVAILABLE_DOCS:"
    
    # Show status of each potential document
    check_file "$RESEARCH" "research.md"
    check_file "$DATA_MODEL" "data-model.md"
    check_dir "$CONTRACTS_DIR" "contracts/"
    check_file "$QUICKSTART" "quickstart.md"
    
    if $INCLUDE_TASKS; then
        check_file "$TASKS" "tasks.md"
    fi
    
    # Show tag validation results
    if $VALIDATE_TAGS; then
        echo ""
        echo "TAG VALIDATION:"
        if [[ ${#orphaned_todos[@]} -gt 0 ]]; then
            echo "⚠️  Orphaned TODOs (missing TASK-XXX):"
            for file in "${orphaned_todos[@]}"; do
                echo "  - $file"
            done
        else
            echo "✓ No orphaned TODOs"
        fi
        
        if [[ ${#metadata_issues[@]} -gt 0 ]]; then
            echo "⚠️  Metadata issues:"
            for issue in "${metadata_issues[@]}"; do
                echo "  - $issue"
            done
        else
            echo "✓ Metadata complete"
        fi
    fi
fi