---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
architecture_research: true  # NEW in v2.0: Uses architecture-meta-template.md
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
  detect_framework: scripts/bash/detect-framework.sh --json  # NEW in v2.0
orchestration:
  pre_conditions: ["clarifications_recorded"]
  auto_trigger: ["research-domains", "detect-framework"]  # NEW: detect-framework
  conditional_chains:
    - condition: "multi_domain == true"
      workflow: "research-integrations"
      reason: "Multi-domain architecture requires integration research"
    - condition: "framework_detected == true"  # NEW in v2.0
      action: "research_official_docs"
      reason: "Framework detected, research latest patterns from official docs"
  post_conditions: ["plan_generated", "architecture_researched"]  # NEW: architecture_researched
  next: "tasks"
---

The user input to you can be provided directly by the agent or as a command argument - you **MUST** consider it before proceeding with the prompt (if not empty).

User input:

$ARGUMENTS

## Workflow Execution

### Phase 0: Pre-Conditions & Context Loading

1. **GATEKEEPER CHECK**: Run `{SCRIPT}` from the repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. All future file paths must be absolute.

2. **Verify clarifications exist**: 
   - Inspect FEATURE_SPEC for a `## Clarifications` section with at least one `Session` subheading
   - **IF MISSING**: PAUSE and instruct the user to run `/clarify` first to reduce rework
   - **IF EXISTS OR USER OVERRIDE**: Continue
   - Do not attempt to fabricate clarifications yourself

3. **Load context** from `.specify/context.json`:
   - `complexity_level`: Determines research depth
   - `multi_domain`: Triggers additional research
   - `research_complete`: Whether tech research was done
   - `technology_recommendations`: Stack from research

4. **Check for existing research**:
   - IF `research.md` exists in SPECS_DIR: Load and use findings
   - ELSE IF `complexity_level >= medium`: Consider running `/research-tech` first

### Phase 1: Domain & Architecture Research (AUTO-TRIGGERED)

**Objective**: Deep-dive into domain-specific patterns and architectural considerations

1. **Analyze spec for domain indicators**:
   ```bash
   # Identify domains (e.g., e-commerce, real-time, data processing)
   # Extract key architectural concerns
   ```

2. **Use web search** to research:
   - Domain-specific architecture patterns
   - Framework-specific folder structures
   - Testing strategies for this domain
   - Common pitfalls and best practices

3. **Example searches**:
   ```
   "[domain] architecture best practices 2025"
   "[framework] project structure [domain]"
   "[domain] scalability patterns production"
   "[technology] [domain] testing strategy"
   ```

4. **Document findings** in `research.md` (append if exists):
   ```markdown
   ## Domain Architecture Research
   
   ### Domain: [Domain Name]
   - **Recommended Pattern**: [Pattern]
   - **Folder Structure**: [Structure]
   - **Key Components**:
     - [Component 1]
   - **Testing Strategy**: [Strategy]
   ```

### Phase 2: Multi-Domain Integration Research (CONDITIONAL)

**TRIGGERED IF**: `multi_domain == true` in context

**Objective**: Research how multiple domains/services interact

1. **Identify domain boundaries**:
   - Which features belong to which domains?
   - What are the integration points?
   - How do they communicate?

2. **Use web search** for integration patterns:
   ```
   "[domain1] [domain2] integration patterns"
   "microservices communication best practices"
   "event-driven architecture [use case]"
   "API gateway patterns [framework]"
   ```

3. **Document in research.md**:
   ```markdown
   ## Multi-Domain Integration
   
   ### Domains Identified
   1. **[Domain 1]**: [Responsibility]
   2. **[Domain 2]**: [Responsibility]
   
   ### Integration Pattern: [Pattern Name]
   - **Communication**: [Sync/Async/Event-driven]
   - **Data Consistency**: [Approach]
   - **Error Handling**: [Strategy]
   - **Reference**: [URL]
   ```

4. **Update context**:
   ```json
   {
     "integration_research_complete": true,
     "integration_pattern": "<pattern>",
     "domain_boundaries": ["domain1", "domain2"]
   }
   ```

### Phase 3: Read & Analyze Specification

1. Read and analyze the feature specification:
   - Feature requirements and user stories
   - Functional and non-functional requirements
   - Success criteria and acceptance criteria
   - Technical constraints or dependencies mentioned
   - **Technology recommendations from research** (if available)

2. Read the constitution at `.specify/memory/constitution.md` to understand constitutional requirements.

3. **Cross-reference with research findings**:
   - Does the spec align with recommended patterns?
   - Are there missing considerations from research?
   - Do clarifications address technical unknowns?

### Phase 4: Execute Implementation Plan Template

1. Load `.specify/templates/plan-template.md` (already copied to IMPL_PLAN path)

2. Set Input path to FEATURE_SPEC

3. Run the Execution Flow (main) function steps 1-9:
   - The template is self-contained and executable
   - Follow error handling and gate checks as specified
   - Let the template guide artifact generation in $SPECS_DIR

4. **Enhance with research findings**:
   - **Technical Context**: Integrate research recommendations
   - **Architecture Decisions**: Reference researched patterns
   - **Technology Stack**: Use researched versions and SDKs
   - **Dependencies**: Include researched integrations
   - **Risks**: Incorporate risks from research

5. Generate artifacts in $SPECS_DIR:
   - **Phase 0**: research.md (enhanced/created)
   - **Phase 1**: 
     - data-model.md (with domain boundaries if multi-domain)
     - contracts/ (API contracts informed by research)
     - quickstart.md
     - agent-specific file (e.g., WINDSURF.md)
   - **Phase 2**: Task approach description (tasks.md created by /tasks)

6. **Incorporate user-provided details** from $ARGUMENTS into Technical Context

7. Update Progress Tracking as you complete each phase

### Phase 5: Verification & Complexity Tracking

1. Verify execution completed:
   - Check Progress Tracking shows all phases complete
   - Ensure all required artifacts were generated
   - Confirm no ERROR states in execution

2. **Track complexity metrics**:
   ```markdown
   ## Complexity Tracking
   
   ### Decisions Made
   - [Decision 1]: [Rationale + Research Reference]
   - [Decision 2]: [Rationale + Research Reference]
   
   ### Research-Driven Choices
   - **Technology**: [Choice] based on [Research Finding]
   - **Architecture**: [Pattern] based on [Case Study]
   - **Integration**: [Approach] based on [SDK Research]
   
   ### Deviations from Research
   - [If any]: [Reason for deviation]
   ```

3. **Update context**:
   ```json
   {
     "plan_generated": true,
     "architecture_pattern": "<pattern>",
     "research_applied": true
   }
   ```

### Phase 6: Completion Report

Report results with:
- Branch name
- File paths for all generated artifacts
- Complexity level
- Whether research was applied
- Number of research passes conducted
- Key architectural decisions
- Recommended next workflow: `/tasks`

**Example output**:
```
✅ Implementation plan complete

📁 Artifacts generated:
- specs/{feature}/plan.md
- specs/{feature}/research.md (3 research passes)
- specs/{feature}/data-model.md
- specs/{feature}/contracts/
- specs/{feature}/quickstart.md

🏗️ Architecture:
- Pattern: [Pattern name]
- Technology stack: [Stack from research]
- Multi-domain: [Yes/No]

🔍 Research applied:
- Domain patterns researched
- Integrations researched: [Yes/No]
- 15 sources consulted

➡️ Next workflow: /tasks
```

## Research Integration Guidelines

1. **Always prefer researched information** over assumptions
2. **Cite research sources** in architectural decisions
3. **Version-specific recommendations** from research
4. **Real-world case studies** over theoretical patterns
5. **Document trade-offs** researched for each decision
6. **Flag gaps** where research was inconclusive

## Agent Instructions

- Use **web search tools** extensively during planning
- **Do not assume** technology stack if not researched
- **Reference research.md** findings in all decisions
- If multi-domain detected, **must research integration patterns**
- Planning should take **10-20 minutes** for complex features
- **Pause for user input** on business-critical architectural choices

Use absolute paths with the repository root for all file operations to avoid path issues.
