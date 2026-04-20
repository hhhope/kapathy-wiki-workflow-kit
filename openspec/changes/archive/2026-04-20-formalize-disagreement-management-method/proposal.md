## Why

The repository already preserves several durable layers well:

- `wiki/ops` for operational traces and retros
- `ADR` for stable project decisions
- OpenSpec for scoped workflow changes
- repo-local skills for reusable execution behavior

But recent workflow disagreements exposed a more upstream gap. The system still tends to preserve outcomes better than it preserves disagreement as calibration material. In practice that means:

- process arguments are compressed too quickly into governance conclusions
- repeated calibration pressure is treated as routing noise instead of goal drift evidence
- the repository lacks a formal default for preserving disagreement evolution before promotion into `ADR`, spec, or skills

The user clarified that the main value is not "more complete ADR hygiene." The main value is preserving disagreement-exposed judgment movement so the project can keep recalibrating toward its deeper goal while co-building a self-evolving agent.

## What Changes

- Define a repository-default disagreement-management method as an upstream workflow layer.
- Make explicit that the first preservation target is disagreement as calibration material, not conclusion-only governance artifacts.
- Define the minimum preserved raw material before the repository is allowed to summarize, name, or promote the disagreement.
- Define the thresholds and intermediate states that prevent premature compression:
  - raw correction pressure
  - disagreement redirection
  - unclear state
  - first positive naming threshold
- Define the boundary between disagreement management and downstream containers such as `wiki/ops retro`, `ADR`, OpenSpec specs, and repo-local skills.

## Capabilities

### New Capabilities

- `disagreement-management-method`: The repository SHALL preserve disagreement as goal-calibration material before promoting it into downstream conclusion layers.

### Modified Capabilities

- `personal-ops`
- `archive-review-defaults`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/formalize-disagreement-management-method/`.
- Defines a new formal workflow capability for disagreement management.
- Prepares later repo-visible publication in `wiki/ops/`, `AGENTS.md`, and possibly `wiki/adr/`, but does not publish those artifacts in this proposal step.
