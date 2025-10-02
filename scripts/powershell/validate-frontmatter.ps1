# validate-frontmatter.ps1 - Validate YAML frontmatter in markdown files
# Exit code: Always 0 (non-blocking validation)
# Output: [INFO], [WARN], [ERROR] messages

param(
    [Parameter(Mandatory=$true)]
    [string]$TargetFile
)

Write-Output "[INFO] Validating frontmatter: $TargetFile"

# Check if file exists
if (-not (Test-Path $TargetFile)) {
    Write-Output "[ERROR] File not found: $TargetFile"
    exit 0
}

# Read file content
$content = Get-Content $TargetFile -Raw

# Check if file has YAML frontmatter (starts with ---)
if ($content -notmatch '^---\s*\r?\n') {
    Write-Output "[ERROR] No YAML frontmatter found (file must start with ---)"
    exit 0
}

Write-Output "[INFO] Frontmatter delimiter found"

# Extract frontmatter (between first two --- lines)
if ($content -match '^---\s*\r?\n([\s\S]*?)\r?\n---') {
    $frontmatter = $Matches[1]
} else {
    Write-Output "[ERROR] Invalid frontmatter block (missing closing ---)"
    exit 0
}

if ([string]::IsNullOrWhiteSpace($frontmatter)) {
    Write-Output "[ERROR] Empty frontmatter block"
    exit 0
}

Write-Output "[INFO] Frontmatter content extracted"

# Detect file type from filename or path
$fileBasename = Split-Path $TargetFile -Leaf
$fileType = "unknown"

if ($fileBasename -eq "spec.md") {
    $fileType = "spec"
} elseif ($fileBasename -eq "plan.md") {
    $fileType = "plan"
} elseif ($fileBasename -eq "tasks.md") {
    $fileType = "tasks"
}

# Validate required fields based on file type
switch ($fileType) {
    "spec" {
        # Required fields for spec.md
        if ($frontmatter -match 'feature_id:') {
            Write-Output "[INFO] Required field present: feature_id"
        } else {
            Write-Output "[ERROR] Missing required field: feature_id"
        }
        
        if ($frontmatter -match 'title:') {
            Write-Output "[INFO] Required field present: title"
        } else {
            Write-Output "[WARN] Missing recommended field: title"
        }
        
        if ($frontmatter -match 'status:') {
            Write-Output "[INFO] Required field present: status"
        } else {
            Write-Output "[WARN] Missing recommended field: status"
        }
        
        if ($frontmatter -match 'created:') {
            Write-Output "[INFO] Required field present: created"
        } else {
            Write-Output "[WARN] Missing recommended field: created"
        }
        
        # Optional fields
        if ($frontmatter -match 'version:') {
            Write-Output "[INFO] Optional field present: version"
        }
    }
    
    "plan" {
        # Required fields for plan.md
        if ($frontmatter -match 'description:') {
            Write-Output "[INFO] Required field present: description"
        } else {
            Write-Output "[WARN] Missing recommended field: description"
        }
        
        if ($frontmatter -match 'version:') {
            Write-Output "[INFO] Optional field present: version"
        }
        
        if ($frontmatter -match 'scripts:') {
            Write-Output "[INFO] Optional field present: scripts"
        }
    }
    
    "tasks" {
        # Tasks.md typically has minimal frontmatter
        Write-Output "[INFO] Tasks file detected (minimal validation)"
    }
    
    default {
        # Generic validation
        Write-Output "[INFO] Performing generic frontmatter validation"
        
        # Check if frontmatter is parseable YAML (basic check)
        if ($frontmatter -match ':') {
            Write-Output "[INFO] Frontmatter appears to be valid YAML"
        } else {
            Write-Output "[WARN] Frontmatter may not be valid YAML (no key-value pairs found)"
        }
    }
}

# Check for common YAML syntax errors
if ($frontmatter -match "`t") {
    Write-Output "[ERROR] Frontmatter contains tabs (YAML requires spaces)"
}

# Validate date format if 'created' field exists
if ($frontmatter -match 'created:\s*(\S+)') {
    $createdDate = $Matches[1]
    if ($createdDate -match '^\d{4}-\d{2}-\d{2}$') {
        Write-Output "[INFO] Date format valid: $createdDate"
    } else {
        Write-Output "[WARN] Date format may be invalid: $createdDate (expected: YYYY-MM-DD)"
    }
}

# Validate status field if present
if ($frontmatter -match 'status:\s*(\S+)') {
    $status = $Matches[1]
    $validStatuses = @("draft", "in-progress", "review", "approved", "implemented", "archived")
    if ($validStatuses -contains $status) {
        Write-Output "[INFO] Status value valid: $status"
    } else {
        Write-Output "[WARN] Status value non-standard: $status (common values: draft, in-progress, review, approved, implemented)"
    }
}

Write-Output "[INFO] Frontmatter validation complete"
exit 0
