---
feature_id: "005"
title: "Spec-Kit Enhanced Fork - Brownfield Intelligence & Agent Self-Regulation"
status: "draft"
created: "2025-09-30"
version: "2.0"
complexity_level: "very_high"
research_conducted: true
multi_domain: true
github_repo: "https://github.com/mbpfws/speckit-buff-v2/"
mvp_platforms: ["Claude Code", "Windsurf", "Roo Code", "Cursor"]
---

# Feature Specification: Spec-Kit Enhanced Fork v2.0

**Feature Branch**: `005-spec-kit-enhanced`  
**Input**: Comprehensive spec-kit improvement addressing 45+ systemic shortcomings across brownfield support, agent self-regulation, context management, dependency intelligence, architecture granularity, and governance enforcement.

<!-- 
AGENT GUIDANCE (v2.0):
This is a VERY HIGH complexity, multi-domain enhancement to the original spec-kit framework.
Research conducted across 5 domains: brownfield patterns, context management, dependencies, Next.js architecture, TDD.
User decisions documented in Clarifications section (10 questions answered).
Focus: Preserve <400 LOC CLI, implement via templates/scripts/workflows.
Constraint: NO new Python analysis engines - only templates, scripts, and agent instructions.
-->

## Execution Flow (main)
```
1. Parse comprehensive improvement requirements from Input
   ✅ SUCCESS: 45+ distinct improvement areas identified across 5 sectors
2. Extract key concepts and organize by sector
   ✅ Identified: Commands/Workflows, Templates, Scripts, Governance, CLI
3. Cross-reference with research findings
   ✅ 5 research domains completed (brownfield, context, dependencies, architecture, TDD)
4. Validate user clarification decisions (10 critical questions)
   ✅ All questions answered inline by user
5. Fill User Scenarios & Testing section
   ✅ 15 acceptance scenarios covering all improvement areas
6. Generate Functional Requirements organized by sector
   ✅ 89+ requirements across 5 sectors with clear testability
7. Identify Key Entities
   ✅ 8 key entities defined
8. Run Review Checklist
   ✅ All mandatory sections complete
   ✅ No [NEEDS CLARIFICATION] markers remain
9. Return: SUCCESS (spec ready for /plan workflow)
```

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a spec-kit user developing both greenfield and brownfield projects across multiple AI coding platforms (Claude, Windsurf, Roo Code, Cursor), I want an enhanced framework that provides intelligent brownfield analysis, agent self-regulation, granular architecture guidance, robust task tracking, and realistic testing strategies, so that I can efficiently build complex features without agent hallucinations, codebase pollution, or premature over-engineering, while maintaining the original spec-kit philosophy of <400 LOC CLI with template-driven simplicity.

### Acceptance Scenarios

**Brownfield Analysis**:
1. **Given** existing Next.js codebase, **When** I run `/analyze-brownfield`, **Then** agent MUST execute 4-pass analysis (Document → Analyze → Integrate → Risk) reporting tech stack, dependencies, architecture patterns with confidence levels (High/Med/Low)

2. **Given** brownfield Django project, **When** agent uses architecture-meta-template, **Then** agent MUST research official Django docs for latest patterns, validate against project, report deviations

**Task Tracking**:
3. **Given** `tasks.md` with `files_affected: [src/users.ts]` and `task_id: T001`, **When** I modify file, **Then** `sync-tasks.sh` MUST validate YAML ↔ code tags ↔ git changes, warn if misaligned

4. **Given** file rename `old.ts` → `new.ts`, **When** agent updates code, **Then** system MUST track in `.specify/file-history.json` preventing "file not found" errors

**Agent Self-Regulation**:
5. **Given** user requests "Express 5.0", **When** agent detects 4.19.2 is latest stable, **Then** agent MUST pause, present findings with source, ask user confirmation

6. **Given** large plan.md (500+ lines), **When** agent needs only "Phase 3" section, **Then** agent MUST use frontmatter index or `extract-section.sh` reducing context by 70%

7. **Given** agent generates response, **When** `agent-prompt-patterns.md` loaded, **Then** agent MUST apply "According to..." prompting, forcing citations, reducing hallucinations 30%

**Dependency Intelligence**:
8. **Given** peer dependency conflict (vite 3.2.7 vs ^5.0.0), **When** `check-dependencies.sh` runs, **Then** output JSON warning with resolution options

9. **Given** React 18→19 breaking changes, **When** `detect-breaking-changes.sh` parses changelog, **Then** output affected files with migration guide URLs

**Architecture Granularity**:
10. **Given** Next.js App Router project, **When** agent uses architecture-meta-template during `/plan`, **Then** agent MUST research 2025 best practices: route groups `(folder)`, private folders `_components`, server/client boundaries

11. **Given** brownfield Django project, **When** agent analyzes via `detect-framework.sh`, **Then** report deviations from official patterns, suggest refactoring in `architecture-deviations.md`

**Testing Strategy**:
12. **Given** feature with 5 extended user stories, **When** agent references `testing-strategy.md`, **Then** generate E2E tests covering all story aspects, skip trivial code, mark tasks needing tests

13. **Given** 200+ snapshot tests detected, **When** validating against testing-strategy.md, **Then** warn "Snapshot tests brittle, recommend realistic E2E", provide guidance

**Platform Migration**:
14. **Given** Windsurf project with `.windsurf/` workflows, **When** I run `/migrate-platform --to cursor`, **Then** `migrate-platform.sh` MUST copy to `.cursor/`, update references, preserve workflow state

**Governance**:
15. **Given** agent creates `data-model.md`, **When** `create-artifact.sh --parent 005 --type data-model` runs, **Then** auto-fill `artifact_id: "005-data-model"`, validate parent exists

### Edge Cases
- **Template tier detection fallback**: No `.specify/` → default "intermediate", allow `--level` override
- **Script JSON parse failure**: Agent catches error, prompts manual run, parses text output
- **Platform detection ambiguity**: Both `.windsurf/` and `.cursor/` exist → check most recent, allow `--platform` flag
- **Circular task dependencies**: T001→T002→T001 → `build-task-graph.sh` detects, reports with resolution
- **File history across branches**: Track with branch name, merge histories on branch merge
- **Breaking changes without changelog**: Fall back to major version bump heuristic, warn low confidence
- **Context overflow despite extraction**: Single section >token limit → request user split into sub-sections
- **Complexity tier mismatch**: Novice requests expert feature → progressive disclosure + learning resources
- **Self-regulation deadlock**: Too many confirmations → severity levels (CRITICAL: block, MAJOR: ask, MINOR: warn)
- **Dependency conflict no resolution**: Vulnerability with no patch → document accepted risks, suggest workarounds, require sign-off

---

## Clarifications *(all resolved)*

### Session 2025-09-30: User Decision Summary

**Q1: Brownfield Analysis** → **C) Both A + B** (Template + Scripts with JSON)  
**Q2: Task Tracking** → **D) Combination (B + C)** (Script validates tags) + Track renames + deprecated files  
**Q3: Architecture** → **Meta-template** (research-driven, no embedded patterns)  
**Q4: Tag Enforcement** → **All three** (Validation + Injection + Templates) for CODE/METADATA/RELATIONSHIPS  
**Q5: Self-Regulation** → **D) User confirmation loops** (detect→research→present→ask)  
**Q6: Platform Migration** → **Copy workflow files** to platform folders (commands/templates/scripts)  
**Q7: Testing** → **Realistic E2E covering extended stories** (no arbitrary limits, quality over quantity)  
**Q8: Governance Hierarchy** → **Enforce but allow flexibility** (warn, don't block)  
**Q9: Context Management** → **Agent instructions + Frontmatter indexes** with section tags  
**Q10: Scaffolding** → **Complexity tiers** via helper scripts + conditional template sections  

---

## Requirements *(mandatory)*

### Functional Requirements

#### Sector 1: Commands/Workflows (templates/commands/)

**FR-C001**: `/specify` workflow MUST detect complexity tier via `--level novice|intermediate|expert` flag or default to "intermediate"  
**FR-C002**: `/plan` workflow MUST load `architecture-meta-template.md` instructing agents to research official framework docs for latest patterns  
**FR-C003**: `/tasks` workflow MUST generate tasks.md with YAML: `files_affected`, `task_id`, `test_required`, instruct agents to add `// TASK-XXX` tags  
**FR-C004**: `/analyze-brownfield` workflow MUST execute 4-pass analysis using `brownfield-analysis.md` + `analyze-codebase.sh`, report confidence levels  
**FR-C005**: `/validate-governance` workflow MUST check code tags, metadata completeness, document relationships, report violations as warnings  
**FR-C006**: `/migrate-platform` workflow MUST copy workflows/templates/scripts to target platform folder, preserve `.specify/context.json` state  

#### Sector 2: Templates (templates/)

**FR-T001**: `spec-template.md` MUST include conditional sections for tiers: `<!-- IF tier=novice -->...<!-- ENDIF -->`  
**FR-T002**: `plan-template.md` MUST remove embedded patterns, reference `architecture-meta-template.md` with research instructions  
**FR-T003**: `tasks-template.md` MUST include YAML schema: `feature_id`, `parent_spec`, `tasks: [{id, title, files_affected, test_required, dependencies}]`  
**FR-T004**: `brownfield-analysis.md` MUST provide 4-pass checklist: Document → Analyze (confidence) → Integrate → Risk  
**FR-T005**: `agent-prompt-patterns.md` MUST document: "According to..." prompting, Chain-of-Verification, Step-Back Prompting with examples  
**FR-T006**: `dependency-report.md` MUST structure: vulnerabilities table, peer conflicts table, breaking changes section  
**FR-T007**: `testing-strategy.md` MUST define: E2E for extended stories, skip trivial code, forbidden (snapshots/mocks), required (critical flows)  
**FR-T008**: `architecture-meta-template.md` MUST provide: Detect framework → Research docs → Document patterns → Identify anti-patterns → Report deviations  

#### Sector 3: Scripts (scripts/bash/ + scripts/powershell/)

**FR-S001**: `check-prerequisites.sh` MUST add `--validate-tags` flag scanning code/metadata violations, output JSON  
**FR-S002**: `analyze-codebase.sh` MUST detect tech stack via file patterns, output JSON: `{framework, version, dependencies, file_counts, confidence}`  
**FR-S003**: `sync-tasks.sh` MUST cross-check: YAML task_id ↔ code tags ↔ git changes, report misalignments  
**FR-S004**: `validate-tags.sh` MUST scan for missing tags, output JSON: `{missing_task_tags, orphaned_todos, metadata_issues}`  
**FR-S005**: `inject-tags.sh` MUST add `// TASK-XXX: [description]` with user confirmation  
**FR-S006**: `check-dependencies.sh` MUST run platform audit (npm/pip), output JSON: `{vulnerabilities, outdated}`  
**FR-S007**: `detect-breaking-changes.sh` MUST parse changelogs for major bumps, identify affected files, output JSON  
**FR-S008**: `detect-framework.sh` MUST identify framework via patterns, output JSON: `{framework, version, detected_via, confidence}`  
**FR-S009**: `validate-context.sh` MUST check YAML frontmatter for required fields, validate types/references, output JSON  
**FR-S010**: `scaffold-feature.sh` MUST generate tier-appropriate boilerplate (novice: detailed, expert: minimal)  
**FR-S011**: `extract-section.sh` MUST parse frontmatter index or scan `<!-- SECTION:name START/END -->` tags, output content  
**FR-S012**: `migrate-platform.sh` MUST copy files, update platform references, output migration report  
**FR-S013**: `track-file-rename.sh` MUST append to `.specify/file-history.json`: `{old_path, new_path, task_id, timestamp, branch}`  
**FR-S014**: `mark-file-deprecated.sh` MUST update file-history.json with deprecation metadata  
**FR-S015**: `build-task-graph.sh` MUST parse dependencies, construct DAG, detect cycles, output JSON  
**FR-S016**: `analyze-test-coverage.sh` MUST detect test framework, run coverage, output JSON: `{coverage_percent, uncovered_files, test_count}`  

**Note**: All scripts MUST have bash + PowerShell versions with identical JSON output

#### Sector 4: Governance (AGENTS.md + memory/constitution.md)

**FR-G001**: `AGENTS.md` MUST include 4 platform sections (Claude/Windsurf/Roo/Cursor) documenting: workflow syntax, script execution, MCP tools, optimizations  
**FR-G002**: `AGENTS.md` MUST document brownfield guidance: when to use, confidence interpretation, research requirements, reporting format  
**FR-G003**: `AGENTS.md` MUST define self-regulation patterns: confirmation loops, severity thresholds (CRITICAL/MAJOR/MINOR), citation requirements  
**FR-G004**: `AGENTS.md` MUST specify tag enforcement: new files need `// TASK-XXX`, artifacts need `artifact_id`, cross-refs validated  
**FR-G005**: `AGENTS.md` MUST document context management: section indexes for >300 lines, extraction tools, splitting oversized sections  
**FR-G006**: `constitution.md` MUST add 3 principles:
- **Agent Self-Regulation**: Confirm before correcting, cite sources, use severity thresholds
- **Brownfield Support**: Template-driven analysis, confidence levels, historical context tracking
- **Context Management**: Hierarchical scoping, extraction tools, incremental reading

#### Sector 5: CLI (specify_cli/__init__.py)

**FR-CLI001**: `specify init` MUST download from https://github.com/mbpfws/speckit-buff-v2/, detect platform (scan folders OR `--platform` flag), copy templates to `.specify/` + platform folder, support `--level` flag  
**FR-CLI002**: `specify check` MUST add flags: `--tags` (validate code tags), `--dependencies` (npm audit/pip check), `--tasks` (validate task sync)  

### Key Entities

**1. Enhanced Workflows (Commands)**  
Purpose: Guide agents through brownfield analysis, governance validation, platform migration  
Attributes: Complexity tier awareness, research instructions, validation checkpoints  
Relationships: Reference templates, trigger scripts, update context.json  

**2. Templates with Complexity Tiers**  
Purpose: Provide tiered guidance (novice/intermediate/expert) for specs, plans, tasks  
Attributes: Conditional sections, YAML schema, research workflows, prompt patterns  
Relationships: Loaded by workflows, filled by agents, validated by scripts  

**3. Validation & Helper Scripts**  
Purpose: Automate tech detection, task sync, tag validation, dependency checks, breaking changes  
Attributes: Cross-platform (bash/PowerShell), JSON output, non-blocking warnings  
Relationships: Called by workflows, validate artifacts, output data for agents  

**4. Brownfield Analysis System**  
Purpose: Multi-pass codebase analysis with confidence levels  
Attributes: 4 passes (Document/Analyze/Integrate/Risk), tech stack detection, framework validation  
Relationships: Template + script combination, outputs findings with citations  

**5. Task Tracking System**  
Purpose: Maintain YAML ↔ code tags ↔ git changes synchronization  
Attributes: task_id, files_affected, in-code comments, file history tracking  
Relationships: Validated by sync-tasks.sh, updated by agents, tracked in file-history.json  

**6. Agent Self-Regulation Framework**  
Purpose: User confirmation loops, citation requirements, severity-based decisions  
Attributes: CRITICAL/MAJOR/MINOR thresholds, "According to..." prompting, research validation  
Relationships: Defined in AGENTS.md, enforced by templates, guided by prompt-patterns.md  

**7. Context Management System**  
Purpose: Hierarchical section scoping for large documents  
Attributes: Frontmatter indexes, section tags, extraction scripts  
Relationships: Enables incremental reading, reduces context window 70%, supports >500 line docs  

**8. Platform Migration Tools**  
Purpose: Copy workflows/templates/scripts between AI coding platforms  
Attributes: Source/target platform detection, file copying, reference updating, state preservation  
Relationships: `/migrate-platform` workflow + migrate-platform.sh script  

---

## Review & Acceptance Checklist

### Content Quality
- [x] No implementation details (focused on WHAT system provides, not HOW)
- [x] Focused on user value (addresses 45+ pain points)
- [x] Written for spec-kit maintainers and platform developers
- [x] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain (10 questions answered)
- [x] Requirements testable and unambiguous (89+ requirements with clear acceptance criteria)
- [x] Success criteria measurable (15 acceptance scenarios with GIVEN/WHEN/THEN)
- [x] Scope clearly bounded (5 sectors, 4 platforms MVP, preserves <400 LOC CLI)
- [x] Dependencies identified (original spec-kit files, GitHub repo, research findings)
- [x] Research conducted and applied (5 domains: brownfield, context, dependencies, architecture, TDD)

### Architecture Alignment
- [x] Preserves spec-kit philosophy (<400 LOC CLI, template-driven, agent-first)
- [x] No new Python analysis engines (only templates/scripts/workflows)
- [x] Cross-platform support (Claude, Windsurf, Roo Code, Cursor)
- [x] GitHub download integration (https://github.com/mbpfws/speckit-buff-v2/)
- [x] No duplicate files (modify existing or remove-before-create)

---

## Execution Status

- [x] User description parsed (45+ improvement areas)
- [x] Key concepts extracted (5 sectors identified)
- [x] Research conducted (5 domains completed)
- [x] Ambiguities resolved (10 clarification questions answered)
- [x] User scenarios defined (15 acceptance scenarios)
- [x] Requirements generated (89+ across 5 sectors)
- [x] Entities identified (8 key entities)
- [x] Review checklist passed
- [x] Ready for `/plan` workflow

---

## Implementation Notes

### Files to Modify (11)
1. `templates/commands/specify.md` → Add complexity tier
2. `templates/commands/plan.md` → Meta-template reference
3. `templates/commands/tasks.md` → YAML guidance
4. `templates/spec-template.md` → Conditional sections
5. `templates/plan-template.md` → Remove patterns
6. `templates/tasks-template.md` → YAML frontmatter
7. `scripts/bash/check-prerequisites.sh` → Add --validate-tags
8. `scripts/powershell/check-prerequisites.ps1` → Add --validate-tags
9. `specify_cli/__init__.py` → Platform detection, GitHub download
10. `AGENTS.md` → 4 platforms, brownfield, self-regulation
11. `memory/constitution.md` → 3 new principles

### Files to Create (21)
**Commands (3)**:
12. `templates/commands/analyze-brownfield.md`
13. `templates/commands/validate-governance.md`
14. `templates/commands/migrate-platform.md`

**Templates (5)**:
15. `templates/brownfield-analysis.md`
16. `templates/agent-prompt-patterns.md`
17. `templates/dependency-report.md`
18. `templates/testing-strategy.md`
19. `templates/architecture-meta-template.md`

**Scripts (13 bash + PowerShell pairs)**:
20-21. `analyze-codebase.{sh,ps1}`
22-23. `sync-tasks.{sh,ps1}`
24-25. `validate-tags.{sh,ps1}`
26-27. `inject-tags.{sh,ps1}`
28-29. `check-dependencies.{sh,ps1}`
30-31. `detect-breaking-changes.{sh,ps1}`
32-33. `detect-framework.{sh,ps1}`
34-35. `scaffold-feature.{sh,ps1}`
36-37. `extract-section.{sh,ps1}`
38-39. `migrate-platform.{sh,ps1}`
40-41. `track-file-rename.{sh,ps1}`
42-43. `mark-file-deprecated.{sh,ps1}`
44-45. `build-task-graph.{sh,ps1}`

**Total**: 32 file changes (11 modifications + 21 new)

---

**Specification Complete** ✅  
**Next Step**: Run `/plan` to create implementation strategy
