## Why

The repository now has a meaningful workflow kit, but its top-level entry experience is still inconsistent: `main` remains under-documented, the bootstrap script does not install the same paths that the docs promise, and the repo-local OpenSpec skills describe interaction patterns that the current Codex runtime does not support. This makes first-time setup confusing for both Chinese and English readers and creates the false impression that OpenSpec itself is broken.

## What Changes

- Rewrite the root README into a bilingual installation and orientation entrypoint with explicit Chinese-first structure and a separate English section.
- Align bootstrap output, verification behavior, and documented quick-start steps so a freshly initialized kit contains the promised inbox and intake entrypoints.
- Repair repo-local `openspec-*` skills so they describe the current runtime's real interaction model and stop depending on nonexistent tools or slash commands.
- Add a Feishu-source comparison page that records what is already reflected in the repo and what still needs to be synced from the referenced article.

## Capabilities

### New Capabilities

- `installation-entry-guides`: Define the repository-level entry, installation, and verification guidance contract for readers and adopters of the workflow kit.

### Modified Capabilities

- `ai-chat-workflow-installer`: Clarify how the canonical installer model is exposed to bilingual readers and how runtime-specific entrypoints are documented without claiming unsupported native adapters.
- `wiki-workflow-kit-bootstrap`: Update the bootstrap and verification contract so installed repositories contain the minimum documented workflow kit paths and can be verified according to installation mode.

## Impact

- Affected docs: root `README.md`, Feishu comparison/source notes, and installation guidance pages.
- Affected code: bootstrap and verification scripts, plus new or updated unit tests around initialization and verification behavior.
- Affected behavior assets: repo-local `.codex/skills/openspec-*` skill files and their evaluation evidence.
- Affected dependencies and tooling guidance: OpenSpec CLI, Python runtime, optional Obsidian setup, and optional Feishu/Lark CLI setup instructions.
