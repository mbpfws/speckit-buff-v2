#!/bin/bash
# detect-complexity.sh - Analyze feature description for technological complexity
# Exit code: Always 0 (non-blocking)
# Output: JSON with complexity metrics and recommendations

set -e

# Parse command line options
JSON_OUTPUT=false
if [ "$1" = "--json" ]; then
    JSON_OUTPUT=true
    shift
fi

# Feature description from argument or stdin
if [ -n "$1" ]; then
    FEATURE_DESC="$1"
else
    FEATURE_DESC="$(cat)"
fi

if [ -z "$FEATURE_DESC" ]; then
    echo '{"error": "No feature description provided", "complexity_level": "unknown"}'
    exit 0
fi

# Initialize complexity metrics
TECH_STACK_COUNT=0
INTEGRATION_COUNT=0
ARCHITECTURE_COUNT=0
COMPLEXITY_KEYWORDS=0
RESEARCH_NEEDED=false
MULTI_DOMAIN=false

# Technology stack indicators (databases, frameworks, APIs, etc.)
TECH_PATTERNS=(
    "database|postgres|mysql|mongodb|redis|elasticsearch"
    "api|rest|graphql|grpc|websocket"
    "framework|react|vue|angular|django|flask|spring|express"
    "cloud|aws|azure|gcp|kubernetes|docker"
    "auth|oauth|jwt|saml|ldap"
    "queue|kafka|rabbitmq|sqs|pubsub"
    "cache|memcached|redis"
    "search|elasticsearch|solr|algolia"
)

# Integration complexity indicators
INTEGRATION_PATTERNS=(
    "integrate|integration|connect|sync"
    "third[- ]party|external|vendor"
    "payment|stripe|paypal"
    "email|sendgrid|mailgun"
    "sms|twilio"
    "analytics|tracking|metrics"
)

# Architecture complexity indicators
ARCHITECTURE_PATTERNS=(
    "microservice|distributed|scalable"
    "real[- ]time|streaming|event[- ]driven"
    "multi[- ]tenant|multi[- ]region"
    "high[- ]availability|fault[- ]tolerant"
    "serverless|lambda"
)

# Complexity keywords
COMPLEXITY_KEYWORDS_LIST=(
    "complex|complicated|sophisticated"
    "enterprise|large[- ]scale|production"
    "performance|optimization|scalability"
    "security|compliance|audit"
    "migration|refactor|legacy"
)

# Count matches
for pattern in "${TECH_PATTERNS[@]}"; do
    if echo "$FEATURE_DESC" | grep -iEq "$pattern"; then
        ((TECH_STACK_COUNT++))
    fi
done

for pattern in "${INTEGRATION_PATTERNS[@]}"; do
    if echo "$FEATURE_DESC" | grep -iEq "$pattern"; then
        ((INTEGRATION_COUNT++))
    fi
done

for pattern in "${ARCHITECTURE_PATTERNS[@]}"; do
    if echo "$FEATURE_DESC" | grep -iEq "$pattern"; then
        ((ARCHITECTURE_COUNT++))
    fi
done

for pattern in "${COMPLEXITY_KEYWORDS_LIST[@]}"; do
    if echo "$FEATURE_DESC" | grep -iEq "$pattern"; then
        ((COMPLEXITY_KEYWORDS++))
    fi
done

# Determine complexity level
TOTAL_SCORE=$((TECH_STACK_COUNT * 2 + INTEGRATION_COUNT * 3 + ARCHITECTURE_COUNT * 4 + COMPLEXITY_KEYWORDS))

if [ "$TOTAL_SCORE" -ge 10 ]; then
    COMPLEXITY_LEVEL="high"
    RESEARCH_NEEDED=true
    MULTI_DOMAIN=true
elif [ "$TOTAL_SCORE" -ge 5 ]; then
    COMPLEXITY_LEVEL="medium"
    RESEARCH_NEEDED=true
elif [ "$TOTAL_SCORE" -ge 2 ]; then
    COMPLEXITY_LEVEL="low-medium"
    RESEARCH_NEEDED=false
else
    COMPLEXITY_LEVEL="low"
    RESEARCH_NEEDED=false
fi

# Check for multi-domain indicators
if [ "$TECH_STACK_COUNT" -ge 3 ] || [ "$INTEGRATION_COUNT" -ge 2 ]; then
    MULTI_DOMAIN=true
fi

# Generate research recommendations
RESEARCH_TOPICS="[]"
if [ "$RESEARCH_NEEDED" = true ]; then
    TOPICS=()
    
    if [ "$TECH_STACK_COUNT" -gt 0 ]; then
        TOPICS+=("\"technology stack evaluation and best practices\"")
    fi
    
    if [ "$INTEGRATION_COUNT" -gt 0 ]; then
        TOPICS+=("\"third-party integration patterns and SDKs\"")
    fi
    
    if [ "$ARCHITECTURE_COUNT" -gt 0 ]; then
        TOPICS+=("\"architecture patterns and scalability strategies\"")
    fi
    
    if [ "${#TOPICS[@]}" -gt 0 ]; then
        RESEARCH_TOPICS="[$(IFS=,; echo "${TOPICS[*]}")]"
    fi
fi

# Determine next workflow
NEXT_WORKFLOW="clarify"
if [ "$RESEARCH_NEEDED" = true ]; then
    NEXT_WORKFLOW="research-tech"
fi

# Output JSON
cat <<EOF
{
  "complexity_level": "$COMPLEXITY_LEVEL",
  "complexity_score": $TOTAL_SCORE,
  "metrics": {
    "tech_stack_indicators": $TECH_STACK_COUNT,
    "integration_indicators": $INTEGRATION_COUNT,
    "architecture_indicators": $ARCHITECTURE_COUNT,
    "complexity_keywords": $COMPLEXITY_KEYWORDS
  },
  "flags": {
    "research_needed": $RESEARCH_NEEDED,
    "multi_domain": $MULTI_DOMAIN
  },
  "recommendations": {
    "next_workflow": "$NEXT_WORKFLOW",
    "research_topics": $RESEARCH_TOPICS,
    "estimated_research_passes": $((TOTAL_SCORE / 5 + 1))
  }
}
EOF

exit 0
