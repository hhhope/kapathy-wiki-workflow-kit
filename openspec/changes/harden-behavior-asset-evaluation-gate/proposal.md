# harden-behavior-asset-evaluation-gate

## Why

The repo already requires `evaluation.md` for semantic skill changes, but the
current gate can pass shallow evidence. It checks for required section names but
does not prove positive and negative behavior, parent-gate preservation, or
non-overlapping routing ownership.

The Agent Intent Routing drift showed the gap: `High-Frequency Skills` already
owned the runtime skill routing map, while a new `Agent Intent Routing` section
introduced a second route table. Existing tests proved routing text existed but
did not detect duplicate ownership.

## What Changes

- Add `wiki/config/behavior-asset-evaluation.yaml` as the checker contract.
- Add `scripts/check_behavior_assets.py` for executable behavior-asset checks.
- Integrate the checker into `scripts/repo_health_check.py`.
- Compress `AGENTS.md` Agent Intent Routing so it references the single
  High-Frequency Skills route table instead of duplicating it.
- Strengthen pressure scenarios and evaluation evidence for skill and runtime
  routing changes.

## Non-Goals

- Do not scan archived OpenSpec changes by default.
- Do not build a general semantic static analyzer.
- Do not require multi-session rollout telemetry as the minimum gate.
