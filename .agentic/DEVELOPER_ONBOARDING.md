# Developer Onboarding Guide  
Welcome to the Agentic SDLC Framework

This guide will help you quickly understand how to work inside this repository using the **Agentic Software Development Lifecycle (SDLC)**.  
The goal is to make development **faster, safer, more consistent, and more collaborative** by using structured agents, skills, prompts, and standards.

---

# 1. What Is the Agentic SDLC?

The Agentic SDLC is a development workflow where **AI agents assist developers** across the entire lifecycle:

- Planning  
- Implementation  
- Testing  
- DevOps / Operations  

Each agent is specialized and follows strict rules, standards, and templates defined in the `.agentic/` folder.

This ensures:
- Consistent code quality  
- Predictable architecture  
- Strong test coverage  
- Reliable DevOps pipelines  
- Faster onboarding for new developers  

---

# 2. How the System Is Organized

.agentic/
│
├── instructions/   → SDLC rules, coding standards, testing standards
├── prompts/        → Task-specific workflows
├── skills/         → Declarative capabilities
└── agents/         → Planner, Implementer, Quality, Ops


Each folder plays a specific role:

### **instructions/**
Defines the rules everyone must follow:
- Coding standards  
- Testing standards  
- Deployment standards  
- SDLC overview  

### **prompts/**
Task-specific workflows for agents:
- Plan a feature  
- Implement an endpoint  
- Add tests  
- Add Docker + CI  

### **skills/**
Reusable capabilities:
- Repo Analyzer  
- Test Coverage  
- Scaffolding  

### **agents/**
The four core agents:
- Planner  
- Implementer  
- Quality  
- Ops  

---

# 3. The Task Selector (Start Here)

Every developer begins with:

.agentic/task_selector.md


This file acts as a **menu** of available tasks.

Examples:
- “Plan a new feature”
- “Implement an API endpoint”
- “Add missing tests”
- “Add Docker + CI”
- “Analyze the repository”

Each task links to the correct **prompt** and triggers the correct **agent**.

---

# 4. Typical Developer Workflow

## Step 1 — Choose a Task  
Open `.agentic/task_selector.md` and select what you want to do.

## Step 2 — Open the Corresponding Prompt  
Example:  
`prompts/implement_endpoint.prompt.md`

## Step 3 — Provide Context  
Describe:
- What you want to build  
- Requirements  
- Constraints  
- Acceptance criteria  

## Step 4 — Agent Executes the Workflow  
Depending on the task:
- Planner Agent creates a feature plan  
- Implementer Agent writes code + tests  
- Quality Agent checks coverage  
- Ops Agent updates Docker/CI  

## Step 5 — Review and Commit  
You review the output, apply changes, and commit.

---

# 5. When to Use Each Agent

### **Planner Agent**
Use when:
- Starting a new feature  
- Updating requirements  
- Designing architecture changes  

### **Implementer Agent**
Use when:
- Writing new code  
- Adding endpoints  
- Creating models/services  
- Adding tests  

### **Quality Agent**
Use when:
- Improving test coverage  
- Reviewing code quality  
- Checking for missing tests  

### **Ops Agent**
Use when:
- Adding Docker  
- Updating CI/CD  
- Improving DevOps pipelines  

---

# 6. Development Standards (Must Follow)

### Coding Standards
- Keep modules small and composable  
- Use Pydantic models for API schemas  
- Keep business logic in services  
- Avoid modifying unrelated files  

### Testing Standards
- Every feature requires tests  
- Unit tests for services  
- Integration tests for API routes  
- Tests must be deterministic  

### Deployment Standards
- Docker images must be minimal  
- CI must run tests on every PR  
- No secrets in code  

---

# 7. How to Extend the Agentic System

You can add:
- New agents  
- New skills  
- New prompts  
- New SDLC rules  
- New domain workflows  

To add a new capability:
1. Create a new skill in `skills/`
2. Create a new prompt in `prompts/`
3. Add or update an agent in `agents/`
4. Add the task to `task_selector.md`

---

# 8. Best Practices for Developers

- Always start with the **Planner Agent** for new features  
- Never implement code without a plan  
- Always include tests  
- Keep changes small and focused  
- Follow all standards in `.agentic/instructions/`  
- Use agents to maintain consistency  

---

# 9. Summary

This Agentic SDLC framework gives your team:
- A guided workflow  
- A multi-agent architecture  
- A consistent development process  
- A scalable foundation for automation  

Welcome aboard — you’re now part of an agentic development workflow designed for clarity, quality, and speed.
