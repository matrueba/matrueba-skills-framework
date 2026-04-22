---
name: start-base-requirements
description: Generates a base project requirements template in REQUIREMENTS_TEMPLATE.md. Use this skill when the user wants to start a new project, needs a requirements template, or asks for help structuring their initial product vision and scope.
---

# Start Base Requirements

Generate a standard requirements template for the user to fill out.

## Workflow

### 1. Generate the Template

Create a file named `REQUIREMENTS_TEMPLATE.md` in the current working directory (or the project root) and copy the exact contents of the bundled template from `assets/REQUIREMENTS_TEMPLATE.md` into it.

### 2. Notify the User

After successfully creating the file, inform the user that `REQUIREMENTS_TEMPLATE.md` is ready to be filled out. Encourage them to use the `req-base-improvements` skill once they have completed a draft to get feedback and refinements.
