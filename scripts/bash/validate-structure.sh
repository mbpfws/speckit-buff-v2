#!/bin/bash
# validate-structure.sh - Validate directory structure
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source common functions if available
if [ -f "$SCRIPT_DIR/common.sh" ]; then
    source "$SCRIPT_DIR/common.sh"
fi

# Target directory (default: current directory)
TARGET_DIR="${1:-.}"

echo "[INFO] Validating structure: $TARGET_DIR"

# Check if target exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "[ERROR] Directory not found: $TARGET_DIR"
    exit 0
fi

# Check for .specify/ directory (if in project root)
if [ -d ".specify" ]; then
    echo "[INFO] Found .specify/ directory"
    
    # Check for required subdirectories
    if [ ! -d ".specify/templates" ]; then
        echo "[ERROR] Missing .specify/templates/ directory"
    else
        echo "[INFO] Templates directory present"
    fi
    
    if [ ! -d ".specify/scripts" ]; then
        echo "[ERROR] Missing .specify/scripts/ directory"
    else
        echo "[INFO] Scripts directory present"
    fi
    
    if [ ! -d ".specify/memory" ]; then
        echo "[WARN] Missing .specify/memory/ directory (optional)"
    else
        echo "[INFO] Memory directory present"
    fi
    
    # Check for config file
    if [ ! -f ".specify/config.yaml" ]; then
        echo "[WARN] Missing .specify/config.yaml (optional)"
    else
        echo "[INFO] Configuration file present"
    fi
fi

# Check for specs/ directory
if [ -d "specs" ]; then
    echo "[INFO] Found specs/ directory"
    
    # Validate feature folders
    for feature_dir in specs/*/; do
        if [ -d "$feature_dir" ]; then
            feature_name=$(basename "$feature_dir")
            
            # Check folder naming convention: {id}-{slug}
            if [[ ! "$feature_name" =~ ^[0-9]{3,}-[a-z0-9-]+$ ]]; then
                echo "[ERROR] Invalid folder naming: $feature_name (expected: ###-kebab-case)"
            else
                echo "[INFO] Feature folder naming valid: $feature_name"
            fi
            
            # Check for spec.md
            if [ ! -f "$feature_dir/spec.md" ]; then
                echo "[ERROR] Missing spec.md in $feature_name"
            fi
        fi
    done
else
    echo "[WARN] No specs/ directory found"
fi

# Check if validating a specific feature directory
if [[ "$TARGET_DIR" =~ specs/[0-9]{3,}- ]]; then
    feature_name=$(basename "$TARGET_DIR")
    echo "[INFO] Validating feature directory: $feature_name"
    
    # Check for required files
    if [ ! -f "$TARGET_DIR/spec.md" ]; then
        echo "[ERROR] Required file missing: spec.md"
    else
        echo "[INFO] spec.md present"
    fi
    
    # Check for optional artifacts
    if [ -f "$TARGET_DIR/plan.md" ]; then
        echo "[INFO] plan.md present"
    fi
    
    if [ -f "$TARGET_DIR/tasks.md" ]; then
        echo "[INFO] tasks.md present"
    fi
    
    if [ -d "$TARGET_DIR/contracts" ]; then
        echo "[INFO] contracts/ directory present"
    fi
fi

echo "[INFO] Structure validation complete"
exit 0
