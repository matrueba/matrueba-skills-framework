#!/usr/bin/env python3
"""
Main orchestration script for the manage_documentation skill.
Coordinates analysis, generation, and documentation creation workflow.
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict

# Relative imports from the scripts in the same directory
import analyze_project
import analyze_git_changes
import generate_docs


class DocumentationWorkflow:
    """Orchestrates the complete documentation workflow"""

    def __init__(self, project_root: str, service_name: str = "", gitlab_link: str = ""):
        self.project_root = project_root
        self.service_name = service_name
        self.gitlab_link = gitlab_link
        self.project_analyzer = analyze_project.ProjectAnalyzer(project_root)
        self.git_analyzer = analyze_git_changes.GitAnalyzer(project_root)

    def run_workflow(self) -> Dict:
        """Execute the complete documentation workflow"""
        print("=" * 70)
        print("📚 DOCUMENTATION GENERATION WORKFLOW")
        print("=" * 70)

        # Step 1: Analyze project
        print("\n[1/4] Analyzing project structure and dependencies...")
        project_analysis = self.project_analyzer.analyze()
        print(f"    ✓ Language detected: {project_analysis['language']}")
        print(f"    ✓ Service: {project_analysis['service_name']}")
        print(f"    ✓ Dependencies found: {len(project_analysis['dependencies'])}")
        print(
            f"    ✓ Databases: {', '.join(project_analysis.get('databases', ['None']))}"
        )

        # Step 2: Analyze git changes
        print("\n[2/4] Analyzing changes since last merge...")
        git_analysis = self.git_analyzer.analyze()
        changes = git_analysis.get("changes", {})
        print(
            f"    ✓ Commits since merge: {changes.get('total_commits', 0)}"
        )
        change_cats = changes.get("change_categories", {})
        if change_cats:
            for category, files in change_cats.items():
                print(f"    ✓ {category.replace('_', ' ').title()}: {len(files)} file(s)")

        # Step 3: Generate documentation
        print("\n[3/4] Generating documentation files...")
        generator = generate_docs.DocumentationGenerator(project_analysis, git_analysis)

        service_name = self.service_name or project_analysis.get("service_name", "MyService")
        files = generator.generate_all_files(
            service_name=service_name,
            gitlab_link=self.gitlab_link,
        )

        # Step 4: Summary and warnings
        print("\n[4/4] Generating summary report...")
        print("\n" + "=" * 70)
        print("✓ DOCUMENTATION GENERATED SUCCESSFULLY")
        print("=" * 70)

        self._print_summary(project_analysis, git_analysis, files)

        return {
            "status": "success",
            "project_analysis": project_analysis,
            "git_analysis": git_analysis,
            "generated_files": files,
            "output_directory": str(generator.output_dir),
        }

    def _print_summary(self, project_analysis: Dict, git_analysis: Dict, files: list):
        """Print summary of generated documentation"""
        print("\n📋 DOCUMENTATION SUMMARY")
        print("-" * 70)

        print(f"\nService: {project_analysis.get('service_name')}")
        print(f"Language: {project_analysis.get('language')}")
        print(f"Output Directory: docs/")

        print(f"\nGenerated Files ({len(files)}):")
        for filename in files:
            print(f"  ✓ {filename}")

        print("\n📊 PROJECT ANALYSIS RESULTS:")
        print(f"  • Dependencies: {len(project_analysis.get('dependencies', {}))}")
        print(f"  • Environment Variables: {len(project_analysis.get('environment_variables', {}))}")
        print(f"  • Databases: {', '.join(project_analysis.get('databases', ['None'])) or 'None'}")
        print(f"  • Message Broker: {project_analysis.get('message_broker', 'None')}")
        print(f"  • Frameworks: {', '.join(project_analysis.get('frameworks', ['None'])) or 'None'}")
        print(f"  • API Type: {project_analysis.get('api_type', 'REST')}")

        changes = git_analysis.get("changes", {})
        print(f"\n📝 RECENT CODE CHANGES:")
        print(f"  • Total Commits: {changes.get('total_commits', 0)}")
        files_changed = changes.get("files_changed", {})
        total_files = (
            len(files_changed.get("added", []))
            + len(files_changed.get("modified", []))
            + len(files_changed.get("deleted", []))
        )
        print(f"  • Total Files Changed: {total_files}")
        print(f"    - Added: {len(files_changed.get('added', []))}")
        print(f"    - Modified: {len(files_changed.get('modified', []))}")
        print(f"    - Deleted: {len(files_changed.get('deleted', []))}")

        self._print_mandatory_review_notice()

    def _print_mandatory_review_notice(self):
        """Print mandatory review notice"""
        print("\n" + "=" * 70)
        print("⚠️  MANDATORY REVIEW REQUIRED")
        print("=" * 70)
        print("""
The documentation has been automatically generated based on code analysis
and existing code patterns. However, HUMAN REVIEW IS MANDATORY before
considering this documentation complete.

PLEASE REVIEW AND UPDATE:

1. ✏️  INTRODUCTION SECTION (main.md)
   - GitLab repository link
   - External documentation links
   - Applicable interfaces documentation

2. ✏️  SERVICE OVERVIEW (main.md)
   - Ensure accurate description of service purpose
   - Verify key responsibilities are listed

3. ✏️  SYSTEM REQUIREMENTS (configuration.md)
   - Confirm database and message broker types and versions
   - Verify language version is correct
   - Update MQTT Client Configuration if applicable

4. ✏️  ENVIRONMENT VARIABLES (configuration.md)
   - Add descriptions for all variables
   - Specify default values where applicable
   - Mark mandatory vs optional variables
   - Add any missing environment variables

5. ✏️  CODE DESCRIPTION (description.md)
   - Complete the architecture diagram (Mermaid or image)
   - Describe key components and their interactions
   - Add implementation details and design patterns

6. ✏️  SERVICE FUNCTIONALITIES (functional_description.md)
   - Add comprehensive list of all service features
   - Use consistent naming for feature identifiers
   - Provide clear descriptions for each capability

7. ✏️  TESTING (testing.md)
   - Define test cases for each functionality
   - Specify test execution commands
   - Update test coverage metrics

8. ✏️  OPTIONAL FILES (if applicable)
   - MQTT Topics: If using MQTT, complete topic definitions
   - API: If exposing REST API, document endpoints

LOCATION OF DOCUMENTATION: docs/ directory

After review and updates, this documentation will be ready for release.
""")
        print("=" * 70)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python manage_docs.py <project_root> [service_name] [gitlab_link]")
        print("\nExample:")
        print(
            "  python manage_docs.py /path/to/project 'My Service' 'https://gitlab.com/...'"
        )
        sys.exit(1)

    project_root = os.path.abspath(sys.argv[1])
    service_name = sys.argv[2] if len(sys.argv) > 2 else ""
    gitlab_link = sys.argv[3] if len(sys.argv) > 3 else ""

    if not os.path.isdir(project_root):
        print(f"Error: {project_root} is not a valid directory")
        sys.exit(1)

    # Change to project root for git commands
    original_cwd = os.getcwd()
    os.chdir(project_root)

    try:
        workflow = DocumentationWorkflow(
            project_root=project_root,
            service_name=service_name,
            gitlab_link=gitlab_link,
        )
        result = workflow.run_workflow()
    finally:
        os.chdir(original_cwd)

    # Save results to JSON
    results_file = Path(project_root) / "documentation_generation_results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"\n✓ Results saved to: {results_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
