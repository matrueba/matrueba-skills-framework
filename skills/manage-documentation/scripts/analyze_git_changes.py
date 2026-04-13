#!/usr/bin/env python3
"""
Analyze git changes since last merge to identify code modifications.
Helps understand what has changed and what parts of documentation need updating.
"""

import subprocess
import json
import sys
from typing import Dict, List, Any
from datetime import datetime


class GitAnalyzer:
    """Analyzes git repository to identify recent changes"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path

    def run_git_command(self, command: List[str]) -> str:
        """Run a git command and return output"""
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=False,
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"

    def get_last_merge_commit(self) -> str:
        """Get the hash of the last merge commit"""
        output = self.run_git_command(
            ["git", "log", "--oneline", "--merges", "-1"]
        )
        if output:
            return output.split()[0]
        return "HEAD~1"

    def get_commits_since_merge(self, since_commit: str = None) -> List[Dict[str, str]]:
        """Get all commits since last merge"""
        if since_commit is None:
            since_commit = self.get_last_merge_commit()

        output = self.run_git_command(
            [
                "git",
                "log",
                f"{since_commit}..HEAD",
                "--pretty=format:%H|%an|%ae|%ad|%s",
                "--date=short",
            ]
        )

        commits = []
        if output:
            for line in output.split("\n"):
                if line.strip():
                    parts = line.split("|")
                    if len(parts) >= 5:
                        commits.append(
                            {
                                "hash": parts[0],
                                "author": parts[1],
                                "email": parts[2],
                                "date": parts[3],
                                "message": parts[4],
                            }
                        )

        return commits

    def get_changed_files(self, since_commit: str = None) -> Dict[str, List[str]]:
        """Get changed files categorized by type"""
        if since_commit is None:
            since_commit = self.get_last_merge_commit()

        output = self.run_git_command(
            ["git", "diff", "--name-status", f"{since_commit}..HEAD"]
        )

        changes = {"added": [], "modified": [], "deleted": []}

        if output:
            for line in output.split("\n"):
                if line.strip():
                    parts = line.split("\t")
                    if len(parts) >= 2:
                        status = parts[0]
                        filepath = parts[-1]
                        if status == "A":
                            changes["added"].append(filepath)
                        elif status == "M":
                            changes["modified"].append(filepath)
                        elif status == "D":
                            changes["deleted"].append(filepath)
                        elif status.startswith(("R", "C")):
                            changes["modified"].append(filepath)

        return changes

    def get_file_diff_stats(self, since_commit: str = None) -> Dict[str, Dict[str, int]]:
        """Get detailed diff statistics for each file"""
        if since_commit is None:
            since_commit = self.get_last_merge_commit()

        output = self.run_git_command(
            [
                "git",
                "diff",
                "--numstat",
                f"{since_commit}..HEAD",
            ]
        )

        stats = {}
        if output:
            for line in output.split("\n"):
                if line.strip():
                    parts = line.split("\t")
                    if len(parts) >= 3:
                        try:
                            additions = int(parts[0]) if parts[0] != "-" else 0
                            deletions = int(parts[1]) if parts[1] != "-" else 0
                            filepath = parts[2]
                            stats[filepath] = {
                                "additions": additions,
                                "deletions": deletions,
                                "total_changes": additions + deletions,
                            }
                        except:
                            pass

        return stats

    def identify_change_categories(self, since_commit: str = None) -> Dict[str, Any]:
        """Identify what types of changes have been made"""
        files_changed = self.get_changed_files(since_commit)
        diff_stats = self.get_file_diff_stats(since_commit)
        commits = self.get_commits_since_merge(since_commit)

        categories = {
            "source_code": [],
            "configuration": [],
            "dependencies": [],
            "tests": [],
            "documentation": [],
            "other": [],
        }

        all_files = (
            files_changed["added"]
            + files_changed["modified"]
            + files_changed["deleted"]
        )

        for filepath in all_files:
            if filepath in [
                "package.json",
                "package-lock.json",
                "requirements.txt",
                "pyproject.toml",
                "poetry.lock",
                "Pipfile",
                "Pipfile.lock",
                "pom.xml",
                "Gemfile",
            ]:
                categories["dependencies"].append(filepath)
            elif filepath.endswith((".py", ".js", ".ts", ".java", ".go", ".rs")):
                categories["source_code"].append(filepath)
            elif filepath.endswith((".env", ".yaml", ".yml", ".json", ".conf")):
                categories["configuration"].append(filepath)
            elif "test" in filepath.lower():
                categories["tests"].append(filepath)
            elif filepath.endswith((".md", ".txt")):
                categories["documentation"].append(filepath)
            else:
                categories["other"].append(filepath)

        return {
            "commits": commits,
            "total_commits": len(commits),
            "files_changed": files_changed,
            "file_statistics": diff_stats,
            "change_categories": {
                k: v for k, v in categories.items() if v
            },  # Only include non-empty categories
            "significant_changes": any(
                categories["source_code"]
                or categories["configuration"]
                or categories["dependencies"]
            ),
        }

    def analyze(self) -> Dict[str, Any]:
        """Run complete git analysis"""
        return {
            "last_merge": self.get_last_merge_commit(),
            "changes": self.identify_change_categories(),
            "timestamp": datetime.now().isoformat(),
        }


def main():
    """Main function"""
    repo_path = "." if len(sys.argv) < 2 else sys.argv[1]

    analyzer = GitAnalyzer(repo_path)
    results = analyzer.analyze()

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
