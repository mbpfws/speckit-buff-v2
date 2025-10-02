# orchestrate-workflow.ps1 - Intelligent workflow orchestration with chaining
# Exit code: Always 0 (non-blocking)
# Output: JSON with workflow execution plan and next steps

param(
    [Parameter(Mandatory=$true)]
    [string]$WorkflowName,
    
    [string]$ContextFile = ".specify/context.json"
)

# Default chaining rules
$defaultRules = @{
    specify = @{
        pre_conditions = @()
        post_conditions = @("complexity_analyzed")
        auto_trigger = @("detect-complexity")
        conditional_trigger = @{
            if = "complexity_level >= medium"
            then = "research-tech"
        }
    }
    "research-tech" = @{
        pre_conditions = @("complexity_analyzed")
        post_conditions = @("research_complete")
        max_iterations = 3
        next = "clarify"
    }
    clarify = @{
        pre_conditions = @()
        post_conditions = @("clarifications_recorded")
        min_questions = 1
        next = "plan"
    }
    plan = @{
        pre_conditions = @("clarifications_recorded")
        post_conditions = @("plan_generated")
        auto_trigger = @("research-domains")
        conditional_trigger = @{
            if = "multi_domain == true"
            then = "research-integrations"
        }
        next = "tasks"
    }
    tasks = @{
        pre_conditions = @("plan_generated")
        post_conditions = @("tasks_generated")
        next = "analyze"
    }
    analyze = @{
        pre_conditions = @("tasks_generated")
        post_conditions = @("analysis_complete")
        gatekeeper = $true
        next = "implement"
    }
    implement = @{
        pre_conditions = @("analysis_complete", "tasks_generated")
        post_conditions = @("implementation_complete")
    }
}

# Load or create rules
$chainRulesFile = ".specify/workflow-rules.json"

if (-not (Test-Path $chainRulesFile)) {
    $dir = Split-Path $chainRulesFile -Parent
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $defaultRules | ConvertTo-Json -Depth 10 | Set-Content $chainRulesFile
}

$rules = Get-Content $chainRulesFile | ConvertFrom-Json

# Load context
$context = @{}
if (Test-Path $ContextFile) {
    $context = Get-Content $ContextFile | ConvertFrom-Json
}

# Get rules for current workflow
$workflowRules = $rules.$WorkflowName
if (-not $workflowRules) {
    $workflowRules = @{}
}

# Check pre-conditions
$preConditions = $workflowRules.pre_conditions
if (-not $preConditions) { $preConditions = @() }

$failedConditions = @()
foreach ($condition in $preConditions) {
    $conditionMet = $context.$condition
    if ($conditionMet -ne $true) {
        $failedConditions += $condition
    }
}

# Determine if workflow can proceed
$canProceed = $failedConditions.Count -eq 0

# Get auto-trigger workflows
$autoTriggers = $workflowRules.auto_trigger
if (-not $autoTriggers) { $autoTriggers = @() }

# Get conditional triggers
$conditionalTrigger = $workflowRules.conditional_trigger

# Evaluate conditional trigger
$shouldTriggerConditional = $false
if ($conditionalTrigger) {
    $condition = $conditionalTrigger.if
    
    if ($condition -match "complexity_level >= medium") {
        $complexity = $context.complexity_level
        if ($complexity -eq "medium" -or $complexity -eq "high") {
            $shouldTriggerConditional = $true
        }
    } elseif ($condition -match "multi_domain == true") {
        $multiDomain = $context.multi_domain
        if ($multiDomain -eq $true) {
            $shouldTriggerConditional = $true
        }
    }
}

# Get next workflow
$nextWorkflow = $workflowRules.next

# Build execution plan
$executionPlan = @()

# Add auto-triggers
foreach ($trigger in $autoTriggers) {
    $executionPlan += @{
        workflow = $trigger
        type = "auto"
    }
}

# Add conditional trigger
if ($shouldTriggerConditional -and $conditionalTrigger.then) {
    $executionPlan += @{
        workflow = $conditionalTrigger.then
        type = "conditional"
    }
}

# Add next workflow
if ($nextWorkflow) {
    $executionPlan += @{
        workflow = $nextWorkflow
        type = "next"
    }
}

# Check if workflow is a gatekeeper
$isGatekeeper = $workflowRules.gatekeeper -eq $true

# Output orchestration result
$result = @{
    workflow = $WorkflowName
    can_proceed = $canProceed
    failed_conditions = $failedConditions
    execution_plan = $executionPlan
    is_gatekeeper = $isGatekeeper
    context = $context
}

Write-Output ($result | ConvertTo-Json -Depth 10 -Compress)
exit 0
