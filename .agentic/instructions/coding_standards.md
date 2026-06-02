# Coding Standards

## General
- Prefer small, composable modules.
- Use clear naming and avoid unnecessary abstraction.
- Include docstrings or comments for non-obvious logic.
- Keep functions pure unless side effects are required.

## API (FastAPI)
- Use Pydantic models for request/response validation.
- Validate all inputs.
- Return typed, predictable responses.
- Use dependency injection for services and DB access.

## Services
- Business logic must live in services, not routes.
- Services must be unit-testable without FastAPI.

## Models
- Use Pydantic for DTOs.
- Keep domain models simple and explicit.

## File Structure
- `api/` → routing, dependencies
- `services/` → business logic
- `models/` → Pydantic models
- `db/` → persistence layer
