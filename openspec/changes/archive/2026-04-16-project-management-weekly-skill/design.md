## Context

The current repo has already established the practical weekly PM flow:

- `wiki/ops/project-management-weekly-loop.md`
- weekly Nirvana source page
- weekly HTML view source page
- weekly intake page
- weekly reminder page

The user now wants this behavior promoted into a skill so future turns that mention project management automatically use the same pattern.

This is a skill-writing task, so it must preserve:

- trigger-focused description
- concise body
- repo-local references
- TDD-style before/after evidence

## Goals / Non-Goals

**Goals:**

- Create a skill that triggers on weekly project-management handling.
- Define the fixed output types:
  - source
  - html/source companion when present
  - intake
  - reminder
  - Codex handoff candidate judgment
- Define what information to extract:
  - milestone
  - progress
  - drift
  - risks
  - next actions
  - ownership
- Use current Nirvana records as the reference example.

**Non-Goals:**

- Add new automation scripts.
- Convert this into a team-global skill outside the repo.
- Encode every project-specific detail from Nirvana into the trigger description.

## Decisions

### Decision: Make the skill trigger on "when to use", not on workflow summary

The description will focus on situations like:

- user says "项目管理"
- user provides weekly report / milestone / risk / gantt / project progress material
- user wants a PM weekly summary or follow-up structure

The description will not summarize the full workflow, to avoid shortcut behavior.

### Decision: Fix the output contract inside the skill

The skill will explicitly require the agent to decide among these outputs:

- spreadsheet or document source page
- weekly HTML/source companion page when a visual file exists
- intake page
- reminder page
- optional Codex handoff candidate decision

### Decision: Include repo references as examples

The skill should point to the current Nirvana weekly pages so future execution has concrete local examples to mirror.

## Risks / Trade-offs

- [Risk] The skill could become too Nirvana-specific. → Mitigation: keep Nirvana as example only; define generic PM triggers and outputs.
- [Risk] The skill could become too long and reduce discoverability. → Mitigation: keep the document concise and trigger-oriented.
- [Risk] Future workflow changes could outdate the skill. → Mitigation: anchor it to current pages and state the core invariant output types.

## Migration Plan

1. Create and validate the change artifacts.
2. Add the repo-local project-management weekly skill.
3. Run post-change checks that prove the skill now exists and contains the required trigger/output structure.
