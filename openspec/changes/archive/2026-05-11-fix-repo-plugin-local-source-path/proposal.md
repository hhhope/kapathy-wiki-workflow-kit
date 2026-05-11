# Fix Repo Plugin Local Source Path

## Why

The repo marketplace is registered in the user's Codex config, but the plugin is
still skipped at runtime. Codex rejects repo-root local plugin paths; marketplace
entries need to point at a plugin subdirectory under `./plugins/`.

## What Changes

- Package the repo-local Codex plugin under
  `plugins/report-wiki-portfolio/`.
- Update `.agents/plugins/marketplace.json` from `"."` to
  `"./plugins/report-wiki-portfolio"`.
- Update the marketplace contract test so this regression is caught before
  runtime.
- Update README documentation to point at the real plugin command path.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `wiki-status-slash-command`: marketplace metadata must point at the
  repo-local plugin subdirectory accepted by the current Codex plugin loader.

## Impact

- Affects `.agents/plugins/marketplace.json`, README, marketplace/runtime
  command tests, the new plugin package directory, and this OpenSpec change
  record.
- Does not change the slash command names, command files, wiki runtime behavior,
  or the documented install command.
