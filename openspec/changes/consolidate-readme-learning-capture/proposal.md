# Change: consolidate README learning capture

## Why

`readme-learning-capture` and `learning-capture` now overlap as runtime entry
points. `learning-capture` already owns external-source learning routing and has
a repo/README module, while `readme-learning-capture` says it is a compatibility
entry point. Keeping both active surfaces makes future agents choose between two
names for the same user intent.

## What Changes

- Retire the active `.codex/skills/readme-learning-capture/` skill surface.
- Move the repo/README scorecard and pressure scenarios under
  `.codex/skills/learning-capture/references/`.
- Make `learning-capture/references/repo-readme.md` self-contained instead of
  delegating back to the retired skill.
- Remove active manifests and tests that require the retired skill surface.

## Impact

- Repo/README learning still exists.
- The single runtime entry is `learning-capture`.
- Historical wiki notes can keep references to the old name as history, but
  active skills, tests, and seed manifests should not expose it.
