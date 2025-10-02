---
description: Analyze existing brownfield codebase with 4-pass workflow
scripts:
  sh: scripts/bash/analyze-codebase.sh --json
  ps: scripts/powershell/analyze-codebase.ps1 -Json
  detect_framework: scripts/bash/detect-framework.sh --json
orchestration:
  pre_conditions: ["project_exists"]
  auto_trigger: ["run-analyze-script", "web-research-validation"]
  post_conditions: ["analysis_complete", "confidence_levels_reported"]
  next: "plan"
---

# Brownfield Project Analysis Workflow

**Purpose**: Analyze existing codebase using 4-pass method (Document → Analyze → Integrate → Risk)  
**Template**: `.specify/templates/brownfield-analysis.md`  
**Research**: Based on specs/005-spec-kit-enhanced/research.md (BMAD Method)

## Workflow Execution

### Pass 1: Document System (10-15 min)

1. **Run automated analysis**:
   ```bash
   # Execute tech stack detection
   .specify/scripts/bash/analyze-codebase.sh --json > codebase-scan.json
   
   # Parse JSON output
   FRAMEWORK=$(jq -r '.framework' codebase-scan.json)
   VERSION=$(jq -r '.version' codebase-scan.json)
   CONFIDENCE=$(jq -r '.confidence' codebase-scan.json)
   ```

2. **Document findings** in brownfield-analysis.md:
   - Tech stack: $FRAMEWORK $VERSION
   - Confidence: $CONFIDENCE
   - File counts by type
   - Key dependencies

### Pass 2: Analyze Architecture (15-20 min)

1. **Detect framework**:
   ```bash
   .specify/scripts/bash/detect-framework.sh --json
   ```

2. **Research official documentation** (CRITICAL):
   - Search: "$FRAMEWORK $VERSION best practices"
   - Search: "$FRAMEWORK $VERSION folder structure"
   - Search: "$FRAMEWORK $VERSION architecture patterns"
   
3. **Use "According to..." prompting**:
   ```markdown
   According to https://nextjs.org/docs/app/building-your-application/routing,
   Next.js 15 App Router uses route groups (folder) for organization.
   
   According to https://docs.djangoproject.com/en/stable/intro/tutorial01/,
   Django projects should organize apps by domain.
   ```

4. **Report confidence levels**:
   - High (90%+): Multiple indicators + official docs validated
   - Medium (60-90%): Some indicators + partial validation
   - Low (<60%): Single indicator + no validation

### Pass 3: Design Integration (10-15 min)

1. **Identify integration points**:
   - Data migration requirements
   - API compatibility
   - Testing strategy
   - Migration phases

2. **Document in brownfield-analysis.md**:
   - Integration approach (Incremental/Big Bang/Strangler Fig)
   - Migration phases with confidence levels
   - Risk assessment

### Pass 4: Risk Assessment (10 min)

1. **Check dependencies**:
   ```bash
   # Run dependency check (if available)
   .specify/scripts/bash/check-dependencies.sh --json
   ```

2. **Identify risks**:
   - Legacy dependencies
   - Breaking changes
   - Security vulnerabilities
   - Technical debt

3. **Prioritize recommendations**:
   - Critical (High confidence + high impact)
   - High Priority (Med-high combinations)
   - Medium Priority (Lower combinations)

## Output

Create `specs/{feature-num}-brownfield-analysis/brownfield-analysis.md` with:
- ✅ 4-pass analysis complete
- ✅ Confidence levels for all findings
- ✅ Citations with "According to [URL]"
- ✅ Integration strategy
- ✅ Risk assessment
- ✅ Prioritized recommendations

## Agent Instructions

**CRITICAL**:
- Use "According to [URL]" for all research findings
- Report confidence levels (High/Med/Low) for every finding
- Conduct web research to validate framework versions
- Never guess version numbers or API details
- Mark uncertainties with "I don't know" + research plan

**Next Step**: Run `/plan` to create implementation strategy based on brownfield analysis
