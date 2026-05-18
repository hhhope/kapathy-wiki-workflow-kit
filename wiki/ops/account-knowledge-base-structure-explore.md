---
title: account knowledge base structure explore
type: intake
language: zh-CN
source_path: chat://openspec-explore/account-knowledge-base-structure-2026-05-07
source_type: conversation
audience: self
knowledge_level: working
domain: wiki
layer: ops
ops_area: learning-capture
canonical_object: account-knowledge-base-structure
artifact_type: explore
period: active
confidence: medium
status: active
updated_at: 2026-05-08
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

2026-05-08 继续校准：主题应明确为“构建团队知识库”，重点不是一般 repo
目录说明，而是从 `lore` 到 `team-lore` 到 `wiki` 的过程演变路径；内容插图、
整体分层结构和页面组织方式都要参考飞书 `Account Harness` 总览页。

## 当前关注点

- repo 当前已经有哪些知识层和运行时治理能力
- wiki 现在的目录结构是否能表达“操作范围 / 已有能力 / 未来要做”
- Feishu 参考页能提供什么页面结构或组织方式
- 输出应先是探索草案，还是需要后续 OpenSpec change 承接落盘
- 如何把 `lore -> team-lore -> wiki` 讲成一个团队知识库演变路径
- 插图应该表达层级关系、控制关系，还是生命周期流转
- 2026-05-08 审核稿反馈：飞书审核稿质量不达标，需要引入对外 report
  scorecard/template gate；问题包括未复用参考组的整体结构、行文标准、图示
  要求，未在内容过多时拆分文章，缺少渐进式引导，口语化严重，并把
  `lore -> team-lore -> wiki` 的演变过程误写成静态分工。

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
- 2026-05-08 需要重构上一版 `account-knowledge-base-workbench.md` 的主题：
  从“account 知识库工作台”改为“团队知识库构建路径”，以 `lore / team-lore /
  wiki` 的演化为主线。
- 当前 repo 已有能力包括 material / meeting note / learning capture /
  OpenSpec lifecycle / wiki runtime stack / behavior replay gate。
- `account-knowledge-base-workbench.md` 的飞书审核稿已创建，但用户明确判定
  “写得不好”；它不应继续作为对外 report 的合格样例。

## 已确认边界

- 最终文档落在 `wiki/ops`。
- 需要先形成审核稿供用户 review；同步到飞书不等于发布通过。
- 不升级成 repo 默认导航规则。
- 不修改 `wiki/index.md`。
- 当前仍处于 explore；不直接修改正式正文，先校准 gate 和重写方向。

## 下一步

- 基于飞书参考页的组织方式，写一版 `wiki/ops/account-knowledge-base-workbench.md`。
- 只把该页加入 `wiki/ops/index.md`，不改全局 wiki 入口。
- 保留参考来源和“不升级为默认导航规则”的边界。
- 重新检查 `lore`、`team-lore`、`wiki` 在当前 repo 中分别对应哪些资产、
  边界和演变阶段。
- 输出新的页面结构草案：包含可视化插图方案、分层结构表、生命周期表、
  问题-答案表、阅读地图。
- 2026-05-08 已按该方向重写 `wiki/ops/account-knowledge-base-workbench.md`：
  主题改为“团队知识库构建路径”，内容按飞书参考组的总览、运行态、安装/
  迁移、验证案例、路线图结构组织。
- 2026-05-08 需要新增或选择一个后续 OpenSpec change，处理“对外 report
  gate”：在生成飞书/对外审核稿前，用评分卡和模板检查参考结构匹配、
  分篇策略、渐进式引导、行文标准、图示要求、核心叙事一致性。

## 2026-05-08 再校准：Account Harness Wiki 命题

用户指出本轮不能继续按“已经有五篇稿，继续润色”的方向推进。真正要先定命题：

- 这篇应是 `Account Harness Wiki` 类文章，而不是普通知识库说明稿。
- 一句话定位区域应先用一张图承载 wiki 生命周期。
- 叙事视角应从用户日常行为出发：先抛问题，再给结论，再说结构、流程、未来和思考。
- 每个章节至少要有图或可视化承载，不接受纯文字堆叠。
- 对“分享使用类”文章，验证结果、案例、可观测场景和可量化指标是关键。
- 当前问题不只是写稿质量，而是现有 skill / ADR / gate 仍会在需求不清时把探索滑成执行，导致反复 drift。

本轮 explore 的当前问题：

1. 现有 `public-report-quality-gate` 是否只拦“发布前质量”，但不能帮助前置命题？
2. 现有 ADR / trace 机制是否记录了过程，却没有把“命题未定不得写稿”变成硬边界？
3. 参考文章的结构、图示、问题-结论写法和量化验证如何转化成本地写作前置判定？
4. 是否需要新 change 承接，而不是继续修改当前飞书稿？

## 2026-05-08 再校准：learning-capture 调用链

用户指出前一轮把 `learning-capture`、`weixin-reader`、`weixin-reference-wiki-capture`
说成并列能力仍然不准确。更准确的运行链应是：

- `learning-capture` 先判断输入是否属于学习材料，并识别 source kind。
- 如果 source kind 是文章，且 URL 是 `mp.weixin.qq.com`，再调用 `weixin-reader`
  抓取标题、作者、日期、URL 和正文。
- 抓取后回到 `learning-capture` 的 article / example / repo 模块，继续走
  admission、scorecard、topic anchoring、过程物落地和 promotion gate。
- `weixin-reader` 只是微信正文 I/O adapter，不拥有“学什么、落哪里、是否升级”的判断。
- `weixin-reference-wiki-capture` 与 repo-local `learning-capture` 有主流程重叠；
  它不应长期作为独立主入口。候选方向是降级为兼容说明，或抽象成
  `reference-template-extraction` 一类被 `learning-capture` 调用的模块。

本轮任务边界需要同时处理三类 drift：

1. runtime drift：链接进入后没有稳定走 `learning-capture -> source adapter -> module`
   的顺序。
2. artifact drift：学习过程物、评分、source grounding、topic anchoring 和 gate review
   不总是稳定落到 repo-visible 文档。
3. scope drift：写稿、学习、治理、skill 编辑混在同一条执行链里，导致 active change
   只解决局部问题。

## 2026-05-08 ASCII 流程草案：问题到思考

这张图用于表达 `Account Harness Wiki` 文章的主叙事，不是正式视觉稿。它先固定
文章顺序和每章必须承载的信息，再作为后续生命周期主图、章节图示和飞书审核稿的
输入。

```text
+---------------------------------------------------------------+
|                    Account Harness Wiki                       |
|  我如何把日常行为变成可复用、可验证、可发布的团队知识系统        |
+---------------------------------------------------------------+

        |
        v
+--------------------+
| 1. 问题             |
+--------------------+
| 日常输入很多：       |
| - AI 对话           |
| - 飞书文档          |
| - 会议纪要          |
| - 外部链接          |
| - 项目经验          |
|                    |
| 如果没有治理：       |
| - 写完就散          |
| - 学了不沉淀        |
| - 沉淀不可复用      |
| - 对外稿反复漂移    |
+--------------------+
        |
        v
+--------------------+
| 2. 结论             |
+--------------------+
| 不是先写稿，         |
| 也不是先加 skill。   |
|                    |
| 先判断输入属于：     |
| - 学习              |
| - 写稿              |
| - 治理变更          |
| - 一次性查询        |
|                    |
| 再进入对应 gate。    |
+--------------------+
        |
        v
+--------------------+
| 3. 结构             |
+--------------------+
| 输入层              |
|   links / docs /    |
|   meetings / chat   |
|        |            |
| 路由层              |
|   learning-capture  |
|   proposition-gate  |
|   OpenSpec          |
|        |            |
| 资产层              |
|   wiki/sources      |
|   wiki/ops          |
|   wiki/examples     |
|   ADR / spec / skill|
|        |            |
| 发布层              |
|   Feishu / H5 /     |
|   public report     |
+--------------------+
        |
        v
+--------------------+
| 4. 流程             |
+--------------------+
| 输入                |
|  |                 |
|  +-- 学习材料        |
|  |     -> score     |
|  |     -> grounding |
|  |     -> wiki note |
|  |                 |
|  +-- 对外稿          |
|  |     -> 命题卡     |
|  |     -> 主图       |
|  |     -> 证据表     |
|  |     -> 审核稿     |
|  |                 |
|  +-- 治理变更        |
|        -> OpenSpec  |
|        -> eval      |
|        -> archive   |
+--------------------+
        |
        v
+--------------------+
| 5. 可观测案例        |
+--------------------+
| 观察指标：           |
| - 链接触发是否走路由 |
| - 微信文章是否先读取 |
| - 75 分以下是否跳过 |
| - 过程物是否落 wiki |
| - 命题未过是否停写稿 |
| - 飞书同步前是否过 gate |
| - 失败稿是否被冻结   |
+--------------------+
        |
        v
+--------------------+
| 6. 未来 / 思考       |
+--------------------+
| 当前先做到：         |
| - 人可审            |
| - 过程可追          |
| - 证据可查          |
| - 失败可复盘        |
|                    |
| 未来再考虑：         |
| - 自动路由          |
| - 自动回放          |
| - 自动发布前检查    |
| - 跨项目 team-lore  |
+--------------------+
```
