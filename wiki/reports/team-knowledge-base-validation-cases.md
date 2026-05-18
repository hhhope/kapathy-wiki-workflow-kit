---
layer: reports
domain: wiki
---

<callout emoji="chart_with_upwards_trend" background-color="light-blue">
本页解释 Account Wiki 怎么证明自己有用：用真实 case、分数变化、门禁结果、Feishu 回读日志和 RED/GREEN 回放，而不是只说“有流程”。
</callout>

配图资产：`wiki/reports/assets/account-wiki-validation-card.png`

## 一句话定位

验证与案例页要回答两个问题：第一，这套 Wiki runtime 有没有在真实任务里拦住错误；第二，拦住之后有没有留下下一次可以复用的证据。

## 这页适合谁看

| 如果你要判断 | 先看这里的什么 | 看完能得到什么 |
|---|---|---|
| 这套 Wiki runtime 是否只是概念 | Case 总表 | 看到哪些任务被验证、失败、冻结或修复 |
| 为什么失败稿不能继续润色 | Case 1 | 看到 `92/100` 如何被作废成 `INVALID` |
| Feishu 同步是否可靠 | Case 2 | 看到 update log、read-back log、读回标题和长度 |
| skill 改了是否真的有效 | Case 3 / Case 4 | 看到 RED/GREEN 如何约束未来触发 |
| 当前证据还缺什么 | 证明边界 | 区分已验证、人工回放和未证明能力 |

---

## 01 验证循环：Claim -> Gate -> Replay -> Evidence -> Writeback

Account Wiki 的验证循环不是抽象口号，而是五个可检查动作。

| 步骤 | 要回答的问题 | 本地证据形态 | 本轮例子 |
|---|---|---|---|
| Claim | 我们声称什么可发布、可触发、可复用？ | gate-review、proposal、正文判断 | “五篇审核稿可更新 Feishu” |
| Gate | 这个 claim 要过哪些硬门禁？ | reference / split / visual / publish gate | 参考子页未读全时 gate 改 FAIL |
| Replay | 未来遇到同类输入怎么走？ | RED/GREEN、pressure scenario | skill 从竖版一图流分流到横版章节卡 |
| Evidence | 当前证据是什么？ | log id、分数、读回长度、命令结果 | update log、read-back log、`12818` 字符 |
| Writeback | 证据写回哪里？ | `wiki/ops`、OpenSpec evaluation、tasks | gate-review 冻结失败稿并记录原因 |

这五步共同回答：这次判断凭什么成立，失败时为什么停止，下次 agent 从哪里恢复上下文。

## 02 Case 总表

| Case | 验证对象 | 关键数据 | 结论 |
|---|---|---|---|
| Case 1 | 五篇审核稿质量判断 | `92 / 100 -> INVALID`；Reference Gate `PASS -> FAIL`；Visual Gate `PASS with residual risk -> FAIL` | Gate 能撤销错误的 review-ready 判断 |
| Case 2 | Feishu 同步可验证性 | 三轮 update/read-back log；五篇包读回长度 `12818` | 外部写入必须能读回，不靠记忆 |
| Case 3 | public-report gate 行为资产 | 7 个 RED 场景全部 FAIL，8 个 GREEN 场景 PASS | 对外稿门禁从无到有，并能阻止 chat-only evidence |
| Case 4 | reference readback 回归修复 | 3 个回归 RED：子页未读、缺图降级、硬 gate 失败仍打分；4 个 GREEN PASS | 参考结构和视觉缺口不能再被降级 |
| Case 5 | learning-use map | scorecard 维度总和校验 `100`；5 个 GREEN PASS | 学习材料必须映射到输出用途或 skip reason |
| Case 6 | infographic 横图分流 | 14-17 均为 `1672x941` 横版教学卡；旧 skill 无横图/章节配图 route | 低信息量章节图不应被膨胀成一图流 |

## 03 Case 1：五篇审核稿从 92 分变成 INVALID

这个 case 证明 gate 能在“看起来已经通过”之后撤销错误判断。

| 检查项 | 初始判断 | 回读后修正 | 数据 / 原因 |
|---|---|---|---|
| Reference Structure Gate | PASS | FAIL | 参考页有具体 reading-map 子页，初始评分前没有完整读 runtime、install/migration、validation、roadmap |
| Split Gate | PASS | PARTIAL | 五个 reader jobs 被打包进一个 Feishu 审核包，不等于最终父子文档结构 |
| Visual Gate | PASS with residual risk | FAIL | 参考入口页使用实际视觉图，缺图不能当小风险 |
| Scorecard | `92 / 100` | `INVALID` | 硬门禁失败后不允许继续保留数字分 |
| Feishu packet | 已更新 | failed draft | 已同步文档被标记为失败稿，不继续润色 |

这个 case 的价值不是“分数变低”，而是系统证明自己能撤回错误信心。没有这个门禁，团队会继续在一个结构错误的 Feishu 包上做文案润色。

## 04 Case 2：Feishu 同步必须有回读数据

Feishu 写入命令成功，只能说明写入动作发生过。Account Wiki 要求更新后读回目标文档，记录能被复盘的数据。

| 同步阶段 | Update log id | Read-back log id | 读回证据 |
|---|---|---|---|
| 总览初版审核稿 | `20260508110132D5903B45E5F4794F6056` | `202605081103056E2DA35E3A5D784C34DC` | 读回开头含“审核稿。本文是...” |
| 总览修复稿 | `20260508112142FA047459B4E778549F81` | `20260508112224E3083FFB2D212C4BB08C` | 读回开头含“团队知识库构建路径” |
| 五篇审核包 | `20260508114500EF657CBA7C205A51F5B5` | `2026050811454826C53E90DD01685638E1` | 标题为“五篇审核稿”，读回长度 `12818` |
| 后续总览修正 | `20260508170815185A32A762E8618B993D` | `20260508171038C608AC7E527A288C2BC9` | 全量读回通过 |
| 最终命名修正 | 未在当前页展开 | `202605081843247C2CAB10CC6F1C9AEB1B` | 标题为 `Account Wiki：团队知识库构建路径`，旧 `Harness` 命名已移除 |

这个 case 证明：同步不是一个口头状态。每次外部写入都要留下 update、read-back、标题或开头内容等可复盘证据。

## 05 Case 3：public-report gate 从无到有

`add-public-report-quality-gate` 的 RED/GREEN 不是泛化判断，而是具体场景压测。

| 压测项 | RED | GREEN |
|---|---|---|
| public report gate 是否存在 | `.codex/skills/public-report-quality-gate/SKILL.md` 不存在，FAIL | skill 存在并定义触发、硬规则、引用资料，PASS |
| repo 是否会路由 Feishu 审核稿 | AGENTS 无 high-frequency route，FAIL | AGENTS 路由 reader-facing reports / Feishu drafts，PASS |
| voice gate 是否能拦 chat-like public drafts | 无硬门禁，FAIL | scorecard 把 chat residue、slogan、internal ops leakage 设为 fail condition，PASS |
| reference draft 是否先映射结构 | 无 reference map 要求，FAIL | SKILL 和 report-group template 要求 reference structure map，PASS |
| 多页报告是否先 split | 无 split gate，FAIL | overview/runtime/migration/validation/roadmap 必须有 split strategy，PASS |
| 叙事漂移是否阻断发布 | 无 Narrative Gate，FAIL | `lore -> team-lore -> wiki` 被误写成静态分工时 gate 失败，PASS |
| Feishu 是否先有 repo-visible evidence | 初始实现不要求稳定 gate-review artifact，FAIL | 必须先写 `wiki/ops/*-report-gate-review.md`，PASS |

这组数据说明：门禁不是后来补的解释，而是从 RED 缺口到 GREEN 行为的可检查变化。

## 06 Case 4：reference readback 回归修复

Case 1 暴露的是失败；Case 4 验证的是失败之后规则有没有补硬。

| 回归风险 | RED 证据 | GREEN 修复 |
|---|---|---|
| 有子页的参考 wiki 没读完就评分 | gate-review 曾在读完整子页前打 `92 / 100` | `SKILL.md`、scorecard、template、spec 要求 linked-page readback |
| 参考有关键视觉，本地缺图却只记 residual risk | gate-review 曾把 Visual Gate 记为 `PASS with residual risk` | scorecard / spec 要求缺少对应视觉或具体视觉计划时 Visual Gate FAIL |
| 硬 gate 失败还保留数字分 | `92 / 100` 后来必须作废 | scorecard / artifact / pressure scenario 要求 `INVALID` |
| 先写稿后补 reference map | 旧 workflow 容易先产出五篇包 | gate-review artifact 顺序改为 reference map/readback -> split -> draft |

这个 case 的价值是让同类错误下次更难发生。

## 07 Case 5：学习材料必须映射到输出用途

外部文章和参考图可以影响输出，但不能用“学到了”三个字替代证据。

| 学习对象 | capability type | 输出用途 | 数据 / 检查 |
|---|---|---|---|
| Account Harness reference group | structure / visual | 多页 reading map、生命周期视觉、页面拆分 | 进入 Account Harness Wiki Replay 表 |
| WaytoAGI Skill article | structure / visual / boundary | “先跑真实行为，再形式化 skill”的叙事边界 | 作为 opening 和边界校准，不直接晋升规则 |
| WeChat agent article | structure / evidence / boundary | problem-first opening、observable cases、current/future separation | 只复用结构，不发明本地指标 |
| public-report scorecard | learning reuse | 增加 Learning reuse 维度 | `awk` 校验维度总和为 `100` |

这个 case 证明学习材料在 runtime 中不是装饰：它必须说明影响了哪个 section、visual、metric、evidence block 或 skip reason。

## 08 Case 6：14-17 参考图触发横版章节卡，而不是一图流

用户给的 14-17 不是竖版海报，而是横版教学卡。

| 图片 | 尺寸 | 可复用结构 | 应用于 Account Wiki |
|---|---:|---|---|
| `14.png` | `1672 x 941` | old/new 对照 + 4 个编号步骤 + 底部结论 | 运行态：旧路径 vs 新 runtime + 4 步协作链 |
| `15.png` | `1672 x 941` | 三层结构 + 图标 + 底部一句话 | Wiki 结构：sources / ops-reports / rules-gates |
| `16.png` | `1672 x 941` | 两类场景对比 + 下方案例区 | 验证页：熟悉流程 vs 不熟悉流程如何靠回放补证据 |
| `17.png` | `1672 x 941` | 两个优化问题 + 两条迭代路径 | 返工页：先解决命题和证据，再逐轮优化视觉 |

这组图给出的不是内容，而是视觉语法：横版、低到中等信息密度、2-4 个块、每块一个图标、底部一句结论。因此 `infographic-onepager` 已补充横版 teaching-card 分流，避免把章节配图硬做成六段一图流。

## 09 当前能证明什么

| 已验证能力 | 支撑数据 | 能说明什么 |
|---|---|---|
| 错误评分可撤销 | `92 / 100 -> INVALID` | gate 能阻止错误 review-ready claim 延续 |
| 外部同步可复盘 | 多组 update/read-back log，读回长度 `12818` | Feishu 状态不是靠记忆判断 |
| 行为资产有 RED/GREEN | public-report gate 7 个 RED、8 个 GREEN；reference readback 3 个 RED、4 个 GREEN | skill / gate 变化有本地回放证据 |
| 学习复用可检查 | scorecard 总和 `100`，learning-use map 表 | 外部学习要映射到输出用途 |
| 视觉路线能纠偏 | 14-17 均为横版 `1672 x 941`，旧 skill 缺横图 route | 低信息量章节图不再被膨胀成一图流 |

## 10 仍然不能过度承诺什么

| 不能说 | 更准确的说法 |
|---|---|
| Account Wiki 已经证明适用于所有团队 | 当前证明来自本仓库、本轮 public-draft 和 skill/gate 返工 |
| Gate 能自动发现所有问题 | Gate 能拦住已定义的 reference、split、voice、visual、publish、replay 风险 |
| Replay 等于长期运行数据 | Replay 是可回放证据，不是多月 telemetry |
| Skill 修改后永远不会误触发 | 只能证明当前压力场景下的 route 更清楚 |
| Feishu 回读等于最终发布 | 回读证明同步正确，不代表业务内容已批准 |

## 收尾判断

Account Wiki 的验证价值在于：它能把失败变成结构化证据。

这次最有价值的数据不是某个高分，而是 `92 / 100` 被撤销为 `INVALID`。这说明系统不只会生产内容，也会在证据不足时停下来，并把“为什么停”写回 Wiki，供下一次继续使用。
