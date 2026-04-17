## Why

The repository has already validated a working wiki workflow model across:

- wiki structure
- repo-local skills
- AGENTS-driven execution
- OpenSpec change governance
- Obsidian as the human-facing workspace

What is still missing is a concrete bootstrap path that can initialize a new repository with this validated setup in one pass. Right now the working model exists only as the current repository state, which makes reuse slow and error-prone.

The user wants an initialization script that installs the current best-practice kit directly, including:

- project skeleton
- AGENTS / CLAUDE entrypoints
- wiki structure
- current validated skills
- OpenSpec scaffold
- Obsidian scaffold
- examples based on current supported tasks

## What Changes

- Add a bootstrap script that initializes the wiki workflow kit into a target directory.
- Add reusable scaffold assets for wiki, examples, OpenSpec, Obsidian, and AI entrypoints.
- Define the first supported example set around current validated capabilities:
  - meeting notes
  - project management
  - learning notes
  - Weixin reading
  - GitHub analysis
  - explore trace

## Capabilities

### New Capabilities

- `wiki-workflow-kit-bootstrap`: The repository SHALL provide a bootstrap path that installs the current validated wiki workflow kit into a new target repository.

### Modified Capabilities

- `ai-chat-workflow-installer`: The installation model SHALL include a concrete initialization script and scaffold assets, not only design guidance.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/bootstrap-wiki-workflow-kit/`.
- Adds bootstrap code under `scripts/`.
- Adds scaffold assets derived from the current repository best practices.
