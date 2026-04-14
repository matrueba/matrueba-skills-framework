# mem_search

Tool used to search past memories from persistent memory.

## Usage

Run the search script from the skill directory:

```bash
python <skill-path>/scripts/mem_search.py \
  --db "<project-root>/.agent-memory/memory.db" \
  --query "search terms" \
  [--type "<type>"] \
  [--limit 10]
```

## When to Search Memory

### Reactive Search (user-triggered)

When the user asks to recall something — any variation of "remember", "recall", "what did we decide", or references to past work:

```bash
python <skill-path>/scripts/mem_search.py \
  --db ".agent-memory/memory.db" \
  --query "relevant keywords from user's question"
```

### Proactive Search (agent-triggered)

Search memory **before responding** in these situations:

1. **User's FIRST message** in a session that references the project, a feature, or a problem — extract keywords and search to check for prior work
2. **Starting work on something that might have been done before** — e.g. user asks to refactor auth and you recall there might be prior decisions about auth architecture
3. **User mentions a topic you have no context on** — check if past sessions covered it before asking the user to explain from scratch

## Search Tips

- Use specific keywords: `"JWT auth middleware"` is better than `"authentication"`
- Filter by type when you know what you're looking for: `--type bugfix`
- Increase the limit if a topic has evolved over time: `--limit 20`
- The search uses FTS5 full-text search, so it supports prefix matching (e.g. `config*` matches `configuration`)
