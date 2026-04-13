# Manage Documentation Skill

Create or update service documentation from code and git history, then leave the result ready for human review.

## Quick Start

Use the Python entrypoint directly:

```bash
python scripts/manage_docs.py /path/to/project
```

Or use the wrapper script:

```bash
./generate-documentation.sh /path/to/project "My Service" "https://gitlab.com/org/project"
```

## What the Skill Does

1. Analyzes the target codebase to infer language, dependencies, frameworks, databases, environment variables, and main files.
2. Analyzes git history since the last merge to understand what changed and which documentation areas are likely affected.
3. Generates standardized Markdown files inside the target project's `docs/` directory.
4. Produces a `documentation_generation_results.json` file in the analyzed project root.
5. Displays a mandatory review checklist so generated content is completed before release.

## Generated Output

Mandatory output:

- `main.md`
- `configuration.md`
- `description.md`
- `functional_description.md`
- `testing.md`

Conditional output:

- `mqtt_topic_definition.md` when a message broker such as MQTT is detected
- `api.md` when the project looks like an API service

## Directory Structure

```text
manage_documentation/
├── SKILL.md
├── README.md
├── INDEX.md
├── generate-documentation.sh
├── scripts/
│   ├── analyze_project.py
│   ├── analyze_git_changes.py
│   ├── generate_docs.py
│   └── manage_docs.py
├── templates/
│   ├── api.md
│   ├── configuration.md
│   ├── description.md
│   ├── functional_description.md
│   ├── main.md
│   ├── mqtt_topic_definition.md
│   └── testing.md
├── reference/
│   ├── configuration_example_comprehensive.md
│   ├── description_example_comprehensive.md
│   ├── functional_example_comprehensive.md
│   ├── main_example_comprehensive.md
│   └── mqtt_topic_definition_example.md
│   └── testing_example_comprehensive.md
└── references/
    └── documentation-format.md
```

## Mandatory Review

After generation, you still need to complete and validate the documentation:

1. Repository and external links.
2. Service overview and responsibilities.
3. Environment variable descriptions and defaults.
4. Architecture diagram.
5. Functional capability list.
6. Test cases and execution commands.

The generator provides structure and a first pass. It does not replace service-owner review.

## Templates and References

Use `templates/` as the structural source for generated files.

Use `reference/` to see completed examples.

Basic examples:

- `main_description_example.md`
- `mqtt_topic_definition_example.md`

Comprehensive examples:

- `main_example_comprehensive.md`
- `configuration_example_comprehensive.md`
- `description_example_comprehensive.md`
- `functional_example_comprehensive.md`
- `test_description_example_comprehensive.md`

For formatting rules and completion criteria, see `references/documentation-format.md`.

## Main Scripts

### `analyze_project.py`

- Detects language and runtime clues.
- Extracts dependencies and environment variables.
- Detects databases, brokers, frameworks, API style, and project structure.

### `analyze_git_changes.py`

- Reads commits since the last merge.
- Categorizes changed files.
- Highlights source, config, dependency, test, and documentation changes.

### `generate_docs.py`

- Generates the documentation files.
- Adds conditional files only when they apply.
- Writes output to the target project's `docs/` directory.

### `manage_docs.py`

- Orchestrates the whole workflow.
- Prints the analysis summary.
- Stores the JSON result in the analyzed project.

## Use From Copilot or Claude

Example prompts:

```text
Create documentation for my service-processor microservice.
Update documentation for the data-transformer service after the latest merge.
```

Helpful extra context:

- Service name.
- GitLab repository URL.
- External documentation links.
- Any team-specific documentation requirements.

## Success Criteria

Documentation is ready only when:

- No placeholder text remains in mandatory sections.
- Links are current.
- Architecture matches the current code.
- Environment variables match the actual runtime behavior.
- Functional identifiers are consistent.
- Tests are documented with realistic commands and scope.

## Troubleshooting

No environment variables detected:

- Check whether `.env`, `.env.example`, or `.env.default` exists in the project root.
- Verify the project actually centralizes runtime variables there.

Missing dependencies:

- Check `package.json`, `requirements.txt`, `pyproject.toml`, or equivalent manifests.
- Review whether dependencies are declared in a nested service directory.

Weak git analysis:

- Confirm the target project is a git repository.
- Confirm merge history exists or provide a baseline manually if needed.

## See Also

- `SKILL.md` for the full workflow.
- `INDEX.md` for navigation.
- `references/documentation-format.md` for format rules.
