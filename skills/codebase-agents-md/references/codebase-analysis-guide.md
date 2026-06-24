# Codebase Analysis Guide

Detailed instructions for analyzing a codebase to extract its tech stack, conventions, and architecture. Follow each section in order.

## 2.1 Language & Runtime

| What to Find | Where to Look |
|---|---|
| Primary language | File extensions (count them — the most common wins), `tsconfig.json`, `pyproject.toml` |
| Language version | `package.json` engines field, `pyproject.toml [tool.python]`, `Dockerfile` base image tag, `.python-version`, `.nvmrc`, `.node-version`, `.tool-versions` |
| Runtime | `Dockerfile` FROM line, `docker-compose.yml` services |

## 2.2 Framework Detection

| What to Find | Where to Look |
|---|---|
| Web framework | Main entry point imports (`next`, `express`, `fastapi`, `flask`, `django`, `gin`, `actix`), framework config files (`next.config.*`, `nuxt.config.*`, `vite.config.*`, `angular.json`) |
| Component library | Import statements scanning for `react`, `vue`, `svelte`, `angular`, `solid` |
| API style | Route definitions (REST paths, GraphQL schemas, tRPC routers) |

## 2.3 Database & Data Layer

| What to Find | Where to Look |
|---|---|
| Database type | Connection string patterns in `.env.example` or docker-compose (e.g., `postgres://`, `mongodb://`, `mysql://`), ORM config files |
| ORM / Data layer | `prisma/schema.prisma`, `alembic/`, `migrations/`, SQLAlchemy models, Drizzle config, TypeORM entities |
| Migration tool | Migration directory structure and CLI scripts |

## 2.4 Infrastructure & DevOps

| What to Find | Where to Look |
|---|---|
| Containerization | `Dockerfile`, `docker-compose.yml`, `.dockerignore` |
| CI/CD | `.gitlab-ci.yml`, `.github/workflows/`, `Jenkinsfile`, `.circleci/`, `bitbucket-pipelines.yml` |
| Deployment | `vercel.json`, `netlify.toml`, `fly.toml`, `render.yaml`, Kubernetes manifests, Terraform files |
| Env var pattern | `.env.example`, `.env.sample`, docker-compose env definitions — document the **pattern**, never the values |

## 2.5 Testing Setup

| What to Find | Where to Look |
|---|---|
| Unit test framework | `jest.config.*`, `vitest.config.*`, `pytest.ini`, `conftest.py`, `_test.go` files, test directories |
| E2E framework | `playwright.config.*`, `cypress.config.*`, `selenium` imports |
| Test scripts | `package.json` scripts containing `test`, `Makefile` test targets |

## 2.6 Linting & Formatting

| What to Find | Where to Look |
|---|---|
| Linter | `.eslintrc.*`, `eslint.config.*`, `ruff.toml`, `pyproject.toml [tool.ruff]`, `.golangci.yml`, `clippy.toml` |
| Formatter | `.prettierrc.*`, `pyproject.toml [tool.black]`, `rustfmt.toml` |
| Type checking | `tsconfig.json` strict settings, `mypy.ini`, `pyproject.toml [tool.mypy]`, `pyright` config |

## 2.7 Auth & Security

| What to Find | Where to Look |
|---|---|
| Auth provider | Import statements for `next-auth`, `passport`, `clerk`, `supabase/auth`, `firebase/auth`, auth middleware files |
| Token strategy | JWT usage (look for `jsonwebtoken`, `jose`), session cookie config |
| Authorization model | RBAC definitions, permission files, CASL setup, policy files |
| Crypto | Hashing library imports (`bcrypt`, `argon2`), encryption config |

## 2.8 Code Conventions (Pattern Extraction)

This step requires scanning actual code — not config files.

1. **Naming conventions**: Sample 10-15 files across the project. Check variable names (camelCase vs snake_case), class names (PascalCase), constants (UPPER_SNAKE_CASE), file names (kebab-case vs camelCase vs PascalCase)
2. **Paradigm**: Look for class usage vs pure functions, dependency injection patterns, design patterns (repositories, factories, observers)
3. **File structure**: Map the top-level directory structure. Identify if it's feature-based (`features/auth/`, `features/users/`), layer-based (`controllers/`, `services/`, `repositories/`), or hybrid
4. **Error handling**: Look for try/catch patterns, custom error classes, Result/Either types, global error handlers
5. **Import patterns**: Absolute vs relative imports, barrel files (`index.ts`), path aliases (`@/`)

## 2.9 Key Libraries & CLI Commands

| What to Find | Where to Look |
|---|---|
| HTTP client | Imports of `axios`, `fetch`, `got`, `httpx`, `requests` |
| State management | `redux`, `zustand`, `pinia`, `mobx`, `jotai`, `recoil` |
| Validation | `zod`, `yup`, `joi`, `pydantic`, `class-validator` |
| Date handling | `date-fns`, `dayjs`, `luxon`, `moment` |
| CLI commands | `package.json` scripts (all of them), `Makefile` targets, `justfile` recipes, shell scripts in `scripts/` |

## 2.10 Specs & Skills

| What to Find | Where to Look |
|---|---|
| Specs | `.specs/` directory — if present, confirm the development workflow section should reference it |
| Skills | `skills/` directory, `.agents/skills/`, any `SKILL.md` files — populate the Project Skills table |

## 2.11 UI Design & Style

| What to Find | Where to Look |
|---|---|
| Design system | `DESIGN.md` at the project root — if found, it is the source of truth for UI design decisions |
| CSS approach | Imports of `tailwind`, styled-components, CSS modules (`.module.css`), SASS/LESS files, CSS-in-JS patterns |
| UI component library | `@mui`, `@chakra-ui`, `antd`, `shadcn`, `radix-ui`, `headlessui` |
