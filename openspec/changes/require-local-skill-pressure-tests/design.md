## Context

This repo already tightened skill governance in two ways:

- skill changes require `evaluation.md`
- repo health check rejects skill changes without that artifact

However, the current required sections:

- `Baseline Scenarios`
- `Before Results`
- `After Results`
- `Residual Risks`

still allow evidence that is descriptive rather than pressure-tested.

## Goal

Make local pressure testing the minimum acceptable proof for semantic skill changes, without requiring multi-end or multi-session rollout tests.

## Decisions

### Decision: Require explicit pressure-test headings

For semantic skill changes, `evaluation.md` should explicitly show:

- `Pressure Scenarios`
- `RED Baseline`
- `GREEN Result`
- `Residual Risks`

This makes it much harder to hide behind vague before/after prose.

### Decision: Local pressure tests are the minimum gate

The minimum required proof is local pressure testing against representative scenarios.

Multi-end, multi-session, or rollout-level tests may still be valuable, but they are follow-up evidence rather than the minimum gate for completion.

### Decision: Backfill the newly enforced format for recent skill changes

The repo should backfill `harden-skill-authoring-contract` so the newly completed change matches the stronger standard.

## Non-Goals

- Require distributed or multi-end rollout testing for every skill change.
- Build a full automated conversation harness in this change.
