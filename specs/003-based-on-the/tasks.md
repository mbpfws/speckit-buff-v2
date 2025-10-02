# Tasks: Spec-Kit Realignment Fork - Back to Basics

**Feature**: 003-based-on-the | **Date**: 2025-09-30  
**Input**: Design documents from `D:/speckit-buff/specs/003-based-on-the/`  
**Prerequisites**: plan.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

---

## Technical Context Summary

**Language**: Python 3.9+  
**CLI Framework**: Click  
**Dependencies**: stdlib, requests, PyYAML, click (minimal)  
**Target**: <400 LOC total for CLI  
**Platforms**: Cross-platform (Windows, macOS, Linux)  
**Installation**: Both uv tool (PATH) and uvx (temporary) methods

**Project Structure**:
```
specify-cli/
├── cli.py (~80 LOC)
├── commands/
│   ├── init.py (~100 LOC)
│   └── check.py (~80 LOC)
├── template_loader.py (~80 LOC)
└── validators.py (~60 LOC)

.specify/templates/
├── spec-template.md
├── plan-template.md
├── tasks-template.md
├── constitution.md
├── brownfield-analysis.md
└── architecture-patterns.md

.specify/scripts/
├── bash/
│   ├── validate-structure.sh
│   ├── validate-naming.sh
│   └── validate-frontmatter.sh
└── powershell/
    ├── validate-structure.ps1
    ├── validate-naming.ps1
    └── validate-frontmatter.ps1
```

---

## Phase 3.1: Project Setup & Infrastructure

- [x] **T001** Create repository structure
  - Create `specify-cli/` directory with `__init__.py`
  - Create `specify-cli/commands/` directory with `__init__.py`
  - Create `.specify/templates/` directory
  - Create `.specify/scripts/bash/` and `.specify/scripts/powershell/` directories
  - Create `tests/contract/`, `tests/integration/`, `tests/unit/` directories
  - Ensure all directories have proper permissions

- [x] **T002** Initialize Python project with pyproject.toml
  - Configure project metadata (name: specify-cli, version: 2.0.0)
  - Add dependencies: click, requests, PyYAML
  - Add dev dependencies: pytest, pytest-cov, black, flake8
  - Configure build system (setuptools or hatchling)
  - Add entry point: `specify = specify_cli.cli:main`
  - Target Python 3.9+ compatibility

- [x] **T003** [P] Configure testing infrastructure
  - Create `pytest.ini` with test paths and options
  - Create `tests/conftest.py` with common fixtures
  - Set up test coverage configuration (.coveragerc)
  - Add test helper utilities in `tests/helpers.py`

- [x] **T004** [P] Configure linting and formatting tools
  - Create `.flake8` config (max line length 100)
  - Create `pyproject.toml` black configuration
  - Add pre-commit hooks configuration (optional)
  - Document code style guidelines in CONTRIBUTING.md

- [x] **T005** [P] Create README.md with installation instructions
  - Document both installation methods (uv tool and uvx)
  - Add quick start guide (specify init, specify check)
  - Include examples for common workflows
  - Add troubleshooting section
  - Document supported platforms and requirements

---

## Phase 3.2: Contract Tests (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

### CLI Command Contract Tests

- [x] **T006** [P] Contract test: CLI init command
  - File: `tests/contract/test_cli_init.py`
  - Based on: `contracts/cli-init.yaml`
  - Tests:
    - `test_init_empty_directory()` - Success case
    - `test_init_with_existing_specify()` - Error without --force
    - `test_init_with_force()` - Overwrites with backup
    - `test_init_specific_version()` - Downloads specific template version
    - `test_init_offline_mode()` - Uses cached templates
    - `test_init_offline_no_cache()` - Error when cache missing
    - `test_init_minimal()` - Installs only essential templates
  - All tests FAILING as expected (TDD ✅)

- [x] **T007** [P] Contract test: CLI check command
  - File: `tests/contract/test_cli_check.py`
  - Based on: `contracts/cli-check.yaml`
  - Tests:
    - `test_check_valid_project()` - All checks pass
    - `test_check_with_errors()` - Reports errors with code 0 (non-blocking)
    - `test_check_with_warnings()` - Reports warnings with code 0
    - `test_check_single_artifact()` - Validates single file
    - `test_check_quality()` - Runs quality tools if configured
    - `test_check_json_output()` - Outputs JSON format
    - `test_check_update_templates()` - Checks for template updates
    - `test_check_fix()` - Applies automatic fixes
    - `test_check_no_specify()` - Error when .specify/ missing
  - All tests FAILING as expected (TDD ✅)

- [x] **T008** [P] Contract test: Validation script API
  - File: `tests/contract/test_validation_api.py`
  - Based on: `contracts/validation-api.yaml`
  - Tests:
    - `test_validate_structure_valid()` - Valid structure passes
    - `test_validate_structure_missing_file()` - Missing file reported
    - `test_validate_naming_valid()` - Naming conventions pass
    - `test_validate_naming_invalid()` - Invalid naming reported
    - `test_validate_frontmatter_valid()` - Valid frontmatter passes
    - `test_validate_frontmatter_missing_field()` - Missing field error
    - `test_cross_platform_parity()` - Bash and PowerShell outputs match
  - All tests FAILING as expected (TDD ✅)

### Integration Test Suite (From quickstart.md)

- [x] **T009** [P] Integration test: Greenfield project initialization (Scenario 1)
  - File: `tests/integration/test_greenfield_init.py` ✅
  - Tests:
    - Project initialization completes in <3 seconds
    - .specify/ directory created with templates and scripts
    - specs/ directory created
    - No analysis engines installed
    - Works with both uv tool and uvx methods
  - Status: 3/3 tests passing

- [x] **T010** [P] Integration test: Brownfield project analysis (Scenario 2)
  - File: `tests/integration/test_brownfield_analysis.py` ✅
  - Tests:
    - Agent performs multi-pass analysis (scan → research → validate)
    - Detects technology stack with high confidence
    - Reports findings with confidence levels
    - Provides prioritized recommendations
  - Status: Template-driven tests (Phase 3.4 will complete)

- [x] **T011** [P] Integration test: Framework architecture patterns (Scenario 3)
  - File: `tests/integration/test_architecture_patterns.py` ✅
  - Tests:
    - Agent loads architecture pattern from template
    - Agent validates pattern against latest documentation
    - Reports outdated patterns with recommendations
    - Provides official documentation references
  - Status: Template-driven tests (Phase 3.4 will complete)

- [x] **T012** [P] Integration test: Artifact validation workflow (Scenario 4)
  - File: `tests/integration/test_artifact_validation.py` ✅
  - Tests:
    - Creates artifact with YAML frontmatter
    - Runs validation scripts successfully
    - Parses [INFO], [WARN], [ERROR] messages
    - Reports validation results to user
    - Non-blocking (exit code 0)
  - Status: 3/3 tests passing

- [x] **T013** [P] Integration test: Multi-platform execution (Scenario 5)
  - File: `tests/integration/test_multi_platform.py` ✅
  - Tests:
    - /specify command works on multiple platforms
    - Templates ensure consistency across platforms
    - Validation scripts produce compatible output
  - Status: 4/4 tests passing

- [x] **T014** [P] Integration test: Quality tool integration (Scenario 6)
  - File: `tests/integration/test_quality_integration.py` ✅
  - Tests:
    - Detects project type and available tools
    - Runs quality checks without blocking
    - Categorizes findings (critical vs warnings)
    - Exit code 0 even with issues found
  - Status: 4/4 tests passing

- [x] **T015** [P] Integration test: CLI simplicity verification (Scenario 7)
  - File: `tests/integration/test_cli_simplicity.py` ✅
  - Tests:
    - Total CLI code <400 LOC (currently 224 LOC ✅)
    - No analysis engines present
    - Only 4 dependencies (stdlib, requests, PyYAML, click)
    - Low cyclomatic complexity
  - Status: Core tests passing (some tests need radon)

- [x] **T016** [P] Integration test: Cross-platform scripts (Scenario 8)
  - File: `tests/integration/test_cross_platform_scripts.py` ✅
  - Tests:
    - Bash scripts work on Unix/Linux/macOS
    - PowerShell scripts work on Windows
    - Outputs functionally identical
    - Both exit with code 0
  - Status: Tests created (Phase 3.5 will make them pass)

- [x] **T017** [P] Integration test: Offline usage (Scenario 9)
  - File: `tests/integration/test_offline_usage.py` ✅
  - Tests:
    - Templates cached locally after first init
    - Validation scripts work offline
    - No errors from network unavailability
    - Explicit --offline flag works
  - Status: 5/5 tests passing

- [x] **T018** [P] Integration test: Backward compatibility (Scenario 10)
  - File: `tests/integration/test_backward_compatibility.py` ✅
  - Tests:
    - V1.x projects work with v2.0 CLI
    - V1.x artifacts validate successfully
    - Clear migration path provided
    - No forced breaking changes
  - Status: 6/6 tests passing

---

## Phase 3.3: Core CLI Implementation (ONLY after tests are failing)

**Dependency**: All Phase 3.2 tests must be failing before starting this phase

### Template Management Module

- [x] **T019** [P] Implement template_loader.py
  - File: `specify_cli/template_loader.py`
  - Functions:
    - `download_templates(version='latest', offline=False)` - Download from GitHub Releases
    - `extract_templates(archive_path, target_dir)` - Extract tar.gz
    - `cache_templates(version, templates_dir)` - Store in ~/.specify/cache/
    - `get_cached_version()` - Read cached template version
    - `check_for_updates()` - Query GitHub API for latest version
  - Target: ~80 LOC ✅
  - Handle network errors gracefully
  - Support semver version selection

### Validation Script Wrapper Module

- [x] **T020** [P] Implement validators.py
  - File: `specify_cli/validators.py`
  - Functions:
    - `run_validation_script(script_name, target_path, platform='auto')` - Execute script
    - `parse_validation_output(output)` - Parse [LEVEL] messages
    - `detect_platform()` - Return 'unix' or 'windows'
    - `ValidationResult` class - Store validation results
    - `ValidationMessage` class - Individual message objects
  - Target: ~60 LOC ✅
  - Execute bash on Unix, PowerShell on Windows
  - Parse output into structured format

### CLI Main Entry Point

- [x] **T021** Implement cli.py main entry point
  - File: `specify_cli/cli.py`
  - Dependencies: T019 (template_loader), T020 (validators)
  - Functions:
    - `@click.group()` main CLI group
    - `--version` option
    - `--help` option
  - Commands: init, check (implemented separately)
  - Target: ~80 LOC ✅
  - Handle global options and errors

### CLI Init Command

- [x] **T022** Implement commands/init.py
  - File: `specify_cli/commands/init.py`
  - Dependencies: T021 (cli.py), T019 (template_loader)
  - Options:
    - `--template-version` - Specify template version
    - `--force` - Overwrite existing .specify/
    - `--offline` - Use cached templates
    - `--minimal` - Install only essential templates
  - Target: ~100 LOC ✅
  - Performance: <3 seconds execution time ✅
  - Creates .specify/ structure per contract

### CLI Check Command

- [x] **T023** Implement commands/check.py
  - File: `specify_cli/commands/check.py`
  - Dependencies: T021 (cli.py), T020 (validators)
  - Options:
    - `--quality` - Run quality tool checks
    - `--validation` - Which validation scripts to run
    - `--update-templates` - Check for template updates
    - `--fix` - Attempt automatic fixes
    - `--format` - Output format (text, json, yaml)
  - Target: ~80 LOC ✅
  - Performance: ~1.3s execution time (close to <1s target)
  - Orchestrates validation scripts per contract

---

## Phase 3.4: Template Creation

**All templates can be created in parallel**

- [x] **T024** [P] Create spec-template.md ✅
  - File: `.specify/templates/spec-template.md`
  - Include:
    - YAML frontmatter example ✅
    - Section structure (Overview, User Stories, Requirements, etc.) ✅
    - Agent guidance embedded in markdown comments ✅
    - Constitutional alignment section ✅
  - Status: Updated with proper frontmatter and agent guidance

- [x] **T025** [P] Create plan-template.md ✅
  - File: `.specify/templates/plan-template.md`
  - Update from current `specs/003-based-on-the/plan.md`
  - Include:
    - Execution flow description ✅
    - Technical context section ✅
    - Constitution check section ✅
    - Phase 0-2 structures ✅
    - Progress tracking checklist ✅
  - Status: Already comprehensive, verified complete

- [x] **T026** [P] Create tasks-template.md ✅
  - File: `.specify/templates/tasks-template.md`
  - Already exists at `.specify/templates/tasks-template.md` ✅
  - Verify completeness and update if needed ✅
  - Include task generation rules ✅
  - Document parallel execution patterns ✅
  - Status: Verified complete with all required sections

- [x] **T027** [P] Create constitution.md template ✅
  - File: `.specify/templates/constitution.md`
  - Document:
    - 7 constitutional principles (from research.md) ✅
    - Cross-platform compatibility ✅
    - Multi-installation support ✅
    - Template-driven consistency ✅
    - Agent-native execution ✅
    - Simplicity principle ✅
    - Governance balance ✅
    - Backward compatibility ✅
  - Provide evaluation criteria for each ✅
  - Status: Complete with full evaluation criteria and usage guidance

- [x] **T028** [P] Create brownfield-analysis.md template ✅
  - File: `.specify/templates/brownfield-analysis.md`
  - Include:
    - Multi-pass analysis workflow (4 passes) ✅
    - Pass 1: Initial scan checklist ✅
    - Pass 2: Online research tasks ✅
    - Pass 3: Validation criteria ✅
    - Pass 4: Report structure with confidence levels ✅
  - Agent instructions embedded ✅
  - Technology detection patterns ✅
  - Status: Comprehensive 4-pass workflow with confidence methodology

- [x] **T029** [P] Create architecture-patterns.md template ✅
  - File: `.specify/templates/architecture-patterns.md`
  - Include:
    - Tier 1 framework patterns (React/Next.js, Django/FastAPI, Spring Boot) ✅
    - Folder structure examples with descriptions ✅
    - Key configuration files list ✅
    - Validation checklist questions for agents ✅
    - Research guidance for latest versions ✅
  - Agent instructions for pattern validation ✅
  - Status: Complete with 10+ framework patterns and validation workflow

---

## Phase 3.5: Validation Scripts (Bash + PowerShell)

**Each bash script must have a PowerShell equivalent with identical output**

### Bash Scripts

- [ ] **T030** [P] Create bash/validate-structure.sh
  - File: `.specify/scripts/bash/validate-structure.sh`
  - Checks:
    - .specify/ directory structure correct
    - specs/ directory exists
    - Artifact folders follow naming convention {id}-{slug}
    - Required files present (spec.md minimum)
  - Output: [INFO], [WARN], [ERROR] messages per contract
  - Exit code: 0 (always)
  - Target: 50-100 LOC
  - Make executable (chmod +x)

- [ ] **T031** [P] Create bash/validate-naming.sh
  - File: `.specify/scripts/bash/validate-naming.sh`
  - Checks:
    - Feature IDs are 3-digit zero-padded integers
    - Feature slugs match pattern [a-z0-9-]+
    - File names follow conventions (lowercase with hyphens)
    - Feature ID consistency (folder vs frontmatter)
  - Output: [INFO], [WARN], [ERROR] messages per contract
  - Exit code: 0 (always)
  - Target: 50-100 LOC
  - Make executable (chmod +x)

- [ ] **T032** [P] Create bash/validate-frontmatter.sh
  - File: `.specify/scripts/bash/validate-frontmatter.sh`
  - Checks:
    - YAML frontmatter present and parseable
    - Required fields: feature_id, created, status
    - Optional fields: parent_spec, version, branch
    - Field validation (types, values)
    - Parent references resolve correctly
  - Output: [INFO], [WARN], [ERROR] messages per contract
  - Exit code: 0 (always)
  - Target: 50-100 LOC
  - Use yq if available, fallback to grep/sed
  - Make executable (chmod +x)

### PowerShell Scripts (Must match bash output)

- [ ] **T033** Create powershell/validate-structure.ps1
  - File: `.specify/scripts/powershell/validate-structure.ps1`
  - Dependencies: T030 (bash version defines contract)
  - Implement identical checks as T030
  - Output format must match bash script exactly
  - Exit code: 0 (always)
  - Target: 50-100 LOC
  - Handle paths with spaces correctly

- [ ] **T034** Create powershell/validate-naming.ps1
  - File: `.specify/scripts/powershell/validate-naming.ps1`
  - Dependencies: T031 (bash version defines contract)
  - Implement identical checks as T031
  - Output format must match bash script exactly
  - Exit code: 0 (always)
  - Target: 50-100 LOC

- [ ] **T035** Create powershell/validate-frontmatter.ps1
  - File: `.specify/scripts/powershell/validate-frontmatter.ps1`
  - Dependencies: T032 (bash version defines contract)
  - Implement identical checks as T032
  - Output format must match bash script exactly
  - Exit code: 0 (always)
  - Target: 50-100 LOC
  - Use PowerShell YAML module or manual parsing

---

## Phase 3.6: Integration & Platform Configuration

- [ ] **T036** Create .specify/config.yaml default configuration
  - File: `.specify/config.yaml`
  - Include:
    - template_source: GitHub releases URL
    - template_version: latest
    - validation: skip_checks, fail_on_error
    - quality: tools, auto_fix
    - offline_mode: false
  - Document all configuration options

- [ ] **T037** [P] Create platform-specific workflow files
  - Files:
    - `.specify/workflows/WINDSURF.md` (already exists, verify)
    - `.specify/workflows/CLAUDE.md` (for Claude Code)
    - `.specify/workflows/GITHUB.md` (for GitHub Copilot)
    - `.specify/workflows/AGENTS.md` (generic fallback)
  - Include: command references, validation guidance, recent changes tracking
  - Target: ~150 lines per file for token efficiency

- [ ] **T038** [P] Create GitHub Release packaging script
  - File: `scripts/package-templates.sh`
  - Creates tar.gz archive of all templates
  - Generates checksum file
  - Prepares release notes
  - Tags with semantic version

---

## Phase 3.7: Documentation & Polish

- [ ] **T039** [P] Update README.md with comprehensive guide
  - Add migration guide from v1.x to v2.0
  - Document differences and improvements
  - Provide troubleshooting section
  - Add FAQ for common issues
  - Include contributing guidelines reference

- [ ] **T040** [P] Create CONTRIBUTING.md
  - Development setup instructions
  - Code style guidelines (black, flake8)
  - Testing requirements (pytest, coverage)
  - Pull request process
  - Template contribution guidelines
  - Validation script contribution guidelines

- [ ] **T041** [P] Create examples/ directory with sample workflows
  - Example 1: Simple CLI tool project
  - Example 2: Web application with React frontend
  - Example 3: Brownfield project analysis
  - Each with spec.md, plan.md, tasks.md

- [ ] **T042** [P] Create CHANGELOG.md with v2.0.0 release notes
  - What's new: Simplified CLI, agent-augmented templates
  - Breaking changes: Removed analysis engines
  - Migration guide summary
  - Known issues and limitations

---

## Phase 3.8: Validation & Quality Assurance

- [ ] **T043** Run all contract tests and verify they pass
  - Execute: `pytest tests/contract/ -v`
  - All T006-T008 tests must pass
  - No test failures allowed
  - Coverage: 100% for contract tests

- [ ] **T044** Run all integration tests and verify they pass
  - Execute: `pytest tests/integration/ -v`
  - All T009-T018 tests must pass (10 scenarios)
  - Performance validation: <3s init, <1s check
  - No test failures allowed

- [ ] **T045** LOC audit: Verify CLI <400 lines total
  - Count lines in specify-cli/cli.py
  - Count lines in specify-cli/commands/init.py
  - Count lines in specify-cli/commands/check.py
  - Count lines in specify-cli/template_loader.py
  - Count lines in specify-cli/validators.py
  - Total must be <400 LOC (excluding comments and blank lines)
  - Document actual LOC count

- [ ] **T046** Cross-platform testing
  - Test on Windows (PowerShell scripts)
  - Test on macOS (bash scripts)
  - Test on Linux (bash scripts)
  - Verify bash and PowerShell scripts produce identical output
  - Test both installation methods (uv tool and uvx)

- [ ] **T047** Performance validation
  - Measure `specify init` execution time (must be <3s)
  - Measure `specify check` execution time (must be <1s)
  - Test with different project sizes
  - Verify memory footprint is minimal

- [ ] **T048** Backward compatibility validation
  - Test v1.x project with v2.0 CLI
  - Verify v1.x artifacts validate successfully
  - Test migration path
  - Document any breaking changes found

- [ ] **T049** Security audit
  - Review download mechanism (HTTPS only)
  - Verify no arbitrary script execution
  - Check path traversal prevention
  - Validate file permissions handling
  - Review dependency security (requests, PyYAML, click)

- [ ] **T050** Final integration test with quickstart.md
  - Execute all 10 scenarios from quickstart.md manually
  - Verify each scenario produces expected results
  - Document any deviations or issues
  - Update quickstart.md if needed

---

## Dependencies Graph

### Critical Path
```
T001-T005 (Setup)
  ↓
T006-T018 (Tests - all must fail)
  ↓
T019-T023 (Core Implementation)
  ↓
T030-T035 (Validation Scripts)
  ↓
T043-T050 (Validation & QA)
```

### Parallel Opportunities

**Setup Phase** (After T001):
- T002, T003, T004, T005 can run in parallel

**Test Phase** (All parallel):
- T006, T007, T008 (Contract tests)
- T009-T018 (Integration tests)

**Core Implementation** (Dependencies):
- T019 [P] template_loader.py (no dependencies)
- T020 [P] validators.py (no dependencies)
- T021 cli.py (depends on T019, T020)
- T022 init.py (depends on T021, T019)
- T023 check.py (depends on T021, T020)

**Templates** (All parallel after T001):
- T024-T029 can all run in parallel

**Validation Scripts** (Two groups):
- Group 1: T030, T031, T032 (bash scripts - parallel)
- Group 2: T033, T034, T035 (PowerShell - after Group 1)

**Documentation** (All parallel):
- T039, T040, T041, T042 can run in parallel

**QA Phase** (Sequential):
- T043 → T044 → T045 → T046 → T047 → T048 → T049 → T050

---

## Parallel Execution Example

**Maximum parallelism in Test Phase:**
```bash
# Launch all contract and integration tests simultaneously:
Task: "Contract test CLI init in tests/contract/test_cli_init.py"
Task: "Contract test CLI check in tests/contract/test_cli_check.py"
Task: "Contract test Validation API in tests/contract/test_validation_api.py"
Task: "Integration test Greenfield init in tests/integration/test_greenfield_init.py"
Task: "Integration test Brownfield analysis in tests/integration/test_brownfield_analysis.py"
Task: "Integration test Architecture patterns in tests/integration/test_architecture_patterns.py"
Task: "Integration test Artifact validation in tests/integration/test_artifact_validation.py"
Task: "Integration test Multi-platform in tests/integration/test_multi_platform.py"
Task: "Integration test Quality integration in tests/integration/test_quality_integration.py"
Task: "Integration test CLI simplicity in tests/integration/test_cli_simplicity.py"
Task: "Integration test Cross-platform scripts in tests/integration/test_cross_platform_scripts.py"
Task: "Integration test Offline usage in tests/integration/test_offline_usage.py"
Task: "Integration test Backward compatibility in tests/integration/test_backward_compatibility.py"
```

**Template creation (all parallel):**
```bash
Task: "Create spec-template.md in .specify/templates/"
Task: "Create plan-template.md in .specify/templates/"
Task: "Create tasks-template.md in .specify/templates/"
Task: "Create constitution.md in .specify/templates/"
Task: "Create brownfield-analysis.md in .specify/templates/"
Task: "Create architecture-patterns.md in .specify/templates/"
```

---

## Validation Checklist

**GATE: Must be satisfied before marking tasks complete**

- [x] All contracts have corresponding tests (T006-T008)
- [x] All entities have model tasks (N/A - no separate entity models needed)
- [x] All tests come before implementation (Phase 3.2 before 3.3)
- [x] Parallel tasks are truly independent (marked [P])
- [x] Each task specifies exact file path ✓
- [x] No [P] task modifies same file as another [P] task ✓
- [x] TDD order maintained (tests fail, then implement, then pass)
- [x] LOC targets specified (<400 total for CLI)
- [x] Performance targets specified (<3s init, <1s check)
- [x] All 10 quickstart scenarios have integration tests ✓

---

## Estimated Effort

**Total Tasks**: 50  
**Estimated Time**: 3-4 weeks for solo developer

**Breakdown by Phase**:
- Setup (T001-T005): 1 day
- Tests (T006-T018): 3-4 days
- Core Implementation (T019-T023): 3-4 days
- Templates (T024-T029): 2-3 days
- Validation Scripts (T030-T035): 3-4 days
- Integration (T036-T038): 1-2 days
- Documentation (T039-T042): 1-2 days
- QA (T043-T050): 2-3 days

---

## Notes

- **TDD Discipline**: Do not skip Phase 3.2. All tests must be written and failing before implementation begins.
- **LOC Target**: Continuously monitor line count during implementation. If approaching 400 LOC, refactor for simplicity.
- **Cross-Platform**: Test bash scripts on Unix and PowerShell scripts on Windows regularly.
- **Performance**: Profile init and check commands to ensure <3s and <1s targets are met.
- **Constitutional Compliance**: Each task should maintain alignment with 7 constitutional principles.
- **Commit Strategy**: Commit after each task completion with descriptive message referencing task ID.

---

**Task Generation Complete** | Ready for implementation via /implement command
