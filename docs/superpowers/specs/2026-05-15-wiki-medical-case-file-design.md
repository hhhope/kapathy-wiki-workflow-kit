# Wiki Medical Case File Design

> Supports OpenSpec change: `introduce-wiki-medical-case-file`.
> This artifact is a post-hoc workflow repair. It does not claim the original
> Superpowers brainstorming gate was completed before the OpenSpec change was
> created.

## Context

The LLM-WIKI medical loop currently has durable stage records for doctor,
confirm, treatment, surgery, and recovery. That is useful for evidence, but it
created an authority drift risk during surgery planning:

```text
doctor record -> confirm record -> treatment record -> surgery record
```

The newest generated stage record can look like the current source of truth.
The user corrected the model: surgery should be based on content that has
already been diagnosed and confirmed, not on a fresh, independent surgery
record.

## Design Goal

Make one canonical case file the human review entry point for a medical-loop
run.

The case file owns:

- diagnosis
- confirmed decisions
- approved treatment
- surgery plan
- recovery result
- proof boundary
- next action

Stage records remain evidence attachments. They do not silently override the
case file.

## Approaches Considered

### Recommended: Canonical Case File With Stage Attachments

Use one file under `wiki/ops/wiki-medical-cases/` as the durable chart. Link
doctor, confirm, treatment, surgery, and recovery records as evidence.

Pros:

- Gives humans one review surface.
- Prevents "latest generated record wins".
- Preserves existing stage records as audit evidence.
- Fits the medical-loop metaphor.

Cons:

- Requires a case-file builder/updater before the full workflow is ergonomic.

### Alternative: Keep Separate Stage Records Only

Continue using separate records and rely on agents to trace the chain.

Pros:

- Minimal implementation change.
- Keeps current scripts mostly unchanged.

Cons:

- Already produced ambiguity.
- Makes review target unclear.
- Encourages drift from confirmed decisions.

### Alternative: Collapse Everything Into Surgery Record

Treat surgery record as the final current chart.

Pros:

- Simple for surgery-only review.

Cons:

- Recreates the failure: surgery becomes a new fact source.
- Weakens doctor/confirm authority.
- Makes recovery and archive harder to reason about.

## Design

Each medical-loop run has one canonical case file:

```text
wiki/ops/wiki-medical-cases/YYYY-MM-DD-<case-slug>.md
```

Required sections:

- `Case Source`
- `Diagnosis`
- `Confirmed Decisions`
- `Treatment`
- `Surgery Plan`
- `Recovery`
- `Archive / Next Action`
- `Evidence Attachments`
- `Proof Boundary`

Sections may be `pending`, but the file should show the full lifecycle shape.

## Review Semantics

Human review targets `Confirmed Decisions` first.

Surgery review is a fidelity check:

- It must derive from confirmed decisions.
- It must not re-diagnose raw script output.
- It must preserve relation weak evidence as manual review.
- It must route governance, ADR, taxonomy, MOC, and OpenSpec-sensitive work to
  the appropriate gate.
- It must not write frontmatter, relation fields, taxonomy config, MOC files,
  ADRs, AGENTS, skills, or OpenSpec lifecycle state without a later explicit
  apply workflow.

## Boundary

This design does not approve surgery application. It only defines the
source-of-truth model for later implementation.

## Approval State

The user approved continuing the concept in chat, but the original OpenSpec
proposal was written before this Superpowers support artifact existed. This
file repairs the evidence chain; it does not rewrite history.
