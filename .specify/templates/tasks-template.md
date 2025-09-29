# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 3.1: Setup
- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize [language] project with [framework] dependencies
- [ ] T003 [P] Configure linting and formatting tools
- [ ] T004 [P] Set up cross-platform validation framework
- [ ] T005 [P] Configure template synchronization system

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T006 [P] Contract test POST /api/users in tests/contract/test_users_post.py
- [ ] T007 [P] Contract test GET /api/users/{id} in tests/contract/test_users_get.py
- [ ] T008 [P] Integration test user registration in tests/integration/test_registration.py
- [ ] T009 [P] Integration test auth flow in tests/integration/test_auth.py
- [ ] T010 [P] Cross-platform compatibility test in tests/cross-platform/test_platform_compatibility.py
- [ ] T011 [P] Multi-installation support test in tests/cross-platform/test_installation_methods.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T012 [P] User model in src/models/user.py
- [ ] T013 [P] UserService CRUD in src/services/user_service.py
- [ ] T014 [P] CLI --create-user in src/cli/user_commands.py
- [ ] T015 POST /api/users endpoint
- [ ] T016 GET /api/users/{id} endpoint
- [ ] T017 Input validation
- [ ] T018 Error handling and logging
- [ ] T019 [P] Cross-platform command definitions in src/commands/
- [ ] T020 [P] Template synchronization logic in src/sync/
- [ ] T021 [P] Architecture validation framework in src/validation/

## Phase 3.4: Integration
- [ ] T022 Connect UserService to DB
- [ ] T023 Auth middleware
- [ ] T024 Request/response logging
- [ ] T025 CORS and security headers
- [ ] T026 [P] Multi-installation method integration
- [ ] T027 [P] Cross-platform agent execution integration
- [ ] T028 [P] Template synchronization integration
- [ ] T029 [P] Architecture validation integration

## Phase 3.5: Polish
- [ ] T030 [P] Unit tests for validation in tests/unit/test_validation.py
- [ ] T031 [P] Cross-platform compatibility tests in tests/cross-platform/
- [ ] T032 [P] Template synchronization tests in tests/sync/
- [ ] T033 [P] Architecture validation tests in tests/validation/
- [ ] T034 [P] Multi-installation tests in tests/installation/
- [ ] T035 Performance tests (<200ms)
- [ ] T036 [P] Update docs/api.md
- [ ] T037 [P] Update cross-platform documentation in docs/cross-platform.md
- [ ] T038 [P] Update template synchronization docs in docs/sync.md
- [ ] T039 Remove duplication
- [ ] T040 Run manual-testing.md
- [ ] T041 Run cross-platform validation suite
- [ ] T042 Run template synchronization verification

## Dependencies
- Setup (T001-T005) before tests (T006-T011)
- Tests (T006-T011) before implementation (T012-T021)
- Core implementation (T012-T021) before integration (T022-T029)
- Integration (T022-T029) before polish (T030-T042)
- T012 blocks T013, T022
- T019, T020, T021 can run in parallel [P]
- T026, T027, T028, T029 can run in parallel [P]
- T030-T034 can run in parallel [P]

## Parallel Example
```
# Launch T006-T011 together:
Task: "Contract test POST /api/users in tests/contract/test_users_post.py"
Task: "Contract test GET /api/users/{id} in tests/contract/test_users_get.py"
Task: "Integration test registration in tests/integration/test_registration.py"
Task: "Integration test auth in tests/integration/test_auth.py"
Task: "Cross-platform compatibility test in tests/cross-platform/test_platform_compatibility.py"
Task: "Multi-installation support test in tests/cross-platform/test_installation_methods.py"

# Launch T019-T021 together:
Task: "Cross-platform command definitions in src/commands/"
Task: "Template synchronization logic in src/sync/"
Task: "Architecture validation framework in src/validation/"

# Launch T030-T034 together:
Task: "Unit tests for validation in tests/unit/test_validation.py"
Task: "Cross-platform compatibility tests in tests/cross-platform/"
Task: "Template synchronization tests in tests/sync/"
Task: "Architecture validation tests in tests/validation/"
Task: "Multi-installation tests in tests/installation/"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Constitution Requirements**:
   - Cross-Platform Compatibility → cross-platform validation tasks [P]
   - Multi-Installation Support → installation method tasks [P]
   - Architecture-First → architecture validation tasks [P]
   - Template-Driven → template synchronization tasks [P]
   - Synchronicity → synchronization logic tasks [P]
   - Agent-Native → command definition tasks [P]
   - Hierarchical Governance → documentation tasks [P]

2. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task

3. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks

4. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

5. **Ordering**:
   - Setup → Constitution Validation → Tests → Models → Services → Endpoints → Integration → Polish
   - Dependencies block parallel execution
   - Constitution validation tasks must pass before proceeding

## Validation Checklist
*GATE: Checked by main() before returning*

### Constitution Compliance
- [ ] All 7 constitution principles have corresponding tasks
- [ ] Cross-platform compatibility tasks included
- [ ] Multi-installation support tasks included
- [ ] Architecture validation tasks included
- [ ] Template synchronization tasks included
- [ ] Agent-native execution tasks included
- [ ] Hierarchical governance tasks included

### Task Quality
- [ ] All contracts have corresponding tests
- [ ] All entities have model tasks
- [ ] All tests come before implementation
- [ ] Parallel tasks truly independent
- [ ] Each task specifies exact file path
- [ ] No task modifies same file as another [P] task
- [ ] Constitution validation tasks are properly sequenced