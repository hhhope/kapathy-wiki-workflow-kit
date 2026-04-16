## Context

The repository already has two durable layers:

- `wiki/ops/` for operating-layer inputs, reminders, and handoff preparation
- OpenSpec artifacts for scoped changes and implementation progress

What is still missing is the bridge for exploration. When a user triggers `openspec-explore`, the discussion can produce valuable context, assumptions, and open questions before any formal change exists. Right now that context primarily lives in chat.

The repository wants a lightweight but mandatory trace that is visible in the repo before the exploration continues.

## Goals / Non-Goals

**Goals**

- Require a repo-visible explore trace before continuing `openspec-explore`
- Keep the trace lightweight
- Reuse existing `wiki/ops/` conventions instead of inventing a parallel container
- Prevent duplicate noise when the same topic is explored multiple times

**Non-Goals**

- Do not force every explore thread into a formal OpenSpec change immediately
- Do not create a brand-new page type beyond the existing `intake` model
- Do not turn explore traces into long-form design documents
- Do not replace the formal role of `proposal.md`, `design.md`, or `tasks.md`

## Decisions

### Decision: Explore traces live in `wiki/ops/`

The trace belongs in `wiki/ops/` because it is an operating-layer opening record, not yet a scoped implementation artifact.

Alternative considered:
- Put the trace directly in a change directory.
  - Rejected because the rule must also work before a formal change exists.

### Decision: Explore traces reuse `type: intake`

The repository will use the existing `intake` page type and add an explicit marker such as `explore_mode: true`.

Alternative considered:
- Add a brand-new `explore-intake` page type.
  - Rejected because the container semantics already fit `intake`, and a new type would add unnecessary complexity.

### Decision: Same-topic exploration updates the existing trace

When the new exploration clearly belongs to the same topic thread, the existing `wiki/ops/` record should be updated rather than duplicated.

Alternative considered:
- Always create a new page for each `openspec-explore` session.
  - Rejected because it would create noisy fragments and weaken continuity.

### Decision: Explore traces and OpenSpec artifacts have separate roles

- The explore trace records how the problem was opened: trigger, assumptions, current focus, unknowns, and next step.
- OpenSpec artifacts record what the repository decided to implement and how progress is tracked.

## Minimal Explore Trace Shape

Frontmatter:

- `title`
- `type: intake`
- `status`
- `updated_at`
- `explore_mode: true`

Body:

- Trigger question
- Current focus
- Current hypotheses
- Open questions
- Next step

## Evaluation Plan

### Baseline scenario

- User triggers `openspec-explore`
- Agent starts analyzing immediately
- No repo-visible exploration trace is created first

### After-change scenario

- User triggers `openspec-explore`
- Agent first checks whether a same-topic `wiki/ops/` explore trace exists
- If not, it creates one; if yes, it updates it
- Only then does the exploration continue

### Evidence to record

- Before-change repo guidance lacks a mandatory `openspec-explore -> wiki/ops/` rule
- After-change repo guidance and `wiki/ops/` sample make the new behavior explicit
- After-change policy still keeps `proposal.md`, `design.md`, and `tasks.md` as the formal source of truth for scoped changes

## Recorded Validation

### Before / after evidence

- Before: `AGENTS.md` had no repository-default `openspec-explore -> wiki/ops/` trace rule, and `wiki/ops/index.md` did not expose an explore-trace sample.
- After: `AGENTS.md` defines the default explore-trace rule, `wiki/ops/index.md` points to a trace sample, and `wiki/ops/sample-explore-trace.md` shows the minimum shape.

### Scope boundary confirmation

- The new rule requires a lightweight `wiki/ops/` trace before exploration continues.
- It does not require every explore thread to become a formal proposal, design, task list, or Codex handoff.
- Formal OpenSpec artifacts still begin only when the work becomes a scoped repository change.
