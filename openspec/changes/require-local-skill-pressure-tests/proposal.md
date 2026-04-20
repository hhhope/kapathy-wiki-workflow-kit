## Why

Skill changes in this repo already require `evaluation.md`, but the evidence format still allows weak before/after summaries with no explicit pressure test. That leaves too much room for structure-only validation and unclear RED/GREEN proof.

The immediate gap was exposed by the `harden-skill-authoring-contract` change:

- it included baseline and after-change evidence
- but the RED/GREEN pressure test was not explicit enough
- and there was no hard repo check requiring local pressure scenarios

## What Changes

- Require skill-change evaluation evidence to include explicit local pressure-test sections:
  - `Pressure Scenarios`
  - `RED Baseline`
  - `GREEN Result`
- Clarify that multi-end or multi-session rollout proof is optional follow-up, not the minimum gate.
- Extend the repo health check to reject skill changes whose `evaluation.md` lacks those sections.
- Backfill explicit local pressure-test evidence for `harden-skill-authoring-contract`.

## Impact

- Updates repo policy and validation for future skill changes.
- Makes local pressure testing the minimum non-negotiable proof for semantic skill edits.
