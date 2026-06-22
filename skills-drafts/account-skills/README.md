# Account Skills Mirror

This directory is a non-plugin mirror of `D:\skills\account-skills`.

It is kept here as draft/reference material for review, reuse, and later
promotion. It is not installed as a Codex plugin, is not registered in this
repo's `AGENTS.md`, and is not automatically loaded by the runtime.

## Source

- Source path: `D:\skills\account-skills`
- WSL path used for this mirror: `/mnt/d/skills/account-skills`
- Mirror target: `skills-drafts/account-skills/`

## Included

- `skills/`: standalone skill folders from the source library.
- `account-cr-agent/`: CR Agent skill package content, without plugin metadata.
- `codex-integration-kit/`: reusable governance rules, templates, docs, scripts,
  and supporting skills.
- `req-agent-kit/`: requirement workflow kit and installer source material.
- `openspec/`: source change/spec history preserved as reference material.
- `tests/`: source tests preserved for future promotion or validation work.
- `.codex/hooks.json` and `.githooks/`: source hook/config material preserved as
  reference, not enabled by this mirror.

## Excluded

The mirror intentionally excludes plugin, generated, and local-state content:

- `.claude-plugin/`
- `.codex-plugin/`
- `.git/`
- `.idea/`
- `graphify-out/`
- Python `__pycache__/`

## Direct Use

Use this mirror by reading or copying individual folders deliberately. For
example:

- inspect `skills/<skill-name>/SKILL.md` when evaluating a source skill;
- copy a selected skill into a runtime skill directory only through a separate
  promotion/evaluation change;
- reuse documents under `codex-integration-kit/` or `req-agent-kit/` as source
  material after checking their local assumptions.

Do not treat this mirror as an active skill install. Individual skills remain
draft/reference assets until they are separately reviewed, adapted if needed,
validated, and wired into local governance.

Some preserved source documents may mention the original package's historical
plugin workflow. Those documents are kept as source history only; they are not
the usage path for this mirror.

## Promotion Boundary

Promoting any mirrored skill into active repo behavior requires a separate
OpenSpec change and the repo skill evaluation gate. That follow-up should decide
whether the target skill is mirrored, adapted, wrapped, or rejected, and should
verify dependencies before adding runtime routing.
