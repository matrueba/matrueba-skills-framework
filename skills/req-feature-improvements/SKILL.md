---
name: req-feature-improvements
description: Reviews and improves feature-specific requirements documents for rigor, completeness, and clarity. Use this skill to evaluate a feature specification (e.g., FEATURE_REQUIREMENTS_TEMPLATE) before starting development to ensure nothing is missing. For full project requirements, use req-base-improvements instead.
---

# Feature Requirements Improvements

Evaluate a feature requirements document for rigor, completeness, and clarity. Ask targeted questions to uncover gaps, then propose concrete improvements and new sections to define a solid feature specification. Save the improved version to the feature's requirements file.

## Workflow

### 1. Obtain the Feature Requirements Document

Check whether the user has provided a feature requirements document (inline, as a file path, or in the current conversation context).

- **If provided:** Read and proceed to the analysis phase.
- **If NOT provided:** Ask the user to supply one. Suggest common locations they might have it:
  > I need a feature requirements document to review. You can:
  >
  > - Paste the content directly here
  > - Give me a file path (e.g., `FEATURE_REQUIREMENTS_TEMPLATE.md` or a specific feature doc)

Do NOT proceed until you have the document content.

### 2. Initial Assessment

Read the document thoroughly and perform a structured evaluation using the quality checklist in `references/feature-quality-checklist.md`. Produce a brief internal assessment covering:

- **Coverage score** — How many of the checklist items are addressed (as a rough percentage)?
- **Strongest areas** — What the document does well.
- **Critical gaps** — What is missing or dangerously vague.
- **Ambiguities** — Statements that could be interpreted in multiple ways.

### 3. Present the Assessment

Share a concise summary with the user using this format. **Crucially, include a visual representation of the checklist** showing what is fulfilled and what is missing, so the user can easily see the gaps:

```markdown
# Feature Requirements Review: [Feature Name]

## Overall Verdict

[🟢 Solid — minor refinements needed | 🟡 Adequate — notable gaps to address | 🔴 Incomplete — significant sections missing]

## Visual Checklist

_(Render a condensed version of the quality checklist here. Use `[x]` for fulfilled items and `[ ]` for missing ones based on your assessment.)_

- [x] Context & Problem Statement
- [ ] Clear Scope (In and Out)
- [x] UX & Workflows
- [ ] Edge Cases & UI States
      _(...continue for the relevant sections...)_

## Strengths

- [What the document does well — be specific]

## Critical Gaps

- [Missing elements that would block implementation or cause ambiguity, like missing API contracts or error states]

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
- "The scope mentions 'in-app notifications' but doesn't specify if they should disappear automatically or require manual dismissal. Which approach do you prefer?"
- "The document lacks a fallback plan for the new API. If the endpoint responds with a 500 error, what should the UI show?"
- "You mentioned role restrictions, but are there specific permissions required for 'View' vs 'Edit' access in this feature?"

### 5. Propose Improvements

Once you have the user's answers (or if they skip the questions), generate a comprehensive improvement proposal. This should include:

#### 5a. Improvements to Existing Sections

For each section that needs work, provide:

- **What to change** — The specific edit or rewrite.
- **Why** — The reasoning behind the improvement (helps the user learn and make better requirements in the future).

#### 5b. New Sections to Add

Identify sections from the `feature-quality-checklist.md` that are entirely missing and should be included, such as:
- **UX & Workflows** (Happy Path, Edge Cases, UI States)
- **Architecture & Technical Contracts** (API Endpoints, DB schema impact)
- **Quality Attributes** (Performance, Security, Acceptance Criteria)
- **Telemetry & Success Metrics**
- **Rollout Plan & Contingency** (Feature flags, Rollback plan)

#### 5c. Consistency Check

Briefly check for alignment with overall project standards, if the context is available:
- Does this feature conflict with existing technical constraints or stack choices?
- Is there an overlap with existing features?

### 6. Generate and Save the Improved Document

After the user reviews and confirms the proposed improvements (or provides corrections):

1. Produce a clean, final version of the improved feature requirements document.
2. Save it back to the original file path (e.g., `features/my-new-feature.md`). If it was inline, ask the user where to save it.
3. If overwriting, ask for confirmation or offer to save it with a new name.

The final document must:
- Incorporate all accepted improvements and new sections.
- Integrate the user's answers to your questions.
- Follow the structure defined in the `start-feature-requirements` template where applicable.

## Evaluation Principles

When assessing feature requirements, keep these principles in mind:

- **A developer should be able to read the feature specs and start implementing without blocking questions.** If they can't, the specs are not rigorous enough.
- **Every edge case should be accounted for.** UI loading/error states, failed API calls, and permissions logic must be defined.
- **Scope boundaries are critical.** Explicitly stating what is NOT included in this feature iteration prevents scope creep.
- **Technical contracts matter.** A feature is rarely isolated; its API payloads, database changes, and dependencies must be clear.
- **Contingency is key.** Features need a rollout strategy and a clear "Kill Switch" or rollback plan.
