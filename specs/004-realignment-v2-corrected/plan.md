---
description: "Implementation plan for Spec-Kit Realignment Fork v2.0"
version: "2.0.0"
scripts:
  sh: .specify/scripts/bash/update-agent-context.sh windsurf
  ps: .specify/scripts/powershell/update-agent-context.ps1 -AgentType windsurf
---

# Implementation Plan: Spec-Kit Realignment Fork v2.0

**Branch**: `004-realignment-v2-corrected` | **Date**: 2025-09-30 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `specs/004-realignment-v2-corrected/spec.md`

<!-- 
AGENT GUIDANCE (v2.0):
This plan follows the clarified architecture from /clarify Session 1.
Key: Workflows are markdown (NOT CLI commands), Scripts = validation + helpers (~18 files)
Constitution: 7 principles evaluated before Phase 0
-->

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path ✅
   → Success: spec.md loaded with 5 clarifications
2. Fill Technical Context ✅
   → Detected: Python CLI tool project
3. Load Constitution ✅
4. Evaluate Constitution Check ✅
   → All 7 principles align with feature requirements
5. Execute Phase 0 → research.md (IN PROGRESS)
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent files
7. Re-evaluate Constitution Check
8. Plan Phase 2 → Describe task generation approach
9. STOP - Ready for /tasks command
```

---

## Summary

Create a fork of spec-kit that realigns with the original vision of being a simple template and script system for AI agents. The fork preserves valuable improvements from the 001-improve-spec-kit initiative (brownfield analysis, architecture guidance, artifact management, quality validation) but implements them through agent-augmented templates and validation scripts rather than complex analysis engines.

**Critical Architectural Decisions** (from /clarify Session 1):
1. Templates embedded in package + optional GitHub updates (hybrid)
2. Workflows are markdown files (NOT CLI subcommands) - agents read and execute
3. Scripts = validation (3) + workflow helpers (6) = ~18 total files
4. Standardized JSON output contract for all helper scripts
5. Scripts embedded in package, copied on init (same pattern as templates)

**Focus**: 
- CLI <400 LOC with ONLY init and check commands
- 7 high-quality templates with embedded agent guidance
- ~18 cross-platform scripts (bash + PowerShell)
- Agent-first design leveraging native AI capabilities
- Template-driven guardrails with non-blocking validation

---

## Technical Context

**Language/Version**: Python 3.9+ (broad compatibility)  
**Primary Dependencies**: Python stdlib, requests (template downloads), PyYAML (frontmatter), click (CLI)  
**Storage**: Local filesystem (templates, specs), GitHub Releases (template distribution), user cache (~/.specify/cache/)  
**Testing**: pytest (CLI + integration tests), bash/PowerShell test frameworks (script parity tests)  
**Target Platform**: Cross-platform (Windows/PowerShell, macOS/bash, Linux/bash) supporting 10 AI coding platforms  
**Project Type**: Single CLI tool + template library + script library  
**Performance Goals**: <3s init, <1s check, <200ms template copy, <50MB memory  
**Constraints**: <400 LOC CLI (Python only), zero analysis engines, offline-capable, minimal dependencies  
**Scale/Scope**: 10 AI platforms, 2 installation methods (PATH + uvx), 7 templates, ~18 scripts, template-driven workflows

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### 1. Cross-Platform Compatibility ✅

**Status**: PASS  
**Evidence**:
- FR-016-020: All 10 platforms supported (Claude Code, Roo Code, GitHub Copilot, Cursor, Gemini CLI, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI)
- FR-017: Templates are platform-agnostic markdown
- FR-018: Scripts provided in bash AND PowerShell
- FR-019: Validation output identical across platforms
- Clarification Q2: Workflows are agent-read markdown (platform handles execution)

### 2. Multi-Installation Support ✅

**Status**: PASS  
**Evidence**:
- FR-003: Supports both `uv tool install` (PATH) and `uvx` (one-time)
- Templates/scripts copied to `.specify/` (not dependent on installation method)
- No persistent state required between invocations
- Cache location consistent (~/.specify/cache/)

### 3. Template-Driven Consistency ✅

**Status**: PASS  
**Evidence**:
- FR-006-010: 7 templates as core system (spec, plan, tasks, constitution, brownfield-analysis, architecture-patterns, agent-file)
- FR-009: Agent guidance embedded in HTML comments
- Clarification Q1: Templates embedded in package with optional GitHub updates
- All improvements (brownfield, architecture guidance) implemented as templates, not engines

### 4. Agent-Native Execution ✅

**Status**: PASS  
**Evidence**:
- FR-011-015: Workflows are markdown for agents to read (NOT CLI commands)
- Clarification Q2: Agents remain primary actors, system augments with scripts
- FR-021-024: Brownfield analysis guides agents through 4-pass workflow
- FR-025-028: Architecture patterns provide guidance, agents validate against official docs
- No automated analysis engines (FR-001: CLI has ONLY init/check)

### 5. Simplicity Principle ✅

**Status**: PASS  
**Evidence**:
- FR-001: CLI has exactly 2 commands (init, check)
- FR-002: CLI <400 LOC (currently 224 LOC = 56% of budget)
- FR-005: Only 4 dependencies (stdlib, requests, PyYAML, click)
- Clarification Q2: Workflows NOT in CLI (keeps LOC low)
- Zero analysis engines
- NFR-009: Cyclomatic complexity <10 per function

### 6. Governance Balance ✅

**Status**: PASS  
**Evidence**:
- FR-038: Scripts exit code 0 (non-blocking)
- FR-037: Clear severity levels ([INFO], [WARN], [ERROR])
- FR-045: Quality checks non-blocking
- FR-047: Findings reported to user for decision
- Agents report, users decide (no auto-blocking)

### 7. Backward Compatibility ✅

**Status**: PASS  
**Evidence**:
- Edge case: V1.x projects validate without changes
- V1.x frontmatter format supported (feature_id, title, status fields)
- V1.x folder structure (specs/{id}-{slug}/) works
- Migration from 003 to 004 successful (valid content preserved)
- No forced breaking changes

**Initial Constitution Check**: ✅ **PASS** - All 7 principles satisfied

---

## Project Structure

### Documentation (this feature)
```
specs/004-realignment-v2-corrected/
├── spec.md                  # Feature spec with clarifications ✅
├── plan.md                  # This file (/plan output)
├── research.md              # Phase 0 output (in progress)
├── data-model.md            # Phase 1 output
├── quickstart.md            # Phase 1 output
├── contracts/               # Phase 1 output
│   ├── cli-init.yaml        # Init command contract
│   ├── cli-check.yaml       # Check command contract
│   └── validation-api.yaml  # Script validation contract
├── WINDSURF.md              # Agent instructions (Phase 1)
└── MIGRATION_NOTES.md       # 003→004 transition docs ✅
```

### Source Code (repository root)
```
# Single project structure (Python CLI tool)

templates/                   # SOURCE templates (in package)
├── spec-template.md         # Feature spec template ✅
├── plan-template.md         # Implementation plan template ✅
├── tasks-template.md        # Task generation template ✅
├── constitution.md          # Constitutional principles ✅
├── brownfield-analysis.md   # 4-pass analysis template ✅
├── architecture-patterns.md # Framework patterns template ✅
└── agent-file-template.md   # Agent context template ✅

templates/commands/          # Workflow definitions (markdown)
├── specify.md               # /specify workflow ✅
├── clarify.md               # /clarify workflow ✅
├── plan.md                  # /plan workflow ✅
├── tasks.md                 # /tasks workflow ✅
├── analyze.md               # /analyze workflow ✅
├── implement.md             # /implement workflow ✅
└── constitution.md          # /constitution workflow

scripts/                     # SOURCE scripts (in package) 
├── bash/                    # Unix scripts
│   ├── validate-structure.sh        # Validation
│   ├── validate-naming.sh           # Validation
│   ├── validate-frontmatter.sh      # Validation
│   ├── check-prerequisites.sh       # Helper (JSON output)
│   ├── setup-plan.sh                # Helper (JSON output)
│   ├── create-new-feature.sh        # Helper (JSON output)
│   └── update-agent-context.sh      # Helper
└── powershell/              # Windows scripts (identical behavior)
    ├── validate-structure.ps1
    ├── validate-naming.ps1
    ├── validate-frontmatter.ps1
    ├── check-prerequisites.ps1
    ├── setup-plan.ps1
    ├── create-new-feature.ps1
    └── update-agent-context.ps1

specify_cli/                 # CLI implementation (Python)
├── __init__.py              # Version ✅
├── cli.py                   # Main entry point ✅
├── commands/
│   ├── __init__.py          # ✅
│   ├── init.py              # Init command ✅
│   └── check.py             # Check command ✅
├── template_loader.py       # Template management ✅
└── validators.py            # Validation script wrapper ✅

tests/                       # Test suite
├── contract/                # Contract tests (TDD)
│   ├── test_cli_init.py     # Init command tests ✅
│   ├── test_cli_check.py    # Check command tests ✅
│   └── test_validation_api.py # Validation tests ✅
├── integration/             # Integration tests
│   ├── test_greenfield_init.py ✅
│   ├── test_brownfield_analysis.py ✅
│   ├── test_architecture_patterns.py ✅
│   └── (others)             # ✅
└── helpers.py               # Test utilities ✅

User Project (after `specify init`):
.specify/                    # USER space (copied from package)
├── templates/               # Templates copied from source
│   ├── (7 template files)
├── scripts/                 # Scripts copied from source
│   ├── bash/                # (9 scripts)
│   └── powershell/          # (9 scripts)
├── memory/                  # NEW v2.0
│   └── constitution.md      # Constitution copy
└── config.yaml              # User configuration
```

**Structure Decision**: Single project structure chosen. This is a Python CLI tool with templates and scripts as package data, not a web/mobile application. All source code in repository root with clear separation: `templates/` (markdown), `scripts/` (bash/PS), `specify_cli/` (Python), `tests/` (pytest).

---

## Phase 0: Outline & Research

### Research Tasks

Based on Technical Context unknowns and spec requirements, research needed for:

#### 1. **Python Package Distribution with Embedded Resources**
**Question**: How to package markdown templates and bash/PowerShell scripts with Python package for both PATH and uvx installation?

**Research needed**:
- Python package data inclusion (setuptools vs pyproject.toml)
- Accessing package resources at runtime (importlib.resources)
- Ensuring scripts remain executable after installation
- Supporting both `uv tool` and `uvx` methods

#### 2. **Cross-Platform Script Execution and JSON Output**
**Question**: Best practices for ensuring bash and PowerShell scripts produce identical JSON output?

**Research needed**:
- JSON generation in bash (using jq or native)
- JSON generation in PowerShell (ConvertTo-Json)
- Path handling cross-platform (Windows backslashes vs Unix forward slashes)
- Testing script parity across platforms

#### 3. **Workflow Command Pattern for AI Agents**
**Question**: How do existing AI coding platforms handle markdown-based workflow definitions?

**Research needed**:
- Windsurf workflows (current platform)
- Claude Code command system
- GitHub Copilot instruction patterns
- Common patterns across 10 platforms

#### 4. **Template Versioning and Distribution via GitHub Releases**
**Question**: Best practices for distributing templates via GitHub Releases with hybrid embedded fallback?

**Research needed**:
- GitHub Releases API for checking latest version
- Tar.gz packaging for template archives
- Semantic versioning for templates
- Cache invalidation strategies

#### 5. **Non-Blocking Validation Script Patterns**
**Question**: Standard patterns for validation scripts that exit 0 with structured output?

**Research needed**:
- Logging level conventions ([INFO], [WARN], [ERROR])
- Exit code 0 rationale and user acceptance
- Structured output parsing by agents
- Common validation tools (eslint, pylint) output formats

### Research Output Location

All research findings consolidated in: `specs/004-realignment-v2-corrected/research.md` ✅

---

## Phase 1: Design & Contracts

*Prerequisites: research.md complete ✅*

### Artifacts Generated ✅

1. **data-model.md** ✅
   - 4 entities: Template System, Script Library, Workflow Definition, Project Configuration
   - All attributes, relationships, business rules documented
   - JSON contracts for helper scripts
   - State transitions and validation rules

2. **contracts/** ✅
   - `cli-init.yaml` - Init command API contract (migrated from 003)
   - `cli-check.yaml` - Check command API contract (migrated from 003)
   - `validation-api.yaml` - Script validation contract (migrated from 003)

3. **quickstart.md** ✅
   - 10 integration test scenarios (migrated from 003)
   - Acceptance criteria for each scenario
   - Cross-platform validation guidance

4. **WINDSURF.md** ✅
   - Agent instructions for this platform
   - Workflow reference (/specify, /clarify, /plan, /tasks, /analyze, /implement)
   - Script execution patterns
   - Current implementation status
   - Recent changes summary

### Post-Design Constitution Re-check ✅

**Status**: PASS - All 7 principles still satisfied after design phase

**Changes from initial check**: None - design maintained all principles

**Complexity Tracking**: No violations to document

---

## Phase 2: Task Planning Approach

*This section describes what the /tasks command will do - DO NOT execute during /plan*

### Task Generation Strategy

**Input Documents**:
- ✅ `plan.md` - Technical stack, architecture, structure decision
- ✅ `research.md` - Technical decisions and patterns
- ✅ `data-model.md` - 4 entities with relationships
- ✅ `contracts/` - 3 API contracts (CLI commands + validation)
- ✅ `quickstart.md` - 10 integration test scenarios

**Task Generation Rules**:
1. Load `.specify/templates/tasks-template.md` as base structure
2. Generate tasks from design artifacts:
   - **From contracts/**: Each contract → contract test task [P]
   - **From data-model.md**: Each entity component → implementation task
   - **From quickstart.md**: Each scenario → integration test task [P]
   - **From research.md**: Each technical decision → setup/config task

**Task Categories** (5 phases):
1. **Phase 3.1: Setup** (5 tasks)
   - Project structure per implementation plan ✅ (already done)
   - pyproject.toml with dependencies ✅ (already done)
   - Testing infrastructure ✅ (already done)
   - Linting and formatting ✅ (already done)
   - README and documentation ✅ (already done)

2. **Phase 3.2: Tests First (TDD)** (~13 tasks)
   - Contract tests for cli-init.yaml [P] ✅ (already done)
   - Contract tests for cli-check.yaml [P] ✅ (already done)
   - Contract tests for validation-api.yaml [P] ✅ (already done)
   - Integration tests for 10 quickstart scenarios [P] ✅ (partially done)

3. **Phase 3.3: Core Implementation** (5 tasks)
   - template_loader.py ✅ (already done)
   - validators.py ✅ (already done)
   - cli.py ✅ (already done)
   - init.py ✅ (already done)
   - check.py ✅ (already done)

4. **Phase 3.4: Template Creation** (6 tasks)
   - spec-template.md ✅ (already done)
   - plan-template.md ✅ (already done)
   - tasks-template.md ✅ (already done)
   - constitution.md ✅ (already done)
   - brownfield-analysis.md ✅ (already done)
   - architecture-patterns.md ✅ (already done)

5. **Phase 3.5: Validation Scripts** (~18 tasks) **← NEXT PHASE**
   - bash/validate-structure.sh [P]
   - bash/validate-naming.sh [P]
   - bash/validate-frontmatter.sh [P]
   - bash/check-prerequisites.sh [P]
   - bash/setup-plan.sh [P]
   - bash/create-new-feature.sh [P]
   - bash/update-agent-context.sh [P]
   - powershell/*.ps1 equivalents (7 scripts) [P]
   - Cross-platform parity tests for all scripts
   - JSON output validation tests

6. **Phase 3.6: Integration & Documentation** (7 tasks)
   - pyproject.toml package data configuration
   - init.py script copying implementation
   - Integration tests for script execution
   - Cross-platform CI/CD configuration
   - Documentation updates
   - Performance optimization
   - Memory footprint validation

7. **Phase 3.7: QA & Validation** (8 tasks)
   - All contract tests passing
   - All integration tests passing
   - LOC count <400 validation
   - Cross-platform testing
   - Constitutional compliance check
   - Performance benchmarks
   - Security audit
   - Release preparation

**Ordering Strategy**:
- **TDD order**: Tests before implementation (Phase 3.2 before 3.3)
- **Dependency order**: Core before integration (3.3 before 3.6)
- **Parallel execution**: Mark [P] for independent file tasks
- **Sequential**: Tasks affecting same files must be sequential

**Parallel Execution Patterns**:
- All validation scripts can be created in parallel [P]
- All PowerShell scripts can be created in parallel [P]
- Integration tests for different scenarios can run in parallel [P]
- Template creation tasks were parallelizable [P]

**Estimated Output**: 
- ~50 total tasks across 7 phases
- ~29 already complete (Setup, Tests-partial, Core, Templates)
- ~21 remaining (Scripts, Integration, QA)

**Task Numbering**: 
- Continue from T001-T029 (already complete)
- New tasks start at T030

**Dependencies**:
- T030-T036 (bash scripts) must complete before T037-T043 (PowerShell equivalents) for reference
- All scripts must complete before integration tests (Phase 3.6)
- Integration must complete before QA (Phase 3.7)

**IMPORTANT**: Phase 2 describes the approach only. The `/tasks` command will generate the actual `tasks.md` file.

---

## Progress Tracking

**Phase Status**:
- [x] Phase 0: Research complete ✅
- [x] Phase 1: Design complete ✅
- [x] Phase 2: Task planning approach described ✅
- [ ] Phase 3: Tasks generated (/tasks command - NOT executed yet)
- [ ] Phase 4: Implementation (use /implement command)
- [ ] Phase 5: Validation (final QA)

**Gate Status**:
- [x] Initial Constitution Check: PASS ✅
- [x] Post-Design Constitution Check: PASS ✅
- [x] All technical unknowns resolved ✅
- [x] No complexity deviations to document ✅

**Artifacts Generated**:
- [x] plan.md (this file) ✅
- [x] research.md ✅
- [x] data-model.md ✅
- [x] contracts/ (3 files) ✅
- [x] quickstart.md ✅
- [x] WINDSURF.md ✅

---

## Execution Flow Status

```
1. Load feature spec ✅
2. Fill Technical Context ✅
3. Load Constitution ✅
4. Evaluate Constitution Check ✅
5. Execute Phase 0 → research.md ✅
6. Execute Phase 1 → contracts, data-model, quickstart, WINDSURF ✅
7. Re-evaluate Constitution Check ✅
8. Plan Phase 2 → Task generation approach ✅
9. STOP - Ready for /tasks command ✅
```

**Status**: ✅ `/plan` workflow COMPLETE

---

*Based on Constitution v2.1.1 - See `.specify/memory/constitution.md`*
