#!/usr/bin/env pwsh

# Automated codebase analysis script (PowerShell)
# Detects tech stack, framework, dependencies, and file counts
# Outputs JSON for agent consumption
#
# Usage: ./analyze-codebase.ps1 [-Json] [-Path /path/to/project]

[CmdletBinding()]
param(
    [switch]$Json = $true,
    [string]$Path = "."
)

$ErrorActionPreference = 'Stop'

Set-Location $Path

# Detection functions
function Detect-JavaScript {
    $confidence = "low"
    $framework = "Unknown"
    $version = "Unknown"
    
    if (Test-Path "package.json") {
        $confidence = "medium"
        $packageJson = Get-Content "package.json" -Raw
        
        # Detect Next.js
        if ($packageJson -match '"next"') {
            $framework = "Next.js"
            if ($packageJson -match '"next":\s*"\^?([0-9.]+)"') {
                $version = $matches[1]
            }
            
            if (Test-Path "app") {
                $framework = "Next.js (App Router)"
                $confidence = "high"
            } elseif (Test-Path "pages") {
                $framework = "Next.js (Pages Router)"
                $confidence = "high"
            }
        }
        # Detect React
        elseif ($packageJson -match '"react"') {
            $framework = "React"
            if ($packageJson -match '"react":\s*"\^?([0-9.]+)"') {
                $version = $matches[1]
            }
            $confidence = "high"
        }
        # Detect Vue
        elseif ($packageJson -match '"vue"') {
            $framework = "Vue.js"
            if ($packageJson -match '"vue":\s*"\^?([0-9.]+)"') {
                $version = $matches[1]
            }
            $confidence = "high"
        }
        # Detect Angular
        elseif ($packageJson -match '"@angular/core"') {
            $framework = "Angular"
            if ($packageJson -match '"@angular/core":\s*"\^?([0-9.]+)"') {
                $version = $matches[1]
            }
            $confidence = "high"
        }
        
        # Check for lock file
        if ((Test-Path "package-lock.json") -or (Test-Path "yarn.lock") -or (Test-Path "pnpm-lock.yaml")) {
            if ($confidence -eq "medium") { $confidence = "high" }
        }
    }
    
    return @{
        Framework = $framework
        Version = $version
        Confidence = $confidence
    }
}

function Detect-Python {
    $confidence = "low"
    $framework = "Unknown"
    $version = "Unknown"
    
    if ((Test-Path "requirements.txt") -or (Test-Path "pyproject.toml")) {
        $confidence = "medium"
        $content = ""
        
        if (Test-Path "requirements.txt") {
            $content = Get-Content "requirements.txt" -Raw
        }
        if (Test-Path "pyproject.toml") {
            $content += Get-Content "pyproject.toml" -Raw
        }
        
        # Detect Django
        if ($content -match "Django") {
            $framework = "Django"
            if ($content -match "Django==([0-9.]+)") {
                $version = $matches[1]
            }
            if (Test-Path "manage.py") {
                $confidence = "high"
            }
        }
        # Detect FastAPI
        elseif ($content -match "fastapi") {
            $framework = "FastAPI"
            if ($content -match "fastapi==([0-9.]+)") {
                $version = $matches[1]
            }
            $confidence = "high"
        }
        # Detect Flask
        elseif ($content -match "Flask") {
            $framework = "Flask"
            if ($content -match "Flask==([0-9.]+)") {
                $version = $matches[1]
            }
            $confidence = "high"
        }
    }
    
    return @{
        Framework = $framework
        Version = $version
        Confidence = $confidence
    }
}

# Main detection
$detectedFramework = "Unknown"
$detectedVersion = "Unknown"
$overallConfidence = "low"
$techType = "Unknown"

# Try JavaScript/TypeScript
if (Test-Path "package.json") {
    $techType = "JavaScript/TypeScript"
    $result = Detect-JavaScript
    $detectedFramework = $result.Framework
    $detectedVersion = $result.Version
    $overallConfidence = $result.Confidence
}
# Try Python
elseif ((Test-Path "requirements.txt") -or (Test-Path "pyproject.toml") -or (Test-Path "manage.py")) {
    $techType = "Python"
    $result = Detect-Python
    $detectedFramework = $result.Framework
    $detectedVersion = $result.Version
    $overallConfidence = $result.Confidence
}
# Try Java
elseif ((Test-Path "pom.xml") -or (Test-Path "build.gradle")) {
    $techType = "Java"
    if (Test-Path "pom.xml") {
        $pom = Get-Content "pom.xml" -Raw
        if ($pom -match "spring-boot-starter") {
            $detectedFramework = "Spring Boot"
            $overallConfidence = "high"
        }
    }
}
# Try Ruby
elseif (Test-Path "Gemfile") {
    $techType = "Ruby"
    $gemfile = Get-Content "Gemfile" -Raw
    if ($gemfile -match "rails") {
        $detectedFramework = "Ruby on Rails"
        $overallConfidence = "high"
    }
}
# Try Go
elseif (Test-Path "go.mod") {
    $techType = "Go"
    $detectedFramework = "Go"
    $overallConfidence = "high"
}
# Try Rust
elseif (Test-Path "Cargo.toml") {
    $techType = "Rust"
    $detectedFramework = "Rust"
    $overallConfidence = "high"
}

# Count files
$tsCount = (Get-ChildItem -Recurse -Filter "*.ts" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$tsxCount = (Get-ChildItem -Recurse -Filter "*.tsx" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$jsCount = (Get-ChildItem -Recurse -Filter "*.js" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$jsxCount = (Get-ChildItem -Recurse -Filter "*.jsx" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$pyCount = (Get-ChildItem -Recurse -Filter "*.py" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$javaCount = (Get-ChildItem -Recurse -Filter "*.java" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$rbCount = (Get-ChildItem -Recurse -Filter "*.rb" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$goCount = (Get-ChildItem -Recurse -Filter "*.go" -File -ErrorAction SilentlyContinue | Measure-Object).Count
$rsCount = (Get-ChildItem -Recurse -Filter "*.rs" -File -ErrorAction SilentlyContinue | Measure-Object).Count

# Extract dependencies
$dependencies = "{}"
if (Test-Path "package.json") {
    $packageJson = Get-Content "package.json" -Raw | ConvertFrom-Json
    if ($packageJson.dependencies) {
        $deps = $packageJson.dependencies.PSObject.Properties | Select-Object -First 10 | ForEach-Object { "`"$($_.Name)`": `"$($_.Value)`"" }
        $dependencies = "{$($deps -join ', ')}"
    }
}

# Determine detected_via
$detectedVia = "file patterns"
if (Test-Path "package.json") { $detectedVia = "package.json" }
elseif (Test-Path "requirements.txt") { $detectedVia = "requirements.txt" }
elseif (Test-Path "pom.xml") { $detectedVia = "pom.xml" }

# Output JSON (matches bash output exactly)
if ($Json) {
    @"
{
  "tech_type": "$techType",
  "framework": "$detectedFramework",
  "version": "$detectedVersion",
  "confidence": "$overallConfidence",
  "file_counts": {
    "typescript": $tsCount,
    "tsx": $tsxCount,
    "javascript": $jsCount,
    "jsx": $jsxCount,
    "python": $pyCount,
    "java": $javaCount,
    "ruby": $rbCount,
    "go": $goCount,
    "rust": $rsCount
  },
  "dependencies": $dependencies,
  "detected_via": "$detectedVia"
}
"@
} else {
    Write-Output "Tech Type: $techType"
    Write-Output "Framework: $detectedFramework"
    Write-Output "Version: $detectedVersion"
    Write-Output "Confidence: $overallConfidence"
    Write-Output "File Counts: TS=$tsCount, JS=$jsCount, PY=$pyCount"
}
