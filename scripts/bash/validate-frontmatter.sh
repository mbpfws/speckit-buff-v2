#!/bin/bash
# validate-frontmatter.sh - Validate YAML frontmatter in markdown files
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

set -e

# Target file (required)
TARGET_FILE="${1}"

if [ -z "$TARGET_FILE" ]; then
    echo "[ERROR] Usage: validate-frontmatter.sh <file.md>"
    exit 0
fi

echo "[INFO] Validating frontmatter: $TARGET_FILE"

# Check if file exists
if [ ! -f "$TARGET_FILE" ]; then
    echo "[ERROR] File not found: $TARGET_FILE"
    exit 0
fi

# Check if file has YAML frontmatter (starts with ---)
if ! head -n 1 "$TARGET_FILE" | grep -q "^---$"; then
    echo "[ERROR] No YAML frontmatter found (file must start with ---)"
    exit 0
fi

echo "[INFO] Frontmatter delimiter found"

# Extract frontmatter (between first two --- lines)
frontmatter=$(awk '/^---$/,/^---$/{if(NR>1 && !/^---$/){print}}' "$TARGET_FILE" | head -n -1)

if [ -z "$frontmatter" ]; then
    echo "[ERROR] Empty frontmatter block"
    exit 0
fi

echo "[INFO] Frontmatter content extracted"

# Detect file type from filename or path
file_basename=$(basename "$TARGET_FILE")
file_type="unknown"

if [[ "$file_basename" == "spec.md" ]]; then
    file_type="spec"
elif [[ "$file_basename" == "plan.md" ]]; then
    file_type="plan"
elif [[ "$file_basename" == "tasks.md" ]]; then
    file_type="tasks"
fi

# Validate required fields based on file type
case "$file_type" in
    spec)
        # Required fields for spec.md
        if echo "$frontmatter" | grep -q "feature_id:"; then
            echo "[INFO] Required field present: feature_id"
        else
            echo "[ERROR] Missing required field: feature_id"
        fi
        
        if echo "$frontmatter" | grep -q "title:"; then
            echo "[INFO] Required field present: title"
        else
            echo "[WARN] Missing recommended field: title"
        fi
        
        if echo "$frontmatter" | grep -q "status:"; then
            echo "[INFO] Required field present: status"
        else
            echo "[WARN] Missing recommended field: status"
        fi
        
        if echo "$frontmatter" | grep -q "created:"; then
            echo "[INFO] Required field present: created"
        else
            echo "[WARN] Missing recommended field: created"
        fi
        
        # Optional fields
        if echo "$frontmatter" | grep -q "version:"; then
            echo "[INFO] Optional field present: version"
        fi
        ;;
        
    plan)
        # Required fields for plan.md
        if echo "$frontmatter" | grep -q "description:"; then
            echo "[INFO] Required field present: description"
        else
            echo "[WARN] Missing recommended field: description"
        fi
        
        if echo "$frontmatter" | grep -q "version:"; then
            echo "[INFO] Optional field present: version"
        fi
        
        if echo "$frontmatter" | grep -q "scripts:"; then
            echo "[INFO] Optional field present: scripts"
        fi
        ;;
        
    tasks)
        # Tasks.md typically has minimal frontmatter
        echo "[INFO] Tasks file detected (minimal validation)"
        ;;
        
    *)
        # Generic validation
        echo "[INFO] Performing generic frontmatter validation"
        
        # Check if frontmatter is parseable YAML (basic check)
        if echo "$frontmatter" | grep -q ":"; then
            echo "[INFO] Frontmatter appears to be valid YAML"
        else
            echo "[WARN] Frontmatter may not be valid YAML (no key-value pairs found)"
        fi
        ;;
esac

# Check for common YAML syntax errors
if echo "$frontmatter" | grep -q $'\t'; then
    echo "[ERROR] Frontmatter contains tabs (YAML requires spaces)"
fi

# Validate date format if 'created' field exists
created_date=$(echo "$frontmatter" | grep -oP 'created:\s*\K\S+' || echo "")
if [ -n "$created_date" ]; then
    if [[ "$created_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "[INFO] Date format valid: $created_date"
    else
        echo "[WARN] Date format may be invalid: $created_date (expected: YYYY-MM-DD)"
    fi
fi

# Validate status field if present
status=$(echo "$frontmatter" | grep -oP 'status:\s*\K\S+' || echo "")
if [ -n "$status" ]; then
    valid_statuses=("draft" "in-progress" "review" "approved" "implemented" "archived")
    if [[ " ${valid_statuses[@]} " =~ " ${status} " ]]; then
        echo "[INFO] Status value valid: $status"
    else
        echo "[WARN] Status value non-standard: $status (common values: draft, in-progress, review, approved, implemented)"
    fi
fi

echo "[INFO] Frontmatter validation complete"
exit 0
