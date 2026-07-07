---
title: CR Agent Issues Explore
type: intake
language: zh-CN
source_path: chat://openspec-explore/cr-agent-issues-2026-07-07
source_type: conversation
audience: self
knowledge_level: working
domain: agent-harness
layer: ops
ops_area: workflow-trace
canonical_object: cr-agent-issues-explore
artifact_type: trace
period: active
confidence: medium
status: active
updated_at: 2026-07-07
ai_generated: true
related_sources:
  - skills-drafts/account-skills/account-cr-agent/
related_focus_threads: []
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# CR Agent Issues Explore

## 触发问题

用户触发 `$report-wiki-portfolio:openspec-explore`，要求看一下 `cr-agent` 还有哪些问题。

## 当前关注点

- `cr-agent` 当前草稿/镜像资产是否存在入口、路由、评审输出或 replay 证据缺口。
- 已有 OpenSpec / wiki 学习记录中是否保留了未关闭问题。
- 本轮仅探索，不实现、不修复、不改写技能行为。

## 当前假设

- `cr-agent` 可能同时存在于当前 repo 的 `skills-drafts/account-skills/`、用户级/插件级技能镜像和历史 OpenSpec 记录中，需要区分来源。
- 真正的问题应优先来自文件证据、测试/eval 证据或已有治理记录，而不是从名字语义猜测。

## 暂未决定

- 这次发现是否需要转成新的 OpenSpec change。
- 若存在多个来源的 `cr-agent`，哪个是当前应治理的目标面。

## 下一步

- 只读检查 `cr-agent` 相关技能、README、replay/eval、OpenSpec 记录和 wiki 学习页。
- 输出问题清单、证据路径和建议的后续治理边界。

## 本轮已确认

- 安装版 `cr-agent` 已有 coverage gate、4 个 replay fixtures 和 21 个单测；repo 镜像草稿只保留了简化入口、1 个 fixture 和基础 replay 校验脚本。
- `release-diff-cr` 仍要求 Markdown CR 报告包含 frontmatter，并且脚本会输出 Obsidian TODO callout；这与 `cr-report` 的 plain report 禁止规则冲突。
- `open-code-review` 学习记录仍停留在 candidate learning，没有被正式转成 `cr-agent` executor 或 OpenSpec change。
