## Why

The repository now has formal project-local skills, but the skill authoring contract is still underspecified. Recent skill generation exposed three concrete gaps:

- there is no hard rule saying project-local `SKILL.md` files must default to English
- repo-specific delivery constraints such as Feishu-facing workflow expectations are not guaranteed to be inherited when new skills are authored
- current skill bodies are drifting longer than necessary, which increases token cost and makes trigger-time retrieval noisier

These gaps create real quality failures:

- new skills can be generated in Chinese because the repo's wiki language policy bleeds into skill files
- Feishu-related delivery boundaries may be omitted unless the author happens to start from a Feishu-aware workflow skill
- skills accumulate duplicated repo context instead of staying compact and reference-oriented

## What Changes

- Tighten the shared skill-authoring contract in `writing-skills`, `skill-creator`, and the common development workflow rule so skill generation defaults to:
  - English-first behavior assets
  - repo-constraint scanning before authoring
  - compact `SKILL.md` bodies with longer material moved to `references/`
- Define the repository-local application of that contract:
  - `wiki/*`: Chinese-first
  - `.codex/skills/*`: English-first
  - repo-specific delivery constraints remain owned by repo `AGENTS.md`
- Refactor the current repo-local skills that violate the new contract.
- Add evaluation evidence and any minimal repo-side checks needed to keep the contract visible.

## Capabilities

### New Capabilities
- `skill-authoring-contract`: Repository-local contract for language, inheritance, and token-efficient skill structure.

### Modified Capabilities
- `principle-skills-layer`
- `project-local-skill-publication`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/harden-skill-authoring-contract/`.
- Updates the shared skill-authoring guidance that future skill work follows.
- Refactors the repo-local skills that currently violate the new contract.
- Leaves evaluation evidence for the language, inheritance, and token-compression changes.
