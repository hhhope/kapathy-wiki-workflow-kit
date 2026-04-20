## Why

The repository now has a concrete weekly project-management workflow, but that behavior still lives in pages and conversation memory. The user wants this turned into a reusable skill so that when they say "项目管理", the agent consistently produces the right output types and follows the same operating pattern.

Without a skill, future turns may drift:

- wrong output shape
- missing weekly archive records
- weak distinction between source, intake, reminder, and Codex handoff
- loss of the current Nirvana-based reference pattern

## What Changes

- Create a local repo skill for weekly project-management handling.
- Encode the trigger conditions, expected inputs, fixed output types, and escalation rules.
- Reference the current Nirvana weekly records as the concrete example pattern.

## Capabilities

### New Capabilities

- `project-management-weekly-skill`: A reusable repo skill that standardizes how project-management requests are interpreted and what outputs must be produced.

### Modified Capabilities

None.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/project-management-weekly-skill/`.
- Adds a new local skill under `.codex/skills/project-management-weekly-skill/`.
- Gives future project-management turns a stable output contract based on the current wiki structure.
