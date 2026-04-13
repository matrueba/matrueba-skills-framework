---
name: create-requirements
description: Acts as a Tech Lead or Product Manager to generate a product requirements sheet. It has two modes — default (delivers the empty template to the user) and interactive (guided interview). Use this skill whenever the user asks you to create requirements for a functionality, document a new feature (such as "Metadata" or others), or if they mention they want to write the scope and impact of a new development.
---

# Create Requirements Sheet

This skill has **two modes of operation**. Your first action must be to determine which mode to use.

## Mode Selection

- If the user has **already specified** the mode (`default` or `interactive`), use it directly without asking.
- If the user has **NOT specified** the mode, **ask** them which one they prefer before continuing:
  > Which mode do you prefer?
  > - **Default**: I'll give you the empty template in `.project-requirements/` for you to complete at your own pace.
  > - **Interactive**: I'll guide you through a step-by-step interview and I'll write the final document.

---

## Default Mode

In this mode, the agent **does not ask questions**. It simply delivers the template ready to be completed by the user.

### Workflow

1. Read the `assets/template.md` file of this skill.
2. Create the file in `.project-requirements/<feature-name>.md` (creating the directory if it doesn't exist). If the user hasn't provided a feature name, use a generic name like `new-feature.md` and communicate it.
3. Inform the user of the path of the created file and instruct them to complete it with their feature's information.

### Default Mode Restrictions

- **DO NOT** fill in any fields in the template. Leave it exactly as it is in `assets/template.md`.
- **DO NOT** ask questions to the user (except for the feature name if it wasn't provided).

---

## Interactive Mode

In this mode, the agent acts as a Tech Lead/PM who **guides the user through a conversational interview** to gather information and draft the final document.

### Workflow

1. **Opening:**
   Introduce yourself and state that you will ask a series of guided questions to complete the feature requirements sheet.
2. **Interview Phase:**
   Ask questions grouped in small blocks (2 or 3 questions at most) to not overwhelm the user. Use the sections of `assets/template.md` as a guide for your questions. Wait for the user to answer each block before moving to the next one.
   *If the user doesn't know an answer or asks for a suggestion, you can make constructive proposals.*
3. **Final Document Generation:**
   Once all information is gathered or the user considers it sufficient, write the document in Markdown format using EXACTLY the structure of the template in `assets/template.md`. **Mandatorily**, you must save this document in the `.project-requirements/` folder of the project (for example: `.project-requirements/metadata.md`), creating the directories if they don't exist.

### Questions to Gather (by Recommended Blocks)

**Block 1: Basics**

- Name of the Functionality (e.g., Metadata)
- Current status (Ideation / Design / Ready for Development)
- Product Owner (PM/PO) and Tech Lead

**Block 2: Context and Scope**

- The Problem to Solve (Why are we building this?) and The final Objective.
- In-Scope (What we are going to do) and Out-of-Scope (What we are NOT going to do in this phase).

**Block 3: Use Cases**

- Entry Points (How does the user discover/access this?).
- Happy Path (Success flow).
- Edge Cases / Error Handling.

**Block 4: Requirements and Design**

- Functional Requirements (Backend/Logic, Frontend/UI, Configurable).
- Architectural Impact (Integration with existing system, Dependencies, Data migration).

**Block 5: Closing**

- Quality Attributes (Performance, Security, Backward Compatibility).
- Telemetry/Success Metrics.
- Launch Strategy (Rollout, Feature flags).

### Interactive Mode Restrictions

- **NEVER** invent requirements that the user has not mentioned or approved.
- If the user doesn't know something, propose a standard solution and ask them to validate it.

---

## Final Document Template

In both modes, the generated file must use the `assets/template.md` file that accompanies this skill as a base, maintaining exactly its format.
