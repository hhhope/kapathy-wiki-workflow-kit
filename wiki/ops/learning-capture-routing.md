---
canonical_object: learning-capture-routing
artifact_type: intake
title: learning-capture-routing / intake
type: intake
language: zh-CN
source_path: chat://openspec-explore/learning-capture-routing/2026-05-06
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: medium
status: active
updated_at: 2026-05-07
ai_generated: true
trace_mode: openspec-explore
same_topic_rule: update-existing
related_objects:
  - example-driven-capture
  - article-learning-capture
  - readme-learning
derived_from:
  - https://github.com/larksuite/cli
  - https://github.com/larksuite/cli/blob/main/skills/lark-base/SKILL.md
---

# learning-capture-routing / intake

## 触发问题

用户追问 `article-learning-capture` 和 `readme-learning-capture` 的本质区别后，
进一步提出：是否可以参考 `larksuite/cli` 的方式，把“学习”这件事先定义清楚，
再按材料类型分模块，而不是让每个材料类型各自长成一个独立治理入口。

## 当前关注点

- 当前缺口不是没有 article 或 README 学习流程，而是缺一个更早的意图判断：
  这次请求到底是不是学习。
- `larksuite/cli` 的可复用点是 `domain skill + module references` 的组织方式，
  不是某个具体命令或某个具体 Lark domain。
- 学习入口应该先判断用户想学什么，再判断证据对象是什么。

## 当前判断

采用渐进式方案：

- 新增薄的 `learning-capture` domain skill。
- 保留 `article-learning-capture` 和 `readme-learning-capture` 作为兼容入口。
- 把 article、repo/README、example/reference 分成模块。
- 不删除旧 skill，不重写历史 wiki，不新增自动抓取或调度代码。

## 约束

- 这是学习路由，不是把所有外部链接都落 wiki。
- 文章学习仍需要原文保全、source class、score-first 和版权边界。
- README/repo 学习仍需要 reused / modified / rejected / repo target。
- 示例学习只能教结构或输出形态，不能单独证明技术事实。
- 外部来源的学习不能直接升级为 `AGENTS.md`、spec 或 hard skill rule。

## 下一步

执行 OpenSpec change `consolidate-learning-capture-routing`，把 domain-router
结构落到 repo-local skill，并在 evaluation 中记录 RED/GREEN 与 trigger
pressure scenarios。

## Runtime trigger 复盘入口（2026-05-07）

## 触发问题

在 `govern-repo-agents-loaded-context` 压缩 repo `AGENTS.md` 后，用户追问：
为什么 `learning-capture-routing` 没有出现在 `High-Frequency Skills`，而只
出现在 `Output Routing`。这暴露出一个分层问题：同一个学习治理对象同时有
规范层、解释层、运行时入口层和输出落点层，压缩时容易只保留 source-of-record，
漏掉 runtime trigger。

## 当前关注点

- 基于整个 wiki 仓库判断：`runtime trigger` 不是新规则，而是 repo 入口文件中
  对行为资产的加载条件。
- `learning-capture-routing` 作为 spec/wiki source，说明学习路由的能力边界。
- `.codex/skills/learning-capture/SKILL.md` 作为 runtime entry，决定当前请求是否
  进入学习路由。
- `Output Routing` 只回答学习结果落到哪里，不能替代 skill 加载入口。

## 当前假设

repo `AGENTS.md` 需要区分三类路由：

- behavior trigger：当前输入来了要不要加载某个 skill。
- asset governance：某个 skill / spec / wiki page 如何被维护和升级。
- output destination：产物应该进入 `wiki/sources`、`wiki/ops`、`wiki/examples`、
  `wiki/adr`、OpenSpec，还是目标 repo 的公开 docs。

如果三类路由压成一个表，agent 会误以为“有 source 链接”就等于“运行时会加载”。

## 开放问题

- repo `AGENTS.md` 的 `High-Frequency Skills` 是否应该只列高频 runtime trigger，
  还是列所有 published repo skill。
- `learning-capture` 这种 domain-router skill 是否属于 high-frequency，还是应该
  有独立的 `Runtime Trigger Map`。
- archive review 的 replay matrix 是否需要把“source exists”与“trigger exists”
  分开计分。

## 下一步

先基于 wiki / spec / skill 资产聊清楚分层，再决定是否通过当前 OpenSpec change
补一行 runtime trigger 或调整 archive-review 结论。
