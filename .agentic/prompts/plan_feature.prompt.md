# Prompt: Plan a Feature (Enterprise Grade)

## Purpose
Create a structured, actionable feature plan aligned with SDLC standards.

## Preconditions
- Developer has a feature request or change request.
- Repository is analyzable by Repo Analyzer Skill.

## Required Inputs
- Feature description
- Business context
- Constraints or assumptions
- Acceptance criteria (if provided)

## Steps
1. Analyze the repository using Repo Analyzer Skill.
2. Identify impacted modules (API, services, models, tests, DevOps).
3. Identify missing components required for the feature.
4. Produce a structured feature plan including:
   - Summary
   - Impacted files
   - Required code changes
   - Required tests (unit + integration)
   - Required DevOps updates
   - Risks and dependencies
5. Validate the plan against SDLC standards.

## Acceptance Criteria
- Plan is complete, unambiguous, and actionable.
- All SDLC stages are represented.
- Tests and DevOps changes are explicitly included.
- No unrelated files or components are included.

## Output Format
A markdown feature plan with the following sections:
- Overview
- Impact Analysis
- Proposed Changes
- Test Strategy
- DevOps Impact
- Risks
- Next Steps
