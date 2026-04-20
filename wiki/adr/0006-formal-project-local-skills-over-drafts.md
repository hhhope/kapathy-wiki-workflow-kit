# ADR-0006 Formal Project-Local Skills Over Draft Skill Docs

- Status: accepted
- Date: 2026-04-16

## Context

这个仓库同时存在两种 skill-like 内容：

- `.codex/skills/` 下的正式项目级 skill
- `skills-drafts/` 下的草稿型流程文档

在 meeting-note 流程里，仓库一度把 `skills-drafts/meeting-note-output/` 当成可执行发布面，结果导致流程“看起来写了”，但新会话并不能把它当作正式 skill 使用。

同时，环境里还存在 `~/.codex/agents/*.md` 这种手工角色模板。它们适合显式 planner/reviewer 角色，但不是 repo 默认 workflow 的发布机制。

## Decision

本仓库后续采用下面的固定边界：

- 项目级正式 skill 只从 `.codex/skills/` 发布
- `skills-drafts/` 只作为草稿、探索或预发布内容，不算已上线能力
- 手工 agent 角色模板只作为显式角色资产，不替代 repo workflow skill routing

## Consequences

- 如果某个流程希望 future session 能稳定命中，就必须落到 `.codex/skills/`
- 只修改 `skills-drafts/` 不能宣称“仓库已经有这个 skill”
- workflow-level 变更需要同时检查：正式 skill 路径、repo guidance、discoverability 验收
