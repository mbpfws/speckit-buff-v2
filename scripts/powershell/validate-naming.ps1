# validate-naming.ps1 - Validate file and folder naming conventions
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

param(
    [string]$TargetDir = "."
)

Write-Output "[INFO] Validating naming conventions: $TargetDir"

# Check if target exists
if (-not (Test-Path $TargetDir -PathType Container)) {
    Write-Output "[ERROR] Directory not found: $TargetDir"
    exit 0
}

# Validate feature folder naming
if ($TargetDir -match 'specs[/\\]([0-9]{3,}-[a-z0-9-]+)$') {
    $featureName = Split-Path $TargetDir -Leaf
    
    # Check format: ###-kebab-case
    if ($featureName -match '^[0-9]{3,}-[a-z0-9-]+$') {
        Write-Output "[INFO] Feature folder naming: PASS ($featureName)"
    } else {
        Write-Output "[ERROR] Feature folder naming: FAIL ($featureName)"
        Write-Output "[ERROR] Expected format: ###-kebab-case (e.g., 001-user-authentication)"
    }
    
    # Extract feature ID from folder name
    $featureId = ($featureName -split '-')[0]
    
    # Check artifact files
    $mdFiles = Get-ChildItem -Path $TargetDir -Filter "*.md" -ErrorAction SilentlyContinue
    foreach ($file in $mdFiles) {
        $filename = $file.Name
        
        # Check for kebab-case (or spec.md, plan.md, tasks.md standard names)
        if ($filename -match '^[a-z0-9-]+\.md$') {
            Write-Output "[INFO] File naming valid: $filename"
        } else {
            Write-Output "[ERROR] File naming invalid: $filename (use kebab-case)"
        }
        
        # Check for spaces in filename
        if ($filename -match '\s') {
            Write-Output "[ERROR] File contains spaces: $filename (replace with hyphens)"
        }
    }
    
    # Check for YAML frontmatter feature_id consistency
    $specFile = Join-Path $TargetDir "spec.md"
    if (Test-Path $specFile) {
        # Extract feature_id from frontmatter
        $content = Get-Content $specFile -Raw
        if ($content -match '---\s*([\s\S]*?)\s*---') {
            $frontmatter = $Matches[1]
            if ($frontmatter -match 'feature_id:\s*(\d+)') {
                $frontmatterId = $Matches[1]
                
                if ($frontmatterId -eq $featureId) {
                    Write-Output "[INFO] Feature ID consistency: PASS (folder: $featureId, spec: $frontmatterId)"
                } else {
                    Write-Output "[ERROR] Feature ID mismatch: folder=$featureId, spec=$frontmatterId"
                }
            } else {
                Write-Output "[WARN] No feature_id found in spec.md frontmatter"
            }
        }
    }
} else {
    # Validate all feature folders in specs/
    if (Test-Path "specs" -PathType Container) {
        $featureDirs = Get-ChildItem -Path "specs" -Directory -ErrorAction SilentlyContinue
        foreach ($featureDir in $featureDirs) {
            $featureName = $featureDir.Name
            
            if ($featureName -match '^[0-9]{3,}-[a-z0-9-]+$') {
                Write-Output "[INFO] Feature folder valid: $featureName"
            } else {
                Write-Output "[ERROR] Feature folder invalid: $featureName (expected: ###-kebab-case)"
            }
        }
    }
}

Write-Output "[INFO] Naming validation complete"
exit 0
