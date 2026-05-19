---
layer: ops
domain: none
ops_area: learning-capture
canonical_object: learning-capture-routing
artifact_type: intake
ai_generated: true
audience: self
confidence: medium
derived_from:
  - https://github.com/larksuite/cli
  - https://github.com/larksuite/cli/blob/main/skills/lark-base/SKILL.md
knowledge_level: working
language: zh-CN
period: active
related_objects:
  - example-driven-capture
  - readme-learning
same_topic_rule: update-existing
source_path: "chat://openspec-explore/learning-capture-routing/2026-05-06"
source_type: conversation
status: active
title: learning-capture-routing / intake
trace_mode: openspec-explore
type: intake
updated_at: 2026-05-07
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
- article 学习从独立 runtime skill 退为 `learning-capture` 内部 reference
  module；`readme-learning-capture` 仍是相邻兼容入口。
- 把 article、repo/README、example/reference 分成模块。
- 不重写历史学习页，不新增自动抓取或调度代码。

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

## larksuite/cli 二次学习结论（2026-05-07）

## 来源

- `larksuite/cli` repo README：<https://github.com/larksuite/cli>
- `lark-base` skill：<https://github.com/larksuite/cli/blob/main/skills/lark-base/SKILL.md>
- 本仓库上一轮学习复盘：`wiki/ops/gstack-lark-learning-retro-2026-04-18.md`

## 学到了什么

`larksuite/cli` 对本仓库最有价值的不是“skill 越多越好”，而是它把 agent
入口拆成了可执行的几层：

- repo README 负责说明整体能力面、agent-native 定位、安装 / auth / command 体系。
- domain skill 负责说明“什么时候用 / 什么时候不用”。
- domain skill 内部再用 module map 把用户意图分流到具体模块和 reference。
- reference 文档承接重细节，避免主 skill 变成长手册。
- 高风险动作通过前置约束和禁止行为保留在运行时入口附近。

这说明本仓库不应该把所有 learning 规则塞进 `AGENTS.md`，也不应该只把
`learning-capture-routing` 放在 source list 里。更稳的做法是：

- `AGENTS.md` 只保留 runtime trigger：外部来源作为学习 / reference /
  adaptation material 时加载 `learning-capture`。
- `.codex/skills/learning-capture/SKILL.md` 负责判断是不是学习，并按 evidence
  object 分到 article / repo-readme / example 模块。
- `references/*` 承接细节流程、scorecard、模板和压力场景。
- `Output Routing` 只负责学习结果落到哪里。

## 是否复杂了

表面上多了一层，但实际是降复杂度。

如果没有 runtime trigger，agent 看到外部链接时只能在 `Output Routing` 和 spec
source 里猜：到底要不要学、要不要落 wiki、要不要加载 skill。这样会把运行时判断
变成隐式推理，反而更复杂。

如果补上 runtime trigger，复杂度被拆开：

- 入口判断：要不要加载 `learning-capture`。
- 领域判断：是不是学习，属于哪种 evidence object。
- 输出判断：产物落到 `wiki/sources`、`wiki/ops`、`wiki/examples`、`wiki/adr`、
  OpenSpec，还是目标 repo docs。
- 晋升判断：有没有证据升级成 `AGENTS.md`、spec 或 skill hard rule。

## 复用什么

- 复用 `larksuite/cli` 的 domain skill + module references 结构。
- 复用“何时用 / 何时不用”的 runtime trigger 写法。
- 复用“重细节进 references”的低 token 主体模式。

## 修改什么

- 不照搬它的 command/domain 组织法，因为本仓库不是 CLI 命令库。
- 不把 `learning-capture` 做成所有链接的默认入口；仍然保留 non-learning 拒绝场景。
- 不把这次学习直接升级成新的 spec SHALL；先作为当前 `govern-repo-agents-loaded-context`
  的结构修正依据。

## 拒绝什么

- 拒绝把 `High-Frequency Skills` 变成所有 skill 的清单。
- 拒绝把 `Output Routing` 当成 runtime trigger。
- 拒绝用 source-of-record 链接替代 agent 运行时加载条件。

## repo target

- 当前落点：本页 `learning-capture-routing / intake`。
- 可执行后续：在 `govern-repo-agents-loaded-context` 中补 `learning-capture`
  runtime trigger，并修正 archive review 的 learning replay 结论。
- 不直接改：root `~/.codex/AGENTS.md`、`CLAUDE.md`、learning skill 本体。

## Runtime / Review 分层定稿（2026-05-07）

本轮通过 OpenSpec change `harden-learning-capture-runtime` 把学习入口拆成运行时
轻门禁和周期性重整理。

## 优先级

| 优先级 | 问题 | 归属 |
|---|---|---|
| P0 | 这个输入现在要不要启动学习？ | `learning-capture` runtime trigger |
| P0 | 是否值得精读？ | admission + scorecard，75 分门槛 |
| P0 | 是否升级成 `AGENTS.md` / spec / skill？ | promotion gate / OpenSpec |
| P1 | 它是文章、repo、example 还是混合？ | learning module routing |
| P1 | 如果主题不明确怎么办？ | candidate，等 weekly review |
| P1 | 应该挂到哪个已有专题？ | topic anchoring |
| P2 | 学完产物落哪里？ | Output Routing |
| P2 | 跨来源概念、链接、整理谁做？ | weekly review / compile |

## 当前落地原则

- Runtime 只做轻判断：intent、source kind、topic anchor、admission、score、
  candidate / skip / deep-read 决策。
- Article 和 repo/README 都使用 75 分 deep-read 门槛；60-74 只留 brief
  candidate，低于 60 只留 skip reason。
- 用户明确主题时，先查已有 wiki topic；例如 agent / harness / eval 文章应优先
  检查 `agent-harness-article-learning` 相关页面。
- 用户没有明确主题且只能弱语义猜测时，不强挂已有专题，留给 weekly review。
- Weekly review 是 health-check / self-check 出口，不是每次输入都跑的编译器。
- Output Routing 只负责产物落点，不能替代 runtime trigger。

## 目录映射

- `wiki/sources`：raw source layer。
- `wiki/ops/*-intake.md`：brainstorming / capture layer。
- `wiki/ops/*-learning.md` 或专题学习页：compiled learning notes。
- `wiki/ops/*-retro.md`：process health / drift review。
- `wiki/examples`：reusable output-shape examples。
- `wiki/adr`：stable decisions。
- OpenSpec：scoped behavior changes。

## 不做

- 不迁移 wiki 目录结构。
- 不实现 weekly-review 自动化。
- 不把外部来源学习直接升级为 behavior asset。

## Link Trigger Replay 治理锚点（2026-05-07）

本轮用户要求把“下次我给链接你会怎么做”的回放作为 skill / agent 治理策略
之一。这个锚点的作用不是新增一种学习流程，而是把已经存在的 runtime trigger
变成可复盘、可引用、可验证的行为矩阵。

## replay matrix

| 输入形态 | runtime route | 输出边界 |
|---|---|---|
| 学习 / 治理线程里的裸文章链接 | `learning-capture` -> article module -> admission -> score | 只有分数和 topic anchor 支持时才落 durable wiki |
| 学习 / 治理线程里的微信链接 | `weixin-reader` -> article module -> admission -> score | 必须先有 source grounding，不把全文搬进 wiki |
| 带学习 / 复用 / 改造意图的 GitHub/README 链接 | repo/README module -> admission -> score | 只有通过阈值才精读并写 durable notes |
| raw fetch / news / fact lookup / short abstract | 不走 learning-capture | 不默认落 wiki |
| 没有学习上下文的裸链接 | clarify 或 ordinary lookup/fetch | 不强行建 durable topic |

## governance boundary

- replay 是 runtime strategy，不是把所有链接都写 wiki。
- wiki capture 是最低正确落点，不是 promotion。
- 文章 takeaway 要进入 `AGENTS.md`、spec `SHALL`、skill hard rule 或 archive-ready
  claim，必须另过 evidence-backed promotion gate 或 scoped OpenSpec change。
- 这次锚点由 OpenSpec change `codify-link-learning-trigger-replay` 负责验证和收口。
