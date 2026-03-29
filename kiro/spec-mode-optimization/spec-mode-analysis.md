## Spec Mode Analysis Prompt

```
You are analyzing an existing codebase before implementing a feature enhancement or bug fix.

Your goal is to understand the current system behavior, identify reusable implementations, and define precise boundaries for change before any code modification is proposed.

Do NOT propose implementation or generate tasks yet.

Produce the analysis in the exact structure below.

Focus only on the components relevant to the requested change.

If information is missing, infer carefully from the repository structure and explain your reasoning.

Return the output in the following format:

--------------------------------------------------

ANALYSIS

1. Existing Behavior
- Explain how the current system implements the relevant functionality.
- Describe the execution flow and major interactions between components.
- Identify where the current behavior is defined and how requests or data move through the system.

2. Relevant Components
List the parts of the codebase involved in the current behavior.

Include:
- files
- functions
- classes
- modules
- services
- APIs

Explain the role of each component in the current implementation.

3. Reusable Implementations
Identify existing logic that could support the requested change.

Examples:
- helper utilities
- shared services
- existing APIs
- middleware
- caching layers
- validation logic
- data access abstractions

Explain how these can be reused instead of creating new implementations.

4. Change Boundary
Define the minimal scope of modification required.

Specify clearly:

What SHOULD change:
- specific functions
- modules
- behaviors

What MUST NOT change:
- unrelated modules
- existing interfaces
- external contracts
- stable production behavior

The boundary must be explicit so that modifications remain localized.

5. Target Behavior
Describe the expected behavior after the change.

Include:
- new functionality
- new execution flow (if any)
- conditions under which the new behavior applies
- expected outputs or responses.

This should represent the intended outcome of the enhancement.

6. Preservation Constraints
List the invariants that must remain unchanged after the modification.

Examples:
- API response schema
- authentication behavior
- authorization rules
- database schema
- existing logging and monitoring
- performance characteristics

Ensure that when the new feature condition does NOT apply, the system behaves exactly as it does today.

--------------------------------------------------

Important Rules

- Prefer modifying existing components rather than introducing new ones.
- Avoid unnecessary refactoring.
- Keep the change surface minimal.
- Preserve existing system behavior wherever possible.
- Clearly identify risks or areas where unintended changes could occur.

Only produce the analysis above. Do not generate implementation or tasks yet.
```

## DELTA Spec Prompt

```
You are generating a DELTA SPEC for modifying an existing codebase.

Your goal is to define ONLY the minimal set of changes required to implement the requested feature enhancement or bug fix.

Do NOT redesign the system.
Do NOT refactor unrelated modules.
Do NOT introduce new architecture unless absolutely necessary.

Assume the current system works correctly and should remain unchanged except where explicitly required.

Use the prior ANALYSIS as the source of truth.

Focus only on the smallest set of changes needed to achieve the target behavior.

Return the output in the following structure:

--------------------------------------------------

DELTA SPEC

1. Change Objective
Describe the exact problem being solved or feature being added.

Explain the minimal behavioral change required.

2. Trigger Condition
Define when the new behavior should activate.

Examples:
- specific API endpoint
- specific request parameter
- specific state condition
- specific error scenario

When this condition is NOT met, the system must behave exactly as it currently does.

3. Minimal Code Changes
List only the code locations that require modification.

For each change include:
- file
- function/class
- exact purpose of modification

Example format:

File:
Function/Class:
Change Required:
Reason:

Avoid introducing new files unless unavoidable.

4. Reused Components
List existing utilities, services, or modules that will be reused.

Explain how they support the change.

Do NOT create duplicate logic if an existing component can be used.

5. Execution Plan
Provide a small sequence of implementation tasks.

Tasks must be:
- minimal
- localized
- ordered

Each task should modify only the necessary component.

Example:

Task 1: Modify cache lookup logic in product_service.py  
Task 2: Add cache write after DB query  
Task 3: Add cache TTL configuration

6. Preservation Rules
Explicitly list what must remain unchanged.

Examples:
- API response schema
- existing authentication logic
- database schema
- logging structure
- performance-critical paths

These constraints must be enforced during implementation.

7. Risk Check
Identify possible risks such as:
- unintended side effects
- regression points
- concurrency issues
- caching inconsistencies

Explain how the implementation plan avoids them.

--------------------------------------------------

Important Rules

- Keep the change surface minimal.
- Modify existing components rather than introducing new abstractions.
- Avoid broad refactoring.
- Preserve current behavior outside the trigger condition.
- Ensure the change is reversible and isolated.

The output should represent the smallest safe modification needed to implement the feature.
```

## 3-Prompt Workflow for Kiro
Analyze → Delta Spec → Execute

  - Step 1: Analysis
Run the Spec Mode Analysis Prompt
  - Step 2: Delta Spec Generation
Using the above analysis, generate a DELTA spec and task list for implementing the target behavior
  - Step 3: Execution