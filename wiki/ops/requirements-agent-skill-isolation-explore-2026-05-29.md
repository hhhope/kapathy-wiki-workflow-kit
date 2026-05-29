---
title: requirements agent skill isolation explore
canonical_object: requirements-agent-skill-isolation
artifact_type: explore_trace
layer: ops
domain: ai-workflow
ops_area: workflow-trace
status: exploring
source_path: chat://openspec-explore/requirements-agent-skill-isolation/2026-05-29
updated: 2026-05-29
---

# Requirements Agent Skill Isolation Explore

## Trigger

The user invoked `$report-wiki-portfolio:openspec-explore` after rejecting a
requirements-analysis-agent answer that exposed Python commands instead of a
Codex-facing workflow entry.

## Boundary

This trace is exploratory only. Do not implement new skills, scripts, or
OpenSpec artifacts inside this explore step.

## Re-Anchor

The requirement workflow should follow the `wiki-medical-agent` pattern:

- the normal entry is a Codex skill;
- Python scripts are internal gates and evidence collectors;
- each lifecycle step has isolated authority;
- the top-level agent routes intent and state instead of asking the user to run
  scripts manually.

## Current Failure Shape

- The completed requirements work created taxonomy, case, checker, intent, and
  OpenSpec handoff scripts.
- It did not create the repo-local Codex skill entry that users expect as the
  normal runtime interface.
- The answer then drifted into a raw CLI usage path, which violated the intended
  medical-agent-style interaction model.
- A follow-up started creating a single skill-entry change, but the user's
  correction is broader: requirements lifecycle skills should be isolated by
  step, then composed by the whole-flow agent.

## Working Model

Requirements should be split into step skills first, then a controller skill:

- `requirements-intake`: collect source material and identify intent.
- `requirements-domain`: classify known domain or produce candidate domains.
- `requirements-roles`: normalize actor and owner roles from the requirements
  taxonomy.
- `requirements-stories`: extract and check user stories.
- `requirements-acceptance`: extract acceptance functions and story mappings.
- `requirements-gate`: run the hard readiness gate.
- `requirements-openspec-handoff`: create OpenSpec draft only after readiness.
- `requirements-analysis-agent`: user-facing controller that reports intent,
  case, state, allowed action, blocked action, and next action.

## Open Questions

- Whether every step skill should be repo-local `.codex/skills/*`, or whether
  some should stay as references under one controller skill.
- Whether the existing partial follow-up artifacts should be discarded and
  replaced by a broader OpenSpec change for the full lifecycle.
- Whether the first implementation should mirror `wiki-medical-agent` exactly
  or use it only as an interaction contract.
