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
- Feishu 参考页可能需要登录权限；如果读取失败，本轮只能标注访问边界。

## 已确认事实

- `PROJECT.md` 定义本仓库为 durable markdown knowledge base，核心目标是把
  Feishu、会议纪要和周期汇报材料转成可复用 wiki。
- 当前 wiki 主入口已经按 `Sources / Domains / Timeline / Reports / Ops`
  组织。
- `wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md` 已记录该飞书
  wiki URL，但正文仍是 placeholder。
- 本轮 lark-cli 读取该飞书 wiki 失败，错误为 `need_user_authorization`；
  因此不能声称已读取参考页正文或层级结构。
- 当前 repo 已有能力包括 material / meeting note / learning capture /
  OpenSpec lifecycle / wiki runtime stack / behavior replay gate。

## 暂未决定

- 最终文档落在 `wiki/ops`、`wiki/index.md`、还是新的 account 知识库入口页
- 是否要同步到飞书 wiki
- 是否需要把结构页升级成 repo 默认导航规则

## 下一步

- 读取本 repo 的 PROJECT、wiki index、ADR、spec、skills 和当前目录结构。
- 尝试读取 Feishu 参考页结构。
- 输出一版“account 知识库结构文档”草案，并明确哪些内容来自 repo 证据、
  哪些来自 Feishu 参考、哪些仍是待验证假设。
