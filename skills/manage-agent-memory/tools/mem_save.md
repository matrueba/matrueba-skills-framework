# mem_save

Tool used to save an observation to persistent memory.

## Usage

Run the save script from the skill directory:

```bash
python <skill-path>/scripts/mem_save.py \
  --db "<project-root>/.agent-memory/memory.db" \
  --title "Short searchable title" \
  --type "<type>" \
  --content "Structured content" \
  [--scope project] \
  [--topic-key "domain/topic"]
```

## When to Save

Call `mem_save` **after each** of these events:

- **Architectural decisions or tradeoffs** — technology choices, pattern selections, design rationale
- **Bug fix completed** — what was wrong, root cause, how you fixed it
- **Non-obvious discovery about the codebase** — hidden coupling, undocumented behavior, surprising side effects
- **Configuration change or environment setup** — env vars, build flags, infrastructure changes
- **Pattern established** — naming conventions, folder structure, coding standards agreed upon
- **User preference or constraint learned** — styling preferences, forbidden approaches, workflow habits

## Save Format

Each memory requires these fields:

| Field | Required | Description |
|-------|----------|-------------|
| `title` | ✅ | Verb + what — short, searchable. e.g. "Fixed N+1 query in UserList", "Chose Zustand over Redux" |
| `type` | ✅ | One of: `bugfix` · `decision` · `architecture` · `discovery` · `pattern` · `config` · `preference` |
| `content` | ✅ | Structured text (see template below) |
| `scope` | ❌ | `project` (default) or `personal` |
| `topic_key` | ❌ | Stable key for evolving decisions, e.g. `architecture/auth-model` |

## Content Template

Structure the `content` field like this:

```
**What**: One sentence — what was done
**Why**: What motivated it (user request, bug, performance, etc.)
**Where**: Files or paths affected
**Learned**: Gotchas, edge cases, things that surprised you (omit if none)
```

## Topic Rules

- Different topics must not overwrite each other (e.g. an architecture decision vs. a bugfix are separate memories even if they touch the same files)
- Reuse the same `topic_key` to **update** an evolving topic instead of creating duplicate observations. When a topic_key is reused, the old entry is updated with the new content and a version counter increments.

## Save Examples

**Example 1 — Decision:**
```bash
python <skill-path>/scripts/mem_save.py \
  --db ".agent-memory/memory.db" \
  --title "Switched from sessions to JWT" \
  --type "decision" \
  --topic-key "architecture/auth-model" \
  --content "**What**: Replaced express-session with jsonwebtoken for auth\n**Why**: Session storage doesn't scale across multiple instances\n**Where**: src/middleware/auth.ts, src/routes/login.ts\n**Learned**: Must set httpOnly and secure flags on the cookie, refresh tokens need separate rotation logic"
```

**Example 2 — Bugfix:**
```bash
python <skill-path>/scripts/mem_save.py \
  --db ".agent-memory/memory.db" \
  --title "Fixed FTS5 syntax error on special chars" \
  --type "bugfix" \
  --content "**What**: Wrapped each search term in quotes before passing to FTS5 MATCH\n**Why**: Users typing queries like 'fix auth bug' would crash because FTS5 interprets special chars as operators\n**Where**: internal/store/store.go — sanitizeFTS() function\n**Learned**: FTS5 MATCH syntax is NOT the same as LIKE — always sanitize user input"
```
