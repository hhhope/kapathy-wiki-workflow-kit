## Why

The repository now has several local skills, migration patterns, and guardrails, but the central problem is not "how to manage skill files." The central problem is how the agent should evolve from work: extract reusable experience, reuse it later, patch it when it fails, and do all of that without asking the user to manually decide every time whether a new skill should be created.

After reviewing the Weixin article about Hermes Agent's Skills loop and locating the corresponding `NousResearch/hermes-agent` project, we need a traceable comparison that captures what Hermes does, what this repository already does well, and where our current approach is still too narrow. The review needs to shift from `skill governance` to `agent self-evolution governance`.

This review should leave a durable artifact instead of a one-off chat summary. The goal is not to copy Hermes wholesale. The goal is to benchmark our current approach against a strong external reference and define the next governance improvements with explicit boundaries, ADRs, and visible retro links.

## What Changes

- Add an OpenSpec review change that records the external sources, comparison dimensions, and repository-specific conclusions for Hermes-style `agent self-evolution governance`.
- Document the current strengths already present in this repository, including OpenSpec boundary enforcement, local-skill migration, structural TDD rules for weekly project-management visuals, and incident-driven retro capture.
- Document the main gaps relative to Hermes, especially:
  - lack of explicit experience-extraction triggers
  - lack of a candidate-memory layer between raw experience and stable reusable method
  - lack of incremental refresh semantics for already-structured knowledge
  - lack of a consistent human-governance layer over agent self-evolution
- Produce ADRs and follow-up change candidates so later implementation work can stay scoped instead of being improvised inside exploration.

## Capabilities

### New Capabilities
- `agent-self-evolution-review-trace`: The repository SHALL retain a traceable review of an external agent self-evolution reference, its source links, and the concrete follow-up implications for this repo.

### Modified Capabilities

None.

## Impact

- Adds review artifacts under `openspec/changes/hermes-skill-governance-review/`.
- Creates a durable record tying the Weixin article and the `NousResearch/hermes-agent` repository to concrete observations about agent self-evolution in this repo.
- Separates ADR capture from retro capture, so later contributors can distinguish "what we decided" from "what went wrong."
- Defines future change boundaries for self-evolution improvements without silently modifying current agent behavior during exploration.
