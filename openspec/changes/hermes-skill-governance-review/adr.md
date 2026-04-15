# ADR Set: Hermes Review Reframe

This file captures decision records from the Hermes review. It is not a retro. It records what this repository decided after comparing Hermes with the current agent workflow.

## ADR-001: Reframe from skill governance to agent self-evolution governance

- Status: accepted
- Date: 2026-04-15

### Context

The first draft of the review centered too narrowly on skill lifecycle and skill inventory. That framing missed the user's primary goal: the agent should not wait for the human to manually decide every time whether a skill should be created. The human should govern the evolution process, not micromanage each creation decision.

### Decision

This repository will treat Hermes primarily as a reference for `agent self-evolution governance`, not merely `skill governance`.

### Consequences

- Future changes should focus on experience extraction, candidate memory, reuse, patching, and human governance.
- Skill metadata remains useful, but it is no longer the top-level framing.

## ADR-002: Separate ADR visibility from retro visibility

- Status: accepted
- Date: 2026-04-15

### Context

The repository already has retro-style capture in `wiki/ops/scope-drift-retro.md`, but that records failures, not design decisions. Important governance choices are still easy to lose in chat history.

### Decision

Governance reviews must capture:

- ADRs for decisions and boundaries
- retros for failures and their lessons

These two record types must remain visible as separate artifacts.

### Consequences

- Later work can distinguish "why we decided this" from "what failed before."
- Governance changes become reviewable without replaying the whole conversation.

## ADR-003: Prefer incremental refresh over default full reprocessing

- Status: proposed
- Date: 2026-04-15

### Context

The repository currently defines intake and weekly project-management processing, but it does not yet make a strong distinction between:

- raw material not yet structured
- already-structured material
- material that changed and only needs refresh
- stale material that may mislead the agent

Without that state model, the agent naturally drifts toward full reprocessing.

### Decision

Future design work should introduce a state-driven incremental refresh model so the agent can decide whether to skip, refresh, relink, or fully restructure.

### Consequences

- This ADR is not yet implemented.
- A follow-up change should decide the concrete state model and where those states live.
