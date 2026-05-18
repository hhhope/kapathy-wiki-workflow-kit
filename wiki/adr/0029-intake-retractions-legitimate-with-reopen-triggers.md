---
layer: adr
domain: none
canonical_object: intake-retractions-legitimate-with-reopen-triggers
artifact_type: adr
---

# ADR-0029 Intake Retractions Are Legitimate With Explicit Reopen Triggers

## Status

Accepted

## Context

`compress-codex-agents-md` applied 11 `candidate-root-edit` rows from the Issue Routing Table adopted by `2026-05-06-decide-root-governance-alignment`. During execution, three of the eleven rows surfaced a gap: the intake finding, written weeks earlier, did not match the actual file state or the actual layer mapping once the Pattern Catalog was in effect.

- **S4** (extend rule-precedence to `agents/*`): `~/.codex/agents/*` are manual-only templates; the existing L274 already says they do not auto-trigger; there is no runtime precedence conflict to resolve.
- **A2** (consolidate three technical-checkpoint blocks): prior compression (M4 Paths merge) had already reduced the structure to a single section; nothing left to consolidate.
- **M5** (add read-only and UI self-check types): UI is governed by `~/.codex/rules/web/design-quality.md`; read-only operations carry real side-effect risk but the three-category (Write / External / DB) split had not yet caused a failure.

The question: can a change "retract" an intake finding rather than implement it? If yes, what prevents retractions from becoming a governance-laxity slope?

Three reading of the intake contract were considered:

1. Intake findings are commitments; each `candidate-root-edit` row must be implemented or the change fails.
2. Intake findings are candidate observations; a change may retract them silently if they no longer hold.
3. Intake findings are candidate observations; a change may retract them, but each retraction must record its reasoning and — critically — the trigger that would force a reopen.

Reading 1 would have forced `compress-codex-agents-md` to either implement overcalls (S4 adding a non-existent precedence conflict) or to never apply the routing table at all. Reading 2 would make the intake document eventually meaningless as retractions accumulate without audit. Reading 3 preserves the intake as a real record while allowing the catalog to be applied to the actual file state.

During the M5 discussion a second refinement emerged: retractions are not binary. The UI portion of M5 was a true overcall (already covered elsewhere); the read-only portion was a legitimate concern that this change chose not to solve yet. Compressing both into a single "retracted" label hid a preserved risk. The correction was to distinguish "fully retracted" from "partially retracted, residual risk preserved."

## Decision

- A change that applies an adopted routing table MAY retract individual rows rather than implement them, if the row no longer maps to the actual file state or if implementing it would duplicate content already covered elsewhere.
- Every retraction MUST be recorded in the change's `evaluation.md` with:
  - which row is being retracted (by ID),
  - why the retraction is justified (pointer to the actual file state or to the duplicating coverage),
  - whether the retraction is full or partial,
  - for partial retractions: which portion is retracted and which portion is preserved as residual risk,
  - for residual-risk portions: an explicit reopen trigger (e.g., "one real production-ish incident" or "a second recurring case").
- Retraction without recorded reopen triggers is not allowed. A row that is neither implemented nor has a trigger becomes silent drift.

## Consequences

- Intake documents remain a faithful audit trail: every row is either implemented, retracted with justification, or retracted partially with a reopen trigger. No row is dropped silently.
- Changes that apply routing tables are smaller and more honest: they do not over-implement phantom issues, and they do not over-defend by labeling kept content "acceptable."
- The governance thread gains a standing question: "what would force us to reopen this?" Each residual-risk entry names its trigger, making future monitoring concrete.
- A weakness remains: reopen triggers depend on someone noticing the trigger fire. The current `compress-codex-agents-md` M5 residual-risk reopen trigger ("one real read-only side-effect incident") has no active detector. This ADR does not solve that; it ensures the trigger is at least named in writing.
- If the volume of retractions starts to exceed the volume of implementations across multiple changes, that is a signal the intake process itself is producing too many overcalls and should be tightened. This ADR does not currently set a numeric threshold; a follow-up could.
