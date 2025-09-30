# validate-structure.ps1 - Validate directory structure
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

param(
    [string]$TargetDir = "."
)

Write-Output "[INFO] Validating structure: $TargetDir"

# Check if target exists
if (-not (Test-Path $TargetDir -PathType Container)) {
    Write-Output "[ERROR] Directory not found: $TargetDir"
    exit 0
}

# Check for .specify/ directory (if in project root)
if (Test-Path ".specify" -PathType Container) {
    Write-Output "[INFO] Found .specify/ directory"
    
    # Check for required subdirectories
    if (-not (Test-Path ".specify/templates" -PathType Container)) {
        Write-Output "[ERROR] Missing .specify/templates/ directory"
    } else {
        Write-Output "[INFO] Templates directory present"
    }
    
    if (-not (Test-Path ".specify/scripts" -PathType Container)) {
        Write-Output "[ERROR] Missing .specify/scripts/ directory"
    } else {
        Write-Output "[INFO] Scripts directory present"
    }
    
    if (-not (Test-Path ".specify/memory" -PathType Container)) {
        Write-Output "[WARN] Missing .specify/memory/ directory (optional)"
    } else {
        Write-Output "[INFO] Memory directory present"
    }
    
    # Check for config file
    if (-not (Test-Path ".specify/config.yaml")) {
        Write-Output "[WARN] Missing .specify/config.yaml (optional)"
    } else {
        Write-Output "[INFO] Configuration file present"
    }
}

# Check for specs/ directory
if (Test-Path "specs" -PathType Container) {
    Write-Output "[INFO] Found specs/ directory"
    
    # Validate feature folders
    $featureDirs = Get-ChildItem -Path "specs" -Directory -ErrorAction SilentlyContinue
    foreach ($featureDir in $featureDirs) {
        $featureName = $featureDir.Name
        
        # Check folder naming convention: {id}-{slug}
        if ($featureName -notmatch '^[0-9]{3,}-[a-z0-9-]+$') {
            Write-Output "[ERROR] Invalid folder naming: $featureName (expected: ###-kebab-case)"
        } else {
            Write-Output "[INFO] Feature folder naming valid: $featureName"
        }
        
        # Check for spec.md
        if (-not (Test-Path "$($featureDir.FullName)/spec.md")) {
            Write-Output "[ERROR] Missing spec.md in $featureName"
        }
    }
} else {
    Write-Output "[WARN] No specs/ directory found"
}

# Check if validating a specific feature directory
if ($TargetDir -match 'specs[/\\][0-9]{3,}-') {
    $featureName = Split-Path $TargetDir -Leaf
    Write-Output "[INFO] Validating feature directory: $featureName"
    
    # Check for required files
    if (-not (Test-Path "$TargetDir/spec.md")) {
        Write-Output "[ERROR] Required file missing: spec.md"
    } else {
        Write-Output "[INFO] spec.md present"
    }
    
    # Check for optional artifacts
    if (Test-Path "$TargetDir/plan.md") {
        Write-Output "[INFO] plan.md present"
    }
    
    if (Test-Path "$TargetDir/tasks.md") {
        Write-Output "[INFO] tasks.md present"
    }
    
    if (Test-Path "$TargetDir/contracts" -PathType Container) {
        Write-Output "[INFO] contracts/ directory present"
    }
}

Write-Output "[INFO] Structure validation complete"
exit 0
