# Testing Standards

## Principles
- Every feature must include tests.
- Tests must be deterministic and isolated.
- Prefer meaningful coverage over line coverage.

## Unit Tests
- Test services and pure logic.
- Mock external dependencies.
- Cover success and failure paths.

## Integration Tests
- Use FastAPI TestClient.
- Test full request → response flow.
- Validate status codes and payloads.

## Structure
- `tests/unit/` for service-level tests
- `tests/integration/` for API-level tests

## Coverage
- Minimum 80% coverage recommended.
- Critical modules should approach 100%.
