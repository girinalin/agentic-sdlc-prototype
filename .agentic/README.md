# Agentic SDLC Framework

This repository implements an **Agentic Software Development Lifecycle (SDLC)** designed to help developers plan, implement, validate, and operate software changes using a structured, multi‑agent workflow.

The system is built using:
- GitHub Copilot Agent Skills
- Declarative agents
- Enterprise SDLC standards
- Modular prompts, skills, and instructions

This README explains how your team can use the agentic system effectively.

---

# 1. Purpose

The Agentic SDLC provides:
- A **guided workflow** for developers
- A **consistent, repeatable process** for changes
- A **menu of agentic capabilities**
- A **clear mapping** between tasks → agents → skills → prompts
- A **standardized way** to plan, implement, test, and operate features

It ensures:
- High‑quality code
- Strong test coverage
- Clean architecture
- Reliable DevOps pipelines

---

# 2. Folder Structure

.agentic/
│
├── instructions/   → SDLC rules, coding standards, testing standards
├── prompts/        → Task-specific instructions for agents
├── skills/         → Declarative capabilities used by agents
└── agents/         → Planner, Implementer, Quality, Ops agents
Each folder plays a specific role in the agentic workflow.

---

# 3. How Developers Use the System

Developers interact with the system through the **Task Selector**:
.agentic/task_selector.md


This file provides a **menu of available tasks**, such as:

- Plan a feature  
- Implement an endpoint  
- Add tests  
- Add Docker + CI  
- Analyze the repository  

Each task links to the correct **prompt** and triggers the correct **agent**.

---

# 4. Agents Overview

## Planner Agent
- Converts feature requests into structured plans  
- Uses Repo Analyzer Skill  
- Produces: impact analysis, test strategy, DevOps impact, risks  

## Implementer Agent
- Writes code following the feature plan  
- Uses Scaffolding Skill  
- Generates API routes, models, services, tests  

## Quality Agent
- Ensures correctness and test coverage  
- Uses Test Coverage Skill  
- Identifies missing tests and quality issues  

## Ops Agent
- Maintains Docker, CI/CD, and DevOps workflows  
- Uses Scaffolding + Repo Analyzer Skills  
- Ensures build/test/deploy reliability  

---

# 5. Skills Overview

## Repo Analyzer Skill
Analyzes repository structure, detects missing components, identifies SDLC gaps.

## Test Coverage Skill
Evaluates test completeness, identifies missing scenarios, recommends new tests.

## Scaffolding Skill
Generates or updates:
- API routes  
- Models  
- Services  
- Unit tests  
- Integration tests  
- Dockerfile  
- CI workflows  

---

# 6. Prompts Overview

Prompts define **task-specific workflows** for each agent.

### plan_feature.prompt.md
Creates a structured feature plan.

### implement_endpoint.prompt.md
Implements API endpoints with tests.

### add_tests.prompt.md
Improves test coverage and quality.

### add_docker_ci.prompt.md
Adds or updates Docker + CI/CD.

All prompts follow enterprise-grade structure:
- Purpose  
- Preconditions  
- Required Inputs  
- Steps  
- Acceptance Criteria  
- Output Format  

---

# 7. Instructions Overview

Instructions define the **rules and standards** that all agents must follow.

### sdlc_overview.md
Defines the 4 SDLC stages:
- Plan  
- Implement  
- Validate  
- Operate  

### coding_standards.md
Defines architecture, naming, API, service, and model conventions.

### testing_standards.md
Defines unit/integration test requirements and coverage expectations.

### deployment_standards.md
Defines Docker, CI/CD, and environment standards.

---

# 8. Typical Developer Workflow

### Step 1 — Developer selects a task  
Open `.agentic/task_selector.md` and choose a task.

### Step 2 — Developer opens the corresponding prompt  
Example:  
`prompts/implement_endpoint.prompt.md`

### Step 3 — Developer provides context  
Feature description, requirements, constraints.

### Step 4 — Agent executes the workflow  
Planner → Implementer → Quality → Ops  
depending on the task.

### Step 5 — Developer reviews and commits  
All changes follow SDLC standards automatically.

---

# 9. Extending the System

You can add:
- New agents  
- New skills  
- New prompts  
- New instructions  
- New SDLC stages  
- New domain-specific workflows  

To add a new capability:
1. Create a new skill in `skills/`
2. Create a new prompt in `prompts/`
3. Add a new agent or update an existing one
4. Add the task to `task_selector.md`

---

# 10. Best Practices

- Always start with the **Planner Agent** for new features.
- Never implement code without a feature plan.
- Every change must include tests.
- Every feature must consider DevOps impact.
- Keep agents small, focused, and declarative.
- Avoid modifying unrelated files.
- Follow all standards in the `instructions/` folder.

---

# 11. Summary

This Agentic SDLC system gives your team:

- A **guided, menu-driven workflow**
- A **multi-agent architecture**
- A **repeatable, high-quality development process**
- A **scalable foundation** for future automation

Your repository is now fully agentic and ready for collaborative, standards-driven development.



