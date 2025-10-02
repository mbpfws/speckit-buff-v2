#!/bin/bash
# orchestrate-workflow.sh - Intelligent workflow orchestration with chaining
# Exit code: Always 0 (non-blocking)
# Output: JSON with workflow execution plan and next steps

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source common functions
if [ -f "$SCRIPT_DIR/common.sh" ]; then
    source "$SCRIPT_DIR/common.sh"
fi

# Arguments
WORKFLOW_NAME="${1}"
CONTEXT_FILE="${2:-.specify/context.json}"

if [ -z "$WORKFLOW_NAME" ]; then
    echo '{"error": "No workflow name provided"}'
    exit 0
fi

# Load workflow chaining rules
CHAIN_RULES_FILE=".specify/workflow-rules.json"

# Default chaining rules
DEFAULT_RULES='{
  "specify": {
    "pre_conditions": [],
    "post_conditions": ["complexity_analyzed"],
    "auto_trigger": ["detect-complexity"],
    "conditional_trigger": {
      "if": "complexity_level >= medium",
      "then": "research-tech"
    }
  },
  "research-tech": {
    "pre_conditions": ["complexity_analyzed"],
    "post_conditions": ["research_complete"],
    "max_iterations": 3,
    "next": "clarify"
  },
  "clarify": {
    "pre_conditions": [],
    "post_conditions": ["clarifications_recorded"],
    "min_questions": 1,
    "next": "plan"
  },
  "plan": {
    "pre_conditions": ["clarifications_recorded"],
    "post_conditions": ["plan_generated"],
    "auto_trigger": ["research-domains"],
    "conditional_trigger": {
      "if": "multi_domain == true",
      "then": "research-integrations"
    },
    "next": "tasks"
  },
  "tasks": {
    "pre_conditions": ["plan_generated"],
    "post_conditions": ["tasks_generated"],
    "next": "analyze"
  },
  "analyze": {
    "pre_conditions": ["tasks_generated"],
    "post_conditions": ["analysis_complete"],
    "gatekeeper": true,
    "next": "implement"
  },
  "implement": {
    "pre_conditions": ["analysis_complete", "tasks_generated"],
    "post_conditions": ["implementation_complete"]
  }
}'

# Load or create rules
if [ ! -f "$CHAIN_RULES_FILE" ]; then
    mkdir -p "$(dirname "$CHAIN_RULES_FILE")"
    echo "$DEFAULT_RULES" > "$CHAIN_RULES_FILE"
fi

RULES=$(cat "$CHAIN_RULES_FILE")

# Load context
CONTEXT="{}"
if [ -f "$CONTEXT_FILE" ]; then
    CONTEXT=$(cat "$CONTEXT_FILE")
fi

# Get rules for current workflow
WORKFLOW_RULES=$(echo "$RULES" | jq -r ".[\"$WORKFLOW_NAME\"] // {}")

# Check pre-conditions
PRE_CONDITIONS=$(echo "$WORKFLOW_RULES" | jq -r '.pre_conditions // []')
FAILED_CONDITIONS=()

if [ "$PRE_CONDITIONS" != "[]" ]; then
    while IFS= read -r condition; do
        # Check if condition is met in context
        CONDITION_MET=$(echo "$CONTEXT" | jq -r ".$condition // false")
        if [ "$CONDITION_MET" != "true" ]; then
            FAILED_CONDITIONS+=("$condition")
        fi
    done < <(echo "$PRE_CONDITIONS" | jq -r '.[]')
fi

# Determine if workflow can proceed
CAN_PROCEED=true
if [ "${#FAILED_CONDITIONS[@]}" -gt 0 ]; then
    CAN_PROCEED=false
fi

# Get auto-trigger workflows
AUTO_TRIGGERS=$(echo "$WORKFLOW_RULES" | jq -r '.auto_trigger // []')

# Get conditional triggers
CONDITIONAL_TRIGGER=$(echo "$WORKFLOW_RULES" | jq -r '.conditional_trigger // {}')

# Evaluate conditional trigger
SHOULD_TRIGGER_CONDITIONAL=false
if [ "$CONDITIONAL_TRIGGER" != "{}" ]; then
    CONDITION=$(echo "$CONDITIONAL_TRIGGER" | jq -r '.if // ""')
    
    # Simple condition evaluation (extend as needed)
    if [[ "$CONDITION" == *"complexity_level >= medium"* ]]; then
        COMPLEXITY=$(echo "$CONTEXT" | jq -r '.complexity_level // "low"')
        if [ "$COMPLEXITY" = "medium" ] || [ "$COMPLEXITY" = "high" ]; then
            SHOULD_TRIGGER_CONDITIONAL=true
        fi
    elif [[ "$CONDITION" == *"multi_domain == true"* ]]; then
        MULTI_DOMAIN=$(echo "$CONTEXT" | jq -r '.multi_domain // false')
        if [ "$MULTI_DOMAIN" = "true" ]; then
            SHOULD_TRIGGER_CONDITIONAL=true
        fi
    fi
fi

# Get next workflow
NEXT_WORKFLOW=$(echo "$WORKFLOW_RULES" | jq -r '.next // ""')

# Build execution plan
EXECUTION_PLAN="[]"

# Add auto-triggers
if [ "$AUTO_TRIGGERS" != "[]" ]; then
    EXECUTION_PLAN=$(echo "$AUTO_TRIGGERS" | jq -c '[.[] | {workflow: ., type: "auto"}]')
fi

# Add conditional trigger
if [ "$SHOULD_TRIGGER_CONDITIONAL" = true ]; then
    TRIGGERED_WORKFLOW=$(echo "$CONDITIONAL_TRIGGER" | jq -r '.then // ""')
    if [ -n "$TRIGGERED_WORKFLOW" ]; then
        EXECUTION_PLAN=$(echo "$EXECUTION_PLAN" | jq -c ". + [{workflow: \"$TRIGGERED_WORKFLOW\", type: \"conditional\"}]")
    fi
fi

# Add next workflow
if [ -n "$NEXT_WORKFLOW" ]; then
    EXECUTION_PLAN=$(echo "$EXECUTION_PLAN" | jq -c ". + [{workflow: \"$NEXT_WORKFLOW\", type: \"next\"}]")
fi

# Check if workflow is a gatekeeper
IS_GATEKEEPER=$(echo "$WORKFLOW_RULES" | jq -r '.gatekeeper // false')

# Output orchestration result
cat <<EOF
{
  "workflow": "$WORKFLOW_NAME",
  "can_proceed": $CAN_PROCEED,
  "failed_conditions": $(printf '%s\n' "${FAILED_CONDITIONS[@]}" | jq -R . | jq -s .),
  "execution_plan": $EXECUTION_PLAN,
  "is_gatekeeper": $IS_GATEKEEPER,
  "context": $CONTEXT
}
EOF

exit 0
