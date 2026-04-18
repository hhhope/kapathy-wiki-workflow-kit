## Why

The repository already has strong governance rules and concrete workflow skills, but it still lacks a short, high-frequency principle layer that can interrupt common agent failure modes before a workflow skill is chosen. The recent review of `forrestchang/andrej-karpathy-skills` clarified the missing layer: a few compact principles that are easier to trigger in-the-moment than long governance prose.

## What Changes

- Add a formal principle-skills layer for high-frequency reasoning constraints.
- Publish four minimal project-local principle skills:
  - `clarify-before-acting`
  - `simplicity-first`
  - `surgical-changes`
  - `verify-before-claiming`
- Add a short `High-Frequency Principles` entry section to the repository `AGENTS.md` that routes to the new layer without replacing existing governance or workflow skills.

## Capabilities

### New Capabilities
- `principle-skills-layer`: Short project-local principle skills for cross-workflow behavioral correction.

### Modified Capabilities
- `project-local-skill-publication`: The repository now publishes both workflow skills and principle skills through `.codex/skills/`.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-principle-skills-layer/`.
- Publishes four new principle skills under `.codex/skills/`.
- Updates repository guidance in `AGENTS.md`.
