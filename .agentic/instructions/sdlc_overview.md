# SDLC Overview

This repository uses an Agentic SDLC.  
Agents collaborate to plan, implement, validate, and operate software changes.

## Goals
- Maintain a clean, modular architecture.
- Ensure every change includes appropriate unit and integration tests.
- Keep Docker, CI/CD, and deployment scripts aligned with the code.
- Prefer small, incremental, reviewable changes.

## SDLC Stages

### 1. Plan
- Understand requirements
- Update or create a feature spec
- Identify affected components
- Validate feasibility and constraints

### 2. Implement
- Write or update code
- Add unit tests
- Add integration tests
- Update documentation
- Follow coding standards

### 3. Validate
- Run tests
- Improve coverage
- Check architecture and code quality
- Ensure changes meet acceptance criteria

### 4. Operate
- Ensure Docker builds cleanly
- Ensure CI/CD workflows run successfully
- Maintain deployment scripts
- Monitor runtime quality
