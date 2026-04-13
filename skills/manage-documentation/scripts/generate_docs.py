#!/usr/bin/env python3
"""
Generate documentation files from project analysis results.
Creates markdown documentation files following the organizational templates.
"""

from pathlib import Path
from typing import Dict, Optional


class DocumentationGenerator:
    """Generates documentation files from project analysis"""

    def __init__(self, analysis_results: Dict, git_analysis: Optional[Dict] = None):
        self.analysis = analysis_results
        self.git_analysis = git_analysis or {}
        self.output_dir = Path("docs")

    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_main_md(self, service_name: str, gitlab_link: str = "", external_docs: str = "") -> str:
        """Generate main.md documentation"""
        template = f"""## Introduction (mandatory)

| MS name | {service_name} |
| :--- | :--- |
| **GitLab link** | {gitlab_link if gitlab_link else "**[Update with GitLab repository link]**"} |
| **External Documentation** | {external_docs if external_docs else "**[Update with external documentation link if available]**"} |
| **Applicable Interfaces** | **[Update with link to applicable interfaces documentation]** |

---

## Overview (mandatory)

{self._generate_overview()}

"""
        return template

    def _generate_overview(self) -> str:
        """Generate overview section based on analysis"""
        framework = self.analysis.get("frameworks", [])
        api_type = self.analysis.get("api_type", "REST")
        db = self.analysis.get("databases", [])
        broker = self.analysis.get("message_broker")

        overview = "This microservice provides "

        if framework:
            overview += f"a {framework[0]} based application"
        else:
            overview += "backend functionality"

        if db:
            overview += f" with {', '.join(db)} data persistence"

        if broker:
            overview += f" and {broker} message broker integration"

        if api_type:
            overview += f".\n\nThe service exposes a {api_type} interface for client interactions"

        overview += ".\n\n**Main Purpose:**\n**[Update with detailed description of service purpose and key responsibilities]**"

        return overview

    def generate_configuration_md(self) -> str:
        """Generate configuration.md documentation"""
        language = self.analysis.get("language", "Unknown")
        language_version = self.analysis.get("language_version", "Unknown")
        dependencies = self.analysis.get("dependencies", {})
        env_vars = self.analysis.get("environment_variables", {})
        databases = self.analysis.get("databases", [])
        broker = self.analysis.get("message_broker")

        template = f"""
## System Requirements (mandatory)

| Requirement | Version | Description |
| :--- | :--- | :--- |
| Language | {language_version if language_version else language} | Runtime environment |
| Database | {", ".join(databases) if databases else "[Update with database type/version]"} | Data persistence |
| Message Broker | {broker if broker else "[Update if applicable]"} | MQTT or similar |

---

## System Dependencies (mandatory)

| Library | Version |
| :--- | :--- |"""

        if dependencies:
            for lib, version in list(dependencies.items())[:10]:  # Limit to 10 deps
                template += f"\n| {lib} | {version} |"
            if len(dependencies) > 10:
                template += f"\n| ... and {len(dependencies) - 10} more | [See full list] |"
        else:
            template += "\n| **[Update with dependency list]** | **[version]** |"

        template += f"""

---

## MQTT Client Configuration 

| Client ID | MQTT Version | User name | Clean session |
| :--- | :--- | :--- | :--- |
| **[Update if applicable]** | **[version]** | **[username]** | **[true/false]** |

---

### Environment Variables (mandatory)

Every variable described in this section is necessary to correctly initialise the microservice, unless explicitly described as optional.

* Variables with default values shall take that configuration if not defined. Thus, code will not be blocked.
* Variables without default values shall block the code execution.

| Variable | Values | Default Value | Description |
| :--- | :--- | :--- | :--- |"""

        if env_vars:
            for var, info in list(env_vars.items())[:10]:
                template += f"\n| {var} | [values] | {info.get('default', '[none]')} | **[Description]** |"
            if len(env_vars) > 10:
                template += f"\n| ... and {len(env_vars) - 10} more | ... | ... | ... |"
        else:
            template += "\n| **[ENV_VAR_NAME]** | [possible values] | [default] | **[Description]** |"

        template += """

---

### Data Bases

| Data Base | Table | Variable |
| :--- | :--- | :--- |
| **[Database Name]** | **[Table Name]** | **[ENV_VAR]** |
"""
        return template

    def generate_description_md(self) -> str:
        """Generate description.md documentation"""
        language = self.analysis.get("language", "Unknown")
        main_files = self.analysis.get("main_files", [])
        structure = self.analysis.get("project_structure", {})

        template = f"""## Code Description (mandatory)

**Language:** {language}

**Main Entry Point(s):** {', '.join(main_files) if main_files else '[Update with main file(s)]'}

Description of the service's main functions and business logic.

**Key Components:**
- **[Component 1]**: [Description]
- **[Component 2]**: [Description]
- **[Component 3]**: [Description]

This section can be complemented with images, diagrams, links, etc...

---

## Architecture Diagram

**Current Architecture:**

```mermaid
graph TB
    Client[Client/External System]
    API[REST API Layer]
    Business[Business Logic]
    DB[(Database)]
    Cache[Cache/Storage]
    External[External Services]

    Client -->|HTTP Request| API
    API --> Business
    Business --> DB
    Business --> Cache
    Business --> External
```

**[Update the diagram above to match your service architecture. Use Mermaid for diagrams or include architecture image]**

### Architecture Components:

- **API Layer**: Handles incoming requests and responses
- **Business Logic**: Core service functionality
- **Data Persistence**: Database operations
- **Cache/Storage**: Data caching and temporary storage
- **External Integration**: Third-party service integration

---

### Additional Information

**Project Structure:**

{self._format_structure(structure)}

**Key Design Patterns:**
- **[Pattern 1]**: [Description]
- **[Pattern 2]**: [Description]

**Important Implementation Details:**
- **[Detail 1]**: [Description]
- **[Detail 2]**: [Description]
"""
        return template

    def _format_structure(self, structure: Dict) -> str:
        """Format project structure for documentation"""
        output = "```\n"
        if structure.get("directories"):
            output += "Project directories:\\n"
            for d in structure["directories"]:
                output += f"  - {d}/\\n"
        if structure.get("key_files"):
            output += "\\nKey files:\\n"
            for f in structure["key_files"]:
                output += f"  - {f}\\n"
        output += "```"
        return output

    def generate_functional_description_md(self, frameworks: list = None) -> str:
        """Generate functional_description.md documentation"""
        template = """## Service Functionalities (mandatory)

**Key Features:**

- **[FEATURE_ID_1]** - [Detailed description of functionality 1]
- **[FEATURE_ID_2]** - [Detailed description of functionality 2]
- **[FEATURE_ID_3]** - [Detailed description of functionality 3]

---

**Additional Capabilities:**

- **[CAPABILITY_ID_1]** - [Description]
- **[CAPABILITY_ID_2]** - [Description]

---

**Notes:**
- Each functionality should be uniquely identifiable with an ID (e.g., FEAT_001, FUNC_AUTHENTICATE)
- Functionality IDs are referenced in the testing.md file

"""
        return template

    def generate_testing_md(self) -> str:
        """Generate testing.md documentation"""
        template = """## Test Description (mandatory)

*The functionality identifiers reference the functional_description.md file*

### Unit Tests

- **[TEST_ID_001]** - **[FEATURE_ID_1]** - Description of the test, which functionalities and capabilities are tested.
- **[TEST_ID_002]** - **[FEATURE_ID_1]** - Integration test description.

### Integration Tests

- **[TEST_ID_003]** - **[FEATURE_ID_2]** - End-to-end test description.
- **[TEST_ID_004]** - **[FEATURE_ID_2, FEATURE_ID_3]** - Multiple functionality integration test.

### Regression Tests

- **[TEST_ID_005]** - **[FEATURE_ID_1, FEATURE_ID_2]** - Critical functionality regression testing.

### Test Coverage

**Target Coverage:** [XY]%
**Current Coverage:** **[Update after running tests]**

### Running Tests

**Test Command:**
```bash
[Update with actual test command, e.g., "npm test" or "pytest"]
```

**Test Report Location:**
- Unit tests report: `[path/to/coverage]`
- Integration tests report: `[path/to/integration-results]`

"""
        return template

    def generate_api_md(self) -> str:
        """Generate api.md documentation for API-based services"""
        api_type = self.analysis.get("api_type") or "API"

        template = f"""## {api_type} Interface Definition (conditional - for API services)

### Interface Overview

- **Interface Type**: {api_type}
- **Base URL**: **[Update with base path or endpoint]**
- **Authentication**: **[Update with authentication mechanism if applicable]**

---

### Endpoints / Operations

| Identifier | Method / Operation | Path / Topic | Description |
| :--- | :--- | :--- | :--- |
| **[API_001]** | **[GET/POST/Query/Mutation]** | **[/resource]** | **[Describe the operation]** |
| **[API_002]** | **[GET/POST/Query/Mutation]** | **[/resource/{{id}}]** | **[Describe the operation]** |

---

### Request and Response Notes

- **Request schema**: **[Link or describe request fields]**
- **Response schema**: **[Link or describe response fields]**
- **Error handling**: **[List relevant error codes or failure cases]**
- **Rate limiting / retries**: **[Document if applicable]**

---

### Examples

```bash
# Update with a real request example for the service
curl -X GET https://example.local/resource
```
"""
        return template

    def generate_mqtt_topics_md(self) -> str:
        """Generate mqtt_topic_definition.md documentation"""
        template = """## MQTT Topics Definition (conditional - for MQTT services)

### Subscribed Topics

#### Topic: device/status/+/update

**Message Example:**
```json
{
  "device_id": "device_001",
  "timestamp": "2024-01-15T10:30:00Z",
  "status": "online",
  "metrics": {
    "temperature": 25.5,
    "humidity": 60
  }
}
```

**Comments:** Subscribes to device status updates from all devices. The `+` wildcard matches any device_id.

---

### Published Topics

#### Topic: service/response/device_001/status

**Message Example:**
```json
{
  "request_id": "req_123",
  "status": "processed",
  "timestamp": "2024-01-15T10:30:01Z",
  "result": "acknowledged"
}
```

**Comments:** Publishes responses to device queries and status acknowledgments.

---

## Topic Reference Guide

| Topic Pattern | Type | Description | QoS |
| :--- | :--- | :--- | :--- |
| `device/status/+/update` | Subscribe | Device status updates | 1 |
| `service/response/+/status` | Publish | Service responses | 1 |

"""
        return template

    def generate_all_files(self, service_name: str = "", gitlab_link: str = "", external_docs: str = ""):
        """Generate all documentation files"""
        self.ensure_output_dir()

        # Extract service name if not provided
        if not service_name:
            service_name = self.analysis.get("service_name", "MyService")

        files_generated = []

        # Generate mandatory files
        files = {
            "main.md": self.generate_main_md(service_name, gitlab_link, external_docs),
            "configuration.md": self.generate_configuration_md(),
            "description.md": self.generate_description_md(),
            "functional_description.md": self.generate_functional_description_md(),
        }

        # Generate optional files
        if self.analysis.get("message_broker"):
            files["mqtt_topic_definition.md"] = self.generate_mqtt_topics_md()

        if self.analysis.get("api_type"):
            files["api.md"] = self.generate_api_md()

        files["testing.md"] = self.generate_testing_md()

        # Write all files
        for filename, content in files.items():
            filepath = self.output_dir / filename
            filepath.write_text(content, encoding="utf-8")
            files_generated.append(filename)
            print(f"✓ Generated: {filename}")

        return files_generated


def main():
    """Main function"""
    # Load analysis from stdin or file
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            analysis = json.load(f)
    else:
        analysis = json.load(sys.stdin)

    # Optional git analysis
    git_analysis = None
    if len(sys.argv) > 2:
        with open(sys.argv[2], "r") as f:
            git_analysis = json.load(f)

    generator = DocumentationGenerator(analysis, git_analysis)
    files = generator.generate_all_files()

    print(f"\n✓ Documentation generated successfully!")
    print(f"Generated files: {', '.join(files)}")
    print(f"Location: {generator.output_dir}")


if __name__ == "__main__":
    main()
