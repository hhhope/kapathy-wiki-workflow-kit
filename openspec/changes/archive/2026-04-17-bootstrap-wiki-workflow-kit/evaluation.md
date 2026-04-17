## Baseline Scenarios

### Scenario 1: Bootstrap script depends on untracked or missing runtime assets

- The repository has validated workflow assets, but no committed bootstrap path installs them into a new target repository.

### Scenario 2: OpenSpec action skills are not part of the committed reusable kit

- `openspec-explore`, `openspec-propose`, `openspec-apply-change`, and `openspec-archive-change` exist in the working tree but are not part of the committed reusable surface.

## Before Results

- No bootstrap script creates a target repository with entrypoints, wiki scaffold, skills, OpenSpec, Obsidian, and examples.
- The bootstrap scope cannot reliably depend on the OpenSpec action skills as versioned kit assets.

## After Results

- The repository includes a committed bootstrap script and verification script.
- The repository includes committed OpenSpec action skill files as part of the reusable kit surface.
- The bootstrap source now includes versioned examples and entry templates.

## Residual Risks

- The first bootstrap version still copies scaffold assets from the current repository layout, so future file moves must update the script manifest.
- `CLAUDE.md` is a first-pass compatibility entrypoint and may need refinement after real usage feedback.
