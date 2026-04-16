## Why

The current project-management weekly skill already requires checking gantt row alignment after editing visual weekly views, but it still does not explicitly require a failing structural check before the edit. That leaves room for post-fix verification without true TDD.

The user explicitly asked for this to be written into the skill.

## What Changes

- Tighten the project-management weekly skill so editable HTML/Gantt/weekly-visual files require a structural failing check before modification.
- Record the refinement in OpenSpec artifacts.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `project-management-weekly-skill`: adds a stricter TDD rule for structural weekly-visual edits.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/project-management-skill-structural-tdd/`.
- Updates `.codex/skills/project-management-weekly-skill/SKILL.md`.
