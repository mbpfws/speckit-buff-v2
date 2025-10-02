# Workflow Execution Flow - When & How to Use Each Component

**Quick Answer**: Use workflows in order: `/specify` → `/clarify` → `/plan` → `/tasks` → `/implement`

---

## Visual Flow: Complete Development Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│ USER: "I need a new feature"                                     │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: /specify (Create Specification)                         │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/specify.md                           │
│ 2. Run create-new-feature.sh --json "feature description"       │
│ 3. Load spec-template.md                                         │
│ 4. Fill template with user input                                │
│ 5. Create specs/XXX-feature-name/spec.md                         │
│ 6. Update context.json: spec_created = true                     │
│                                                                  │
│ Output: specs/001-add-user-auth/spec.md                         │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: /clarify (Optional - Ask Questions)                     │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/clarify.md                           │
│ 2. Run check-prerequisites.sh --json --paths-only               │
│ 3. Parse JSON: FEATURE_SPEC path                                │
│ 4. Load spec.md, scan for ambiguities                           │
│ 5. Ask user 5 clarification questions (one at a time)           │
│ 6. Record answers in spec.md ## Clarifications section          │
│ 7. Update context.json: clarifications_recorded = true          │
│                                                                  │
│ Output: Updated spec.md with clarifications                     │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: /plan (Generate Implementation Plan)                    │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/plan.md                              │
│ 2. Run setup-plan.sh --json                                     │
│ 3. Parse JSON: FEATURE_SPEC, IMPL_PLAN, SPECS_DIR               │
│ 4. Load .specify/memory/constitution.md                         │
│ 5. Evaluate 7 constitutional principles                         │
│ 6. Phase 0: Research (create research.md)                       │
│ 7. Phase 1: Design (create data-model.md, contracts/)           │
│ 8. Phase 2: Describe task generation approach                   │
│ 9. Create plan.md                                                │
│ 10. Update context.json: plan_generated = true                  │
│                                                                  │
│ Output: plan.md, research.md, data-model.md, contracts/         │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: /tasks (Create Task Breakdown)                          │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/tasks.md                             │
│ 2. Run check-prerequisites.sh --json                            │
│ 3. Parse JSON: FEATURE_DIR, AVAILABLE_DOCS                      │
│ 4. Load plan.md, data-model.md, contracts/                      │
│ 5. Load tasks-template.md                                        │
│ 6. Generate ordered task list with dependencies                 │
│ 7. Mark [P] for parallel tasks                                  │
│ 8. Create tasks.md                                               │
│ 9. Update context.json: tasks_generated = true                  │
│                                                                  │
│ Output: tasks.md (T001, T002, T003...)                          │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: /implement (Execute Implementation)                     │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/implement.md                         │
│ 2. Run check-prerequisites.sh --json --require-tasks            │
│ 3. Parse JSON: FEATURE_DIR, AVAILABLE_DOCS, TASKS               │
│ 4. Load tasks.md for complete task list                         │
│ 5. Execute tasks phase-by-phase:                                │
│    - Setup → Tests → Core → Integration → Polish                │
│ 6. Follow TDD: Tests before implementation                      │
│ 7. For each completed task: Mark [x] in tasks.md                │
│ 8. Report progress after each task                              │
│                                                                  │
│ Output: Implemented code, updated tasks.md with [x] marks       │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: /analyze (Optional - Quality Check)                     │
│                                                                  │
│ Agent Action:                                                    │
│ 1. Read .windsurf/workflows/analyze.md                           │
│ 2. Run check-prerequisites.sh --json --require-tasks            │
│ 3. Load spec.md, plan.md, tasks.md                              │
│ 4. Load constitution.md                                          │
│ 5. Perform READ-ONLY analysis:                                  │
│    - Consistency between artifacts                              │
│    - Coverage of requirements                                   │
│    - Constitutional compliance                                  │
│ 6. Report findings with severity (CRITICAL, HIGH, MEDIUM, LOW)  │
│ 7. Offer remediation plan (user must approve)                   │
│                                                                  │
│ Output: Analysis report with recommendations                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## The 20 Scripts: What They Do & When They're Called

### Group 1: Feature Creation (2 scripts)

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **create-new-feature.sh/.ps1** | `/specify` workflow | Creates git branch, feature directory, initial spec.md | At start of every new feature |
| | | Returns: BRANCH_NAME, SPEC_FILE, FEATURE_DIR (JSON) | |

**Example**:
```bash
# Called by /specify workflow
.specify/scripts/bash/create-new-feature.sh --json "Add user authentication"

# Returns:
{
  "BRANCH_NAME": "001-add-user-authentication",
  "SPEC_FILE": "/path/specs/001-add-user-authentication/spec.md",
  "FEATURE_DIR": "/path/specs/001-add-user-authentication"
}
```

---

### Group 2: Prerequisite Checking (2 scripts)

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **check-prerequisites.sh/.ps1** | `/clarify`, `/tasks`, `/analyze`, `/implement` | Gets feature paths and available docs | Before any workflow that needs feature context |
| | | Returns: REPO_ROOT, BRANCH, FEATURE_DIR, FEATURE_SPEC, IMPL_PLAN, TASKS, AVAILABLE_DOCS (JSON) | Multiple times per feature |

**Flags**:
- `--json` - Output JSON format
- `--paths-only` - Only return paths, don't check file existence
- `--require-tasks` - Fail if tasks.md doesn't exist
- `--include-tasks` - Include parsed task list in output

**Example**:
```bash
# Called by /implement workflow
.specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks

# Returns:
{
  "REPO_ROOT": "/path/to/repo",
  "BRANCH": "001-add-user-authentication",
  "FEATURE_DIR": "/path/specs/001-add-user-authentication",
  "FEATURE_SPEC": "/path/specs/001-add-user-authentication/spec.md",
  "IMPL_PLAN": "/path/specs/001-add-user-authentication/plan.md",
  "TASKS": "/path/specs/001-add-user-authentication/tasks.md",
  "AVAILABLE_DOCS": ["spec.md", "plan.md", "research.md", "data-model.md", "tasks.md"]
}
```

---

### Group 3: Planning Setup (2 scripts)

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **setup-plan.sh/.ps1** | `/plan` workflow | Initializes planning artifacts, verifies spec exists | At start of planning phase |
| | | Returns: REPO_ROOT, BRANCH, FEATURE_SPEC, IMPL_PLAN, SPECS_DIR (JSON) | Once per feature |

**Example**:
```bash
# Called by /plan workflow
.specify/scripts/bash/setup-plan.sh --json

# Returns:
{
  "REPO_ROOT": "/path/to/repo",
  "BRANCH": "001-add-user-authentication",
  "FEATURE_SPEC": "/path/specs/001-add-user-authentication/spec.md",
  "IMPL_PLAN": "/path/specs/001-add-user-authentication/plan.md",
  "SPECS_DIR": "/path/specs/001-add-user-authentication"
}
```

---

### Group 4: Agent Context (2 scripts)

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **update-agent-context.sh/.ps1** | `/plan` workflow Phase 1 | Updates WINDSURF.md, CLAUDE.md, etc. with feature context | During planning phase |
| | | No JSON output, modifies agent file in place | Once per feature |

**Example**:
```bash
# Called by /plan workflow
.specify/scripts/bash/update-agent-context.sh windsurf

# Updates: specs/001-add-user-authentication/WINDSURF.md
# Adds: Current status, next steps, file references
```

---

### Group 5: Validation (6 scripts - 3 bash + 3 PowerShell)

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **validate-structure.sh/.ps1** | `specify check` or manual | Validates .specify/ directory structure, folder naming | After init, before implementation |
| **validate-naming.sh/.ps1** | `specify check` or manual | Validates file naming conventions (kebab-case) | Anytime, preferably before commits |
| **validate-frontmatter.sh/.ps1** | `specify check` or manual | Validates YAML frontmatter in spec.md, plan.md | After creating specs/plans |

**Output Format**: `[INFO]`, `[WARN]`, `[ERROR]` messages, exit 0 (non-blocking)

**Example**:
```bash
# Called by specify check
.specify/scripts/bash/validate-structure.sh

# Output:
[INFO] Validating project structure...
[INFO] ✓ .specify/ directory exists
[INFO] ✓ .specify/templates/ exists
[WARN] specs/001-add-user-auth/ missing plan.md
[ERROR] specs/002-old-feature/spec.md has invalid frontmatter
[INFO] Validation complete (1 error, 1 warning)
```

---

### Group 6: Orchestration (2 scripts) - **Advanced**

| Script | Called By | Purpose | When to Use |
|--------|-----------|---------|-------------|
| **detect-complexity.sh/.ps1** | Auto-detection or manual | Analyzes feature complexity, suggests workflow path | Before starting implementation |
| **orchestrate-workflow.sh/.ps1** | Advanced workflow coordination | Coordinates multi-step workflows, state management | For complex features with dependencies |

**Example**:
```bash
# Auto-detect complexity
.specify/scripts/bash/detect-complexity.sh --json

# Returns:
{
  "COMPLEXITY_LEVEL": "medium",
  "INDICATORS": ["multiple services", "database schema changes"],
  "RECOMMENDATIONS": ["use /clarify", "create contracts", "TDD approach"]
}
```

---

### Group 7: Common Utilities (2 scripts)

| Script | Used By | Purpose | When to Use |
|--------|---------|---------|-------------|
| **common.sh** | All bash scripts | Shared functions: find_repo_root(), get_current_branch() | Sourced by other scripts |
| **common.ps1** | All PowerShell scripts | Shared functions: Find-RepoRoot, Get-CurrentBranch | Dot-sourced by other scripts |

**Not called directly by users or workflows** - internal library

---

## The 8 Workflow Commands: When to Use Each

### 1. `/specify` - Create Feature Specification
**When**: Start of every new feature  
**Prerequisites**: None (first step)  
**Creates**: `specs/XXX-feature-name/spec.md`  
**Calls**: `create-new-feature.sh`  
**Duration**: 5-10 minutes

**Use When**:
- Starting a new feature
- Need to document requirements
- Want to clarify scope before coding

---

### 2. `/clarify` - Ask Clarification Questions
**When**: After `/specify`, before `/plan` (optional but recommended)  
**Prerequisites**: spec.md must exist  
**Updates**: spec.md (adds ## Clarifications section)  
**Calls**: `check-prerequisites.sh --paths-only`  
**Duration**: 10-20 minutes (interactive)

**Use When**:
- Spec has ambiguous requirements
- Need to de-risk unclear areas
- Want to prevent misunderstandings
- Complex features with multiple interpretations

---

### 3. `/plan` - Generate Implementation Plan
**When**: After `/specify` (and optional `/clarify`)  
**Prerequisites**: spec.md must exist, clarifications recommended  
**Creates**: `plan.md`, `research.md`, `data-model.md`, `contracts/`  
**Calls**: `setup-plan.sh`, `update-agent-context.sh`  
**Duration**: 20-40 minutes

**Use When**:
- Ready to design the solution
- Need technical approach
- Want to research unknowns
- Need data models and contracts

---

### 4. `/tasks` - Create Task Breakdown
**When**: After `/plan`  
**Prerequisites**: plan.md must exist  
**Creates**: `tasks.md` with ordered task list (T001, T002, ...)  
**Calls**: `check-prerequisites.sh`  
**Duration**: 10-20 minutes

**Use When**:
- Ready to break down implementation
- Need actionable task list
- Want to estimate effort
- Need to identify parallel work

---

### 5. `/implement` - Execute Implementation
**When**: After `/tasks`  
**Prerequisites**: tasks.md must exist  
**Updates**: Code files, marks tasks [x] in tasks.md  
**Calls**: `check-prerequisites.sh --require-tasks --include-tasks`  
**Duration**: Hours to days (actual coding)

**Use When**:
- Ready to write code
- All planning complete
- Tasks are clear and actionable
- Following TDD approach

---

### 6. `/analyze` - Cross-Artifact Analysis
**When**: After `/tasks`, before or during `/implement` (optional)  
**Prerequisites**: spec.md, plan.md, tasks.md must exist  
**Output**: Analysis report with recommendations  
**Calls**: `check-prerequisites.sh --require-tasks`  
**Duration**: 5-10 minutes

**Use When**:
- Want quality assurance check
- Need to verify consistency
- Constitutional compliance review
- Before major implementation work

---

### 7. `/constitution` - Establish Project Principles
**When**: At project start or when defining governance  
**Prerequisites**: None  
**Creates**: `.specify/memory/constitution.md`  
**Calls**: No scripts  
**Duration**: 15-30 minutes

**Use When**:
- Starting a new project
- Need to define coding standards
- Want to establish architecture principles
- Team alignment on approach

---

### 8. `/research-tech` - Technical Research
**When**: During `/plan` or when facing unknowns  
**Prerequisites**: None  
**Creates**: `research.md` with findings  
**Calls**: No scripts (uses web search)  
**Duration**: 20-40 minutes

**Use When**:
- Using new technologies
- Need to research best practices
- Evaluating technical options
- Unknown implementation approaches

---

## The 7 Templates: How They're Used

### 1. `spec-template.md`
**Used By**: `/specify` workflow  
**Filled By**: Agent with user input  
**Becomes**: `specs/XXX-feature/spec.md`  
**Has**: YAML frontmatter, feature description, requirements, edge cases

### 2. `plan-template.md`
**Used By**: `/plan` workflow  
**Filled By**: Agent with research and design  
**Becomes**: `specs/XXX-feature/plan.md`  
**Has**: Technical context, architecture, phases, constitution check

### 3. `tasks-template.md`
**Used By**: `/tasks` workflow  
**Filled By**: Agent with task breakdown  
**Becomes**: `specs/XXX-feature/tasks.md`  
**Has**: Ordered tasks with [P] parallel markers, dependencies, phases

### 4. `constitution.md`
**Used By**: `/constitution` workflow, `/plan` Phase 0  
**Filled By**: User/agent with project principles  
**Becomes**: `.specify/memory/constitution.md`  
**Has**: 7 principles (or custom), validation rules, governance

### 5. `brownfield-analysis.md`
**Used By**: `/specify` workflow (when analyzing existing code)  
**Filled By**: Agent after 4-pass code analysis  
**Becomes**: Part of spec.md or separate analysis  
**Has**: 4 passes - structure, context, complexity, integration

### 6. `architecture-patterns.md`
**Used By**: `/plan` workflow (reference)  
**Filled By**: Pre-populated with 10+ frameworks  
**Becomes**: Reference material, not copied  
**Has**: React, Next.js, FastAPI, Django, Rails patterns

### 7. `agent-file-template.md`
**Used By**: `/plan` Phase 1  
**Filled By**: Agent with feature context  
**Becomes**: `specs/XXX-feature/WINDSURF.md` (or CLAUDE.md, etc.)  
**Has**: Current status, next steps, file references, agent guidance

---

## Context Tracking: State Management

### `.specify/context.json` Structure
```json
{
  "version": "2.2.0",
  "initialized": true,         // After specify init
  "complexity_analyzed": false, // After detect-complexity.sh
  "spec_created": false,       // After /specify
  "clarifications_recorded": false, // After /clarify
  "plan_generated": false,     // After /plan
  "tasks_generated": false,    // After /tasks
  "research_complete": false   // After /research-tech or /plan Phase 0
}
```

### How Workflows Use Context

**Before Workflow Execution**:
```javascript
// Agent reads context.json
if (!context.spec_created) {
  return "Error: Run /specify first to create specification"
}

if (!context.clarifications_recorded) {
  return "Warning: Consider running /clarify to reduce ambiguity"
}
```

**After Workflow Execution**:
```javascript
// Agent updates context.json
context.plan_generated = true
save(context)
```

---

## Summary: The "10" Expanded to 20

**Original "10" Core Scripts** (likely referred to):
1. check-prerequisites.sh/.ps1 (2 files)
2. create-new-feature.sh/.ps1 (2 files)
3. setup-plan.sh/.ps1 (2 files)
4. update-agent-context.sh/.ps1 (2 files)
5. validate-structure.sh/.ps1 (2 files)
6. validate-naming.sh/.ps1 (2 files)
7. validate-frontmatter.sh/.ps1 (2 files)
8. common.sh/.ps1 (2 files)
9. detect-complexity.sh/.ps1 (2 files)
10. orchestrate-workflow.sh/.ps1 (2 files)

**Total**: 10 script pairs × 2 platforms = **20 files**

**Plus**:
- 8 workflow command files (specify, clarify, plan, tasks, implement, analyze, constitution, research-tech)
- 7 template files
- 1 context.json (created on init)

**Grand Total**: **36 files** working together for spec-driven development

---

## Quick Decision Tree

```
Need new feature?
  ↓
  /specify → creates spec.md
  ↓
Unclear requirements?
  ↓ YES
  /clarify → asks questions, updates spec.md
  ↓ NO
  /plan → creates plan.md, research.md, data-model.md
  ↓
Ready to break down work?
  ↓
  /tasks → creates tasks.md
  ↓
Need quality check before coding?
  ↓ YES
  /analyze → reports issues
  ↓ NO
  /implement → writes code, marks tasks [x]
  ↓
Done! ✅
```

**The system is sensible**: Each component has a clear role, workflows call scripts, scripts provide data, templates provide structure, context tracks state. Everything works together for conversational, spec-driven development.
