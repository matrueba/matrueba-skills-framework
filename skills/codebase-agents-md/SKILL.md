---
name: codebase-agents-md
description: "Analyze an existing codebase and automatically generate a fully populated AGENTS.md file by extracting real information from the source code, config files, and project structure. Use this skill whenever the user wants to generate AI coding rules from their existing code, auto-detect their tech stack and conventions, create an AGENTS.md based on what's already in the repo, reverse-engineer project standards from code, or bootstrap AI context from a codebase. Also triggers when the user says things like 'read my code and create rules', 'generate AGENTS.md from this project', 'detect my stack', 'analyze my codebase for AI context', or 'auto-generate coding guidelines'. This skill differs from create-agents-md in that it requires an existing codebase — it reads and analyzes code rather than offering an empty template."
---

# Codebase Agents MD

This skill reads an existing codebase, extracts its tech stack, conventions, architecture, and patterns, then generates a fully populated `AGENTS.md` — the single source of truth that AI assistants read before generating code.

The key difference from the `create-agents-md` skill: this skill **never** produces a template with placeholders. Every section is filled with concrete values extracted from the actual code. If something cannot be determined, it is marked with `<!-- TODO: Verify -->` so the developer knows to review it.

## Prerequisites

This skill requires a project with existing source code. If the project is empty or has no meaningful code, redirect to the `create-agents-md` skill instead — it has a template mode designed for that scenario.

## Reference Files

- `references/codebase-analysis-guide.md` — Detailed guide with tables of what to look for and where, organized by category (language, framework, database, infra, testing, auth, conventions, etc.). **Read this file before starting Phase 2.**
- `references/agents-md-template.md` — The output template used to structure the generated `AGENTS.md`. **Read this file before starting Phase 3.**

## Execution Flow

### Phase 1: Validate the Project Has Code

Before starting analysis, confirm the project has enough code to analyze:

1. Check for source files in common languages (`.ts`, `.js`, `.py`, `.go`, `.rs`, `.java`, `.cs`, `.rb`, `.php`, etc.)
2. Check for package manifests (`package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `composer.json`, `Gemfile`)
3. If neither exists, stop and tell the developer: "This project doesn't have enough code for automated analysis. Use the `create-agents-md` skill to start with a template instead."

### Phase 2: Deep Codebase Analysis

Read `references/codebase-analysis-guide.md` and work through each section systematically. Don't guess — extract real data from actual files. The guide covers:

1. Language & Runtime
2. Framework Detection
3. Database & Data Layer
4. Infrastructure & DevOps
5. Testing Setup
6. Linting & Formatting
7. Auth & Security
8. Code Conventions (pattern extraction from actual source files)
9. Key Libraries & CLI Commands
10. Specs & Skills
11. UI Design & Style (including `DESIGN.md` detection)

**Strategy:** Scan broadly using file listing and grep to locate relevant files, then read only what matters. Don't try to read every file in a large codebase.

### Phase 3: Generate the AGENTS.md

1. Read the template from `references/agents-md-template.md`.
2. Fill **every** section with concrete values extracted during Phase 2. There should be zero `[placeholder]` markers in the final output — every bracket must be replaced with a real value.
3. For anything that couldn't be determined from the code, use a `<!-- TODO: Verify -->` comment with a best guess and explanation of why the value is uncertain.
4. If a `DESIGN.md` exists, populate section 3.4 (UI Design & Style) referencing it. If the project has a frontend but no `DESIGN.md`, add `<!-- TODO: Create DESIGN.md -->` to suggest the developer creates one.
5. Remove sections that don't apply. A backend-only API project doesn't need "UI Design & Style". A CLI tool doesn't need "State Management". Use judgment — less is better than empty sections.
6. For the **Project Skills** table (section 8), auto-populate it by reading each detected skill's `SKILL.md` frontmatter to get the name and description.
7. Write the file to the project root as `AGENTS.md`.

### Phase 4: Present Results

After generating:

1. Show a **summary table** of what was detected, organized by category:
   ```
   | Category          | Detected Value            |
   |-------------------|---------------------------|
   | Language           | TypeScript 5.4            |
   | Framework          | Next.js 14 (App Router)   |
   | Database           | PostgreSQL (Supabase)     |
   | ...                | ...                       |
   ```
2. List any `<!-- TODO: Verify -->` sections that need human review.
3. List any sections that were removed and why.
4. Remind the developer: "Review the generated `AGENTS.md` and adjust anything I got wrong. This file should live in the project root and be committed to version control."

## Important Guidelines

- **Never fabricate information.** If you scan the code and can't determine the database, don't guess PostgreSQL because it's popular — mark it as TODO.
- **Never expose secrets.** Document env var names (`DATABASE_URL`, `JWT_SECRET`), never their values.
- **Respect existing content.** If an `AGENTS.md` already exists, read it first. Merge your findings with existing content — preserve any custom sections the developer added. Present a diff of what changed.
- **Prioritize evidence.** A value found in code or config beats an assumption. For example, if `package.json` says `"node": ">=18"` but the Dockerfile uses `node:20-alpine`, document both and note the discrepancy with a TODO.
- **Keep it maintainable.** Don't over-specify minor library versions. Focus on the big decisions: major framework, architecture style, key conventions.
