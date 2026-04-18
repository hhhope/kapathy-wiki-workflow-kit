## Why

The user has a working external Weixin article reader skill under `~/.claude/skills/weixin-reader`, but it is not available to this repo's local Codex skill system. The skill is useful for reading mp.weixin.qq.com articles, but it still assumes an external path and uses a non-Codex trigger description style.

To use it reliably in this repo, it needs to be localized rather than referenced externally.

## What Changes

- Migrate the external `weixin-reader` skill into this repo's local `.codex/skills/`.
- Adapt the skill description and command references for local Codex usage.
- Bring over the helper script needed by the skill.

## Capabilities

### New Capabilities

- `weixin-reader`: The repo gains a local skill for fetching and reading Weixin public-account articles.

### Modified Capabilities

None.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/migrate-weixin-reader-skill/`.
- Adds `.codex/skills/weixin-reader/SKILL.md`.
- Adds `.codex/skills/weixin-reader/scripts/fetch_weixin.py`.
