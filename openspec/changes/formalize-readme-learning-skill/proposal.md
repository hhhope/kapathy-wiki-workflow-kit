## Why

The repository now has two pieces in place:

- `example-driven wiki capture` formalizes that reusable learnings from examples should become repo-visible records without an extra reminder
- recent `gstack` and `larksuite/cli` learning pages show that GitHub-hosted READMEs can produce reusable workflow and skill insights

But there is still no dedicated skill for this task family.

That leaves a practical gap:

- GitHub or GitLab README analysis still depends on generic prompting
- the agent may stop at source summary instead of extracting reusable workflow learning
- the agent may fail to preserve the adaptation boundary between source and repository

The user wants a stable trigger:

- next time the user provides a GitHub or GitLab repo or README, the agent should route through a dedicated skill

## What Changes

- Add a repo-local skill for GitHub / GitLab README learning and adaptation
- Define the minimum extraction boundary for this task family:
  - what was reused
  - what was modified
  - what was rejected or left unformalized
  - where the learning should land in the repo
- Update example guidance so README analysis points to the new skill
- Record skill evaluation evidence in the change directory

## Capabilities

### New Capabilities

- `readme-learning-skill`: the repository SHALL provide a dedicated skill for GitHub and GitLab README learning tasks that extracts reusable repository learning rather than stopping at generic summary.

### Modified Capabilities

- `example-driven-wiki-capture`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/formalize-readme-learning-skill/`
- Adds a repo-local skill under `.codex/skills/`
- Tightens routing for future GitHub / GitLab README analysis requests
