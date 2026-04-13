# Context & Rules for AI Assistants

**SYSTEM INSTRUCTION:** This file represents the absolute source of truth for this project. YOU MUST read this file before generating any code or answering questions. If a user request conflicts with these rules, prioritize these rules.

## 1. Project DNA

- **Project Name:** [Insert Name]
- **Description:** [Brief 1-2 sentence description of what the software does.]
- **Architecture:** Clean Architecture
- **Primary Objective:** Deliver the highest quality code possible — clean, maintainable, well-tested, and production-ready.

## 2. Tech Stack & Versions

*Use these specific versions. Do not introduce alternatives without explicit permission.*

### 2.1 Core

- **Language:** [e.g., TypeScript 5.x / Python 3.12]
- **Framework:** [e.g., Next.js 14 (App Router) / FastAPI]
- **Database:** [e.g., PostgreSQL 16 (Supabase) / MongoDB]
- **ORM/Data Layer:** [e.g., Prisma / SQLAlchemy / Sequelize]

### 2.2 Infrastructure & DevOps

- **Runtime:** Docker Container
- **CI/CD:** Gitlab

### 2.3 Additional Libraries (Standard Utils)

*Use these libraries to avoid bloating the bundle with duplicates.*

- **Date Handling:** [e.g., date-fns / Day.js / Native Date]
- **Validation:** [e.g., Zod / Pydantic / Joi]
- **HTTP Client:** [e.g., Axios / Native Fetch / TanStack Query]

### 2.4 Testing

- **Unit Testing Framework:** [e.g., Vitest / Mocha / Jest]
- **E2E Testing Framework:** [e.g., Playwright / Selenium]

### 2.5 Cybersecurity & Auth

*Strict adherence to security protocols is mandatory.*

- **Authentication:** [e.g., NextAuth.js v5 / Supabase Auth / Clerk]
- **Token Strategy:** [e.g., JWT (Stateless) / Session Cookies (HttpOnly)]
- **Cryptography:** [e.g., bcrypt for hashing / AES-256 for data at rest]
- **Authorization:** [e.g., RBAC (Role Based) / ABAC (Attribute Based) using CASL]

## 3. Engineering Standards

### 3.1 Code Style & Conventions

- **Paradigm:** [e.g., Strictly Functional, OOP with Design Patterns, Scripting]
- **Typing Policy:** [e.g., Strict Static Typing (No 'any'), Duck Typing with TypeHints]
- **Naming Convention:**
  - Variables: `[camelCase/snake_case]`
  - Classes/Components: `[PascalCase]`
  - Constants: `[UPPER_SNAKE_CASE]`
- **File Structure Strategy:** [e.g., Feature-based folders, MVC standard layout, Atomic Design]

### 3.2 Error Handling & Logging

- **Strategy:** Global Exception Handlers
- **Logging:** Use deeptrack/logging libraries

### 3.3 Security & Performance (CRITICAL)

- **Secrets:** Never expose API keys or secrets in code. Use `[ENV VAR PATTERN]`.
- **Validation:** Validate all external inputs at the boundary using `[Validation Library]`.
- **Performance:** [e.g., "O(n) complexity limit for data processing", "Optimize for memory usage over speed"]

## 4. Architectural Principles

*Choose the principles that apply to this specific project.*

- **SOLID:** [Yes/No/Partial]
- **DRY (Don't Repeat Yourself):** [Strict/Pragmatic]
- **Dependency Rule:** Inner layers must not depend on outer layers. Dependencies always point inward.
- **Abstraction Level:** [e.g., "Prefer composition over inheritance", "Keep abstractions shallow"]
- **Data Flow:** [e.g., Unidirectional data flow, Event sourcing]

## 5. Development Workflow

Before writing code, follow this sequence:

1. **🔍 ANALYZE SPECS:** Read `.specs/[feature].md` to check if specs have been generated
2. **🧠 PLAN:** Outline the steps based on the spec.
3. **💻 CODE:** Write code using the defined stack and defined skills.
4. **🔒 SECURE:** Ensure auth checks and input validation are present.
5. **✅ VERIFY:** Ensure code matches the `.specs` definition.

### Preferred CLI Commands

- **Install Dependencies:** `[Command]`
- **Run Local:** `[Command]`
- **Test:** `[Command]`
- **Lint/Format:** `[Command]`

## 6. Do's and Don'ts

| Category | DO ✅ | DON'T ❌ |
| --- | --- | --- |
| **Comments** | Explain *WHY*, not *WHAT*. | Comment obvious code |
| **Refactoring** | Propose refactors if you see technical debt. | Refactor unrelated files without permission. |
| **Dependencies** | Use existing libraries defined in project. | Add new libraries without asking. |

## 7. AI Interaction Guidelines

**Tone:** Professional, Technical, Concise.

**Code Output:**

- For large files, use precise search/replace blocks or standard diff syntax.
- Do not add comments like "// ... existing code" inside crucial logic blocks; show enough context.

**Behavior:**

- Challenge the user: If I ask for a pattern that violates the SOLID principles defined above, warn me and propose the correct alternative.

## 8. Project Skills

*This project uses skills to extend AI capabilities for specific tasks. Consult the corresponding skill when a task matches its trigger condition.*

| Skill Name | Path | When to Use |
| --- | --- | --- |
| [skill-name] | `skills/[skill-name]/SKILL.md` | [Describe when the AI should invoke this skill] |
| [skill-name] | `skills/[skill-name]/SKILL.md` | [Describe when the AI should invoke this skill] |
