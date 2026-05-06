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
updated_at: 2026-05-06
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
