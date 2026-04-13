---
name: create-agents-md
description: "Generate or update an AGENTS.md file that serves as the AI assistant rulebook for a project. Use this skill whenever the user wants to create an AGENTS.md, set up AI coding guidelines, define project DNA for copilot/AI assistants, establish coding standards and conventions for AI tools, or bootstrap a new project with AI context rules. Also use it when the user mentions 'context for AI', 'copilot instructions', 'AI rules', 'project setup for AI', or wants to document their tech stack and engineering standards in a way that AI assistants can follow."
---

# Create AGENTS.md

This skill generates an `AGENTS.md` file — the single source of truth that AI assistants read before generating code or answering questions about the project.

## Why This Matters

Without an `AGENTS.md`, every AI assistant interaction starts from zero — it guesses the framework, the naming conventions, the preferred libraries. The result is inconsistent code that fights your project's patterns. A well-written `AGENTS.md` eliminates this by giving the AI the same context a senior engineer would have after onboarding.

## Interaction Flow

### Step 1: Determine Project State

Before anything, figure out what you're working with:

1. **Check if `AGENTS.md` already exists** in the project root. If it does, read it — you'll be updating rather than creating from scratch.
2. **Assess whether the project has code**:
   - Look for source files, `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `Dockerfile`, `docker-compose.yml`, `.gitlab-ci.yml`, `.github/workflows/`, and similar markers.
   - Check for existing config files: `.eslintrc`, `.prettierrc`, `tsconfig.json`, `ruff.toml`, `mypy.ini`, etc.
   - If the project has meaningful code, proceed to **Step 2A** (analyze and generate).
   - If the project is empty or minimal (just a README or skeleton), proceed to **Step 2B** (template mode).

### Step 2A: Analyze Codebase and Generate

For projects with existing code, read the codebase to extract real information rather than guessing. This is the core value of the skill — producing an `AGENTS.md` that actually reflects the project.

#### What to Analyze

| Area | Where to Look |
|---|---|
| **Language & version** | File extensions, `tsconfig.json`, `pyproject.toml`, `package.json` engines field, `Dockerfile` base image |
| **Framework** | Import statements, main entry points, `package.json` dependencies, framework config files |
| **Database** | Connection strings (pattern only, not secrets), ORM config, migration files |
| **Infrastructure** | `Dockerfile`, `docker-compose.yml`, CI/CD config files, deployment scripts |
| **Testing** | Test directories, test config (`jest.config`, `pytest.ini`, `vitest.config`), `package.json` scripts |
| **Linting & formatting** | `.eslintrc`, `.prettierrc`, `ruff.toml`, `mypy.ini`, `pyproject.toml [tool.*]` sections |
| **Auth & security** | Auth middleware, JWT usage, session config, RBAC definitions |
| **Architecture patterns** | Folder structure (feature-based vs layer-based), dependency injection, design patterns in code |
| **Naming conventions** | Scan variable/function/class names to detect camelCase, snake_case, PascalCase usage |
| **Error handling** | Try/catch patterns, custom error classes, result types, global handlers |
| **Key libraries** | `package.json` dependencies, `requirements.txt`, import statements for HTTP clients, state management, validation, date handling, UI frameworks |
| **CLI commands** | `package.json` scripts, `Makefile`, `justfile`, shell scripts in `scripts/` |
| **Env var patterns** | `.env.example`, `.env.sample`, docker-compose env definitions |
| **Specs** | `.specs/` directory to confirm the workflow step is applicable |
| **Skills** | Look for `skills/` directories or `.md` files referencing skills to populate the Project Skills table |

#### How to Generate

1. Gather findings from the analysis above.
2. Read the template from `references/agents-md-template.md`.
3. Fill in every section with concrete values from the analysis. Replace all `[placeholder]` markers with real data.
4. For sections where the codebase doesn't provide a clear answer (e.g., architectural principles that aren't explicitly documented), mark them with a `<!-- TODO: Verify -->` comment so the developer knows to check.
5. Remove sections that genuinely don't apply (e.g., "UI/Components" for a CLI tool) rather than leaving empty placeholders.
6. Write the file to the project root as `AGENTS.md`.

### Step 2B: Template Mode (Empty Project)

When the project has no code to analyze:

1. Read the template from `references/agents-md-template.md`.
2. Write it directly to the project root as `AGENTS.md`, keeping all `[placeholder]` markers intact.
3. Tell the developer: "I've created an `AGENTS.md` template with placeholders. Fill in the sections as your project takes shape — the ones marked with `[brackets]` need your input."

### Step 3: Present to Developer

After generating, always:

1. Show a brief summary of what was detected/filled in (for 2A) or what needs filling (for 2B).
2. Highlight any `<!-- TODO: Verify -->` sections that need human review.
3. Remind the developer that this file should live in the project root and be committed to version control.

## Important Guidelines

- **Never fabricate information.** If you can't determine the database type from the code, don't guess — leave the placeholder or add a TODO comment.
- **Never expose secrets.** If you find environment variables, document the pattern (`DATABASE_URL`) not the value.
- **Respect existing content.** If updating an existing `AGENTS.md`, preserve any custom sections the developer added. Merge new findings with existing content rather than overwriting.
- **Keep it maintainable.** The `AGENTS.md` is a living document. Don't over-specify things that change frequently (exact dependency versions of minor libs). Focus on the decisions that matter — major framework, architecture, conventions.
