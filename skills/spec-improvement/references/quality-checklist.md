# Quality Checklist for Specifications

Apply this checklist to every reviewed spec. Each unfulfilled point is a candidate for a proposed improvement.

## Structure

- [ ] Has a clear and descriptive title
- [ ] Includes Author
- [ ] Includes creation date
- [ ] Ticket/Issue

## Essential Content

- [ ] **Goals**: Clearly describes WHAT is to be achieved
- [ ] **Scope**: Defines what is in-scope and what is out-of-scope
- [ ] **Requirements**: Define the main rquirements
- [ ] **User Stories**: Describes the user stories using Gherkin format
- [ ] **Acceptance Criteria**: Defines when it is considered "done"

## Clarity

- [ ] Technical terms are defined or are consistent with the rest of the project
- [ ] There are no ambiguities that allow for multiple interpretations
- [ ] Examples illustrate complex cases
- [ ] File paths, endpoints, or component names are specific

## Completeness

- [ ] Covers relevant error cases or edge cases
- [ ] Defines technical constraints (performance, limits, data formats)
- [ ] Mentions security considerations if applicable
- [ ] Includes wireframes, diagrams, or mockups if the spec is visual

## Consistency

- [ ] Entity names match other project specs
- [ ] Does not contradict architectural decisions documented in other specs
- [ ] APIs or contracts described are compatible with dependent specs

## Implementability

- [ ] A developer can read the spec and start implementing without blocking questions
- [ ] Derived tasks are estimable (not too vague)
- [ ] Input/output data are defined with types and validations