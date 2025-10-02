
# Implementation Plan: Spec-Kit Enhanced Fork v2.0

**Branch**: `005-spec-kit-enhanced` | **Date**: 2025-09-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/005-spec-kit-enhanced/spec.md`

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

Enhance spec-kit framework with brownfield intelligence, agent self-regulation, and cross-platform governance while preserving <400 LOC CLI philosophy. Implement via templates/scripts/workflows only (no new Python analysis engines). Address 45+ systemic shortcomings across 5 sectors: Commands (6), Templates (8), Scripts (26), Governance (2), CLI (2). Research-driven approach with 5 domains completed: brownfield patterns (4-pass analysis), agent context management ("According to..." prompting reduces hallucinations 30%), dependency intelligence (npm audit + breaking changes), Next.js 2025 architecture (route groups, server/client boundaries), realistic TDD (E2E for extended stories). MVP supports 4 platforms: Claude Code, Windsurf, Roo Code, Cursor.

## Technical Context
**Language/Version**: Python 3.9+ (CLI), Bash + PowerShell (scripts), Markdown (templates)  
**Primary Dependencies**: Python stdlib, requests, PyYAML, click (CLI <400 LOC constraint)  
**Storage**: File system (.specify/ folder), .specify/context.json (workflow state), .specify/file-history.json (file tracking), Git (version control)  
**Testing**: Cross-platform parity tests (bash output === PowerShell output), integration tests (workflow execution), manual validation (15 acceptance scenarios)  
**Target Platform**: Cross-OS (Windows/macOS/Linux), 4 AI platforms (Claude Code, Windsurf, Roo Code, Cursor)
**Project Type**: Framework enhancement (spec-kit fork)  
**Performance Goals**: specify init <3s, specify check <1s, script execution <500ms, template copy <200ms  
**Constraints**: <400 LOC CLI total, NO new Python analysis engines, preserve original spec-kit philosophy (template-driven, agent-first), GitHub download from https://github.com/mbpfws/speckit-buff-v2/  
**Scale/Scope**: 32 file changes (11 modifications + 21 new), 89+ requirements across 5 sectors, 10 platforms eventual support (4 MVP)

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Note**: The constitution template at `.specify/memory/constitution.md` is a placeholder. For this feature, we apply **original spec-kit principles** from research + user clarifications:

### Principle 1: Preserve <400 LOC CLI (NON-NEGOTIABLE)
✅ **PASS**: Only `specify_cli/__init__.py` modified, adding platform detection + GitHub download logic (~50 LOC addition, stays under 400 total)

### Principle 2: Template-Driven, Agent-First Design  
✅ **PASS**: All enhancements via templates (8 new), scripts (26 new), workflows (3 new). Zero Python analysis engines added.

### Principle 3: Cross-Platform Compatibility
✅ **PASS**: All scripts have bash + PowerShell versions with identical JSON output. Templates platform-agnostic. MVP supports 4 platforms.

### Principle 4: NO Breaking Changes to Original Spec-Kit
✅ **PASS**: Modifications preserve backward compatibility. Existing workflows continue functioning. New features opt-in via flags.

### Principle 5: Research-Driven Decisions
✅ **PASS**: 5 research domains completed (brownfield, context management, dependencies, architecture, TDD). All decisions cite sources.

**Conclusion**: All constitutional principles satisfied. No complexity deviations to justify.

## Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->
```
# Spec-Kit Framework Enhancement Structure
D:/speckit-buff/
├── specify_cli/
│   └── __init__.py                    # [MODIFY] Add platform detection, GitHub download
├── templates/
│   ├── commands/
│   │   ├── specify.md                 # [MODIFY] Add complexity tier detection
│   │   ├── plan.md                    # [MODIFY] Meta-template reference
│   │   ├── tasks.md                   # [MODIFY] YAML metadata guidance
│   │   ├── analyze-brownfield.md      # [NEW] 4-pass workflow
│   │   ├── validate-governance.md     # [NEW] Tag/metadata validation
│   │   └── migrate-platform.md        # [NEW] Cross-platform migration
│   ├── spec-template.md               # [MODIFY] Conditional tier sections
│   ├── plan-template.md               # [MODIFY] Remove embedded patterns
│   ├── tasks-template.md              # [MODIFY] YAML frontmatter
│   ├── brownfield-analysis.md         # [NEW] 4-pass checklist
│   ├── agent-prompt-patterns.md       # [NEW] CoVe, Step-Back, Citations
│   ├── dependency-report.md           # [NEW] npm audit template
│   ├── testing-strategy.md            # [NEW] Realistic TDD
│   └── architecture-meta-template.md  # [NEW] Research workflow
├── scripts/
│   ├── bash/
│   │   ├── check-prerequisites.sh     # [MODIFY] Add --validate-tags
│   │   ├── analyze-codebase.sh        # [NEW] Tech stack detection
│   │   ├── sync-tasks.sh              # [NEW] YAML ↔ tags ↔ git
│   │   ├── validate-tags.sh           # [NEW] Scan missing tags
│   │   ├── inject-tags.sh             # [NEW] Auto-add with confirm
│   │   ├── check-dependencies.sh      # [NEW] npm audit/pip
│   │   ├── detect-breaking-changes.sh # [NEW] Changelog parsing
│   │   ├── detect-framework.sh        # [NEW] Framework detection
│   │   ├── validate-context.sh        # [NEW] Frontmatter validation
│   │   ├── scaffold-feature.sh        # [NEW] Tier boilerplate
│   │   ├── extract-section.sh         # [NEW] Section extraction
│   │   ├── migrate-platform.sh        # [NEW] Platform file copy
│   │   ├── track-file-rename.sh       # [NEW] File history
│   │   ├── mark-file-deprecated.sh    # [NEW] Deprecation metadata
│   │   └── build-task-graph.sh        # [NEW] DAG + cycle detect
│   └── powershell/                    # [NEW] 13 PowerShell versions
│       └── (same scripts as bash with .ps1 extension)
├── AGENTS.md                          # [MODIFY] 4 platforms + brownfield + self-regulation
└── memory/
    └── constitution.md                # [MODIFY] Add 3 principles

tests/
├── cross-platform/                    # [NEW] Bash/PowerShell parity tests
├── integration/                       # [NEW] Workflow execution tests
└── scripts/                           # [NEW] Script JSON output validation
```

**Structure Decision**: Framework enhancement following original spec-kit architecture. All enhancements implemented via templates/scripts/workflows in existing directory structure. No new top-level directories. Platform-specific files copied to `.claude/`, `.windsurf/`, `.cursor/`, `.roo/` during `specify init`.

## Phase 0: Outline & Research

**Status**: ✅ COMPLETE - research.md already exists from `/specify` workflow

**Research Completed**: 5 domains (50+ sources)
1. **Brownfield Software Analysis**: BMAD Method, 4-pass pattern, confidence levels
2. **AI Agent Context Management**: "According to..." prompting (30% reduction), CoVe, Step-Back
3. **Dependency Version Conflicts**: npm audit, PeerChecker (14x faster), breaking changes
4. **Next.js App Router 2025**: Route groups, private folders, server/client boundaries
5. **TDD Minimal & Realistic**: E2E for extended stories, skip trivial code

**Key Decisions Documented in research.md**:
- Brownfield: Template + scripts (4-pass analysis with confidence levels)
- Task Tracking: YAML + in-code tags + validation script
- Architecture: Meta-template requiring agent research (no embedded patterns)
- Context Management: Frontmatter indexes + section extraction (70% reduction)
- Testing: Realistic E2E covering extended stories (quality > quantity)

**No NEEDS CLARIFICATION Found**: All 10 user questions answered in spec.md Clarifications section.

**Output**: ✅ research.md (comprehensive, 50+ sources cited)

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

**Status**: ✅ COMPLETE

### 1. Data Model Design

Since this is a framework enhancement (not a traditional application), the "data model" represents file structures and workflow states rather than database entities.

**Output**: ✅ `data-model.md` created with 8 key entities:
1. Feature Specification (spec.md) - root document with YAML frontmatter
2. Implementation Plan (plan.md) - design artifacts and technical approach
3. Task List (tasks.md) - ordered tasks with files_affected, dependencies
4. Research Findings (research.md) - domain research with citations
5. File History Tracker (.specify/file-history.json) - renames and deprecations
6. Workflow Context (.specify/context.json) - state management across commands
7. Platform-Specific Agent Files (CLAUDE.md, WINDSURF.md, etc.) - platform instructions
8. Script Output (JSON) - standardized format for cross-platform scripts

### 2. API Contracts

**Not Applicable**: This is a framework/CLI tool without traditional API endpoints. 

**Alternative**: Script contracts defined via JSON schemas in data-model.md:
- analyze-codebase.sh → `{framework, version, dependencies, confidence}`
- check-dependencies.sh → `{vulnerabilities, outdated}`
- sync-tasks.sh → `{missing_task_tags, orphaned_todos, metadata_issues}`

**Validation**: Cross-platform parity tests ensure bash output === PowerShell output

### 3. Contract Tests

**Framework Validation Tests** (replace traditional contract tests):
- **Script Parity Tests**: Validate bash and PowerShell versions produce identical JSON
- **Template Rendering Tests**: Validate conditional sections render correctly for novice/intermediate/expert tiers
- **Workflow Integration Tests**: Validate /specify → /clarify → /plan → /tasks → /implement flow
- **Governance Validation Tests**: Validate tag enforcement, metadata completeness, document relationships

**Test Strategy**: Manual validation via 15 acceptance scenarios (from spec.md) + automated parity tests

### 4. Quickstart & Integration Scenarios

**Output**: ✅ `quickstart.md` created with 6 scenarios:
1. **New Greenfield Project**: /specify → /clarify → /plan → /tasks flow
2. **Brownfield Project Analysis**: /analyze-brownfield with 4-pass workflow
3. **Cross-Platform Migration**: /migrate-platform (Windsurf → Cursor)
4. **Task & File Tracking**: sync-tasks.sh validation + file-history.json
5. **Dependency Intelligence**: check-dependencies.sh + breaking changes detection
6. **Complexity Tiers for Novices**: --level novice scaffolding

### 5. Agent File Update

**Output**: ✅ `.windsurf/rules/specify-rules.md` updated via `update-agent-context.sh`

**Changes**:
- Added language: Python 3.9+, Bash, PowerShell, Markdown
- Added framework: Python stdlib, requests, PyYAML, click
- Added storage: File system (.specify/), context.json, file-history.json, Git
- Added project type: Framework enhancement
- Preserved manual additions between markers
- Kept under 150 lines for token efficiency

**Platform-Specific Files Generated During init**:
- `.claude/CLAUDE.md` (for Claude Code)
- `.windsurf/rules/specify-rules.md` (for Windsurf)
- `.cursor/CURSOR.md` (for Cursor)
- `.roo/ROO.md` (for Roo Code)

### Constitution Re-Check

**Status**: ✅ ALL PRINCIPLES PASS (no changes from initial check)

1. ✅ Preserve <400 LOC CLI
2. ✅ Template-Driven, Agent-First Design
3. ✅ Cross-Platform Compatibility
4. ✅ NO Breaking Changes
5. ✅ Research-Driven Decisions

**Conclusion**: Design maintains constitutional compliance. No refactoring needed.

---

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:

The /tasks command will generate tasks.md organized by the 5 sectors identified in spec.md:

### Sector 1: Commands/Workflows (6 tasks)
- T001: Enhance `/specify` workflow with complexity tier detection
- T002: Update `/plan` workflow to use architecture-meta-template
- T003: Modify `/tasks` workflow for YAML metadata generation
- T004: Create `/analyze-brownfield` workflow (4-pass analysis)
- T005: Create `/validate-governance` workflow (tag/metadata checks)
- T006: Create `/migrate-platform` workflow (cross-platform file copy)

### Sector 2: Templates (8 tasks)
- T007: Add conditional sections to spec-template.md (novice/intermediate/expert)
- T008: Remove embedded patterns from plan-template.md, add meta-template reference
- T009: Add YAML frontmatter schema to tasks-template.md
- T010: Create brownfield-analysis.md (4-pass checklist)
- T011: Create agent-prompt-patterns.md (CoVe, Step-Back, Citations)
- T012: Create dependency-report.md (npm audit template)
- T013: Create testing-strategy.md (realistic TDD guidelines)
- T014: Create architecture-meta-template.md (research workflow)

### Sector 3: Scripts (26 tasks = 13 bash + 13 PowerShell)
- T015-T016: Modify check-prerequisites.{sh,ps1} with --validate-tags flag
- T017-T018: Create analyze-codebase.{sh,ps1} (tech stack detection)
- T019-T020: Create sync-tasks.{sh,ps1} (YAML ↔ tags ↔ git validation)
- T021-T022: Create validate-tags.{sh,ps1} (scan missing tags)
- T023-T024: Create inject-tags.{sh,ps1} (auto-add with confirmation)
- T025-T026: Create check-dependencies.{sh,ps1} (npm audit/pip check)
- T027-T028: Create detect-breaking-changes.{sh,ps1} (changelog parsing)
- T029-T030: Create detect-framework.{sh,ps1} (framework detection)
- T031-T032: Create validate-context.{sh,ps1} (frontmatter validation)
- T033-T034: Create scaffold-feature.{sh,ps1} (tier boilerplate)
- T035-T036: Create extract-section.{sh,ps1} (section extraction)
- T037-T038: Create migrate-platform.{sh,ps1} (platform file copy)
- T039-T040: Create track-file-rename.{sh,ps1} (file history tracking)

### Sector 4: Governance (2 tasks)
- T041: Update AGENTS.md (4 platforms + brownfield + self-regulation)
- T042: Update memory/constitution.md (3 new principles)

### Sector 5: CLI (2 tasks)
- T043: Enhance specify_cli/__init__.py init command (GitHub download, platform detection)
- T044: Add flags to specify_cli/__init__.py check command (--tags, --dependencies, --tasks)

### Testing & Validation (10 tasks)
- T045: Create cross-platform parity tests (bash === PowerShell JSON)
- T046: Create template rendering tests (conditional sections)
- T047: Create workflow integration tests (/specify → /plan → /tasks)
- T048: Create governance validation tests (tag enforcement)
- T049: Manual validation: Scenario 1 (Greenfield project)
- T050: Manual validation: Scenario 2 (Brownfield analysis)
- T051: Manual validation: Scenario 3 (Platform migration)
- T052: Manual validation: Scenario 4 (Task tracking)
- T053: Manual validation: Scenario 5 (Dependency intelligence)
- T054: Manual validation: Scenario 6 (Complexity tiers)

**Ordering Strategy**:
1. **Templates First** (T007-T014): Foundation for other sectors
2. **Scripts** (T015-T040): Parallel execution possible [P] for bash/PowerShell pairs
3. **Workflows** (T001-T006): Depend on templates + scripts
4. **Governance** (T041-T042): Can be parallel with workflows [P]
5. **CLI** (T043-T044): Depends on all scripts existing
6. **Testing** (T045-T054): After implementation complete

**Dependencies**:
- T001-T006 depend on T007-T014 (workflows need templates)
- T001-T006 depend on T015-T040 (workflows call scripts)
- T043-T044 depend on T015-T040 (CLI calls scripts)
- T045-T054 depend on all implementation tasks

**Estimated Output**: 54 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

**Status**: ✅ NO VIOLATIONS - All constitutional principles satisfied

No complexity deviations to justify. All enhancements implemented within spec-kit's original architectural constraints:
- ✅ CLI remains <400 LOC
- ✅ Template-driven approach preserved
- ✅ No new Python analysis engines
- ✅ Cross-platform compatibility maintained
- ✅ Backward compatibility with existing projects

---

## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command) - ✅ research.md created
- [x] Phase 1: Design complete (/plan command) - ✅ data-model.md, quickstart.md, WINDSURF.md updated
- [x] Phase 2: Task planning complete (/plan command - describe approach only) - ✅ 54 tasks outlined
- [ ] Phase 3: Tasks generated (/tasks command) - **NEXT STEP**
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS (all 5 principles satisfied)
- [x] Post-Design Constitution Check: PASS (no design changes needed)
- [x] All NEEDS CLARIFICATION resolved (10 user questions answered in spec.md)
- [x] Complexity deviations documented (NONE - no violations)

**Artifacts Generated**:
- [x] specs/005-spec-kit-enhanced/spec.md (from /specify workflow)
- [x] specs/005-spec-kit-enhanced/research.md (Phase 0)
- [x] specs/005-spec-kit-enhanced/plan.md (this file)
- [x] specs/005-spec-kit-enhanced/data-model.md (Phase 1)
- [x] specs/005-spec-kit-enhanced/quickstart.md (Phase 1)
- [x] .windsurf/rules/specify-rules.md (Phase 1 - agent context)
- [x] .specify/context.json (workflow state tracking)

**Ready for**: `/tasks` command to generate detailed task breakdown

---

*Implementation plan follows original spec-kit principles: template-driven, agent-first, <400 LOC CLI*  
*Research-driven decisions documented in research.md (5 domains, 50+ sources)*  
*Next workflow: /tasks*
