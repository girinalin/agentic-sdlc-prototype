# Deployment Standards

## Docker
- Use multi-stage builds when possible.
- Keep images minimal.
- Expose only required ports.
- Avoid embedding secrets.

## CI/CD
- Run tests on every PR.
- Fail fast on linting or test failures.
- Build Docker image as part of CI.
- Keep workflows readable and modular.

## Environments
- Local: docker-compose
- CI: GitHub Actions
- Production: containerized deployment (future extension)

## Versioning
- Semantic versioning for releases.
