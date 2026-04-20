## Context

The repository already knows how to preserve disagreement material better than it did earlier:

- disagreement is calibration material before conclusion promotion
- anti-compression states are explicit
- `wiki/ops retro` is the first durable landing zone before `ADR`

That solved the preservation problem, but not the interruption problem.

The latest failure showed the gap clearly:

- the original user need was to improve agent understanding of historical disagreement and decision evolution
- the work later drifted into runtime context, routing, context injection, and bounded self-directed execution
- the user explicitly said the work had drifted
- the conversation still continued along the technical chain
- the disagreement was not automatically captured to `wiki/ops retro` before more continuation

So the missing mechanism is not more disagreement storage. The missing mechanism is a stop condition that forces requirement re-anchor.

## Goals / Non-Goals

**Goals**

- Define a live conversation gate that interrupts continuation when drift is signaled.
- Make the trigger signals concrete enough to drive default behavior.
- Require a repo-visible re-anchor artifact before further implementation continuation.
- Keep the gate narrow and human-readable.

**Non-Goals**

- Do not add external automation or runtime detection.
- Do not create a new repo-local skill in this change.
- Do not guarantee perfect drift detection.
- Do not turn every disagreement into a gate event.

## Decisions

### Decision: Use concrete drift signals instead of abstract disagreement language

The gate should not trigger on generic disagreement. It should trigger on clear signals that the current work may have drifted away from the last confirmed requirement.

Trigger signals:

- the user repeatedly says the work has drifted, is off-target, or should return to an earlier requirement
- the same `continue` can now mean materially different next steps
- the work is crossing from analysis, documentation, or modeling into runtime, automation, or execution
- the agent is continuing from the current technical chain instead of the last confirmed product goal

Alternative considered:
- Trigger on any strong disagreement.
  - Rejected because it would over-fire on normal calibration and factual correction.

### Decision: Gate action is stop-and-reanchor, not instant promotion

When the gate fires, the repository should stop continuation first and re-anchor before deciding promotion.

Mandatory actions:

1. stop implementation continuation
2. restate the original confirmed requirement
3. state the current chain being followed
4. judge whether drift has occurred
5. create or update a repo-visible `wiki/ops retro` unless the disagreement is already fully resolved in the active change

Alternative considered:
- Immediately promote the disagreement to `ADR`.
  - Rejected because drift may still be unresolved and unstable.

### Decision: Unblock requires explicit re-anchor

The repository should not continue implementation after gate trigger until re-anchor is explicit.

Unblock conditions:

- the user explicitly confirms the next mainline
- or a new OpenSpec change is created for the new direction
- or the retro / archive-review artifact records `keep`, `freeze`, and `next action`

Alternative considered:
- Allow the agent to continue after a short explanation.
  - Rejected because that recreates the same failure mode.

## Publication Plan

Publish the gate in three places:

- `AGENTS.md` as repository-default workflow policy
- `wiki/ops/disagreement-management-method.md` as method-layer guidance
- a repo-visible retro for the current drift event

The stable-decision question for ADR should be decided during archive review. The current change should not assume ADR promotion before the gate wording is validated.

## Pressure-Test Plan

Validate against these cases:

1. user says `continue`, but the current technical chain has already drifted beyond the last confirmed requirement
2. user rejects the framing repeatedly and asks to return to the earlier requirement
3. ordinary factual correction should not fire the gate

The change passes only if the gate distinguishes drift re-anchor from normal correction.

## Risks / Trade-offs

- [Risk] The gate could over-fire on ordinary disagreement. -> Mitigation: keep trigger language narrow and add explicit non-goals.
- [Risk] The gate could remain advisory instead of stopping work. -> Mitigation: define mandatory action and unblock conditions, not only principles.
- [Risk] Operators may still skip repo-visible capture. -> Mitigation: require retro or change-local closure artifact before continuation.
