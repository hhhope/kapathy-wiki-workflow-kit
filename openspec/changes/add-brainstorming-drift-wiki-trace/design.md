# Design: brainstorming drift wiki trace

## Rule Shape

When `$superpowers:brainstorming` is active and the user explicitly flags
repeated drift, the repository should stop the brainstorming continuation and
create or update a repo-visible `wiki/ops` trace before proceeding.

Concrete trigger signals include:

- the user says the agent has drifted, misunderstood, or mixed layers more than
  once in the same design discussion
- the user points to a numbered repetition such as "third drift"
- the agent is following the current technical chain instead of the user's
  stated design object
- the discussion crosses from design clarification into runtime, skill,
  OpenSpec, ADR, or repair execution without an approved design boundary

## Trace Shape

The trace should be a `wiki/ops` retro or workflow trace, not an ADR. It should
record:

- original user intent
- drift chain
- rejected framing
- corrected framing
- cause analysis
- affected active change, if any
- whether ADR consideration is deferred
- next allowed action

This mirrors the existing pattern for `$openspec-explore` trace and live
conversation re-anchor without treating brainstorming as the same skill.

## Boundary

The trace is evidence and re-anchor material. It does not by itself modify:

- Superpowers skills
- repo-local `.codex/skills/*`
- `AGENTS.md`
- runtime scripts
- accepted ADRs
- completed OpenSpec tasks

Those behavior changes require explicit OpenSpec implementation scope.

## 2026-05-14 Incident

The first trace records the wiki runtime conversation where the agent drifted
three times:

1. It treated `/wiki:apply` repair-route planning as if the repair routes were
   already executable runtime infrastructure.
2. It treated decision-trace eval as the repair path, instead of recognizing
   `$wiki-react` as the router and eval as validation only.
3. It continued from repair-route mechanics after the user invoked
   `$superpowers:brainstorming`, instead of stopping to record the repeated
   drift and re-anchor the design question.

## Verification

Verification should check:

- the OpenSpec proposal, design, tasks, and spec delta exist
- the incident trace exists under `wiki/ops`
- the trace has taxonomy-valid frontmatter for a new ops page
- the trace explicitly separates retro evidence from ADR decision
- no runtime scripts, skills, AGENTS, or accepted ADR files are modified by this
  proposal step
