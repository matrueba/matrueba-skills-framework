---
name: spec-generator
description: Creates technical specifications from feature requirements using a standardized template. Use this skill when the user asks to generate a spec, create a specification document, or implement a spec based on input requirements.
---

# spec-generator

This skill generates standardized technical specifications based on raw feature requirements.

## Interaction Flow

Before generating the specification, you MUST ensure you have all the necessary information. If the user invokes this skill but does not provide all of the following details, **you must explicitly ask them for the missing information before proceeding**:

1. **Requirements**: The raw requirements, user stories, or details about what needs to be built.
   - If this information is not provided when you are called, you must explicitly inform the user in the chat about the two possibilities: they can either provide the requirements directly in the chat, or they can direct you to read an existing requirement document located in the `.project-requirements/` directory.
   - If the user provides a file path in `.project-requirements/`, you must read that file to obtain the requirements.
2. **Spec Name**: A short, descriptive name for the feature (e.g., "user authentication", "payment gateway").
3. **Spec Type**: Whether this is a completely new feature (`new`) or a modification to an existing one (`changes`).
   - Note: If the requirements are provided via a file in the `.project-requirements/` directory, automatically infer the Spec Type as `new` without asking.

Do not make assumptions about missing information unless the user explicitly tells you to do so (except for the Spec Type inference mentioned above). Once you have all three pieces of information, proceed with drafting the specification.

## How to use this skill

1. **Draft the specification**:
   - Read the template located at `assets/template.md` and use it as the base structure for your specification.
   - Fill in all the relevant sections (Summary, UX & Requirements, Technical Design, Cross-Cutting Concerns, Edge Cases, Testing Strategy, Execution Plan) based on the provided requirements.
   - You may omit specific sections from the template _only_ if they are strictly not applicable based on the requirements, but never omit mandatory sections like UX & Requirements.
2. **Save the specification**:
   - For a **new** feature (`new`), create the specification file at `.specs/new/<feature-name>/spec.md`.
   - For a **change** to an existing feature (`changes`), create the specification file at `.specs/changes/<feature-name>/spec.md`.
   - Ensure the `<feature-name>` directory is properly formatted (using kebab-case, e.g., `user-authentication`).
3. **Notify the User**
   - After successfully creating the `.specs/<spec-name>/spec.md`, suggest the user use the `spec-improvement` skill to get feedback and refinements.
