# Prompt: Add Docker + CI/CD (Enterprise Grade)

## Purpose
Ensure the project is containerized and validated through CI/CD.

## Preconditions
- Backend and/or frontend exist.
- No or incomplete Docker/CI setup.

## Required Inputs
- Runtime requirements
- Build constraints
- Deployment environment (optional)

## Steps
1. Detect language/framework (FastAPI + React).
2. Generate or update:
   - Dockerfile(s)
   - docker-compose.yml
   - GitHub Actions workflow
3. Validate Docker build.
4. Validate CI workflow steps:
   - Install dependencies
   - Run tests
   - Build image
5. Summarize changes.

## Acceptance Criteria
- Docker builds cleanly.
- CI runs successfully.
- No secrets or environment-specific values are hardcoded.

## Output Format
A markdown summary including:
- Files created/updated
- Build/test results
- Next steps
