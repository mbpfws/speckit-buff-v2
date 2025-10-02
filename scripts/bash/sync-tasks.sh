#!/usr/bin/env bash

# Task synchronization validation script
# Cross-checks: YAML metadata ↔ in-code tags ↔ git changes
# Outputs JSON with misalignments
#
# Usage: ./sync-tasks.sh [--validate] [--json]

set -e

JSON_MODE=true
VALIDATE_MODE=false

for arg in "$@"; do
    case "$arg" in
        --validate) VALIDATE_MODE=true ;;
        --json) JSON_MODE=true ;;
    esac
done

# Get repo root
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")

# Find feature directory
FEATURE_NUM=$(echo "$CURRENT_BRANCH" | grep -oE '^[0-9]+' || echo "")
if [[ -z "$FEATURE_NUM" ]]; then
    echo '{"error":"Not on a feature branch (###-feature-name format)"}' >&2
    exit 1
fi

FEATURE_DIR="$REPO_ROOT/specs/$CURRENT_BRANCH"
TASKS_FILE="$FEATURE_DIR/tasks.md"

if [[ ! -f "$TASKS_FILE" ]]; then
    echo "{\"error\":\"tasks.md not found at $TASKS_FILE\"}" >&2
    exit 1
fi

# Arrays for tracking issues
declare -a misalignments
declare -a warnings

# Parse YAML frontmatter from tasks.md
parse_yaml_tasks() {
    local in_yaml=false
    local in_tasks=false
    
    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if $in_yaml; then
                break
            else
                in_yaml=true
            fi
            continue
        fi
        
        if $in_yaml; then
            if [[ "$line" =~ ^tasks: ]]; then
                in_tasks=true
            elif $in_tasks && [[ "$line" =~ ^[[:space:]]+- ]]; then
                # Skip, handled by id: parsing
                continue
            elif $in_tasks && [[ "$line" =~ ^[[:space:]]+id:[[:space:]]+\"(.+)\" ]]; then
                task_id="${BASH_REMATCH[1]}"
            elif $in_tasks && [[ "$line" =~ ^[[:space:]]+files_affected: ]]; then
                # Next lines are file paths
                while IFS= read -r file_line; do
                    if [[ "$file_line" =~ ^[[:space:]]+-[[:space:]]+\"(.+)\" ]]; then
                        file_path="${BASH_REMATCH[1]}"
                        # Check if file has matching TASK tag
                        if [[ -f "$REPO_ROOT/$file_path" ]]; then
                            if ! grep -q "TASK-$task_id" "$REPO_ROOT/$file_path" 2>/dev/null; then
                                misalignments+=("$file_path: missing TASK-$task_id tag")
                            fi
                        fi
                    else
                        break
                    fi
                done
            fi
        fi
    done < "$TASKS_FILE"
}

# Scan source files for TASK tags
scan_source_files() {
    for src_dir in "src" "lib" "app" "components" "services" "templates" "scripts"; do
        if [[ -d "$REPO_ROOT/$src_dir" ]]; then
            while IFS= read -r file; do
                # Extract TASK-XXX tags from file
                while IFS= read -r tag; do
                    task_id=$(echo "$tag" | grep -oE 'TASK-T[0-9]+' | head -1)
                    if [[ -n "$task_id" ]]; then
                        # Check if this task exists in tasks.md
                        if ! grep -q "id: \"$task_id\"" "$TASKS_FILE" 2>/dev/null; then
                            warnings+=("${file#$REPO_ROOT/}: references non-existent $task_id")
                        fi
                    fi
                done < <(grep -n "TASK-T[0-9]" "$file" 2>/dev/null || true)
            done < <(find "$REPO_ROOT/$src_dir" -type f \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -o -name "*.py" -o -name "*.sh" -o -name "*.ps1" \) 2>/dev/null)
        fi
    done
}

# Check git changes against tasks
check_git_changes() {
    # Get recently modified files
    local changed_files=$(git diff --name-only HEAD~1..HEAD 2>/dev/null || git diff --name-only --cached 2>/dev/null || true)
    
    if [[ -n "$changed_files" ]]; then
        while IFS= read -r file; do
            if [[ -f "$REPO_ROOT/$file" ]]; then
                # Check if file has TASK tag
                if ! grep -q "TASK-T[0-9]" "$REPO_ROOT/$file" 2>/dev/null; then
                    # Check if it's a source file that should have a tag
                    if [[ "$file" =~ \.(ts|tsx|js|jsx|py|sh|ps1)$ ]]; then
                        warnings+=("$file: modified but has no TASK tag")
                    fi
                fi
            fi
        done <<< "$changed_files"
    fi
}

# Run validation
if $VALIDATE_MODE; then
    parse_yaml_tasks
    scan_source_files
    check_git_changes
fi

# Output JSON
if $JSON_MODE; then
    misalign_json=$(printf '"%s",' "${misalignments[@]}")
    misalign_json="[${misalign_json%,}]"
    
    warn_json=$(printf '"%s",' "${warnings[@]}")
    warn_json="[${warn_json%,}]"
    
    cat << EOF
{
  "status": "$(if [[ ${#misalignments[@]} -eq 0 ]]; then echo "ok"; else echo "misaligned"; fi)",
  "misalignments": $misalign_json,
  "warnings": $warn_json,
  "tasks_file": "$TASKS_FILE",
  "files_checked": $(find "$REPO_ROOT" -type f \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -o -name "*.py" \) 2>/dev/null | wc -l | tr -d ' ')
}
EOF
else
    echo "Task Synchronization Check"
    echo "=========================="
    echo "Tasks file: $TASKS_FILE"
    
    if [[ ${#misalignments[@]} -gt 0 ]]; then
        echo ""
        echo "❌ Misalignments found:"
        for item in "${misalignments[@]}"; do
            echo "  - $item"
        done
    else
        echo "✓ No misalignments"
    fi
    
    if [[ ${#warnings[@]} -gt 0 ]]; then
        echo ""
        echo "⚠️  Warnings:"
        for item in "${warnings[@]}"; do
            echo "  - $item"
        done
    fi
fi
