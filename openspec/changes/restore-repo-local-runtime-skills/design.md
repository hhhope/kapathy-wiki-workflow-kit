# Design: Repo-Local Runtime Skills

## Decision

Use `.codex/skills` as the repository-owned runtime skill surface for this
project.

## Rationale

The previous design optimized for plain user-scope skill names, but it depended
on two assumptions that do not hold reliably here:

- Codex plugin marketplace support is not available as an active runtime
  mechanism.
- User/root skill installs are local machine state and can drift independently
  of the repository.

This repository already owns workflow-specific skills under `.codex/skills`.
Restoring OpenSpec and wiki runtime entrypoints there makes the repo checkout
self-contained. The tradeoff is that Codex may display repo skills with the
`report-wiki-portfolio:` prefix in some surfaces. That prefix is acceptable for
repo-owned behavior because availability and source-of-truth stability are more
important than a plain global name.

## Skill Ownership

| Skill family | Runtime location | Ownership |
|---|---|---|
| Report/wiki workflow skills | `.codex/skills/*` | repo-owned |
| Wiki runtime skills | `.codex/skills/wiki-*` | repo-owned |
| OpenSpec helper skills used by this repo | `.codex/skills/openspec-*` | repo-owned runtime copy |
| Generic cross-repo skills | `/home/yan/.codex/skills/*` | root/user scope, optional |

## Compatibility

Existing files under `plugins/report-wiki-portfolio/` may remain as source or
legacy command contracts, but README and repo guidance must not require plugin
installation or user-scope copying for the supported runtime path.

## Verification

- Tests fail before `.codex/skills/openspec-*` and `.codex/skills/wiki-*` are
  restored.
- Tests pass after repo-local skill files exist and README/AGENTS point to them.
- OpenSpec validation passes for this change.
