# Install OpenSpec Skills User Scope

## Why

Codex displays trusted repo-local skills with the project namespace. In this
repo, `.codex/skills/openspec-explore/SKILL.md` is shown as
`report-wiki-portfolio:openspec-explore`, even when no plugin or marketplace is
registered.

The desired runtime name is the plain OpenSpec skill name, for example
`openspec-explore`.

## What Changes

- Move the OpenSpec skill source files out of repo-local `.codex/skills`.
- Keep installable source copies under
  `plugins/report-wiki-portfolio/skills/openspec-*`.
- Install those OpenSpec skills into `/home/yan/.codex/skills` so Codex exposes
  them as user-scope `openspec-*` skills.
- Update repo guidance to reference `$openspec-*` skills instead of
  `.codex/skills/openspec-*` repo-local paths.

## Capabilities

### New Capabilities

- `repo-skill-namespace-surface`: the repo avoids publishing OpenSpec skills as
  repo-local namespaced skills when plain user-scope names are required.

### Modified Capabilities

- None.

## Impact

- Affects OpenSpec skill source location, repo guidance, tests, and this change
  record.
- Does not change OpenSpec CLI behavior, OpenSpec specs, wiki runtime scripts,
  or plugin marketplace behavior.
