# Agent Skills Summary

This directory contains all the custom agent skills available in this repository. Each skill extends the agent capabilities for specific tasks.

## Guide
Each skill in the catalog is documented using the following format:

Skill Name
	- Shortcut: Quick shortcut command (e.g. /commit) if available, otherwise -.
	- Interactive?: Yes if the skill conducts a guided interview/asks questions, No if it executes directly.
	- Description: Explanation of what the skill does and when it should trigger.
	- Trigger Keywords: Keywords and phrases that trigger the skill or help manually invoke it.
	- Key Outputs: Primary files or deliverables produced by the skill.
	- Resources: Bundled folders (Scripts, Refs, Evals) accompanying the skill.

## Skill Catalog

[agent-loop](file:///root/matrueba-skills-framework/skills/agent-loop/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Executes an agent task in a progressive, iterative loop (similar to ralph loop). Use this skill for complex tasks that benefit from repeated refinement, detailed documentation of progress, and human-in-the-loop safety checks for critical actions. Trigger when the user mentions "loop mode", "iterative execution", or "ralph loop".
	- Trigger Keywords: "iterative execution", "loop mode", "ralph loop"
	- Key Outputs: Task progress documentation and iterative refinements
	- Resources: Scripts, Refs, Evals

[caveman](file:///root/matrueba-skills-framework/skills/caveman/SKILL.md)
	- Shortcut: `/caveman`
	- Interactive?: No
	- Description: Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Supports intensity levels: lite, full (default), ultra, wenyan-lite, wenyan-full, wenyan-ultra. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman. Also auto-triggers when token efficiency is requested.
	- Trigger Keywords: /caveman, "be brief", "caveman mode", "less tokens", "talk like caveman", "use caveman"
	- Key Outputs: Compressed natural language responses
	- Resources: None

[caveman-commit](file:///root/matrueba-skills-framework/skills/caveman-commit/SKILL.md)
	- Shortcut: `/caveman-commit`, `/commit`
	- Interactive?: No
	- Description: Ultra-compressed commit message generator. Cuts noise from commit messages while preserving intent and reasoning. Conventional Commits format. Subject ≤50 chars, body only when "why" isn't obvious. Use when user says "write a commit", "commit message", "generate commit", "/commit", or invokes /caveman-commit. Auto-triggers when staging changes.
	- Trigger Keywords: ", ", /caveman-commit, /commit, "t obvious. Use when user says ", "why"
	- Key Outputs: Conventional commit message in caveman speak
	- Resources: None

[caveman-compress](file:///root/matrueba-skills-framework/skills/caveman-compress/SKILL.md)
	- Shortcut: `/caveman:compress`
	- Interactive?: No
	- Description: Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format to save input tokens. Preserves all technical substance, code, URLs, and structure. Compressed version overwrites the original file. Human-readable backup saved as FILE.original.md. Trigger: /caveman:compress <filepath> or "compress memory file"
	- Trigger Keywords: /caveman:compress, "compress memory file"
	- Key Outputs: Compressed memory file (replaces original, backup created as .original.md)
	- Resources: Scripts

[caveman-help](file:///root/matrueba-skills-framework/skills/caveman-help/SKILL.md)
	- Shortcut: `/caveman-help`
	- Interactive?: No
	- Description: Quick-reference card for all caveman modes, skills, and commands. One-shot display, not a persistent mode. Trigger: /caveman-help, "caveman help", "what caveman commands", "how do I use caveman".
	- Trigger Keywords: /caveman-help, "caveman help", "how do I use caveman", "what caveman commands"
	- Key Outputs: Quick-reference list of caveman commands
	- Resources: None

[caveman-review](file:///root/matrueba-skills-framework/skills/caveman-review/SKILL.md)
	- Shortcut: `/caveman-review`, `/review`
	- Interactive?: No
	- Description: Ultra-compressed code review comments. Cuts noise from PR feedback while preserving the actionable signal. Each comment is one line: location, problem, fix. Use when user says "review this PR", "code review", "review the diff", "/review", or invokes /caveman-review. Auto-triggers when reviewing pull requests.
	- Trigger Keywords: /caveman-review, /review, "code review", "review the diff", "review this PR"
	- Key Outputs: Single-line code review comments
	- Resources: None

[codebase-agents-md](file:///root/matrueba-skills-framework/skills/codebase-agents-md/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Analyze an existing codebase and automatically generate a fully populated AGENTS.md file by extracting real information from the source code, config files, and project structure. Use this skill whenever the user wants to generate AI coding rules from their existing code, auto-detect their tech stack and conventions, create an AGENTS.md based on what's already in the repo, reverse-engineer project standards from code, or bootstrap AI context from a codebase. Also triggers when the user says things like 'read my code and create rules', 'generate AGENTS.md from this project', 'detect my stack', 'analyze my codebase for AI context', or 'auto-generate coding guidelines'. This skill differs from create-agents-md in that it requires an existing codebase — it reads and analyzes code rather than offering an empty template.
	- Trigger Keywords: ", ", ", or ", "s already in the repo, reverse-engineer project standards from code, or bootstrap AI context from a codebase. Also triggers when the user says things like "
	- Key Outputs: AGENTS.md file in the project root
	- Resources: Refs

[compress](file:///root/matrueba-skills-framework/skills/compress/SKILL.md)
	- Shortcut: `/caveman:compress`
	- Interactive?: No
	- Description: Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format to save input tokens. Preserves all technical substance, code, URLs, and structure. Compressed version overwrites the original file. Human-readable backup saved as FILE.original.md. Trigger: /caveman:compress <filepath> or "compress memory file"
	- Trigger Keywords: /caveman:compress, "compress memory file"
	- Key Outputs: Compressed memory file (replaces original, backup created as .original.md)
	- Resources: Scripts

[create-agents-md](file:///root/matrueba-skills-framework/skills/create-agents-md/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Generate or update an AGENTS.md file that serves as the AI assistant rulebook for a project. Use this skill whenever the user wants to create an AGENTS.md, set up AI coding guidelines, define project DNA for copilot/AI assistants, establish coding standards and conventions for AI tools, or bootstrap a new project with AI context rules. Also use it when the user mentions 'context for AI', 'copilot instructions', 'AI rules', 'project setup for AI', or wants to document their tech stack and engineering standards in a way that AI assistants can follow.
	- Trigger Keywords: /AI, "AI rules", "context for AI", "copilot instructions", "project setup for AI"
	- Key Outputs: AGENTS.md file in the project root
	- Resources: Refs, Evals

[create-requirements](file:///root/matrueba-skills-framework/skills/create-requirements/SKILL.md)
	- Shortcut: -
	- Interactive?: Yes
	- Description: Acts as a Tech Lead or Product Manager to generate a product requirements sheet. It has two modes — default (delivers the empty template to the user) and interactive (guided interview). Use this skill whenever the user asks you to create requirements for a functionality, document a new feature (such as "Metadata" or others), or if they mention they want to write the scope and impact of a new development.
	- Trigger Keywords: "Metadata"
	- Key Outputs: Product requirements specification sheet
	- Resources: None

[design-system-generator](file:///root/matrueba-skills-framework/skills/design-system-generator/SKILL.md)
	- Shortcut: -
	- Interactive?: Yes
	- Description: Generates a comprehensive frontend Design System & Guidelines document (DESIGN.md) for AI-assisted development. Use this skill when the user asks to define the visual style, design system, design tokens, CSS architecture, or frontend guidelines for a project. It asks discovery questions and produces a structured DESIGN.md file.
	- Trigger Keywords: "design-system-generator"
	- Key Outputs: DESIGN.md design system file in the project root
	- Resources: None

[frontend-design](file:///root/matrueba-skills-framework/skills/frontend-design/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
	- Trigger Keywords: /CSS, /beautifying
	- Key Outputs: Production-grade frontend UI components and layouts
	- Resources: None

[generate-commit-message](file:///root/matrueba-skills-framework/skills/generate-commit-message/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Analyze staged or unstaged changes since the last commit and propose a commit message following the Conventional Commits 1.0.0 specification. Use this skill whenever the user asks for a commit message, wants help writing a commit, asks to describe recent changes for a commit, or mentions 'conventional commit'. Also use it when the user says things like 'what should I commit', 'summarize my changes for git', or 'prepare a commit'.
	- Trigger Keywords: "conventional commit", "prepare a commit", "summarize my changes for git", "what should I commit"
	- Key Outputs: Git commit message adhering to Conventional Commits
	- Resources: Scripts, Evals

[manage-agent-memory](file:///root/matrueba-skills-framework/skills/manage-agent-memory/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Persistent memory system that saves and retrieves observations across sessions using SQLite with FTS5 full-text search. Use this skill proactively: save memories after architectural decisions, bug fixes, codebase discoveries, config changes, established patterns, or learned user preferences. Search memories when the user asks to recall past work, when starting tasks that may overlap with prior work, when the user references a topic you lack context on, or on the user's FIRST message to check for relevant prior work. Also trigger when the user says 'remember', 'recall', 'what did we do', 'have we done this before', or references past sessions.
	- Trigger Keywords: ", ", "s FIRST message to check for relevant prior work. Also trigger when the user says "
	- Key Outputs: Persistent database updates and query results
	- Resources: Scripts

[manage_documentation](file:///root/matrueba-skills-framework/skills/manage-documentation/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Create or update service documentation by analyzing code changes since the last merge. Use this skill when you need to generate comprehensive documentation following organizational standards. The skill analyzes the codebase to understand the service architecture, reviews git history for recent changes, and generates documentation in the mandatory template format. Use this whenever the user mentions updating docs, creating service documentation, documenting code changes, or preparing documentation for a project release.
	- Trigger Keywords: "manage-documentation"
	- Key Outputs: Updated service documentation matching code changes
	- Resources: Scripts, Refs

[next-best-practices](file:///root/matrueba-skills-framework/skills/next-best-practices/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Next.js best practices - file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, bundling
	- Trigger Keywords: /font
	- Key Outputs: Optimized Next.js components and APIs
	- Resources: None

[python-performance-optimization](file:///root/matrueba-skills-framework/skills/python-performance-optimization/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance.
	- Trigger Keywords: "python-performance-optimization"
	- Key Outputs: Performance profiling reports and optimized Python code
	- Resources: Refs

[req-base-improvements](file:///root/matrueba-skills-framework/skills/req-base-improvements/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Reviews and improves base project requirements documents for rigor, completeness, and clarity. Use this skill to evaluate the initial requirements sheet, define the core product vision, or ensure nothing is missing before starting a new project. For specific features, use req-feature-improvements instead.
	- Trigger Keywords: "req-base-improvements"
	- Key Outputs: Reviewed and improved base project requirements doc
	- Resources: Refs, Evals

[req-feature-improvements](file:///root/matrueba-skills-framework/skills/req-feature-improvements/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Reviews and improves feature-specific requirements documents for rigor, completeness, and clarity. Use this skill to evaluate a feature specification (e.g., FEATURE_REQUIREMENTS_TEMPLATE) before starting development to ensure nothing is missing. For full project requirements, use req-base-improvements instead.
	- Trigger Keywords: "req-feature-improvements"
	- Key Outputs: Reviewed and improved feature-specific requirements doc
	- Resources: Refs

[seo-audit](file:///root/matrueba-skills-framework/skills/seo-audit/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "page speed," "core web vitals," "crawl errors," or "indexing issues." Use this even if the user just says something vague like "my SEO is bad" or "help with SEO" — start with an audit. For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema-markup. For AI search optimization, see ai-seo.
	- Trigger Keywords: " ", " Use this even if the user just says something vague like ", " or ", "SEO audit,", "SEO health check,", "SEO issues,", "lost rankings,", "meta tags review,", "my traffic dropped,", "not showing up in Google,", "on-page SEO,", "site isn", "technical SEO,", "why am I not ranking,"
	- Key Outputs: Technical SEO audit report and recommendations
	- Resources: Refs, Evals

[skill-creator](file:///root/matrueba-skills-framework/skills/skill-creator/SKILL.md)
	- Shortcut: -
	- Interactive?: Yes
	- Description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
	- Trigger Keywords: "skill-creator"
	- Key Outputs: New/updated SKILL.md file and packaged .skill file
	- Resources: Scripts, Refs

[spec-generator](file:///root/matrueba-skills-framework/skills/spec-generator/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Creates technical specifications from feature requirements using a standardized template. Use this skill when the user asks to generate a spec, create a specification document, or implement a spec based on input requirements.
	- Trigger Keywords: "spec-generator"
	- Key Outputs: Technical specifications document
	- Resources: None

[specs-improvement](file:///root/matrueba-skills-framework/skills/spec-improvement/SKILL.md)
	- Shortcut: -
	- Interactive?: Yes
	- Description: Reviews and improves project specifications located in the ./specs directory. Use when you need to analyze, improve, or complete one or all project specifications. Proposes concrete improvements, identifies ambiguities, and asks the user questions to refine each spec. It can also be used to create a new spec from scratch.
	- Trigger Keywords: /specs
	- Key Outputs: Reviewed and improved spec document in ./specs
	- Resources: Refs

[start-base-requirements](file:///root/matrueba-skills-framework/skills/start-base-requirements/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Generates a base project requirements template in REQUIREMENTS_TEMPLATE.md. Use this skill when the user wants to start a new project, needs a requirements template, or asks for help structuring their initial product vision and scope.
	- Trigger Keywords: "start-base-requirements"
	- Key Outputs: REQUIREMENTS_TEMPLATE.md file
	- Resources: None

[start-feature-requirements](file:///root/matrueba-skills-framework/skills/start-feature-requirements/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Generates a feature requirements template in FEATURE_REQUIREMENTS_TEMPLATE.md. Use this skill when the user wants to start specifying a new feature for an existing project, needs a feature template, or asks for help structuring their feature vision and scope.
	- Trigger Keywords: "start-feature-requirements"
	- Key Outputs: FEATURE_REQUIREMENTS_TEMPLATE.md file
	- Resources: None

[suggest-fonts](file:///root/matrueba-skills-framework/skills/suggest-fonts/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: Analyzes the project's brand identity, purpose, and technical specifications to suggest premium font pairings and typography settings. Use this skill when the user wants to define or improve the visual style of their application, or when starting a new UI design.
	- Trigger Keywords: "suggest-fonts"
	- Key Outputs: Typography pairings and settings recommendations
	- Resources: None

[vercel-react-best-practices](file:///root/matrueba-skills-framework/skills/vercel-react-best-practices/SKILL.md)
	- Shortcut: -
	- Interactive?: No
	- Description: React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
	- Trigger Keywords: /Next
	- Key Outputs: Optimized React components and Vercel performance compliance
	- Resources: None
