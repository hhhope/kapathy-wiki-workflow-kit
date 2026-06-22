# AICoding 生命周期协作卡

## 一句话结论

研发流程不该只有“写代码”和“做验收”两段，而应该是 `需求 -> SDD -> 研发 -> CR -> 验收 -> 沉淀` 六段协作，每一段都让 AI 扮演不同角色。

## 阶段总表

| 阶段 | 推荐方法 | 主要载体 | AI 的主职责 | 完成标志 |
|---|---|---|---|---|
| 需求 | `brainstorm first` | Feishu / PRD / Jira / 会议纪要 | 拆问题、列方案、比边界、列未知项 | 目标、边界、优先级清楚 |
| 设计 | `SDD first` | OpenSpec `proposal/design`、详设文档 | 收敛结构、接口、风险、验收思路 | 方案可实施、边界可解释 |
| 研发 | `implementation under SDD` | 代码、skills、Graphify、Lore | 按设计实施、减少盲搜、记录新事实 | 改动与设计一致、没有明显漂移 |
| CR | `CR shift-left` | reviewer agent、rules、diff | 提前做结构/安全/边界 review | 问题在提交前暴露 |
| 验收 | `TDD inside OpenSpec` | tests、benchmark、routing checks、raw data proof、eval docs | 证明结果成立，而不是口头判断“应该可以” | 有可追溯证据 |
| 沉淀 | `absorb continuously` | logs、weekly review、Lore、Feishu share | 把有效事实、pitfall、结果沉成可复用知识 | 下次任务更便宜 |

## 1. 需求阶段

| 先问什么 | 不该做什么 |
|---|---|
| 这次要解决的真实问题是什么 | 不要一上来跳实现 |
| 边界、优先级和非目标是什么 | 不要把所有想法都混成一个任务 |
| 有哪些未知项会影响设计 | 不要假装需求已经完整 |

AI 在这一段更像：

- 脑暴助手
- 对齐助手
- 未知项整理器

## 2. 设计阶段

| 先做什么 | 为什么 |
|---|---|
| 用 OpenSpec 收 proposal / design | 把思路变成可实现结构 |
| 把风险和边界前置写清楚 | 避免研发期边写边猜 |
| 把验收思路提前写进去 | 让 TDD 不再是最后补 |

这一段的核心不是“写漂亮设计文档”，而是：

- 让实现有边界
- 让 CR 有基线
- 让验收有入口

## 3. 研发阶段

| 默认动作 | 目的 |
|---|---|
| 先看 `AGENTS.md`、PROJECT、git truth | 确认能不能开工 |
| 再看 OpenSpec / Lore / Graphify | 用最小上下文决定先读什么 |
| 再按 skill 实施 | 降低临场发挥和盲搜成本 |
| 把新事实留进 logs / evidence | 为后续吸收留痕 |

这一段 AI 的角色不是“自由发挥的 coder”，而是：

- 受约束的实施者
- 低 token 成本的结构检索者
- 会留下证据的执行者

## 4. CR 阶段

| 为什么要前置 | 如何前置 |
|---|---|
| 如果 CR 全留到最后，返工成本最高 | 在开发中就跑 reviewer pass |
| 很多问题其实不是代码写完后才出现 | 设计边界、权限边界、数据边界都能提前查 |
| 安全和结构问题越晚发现越贵 | 用 rules + reviewer agent 做 early pass |

推荐分成两轮：

1. 实现中途的结构/边界 review
2. 提交前的完整 diff review

## 5. 验收阶段

| 验什么 | 用什么 |
|---|---|
| 行为是否成立 | TDD / tests |
| 路由是否成立 | routing checks |
| 结构检索是否有价值 | benchmark / Graphify evidence |
| 新字段/新接口是否真实存在 | raw data proof |
| 结论是否可追溯 | eval docs / readback |

这里的重点是：

- `TDD` 不再是实现后补的一层皮
- 而是和 OpenSpec change 一起进入过程层

## 6. 沉淀阶段

| 沉什么 | 去哪里 |
|---|---|
| 一次性的任务事实 | logs |
| 可复用的原则 / 边界 / pitfall | Lore |
| 对外要解释的内容 | Feishu share / wiki |
| 有价值的评测结论 | evidence / benchmark docs |

Lore 在这里吸收的是 `raw wiki` 思路：

- 先记真实事实
- 再做 weekly review
- 最后升级成 durable memory

## 这张协作卡怎么用

| 如果你在 | 就优先看 |
|---|---|
| 新需求刚开始 | 需求阶段 + 设计阶段 |
| 已经进入实现 | 研发阶段 + CR 阶段 |
| 准备收口 | 验收阶段 + 沉淀阶段 |
| 想推进到更高阶段 | 对照 `L1-L4` 路线图 |

## 一句话收束

让 AI 更有效，不是让它一步到位替你做完所有事情，而是让它在每个研发阶段都做对该做的那部分。
