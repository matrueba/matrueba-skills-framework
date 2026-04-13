# Resource Index - Manage Documentation Skill

Quick reference to the files that matter when using or maintaining this skill.

## Core Documentation

### SKILL.md

Primary workflow definition.

- End-to-end process.
- Mandatory versus conditional outputs.
- Review checklist.
- Expected success criteria.

Use it when you need the full operating model of the skill.

### README.md

Quick-start guide.

- Entry commands.
- Output description.
- Main scripts.
- Troubleshooting basics.

Use it when you need to run the skill or explain it quickly.

### references/documentation-format.md

Formatting and completion standard.

- Required sections by file.
- Table conventions.
- Placeholder policy.
- Quality checklist.

Use it when validating generated documentation before release.

## Reference Examples

All examples live in `reference/`.

### Baseline Examples


#### mqtt_topic_definition_example.md

- Topic naming.
- JSON message example.
- Topic comments.

### Comprehensive Examples

#### main_example_comprehensive.md

- Richer overview.
- Technology stack context.
- Responsibility breakdown.

#### configuration_example_comprehensive.md

- Extended system requirements.
- Fully described environment variables.
- Broader database mapping.

#### description_example_comprehensive.md

- Full Mermaid architecture diagram.
- Detailed component descriptions.
- Design and scaling notes.

#### functional_example_comprehensive.md

- Full feature inventory.
- Functional dependencies.
- Primary use-case flow.

#### testing_example_comprehensive.md

- Unit, integration, and regression test structure.
- Traceability to functionality identifiers.
- Example commands, coverage, and report locations.

Use the comprehensive examples as the target quality bar.

## Scripts

All automation scripts live in `scripts/`.

### analyze_project.py

- Detects language and runtime clues.
- Extracts dependencies.
- Finds env vars, databases, brokers, frameworks, and entry points.

Usage: `python scripts/analyze_project.py <project_path>`

### analyze_git_changes.py

- Reads commits since the last merge.
- Categorizes changed files.
- Flags dependency, config, code, test, and documentation changes.

Usage: `python scripts/analyze_git_changes.py [repo_path]`

### generate_docs.py

- Generates Markdown output in `docs/`.
- Adds conditional files when the analysis justifies them.

Usage: `python scripts/generate_docs.py [analysis.json] [git_analysis.json]`

### manage_docs.py

- Orchestrates the full run.
- Prints the final summary.
- Stores `documentation_generation_results.json` in the analyzed project.

Usage: `python scripts/manage_docs.py <project_root> [service_name] [gitlab_link]`

### generate-documentation.sh

- Thin wrapper around `manage_docs.py`.
- Adds argument validation and colored output.

Usage: `./generate-documentation.sh <project_path> [service_name] [gitlab_link]`

## Templates

Templates live in `templates/` and define the generated file structure.

- `main.md`
- `configuration.md`
- `description.md`
- `functional_description.md`
- `testing.md`
- `api.md`
- `mqtt_topic_definition.md`

Generated project documentation is written to the analyzed project's `docs/` directory, not into this skill folder.

## Suggested Reading Order

If you are new to the skill:

1. Read `README.md`.
2. Read `references/documentation-format.md`.
3. Review the files in `reference/`.
4. Run the workflow against a sample service.
5. Complete the human review checklist.

If you are maintaining the skill:

1. Read `SKILL.md`.
2. Review `scripts/`.
3. Compare output with the comprehensive examples.

## Generated Output Summary

```text
docs/
├── main.md
├── configuration.md
├── description.md
├── functional_description.md
├── testing.md
├── api.md                         # When the service exposes an API
└── mqtt_topic_definition.md       # When the service uses a broker such as MQTT
```

## Review Focus

Always verify these areas after generation:

- Links to repository and external docs.
- Environment variable descriptions.
- Architecture accuracy.
- Functionality identifiers.
- Test coverage description.

## Quick Links

- Start here: `README.md`
- Full workflow: `SKILL.md`
- Format guide: `references/documentation-format.md`
- Example set: `reference/`
