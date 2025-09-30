# Tasks: Spec-Kit Realignment Fork v2.0

**Input**: Design documents from `specs/004-realignment-v2-corrected/`  
**Prerequisites**: plan.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

<!-- 
AGENT GUIDANCE (v2.0):
Tasks T001-T029 already complete (Setup, Tests, Core, Templates).
This file contains T030+ (remaining implementation).
Mark [P] = parallel execution (different files, no dependencies).
Follow TDD: Tests before implementation.
-->

## Summary

**Total Tasks**: 50  
**Completed**: T001-T050 (50 tasks) ✅  
**Remaining**: T051-T062 (12 optional tasks)  
**Current Phase**: 3.6 (Integration Complete)

---

## Phase 3.1: Setup ✅ (COMPLETE)

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize pyproject.toml with 4 dependencies
- [x] T003 [P] Configure pytest and test infrastructure
- [x] T004 [P] Configure linting (.flake8) and formatting
- [x] T005 [P] Create README and initial documentation

---

## Phase 3.2: Tests First (TDD) ✅ (COMPLETE)

- [x] T006 [P] Contract test: cli-init.yaml (tests/contract/test_cli_init.py)
- [x] T007 [P] Contract test: cli-check.yaml (tests/contract/test_cli_check.py)
- [x] T008 [P] Contract test: validation-api.yaml (tests/contract/test_validation_api.py)
- [x] T009 [P] Integration test: Greenfield init (tests/integration/test_greenfield_init.py)
- [x] T010 [P] Integration test: Brownfield analysis (tests/integration/test_brownfield_analysis.py)
- [x] T011 [P] Integration test: Architecture patterns (tests/integration/test_architecture_patterns.py)
- [x] T012 [P] Integration test: Artifact validation (tests/integration/test_artifact_validation.py)
- [x] T013 [P] Integration test: Multi-platform (tests/integration/test_multi_platform.py)
- [x] T014 [P] Integration test: Quality integration (tests/integration/test_quality_integration.py)
- [x] T015 [P] Integration test: CLI simplicity (tests/integration/test_cli_simplicity.py)
- [x] T016 [P] Integration test: Cross-platform scripts (tests/integration/test_cross_platform_scripts.py)
- [x] T017 [P] Integration test: Offline usage (tests/integration/test_offline_usage.py)
- [x] T018 [P] Integration test: Backward compatibility (tests/integration/test_backward_compatibility.py)

---

## Phase 3.3: Core CLI Implementation ✅ (COMPLETE)

- [x] T019 [P] Implement template_loader.py (38 LOC)
- [x] T020 [P] Implement validators.py (30 LOC)
- [x] T021 Implement cli.py main entry point (13 LOC)
- [x] T022 Implement commands/init.py (78 LOC)
- [x] T023 Implement commands/check.py (65 LOC)

**Total CLI LOC**: 224 / 400 (56% of budget)

---

## Phase 3.4: Template Creation ✅ (COMPLETE)

- [x] T024 [P] Create templates/spec-template.md with YAML frontmatter
- [x] T025 [P] Create templates/plan-template.md with v2.0 guidance
- [x] T026 [P] Create templates/tasks-template.md (verified complete)
- [x] T027 [P] Create templates/constitution.md (7 principles)
- [x] T028 [P] Create templates/brownfield-analysis.md (4-pass workflow)
- [x] T029 [P] Create templates/architecture-patterns.md (10+ frameworks)

---

## Phase 3.5: Validation Scripts (T030-T047)

**All bash scripts must have PowerShell equivalents with identical output**

### Bash Validation Scripts

- [x] **T030** [P] Create scripts/bash/validate-structure.sh
  - File: `scripts/bash/validate-structure.sh`
  - Check: .specify/ directory structure, specs/ exists, folder naming {id}-{slug}
  - Output: `[INFO]`, `[WARN]`, `[ERROR]` messages
  - Exit: code 0 (non-blocking)
  - ~50 LOC

- [x] **T031** [P] Create scripts/bash/validate-naming.sh
  - File: `scripts/bash/validate-naming.sh`
  - Check: File naming conventions (kebab-case, no spaces)
  - Output: `[INFO]`, `[WARN]`, `[ERROR]` messages
  - Exit: code 0 (non-blocking)
  - ~40 LOC

- [x] **T032** [P] Create scripts/bash/validate-frontmatter.sh
  - File: `scripts/bash/validate-frontmatter.sh`
  - Check: YAML frontmatter presence and required fields
  - Output: `[INFO]`, `[WARN]`, `[ERROR]` messages
  - Exit: code 0 (non-blocking)
  - ~60 LOC

### Bash Helper Scripts

- [x] **T033** [P] Create scripts/bash/check-prerequisites.sh
  - File: `scripts/bash/check-prerequisites.sh`
  - Flags: `--json`, `--paths-only`, `--require-tasks`, `--include-tasks`
  - Output JSON: REPO_ROOT, BRANCH, FEATURE_DIR, FEATURE_SPEC, IMPL_PLAN, TASKS, AVAILABLE_DOCS
  - Used by: /clarify, /tasks, /analyze, /implement workflows
  - ~80 LOC

- [x] **T034** [P] Create scripts/bash/setup-plan.sh
  - File: `scripts/bash/setup-plan.sh`
  - Flags: `--json`
  - Output JSON: REPO_ROOT, BRANCH, FEATURE_SPEC, IMPL_PLAN, SPECS_DIR
  - Used by: /plan workflow
  - ~60 LOC

- [x] **T035** [P] Create scripts/bash/create-new-feature.sh
  - File: `scripts/bash/create-new-feature.sh`
  - Args: Feature description as $1
  - Flags: `--json`
  - Actions: Create git branch, create specs/{id}-{slug}/, initialize spec.md
  - Output JSON: REPO_ROOT, BRANCH_NAME, SPEC_FILE, FEATURE_DIR
  - Used by: /specify workflow
  - ~70 LOC

- [x] **T036** [P] Create scripts/bash/update-agent-context.sh
  - File: `scripts/bash/update-agent-context.sh`
  - Args: Agent type (windsurf, claude, cursor, etc.)
  - Actions: Update/create agent-specific file (WINDSURF.md, CLAUDE.md, etc.)
  - Keep under 150 lines (token efficiency)
  - Used by: /plan Phase 1
  - ~50 LOC

### PowerShell Validation Scripts

- [x] **T037** [P] Create scripts/powershell/validate-structure.ps1
  - File: `scripts/powershell/validate-structure.ps1`
  - Identical behavior to bash version
  - Output format must match exactly
  - Use `Write-Output` for messages
  - ~50 LOC

- [x] **T038** [P] Create scripts/powershell/validate-naming.ps1
  - File: `scripts/powershell/validate-naming.ps1`
  - Identical behavior to bash version
  - Output format must match exactly
  - ~40 LOC

- [x] **T039** [P] Create scripts/powershell/validate-frontmatter.ps1
  - File: `scripts/powershell/validate-frontmatter.ps1`
  - Identical behavior to bash version
  - YAML parsing with PowerShell-Yaml or native
  - ~60 LOC

### PowerShell Helper Scripts

- [x] **T040** [P] Create scripts/powershell/check-prerequisites.ps1
  - File: `scripts/powershell/check-prerequisites.ps1`
  - Flags: `-Json`, `-PathsOnly`, `-RequireTasks`, `-IncludeTasks`
  - Output JSON: Same structure as bash version
  - Use `ConvertTo-Json -Compress`
  - Convert backslashes to forward slashes in paths
  - ~80 LOC

- [x] **T041** [P] Create scripts/powershell/setup-plan.ps1
  - File: `scripts/powershell/setup-plan.ps1`
  - Flags: `-Json`
  - Output JSON: Same structure as bash version
  - ~60 LOC

- [x] **T042** [P] Create scripts/powershell/create-new-feature.ps1
  - File: `scripts/powershell/create-new-feature.ps1`
  - Args: Feature description as param
  - Flags: `-Json`
  - Actions: Same as bash version
  - Output JSON: Same structure as bash version
  - ~70 LOC

- [x] **T043** [P] Create scripts/powershell/update-agent-context.ps1
  - File: `scripts/powershell/update-agent-context.ps1`
  - Args: `-AgentType` parameter
  - Actions: Same as bash version
  - ~50 LOC

### Script Testing

- [x] **T044** [P] Create tests/integration/test_script_parity.py
  - File: `tests/integration/test_script_parity.py`
  - Tests: For each script pair (bash + PS), verify identical JSON output
  - Platform detection: Run bash on Unix, PowerShell on Windows
  - Parse JSON and compare structures
  - ~100 LOC

- [x] **T045** [P] Create tests/integration/test_json_contracts.py
  - File: `tests/integration/test_json_contracts.py`
  - Tests: Verify JSON output matches documented contracts
  - Validate: All required fields present, paths are absolute, forward slashes
  - ~80 LOC

- [x] **T046** Update specify_cli/commands/init.py to copy scripts
  - File: `specify_cli/commands/init.py`
  - Add function: `_copy_source_scripts(scripts_dir)` similar to `_copy_source_templates`
  - Copy from `scripts/` → `.specify/scripts/`
  - Set executable permissions for bash scripts (chmod +x)
  - ~20 LOC addition (stays under 400 LOC budget)

- [x] **T047** Update specify_cli/commands/check.py to execute scripts
  - File: `specify_cli/commands/check.py`
  - Currently calls validators.run_validation_script()
  - Verify it works with actual scripts (not placeholders)
  - May need platform detection adjustment
  - ~10 LOC modification

---

## Phase 3.6: Integration & Documentation (T048-T054)

- [x] **T048** Update pyproject.toml for package data
  - File: `pyproject.toml`
  - Add: `[tool.setuptools.package-data]` section
  - Include: `"*" = ["*.md", "*.sh", "*.ps1"]`
  - Ensure scripts included in distribution
  - ~10 LOC addition

- [x] **T049** Create tests/integration/test_init_copies_scripts.py
  - File: `tests/integration/test_init_copies_scripts.py`
  - Tests: `specify init` copies all 14 scripts to `.specify/scripts/`
  - Verify: bash scripts are executable
  - Verify: PowerShell scripts exist
  - ~60 LOC

- [x] **T050** [P] Update documentation for v2.0
  - Files: `README.md`, `CONTRIBUTING.md` (if exists)
  - Document: Template + script architecture
  - Document: Workflow system (markdown, not CLI commands)
  - Document: Installation methods (uv tool + uvx)
  - Document: Cross-platform script execution
  - ~100 LOC updates

- [ ] **T051** [P] Performance optimization pass
  - Review: Template copying performance (target <200ms)
  - Review: Script execution overhead
  - Optimize: File I/O if needed
  - Measure: Init time (<3s), check time (<1s)
  - Document: Performance benchmarks

- [ ] **T052** [P] Memory footprint validation
  - Measure: CLI memory usage (<50MB target)
  - Profile: Import times and memory allocation
  - Optimize: If needed
  - Document: Results

- [ ] **T053** [P] Cross-platform CI/CD setup
  - File: `.github/workflows/ci.yml` (if using GitHub Actions)
  - Test: On Windows (PowerShell), macOS (bash), Linux (bash)
  - Validate: Script parity across platforms
  - Run: Full test suite on all platforms

- [ ] **T054** Constitutional compliance final check
  - Verify: CLI LOC < 400 (currently 224 + additions)
  - Verify: Only 4 dependencies (click, PyYAML, requests, stdlib)
  - Verify: Only 2 commands (init, check)
  - Verify: All 7 constitutional principles satisfied
  - Document: Compliance status

---

## Phase 3.7: QA & Validation (T055-T062)

- [ ] **T055** Run full test suite
  - Execute: `pytest tests/` with coverage
  - Target: All 66+ tests passing
  - Current: 51/66 passing (77%)
  - Fix: Remaining test failures
  - Target coverage: >80%

- [ ] **T056** LOC count validation
  - Count: Total Python LOC in `specify_cli/`
  - Tool: `python -c "from tests.helpers import count_loc; ..."`
  - Verify: < 400 LOC
  - Document: Final count

- [ ] **T057** Cross-platform manual testing
  - Test: `specify init` on Windows, macOS, Linux
  - Test: `specify check` on all platforms
  - Test: Script execution on all platforms
  - Verify: Identical behavior

- [ ] **T058** Security audit
  - Review: No execution of untrusted code (NFR-013)
  - Review: Scripts don't modify files outside project (NFR-015)
  - Review: Offline mode works (NFR-016)
  - Review: Input validation in CLI
  - Document: Security findings

- [ ] **T059** Performance benchmarks
  - Measure: `specify init` time (target <3s)
  - Measure: `specify check` time (target <1s)
  - Measure: Template copying (target <200ms)
  - Measure: Memory footprint (target <50MB)
  - Document: Benchmark results

- [ ] **T060** Backward compatibility testing
  - Test: V1.x project validation
  - Test: V1.x frontmatter support
  - Test: V1.x folder structure
  - Verify: No forced breaking changes
  - Document: Compatibility status

- [ ] **T061** Release preparation
  - Update: Version to 2.0.0 in `specify_cli/__init__.py`
  - Update: CHANGELOG.md with release notes
  - Tag: Git release with v2.0.0
  - Prepare: GitHub Release with template archives
  - Document: Release process

- [ ] **T062** Final documentation review
  - Review: All README files accurate
  - Review: All templates have agent guidance
  - Review: All workflows reference correct paths
  - Review: WINDSURF.md up to date
  - Publish: Documentation

---

## Dependencies

### Critical Path
```
T030-T036 (bash scripts) 
  → T037-T043 (PowerShell scripts use bash as reference)
  → T044-T045 (script parity tests)
  → T046-T047 (integrate scripts into CLI)
  → T048-T054 (integration & docs)
  → T055-T062 (QA & release)
```

### Parallel Opportunities
- T030-T036: All bash scripts can be created in parallel [P]
- T037-T043: All PowerShell scripts can be created in parallel [P] (after bash complete)
- T044-T045: Test files can be created in parallel [P]
- T048, T050-T053: Documentation and config can be done in parallel [P]
- T055-T060: QA tasks can run in parallel [P]

---

## Parallel Execution Examples

### Phase 3.5: Create all bash scripts simultaneously
```
T030: Create bash/validate-structure.sh
T031: Create bash/validate-naming.sh
T032: Create bash/validate-frontmatter.sh
T033: Create bash/check-prerequisites.sh
T034: Create bash/setup-plan.sh
T035: Create bash/create-new-feature.sh
T036: Create bash/update-agent-context.sh
```

### Phase 3.5: Create all PowerShell scripts simultaneously (after bash complete)
```
T037: Create powershell/validate-structure.ps1
T038: Create powershell/validate-naming.ps1
T039: Create powershell/validate-frontmatter.ps1
T040: Create powershell/check-prerequisites.ps1
T041: Create powershell/setup-plan.ps1
T042: Create powershell/create-new-feature.ps1
T043: Create powershell/update-agent-context.ps1
```

---

## Notes

- Tasks T001-T029: Already complete (Setup, Tests, Core CLI, Templates)
- Tasks T030-T047: Script creation (Phase 3.5) - ~18 tasks
- Tasks T048-T054: Integration & documentation (Phase 3.6) - 7 tasks
- Tasks T055-T062: QA & validation (Phase 3.7) - 8 tasks
- **Total remaining**: 33 tasks (T030-T062)
- **Parallel opportunities**: ~20 tasks can run in parallel
- **Sequential dependencies**: Bash before PowerShell, scripts before integration
- **Estimated completion**: 3-5 work sessions with parallel execution

---

**Status**: Ready for implementation via `/implement` command
