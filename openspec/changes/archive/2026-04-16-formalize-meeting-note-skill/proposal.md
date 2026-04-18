## Why

The repository already has a fixed meeting-note format, but the current `meeting-note-output` guidance only exists under `skills-drafts/`. That made the workflow look documented without making it discoverable to new Codex sessions, which caused the meeting-note flow to miss the formal skill trigger and Feishu delivery path.

The repo also needs a durable rule that distinguishes project-local skills from manual agent role templates, so future workflow changes do not confuse "draft guidance", "formal skill", and "manual sub-agent role" again.

## What Changes

- Promote the meeting-note workflow from `skills-drafts/meeting-note-output/` into a formal project-local skill under `.codex/skills/`.
- Define a publication rule: project-local skills are only considered active when they exist under `.codex/skills/`; `skills-drafts/` remains draft space only.
- Record the boundary that agent role templates are manual role assets, not repo-default routing mechanisms.
- Align repo guidance and meeting-note references to point at the formal skill path instead of the draft-only path.
- Add verification steps that prove the formal meeting-note skill exists in the discoverable local skill directory and that draft-only presence is no longer treated as sufficient.

## Capabilities

### New Capabilities
- `project-local-skill-publication`: Defines what makes a repo-local skill formally active, what remains draft-only, and how manual agent role templates differ from skills.

### Modified Capabilities
- `meeting-note-output-format`: Meeting-note workflow must be backed by a formally published local skill rather than draft-only guidance.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/formalize-meeting-note-skill/`.
- Adds `.codex/skills/meeting-note-output/SKILL.md` and related bundled files if needed.
- Updates repository guidance that currently points to `skills-drafts/meeting-note-output/`.
- Clarifies the usable path for project-local skills versus manual agent role templates.
