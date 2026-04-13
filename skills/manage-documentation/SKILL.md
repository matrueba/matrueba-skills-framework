---
name: manage_documentation
description: "Create or update service documentation by analyzing code changes since the last merge. Use this skill when you need to generate comprehensive documentation following organizational standards. The skill analyzes the codebase to understand the service architecture, reviews git history for recent changes, and generates documentation in the mandatory template format. Use this whenever the user mentions updating docs, creating service documentation, documenting code changes, or preparing documentation for a project release."
compatibility: "Requires: git (for analyzing code changes), access to source code files"
---

# Manage Documentation Skill

## Overview

This skill automates the process of creating or updating service documentation by:

1. **Analyzing the codebase** to understand service structure, dependencies, and architecture
2. **Reviewing git history** since the last merge to identify code changes
3. **Extracting configuration and requirements** from source code (package.json, environment files, Dockerfile, etc.)
4. **Generating documentation** following the standardized template format
5. **Organizing output** in the `docs/` directory with proper structure
6. **Highlighting mandatory sections** that must be reviewed by the user

## When to Use This Skill

- After significant code changes or a merge, to keep documentation up-to-date
- When creating documentation for a new microservice or component
- To standardize service documentation across your organization
- When preparing to release a new version with comprehensive documentation
- To document architecture, configuration, dependencies, and functionalities
- When analyzing changes and needing to ensure documentation reflects the current state

## Workflow

### Step 1: Gather Initial Context

1. **Identify the service**: Get the service/microservice name and GitLab repository link from the user
2. **Determine scope**: Ask if this is a new service documentation or an update to existing documentation
3. **Review existing docs**: Check if documentation already exists in `docs/` directory
4. **Get baseline**: Identify the last merge/commit to use as the baseline for analyzing changes

### Step 2: Analyze the Codebase

Perform a comprehensive analysis of the source code:

- **Language and Runtime**: Detect programming language and version (Node.js, Python, etc.)
- **Dependencies**: Extract from `package.json`, `requirements.txt`, or equivalent
- **Environment Configuration**: Parse environment variable files, configuration files
- **Database Setup**: Identify database connections, migrations, schemas
- **Message Broker**: Detect MQTT configurations
- **Architecture**: Analyze main code structure, entry points, key modules
- **API Endpoints**: Extract from code or OpenAPI/Swagger files if present
- **Tests**: Identify existing test structure and test types
- **External Dependencies**: Document libraries, frameworks, and external services

### Step 3: Review Code Changes

Analyze git history since the last merge:

- **Breaking Changes**: Identify any changes that might affect documentation
- **New Features**: Find newly added functionalities
- **Configuration Changes**: Spot changes in environment variables or configuration
- **Dependency Updates**: Note added or upgraded libraries
- **Architecture Changes**: Identify structural modifications

### Step 4: Check for Examples

Review the `reference/` directory to understand:
- Expected format and structure
- Mandatory vs. optional sections
- Examples of complete documentation
- How different services are documented

See the **reference/** directory for complete documentation examples:
- `mqtt_topic_definition_example.md` - Example of MQTT topics documentation
- `main_example_comprehensive.md` - Extended main documentation example
- `configuration_example_comprehensive.md` - Full configuration example
- `description_example_comprehensive.md` - Detailed architecture and code description example
- `functional_example_comprehensive.md` - Full functionality inventory example
- `test_description_example_comprehensive.md` - Full testing example with traceability to documented functionalities

Use `references/documentation-format.md` as the quality bar for the generated output and review checklist.

### Step 5: Generate Documentation Files

Create documentation following the **templates/** directory structure. Generate appropriate files based on the service type:

#### Mandatory Files (Always Required)

1. **main.md** - Main documentation with Introduction and Overview sections
   - Introduction table with service name, GitLab link, external documentation
   - Overview describing the microservice

2. **configuration.md** - System Requirements, Dependencies, and Environment Variables
   - System requirements table (Language, Database, Message Broker)
   - System dependencies table (Libraries and versions)
   - Environment variables with descriptions and default values
   - Database configurations

3. **description.md** - Code description and service architecture
   - Code description of main functions
   - Architecture diagram (using mermaid or image)
   - Additional information about the service

4. **functional_description.md** - Service functionalities list
   - Functional identifiers for each capability
   - Brief descriptions of what the service does

#### Optional Files (Based on Service Type)

5. **testing.md** - Test descriptions and functionality testing
   - Test identifiers and descriptions
   - References to functional_description.md identifiers
   - Coverage of main functionalities

6. **api.md** - API endpoints (if applicable)
   - Endpoint definitions
   - Request/response formats
   - Authentication requirements

7. **mqtt_topic_definition.md** - MQTT topics (if applicable)
   - Topic definitions
   - Message examples
   - Comments and notes

### Step 6: Generate Documentation

Create the `docs/` directory structure:

```
docs/
├── main.md (mandatory)
├── configuration.md (mandatory)
├── description.md (mandatory)
├── functional_description.md (mandatory)
├── testing.md (optional, if applicable)
├── api.md (optional, if applicable)
└── mqtt_topic_definition.md (optional, if applicable)
```

### Step 7: Present Results and Request Review

Display:
1. **Summary of generated documentation** - List of files created/updated
2. **Key sections identified** - What was discovered in the code analysis
3. **Mandatory review notice** - Clear warning that user MUST review the documentation

## Documentation Template Files

The templates are located in `templates/` directory:

- `templates/main.md` - Template for main.md
- `templates/configuration.md` - Template for configuration.md
- `templates/description.md` - Template for description.md
- `templates/functional_description.md` - Template for functional_description.md
- `templates/testing.md` - Template for testing.md
- `templates/api.md` - Template for api.md (for API services)
- `templates/mqtt_topic_definition.md` - Template for MQTT topics

Use `reference/` for completed examples and `references/documentation-format.md` for completion rules.

## Mandatory Sections Reference

The following sections are **MANDATORY** in their respective files and must be completed:

### main.md
- **Introduction** - Service metadata (name, link, external documentation)
- **Overview** - Service description

### configuration.md
- **System Requirements** - Language, Database, Message Broker versions
- **System Dependencies** - Libraries and versions
- **Environment Variables** - All critical environment variables with descriptions

### description.md
- **Code Description** - Main functions and service logic
- **Architecture Diagram** - Visual representation of service structure

### functional_description.md
- **Service Functionalities** - List of all key functionalities

## Documentation Format Standards

All documentation must follow these standards:

- **Title Format**: Use level 2 headings (##) for main sections
- **Tables**: Use markdown tables for structured information (Requirements, Dependencies, Environment Variables)
- **Code Examples**: Use JSON code blocks for message/configuration examples
- **Links**: Include GitLab repository links and external documentation links
- **Comments**: Add descriptive comments only where necessary
- **Consistency**: Maintain consistent naming and terminology throughout

## Important Notes

1. **Mandatory Review**: After generation, the user MUST review all generated documentation. This is not optional.
2. **Accuracy**: The generated documentation should accurately reflect the current state of the codebase after the most recent merge/commit.
3. **Completeness**: Mandatory sections must be completed with actual values extracted from the code, not placeholder text.
4. **Maintenance**: Documentation should be updated whenever significant code changes occur.
5. **Templates as Guides**: Use templates as structure guides, but fill them with actual service-specific information analyzed from the codebase.

## Common Patterns

### Pattern 1: New Microservice Documentation
```
User: "Create documentation for the new order-service microservice"
→ Analyze codebase structure
→ Extract dependencies and requirements
→ Generate all mandatory files
→ Create optional files based on service type (API, MQTT, etc.)
→ Present results with mandatory review notice
→ Output: Complete docs/ directory
```

### Pattern 2: Update Documentation After Merge
```
User: "Update documentation for authentication-service after the latest merge"
→ Review changes since last merge
→ Identify new features, configs, or dependencies
→ Update affected files (likely configuration.md and possibly description.md)
→ Generate updated docs/ directory
→ Present results with mandatory review notice
→ Output: Updated docs/ with change summary
```

### Pattern 3: Complete Service Re-documentation
```
User: "I need comprehensive documentation for the current state of data-processor service"
→ Deep codebase analysis
→ Repository structure analysis
→ Full dependency extraction
→ Generate all applicable documentation files
→ Present complete documentation package
→ Present results with mandatory review notice
→ Output: Complete and comprehensive docs/ directory
```

## Integration with Git

The skill uses git to:
- Identify last merge using `git log --merges`
- Extract recent changes: `git diff <last-merge>..HEAD`
- Analyse commit history for significant changes
- Track file modifications to update relevant documentation

## Success Criteria

Your documentation is ready when:
- ✅ All mandatory sections are completed with actual service data
- ✅ main.md contains service identification and overview
- ✅ configuration.md has all system requirements and environment variables
- ✅ description.md includes code description and architecture diagram
- ✅ functional_description.md lists all service functionalities
- ✅ All generated files follow the template format
- ✅ docs/ directory is properly organized
- ✅ **User has reviewed and approved the documentation** (MANDATORY)

## Tips for Best Results

1. **Analyze First**: Spend time analyzing the codebase thoroughly before generating documentation
2. **Extract Configuration**: Fully extract environment variables, dependencies, and requirements from source files
3. **Use Examples**: Reference the examples in the `reference/` directory to understand proper formatting
4. **Check Architecture**: Create clear architecture diagrams that show how components interact
5. **List Functionalities**: Ensure all major functionalities are documented with meaningful identifiers
6. **Verify Completeness**: Double-check that no mandatory sections have placeholder text
7. **Request Review**: Always request that the user review the generated documentation - this is crucial

---

## File Structure Overview

```
manage_documentation/
├── SKILL.md (this file - skill definition)
├── README.md (quick start guide)
├── INDEX.md (resource index)
├── generate-documentation.sh (shell wrapper)
├── scripts/ (analysis and generation scripts)
│   ├── analyze_project.py
│   ├── analyze_git_changes.py
│   ├── generate_docs.py
│   └── manage_docs.py
├── templates/ (documentation templates)
│   ├── main.md
│   ├── configuration.md
│   ├── description.md
│   ├── functional_description.md
│   ├── testing.md
│   ├── api.md
│   └── mqtt_topic_definition.md
└── reference/ (example documentation)
   ├── mqtt_topic_definition_example.md
   ├── main_example_comprehensive.md
   ├── configuration_example_comprehensive.md
   ├── description_example_comprehensive.md
   ├── functional_example_comprehensive.md
   └── test_description_example_comprehensive.md
```
