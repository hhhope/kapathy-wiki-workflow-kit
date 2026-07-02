# Atlas 学习 / 汇报协作控制器设计

## 路由状态

路由：`$superpowers:brainstorming` -> Superpowers design spec。

本文是 brainstorming 阶段的设计稿，只用于审核 Atlas 的目标、范围和未来变更边界。本文不实现 Atlas，不修改 repo-local skills，也不改变 OpenSpec 生命周期状态。

## 1. 问题

Stripe AI 支付分享稿和 H5 工作暴露了一个反复出现的协作问题。

仓库里已经有不少可用能力：

- `learning-capture`：负责学习材料、证据分层和输出复用。
- `public-report-quality-gate`：负责 reader-facing 报告、H5、分享稿的质量门禁。
- `visual-agent`：负责视觉模式、视觉路由和视觉验证。
- `material-collaboration-defaults`：负责材料默认处理流。
- `wiki-medical-agent`、`req-agent`、`openspec-router`：提供了 controller / router 型 skill 的已有范式。

缺的不是另一个写作方法 worker。缺的是一个面向学习/汇报类多轮协作的状态控制器。

Stripe 这轮失败里，章节标题、小节结构、话术、转场、证据边界和逐节视觉都曾经被确认过，但用户说“继续”“确认”“修复”以后，后续输出仍反复丢掉这些已确认内容。问题不是没有 reference，而是已确认状态没有控制下一步动作。

## 2. 为什么不是 `writing-method-composer`

`writing-method-composer` 仍然有价值，但它解决的是另一个问题。

它回答：

```text
这是什么类型的文章 / 分享 / H5？
主线是什么？
需要哪些 proof modules 和写作方法？
需要多深的证据？
```

Atlas 回答：

```text
哪些内容已经确认？
当前协作处于哪个阶段？
本轮允许做什么？
本轮禁止做什么？
下一步应该路由到哪个 worker skill？
产物能不能说完成，还是已经漂移？
```

因此 Atlas 不应该并入 `writing-method-composer`，`writing-method-composer` 也不应该承担多轮协作状态控制。

## 3. 设计目标

新增一个 repo-local controller skill，名称：

```text
atlas
```

显示名：

```text
Atlas：学习汇报协作图谱
```

一句话定位：

```text
Atlas coordinates stateful learning/report collaborations by preserving confirmed anchors, routing worker skills, and checking final drift before completion.
```

中文解释：

```text
Atlas 管学习/汇报类多轮协作：守住确认锚点，路由学习、报告和视觉 skill，并在完成前检查是否漂移。
```

## 4. 范围

Atlas 只管学习/汇报类协作，尤其是：

- 学习材料会进入报告、H5、分享稿、演讲稿、wiki 输出或其他 reader-facing artifact。
- 报告、H5、PPT、分享稿、演讲稿、视觉包、材料处理发生多轮协作。
- 当前任务已经有确认锚点、用户纠偏、locked 结构、选定输出形态、证据边界或漂移历史。
- 用户在已经确认/纠偏/拒绝过某个产物后要求继续。

Atlas 不管：

- 一次性 shell 命令。
- 普通代码实现，且没有学习/汇报输出状态。
- OpenSpec 生命周期。
- 全 repo 治理。
- 全局 agent 行为。
- 直接写正文、画图、抓材料、发布内容。

## 5. 核心决策

采用 B+C：

```text
B = Continuation State Gate
C = Final Drift Gate
```

Atlas 第一版不做重型状态机，而是采用轻量 phase + 硬继续门 + 硬完成门。

它要解决的真实失败链路是：

```text
已确认锚点存在
  -> 继续时没有 read-back
  -> worker skill 生成了新结构
  -> 产物看起来完成了，但已经偏离确认内容
```

## 6. 架构

Atlas 是 controller，只路由和控状态，不替代 worker。

```text
                    User
                     |
                     v
          +----------------------+
          |        Atlas         |
          | 学习汇报协作图谱       |
          +----------------------+
          | - current phase      |
          | - confirmed anchors  |
          | - allowed actions    |
          | - blocked actions    |
          | - open gaps          |
          | - worker routing     |
          | - final drift gate   |
          +----------+-----------+
                     |
        +------------+------------+
        |            |            |
        v            v            v
+---------------+ +----------------+ +--------------+
| learning-     | | public-report- | | visual-agent |
| capture       | | quality-gate   | |              |
| 学习/证据      | | 汇报/表达       | | 视觉/图示     |
+---------------+ +----------------+ +--------------+
        |            |            |
        +------------+------------+
                     |
                     v
          +----------------------+
          | Reader-facing Output |
          | 分享稿 / H5 / 报告     |
          +----------------------+
                     |
                     v
          +----------------------+
          | Final Drift Gate     |
          | 完成前漂移检查         |
          +----------------------+
```

## 7. 触发模型

Atlas 按场景触发，不按固定短语触发。

两个条件同时满足时触发：

```text
1. 用户表达继续、修复、确认、认可、执行、落地或继续推进。
2. 当前任务是 stateful learning/report collaboration。
```

`stateful learning/report collaboration` 指当前线程至少具备以下之一：

- 已确认标题、章节、小节、话术、转场或视觉设计。
- 已选择输出形态：报告、H5、分享稿、PPT、演讲稿、wiki、Feishu 等。
- 用户拥有的判断或纠偏。
- 证据边界、source role、缺证约束。
- 既有 drift / reanchor 历史。
- 明确的 reader-facing 目标。

当 reader-facing 或交付敏感产物存在确认锚点或漂移历史时，完成前也必须触发 Atlas 的 Final Drift Gate。

## 8. Continuation State Gate

worker skill 继续处理 stateful learning/report 任务前，Atlas 必须输出紧凑状态块。

最小格式：

```text
- `Using atlas`
- `Current Object`
- `Current Phase`
- `Confirmed Anchors`
- `Allowed Actions`
- `Blocked Actions`
- `Open Gaps`
- `Worker Route`
- `Next Output`
```

示例：

```text
- `Using atlas`
- `Current Object`: Stripe AI payment sharing H5
- `Current Phase`: visual_binding
- `Confirmed Anchors`: 第 1-3 章 locked；第 7 章五条战线；每节需要自己的视觉
- `Allowed Actions`: 修复第 7 章视觉映射
- `Blocked Actions`: 改章节名；合并小节；把逐节视觉压成一张总览；改变主线
- `Open Gaps`: 市场/监管时间轴仍需来源复核
- `Worker Route`: public-report-quality-gate -> visual-agent
- `Next Output`: 只输出第 7 章视觉重锚表
```

如果状态块暴露 blocker，Atlas 必须停止，要求补确认或返回最小修复目标。它不能继续进入写稿、H5 实现、视觉生成或 skill 编辑。

## 9. 轻量阶段模型

Atlas 第一版使用小阶段集合：

```text
intent_calibration
structure_lock
evidence_mapping
drafting
visual_binding
implementation
review_or_reanchor
```

这些 phase 不是完整工作流引擎，只是用于判断 allowed / blocked actions 的共享词表。

如果任务无法归入这些阶段，Atlas 使用：

```text
phase: unclear
allowed_actions: clarify or re-anchor only
blocked_actions: produce or edit delivery artifact
```

## 10. Confirmed Anchors

Confirmed anchors 是用户确认过或纠偏过、后续不能静默修改的内容。

锚点类型：

```text
content_anchor       = 主线、论点、判断、用户拥有的结论
structure_anchor     = 章节、小节、顺序、时间分配
voice_anchor         = 话术风格、professional drama、表达颗粒度
evidence_anchor      = source role、证据强度、缺证点、边界
visual_anchor        = 逐节视觉、视觉形式、视觉证明任务
output_shape_anchor  = 报告、H5、分享稿、PPT、wiki、Feishu、markdown
boundary_anchor      = 允许动作、禁止动作、非目标
```

Atlas v1 不需要持久状态数据库。它可以从当前对话和 repo-visible records 中恢复锚点。未来如果 replay 证明聊天恢复不够，再考虑结构化 state file。

## 11. Acceptance Scorecard

Atlas 拥有协作评分卡 registry，但不把 Stripe 事故里的 11 个点固化成永久清单。

Stripe retro 只是第一批 signal，未来还会增长。因此评分卡必须渐进式披露。

```text
Core Gates
  - state inheritance
  - execution boundary
  - final consistency
  - generic vs custom boundary

Reader Artifact Gates
  - mainline clarity
  - section integrity
  - narrative progression
  - professional drama

Evidence Gates
  - evidence duty
  - claim strength
  - method fit

Visual Gates
  - visual proof binding
  - per-section visual integrity

Boundary Gates
  - hard failure
  - user-owned judgment
```

Atlas 只加载相关 gate family。

示例：

```text
simple material cleanup                 -> Core only
complex report                          -> Core + Reader + Evidence
H5/share visual draft                   -> Core + Reader + Visual
source-heavy strategy report            -> Core + Reader + Evidence + Final Drift
learning/report workflow behavior talk  -> Core + Boundary, not Reader
```

## 12. Final Drift Gate

对 stateful learning/report artifact 声称完成前，Atlas 必须执行最终漂移检查。

最小检查项：

```text
- 有没有确认锚点消失？
- 章节/小节数量或名称有没有未经批准改变？
- 话术、转场、证据边界有没有被压缩掉？
- 承重判断是否缺少要求的证据状态？
- 视觉产物是否未经批准把逐节视觉合成一张综合图？
- 输出形态是否从已选择形态变成另一个形态？
- Stripe 定制规则是否被误升格为通用规则？
- 可泛化协作规则是否没有进入候选治理层？
```

失败行为：

```text
不能说 done。
必须报告失败 gate。
返回对应 phase。
命名最小修复目标。
```

## 13. Worker Ownership

Atlas owns：

- stateful learning/report detection；
- phase selection；
- confirmed anchor read-back；
- allowed / blocked action decisions；
- worker routing；
- final drift gate；
- drift 后的 re-anchor decision。

Atlas does not own：

- `learning-capture` 拥有的 source reading / evidence scoring；
- `public-report-quality-gate` 拥有的 reader-facing report quality；
- `visual-agent` 拥有的 visual mode / visual verification；
- `material-collaboration-defaults` 拥有的 material intake defaults；
- repo OpenSpec skills 拥有的 OpenSpec lifecycle；
- 最终文风执行。

## 14. Skill 协作规则

对 stateful learning/report continuation，Atlas 应该是第一个 skill。

worker skill 被 Atlas 路由时必须保留 Atlas 状态：

```text
Atlas -> learning-capture
  learning-capture 处理 source role、learning level、evidence strength、
  output use。它不能扩大 Atlas 的 allowed action。

Atlas -> public-report-quality-gate
  public-report-quality-gate 处理 Article Intent Contract、Reference Output
  Shape、paragraph drift、judgment ownership、publish/review boundary。它不能
  丢 confirmed anchors。

Atlas -> visual-agent
  visual-agent 处理 mode choice、task classification、visual proof binding、
  output verification、visual worker routing。除非 Atlas state 或用户明确允许，
  否则不能把逐节视觉合并成综合图。
```

如果 worker 发现新 blocker，路由回 Atlas：

```text
worker blocker -> Atlas re-anchor -> user confirmation or narrowed next output
```

## 15. 第一轮实现范围

未来实现应新增一个紧凑 repo-local skill：

```text
.codex/skills/atlas/
  SKILL.md
  references/
    continuation-state-gate.md
    scorecard-registry.md
    final-drift-gate.md
    worker-routing.md
    replay-scenarios.md
  evaluation.md
```

OpenSpec 批准后，预期改动：

```text
add .codex/skills/atlas/*

update .codex/skills/learning-capture/SKILL.md
  - 识别 Atlas-routed learning/report collaboration
  - 保留 Atlas allowed/blocked actions
  - 把 evidence blocker 返回给 Atlas

update .codex/skills/public-report-quality-gate/SKILL.md
  - 保留 Atlas confirmed anchors
  - 对 stateful output 暴露 Atlas final drift failure

update .codex/skills/visual-agent/SKILL.md
  - 保留 Atlas visual anchors
  - 未经批准时拒绝 per-section visual compression

optionally update .codex/skills/material-collaboration-defaults/SKILL.md
  - 当 rich material/report continuation 已有 confirmed anchors 或 drift history
    时，路由到 Atlas
```

## 16. 明确不做

第一轮 Atlas change 不做：

- global AGENTS changes；
- full skill governance knowledge base；
- code task state machine；
- OpenSpec lifecycle replacement；
- `writing-method-composer`；
- persistent state database；
- 大范围重写 `learning-capture`、`public-report-quality-gate` 或 `visual-agent`；
- 自动 Feishu sync 或 publish behavior。

## 17. Checker 与 Evaluation 预期

Reference text alone is not enough。未来实现必须有 replay evidence。

最小 evaluation scenarios：

```text
1. User says "continue" after chapters are locked.
   RED: agent drafts or edits without reading anchors.
   GREEN: Atlas emits state block and blocks chapter rename/section merge.

2. User approved per-section visuals.
   RED: H5 implementation compresses sections into one composite visual.
   GREEN: Atlas/visual-agent route fails final drift and returns to
   visual_binding.

3. LinkedIn/JD evidence is incomplete.
   RED: output claims organization capability from weak samples.
   GREEN: Atlas routes to learning-capture evidence blocker or marks
   proof-boundary.

4. User asks for skill behavior changes after a retro.
   RED: agent edits skill directly from conversation.
   GREEN: Atlas marks behavior asset as out of direct scope and requires
   OpenSpec / skill authoring gate.

5. Simple one-off task.
   RED: Atlas over-applies heavy state block to a trivial command.
   GREEN: Atlas does not trigger because there is no stateful collaboration.
```

最小验收标准：

- Atlas has a compact `SKILL.md`。
- Atlas route block includes current object, phase, anchors, allowed actions,
  blocked actions, worker route, and next output。
- Atlas does not duplicate worker skill bodies。
- Worker skills preserve Atlas state when routed by Atlas。
- Final Drift Gate prevents completion claims after anchor loss。
- Evaluation includes RED/GREEN replay from the Stripe H5 failure。

## 18. 迁移路径

采用分阶段迁移：

```text
Stage 0: This design only.
Stage 1: OpenSpec proposal for Atlas.
Stage 2: Add Atlas skill and evaluation with replay.
Stage 3: Minimal worker skill integration.
Stage 4: Use Stripe sharing/H5 as acceptance replay.
Stage 5: Decide whether writing-method-composer is still needed separately.
```

不能仅凭本文进入 Stage 2。

## 19. 自检

- Scope 限定在 learning/report stateful collaboration。
- Atlas 是 controller，不是 worker。
- 设计采用 B+C：Continuation State Gate + Final Drift Gate。
- 触发不依赖固定短语。
- 设计保留 `learning-capture`、`public-report-quality-gate` 和 `visual-agent` 的 ownership。
- 第一轮实现范围明确，不扩成全局治理。
- 未来 runtime behavior claim 必须有 replay evidence。
