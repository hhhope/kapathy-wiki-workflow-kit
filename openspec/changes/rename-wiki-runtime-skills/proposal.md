# Rename Wiki Runtime Skills

## Why

Codex 0.130.0 does not expose this repository's custom `/wiki:*` slash
commands in the TUI, even after the repo plugin marketplace is registered and
the plugin is installed by default. The runtime surface that is actually visible
today is `skills/list`.

The current repo-local skills are shown as `report-wiki-portfolio:*` in this
trusted project, which makes wiki runtime entrypoints hard to discover and does
not match the intended short `wiki-*` naming style.

## What Changes

- Publish the wiki runtime entrypoints as user-scope Codex skills named
  `wiki-status`, `wiki-manifest`, `wiki-inbox`, `wiki-query`, `wiki-graph`,
  `wiki-scorecard`, `wiki-route`, `wiki-context`, `wiki-apply`, and
  `wiki-queue`.
- Keep repo-local command files as the source command contracts, but document
  the supported invocation surface as `$wiki-*` skills instead of `/wiki:*`
  slash commands.
- Add tests and behavior replay evidence for the skill names and the
  non-promotion boundary.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `wiki-runtime-slash-command-surface`: the discoverable runtime surface is now
  a wiki runtime skill surface.
- `wiki-status-slash-command`: the supported status entrypoint is now
  `$wiki-status`.

## Impact

- Affects wiki runtime skill source files, README, tests, and this OpenSpec
  change record.
- Does not change wiki runtime scripts, graph extraction, score formulas,
  queue semantics, or OpenSpec lifecycle behavior.
