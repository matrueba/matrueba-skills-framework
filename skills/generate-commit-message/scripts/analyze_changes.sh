#!/usr/bin/env bash
# Analyze git changes since the last commit for commit message generation.
# Usage: bash analyze_changes.sh [repo-path]
#
# Outputs a structured summary of staged or unstaged changes.

set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo "ERROR: Not a git repository: $REPO" >&2
  exit 1
fi

echo "=== REPOSITORY ==="
basename "$(git rev-parse --show-toplevel)"

echo ""
echo "=== BRANCH ==="
git branch --show-current 2>/dev/null || echo "(detached HEAD)"

echo ""
echo "=== LAST COMMIT ==="
git log -1 --oneline 2>/dev/null || echo "(no commits)"

# Prefer staged changes; fall back to unstaged
STAGED=$(git diff --cached --name-status)
if [[ -n "$STAGED" ]]; then
  echo ""
  echo "=== CHANGE SOURCE: staged ==="

  echo ""
  echo "=== FILES CHANGED ==="
  git diff --cached --stat

  echo ""
  echo "=== DIFF ==="
  git diff --cached

else
  UNSTAGED=$(git diff --name-status)
  if [[ -n "$UNSTAGED" ]]; then
    echo ""
    echo "=== CHANGE SOURCE: unstaged ==="

    echo ""
    echo "=== FILES CHANGED ==="
    git diff --stat

    echo ""
    echo "=== DIFF ==="
    git diff

  else
    UNTRACKED=$(git ls-files --others --exclude-standard)
    if [[ -n "$UNTRACKED" ]]; then
      echo ""
      echo "=== CHANGE SOURCE: untracked files ==="

      echo ""
      echo "=== NEW FILES ==="
      echo "$UNTRACKED"

      echo ""
      echo "=== FILE CONTENTS ==="
      while IFS= read -r f; do
        echo "--- $f ---"
        head -c 4096 "$f" 2>/dev/null || echo "(binary or unreadable)"
        echo ""
      done <<< "$UNTRACKED"

    else
      echo ""
      echo "=== NO CHANGES DETECTED ==="
      echo "Working tree is clean. Nothing to commit."
    fi
  fi
fi
