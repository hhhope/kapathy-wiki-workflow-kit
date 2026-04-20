## Why

The repository already states that semantic skill changes require behavior-level evaluation, but that requirement is still easy to bypass. The recent principle-skills publication followed the OpenSpec and publication flow, yet still missed true behavior TDD because no repository-level artifact or executable check enforced it.

## What Changes

- Require a dedicated `evaluation.md` artifact when an active change publishes or semantically edits project-local skills under `.codex/skills/`.
- Define the minimum behavior-proof structure for `evaluation.md`.
- Extend the repo health-check entry to fail when a skill-touching active change lacks the required behavior-evidence artifact.

## Capabilities

### New Capabilities
- `skill-evaluation-evidence`: Repository-level behavior-proof artifact for semantic skill changes.

### Modified Capabilities
- `repo-health-check`: The health-check entry now validates skill evaluation evidence for active changes.
- `project-local-skill-publication`: Published skill changes now require behavior-proof evidence, not only structure proof.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/enforce-skill-evaluation-evidence/`.
- Updates repository guidance in `AGENTS.md`.
- Extends repo health-check code and tests.
