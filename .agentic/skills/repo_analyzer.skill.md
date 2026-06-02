# Name
Repo Analyzer Skill

# Description
Analyze the repository structure, identify missing components, detect SDLC gaps, and provide actionable recommendations.  
This skill is used by Planner, Quality, and Ops agents to understand the current state of the codebase.

# Inputs
- Optional: area of focus (api, services, models, tests, docker, ci, architecture)

# Outputs
- Repository summary
- Missing components
- SDLC gaps
- Recommended next steps

# Behavior
- Scan the repository structure.
- Identify presence/absence of:
  - API modules
  - Service layer logic
  - Models
  - Unit tests
  - Integration tests
  - Dockerfile
  - docker-compose
  - GitHub Actions workflows
  - Documentation
- Detect architectural inconsistencies.
- Identify outdated or unused files.
- Recommend 2–5 improvements aligned with SDLC standards.

# Constraints
- Must not modify files.
- Must not generate code.
- Must not assume frameworks beyond what exists in the repo.

# Examples
- “Analyze the repo and list missing tests.”
- “Identify SDLC gaps in the backend folder.”
- “What components are missing for a new feature?”
