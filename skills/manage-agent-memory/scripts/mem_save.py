#!/usr/bin/env python3
"""
mem_save.py — Save an observation to persistent memory.

Usage:
    python mem_save.py \
        --db <path-to-memory.db> \
        --title "Short searchable title" \
        --type decision \
        --content "Structured content..." \
        [--scope project] \
        [--topic-key "architecture/auth-model"]
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent so we can import mem_db
sys.path.insert(0, str(Path(__file__).resolve().parent))
from mem_db import get_connection, save_memory

VALID_TYPES = {
    "bugfix",
    "decision",
    "architecture",
    "discovery",
    "pattern",
    "config",
    "preference",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Save an observation to persistent memory."
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Path to the SQLite memory database.",
    )
    parser.add_argument(
        "--title",
        required=True,
        help='Short, searchable title (verb + what). e.g. "Fixed N+1 query in UserList"',
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=sorted(VALID_TYPES),
        help="Memory type.",
    )
    parser.add_argument(
        "--content",
        required=True,
        help="Structured content with What/Why/Where/Learned fields.",
    )
    parser.add_argument(
        "--scope",
        default="project",
        choices=["project", "personal"],
        help="Scope of the memory (default: project).",
    )
    parser.add_argument(
        "--topic-key",
        default=None,
        help="Stable key for evolving topics, e.g. architecture/auth-model. "
        "Reusing a topic_key updates the existing memory instead of creating a new one.",
    )

    args = parser.parse_args()

    conn = get_connection(args.db)
    try:
        result = save_memory(
            conn=conn,
            title=args.title,
            mem_type=args.type,
            content=args.content,
            scope=args.scope,
            topic_key=args.topic_key,
        )
        print(json.dumps(result, indent=2))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
