---
title: superpowers-brainstorming-skill-visibility / explore
type: explore
canonical_object: superpowers-brainstorming-skill-visibility
artifact_type: explore
language: zh-CN
audience: self
domain: personal-ops
status: active
updated_at: 2026-05-14
ai_generated: true
trace_mode: openspec-explore
notes_scope: 调查为什么本地 Superpowers 缓存中存在 brainstorming skill，但当前会话未暴露 Superpowers:brainstorming
---

# superpowers-brainstorming-skill-visibility / explore

## Trigger

用户指出本地路径
`/home/yan/.codex/plugins/cache/openai-curated/superpowers/08373044/skills`
中存在 Superpowers skill，因此质疑当前会话为什么报告没有
`Superpowers:brainstorming`。

## Current Question

- 本地缓存中是否确实存在 `brainstorming` skill？
- 当前会话可见 skill 列表为什么没有暴露 `Superpowers:brainstorming`？
- 是插件缓存、skill registry、命名映射，还是会话注入来源不一致？

## Boundary

本次只做探索和证据定位，不改插件、不安装 skill、不修改 repo runtime。

## Findings

### 1. Local cache does contain brainstorming

Confirmed path:

`/home/yan/.codex/plugins/cache/openai-curated/superpowers/08373044/skills/brainstorming/SKILL.md`

The skill frontmatter is valid:

- `name: brainstorming`
- description requires use before creative work, feature creation, functionality
  changes, or behavior modification.

The plugin manifest is also valid:

- plugin name: `superpowers`
- version: `5.1.0`
- skills path: `./skills/`
- keywords include `brainstorming`

### 2. Codex config enables the plugin

`/home/yan/.codex/config.toml` contains:

```toml
[plugins."superpowers@openai-curated"]
enabled = true
```

So the issue is not a missing local cache and not an obviously disabled plugin.

### 3. Current account-meeting-lore session did not inject that skill root

The current session-visible skill roots only included:

- repo-local `.codex/skills`
- `/home/yan/.codex/skills`
- `/home/yan/.agents/skills`
- `/home/yan/.codex/skills/.system`

It did not include:

`/home/yan/.codex/plugins/cache/openai-curated/superpowers/08373044/skills`

That is why `Superpowers:brainstorming` was not in the visible skill list even
though the file exists on disk.

### 4. Other sessions can inject a Superpowers cache root

A separate session under `/mnt/d/cloud/team-knowledge` showed a plugin skill
root like:

`/home/yan/.codex/plugins/cache/openai-curated/superpowers/7955f1db/skills`

This suggests the mechanism can work, but this account-meeting-lore session did
not receive the openai-curated Superpowers skill root.

Later evidence from newer `/mnt/d/cloud/team-knowledge` sessions showed the
current cache root exactly:

`/home/yan/.codex/plugins/cache/openai-curated/superpowers/08373044/skills`

Those sessions include `r4` in `### Skill roots`; the current
account-meeting-lore worker session does not.

## Current Interpretation

The failure mode is a stale or incomplete session skill-index /
plugin-injection mismatch:

- plugin installed: yes
- plugin enabled in config: yes
- `brainstorming` skill present in cache: yes
- current session skill registry exposed `Superpowers:brainstorming`: no

The earlier answer that "there is no `Superpowers:brainstorming` skill file" was
wrong because it checked the gstack skill directory, not the Codex plugin cache.

The most likely root cause is session immutability: skill roots are injected
when the Codex session or worker thread starts, and this existing
account-meeting-lore worker did not get the plugin cache root. Newer sessions
can get it, so reinstall is not the first remedy.

## Practical Consequence

When this happens, the agent should not conclude the skill does not exist. It
should say the skill exists on disk but is not injected into the current
session-visible registry, then either:

- read the plugin cache skill manually as evidence, or
- restart/open a new Codex session after plugin cache refresh, so the skill root
  is injected.

No reinstall is required unless a fresh session still lacks the plugin cache
root after confirming `[plugins."superpowers@openai-curated"] enabled = true`.
