## Why

The repository now has several local skills, migration patterns, and guardrails, but the governance model is still mostly enforced by local discipline and incident-driven patching. After reviewing the Weixin article about Hermes Agent's Skills loop and locating the corresponding `NousResearch/hermes-agent` project, we need a traceable comparison that captures what Hermes does, what this repository already does well, and where our skill governance engineering still has clear gaps.

This review should leave a durable artifact instead of a one-off chat summary. The goal is not to copy Hermes wholesale. The goal is to benchmark our current approach against a strong external reference and define the next governance improvements with explicit boundaries.

## What Changes

- Add an OpenSpec review change that records the external sources, comparison dimensions, and repository-specific conclusions for Hermes-style skill governance.
- Document the current strengths already present in this repository, including OpenSpec boundary enforcement, local-skill migration, and structural TDD rules for weekly project-management visuals.
- Document the main gaps relative to Hermes, including skill lifecycle state, stale-skill maintenance, progressive disclosure/loading budget, hub-style trust policy, and stronger traceability from incidents back into skill updates.
- Produce follow-up change candidates so later implementation work can stay scoped instead of being improvised inside exploration.

## Capabilities

### New Capabilities
- `skill-governance-review-trace`: The repository SHALL retain a traceable review of an external skill-governance reference, its source links, and the concrete follow-up implications for this repo.

### Modified Capabilities

None.

## Impact

- Adds review artifacts under `openspec/changes/hermes-skill-governance-review/`.
- Creates a durable record tying the Weixin article and the `NousResearch/hermes-agent` repository to concrete governance observations for this repo.
- Defines future change boundaries for skill-governance improvements without silently modifying current skill behavior during exploration.
