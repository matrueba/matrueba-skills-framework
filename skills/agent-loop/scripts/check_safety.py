#!/usr/bin/env python3
import argparse
import re

CRITICAL_PATTERNS = [
    r"rm\s+(-[rf]+\s+)?[\w/.*-]+",  # Deletion
    r"delete_block",                # MCP deletion
    r"overwrite:\s*true",           # Large overwrites (in prompts or JSON)
    r"git\s+reset",                 # Destructive Git
    r"git\s+clean",                 # Destructive Git
    r"mv\s+.+\s+/.+",               # Moving to root or critical paths
    r"curl\s+",                     # Network calls (exfiltration risk)
    r"wget\s+",                     # Network calls
    r"chmod\s+",                    # Permission changes
]

def check_safety(command):
    for pattern in CRITICAL_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True, pattern
    return False, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a command is critical/dangerous.")
    parser.add_argument("--command", required=True, help="The command or action string to check")
    
    args = parser.parse_args()
    is_critical, logic = check_safety(args.command)
    
    if is_critical:
        print(f"[CRITICAL] detected pattern: {logic}")
        exit(1)
    else:
        print("[SAFE] No critical patterns detected.")
        exit(0)
