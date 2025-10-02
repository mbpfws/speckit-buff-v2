# Spec-Kit Tests

## Test Structure

- `contract/` - Contract tests for CLI commands (T006-T008)
- `integration/` - End-to-end integration tests (T009-T018)
- `unit/` - Unit tests for individual modules

## Running Tests

```bash
# Run all tests
pytest

# Run specific test suite
pytest tests/contract/
pytest tests/integration/
pytest tests/unit/

# Run with coverage
pytest --cov=specify_cli --cov-report=html

# Run specific test
pytest tests/contract/test_cli_init.py::TestInitEmptyDirectory
```

## Test Status

### Phase 3.2: Contract Tests (TDD)

All tests written following TDD - they MUST fail initially:

- ✅ T006: `test_cli_init.py` - CLI init command contract tests
- ✅ T007: `test_cli_check.py` - CLI check command contract tests
- ✅ T008: `test_validation_api.py` - Validation script API tests
- ⏳ T009-T018: Integration tests (partial - key tests created)

### Expected Initial State

All contract tests should **FAIL** initially because implementation doesn't exist yet.
This is the correct TDD approach:

1. ❌ Write failing tests (Phase 3.2)
2. ✅ Implement code to make tests pass (Phase 3.3)
3. ✅ Refactor while keeping tests green

## Test Categories

### Contract Tests
Based on `contracts/*.yaml` specifications:
- Define expected CLI behavior
- Test all success and error cases
- Validate performance targets
- Ensure proper exit codes

### Integration Tests
Based on `quickstart.md` scenarios:
- Test complete workflows end-to-end
- Verify cross-platform compatibility
- Validate performance requirements
- Test offline capabilities

### Unit Tests
Test individual modules in isolation:
- `template_loader.py` functions
- `validators.py` functions
- Utility helpers

## Coverage Goals

- Contract tests: 100% of contracts covered
- Integration tests: All 10 quickstart scenarios
- Unit tests: >80% code coverage
- Overall: >85% coverage target
