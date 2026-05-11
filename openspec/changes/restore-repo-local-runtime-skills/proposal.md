# Restore Repo-Local Runtime Skills

## Why

Codex in this repository cannot rely on plugin marketplace loading for the
runtime workflow surface. The previous user-scope install strategy also leaves
runtime skills as machine-local state under `/home/yan/.codex/skills`, which can
drift from the repository and already lost `openspec-explore` locally.

The repo needs a self-contained skill surface that is present whenever the repo
is checked out and trusted, even if plugin support is absent and user/root skill
state is stale.

## What Changes

- Restore OpenSpec helper skills under `.codex/skills/openspec-*`.
- Publish wiki runtime skills under `.codex/skills/wiki-*`.
- Treat plugin command and `plugins/report-wiki-portfolio/skills/*` files as
  legacy/source compatibility, not the required runtime surface.
- Update README, AGENTS guidance, specs, and tests to make `.codex/skills` the
  repo-owned runtime skill source.
- Record evaluation evidence for the skill routing reversal.

## Capabilities

### Modified Capabilities

- `repo-skill-namespace-surface`: OpenSpec helpers are repo-local runtime skills
  instead of user-scope installs.
- `wiki-runtime-slash-command-surface`: wiki runtime skills are repo-local
  skills instead of installable user-scope skills.
- `wiki-status-slash-command`: wiki status is exposed through the repo-local
  `.codex/skills/wiki-status` skill.

## Impact

- Affects repo-local Codex skills, README, AGENTS routing, tests, and OpenSpec
  specs.
- Does not change wiki runtime scripts, graph/score/routing semantics, or the
  OpenSpec CLI.
- Keeps existing plugin files unless a later cleanup change retires them.
