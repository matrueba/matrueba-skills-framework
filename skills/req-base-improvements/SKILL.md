---
name: req-base-improvements
description: Reviews and improves base project requirements documents for rigor, completeness, and clarity. Use this skill to evaluate the initial requirements sheet, define the core product vision, or ensure nothing is missing before starting a new project. For specific features, use req-feature-improvements instead.
---

# Requirements Improvements

Evaluate a base project requirements document for rigor, completeness, and clarity. Ask targeted questions to uncover gaps, then propose concrete improvements and new sections to define a solid foundation. Save the improved version to `REQUIREMENTS.md`.

## Workflow

### 1. Obtain the Requirements Document

Check whether the user has provided a requirements document (inline, as a file path, or in the current conversation context).

- **If provided:** Read and proceed to the analysis phase.
- **If NOT provided:** Ask the user to supply one. Suggest common locations they might have it:
  > I need a requirements document to review. You can:
  >
  > - Paste the content directly here
  > - Give me a file path (e.g., `REQUIREMENTS.md`)

Do NOT proceed until you have the document content.

### 2. Initial Assessment

Read the document thoroughly and perform a structured evaluation using the quality checklist in `references/quality-checklist.md`. Produce a brief internal assessment covering:

- **Coverage score** — How many of the checklist items are addressed (as a rough percentage)?
- **Strongest areas** — What the document does well.
- **Critical gaps** — What is missing or dangerously vague.
- **Ambiguities** — Statements that could be interpreted in multiple ways.

### 3. Present the Assessment

Share a concise summary with the user using this format. **Crucially, include a visual representation of the checklist** showing what is fulfilled and what is missing, so the user can easily see the gaps:

```markdown
# Requirements Review: [Document Title or Feature Name]

## Overall Verdict

[🟢 Solid — minor refinements needed | 🟡 Adequate — notable gaps to address | 🔴 Incomplete — significant sections missing]

## Visual Checklist

_(Render a condensed version of the quality checklist here. Use `[x]` for fulfilled items and `[ ]` for missing ones based on your assessment.)_

- [x] Document Metadata
- [ ] Clear Scope and Out of Scope
- [x] User Profiles
- [ ] Prioritization (MoSCoW)
      _(...continue for the relevant sections...)_

## Strengths

- [What the document does well — be specific]

## Critical Gaps

- [Missing elements that would block implementation or cause ambiguity]

## Ambiguities

- [Statements open to multiple interpretations, with a brief explanation of why they are problematic]
```

### 4. Ask Targeted Questions (3 to 5)

After presenting the assessment, ask the user **between 3 and 5 targeted questions** to fill the most impactful gaps. These questions should:

- Be ordered by priority (most blocking first).
- Target information that you cannot reasonably infer from the existing document.
- Be specific enough that the user can answer in one or two sentences.
- Avoid generic questions like "Can you provide more detail?" — instead, name the exact gap.

_Example questions:_

- "The document mentions 'high availability' but doesn't define an SLA. What uptime percentage are you targeting (e.g., 99.9%)?"
- "There are no error-handling flows described. What should happen when the external payment API is unreachable — retry, queue, or fail immediately?"
- "The scope says 'mobile support' but doesn't specify platforms. Are you targeting iOS, Android, or both? PWA or native?"
- "Who is the primary decision-maker or product owner for this project?"
- "Are there any hard technical constraints (e.g., specific cloud provider, programming language) we must adhere to from day one?"

### 5. Propose Improvements

Once you have the user's answers (or if they skip the questions), generate a comprehensive improvement proposal. This should include:

#### 5a. Improvements to Existing Sections

For each section that needs work, provide:

- **What to change** — The specific edit or rewrite.
- **Why** — The reasoning behind the improvement (helps the user learn and make better requirements in the future).

#### 5b. New Sections to Add

Identify sections that are entirely missing and should be included. Reference the standard template sections from the quality checklist. Common candidates:

- **Introduction** (Purpose, Product Vision, Scope, Out of Scope, Glossary)
- **User Profiles / Personas** — Roles and needs of each user type.
- **Functional Requirements** — User stories, business logic, data management.
- **Workflows** — Step-by-step key processes with flowcharts or sequence diagrams.
- **Quality Attributes (Non-Functional Requirements)** — Performance, scalability, security, usability, availability, observability, testing strategy.
- **Interface Requirements (UI)** — Theming, color palette, typography, responsive behavior, asset strategy, animations, interface states (loading, empty, error).
- **Constraints** — Technological choices with rationale, third-party services, regulatory/legal, resources and time.
- **Dependencies & Assumptions** — External systems, facts taken for granted that could affect the project.
- **Acceptance Criteria** — Testable conditions for "done" (Definition of Done).

Only propose sections that are genuinely relevant to the base project — don't pad the document with unnecessary boilerplate.

#### 5c. Consistency Check

If the repository already has a `README.md`, an `architecture.md`, or a `package.json`, briefly check for:

- Alignment with existing technical constraints or stack choices.
- Inconsistent terminology.
- Overlapping scope with what's already built.

Report any findings in the proposal.

### 6. Generate and Save REQUIREMENTS.md

After the user reviews and confirms the proposed improvements (or provides corrections):

1. Produce a clean, final version of the improved requirements document.
2. Save it as `REQUIREMENTS.md` in the project root (or in a path specified by the user).
3. If a `REQUIREMENTS.md` already exists, ask the user whether to overwrite it or save with a different name.

The final document must:

- Incorporate all accepted improvements and new sections.
- Integrate the user's answers to your questions.
- Maintain the original structure where it was already strong.
- Use clear, unambiguous language throughout.
- Include a "Last Reviewed" date at the top.

## Evaluation Principles

When assessing requirements quality, keep these principles in mind:

- **A developer should be able to read the requirements and start implementing without blocking questions.** If they can't, the requirements are not rigorous enough.
- **Every requirement should be testable.** If you can't write an acceptance test for it, it's too vague.
- **Scope boundaries matter as much as scope contents.** Explicitly stating what is NOT included prevents scope creep and misunderstandings.
- **Assumptions are hidden risks.** Unstated assumptions will surface as bugs or delays — surface them early.
- **Prioritization prevents paralysis.** If everything is "must have", nothing is. Help the user distinguish between critical, important, and nice-to-have requirements by applying a prioritization framework like **MoSCoW** (Must have, Should have, Could have, Won't have).
