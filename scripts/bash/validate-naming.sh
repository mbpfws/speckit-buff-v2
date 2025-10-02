#!/bin/bash
# validate-naming.sh - Validate file and folder naming conventions
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

set -e

# Target directory (default: current directory)
TARGET_DIR="${1:-.}"

echo "[INFO] Validating naming conventions: $TARGET_DIR"

# Check if target exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "[ERROR] Directory not found: $TARGET_DIR"
    exit 0
fi

# Validate feature folder naming
if [[ "$TARGET_DIR" =~ specs/([0-9]{3,}-[a-z0-9-]+)$ ]]; then
    feature_name=$(basename "$TARGET_DIR")
    
    # Check format: ###-kebab-case
    if [[ "$feature_name" =~ ^[0-9]{3,}-[a-z0-9-]+$ ]]; then
        echo "[INFO] Feature folder naming: PASS ($feature_name)"
    else
        echo "[ERROR] Feature folder naming: FAIL ($feature_name)"
        echo "[ERROR] Expected format: ###-kebab-case (e.g., 001-user-authentication)"
    fi
    
    # Extract feature ID from folder name
    feature_id=$(echo "$feature_name" | grep -oP '^\d+')
    
    # Check artifact files
    for file in "$TARGET_DIR"/*.md; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            
            # Check for kebab-case (or spec.md, plan.md, tasks.md standard names)
            if [[ "$filename" =~ ^[a-z0-9-]+\.md$ ]]; then
                echo "[INFO] File naming valid: $filename"
            else
                echo "[ERROR] File naming invalid: $filename (use kebab-case)"
            fi
            
            # Check for spaces in filename
            if [[ "$filename" =~ \  ]]; then
                echo "[ERROR] File contains spaces: $filename (replace with hyphens)"
            fi
        fi
    done
    
    # Check for YAML frontmatter feature_id consistency
    if [ -f "$TARGET_DIR/spec.md" ]; then
        # Extract feature_id from frontmatter
        frontmatter_id=$(awk '/^---$/,/^---$/{if(!/^---$/){print}}' "$TARGET_DIR/spec.md" | grep -oP 'feature_id:\s*\K\d+' || echo "")
        
        if [ -n "$frontmatter_id" ]; then
            if [ "$frontmatter_id" = "$feature_id" ]; then
                echo "[INFO] Feature ID consistency: PASS (folder: $feature_id, spec: $frontmatter_id)"
            else
                echo "[ERROR] Feature ID mismatch: folder=$feature_id, spec=$frontmatter_id"
            fi
        else
            echo "[WARN] No feature_id found in spec.md frontmatter"
        fi
    fi
else
    # Validate all feature folders in specs/
    if [ -d "specs" ]; then
        for feature_dir in specs/*/; do
            if [ -d "$feature_dir" ]; then
                feature_name=$(basename "$feature_dir")
                
                if [[ "$feature_name" =~ ^[0-9]{3,}-[a-z0-9-]+$ ]]; then
                    echo "[INFO] Feature folder valid: $feature_name"
                else
                    echo "[ERROR] Feature folder invalid: $feature_name (expected: ###-kebab-case)"
                fi
            fi
        done
    fi
fi

echo "[INFO] Naming validation complete"
exit 0
