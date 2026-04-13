---
name: generate-commit-message
description: "Analyze staged or unstaged changes since the last commit and propose a commit message following the Conventional Commits 1.0.0 specification. Use this skill whenever the user asks for a commit message, wants help writing a commit, asks to describe recent changes for a commit, or mentions 'conventional commit'. Also use it when the user says things like 'what should I commit', 'summarize my changes for git', or 'prepare a commit'."
compatibility: "Requires: git repository with at least one prior commit"
---

# Generate Commit Message

Analyze code changes since the last commit and propose a concise commit message following [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

## Conventional Commits Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type       | When to use                                      |
|------------|--------------------------------------------------|
| `feat`     | A new feature                                    |
| `fix`      | A bug fix                                        |
| `docs`     | Documentation only changes                       |
| `style`    | Formatting, semicolons, etc. (no logic change)   |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf`     | Performance improvement                          |
| `test`     | Adding or correcting tests                       |
| `build`    | Build system or external dependencies            |
| `ci`       | CI configuration changes                         |
| `chore`    | Other changes that don't modify src or test files|
| `revert`   | Reverts a previous commit                        |

### Rules

- The description is lowercase, imperative mood, no period at the end
- Scope is optional and describes the section of the codebase affected (e.g., `auth`, `api`, `parser`)
- Breaking changes append `!` after type/scope and optionally include a `BREAKING CHANGE:` footer
- Keep the subject line under 72 characters

## Workflow

### Step 1: Detect Changes

Run `scripts/analyze_changes.sh` from the skill directory to collect structured change data:

```bash
bash <skill-path>/scripts/analyze_changes.sh [repo-path]
```

If the script is unavailable, gather changes manually:

1. Check for staged changes first: `git diff --cached --stat` and `git diff --cached`
2. If nothing is staged, check unstaged changes: `git diff --stat` and `git diff`
3. If no diff at all, check untracked files: `git status --short`

### Step 2: Classify the Change

Analyze the diff output and determine:

1. **Type** — What kind of change is this? Use the types table above. If changes span multiple types, pick the most significant one or suggest splitting into multiple commits.
2. **Scope** — Which part of the codebase is affected? Derive from the directory or module where most changes occur. Omit if changes are broad or scope is unclear.
3. **Description** — Summarize what the change does in imperative mood ("add", "fix", "remove", not "added", "fixed", "removed").

### Step 3: Determine if a Body is Needed

Add a body only when the description alone doesn't convey enough context:

- The "why" behind the change is non-obvious
- Multiple files changed for a single logical reason
- A workaround or trade-off needs explanation

Keep the body to 1-3 lines. Don't repeat the description.

### Step 4: Detect Breaking Changes

If any of these are true, mark it as a breaking change:

- Public API signatures changed
- Configuration format changed
- Removed or renamed exported symbols
- Database schema changes that aren't backward-compatible

### Step 5: Present the Commit Message

Present the proposed message in a code block so the user can copy it directly:

```
type(scope): description
```

If the changes are complex or ambiguous, present 2-3 alternatives ranked by fit and briefly explain the reasoning.

### Step 6: Offer to Commit

After the user approves, offer to run the commit command:

```bash
git commit -m "type(scope): description"
```

For messages with a body:

```bash
git commit -m "type(scope): description" -m "body text here"
```

## Examples

**Example 1 — Simple feature:**
```
feat(auth): add JWT token refresh endpoint
```

**Example 2 — Bug fix with scope:**
```
fix(parser): handle empty arrays in config validation
```

**Example 3 — Breaking change:**
```
feat(api)!: change user endpoint response format

BREAKING CHANGE: /api/users now returns paginated results with a `data` wrapper object
```

**Example 4 — Docs only:**
```
docs: update installation instructions in README
```

**Example 5 — Multiple small changes:**
```
chore: update dependencies and fix linting warnings
```

## Guidelines

- Prefer one commit per logical change. If the diff contains unrelated work, suggest splitting.
- Don't invent details that aren't in the diff.
- When in doubt between two types, prefer the one that better describes the user-facing impact.
- Always use English for the commit message, regardless of the conversation language.
