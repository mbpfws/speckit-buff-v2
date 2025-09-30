#!/usr/bin/env bash

# Automated codebase analysis script
# Detects tech stack, framework, dependencies, and file counts
# Outputs JSON for agent consumption
#
# Usage: ./analyze-codebase.sh [--json] [--path /path/to/project]
#
# Based on: specs/005-spec-kit-enhanced/research.md (brownfield analysis)

set -e

# Parse arguments
JSON_MODE=true
PROJECT_PATH="."

for arg in "$@"; do
    case "$arg" in
        --json)
            JSON_MODE=true
            ;;
        --path)
            shift
            PROJECT_PATH="$1"
            ;;
        --help|-h)
            cat << 'EOF'
Usage: analyze-codebase.sh [OPTIONS]

Automated codebase analysis for brownfield projects.

OPTIONS:
  --json          Output in JSON format (default)
  --path PATH     Path to project root (default: current directory)
  --help, -h      Show this help message

OUTPUT:
  {
    "framework": "Next.js",
    "version": "15.x",
    "dependencies": {...},
    "file_counts": {...},
    "confidence": "high|medium|low"
  }
EOF
            exit 0
            ;;
    esac
done

cd "$PROJECT_PATH" || exit 1

# Detection functions
detect_javascript() {
    local confidence="low"
    local framework="Unknown"
    local version="Unknown"
    
    if [[ -f "package.json" ]]; then
        confidence="medium"
        
        # Detect Next.js
        if grep -q '"next"' package.json 2>/dev/null; then
            framework="Next.js"
            version=$(grep '"next"' package.json | sed 's/.*"next": "\^*\([0-9.]*\)".*/\1/')
            
            # Check for App Router
            if [[ -d "app" ]]; then
                framework="Next.js (App Router)"
                confidence="high"
            elif [[ -d "pages" ]]; then
                framework="Next.js (Pages Router)"
                confidence="high"
            fi
        # Detect React
        elif grep -q '"react"' package.json 2>/dev/null; then
            framework="React"
            version=$(grep '"react"' package.json | sed 's/.*"react": "\^*\([0-9.]*\)".*/\1/')
            confidence="high"
        # Detect Vue
        elif grep -q '"vue"' package.json 2>/dev/null; then
            framework="Vue.js"
            version=$(grep '"vue"' package.json | sed 's/.*"vue": "\^*\([0-9.]*\)".*/\1/')
            confidence="high"
        # Detect Angular
        elif grep -q '"@angular/core"' package.json 2>/dev/null; then
            framework="Angular"
            version=$(grep '"@angular/core"' package.json | sed 's/.*"@angular\/core": "\^*\([0-9.]*\)".*/\1/')
            confidence="high"
        fi
        
        # Check for lock file (increases confidence)
        if [[ -f "package-lock.json" ]] || [[ -f "yarn.lock" ]] || [[ -f "pnpm-lock.yaml" ]]; then
            [[ "$confidence" == "medium" ]] && confidence="high"
        fi
    fi
    
    echo "$framework|$version|$confidence"
}

detect_python() {
    local confidence="low"
    local framework="Unknown"
    local version="Unknown"
    
    if [[ -f "requirements.txt" ]] || [[ -f "pyproject.toml" ]]; then
        confidence="medium"
        
        # Detect Django
        if grep -q "Django" requirements.txt pyproject.toml 2>/dev/null; then
            framework="Django"
            version=$(grep "Django" requirements.txt pyproject.toml 2>/dev/null | sed 's/.*Django==\([0-9.]*\).*/\1/' | head -1)
            
            if [[ -f "manage.py" ]]; then
                confidence="high"
            fi
        # Detect FastAPI
        elif grep -q "fastapi" requirements.txt pyproject.toml 2>/dev/null; then
            framework="FastAPI"
            version=$(grep "fastapi" requirements.txt pyproject.toml 2>/dev/null | sed 's/.*fastapi==\([0-9.]*\).*/\1/' | head -1)
            confidence="high"
        # Detect Flask
        elif grep -q "Flask" requirements.txt pyproject.toml 2>/dev/null; then
            framework="Flask"
            version=$(grep "Flask" requirements.txt pyproject.toml 2>/dev/null | sed 's/.*Flask==\([0-9.]*\).*/\1/' | head -1)
            confidence="high"
        fi
    fi
    
    echo "$framework|$version|$confidence"
}

detect_java() {
    local confidence="low"
    local framework="Unknown"
    local version="Unknown"
    
    if [[ -f "pom.xml" ]]; then
        confidence="medium"
        
        # Detect Spring Boot
        if grep -q "spring-boot-starter" pom.xml 2>/dev/null; then
            framework="Spring Boot"
            version=$(grep "<version>" pom.xml | head -1 | sed 's/.*<version>\([0-9.]*\)<\/version>.*/\1/')
            confidence="high"
        fi
    elif [[ -f "build.gradle" ]] || [[ -f "build.gradle.kts" ]]; then
        confidence="medium"
        
        if grep -q "spring-boot" build.gradle* 2>/dev/null; then
            framework="Spring Boot"
            confidence="high"
        fi
    fi
    
    echo "$framework|$version|$confidence"
}

# Main detection logic
detected_framework="Unknown"
detected_version="Unknown"
overall_confidence="low"
tech_type="Unknown"

# Try JavaScript/TypeScript
if [[ -f "package.json" ]]; then
    tech_type="JavaScript/TypeScript"
    IFS='|' read -r detected_framework detected_version overall_confidence < <(detect_javascript)
# Try Python
elif [[ -f "requirements.txt" ]] || [[ -f "pyproject.toml" ]] || [[ -f "manage.py" ]]; then
    tech_type="Python"
    IFS='|' read -r detected_framework detected_version overall_confidence < <(detect_python)
# Try Java
elif [[ -f "pom.xml" ]] || [[ -f "build.gradle" ]]; then
    tech_type="Java"
    IFS='|' read -r detected_framework detected_version overall_confidence < <(detect_java)
# Try Ruby
elif [[ -f "Gemfile" ]]; then
    tech_type="Ruby"
    if grep -q "rails" Gemfile 2>/dev/null; then
        detected_framework="Ruby on Rails"
        detected_version=$(grep "rails" Gemfile | sed "s/.*rails.*['\"]\\([0-9.]*\\)['\"].*/\\1/")
        overall_confidence="high"
    fi
# Try Go
elif [[ -f "go.mod" ]]; then
    tech_type="Go"
    detected_framework="Go"
    detected_version=$(grep "^go " go.mod | awk '{print $2}')
    overall_confidence="high"
# Try Rust
elif [[ -f "Cargo.toml" ]]; then
    tech_type="Rust"
    detected_framework="Rust"
    overall_confidence="high"
fi

# Count files by type
count_files() {
    local ext="$1"
    find . -type f -name "*.$ext" 2>/dev/null | wc -l | tr -d ' '
}

ts_count=$(count_files "ts")
tsx_count=$(count_files "tsx")
js_count=$(count_files "js")
jsx_count=$(count_files "jsx")
py_count=$(count_files "py")
java_count=$(count_files "java")
rb_count=$(count_files "rb")
go_count=$(count_files "go")
rs_count=$(count_files "rs")

# Extract key dependencies
dependencies="{}"
if [[ -f "package.json" ]]; then
    dependencies=$(grep -A 50 '"dependencies"' package.json | grep '"' | head -10 | sed 's/^[ \t]*//' | tr '\n' ',' | sed 's/,$//')
    dependencies="{$dependencies}"
elif [[ -f "requirements.txt" ]]; then
    dependencies=$(head -10 requirements.txt | tr '\n' ',' | sed 's/,$//')
    dependencies="{\"packages\":\"$dependencies\"}"
fi

# Output JSON
if $JSON_MODE; then
    cat << EOF
{
  "tech_type": "$tech_type",
  "framework": "$detected_framework",
  "version": "$detected_version",
  "confidence": "$overall_confidence",
  "file_counts": {
    "typescript": $ts_count,
    "tsx": $tsx_count,
    "javascript": $js_count,
    "jsx": $jsx_count,
    "python": $py_count,
    "java": $java_count,
    "ruby": $rb_count,
    "go": $go_count,
    "rust": $rs_count
  },
  "dependencies": $dependencies,
  "detected_via": "$(if [[ -f "package.json" ]]; then echo "package.json"; elif [[ -f "requirements.txt" ]]; then echo "requirements.txt"; elif [[ -f "pom.xml" ]]; then echo "pom.xml"; else echo "file patterns"; fi)"
}
EOF
else
    echo "Tech Type: $tech_type"
    echo "Framework: $detected_framework"
    echo "Version: $detected_version"
    echo "Confidence: $overall_confidence"
    echo "File Counts: TS=$ts_count, JS=$js_count, PY=$py_count"
fi
