# Add Repo Plugin Marketplace Install Path

## Why

The repo now contains a Codex plugin command for `/wiki:status`, but plugin
discovery is marketplace-based. A clone of this repo should include the
marketplace metadata and installation instructions needed for Codex to discover
the repo plugin without relying on personal global prompt files.

## What Changes

- Add repo-local `.agents/plugins/marketplace.json`.
- Document the Codex plugin install flow in `README.md`.
- Add tests that validate the marketplace entry, plugin manifest, command file,
  and install instructions stay aligned.

## Impact

- A user can install the repo marketplace from the repo root with
  `codex plugin marketplace add .`.
- After Codex reloads the marketplace/plugin, `/wiki:status` is the documented
  command.
- This does not add new wiki query, scorecard, graph, or change queue behavior.
