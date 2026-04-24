---
name: start-feature-requirements
description: Generates a feature requirements template in FEATURE_REQUIREMENTS_TEMPLATE.md. Use this skill when the user wants to start specifying a new feature for an existing project, needs a feature template, or asks for help structuring their feature vision and scope.
---

# Start Feature Requirements

Generate a standard feature requirements template for the user to fill out.

## Workflow

### 1. Generate the Template

Create a file named `FEATURE_REQUIREMENTS_TEMPLATE.md` in the current working directory (or the project root) and copy the exact contents of the bundled template from `assets/FEATURE_REQUIREMENTS_TEMPLATE.md` into it.

### 2. Notify the User

After successfully creating the file, inform the user that `FEATURE_REQUIREMENTS_TEMPLATE.md` is ready to be filled out. Encourage them to use the requirements improvements skill once they have completed a draft to get feedback and refinements.
