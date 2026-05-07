---
title: account knowledge base structure explore
type: intake
language: zh-CN
source_path: chat://openspec-explore/account-knowledge-base-structure-2026-05-07
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: medium
status: active
updated_at: 2026-05-07
ai_generated: true
related_sources:
  - https://my.feishu.cn/wiki/FYDcwFGaOi6A1Bkg9rfcIp3DnCS
related_focus_threads:
  - main-thread.md
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# account knowledge base structure explore

## 触发问题

用户希望回看整个 repo project、wiki 结构、操作范围、已有能力和未来要做的事，
并结合一个飞书 wiki 参考页，整理出 account 知识库的类似结构文档。

## 当前关注点

- repo 当前已经有哪些知识层和运行时治理能力
- wiki 现在的目录结构是否能表达“操作范围 / 已有能力 / 未来要做”
- Feishu 参考页能提供什么页面结构或组织方式
- 输出应先是探索草案，还是需要后续 OpenSpec change 承接落盘

## 当前假设

- 这不是单纯整理目录，而是在给 account 知识库设计可读、可维护、可执行的
  结构页。
- 如果要修改 repo 默认结构、wiki 导航或发布新正式页面，应通过 OpenSpec
  change 承接。
- Feishu 参考页需要登录权限；授权成功后才能把页面结构作为参考证据。

## 已确认事实

- `PROJECT.md` 定义本仓库为 durable markdown knowledge base，核心目标是把
  Feishu、会议纪要和周期汇报材料转成可复用 wiki。
- 当前 wiki 主入口已经按 `Sources / Domains / Timeline / Reports / Ops`
  组织。
- `wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md` 已记录该飞书
  wiki URL，并在 2026-05-07 授权后补充了结构摘要。
- 首次读取该飞书 wiki 失败，错误为 `need_user_authorization`；随后通过
  `lark-cli auth login --domain docs,wiki` 授权成功，并读取到参考页标题和
  markdown 结构。
- 参考页结构包括入口说明、一句话定位、适合谁看、层级表、当前阶段、默认
  生命周期、整体约束、解决问题、分工、默认使用顺序、阅读地图。
- 当前 repo 已有能力包括 material / meeting note / learning capture /
  OpenSpec lifecycle / wiki runtime stack / behavior replay gate。

## 已确认边界

- 最终文档落在 `wiki/ops`。
- 不同步到飞书 wiki。
- 不升级成 repo 默认导航规则。
- 不修改 `wiki/index.md`。

## 下一步

- 基于飞书参考页的组织方式，写一版 `wiki/ops/account-knowledge-base-workbench.md`。
- 只把该页加入 `wiki/ops/index.md`，不改全局 wiki 入口。
- 保留参考来源和“不升级为默认导航规则”的边界。
