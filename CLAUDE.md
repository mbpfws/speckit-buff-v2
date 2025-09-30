# Windsurf Agent Instructions: Spec-Kit Realignment Fork v2.0

**Project**: spec-kit fork v2.0 | **Feature**: 004-realignment-v2-corrected | **Updated**: 2025-09-30

## Project Context

This is a fork of spec-kit that returns to its original vision: simple templates and scripts for AI agents. You are implementing a minimalist CLI (<400 LOC) that manages high-quality markdown templates and provides non-blocking validation through cross-platform scripts.

**Current Status**: Phase 1 Design complete (clarifications, research, data model, contracts, quickstart)

### Core Philosophy (from Clarifications)
- **Templates guide, agents execute, scripts validate, users decide**
- **Workflows are markdown** (NOT CLI commands) - agents read and execute
- **Scripts = validation (3) + helpers (6) = ~18 total files**
- **Simplicity over complexity**: CLI has ONLY init and check commands
- **Agent-first**: Leverage your native capabilities

### Architecture (Clarified)
1. **CLI Python code**: ONLY `specify init` and `specify check` (<400 LOC)
2. **Workflows**: Markdown files in `templates/commands/*.md` (you read them)
3. **Templates**: 7 markdown files copied from `templates/` → `.specify/templates/`
4. **Scripts**: ~18 files (bash + PowerShell) copied from `scripts/` → `.specify/scripts/`
5. **Constitution**: 7 principles in `.specify/memory/constitution.md`

---

## Available Workflows

### /specify - Create Feature Specification
```bash
# Workflow: templates/commands/specify.md
1. Run: .specify/scripts/bash/create-new-feature.sh --json "$FEATURE_DESC"
2. Parse JSON: BRANCH_NAME, SPEC_FILE, FEATURE_DIR
3. Load: .specify/templates/spec-template.md
4. Fill template with YAML frontmatter (feature_id, title, status, created, version)
5. Create: specs/{id}-{slug}/spec.md
6. Report completion
```

### /clarify - Identify Ambiguities
```bash
# Workflow: templates/commands/clarify.md
1. Run: .specify/scripts/bash/check-prerequisites.sh --json --paths-only
2. Parse JSON: FEATURE_DIR, FEATURE_SPEC
3. Load current spec, scan for ambiguities across 10 categories
4. Ask max 5 clarification questions (one at a time)
5. Record answers in spec.md ## Clarifications section
6. Report completion
```

### /plan - Generate Implementation Plan
```bash
# Workflow: templates/commands/plan.md
1. Run: .specify/scripts/bash/setup-plan.sh --json
2. Parse JSON: FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH
3. Check for ## Clarifications section (pause if missing)
4. Load: .specify/memory/constitution.md
5. Evaluate 7 constitutional principles
6. Execute Phase 0: Create research.md (use web search)
7. Execute Phase 1: Create data-model.md, contracts/, quickstart.md, WINDSURF.md
8. Phase 2: Describe task generation approach (DON'T create tasks.md yet)
9. Report completion
```

### /tasks - Create Task Breakdown
```bash
# Workflow: templates/commands/tasks.md
1. Run: .specify/scripts/bash/check-prerequisites.sh --json
2. Parse JSON: FEATURE_DIR, AVAILABLE_DOCS
3. Load: plan.md, data-model.md, contracts/, research.md, quickstart.md
4. Load: .specify/templates/tasks-template.md
5. Generate ordered task list (TDD: tests before implementation)
6. Mark [P] for parallel tasks (different files, no dependencies)
7. Create: specs/{feature}/tasks.md with T001, T002, etc.
8. Report completion
```

### /analyze - Cross-Artifact Analysis
```bash
# Workflow: templates/commands/analyze.md
1. Run: .specify/scripts/bash/check-prerequisites.sh --json --require-tasks
2. Parse JSON: FEATURE_DIR, SPEC, PLAN, TASKS
3. Load: .specify/memory/constitution.md
4. Perform READ-ONLY analysis (consistency, coverage, ambiguity)
5. Report findings with severity (CRITICAL, HIGH, MEDIUM, LOW)
6. Offer remediation plan (user must approve)
```

### /implement - Execute Implementation
```bash
# Workflow: templates/commands/implement.md
1. Run: .specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
2. Parse JSON: FEATURE_DIR, AVAILABLE_DOCS, task list
3. Execute tasks phase-by-phase (Setup → Tests → Core → Integration → Polish)
4. Follow TDD: tests before implementation
5. Mark tasks complete in tasks.md as you finish them
6. Report progress after each task
```

---

## Script Execution Patterns

### Helper Scripts (JSON Output)
All helper scripts with `--json` flag output standardized JSON:

**check-prerequisites.sh**:
```json
{
  "REPO_ROOT": "/absolute/path",
  "BRANCH": "004-realignment-v2-corrected",
  "FEATURE_DIR": "/absolute/path/specs/004-realignment-v2-corrected",
  "FEATURE_SPEC": "/absolute/path/specs/004-realignment-v2-corrected/spec.md",
  "IMPL_PLAN": "/absolute/path/specs/004-realignment-v2-corrected/plan.md",
  "TASKS": "/absolute/path/specs/004-realignment-v2-corrected/tasks.md",
  "AVAILABLE_DOCS": ["spec.md", "plan.md", "research.md", ...]
}
```

**setup-plan.sh**:
```json
{
  "REPO_ROOT": "/absolute/path",
  "BRANCH": "004-realignment-v2-corrected",
  "FEATURE_SPEC": "/absolute/path/specs/004-realignment-v2-corrected/spec.md",
  "IMPL_PLAN": "/absolute/path/specs/004-realignment-v2-corrected/plan.md",
  "SPECS_DIR": "/absolute/path/specs/004-realignment-v2-corrected"
}
```

### Validation Scripts (Structured Output)
```
[INFO] Starting validation
[WARN] Optional file missing: research.md
[ERROR] Required file missing: spec.md
[INFO] Validation complete
```

---

## Recent Changes (Branch 004)

### Session Summary
1. **Realignment**: Fixed 003 architectural misunderstandings
2. **Clarifications** (5 questions):
   - Q1: Template distribution → Hybrid (embedded + GitHub)
   - Q2: Workflow execution → Agent-read markdown (NOT CLI commands)
   - Q3: Script organization → Validation (3) + Helpers (6) = ~18 files
   - Q4: JSON contracts → Standardized for all helpers
   - Q5: Script distribution → Embedded in package, copied on init
3. **Research**: 5 technical areas researched with web search
4. **Data Model**: 4 entities documented (Template System, Script Library, Workflow Definition, Project Config)
5. **Contracts**: Migrated from 003 (cli-init.yaml, cli-check.yaml, validation-api.yaml)
6. **Quickstart**: 10 integration scenarios documented

### Key Architectural Decisions
- ✅ CLI has ONLY 2 commands (init, check) - workflows are markdown
- ✅ ~18 scripts total (not just 3 validation scripts)
- ✅ All helper scripts have standardized JSON output
- ✅ Constitution in `.specify/memory/constitution.md`
- ✅ Package structure: `templates/` AND `scripts/` directories

---

## Development Guidelines

### When Implementing
1. **Keep CLI <400 LOC**: Currently 224 LOC (56% of budget) - stay under
2. **Scripts are separate**: Don't add script logic to Python code
3. **Follow TDD**: Write tests before implementation
4. **Mark tasks complete**: Update tasks.md with [x] as you finish
5. **Commit frequently**: After each completed task

### When Using Templates
1. **Load from `.specify/templates/`** (user space, not `templates/` source)
2. **Include YAML frontmatter** in all artifacts
3. **Add agent guidance** in HTML comments
4. **Follow template structure** exactly

### When Executing Scripts
1. **Use absolute paths** always
2. **Parse JSON output** from helpers
3. **Parse [LEVEL] messages** from validation
4. **Report findings to user** (don't auto-fix)

---

## Technology Stack

**Language**: Python 3.9+  
**Dependencies**: click, PyYAML, requests, stdlib  
**Testing**: pytest (CLI + integration tests)  
**Scripts**: bash (Unix) + PowerShell (Windows)  
**Platform**: Windows/macOS/Linux + 10 AI coding platforms

---

## Constitution (7 Principles)

All decisions MUST align with:
1. **Cross-Platform Compatibility** - 10 AI platforms, Windows/macOS/Linux
2. **Multi-Installation Support** - PATH (uv tool) + one-time (uvx)
3. **Template-Driven Consistency** - Templates are core, agents fill them
4. **Agent-Native Execution** - Agents are primary actors, system augments
5. **Simplicity Principle** - <400 LOC CLI, zero analysis engines
6. **Governance Balance** - Non-blocking validation, users decide
7. **Backward Compatibility** - V1.x projects work without changes

**Violations require justification** in plan.md Complexity Tracking.

---

## Current Implementation Status

**Completed** (Phase 3.1-3.4):
- ✅ Project structure (pyproject.toml, README, tests)
- ✅ Contract tests (CLI init, check, validation API)
- ✅ Integration tests (10 scenarios from quickstart)
- ✅ Core CLI (init.py, check.py) - 224 LOC
- ✅ Template system (7 templates in source)
- ✅ Constitution template

**Next** (Phase 3.5):
- Create ~18 scripts (bash + PowerShell)
  - Validation: validate-structure, validate-naming, validate-frontmatter
  - Helpers: check-prerequisites, setup-plan, create-new-feature, update-agent-context
- Test cross-platform parity
- Implement JSON output contracts

**Then** (Phase 3.6-3.7):
- Integration & documentation
- QA & validation
- Performance optimization

---

**You are currently executing**: `/plan` workflow Phase 2 (task planning approach)  
**Next command will be**: `/tasks` to generate actual tasks.md
