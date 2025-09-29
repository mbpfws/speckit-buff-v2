# Test Suite

This directory contains the test suite for the Spec-Kit Enhancement Initiative.

## Test Structure

```
tests/
├── contract/          # Contract tests (API definitions)
│   ├── test_project_analyzer.py
│   ├── test_architecture_engine.py
│   ├── test_governance_system.py
│   └── test_agent_workflow.py
├── integration/       # Integration tests (to be implemented)
├── unit/             # Unit tests (to be implemented)
├── requirements.txt  # Test dependencies
├── pytest.ini       # Pytest configuration
└── run_contract_tests.py  # Helper script to verify TDD
```

## Running Tests

### Install Test Dependencies
```bash
pip install -r tests/requirements.txt
```

### Run All Tests
```bash
pytest tests/
```

### Run Contract Tests Only
```bash
pytest tests/contract/ -m contract
```

### Run Integration Tests Only
```bash
pytest tests/integration/ -m integration
```

### Run Unit Tests Only
```bash
pytest tests/unit/ -m unit
```

### Verify TDD (Tests Should Fail)
```bash
python tests/run_contract_tests.py
```

## Test Markers

- `@pytest.mark.contract`: Tests that verify API contracts
- `@pytest.mark.integration`: Tests that verify component integration
- `@pytest.mark.unit`: Tests that verify individual components

## TDD Approach

The contract tests follow the Test-Driven Development (TDD) approach:

1. **Red**: Write failing tests first (Phase 3.2)
2. **Green**: Implement the minimum code to make tests pass (Phase 3.3)
3. **Refactor**: Improve the implementation while keeping tests green (Phase 3.4+)

Currently in **Red phase** - tests are written and should fail because the implementations don't exist yet.

## Test Coverage

The contract tests cover:

1. **Project Analyzer API** (`test_project_analyzer.py`)
   - Project analysis endpoint
   - Architecture analysis endpoint
   - Error handling and validation

2. **Architecture Engine API** (`test_architecture_engine.py`)
   - Pattern detection endpoint
   - Architecture guidance endpoint
   - Various analysis modes

3. **Governance System API** (`test_governance_system.py`)
   - Artifact creation endpoint
   - Synchronization endpoint
   - Validation endpoint
   - Platform-specific features

4. **Agent Workflow Manager API** (`test_agent_workflow.py`)
   - Context management endpoint
   - Prompt optimization endpoint
   - Agent validation endpoint
   - Cross-platform support

## Notes

- All tests are asynchronous and use `httpx` for HTTP testing
- Tests validate both successful responses and error conditions
- Tests follow the OpenAPI specifications defined in `specs/001-improve-spec-kit/contracts/`
- Mock servers are not used - tests expect real implementations to exist