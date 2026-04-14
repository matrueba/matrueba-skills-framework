---
name: manage-agent-memory
description: "Persistent memory system that saves and retrieves observations across sessions using SQLite with FTS5 full-text search. Use this skill proactively: save memories after architectural decisions, bug fixes, codebase discoveries, config changes, established patterns, or learned user preferences. Search memories when the user asks to recall past work, when starting tasks that may overlap with prior work, when the user references a topic you lack context on, or on the user's FIRST message to check for relevant prior work. Also trigger when the user says 'remember', 'recall', 'what did we do', 'have we done this before', or references past sessions."
---

# Manage Agent Memory

A persistent memory system backed by SQLite with FTS5 full-text search. It provides two tools — `mem_save` and `mem_search` — to store and retrieve observations across sessions.

The database lives at `<project-root>/.agent-memory/memory.db` and persists between sessions.

## Tools

The skill provides two tools for you to interact with the database. Please refer to their respective `.md` files in the `tools/` directory for syntax, usage examples, and triggering rules:

- **`mem_save`** ([tools/mem_save.md](tools/mem_save.md)): Save an observation. Use proactively for decisions, bug fixes, patterns, etc.
- **`mem_search`** ([tools/mem_search.md](tools/mem_search.md)): Search past memories. Use proactively on first contact, or reactively when the user asks.

---

## Database Location

The memory database is stored at:

```
<project-root>/.agent-memory/memory.db
```

The scripts automatically create the database and its directory if they don't exist. Add `.agent-memory/` to `.gitignore` — memories are local to the developer, not shared via version control.
