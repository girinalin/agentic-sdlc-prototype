# Name
Scaffolding Skill

# Description
Generate or update project scaffolding for APIs, services, models, tests, Docker, and CI/CD.  
Used by Implementer and Ops agents to create consistent, standards‑aligned components.

# Inputs
- Component type (api, model, service, test, docker, ci)
- Requirements or feature description

# Outputs
- Generated scaffolding code
- File paths and summaries
- Test templates
- DevOps templates

# Behavior
- Create or update:
  - API routes
  - Pydantic models
  - Service layer modules
  - Unit tests
  - Integration tests
  - Dockerfile
  - docker-compose.yml
  - GitHub Actions workflows
- Ensure generated code:
  - Follows coding standards
  - Includes tests
  - Is minimal and modular
  - Does not modify unrelated files

# Constraints
- Must follow SDLC standards.
- Must not introduce unused dependencies.
- Must not generate overly complex abstractions.

# Examples
- “Generate scaffolding for a new items endpoint.”
- “Create Docker + CI scaffolding for the backend.”
- “Add unit test scaffolding for a new service.”
