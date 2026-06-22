# Mirror account-skills without plugin mode

## Why

The user wants the local `D:\skills\account-skills` material uploaded into this
repository and explicitly does not want plugin-mode packaging. The source repo
contains plugin marketplace metadata, local IDE/git state, generated graph
output, reusable kits, and ordinary skills. This change mirrors the ordinary
skills/kits content into the repo as draft/reference material without wiring it
into runtime plugin or repo-local skill routing.

## What Changes

- Add `skills-drafts/account-skills/` as a ordinary directory mirror of the
  source account-skills package.
- Exclude plugin and local/generated state: `.claude-plugin/`, `.git/`,
  `.idea/`, and `graphify-out/`.
- Preserve ordinary reusable content such as `skills/`, `account-cr-agent/`,
  `codex-integration-kit/`, `req-agent-kit/`, `tests/`, source OpenSpec docs,
  source AGENTS/PROJECT metadata, `.codex/hooks.json`, and `.githooks`.
- Add a repo-local README that explains the mirror is not a plugin install and
  shows direct skills-directory usage.

## Out of Scope

- Registering mirrored skills in this repository's `AGENTS.md`.
- Installing mirrored skills into `.codex/skills/`.
- Rewriting source `SKILL.md` files semantically.
- Publishing or packaging plugin marketplace metadata.
- Running the source repo's full test suite.
