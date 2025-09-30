# detect-complexity.ps1 - Analyze feature description for technological complexity
# Exit code: Always 0 (non-blocking)
# Output: JSON with complexity metrics and recommendations

param(
    [Parameter(ValueFromPipeline=$true)]
    [string]$FeatureDesc
)

if ([string]::IsNullOrWhiteSpace($FeatureDesc)) {
    Write-Output '{"error": "No feature description provided", "complexity_level": "unknown"}'
    exit 0
}

# Initialize complexity metrics
$techStackCount = 0
$integrationCount = 0
$architectureCount = 0
$complexityKeywords = 0
$researchNeeded = $false
$multiDomain = $false

# Technology stack indicators
$techPatterns = @(
    "database|postgres|mysql|mongodb|redis|elasticsearch",
    "api|rest|graphql|grpc|websocket",
    "framework|react|vue|angular|django|flask|spring|express",
    "cloud|aws|azure|gcp|kubernetes|docker",
    "auth|oauth|jwt|saml|ldap",
    "queue|kafka|rabbitmq|sqs|pubsub",
    "cache|memcached|redis",
    "search|elasticsearch|solr|algolia"
)

# Integration complexity indicators
$integrationPatterns = @(
    "integrate|integration|connect|sync",
    "third[- ]party|external|vendor",
    "payment|stripe|paypal",
    "email|sendgrid|mailgun",
    "sms|twilio",
    "analytics|tracking|metrics"
)

# Architecture complexity indicators
$architecturePatterns = @(
    "microservice|distributed|scalable",
    "real[- ]time|streaming|event[- ]driven",
    "multi[- ]tenant|multi[- ]region",
    "high[- ]availability|fault[- ]tolerant",
    "serverless|lambda"
)

# Complexity keywords
$complexityKeywordsList = @(
    "complex|complicated|sophisticated",
    "enterprise|large[- ]scale|production",
    "performance|optimization|scalability",
    "security|compliance|audit",
    "migration|refactor|legacy"
)

# Count matches
foreach ($pattern in $techPatterns) {
    if ($FeatureDesc -match $pattern) {
        $techStackCount++
    }
}

foreach ($pattern in $integrationPatterns) {
    if ($FeatureDesc -match $pattern) {
        $integrationCount++
    }
}

foreach ($pattern in $architecturePatterns) {
    if ($FeatureDesc -match $pattern) {
        $architectureCount++
    }
}

foreach ($pattern in $complexityKeywordsList) {
    if ($FeatureDesc -match $pattern) {
        $complexityKeywords++
    }
}

# Determine complexity level
$totalScore = ($techStackCount * 2) + ($integrationCount * 3) + ($architectureCount * 4) + $complexityKeywords

if ($totalScore -ge 10) {
    $complexityLevel = "high"
    $researchNeeded = $true
    $multiDomain = $true
} elseif ($totalScore -ge 5) {
    $complexityLevel = "medium"
    $researchNeeded = $true
} elseif ($totalScore -ge 2) {
    $complexityLevel = "low-medium"
    $researchNeeded = $false
} else {
    $complexityLevel = "low"
    $researchNeeded = $false
}

# Check for multi-domain indicators
if ($techStackCount -ge 3 -or $integrationCount -ge 2) {
    $multiDomain = $true
}

# Generate research recommendations
$researchTopics = @()

if ($researchNeeded) {
    if ($techStackCount -gt 0) {
        $researchTopics += "technology stack evaluation and best practices"
    }
    
    if ($integrationCount -gt 0) {
        $researchTopics += "third-party integration patterns and SDKs"
    }
    
    if ($architectureCount -gt 0) {
        $researchTopics += "architecture patterns and scalability strategies"
    }
}

# Determine next workflow
$nextWorkflow = "clarify"
if ($researchNeeded) {
    $nextWorkflow = "research-tech"
}

# Output JSON
$result = @{
    complexity_level = $complexityLevel
    complexity_score = $totalScore
    metrics = @{
        tech_stack_indicators = $techStackCount
        integration_indicators = $integrationCount
        architecture_indicators = $architectureCount
        complexity_keywords = $complexityKeywords
    }
    flags = @{
        research_needed = $researchNeeded
        multi_domain = $multiDomain
    }
    recommendations = @{
        next_workflow = $nextWorkflow
        research_topics = $researchTopics
        estimated_research_passes = [math]::Floor($totalScore / 5) + 1
    }
}

Write-Output ($result | ConvertTo-Json -Compress)
exit 0
