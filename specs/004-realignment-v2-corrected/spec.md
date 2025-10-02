---
feature_id: "004"
title: "Spec-Kit Realignment Fork v2.0 - Back to Basics"
status: "draft"
created: "2025-09-30"
version: "2.0.0"
migrated_from: "003-based-on-the"
---

# Feature Specification: Spec-Kit Realignment Fork v2.0

**Input**: Based on the analysis report showing spec-kit has drifted from its original vision of being a simple template and script system for AI agents, create a fork that realigns with the original principles while incorporating the improvements from specs/001-improve-spec-kit/spec.md but simplified according to the original minimalist philosophy.

<!-- 
AGENT GUIDANCE (v2.0):
This spec migrates from 003 with corrected template/command system.
Focus on: Simple CLI, high-quality templates, agent-first design, template-driven guardrails.
Constitution: 7 principles from .specify/memory/constitution.md
-->

## User Scenarios & Testing

### Primary User Story
As a developer who believes in the original vision of spec-kit, I want a fork that returns to simple, elegant templates and scripts while preserving the valuable improvements from the enhancement initiative, so that I can efficiently develop both greenfield and brownfield projects with minimal tooling overhead, maximum AI agent autonomy, and augmented agent research capabilities.

### Acceptance Scenarios
1. **Given** a new project, **When** I run `specify init`, **Then** it MUST download templates from `templates/` to `.specify/` and set up structure within 3 seconds
2. **Given** a brownfield project, **When** agent uses brownfield-analysis.md template, **Then** it MUST perform 4-pass analysis (scan → research → validate → report) with confidence levels
3. **Given** framework-specific needs, **When** agent uses architecture-patterns.md, **Then** it MUST validate patterns against official docs for 10+ frameworks
4. **Given** artifact creation, **When** agent completes work, **Then** validation scripts MUST check compliance and report to user (non-blocking)
5. **Given** workflow commands, **When** I use `/specify`, `/plan`, `/tasks`, **Then** workflows MUST reference `.specify/templates/` correctly
6. **Given** cross-platform needs, **When** I use any of 10 AI platforms, **Then** commands MUST work with bash/PowerShell scripts
7. **Given** constitution, **When** planning features, **Then** agents MUST evaluate 7 principles and document deviations
8. **Given** simplicity focus, **When** examining CLI, **Then** total code MUST be <400 LOC with only init and check commands
9. **Given** quality integration, **When** running `specify check --quality`, **Then** agents MUST detect tools and report findings (non-blocking)
10. **Given** offline mode, **When** using `specify init --offline`, **Then** cached templates MUST be used without network

### Edge Cases
- Template updates: GitHub releases with version tagging, `specify init --template-version vX.Y.Z`
- Custom modifications: Users own `.specify/`, templates are starting points
- Offline usage: Templates cached in `~/.specify/cache/`, work offline after first init
- Backward compatibility: V1.x projects validate without changes

## Requirements

### Functional Requirements

#### Core CLI (FR-001 to FR-005)
- **FR-001**: System MUST provide CLI with exactly 2 commands: `init` and `check`
- **FR-002**: System MUST implement CLI in <400 lines of code total
- **FR-003**: System MUST support both `uv tool install` and `uvx` execution
- **FR-004**: CLI MUST work on Windows (PowerShell), macOS (bash), Linux (bash)
- **FR-005**: System MUST have only 4 dependencies: stdlib, requests, PyYAML, click

#### Template System (FR-006 to FR-010)
- **FR-006**: System MUST store source templates in package `templates/` directory
- **FR-007**: System MUST copy templates from `templates/` to `.specify/templates/` on init
- **FR-008**: System MUST include 7 templates: spec, plan, tasks, constitution, brownfield-analysis, architecture-patterns, agent-file
- **FR-009**: Templates MUST include agent guidance in HTML comments
- **FR-010**: System MUST support `--minimal` flag for essential templates only

#### Workflow Commands (FR-011 to FR-015)
- **FR-011**: System MUST provide workflow definitions in `templates/commands/` directory
- **FR-012**: Workflows MUST reference `.specify/templates/` for user space templates
- **FR-013**: `/plan` workflow MUST load `.specify/memory/constitution.md`
- **FR-014**: `/tasks` workflow MUST generate from `.specify/templates/tasks-template.md`
- **FR-015**: `/analyze` workflow MUST validate against constitution

#### Cross-Platform Compatibility (FR-016 to FR-020)
- **FR-016**: System MUST support 10 AI coding platforms
- **FR-017**: Templates MUST be platform-agnostic (markdown only)
- **FR-018**: Scripts MUST be provided in bash AND PowerShell
- **FR-019**: Validation output MUST be identical across platforms
- **FR-020**: System MUST auto-detect platform and use correct scripts

#### Brownfield Analysis (FR-021 to FR-024) - Agent-Augmented
- **FR-021**: Template MUST guide 4-pass analysis workflow
- **FR-022**: Agents MUST detect 8+ technology stacks (JS/TS, Python, Java, Ruby, Go, .NET, Rust, PHP)
- **FR-023**: Agents MUST report findings with confidence levels (High/Med/Low)
- **FR-024**: Template MUST include research checklist for validation

#### Architecture Guidance (FR-025 to FR-028) - Hybrid Research
- **FR-025**: Template MUST document 10+ framework patterns
- **FR-026**: Agents MUST validate patterns against official documentation
- **FR-027**: Template MUST include validation questions for agents
- **FR-028**: Agents MUST check for version-specific breaking changes

#### Constitutional Principles (FR-029 to FR-035)
- **FR-029**: System MUST store constitution in `.specify/memory/constitution.md`
- **FR-030**: Constitution MUST define 7 principles: Cross-Platform, Multi-Installation, Template-Driven, Agent-Native, Simplicity, Governance Balance, Backward Compatibility
- **FR-031**: `/plan` workflow MUST evaluate constitution before Phase 0
- **FR-032**: Agents MUST document principle violations in plan.md Complexity Tracking
- **FR-033**: Constitution violations MUST require justification or simplification
- **FR-034**: Constitution MUST include evaluation criteria for each principle
- **FR-035**: Constitution MUST be copied from source on init

#### Validation Scripts (FR-036 to FR-041)
- **FR-036**: Scripts MUST validate structure, naming, frontmatter
- **FR-037**: Scripts MUST output [INFO], [WARN], [ERROR] format
- **FR-038**: Scripts MUST exit with code 0 (non-blocking)
- **FR-039**: Bash and PowerShell scripts MUST produce identical output
- **FR-040**: Scripts MUST be stored in `.specify/scripts/bash/` and `.specify/scripts/powershell/`
- **FR-041**: `specify check` MUST execute platform-appropriate scripts

#### Quality Tool Integration (FR-042 to FR-047)
- **FR-042**: System MUST detect project type (JS, Python, Java, etc.)
- **FR-043**: Agents MUST check for standard tools (eslint, pylint, etc.)
- **FR-044**: `specify check --quality` MUST run available tools
- **FR-045**: Quality checks MUST be non-blocking (exit 0)
- **FR-046**: System MUST categorize findings (critical/error/warning/info)
- **FR-047**: System MUST report findings to user for decision

### Non-Functional Requirements

#### Performance
- **NFR-001**: `specify init` MUST complete in <3 seconds
- **NFR-002**: `specify check` MUST complete in <1 second
- **NFR-003**: Template copying MUST be <200ms
- **NFR-004**: Memory footprint MUST be <50MB

#### Usability
- **NFR-005**: CLI help text MUST be clear and concise
- **NFR-006**: Error messages MUST be actionable
- **NFR-007**: Templates MUST include examples
- **NFR-008**: Workflows MUST be self-documenting

#### Maintainability
- **NFR-009**: CLI code MUST have <10 cyclomatic complexity per function
- **NFR-010**: Templates MUST be versioned
- **NFR-011**: System MUST support template updates via `specify init --force`
- **NFR-012**: Code MUST have type hints (Python 3.9+)

#### Security
- **NFR-013**: System MUST NOT execute untrusted code
- **NFR-014**: Template downloads MUST verify checksums (future)
- **NFR-015**: Scripts MUST NOT modify files outside project directory
- **NFR-016**: Offline mode MUST work without network access

## Key Entities

### Template System
- **Source Location**: `templates/` in package
- **User Location**: `.specify/templates/` after init
- **Version**: Tracked in `.specify/.version`
- **Updates**: Via GitHub Releases or `--force` flag

### Workflow Commands
- **Location**: `templates/commands/*.md`
- **Format**: YAML frontmatter + markdown instructions
- **Execution**: By AI agents reading instructions
- **Scripts**: Reference `.specify/scripts/` for validation

### Constitution
- **Source**: `templates/constitution.md`
- **User Copy**: `.specify/memory/constitution.md`
- **Principles**: 7 non-negotiable rules
- **Usage**: Evaluated in `/plan` workflow

### Validation Scripts
- **Languages**: Bash (Unix) + PowerShell (Windows)
- **Purpose**: Validate structure, naming, frontmatter
- **Output**: Structured [LEVEL] messages
- **Execution**: Via `specify check` command

## Implementation Notes

### Migration from 003
- Preserve valid spec content (requirements, scenarios)
- Update template system (source vs user space)
- Fix workflow command paths
- Add constitution integration
- Complete template set (7 templates)

### What Changed in v2.0
1. **Template Architecture**: Source (`templates/`) vs User (`.specify/`)
2. **Constitution**: Now in `.specify/memory/constitution.md`
3. **Workflows**: Updated paths to `.specify/templates/`
4. **New Templates**: constitution.md, brownfield-analysis.md, architecture-patterns.md
5. **Agent Guidance**: HTML comments in all templates

### Critical Success Factors
1. Template system MUST copy correctly
2. Workflows MUST reference correct paths
3. Constitution MUST be accessible
4. Tests MUST pass (51/66 currently)
5. CLI MUST stay <400 LOC

---

## Review & Acceptance Checklist

### Content Quality
- [x] No implementation details
- [x] Focused on user value
- [x] All mandatory sections complete
- [x] Constitution principles addressed

### Requirement Completeness  
- [x] No [NEEDS CLARIFICATION] markers
- [x] Requirements testable and unambiguous
- [x] Success criteria measurable
- [x] Scope clearly bounded
- [x] Dependencies identified (migration from 003)

### v2.0 Specific
- [x] Template architecture documented
- [x] Workflow paths corrected
- [x] Constitution integration specified
- [x] Migration path clear

---

## Clarifications

### Session 1: 2025-09-30

**Q1: Template Distribution Strategy**  
**Answer**: Hybrid - Embedded fallback + optional GitHub downloads (most flexible)  
**Rationale**: 
- Templates embedded in package at `templates/` for offline reliability
- GitHub Releases used for updates (`specify init --force` or new versions)
- First `init` uses embedded templates immediately (<200ms target)
- Optional: Check GitHub for newer versions, cache in `~/.specify/cache/`
- Offline mode always works with embedded templates
- **Implementation**: FR-007 clarified - copy from embedded `templates/`, optionally update from GitHub

**Q2: Workflow Command Execution Model**  
**Answer**: Agent-read only - Commands are markdown documentation for agents to interpret and execute  
**Rationale**:
- **FR-001 "exactly 2 commands"** means CLI Python code has ONLY `specify init` and `specify check`
- Workflow files (`/specify`, `/plan`, `/tasks`, etc.) are **NOT CLI commands** - they are markdown instructions in `templates/commands/*.md`
- AI agents read these markdown files and execute the bash/PowerShell scripts referenced within
- Different AI platforms handle this differently:
  - Some execute scripts via terminal/CLI natively
  - Some read description and decide which stage to run commands
  - Most can execute scripts when instructed in markdown
- Scripts get appended to `.specify/scripts/` folder during init
- This keeps CLI <400 LOC because workflow orchestration is in markdown, not Python
- **Architecture**: CLI = Python code (init/check), Workflows = Agent-read markdown + bash/PS scripts
- **Implementation**: No CLI subcommands for workflows, agents parse markdown and execute scripts directly

**Q3: Script Types and Organization**  
**Answer**: Interpretation B - Validation + Workflow Helper Scripts  
**Rationale**:
- `.specify/scripts/` contains BOTH validation scripts AND workflow helper scripts
- **Validation Scripts (3)**: validate-structure, validate-naming, validate-frontmatter
  - Called by `specify check` command
  - Output: [INFO], [WARN], [ERROR] format
  - Must have bash + PowerShell versions with identical output
- **Workflow Helper Scripts (6+)**: Support agent workflow execution
  - `check-prerequisites.sh` - Get FEATURE_DIR, FEATURE_SPEC, AVAILABLE_DOCS (used by /clarify, /tasks, /analyze)
  - `setup-plan.sh` - Initialize planning artifacts (used by /plan)
  - `create-new-feature.sh` - Create feature branch and spec file (used by /specify)
  - `update-agent-context.sh` - Update agent-specific files (used by /plan Phase 1)
  - Additional helpers as workflows require
- **Total Scripts**: ~9 scripts × 2 platforms = ~18 files
- **Testing**: All scripts must have cross-platform parity tests
- **Implementation**: Phase 3.5 creates all scripts, not just validation ones

**Q4: Workflow Helper Script JSON Output Format**  
**Answer**: Standardized JSON contract with consistent fields across all helper scripts  
**Rationale**:
- All helper scripts with `--json` flag MUST output valid JSON to stdout
- Field names MUST be consistent between bash and PowerShell versions
- All paths MUST be absolute (no relative paths)
- **check-prerequisites.sh JSON**: `REPO_ROOT`, `BRANCH`, `FEATURE_DIR`, `FEATURE_SPEC`, `IMPL_PLAN`, `TASKS`, `AVAILABLE_DOCS` (array)
- **setup-plan.sh JSON**: `REPO_ROOT`, `BRANCH`, `FEATURE_SPEC`, `IMPL_PLAN`, `SPECS_DIR`
- **create-new-feature.sh JSON**: `REPO_ROOT`, `BRANCH_NAME`, `SPEC_FILE`, `FEATURE_DIR`
- Agents parse this JSON to get paths for workflow execution
- **Critical**: Windows paths use forward slashes in JSON for cross-platform consistency
- **Implementation**: Document JSON schema for each script, include in tests

**Q5: Script Distribution and Creation Strategy**  
**Answer**: Approach A - Embedded Scripts (same pattern as templates)  
**Rationale**:
- Scripts embedded in package at `scripts/bash/` and `scripts/powershell/`
- During `specify init`: Copy `scripts/` → `.specify/scripts/` (same as template copying)
- **Package structure**: `scripts/bash/*.sh` and `scripts/powershell/*.ps1` (18 files total)
- Maintenance via GitHub repository (original spec-kit pattern)
- Users can customize their `.specify/scripts/` after init
- Keeps init.py simple (~20 LOC for script copying)
- Aligns with Q1 hybrid template distribution strategy
- **Implementation**: Add `scripts/` directory to package, update init.py to copy scripts like templates

### Summary of Clarifications

**Architecture Decisions Made**:
1. **Template Distribution**: Hybrid approach - embedded in package with optional GitHub updates
2. **Workflow Execution**: Agent-read markdown files (NOT CLI subcommands) - preserves <400 LOC limit
3. **Script Organization**: Validation (3) + Workflow Helpers (6+) = ~18 files in `.specify/scripts/`
4. **JSON Contract**: Standardized format for all helper scripts with absolute paths
5. **Script Distribution**: Embedded in package `scripts/` directory, copied on init (same as templates)

**Impact on Requirements**:
- FR-001 clarified: CLI has ONLY `init` and `check` Python commands (workflows are markdown)
- FR-036-041 expanded: Validation scripts are subset of total scripts
- FR-007 clarified: Templates AND scripts copied from package on init
- Package structure expanded: `templates/` AND `scripts/` directories

**What Changed from Original Understanding**:
- ❌ **Wrong (003)**: Workflows might be CLI subcommands → Would exceed 400 LOC
- ✅ **Correct (004)**: Workflows are markdown files agents read and execute via scripts
- ❌ **Wrong (003)**: Only 3 validation scripts needed
- ✅ **Correct (004)**: Need ~9 scripts (3 validation + 6 helpers) for complete workflow support
- ❌ **Wrong (003)**: Script JSON format undefined
- ✅ **Correct (004)**: Standardized JSON contract documented

**Confidence Level**: ✅ **HIGH** - All major architectural ambiguities resolved

---

**Status**: ✅ Clarification complete. Spec ready for `/plan` workflow.
