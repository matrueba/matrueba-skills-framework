#!/usr/bin/env python3
"""
mem_search.py — Search past memories using FTS5 full-text search.

Usage:
    python mem_search.py \
        --db <path-to-memory.db> \
        --query "search terms" \
        [--type decision] \
        [--limit 10]
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent so we can import mem_db
sys.path.insert(0, str(Path(__file__).resolve().parent))
from mem_db import get_connection, search_memories

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
        description="Search past memories using full-text search."
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Path to the SQLite memory database.",
    )
    parser.add_argument(
        "--query",
        required=True,
        help="Search terms (FTS5 full-text search). Supports prefix matching with *.",
    )
    parser.add_argument(
        "--type",
        default=None,
        choices=sorted(VALID_TYPES),
        help="Optional: filter results by memory type.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of results to return (default: 10).",
    )

    args = parser.parse_args()

    conn = get_connection(args.db)
    try:
        results = search_memories(
            conn=conn,
            query=args.query,
            mem_type=args.type,
            limit=args.limit,
        )

        if not results:
            print(json.dumps({"matches": 0, "results": []}, indent=2))
            return

        # Remove the FTS rank column from output (internal detail)
        for r in results:
            r.pop("rank", None)

        output = {
            "matches": len(results),
            "results": results,
        }
        print(json.dumps(output, indent=2))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
