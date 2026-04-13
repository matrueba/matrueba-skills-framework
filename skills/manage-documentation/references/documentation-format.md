# Documentation Format Guide

## Overview

This guide explains the documentation format standards used across services and components. The documentation is organized into several mandatory and optional files that together provide comprehensive coverage of the service.

## File Structure

```
docs/
├── main.md (MANDATORY)
├── configuration.md (MANDATORY)
├── description.md (MANDATORY)
├── functional_description.md (MANDATORY)
├── testing.md (OPTIONAL - recommended for all services)
├── api.md (OPTIONAL - only for REST/GraphQL/gRPC APIs)
└── mqtt_topic_definition.md (OPTIONAL - only for MQTT services)
```

## Mandatory Files

### 1. main.md - Main Service Documentation

**Purpose:** Provides basic service identification and overview.

**Mandatory Sections:**
- **Introduction** - Service metadata table with:
  - MS name: Service/microservice identifier
  - GitLab link: Repository URL
  - External Documentation: Link to external docs (OpenAPI, tutorials, etc.)
  - Applicable Interfaces: Link to MQTT topic definitions or API specs
- **Overview** - Narrative description of the service

**Example:**
```markdown
## Introduction (mandatory)

| MS name | chirpstack-network-manager |
| :--- | :--- |
| **GitLab link** | *https://gitlab.com/deeptrack1/sw/tb3-1-lora_server_stack* |
| **External Documentation** | *https://www.chirpstack.io/docs/* |
| **Applicable Interfaces** | *https://swpvhardware.atlassian.net/wiki/spaces/SD/pages/55541792/MQTT+-+Topic+Reference* |

## Overview

The ChirpStack Network Manager is a network server implementation that manages LoRaWAN devices...
```

### 2. configuration.md - System Requirements & Configuration

**Purpose:** Documents runtime requirements, dependencies, and configuration options.

**Mandatory Sections:**
- **System Requirements** - Table with Language, Database, Message Broker and versions
- **System Dependencies** - Library/package list with versions
- **Environment Variables** - Complete list with descriptions and defaults

**Optional Sections:**
- MQTT Client Configuration - If using MQTT
- Databases - If using persistent storage

**Key Rules:**
- Variables with default values shall take that configuration if not defined
- Variables without default values shall block execution
- Each variable must have a description

**Example Table:**
```markdown
| Variable | Values | Default Value | Description |
| :--- | :--- | :--- | :--- |
| LOG_LEVEL | debug, info, warn, error | info | Application logging level |
| DB_HOST | localhost, hostname, IP | localhost | Database hostname |
| DB_PORT | any valid port | 5432 | Database connection port |
```

### 3. description.md - Code Description & Architecture

**Purpose:** Explains service structure, main components, and architecture.

**Mandatory Sections:**
- **Code Description** - Description of main functions and business logic
- **Architecture Diagram** - Visual representation using Mermaid or image

**Optional Sections:**
- Architecture Components - Detailed component descriptions
- Additional Information - Design patterns, key implementations
- Data Flow - How data moves through the system

**Architecture Diagram Format (Mermaid):**
```mermaid
graph TB
    Client[Client/External System]
    API[REST API Layer]
    Business[Business Logic]
    DB[(Database)]
    Cache[Cache/Storage]
    
    Client -->|HTTP Request| API
    API --> Business
    Business --> DB
    Business --> Cache
```

### 4. functional_description.md - Service Functionalities

**Purpose:** Lists all key features and capabilities of the service.

**Mandatory Sections:**
- **Service Functionalities** - List of all major features with identifiers

**Format Rules:**
- Use consistent identifier format (e.g., FEAT_001, FUNC_AUTHENTICATE)
- One-line descriptions for each functionality
- Identifiers are referenced in testing.md and mqtt_topic_definition.md

**Example:**
```markdown
## Service Functionalities

- **[AUTH_001]** - JWT token generation and validation
- **[AUTH_002]** - User authentication with email/password
- **[AUTH_003]** - OAuth2 integration with external providers
- **[SECURE_001]** - End-to-end encryption for sensitive data
```

## Optional (But Recommended) Files

### 5. testing.md - Test Description

**Purpose:** Documents test cases and test coverage.

**Sections:**
- Unit Tests - Basic functionality tests
- Integration Tests - Component interaction tests
- Regression Tests - Critical path tests
- Test Coverage - Target and current metrics
- Running Tests - Commands to execute tests

**Format:**
```markdown
- **[TEST_ID_001]** - **[FEATURE_ID]** - Description of test
```

### 6. api.md - API Endpoints (REST/GraphQL/gRPC)

**Purpose:** Documents service API endpoints.

**Content:**
- Endpoint definitions (path, method, parameters)
- Request/response schemas
- Authentication requirements
- Error codes and messages
- Rate limiting information
- Example curl/fetch commands

### 7. mqtt_topic_definition.md - MQTT Topics (MQTT Services Only)

**Purpose:** Documents MQTT topics used by the service.

**Sections per Topic:**
- Topic name/pattern
- Message example (JSON)
- QoS level
- Direction (Publish/Subscribe)
- Comments and notes

**Format:**
```markdown
#### Topic: device/status/+/update

**Message Example:**
```json
{
  "device_id": "device_001",
  "timestamp": "2024-01-15T10:30:00Z",
  "status": "online"
}
```

**Comments:** Subscribes to device status updates from all devices.
```

## Writing Guidelines

### Document Consistency

1. **Title Format:** Use level 2 headings (##) for main sections, level 3 (###) for subsections
2. **Tables:** Use markdown tables for structured information
3. **Code:** Use JSON code blocks for examples, bash for commands
4. **Links:** Absolute links to external resources, relative for internal references
5. **Language:** Clear, technical but accessible writing

### Placeholders vs. Actual Content

- **DO NOT** submit documentation with placeholder text like `[Update with...]`
- **DO** fill in all mandatory sections with actual, specific information
- **DO** include actual extracted data (real dependencies, environment variables)
- **DO** only use placeholder text during initial generation - must be replaced during review

### Environment Variable Documentation

Each variable should include:
- **Name:** Exact environment variable name
- **Values:** Possible values or value format
- **Default:** Default value if variable is optional
- **Description:** Clear explanation of purpose and usage

Example:
```markdown
| DATABASE_URL | postgresql://user:pass@host:port/db | [required] | PostgreSQL connection string |
| LOG_LEVEL | debug,info,warn,error | info | Logging verbosity level |
| CACHE_TTL | number (seconds) | 3600 | Cache entry time-to-live |
```

## Mandatory vs. Optional Sections by Service Type

### All Services
- main.md (complete)
- configuration.md (System Requirements, Dependencies, Env Vars)
- description.md (Code Description, Architecture)
- functional_description.md

### Services with Databases
- configuration.md (Databases section)

### Services with MQTT
- configuration.md (MQTT Client Configuration section)
- mqtt_topic_definition.md

### API Services (REST/GraphQL/gRPC)
- api.md (recommended)

### All Services
- testing.md (recommended)

## Quality Checklist

Before considering documentation complete:

- [ ] All mandatory sections filled with actual data
- [ ] No placeholder text remaining
- [ ] Links are valid and current
- [ ] Code examples are correct and tested
- [ ] Architecture diagram accurately represents current structure
- [ ] Environment variables match actual code configuration
- [ ] Dependencies list is complete and current
- [ ] Functionality identifiers are unique and consistent
- [ ] Test cases cover major functionalities
- [ ] All tables are properly formatted
- [ ] Cross-references between files are consistent

## Common Mistakes to Avoid

1. ❌ Leaving placeholder text like `[Update with...]`
2. ❌ Incomplete environment variable descriptions
3. ❌ Missing version information for dependencies
4. ❌ Outdated architecture diagram not matching current code
5. ❌ Inconsistent feature identifier naming
6. ❌ Missing links to GitLab or external documentation
7. ❌ Irrelevant MQTT topics documentation for non-MQTT services
8. ❌ Missing test descriptions
9. ❌ Unclear or generic service overview
10. ❌ Incomplete or incorrect database configuration

## Version Control

Documentation should be:
- Stored in `docs/` directory of the service repository
- Updated whenever significant code changes occur
- Reviewed and approved by team before release
- Kept in sync with actual service implementation
