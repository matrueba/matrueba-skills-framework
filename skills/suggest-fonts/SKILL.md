---
name: suggest-fonts
description: Analyzes the project's brand identity, purpose, and technical specifications to suggest premium font pairings and typography settings. Use this skill when the user wants to define or improve the visual style of their application, or when starting a new UI design.
---

# Suggest Fonts

This skill helps you select the perfect typography for a project by analyzing its core identity and requirements without wasting context on irrelevant files.

## Workflow

### 1. Initial Analysis (Context Collection)

To understand the project's "soul" and technical constraints, you MUST inspect the following specific locations IN ORDER. **Do not perform a recursive crawl of the entire project.**

1.  **`AGENTS.md`**: Look for the brand voice, persona descriptions, and overall project philosophy.
2.  **`specs/` directory**: Search for functional requirements, UI/UX specifications, or design notes.
3.  **Core Project Metadata**: Quickly check the `README.md` or `package.json` for the project name and high-level description if the above files are missing.

### 2. User Interview (Gap Filling)

If after the initial analysis you do not have a clear picture of the project's visual direction (e.g., target audience, desired "vibe", industry), you MUST ask the user **3 to 5 targeted questions**.

_Example questions:_

- Who is the primary audience (technical users, consumers, corporate)?
- What "vibe" should the interface project (minimalist, brutalist, friendly, professional, futuristic)?
- Are there any accessibility requirements or specific technical constraints (e.g., must be a system font)?
- Do you have a preferred primary color or a specific brand name?

### 3. Typography Suggestion

Based on the gathered context, provide **three distinct typography palettes**. Each should include:

- **Heading Font**: Recommended weight and style.
- **Body Font**: Recommended weight and line-height.
- **Rationale**: Why this pairing fits the specific project context found in `agents.md` or `specs`.
- **Implementation**: Vanilla CSS code snippet for easy application.

Refer to `assets/fonts.md` (if available) for premium, curated font pairs from Google Fonts or standard system stacks.

## Design Principles for Selections

- **Visual Excellence**: Avoid defaults. Use modern, premium fonts (e.g., Inter, Montserrat, Playfair Display, Outfit).
- **Harmony**: Ensure the heading and body fonts complement each other.
- **Readability**: Prioritize legibility in body text.
- **Hierarchy**: Define clear contrast between headings and body.
