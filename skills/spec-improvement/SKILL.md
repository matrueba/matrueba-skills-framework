---
name: specs-improvement
description: Reviews and improves project specifications located in the ./specs directory. Use when you need to analyze, improve, or complete one or all project specifications. Proposes concrete improvements, identifies ambiguities, and asks the user questions to refine each spec. It can also be used to create a new spec from scratch.
---

# Specifications Improvement

Analyze the project specifications in `./specs` and generate structured improvement proposals, also formulating questions for the user to complete and refine each spec.

## Review Workflow

1. **Determine the scope:**
   **Review all specs?** → List all files in `./specs`, read each one, and generate a summary of findings.
   **Review a specific spec?** → Read the file indicated by the user.

2. **Analyze each spec** applying the quality checklist → See [quality-checklist.md](references/checklist-calidad.md)

3. **Generate an improvement proposal** using the output format defined below.

4. **Ask questions** to the user to complete missing or ambiguous information.

5. **Apply improvements** after user confirmation, updating the spec file.

## Output Format

For each reviewed spec, generate the following output:

```markdown
# Review: [Spec Name]

## General Status

[🟢 Complete | 🟡 Needs improvements | 🔴 Incomplete]

## Summary

[Brief description of what the spec covers and its current state]

## Strengths

- [What is well defined]

## Proposed Improvements

### High Priority

1. [Improvement with justification]

### Medium Priority

1. [Improvement with justification]

### Low Priority

1. [Improvement with justification]

## Missing Sections

- [Sections that should be included]

## Questions for the User

1. [Concrete question to clarify ambiguities or complete the spec]
2. [...]


## Analysis Rules

- Check that each spec has: a clear objective, defined scope, use cases, acceptance criteria, and constraints or dependencies.

- Identify ambiguities that could cause implementation issues.

- Detect contradictions between different specs.

- Verify that entity names (routes, components, APIs) are consistent across specs.

- Limit questions for the user to a maximum of 3 per spec to avoid overwhelming them.

- Prioritize questions by impact: start with those that block implementation.