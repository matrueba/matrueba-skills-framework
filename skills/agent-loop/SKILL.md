---
name: agent-loop
description: Executes an agent task in a progressive, iterative loop (similar to ralph loop). Use this skill for complex tasks that benefit from repeated refinement, detailed documentation of progress, and human-in-the-loop safety checks for critical actions. Trigger when the user mentions "loop mode", "iterative execution", or "ralph loop".
---

# Agent Loop

This skill enables you to tackle complex objectives by breaking them down into iterative cycles of research, planning, execution, and documentation. It ensures transparency and safety through progressive logging and mandatory user confirmation for critical actions.

## 1. Initialization

When this skill is triggered, you MUST perform the following setup steps:

1.  **Iterative Budget**: Ask the user for the number of iterations they want to run.
    - Default: **3 iterations**.
    - Maximum: **30 iterations**.
2.  **Execution Mode**: Ask the user to choose between:
    - **Default**: Focus on token efficiency. Use broad searches, cache-ready tools, and avoid redundant file reads.
    - **Madness**: Focus on absolute quality and exhaustive verification. Token consumption is not a concern.
3.  **Documentation Site**: Initialize a file named `AGENT_LOOP_LOG.md` in the current working directory to track progress.

## 2. The Iteration Cycle

In each iteration, follow this workflow:

### A. Research & Analysis
- **Goal Check**: Evaluate the current state against the primary objective.
- **Progress Report**: Identify what has been accomplished and what remains.
- **Mode Logic**:
    - `default`: Use `grep` and `ls -R` efficiently. Read only high-impact files.
    - `madness`: Perform deep traversals, exhaustive `view_file` calls, and cross-reference multiple sources.

### B. Planning
- Draft a mini-plan for the *current* iteration.
- **Safety Pre-check**: If the plan involves any potentially destructive or critical actions (see Safety section), you MUST pause and ask for user confirmation.

### C. Execution
- Perform the planned actions using the available toolset.
- **Mode Logic**:
    - `default`: Make concise edits. Avoid massive overwrites unless necessary.
    - `madness`: Implement comprehensive solutions, including extensive tests and meticulous documentation.

### D. Documentation & Logging
- After executing changes, run the `scripts/log_iteration.py` helper to update the log.
- Include:
    - Iteration ID.
    - Actions taken.
    - Outcome and status of the objective.
    - Planned next steps.

## 3. Safety: Human-in-the-Loop

You MUST detect when a "critical action" is about to be performed. A critical action is defined as:
- Deleting files or directories (`rm`, `delete_block`).
- Large-scale file overwrites (multiple `multi_replace_file_content` or `overwrite: true` with large payloads).
- Structural project changes (moves, resets, destructive git commands).
- External network requests or data exfiltration.

**Protocol**:
1. Flag the command as **[CRITICAL]**.
2. Explain *why* it is critical and what the potential impact is.
3. **STOP** execution and wait for the user to say "Proceed", "Skip", or "Abort".

## 4. Completion

The loop ends when:
1. The objective is met.
2. The iteration budget is exhausted.
3. The user manually terminates the loop.

Upon completion, provide a final summary of all work done and point the user to `AGENT_LOOP_LOG.md`.

---

## Technical Helpers

- **Log Progress**: `python scripts/log_iteration.py --iteration N --msg "Summary of work"`
- **Safety Check**: `python scripts/check_safety.py --command "your command"`
