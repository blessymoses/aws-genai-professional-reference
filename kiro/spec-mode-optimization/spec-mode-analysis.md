# Spec Mode Analysis Prompt

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
## Step 1: Analysis
Run the Spec Mode Analysis Prompt

## Step 1: Spec Generation
```
Using the above analysis, generate a minimal spec and task list
for implementing the target behavior.
```