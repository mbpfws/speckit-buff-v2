# Testing Strategy: Realistic & Minimal TDD

**Philosophy**: Quality over quantity, realistic scenarios over coverage metrics  
**Based on**: Research findings from specs/005-spec-kit-enhanced/research.md  
**Goal**: Focus on valuable tests, skip trivial code

---

## Core Principles (2025 TDD Best Practices)

### ✅ What TO Test

1. **Business Logic & Algorithms**
   - Complex calculations
   - Data transformations
   - Validation rules
   - State machines

2. **Error Handling & Edge Cases**
   - Boundary conditions
   - Invalid input handling
   - Network failures
   - Race conditions

3. **API Contracts & Data Transformations**
   - Request/response schemas
   - Data serialization/deserialization
   - API endpoint behavior
   - Database queries

4. **Critical User Flows (E2E)**
   - Complete user journeys (extended stories)
   - Authentication flows
   - Payment processing
   - Data submission workflows

### ❌ What NOT to Test Excessively

1. **Trivial Code**
   - Getters/setters
   - One-liners
   - Simple delegations
   - Pass-through functions

2. **UI Components (Snapshot Tests)**
   - Brittle, break on every style change
   - Low value, high maintenance
   - Use visual regression testing instead

3. **Database Layer**
   - Use integration tests sparingly
   - Mock database for unit tests
   - Test business logic, not ORM internals

4. **Third-Party Library Internals**
   - Trust library maintainers
   - Test your usage, not library code
   - Integration tests for library interactions

---

## Test Types & Guidelines

### End-to-End (E2E) Tests

**Purpose**: Validate complete user scenarios  
**Coverage**: Extended user stories (not just happy path)  
**Quantity**: Focus on quality, not arbitrary numbers

**Guidelines**:
- Cover all aspects of extended user stories
- Include error scenarios and edge cases
- Test realistic data volumes
- Validate UI + API + Database integration

**Example Extended Story**:
```gherkin
Feature: User Registration with Email Verification

Scenario: Complete registration flow
  Given user visits registration page
  When user enters valid email and password
  And user submits registration form
  Then system creates user account
  And system sends verification email
  And user receives email within 5 minutes
  When user clicks verification link
  Then account is activated
  And user can log in successfully

Scenario: Registration with invalid email
  Given user visits registration page
  When user enters invalid email format
  Then system shows inline validation error
  And submit button remains disabled

Scenario: Registration with existing email
  Given user with email "test@example.com" exists
  When new user tries to register with same email
  Then system shows "Email already registered" error
  And suggests password reset option
```

**E2E Test Checklist**:
- [ ] Happy path covered
- [ ] Error scenarios covered
- [ ] Edge cases covered (boundary conditions)
- [ ] Performance validated (response times)
- [ ] Accessibility checked (keyboard navigation, screen readers)

### Integration Tests

**Purpose**: Test component interactions  
**Coverage**: Business logic + external dependencies  
**Value**: Most valuable for catching real issues

**Guidelines**:
- Test service layer with real database (test DB)
- Test API endpoints with real HTTP requests
- Test external service integrations (use test/sandbox APIs)
- Mock only when necessary (slow/expensive operations)

**Example**:
```typescript
// Integration test for user service
describe('UserService Integration', () => {
  beforeEach(async () => {
    await setupTestDatabase();
  });

  it('creates user and sends welcome email', async () => {
    const user = await userService.create({
      email: 'test@example.com',
      password: 'secure123'
    });

    expect(user.id).toBeDefined();
    expect(user.email).toBe('test@example.com');
    
    // Verify email sent (check email service test inbox)
    const emails = await emailService.getTestInbox();
    expect(emails).toContainEqual(
      expect.objectContaining({
        to: 'test@example.com',
        subject: 'Welcome to App'
      })
    );
  });
});
```

### Unit Tests

**Purpose**: Test isolated business logic  
**Coverage**: Algorithms, calculations, transformations  
**Speed**: Fast, no external dependencies

**Guidelines**:
- Test pure functions
- Mock external dependencies
- Focus on logic, not implementation details
- Skip trivial code (getters, setters, simple assignments)

**Example**:
```typescript
// Unit test for validation logic
describe('Email Validator', () => {
  it('validates correct email format', () => {
    expect(isValidEmail('user@example.com')).toBe(true);
  });

  it('rejects invalid formats', () => {
    expect(isValidEmail('invalid')).toBe(false);
    expect(isValidEmail('@example.com')).toBe(false);
    expect(isValidEmail('user@')).toBe(false);
  });

  it('handles edge cases', () => {
    expect(isValidEmail('')).toBe(false);
    expect(isValidEmail(null)).toBe(false);
    expect(isValidEmail('a'.repeat(255) + '@example.com')).toBe(false);
  });
});
```

---

## Coverage Targets (Realistic)

**NOT about 100% coverage** - Focus on critical paths

### Recommended Targets

| Test Type | Target Coverage | Rationale |
|-----------|----------------|-----------|
| E2E | All extended user stories | Complete scenarios, not line coverage |
| Integration | 60-70% of service layer | Business logic + external interactions |
| Unit | 70-80% of pure functions | Algorithms, calculations, validations |
| Overall | 60-70% code coverage | Quality over quantity |

### What Counts Toward Coverage

✅ **Include**:
- Business logic functions
- Data transformations
- Validation rules
- Error handling
- API endpoints

❌ **Exclude**:
- Configuration files
- Type definitions
- Trivial getters/setters
- Framework boilerplate
- Third-party library code

---

## TDD Cycle (Adapted for Realism)

### Traditional Red-Green-Refactor

1. **Red**: Write failing test
2. **Green**: Write minimum code to pass
3. **Refactor**: Clean up while tests pass

### Realistic Adaptation

1. **Explore**: Test-drive unfamiliar libraries first (throwaway code)
2. **Red**: Write test for business logic (skip boilerplate)
3. **Green**: Implement feature
4. **Refactor**: Clean up with tests as safety net
5. **Validate**: Run E2E tests for complete scenarios

**When to Skip TDD**:
- Prototyping/spike work
- UI layout (use visual regression instead)
- Configuration files
- Simple CRUD operations (covered by integration tests)

---

## Test Organization

### Folder Structure

```
tests/
├── e2e/                    # End-to-end tests
│   ├── auth.spec.ts        # Authentication flows
│   ├── checkout.spec.ts    # Payment processing
│   └── user-journey.spec.ts
├── integration/            # Integration tests
│   ├── user-service.test.ts
│   ├── api-endpoints.test.ts
│   └── database.test.ts
└── unit/                   # Unit tests
    ├── validators.test.ts
    ├── calculators.test.ts
    └── transformers.test.ts
```

### Naming Conventions

- **E2E**: `*.spec.ts` (Playwright, Cypress convention)
- **Integration**: `*.test.ts` (Jest, Vitest convention)
- **Unit**: `*.test.ts`

---

## Test Requirements in tasks.md

**YAML Metadata**:
```yaml
tasks:
  - id: T001
    title: "Implement user registration"
    files_affected:
      - src/services/user-service.ts
      - src/api/auth.ts
    test_required: true
    test_types:
      - e2e: "Complete registration flow with email verification"
      - integration: "UserService.create() with database"
      - unit: "Email validation logic"
```

**Agent Instructions**:
- If `test_required: true`, generate tests BEFORE implementation
- If `test_required: false`, skip test generation (trivial code, config files)
- Always include E2E tests for user-facing features
- Integration tests for service layer
- Unit tests for complex algorithms only

---

## Forbidden Test Patterns

### ❌ Excessive Snapshot Tests
```typescript
// BAD: Brittle, breaks on every style change
it('renders correctly', () => {
  const { container } = render(<Component />);
  expect(container).toMatchSnapshot();
});
```

**Better**: Test behavior, not implementation
```typescript
// GOOD: Tests user-visible behavior
it('displays user name when logged in', () => {
  render(<Header user={{ name: 'Alice' }} />);
  expect(screen.getByText('Alice')).toBeInTheDocument();
});
```

### ❌ Mock-Heavy Tests
```typescript
// BAD: Mocking everything, testing nothing
it('calls service method', () => {
  const mockService = jest.fn();
  const mockDb = jest.fn();
  const mockLogger = jest.fn();
  // ... test that just verifies mocks were called
});
```

**Better**: Integration test with real dependencies
```typescript
// GOOD: Tests real behavior with test database
it('creates user in database', async () => {
  const user = await userService.create({ email: 'test@example.com' });
  const found = await db.users.findById(user.id);
  expect(found.email).toBe('test@example.com');
});
```

### ❌ Testing Implementation Details
```typescript
// BAD: Coupled to implementation
it('calls setState with correct value', () => {
  const wrapper = shallow(<Component />);
  wrapper.instance().handleClick();
  expect(wrapper.state('count')).toBe(1);
});
```

**Better**: Test user-visible behavior
```typescript
// GOOD: Tests what user sees
it('increments counter when button clicked', () => {
  render(<Counter />);
  fireEvent.click(screen.getByRole('button', { name: 'Increment' }));
  expect(screen.getByText('Count: 1')).toBeInTheDocument();
});
```

---

## Performance Testing

**Guidelines**:
- Test realistic data volumes (not just 10 records)
- Validate response times for critical paths
- Use performance budgets (e.g., <200ms p95)
- Profile slow tests and optimize

**Example**:
```typescript
it('handles 1000 users efficiently', async () => {
  const start = Date.now();
  const users = await userService.list({ limit: 1000 });
  const duration = Date.now() - start;

  expect(users.length).toBe(1000);
  expect(duration).toBeLessThan(200); // <200ms requirement
});
```

---

## Test Maintenance

### When to Update Tests

✅ **Update**:
- Business logic changes
- API contract changes
- Bug fixes (add regression test)
- New features (add E2E test)

❌ **Don't Update**:
- Refactoring (tests should still pass)
- UI styling changes (unless behavior changes)
- Internal implementation details

### When to Delete Tests

- Feature removed
- Test duplicates another test
- Test is flaky and low value
- Test tests implementation details (rewrite to test behavior)

---

## Validation Checklist

Before marking feature complete:
- [ ] All extended user stories have E2E tests
- [ ] Critical business logic has unit tests
- [ ] Service layer has integration tests
- [ ] No excessive snapshot tests
- [ ] No mock-heavy tests
- [ ] Tests validate behavior, not implementation
- [ ] Performance requirements validated
- [ ] Tests are maintainable (not brittle)

---

## Tools & Frameworks

**Recommended Stack**:
- **E2E**: Playwright (cross-browser, reliable)
- **Integration/Unit**: Vitest or Jest
- **Assertions**: Testing Library (behavior-focused)
- **Coverage**: c8 or Istanbul

**Avoid**:
- Enzyme (outdated, implementation-focused)
- Excessive mocking libraries (prefer real dependencies)

---

*Based on 2025 TDD research - see specs/005-spec-kit-enhanced/research.md for sources*  
*Philosophy: Realistic scenarios > Coverage metrics*
