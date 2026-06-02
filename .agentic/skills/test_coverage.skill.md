# Name
Test Coverage Skill

# Description
Evaluate test completeness, identify missing scenarios, and recommend new tests.  
Used by the Quality Agent to enforce testing standards.

# Inputs
- Module or feature to analyze
- Optional: known gaps

# Outputs
- Coverage gaps
- Missing unit tests
- Missing integration tests
- Recommended test cases

# Behavior
- Map code modules to corresponding tests.
- Identify untested:
  - Functions
  - Branches
  - Error paths
  - Edge cases
- Recommend:
  - Unit tests for services
  - Integration tests for API routes
- Validate test quality against testing standards.

# Constraints
- Must not generate full code unless requested by the agent.
- Must not modify repository structure.

# Examples
- “Analyze test coverage for item_service.”
- “Identify missing integration tests for the items API.”
- “List untested error paths.”
