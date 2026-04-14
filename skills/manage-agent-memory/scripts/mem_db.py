"""
mem_db.py — Shared database layer for manage-memory skill.

Creates and manages a SQLite database with FTS5 full-text search
for persistent memory storage across agent sessions.
"""

import os
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def get_connection(db_path: str) -> sqlite3.Connection:
    """Open (or create) the memory database and ensure the schema exists."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    _ensure_schema(conn)
    return conn


def _ensure_schema(conn: sqlite3.Connection) -> None:
    """Create tables and FTS5 virtual table if they don't exist."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS memories (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT    NOT NULL,
            type        TEXT    NOT NULL,
            scope       TEXT    NOT NULL DEFAULT 'project',
            topic_key   TEXT,
            content     TEXT    NOT NULL,
            version     INTEGER NOT NULL DEFAULT 1,
            created_at  TEXT    NOT NULL,
            updated_at  TEXT    NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_memories_type
            ON memories(type);

        CREATE INDEX IF NOT EXISTS idx_memories_topic_key
            ON memories(topic_key);

        -- FTS5 virtual table for full-text search across title and content
        CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts USING fts5(
            title,
            content,
            type,
            content='memories',
            content_rowid='id',
            tokenize='porter unicode61'
        );

        -- Triggers to keep FTS index in sync with the main table
        CREATE TRIGGER IF NOT EXISTS memories_ai AFTER INSERT ON memories BEGIN
            INSERT INTO memories_fts(rowid, title, content, type)
            VALUES (new.id, new.title, new.content, new.type);
        END;

        CREATE TRIGGER IF NOT EXISTS memories_ad AFTER DELETE ON memories BEGIN
            INSERT INTO memories_fts(memories_fts, rowid, title, content, type)
            VALUES ('delete', old.id, old.title, old.content, old.type);
        END;

        CREATE TRIGGER IF NOT EXISTS memories_au AFTER UPDATE ON memories BEGIN
            INSERT INTO memories_fts(memories_fts, rowid, title, content, type)
            VALUES ('delete', old.id, old.title, old.content, old.type);
            INSERT INTO memories_fts(rowid, title, content, type)
            VALUES (new.id, new.title, new.content, new.type);
        END;
    """)


def save_memory(
    conn: sqlite3.Connection,
    title: str,
    mem_type: str,
    content: str,
    scope: str = "project",
    topic_key: str | None = None,
) -> dict:
    """
    Save or update a memory.

    If a topic_key is provided and an existing memory has the same topic_key,
    the existing row is updated (content replaced, version incremented).
    Otherwise a new row is inserted.

    Returns a dict with the saved memory's metadata.
    """
    now = datetime.now(timezone.utc).isoformat()

    if topic_key:
        row = conn.execute(
            "SELECT id, version FROM memories WHERE topic_key = ?",
            (topic_key,),
        ).fetchone()

        if row:
            new_version = row["version"] + 1
            conn.execute(
                """
                UPDATE memories
                SET title = ?, type = ?, scope = ?, content = ?,
                    version = ?, updated_at = ?
                WHERE id = ?
                """,
                (title, mem_type, scope, content, new_version, now, row["id"]),
            )
            conn.commit()
            return {
                "action": "updated",
                "id": row["id"],
                "version": new_version,
                "title": title,
                "topic_key": topic_key,
            }

    cursor = conn.execute(
        """
        INSERT INTO memories (title, type, scope, topic_key, content, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, mem_type, scope, topic_key, content, now, now),
    )
    conn.commit()
    return {
        "action": "created",
        "id": cursor.lastrowid,
        "version": 1,
        "title": title,
        "topic_key": topic_key,
    }


def sanitize_fts_query(query: str) -> str:
    """
    Sanitize user input for FTS5 MATCH syntax.

    FTS5 treats characters like -, +, (, ) as operators.
    We wrap each token in double quotes to force literal matching,
    and join them with spaces (implicit AND).
    """
    # Remove characters that are problematic even inside quotes
    cleaned = re.sub(r'["\']', "", query)
    tokens = cleaned.split()
    if not tokens:
        return '""'
    return " ".join(f'"{token}"' for token in tokens)


def search_memories(
    conn: sqlite3.Connection,
    query: str,
    mem_type: str | None = None,
    limit: int = 10,
) -> list[dict]:
    """
    Full-text search across memories using FTS5.

    Returns a list of matching memories ordered by relevance (BM25 rank).
    Optionally filters by memory type.
    """
    sanitized = sanitize_fts_query(query)

    if mem_type:
        # Combine content search with type filter
        sql = """
            SELECT m.id, m.title, m.type, m.scope, m.topic_key,
                   m.content, m.version, m.created_at, m.updated_at,
                   rank
            FROM memories_fts fts
            JOIN memories m ON m.id = fts.rowid
            WHERE memories_fts MATCH ?
              AND m.type = ?
            ORDER BY rank
            LIMIT ?
        """
        rows = conn.execute(sql, (sanitized, mem_type, limit)).fetchall()
    else:
        sql = """
            SELECT m.id, m.title, m.type, m.scope, m.topic_key,
                   m.content, m.version, m.created_at, m.updated_at,
                   rank
            FROM memories_fts fts
            JOIN memories m ON m.id = fts.rowid
            WHERE memories_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """
        rows = conn.execute(sql, (sanitized, limit)).fetchall()

    return [dict(row) for row in rows]
