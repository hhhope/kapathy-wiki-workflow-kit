## Why

The repository now has a meaningful workflow surface:

- repo governance in `AGENTS.md`, ADRs, and OpenSpec
- formal repo-local skills under `.codex/skills/`
- wiki operating guidance under `wiki/`

That surface works inside this repository, but it is not yet packaged into a reusable installation flow for multiple AI chat runtimes. The user wants a one-click installation experience that can carry the current wiki workflow and skill model into at least three targets:

- Cursor
- Claude
- Codex

The repository also needs a shareable explanation for Feishu so that the installation model can be communicated clearly instead of remaining implicit in repo structure.

Without a formal change, this work risks drifting into ad hoc file exports or a misleading "single skill for every platform" story even though the three targets have different runtime surfaces.

## What Changes

- Define a canonical repository-owned AI chat workflow installer model.
- Define platform adapter outputs for Cursor, Claude, and Codex.
- Define the repository boundary between:
  - canonical workflow source
  - platform-specific installation artifacts
  - shareable explanation material
- Create a Feishu-shareable explanation artifact for the installer model and its platform mappings.

## Capabilities

### New Capabilities

- `ai-chat-workflow-installer`: The repository SHALL define a reusable installer model that maps its workflow and skill system into multiple AI chat runtimes.

### Modified Capabilities

- `project-local-skill-publication`: Repo-local skills SHALL be installable as part of a broader AI chat workflow package rather than treated as the only portable runtime surface.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-ai-chat-workflow-installer/`.
- Establishes the intended design for future installer outputs without yet changing runtime guidance.
- Prepares a later implementation pass for installer assets and Feishu-facing documentation.
