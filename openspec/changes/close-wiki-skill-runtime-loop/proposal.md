# Proposal

## Why

The active wiki runtime surface is split between repo-local skills and slash
command contract files. The current runtime should be closed around
`.codex/skills/wiki-*` so future agents can execute wiki workflows without
following stale `/wiki:*` command documents.

## What Changes

- Make repo-local `.codex/skills/wiki-*` files self-contained runtime contracts.
- Remove active slash command contract files under `commands/` and
  `plugins/report-wiki-portfolio/commands/`.
- Update README, active specs, and tests so the current runtime truth is the
  repo-local skill surface.
- Preserve generated status artifacts and archived historical OpenSpec records.

## Out of Scope

- Restoring plugin runtime.
- Defining a general agent runtime framework.
- Migrating historical frontmatter backlog.
- Editing archived OpenSpec history unless a current test imports it.
