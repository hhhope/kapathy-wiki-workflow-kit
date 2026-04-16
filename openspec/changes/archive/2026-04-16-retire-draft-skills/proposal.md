## Why

The repository has already proven that project-local workflow reuse must publish through `.codex/skills/` rather than `skills-drafts/`. After formalizing the meeting-note workflow, one remaining draft skill still sits under `skills-drafts/`, and the draft directory still contains live-looking `SKILL.md` files. That leaves room for the same failure mode to recur: a contributor sees a draft skill, assumes it is published, and ships a workflow that future sessions cannot reliably discover.

## What Changes

- Publish the remaining `material-collaboration-defaults` workflow as a formal project-local skill under `.codex/skills/`.
- Remove active `SKILL.md` files from `skills-drafts/` so the draft directory no longer looks like a published runtime surface.
- Tighten repository guidance and OpenSpec requirements so every future draft skill must be either formally published under `.codex/skills/` or explicitly retired before the change is considered complete.

## Capabilities

### New Capabilities
- None.

### Modified Capabilities
- `material-collaboration-defaults`: The workflow now requires formal project-local skill publication.
- `project-local-skill-publication`: Publication rules now require draft-skill retirement or promotion before completion.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/retire-draft-skills/`.
- Publishes `.codex/skills/material-collaboration-defaults/SKILL.md`.
- Removes `SKILL.md` files from `skills-drafts/`.
- Tightens repository guidance in `AGENTS.md` and durable policy in `wiki/adr/`.
