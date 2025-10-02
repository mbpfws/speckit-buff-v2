
# Implementation Plan: Spec-Kit Realignment Fork - Back to Basics

**Branch**: `003-based-on-the` | **Date**: 2025-09-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `D:/speckit-buff/specs/003-based-on-the/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
Create a fork of spec-kit that realigns with the original vision of being a simple template and script system for AI agents. The fork preserves valuable improvements from the 001-improve-spec-kit initiative (brownfield analysis, architecture guidance, artifact management, quality validation) but implements them through agent-augmented templates and validation scripts rather than complex analysis engines. Focus on: (1) CLI under 400 lines with only init and check commands, (2) high-quality markdown templates with embedded research instructions, (3) cross-platform validation scripts, (4) agent-first design leveraging native AI capabilities, (5) template-driven guardrails with non-blocking validation.

## Technical Context
**Language/Version**: Python 3.9+ (minimal version for broad compatibility)  
**Primary Dependencies**: Python stdlib, requests (template downloads), PyYAML (frontmatter parsing)  
**Storage**: Local filesystem (templates, specs, artifacts), GitHub Releases (template distribution)  
**Testing**: pytest (CLI tests), bash/PowerShell test frameworks (validation script tests)  
**Target Platform**: Cross-platform (Windows, macOS, Linux) supporting all 10 AI coding platforms
**Project Type**: Single CLI tool with template library and validation scripts  
**Performance Goals**: <3s init time, <1s validation checks, minimal memory footprint  
**Constraints**: <400 LOC for CLI, zero analysis engines, offline-capable after initial setup  
**Scale/Scope**: Support 10 AI platforms, 2 installation methods (PATH + uvx), template-driven workflows

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Note**: The constitution template is currently empty/placeholder. Based on the feature requirements and the 001-improve-spec-kit governance principles, the following constitutional principles apply:

### Cross-Platform Compatibility ✅
- **Requirement**: All 10 platforms supported (Claude Code, Roo Code, GitHub Copilot, Cursor, Gemini CLI, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI)
- **Status**: PASS - Templates are platform-agnostic, validation scripts provided in bash/PowerShell
- **Evidence**: FR-016 through FR-020, FR-038 through FR-041

### Multi-Installation Support ✅
- **Requirement**: Both PATH (uv tool) and uvx (one-time) installation patterns
- **Status**: PASS - CLI designed for both methods
- **Evidence**: FR-004

### Template-Driven Consistency ✅
- **Requirement**: High-quality markdown templates as core system
- **Status**: PASS - Templates are self-contained with embedded guidance
- **Evidence**: FR-006 through FR-010, all simplified improvements use template-driven approach

### Agent-Native Execution ✅
- **Requirement**: AI agents remain primary actors, system augments not replaces
- **Status**: PASS - Agents use templates, scripts validate, users decide
- **Evidence**: FR-011 through FR-015, agent-augmented analysis (FR-021-024), hybrid research (FR-025-028)

### Simplicity Principle ✅
- **Requirement**: Minimal tooling overhead, no complex analysis engines
- **Status**: PASS - CLI <400 LOC, zero analysis engines, minimal dependencies
- **Evidence**: FR-001, FR-002, FR-005, Implementation Notes section

### Governance Balance ✅
- **Requirement**: Non-blocking validation, user autonomy preserved
- **Status**: PASS - Scripts provide warnings, agents report, users decide
- **Evidence**: FR-042 through FR-047, governance enforcement philosophy (Q4 clarification)

### Backward Compatibility ✅
- **Requirement**: Existing spec-kit projects work without changes
- **Status**: PASS - Template structure preserved, clear migration path
- **Evidence**: FR-046, Migration from Current spec-kit section

**Initial Constitution Check**: ✅ PASS

## Project Structure

### Documentation (this feature)
```
specs/003-based-on-the/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
│   ├── cli-init.yaml    # Init command contract
│   ├── cli-check.yaml   # Check command contract
│   └── validation-api.yaml  # Validation script interfaces
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
specify-cli/
├── __init__.py          # Package initialization
├── cli.py               # Main CLI entry point (<400 LOC target)
├── commands/
│   ├── __init__.py
│   ├── init.py          # Init command implementation
│   └── check.py         # Check command implementation
├── template_loader.py   # Template download from GitHub Releases
└── validators.py        # Validation script integration

.specify/
├── templates/           # High-quality markdown templates
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   ├── constitution.md
│   ├── brownfield-analysis.md  # Agent-augmented checklists
│   └── architecture-patterns.md  # Framework starter patterns
├── scripts/
│   ├── bash/            # Unix/Linux validation scripts
│   │   ├── validate-structure.sh
│   │   ├── validate-naming.sh
│   │   └── validate-frontmatter.sh
│   └── powershell/      # Windows validation scripts
│       ├── validate-structure.ps1
│       ├── validate-naming.ps1
│       └── validate-frontmatter.ps1
└── workflows/           # Platform-specific instruction files
    ├── CLAUDE.md        # Claude Code instructions
    ├── ROO.md           # Roo Code instructions
    ├── WINDSURF.md      # Windsurf instructions
    └── AGENTS.md        # Generic agent instructions

tests/
├── contract/            # Contract tests for CLI commands
│   ├── test_init_contract.py
│   └── test_check_contract.py
├── integration/         # End-to-end workflow tests
│   ├── test_greenfield_workflow.py
│   └── test_brownfield_workflow.py
└── unit/                # Unit tests for core functions
    ├── test_template_loader.py
    └── test_validators.py

pyproject.toml           # Package configuration (uv project)
README.md                # Fork documentation with migration guide
```

**Structure Decision**: Single CLI project with embedded template library. This structure supports:
1. **Simplicity**: All CLI code in `specify-cli/` directory, targeted <400 LOC for core CLI
2. **Template-Driven**: Templates in `.specify/templates/` with agent research instructions
3. **Cross-Platform**: Dual validation scripts (bash + PowerShell) for all platforms
4. **Agent-Native**: Platform-specific workflow files guide AI agents appropriately
5. **Offline-Capable**: Templates cached locally after initial download
6. **Backward Compatible**: `.specify/` structure matches original spec-kit pattern

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:
   ```
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh windsurf`
     **IMPORTANT**: Execute it exactly as specified above. Do not add or remove any arguments.
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
The /tasks command will generate a detailed task breakdown based on the design artifacts created in Phase 1. The strategy follows TDD principles and constitutional alignment.

### Input Artifacts
- `research.md`: Technical decisions and research findings
- `data-model.md`: Core entities (10 identified)
- `contracts/`: CLI command contracts (3 contracts)
- `quickstart.md`: Integration test scenarios (10 scenarios)

### Task Categories

#### 1. Project Setup Tasks
- Create repository structure (specify-cli/, .specify/, tests/)
- Configure pyproject.toml with dependencies (click, requests, PyYAML)
- Set up testing infrastructure (pytest configuration)
- Create README.md with installation instructions

#### 2. Contract Test Tasks [P]
Based on `contracts/` directory:
- **Contract Test: cli-init.yaml** → Test init command behavior
- **Contract Test: cli-check.yaml** → Test check command behavior
- **Contract Test: validation-api.yaml** → Test validation script interfaces

Each contract test task follows TDD: Write failing test → Implement → Pass

#### 3. Core Implementation Tasks

**CLI Module** (Target: <400 LOC total):
- Implement `cli.py` main entry point with Click (~80 LOC)
- Implement `commands/init.py` for template download (~100 LOC)
- Implement `commands/check.py` for validation orchestration (~80 LOC)
- Implement `template_loader.py` for GitHub releases (~80 LOC)
- Implement `validators.py` for script execution wrappers (~60 LOC)

**Template Files**:
- Create `spec-template.md` with agent guidance
- Create `plan-template.md` (update from current)
- Create `tasks-template.md` for task generation
- Create `constitution.md` guiding principles
- Create `brownfield-analysis.md` agent checklists
- Create `architecture-patterns.md` framework patterns

**Validation Scripts** (Dual implementation):
- Create `bash/validate-structure.sh` (50-100 LOC)
- Create `bash/validate-naming.sh` (50-100 LOC)
- Create `bash/validate-frontmatter.sh` (50-100 LOC)
- Create `powershell/validate-structure.ps1` (parity)
- Create `powershell/validate-naming.ps1` (parity)
- Create `powershell/validate-frontmatter.ps1` (parity)

#### 4. Integration Test Tasks
Based on `quickstart.md` scenarios:
- Integration test: Greenfield project initialization (Scenario 1)
- Integration test: Brownfield project analysis (Scenario 2)
- Integration test: Framework-specific architecture (Scenario 3)
- Integration test: Artifact validation workflow (Scenario 4)
- Integration test: Multi-platform execution (Scenario 5)
- Integration test: Quality tool integration (Scenario 6)
- Integration test: CLI simplicity verification (Scenario 7)
- Integration test: Cross-platform scripts (Scenario 8)
- Integration test: Offline usage (Scenario 9)
- Integration test: Backward compatibility (Scenario 10)

#### 5. Documentation Tasks
- Update README.md with migration guide from v1.x
- Create CONTRIBUTING.md for fork contributors
- Create examples/ directory with sample workflows
- Document platform-specific workflows (10 AI platforms)

### Task Ordering Strategy

**Phase A: Foundation** (Can run in parallel after project setup)
1. Project setup and configuration
2. Contract test writing (all tests fail initially)

**Phase B: Core Implementation** (Sequential by dependency)
1. Template loader (no dependencies)
2. Validators wrapper (no dependencies)
3. CLI main + init command (depends on template loader)
4. CLI check command (depends on validators)
5. Templates creation (can be parallel)
6. Validation scripts (bash + PowerShell pairs)

**Phase C: Integration & Validation** (After core implementation)
1. Integration tests execution (verify quickstart scenarios)
2. Cross-platform testing (Windows, macOS, Linux)
3. Performance validation (<3s init, <1s check)
4. LOC audit (verify <400 LOC constraint)

**Phase D: Documentation & Release**
1. Documentation completion
2. Migration guide finalization
3. Release preparation (GitHub Release setup)
4. Backward compatibility testing

### Dependency Annotations
- `[P]`: Parallel execution possible (no blocking dependencies)
- `[DEP: task-id]`: Depends on specified task completion
- `[TEST]`: Test task (must fail before implementation)
- `[IMPL]`: Implementation task (makes tests pass)

### Estimated Breakdown
- **Setup Tasks**: 5 tasks
- **Contract Tests**: 3 tasks [TEST]
- **Core Implementation**: 15 tasks [IMPL]
- **Template Creation**: 6 tasks [P]
- **Validation Scripts**: 6 tasks (3 bash + 3 PowerShell)
- **Integration Tests**: 10 tasks [TEST]
- **Documentation**: 5 tasks [P]

**Total Estimated**: ~50 tasks

### Success Criteria for Task Generation
- All tasks numbered sequentially (T001, T002, ...)
- Dependencies clearly marked
- TDD order maintained (tests before implementations)
- Parallel tasks identified for efficiency
- Each task has clear acceptance criteria
- LOC targets specified for code tasks

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Post-Design Constitution Check
*Re-evaluation after Phase 1 design artifacts generated*

### Cross-Platform Compatibility ✅
- **Status**: PASS - All design artifacts are platform-agnostic
- **Evidence**: Templates (markdown), contracts (YAML), scripts (bash + PowerShell)
- **Verification**: No platform-specific dependencies introduced

### Multi-Installation Support ✅
- **Status**: PASS - Design supports both uv tool and uvx patterns
- **Evidence**: CLI contract (cli-init.yaml) documents both installation methods
- **Verification**: No installation-specific code in design

### Template-Driven Consistency ✅
- **Status**: PASS - Templates remain core of system design
- **Evidence**: 6 template files specified in design, agent instructions embedded
- **Verification**: Data model shows Template as first-class entity

### Agent-Native Execution ✅
- **Status**: PASS - Design leverages agent capabilities without replacement
- **Evidence**: Brownfield analysis via agent checklists, architecture via agent research
- **Verification**: No analysis engines in implementation design

### Simplicity Principle ✅
- **Status**: PASS - Design maintains <400 LOC target
- **Evidence**: LOC breakdown in Phase 2 totals ~400 LOC for CLI
- **Verification**: Minimal dependencies confirmed (4 total: stdlib, requests, PyYAML, click)

### Governance Balance ✅
- **Status**: PASS - Non-blocking validation design maintained
- **Evidence**: Validation API contract specifies exit code 0 always
- **Verification**: Agent reporting pattern documented in contracts

### Backward Compatibility ✅
- **Status**: PASS - Design preserves v1.x compatibility
- **Evidence**: Quickstart Scenario 10 tests v1.x project compatibility
- **Verification**: No breaking changes to template structure

**Post-Design Constitution Check**: ✅ PASS - No violations introduced during design

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

**No Violations**: All constitutional principles satisfied. No complexity deviations to document.


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command) ✅
  - Generated: research.md (9 technical decisions documented)
  - All NEEDS CLARIFICATION markers resolved
- [x] Phase 1: Design complete (/plan command) ✅
  - Generated: data-model.md (10 core entities)
  - Generated: contracts/ (3 contracts: cli-init, cli-check, validation-api)
  - Generated: quickstart.md (10 integration test scenarios)
  - Generated: WINDSURF.md (platform-specific agent instructions)
- [x] Phase 2: Task planning complete (/plan command - describe approach only) ✅
  - Documented: Task generation strategy with ~50 tasks estimated
  - Defined: Task categories, ordering, dependencies
  - Specified: Success criteria for /tasks command
- [x] Phase 3: Tasks generated (/tasks command) ✅
  - Generated: tasks.md with 50 tasks (T001-T050)
  - Organized: 8 phases (Setup, Tests, Implementation, Templates, Scripts, Integration, Docs, QA)
  - Dependencies: Critical path and parallel opportunities documented
  - TDD order: All tests (T006-T018) before implementation (T019-T023)
- [ ] Phase 4: Implementation execution - READY (use /implement command)
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS ✅
- [x] Post-Design Constitution Check: PASS ✅
- [x] All NEEDS CLARIFICATION resolved ✅
- [x] Complexity deviations documented: None (all principles satisfied) ✅

**Artifacts Generated**:
1. `research.md` (Phase 0) - 9 research sections
2. `data-model.md` (Phase 1) - 10 entities with validation rules
3. `contracts/cli-init.yaml` (Phase 1) - Init command contract
4. `contracts/cli-check.yaml` (Phase 1) - Check command contract
5. `contracts/validation-api.yaml` (Phase 1) - Validation script interface
6. `quickstart.md` (Phase 1) - 10 integration test scenarios
7. `WINDSURF.md` (Phase 1) - Agent instructions for Windsurf platform
8. `plan.md` (This file) - Updated with Phase 2 planning approach
9. `tasks.md` (Phase 3) - 50 tasks organized in 8 phases with TDD ordering

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
