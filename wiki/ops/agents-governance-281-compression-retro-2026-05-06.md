---
title: agents-governance 281 行压缩 / retro
type: retro
canonical_object: agents-governance-drift
artifact_type: retro
language: zh-CN
audience: self
domain: wiki
layer: ops
ops_area: agent-governance
status: active
updated_at: 2026-05-06
ai_generated: true
derived_from:
  - openspec/changes/archive/2026-05-06-decide-root-governance-alignment/
  - openspec/changes/compress-codex-agents-md/
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/behavior-asset-governance-design-trace.md
  - wiki/language-policy.md
related_objects:
  - codex-global-agents-md
  - agents-governance-drift
  - root-governance-alignment
---

# agents-governance 281 行压缩复盘

## 背景

`~/.codex/AGENTS.md` 在 2026-04-01 到 2026-04-25 间从 223 行涨到 281 行（+26%），
然后卡在 281 行不动整一个月。整个 4-25 → 5-05 期间，团队的精力都在
`decide-root-governance-alignment` 这个 OpenSpec change 上——建模、写 design-trace、
反复 review 文字——**但文件一行都没改**。

到 5-06 归档那轮，文件真正被碰了。行数 281 → 283（+2），字节 12715 → 12459（-2%）。
行数没大降，但 Pattern Catalog 合规度 + 跨机器可移植性达成。

这份 retro 记录**这一个月是怎么被"立规矩"这件事困住的**，以及过程里几次争论的代价。

## 四个关键节点

### 节点 1：误把"立规矩"当"用规矩"

4-25 到 5-05 整整 10 天，对话反复在"这套规范够不够好"上打转。每轮：
改 trace → 发现新 candidate 标签 → 继续打磨 → 模型永远 candidate → 281 行没动。

5-05 意识到：**真问题不是规范不够好，是没有人签字把规范变成 decided**。
加了 trace §13 "no more copy-edit" 规则把自己挂住，才逃出这个循环。

**代价**：
- 1 个月的文档精力如果不算浪费，起码 70% 是在"描述描述描述"
- 治理模型的内容在 4-29 design.md 里就已经完整，"签字动作"拖了 6 天
- 归档前不得不加 §13 anti-drift 自锁——本身是漂移的证据

### 节点 2：skill-gate vs. abstraction-routing 偷换

我（claude）给 codex 准备的第一版复核简报里，把"behavior-asset 抽象路由"悄悄
收窄成了"skill gate"。两个测试题的主语都是 "skill"：

> "下次我想写 skill 时，规范告诉我应该先查什么？"
> "skill 跟已有 rule 重复，规范在哪一步能捕获？"

用户要治理的是 8 个落点（root / repo / rules / skills / wiki / ADR / OpenSpec / 不沉淀），
skill 只是其一。这种收窄如果不被发现，codex 的复核会得出一个错误的 PASS 信号。

**发现方法**：用户让 codex 背靠背复核 claude 的推荐是否忠实于设计目标，抓到 1 FAIL + 3 PARTIAL + 1 PASS。

**代价**：
- 不被发现：验证方法会把 1/8 的路径当成 8/8 来报 PASS，D1/D2/D3 会在假证据上拍板
- 发现后的修正通过 evaluation.md §Meta-review 落盘（2026-05-05）
- 补了一轮 codex 再复核，验证修正落盘忠实——5/5 全 FAITHFUL
- 单次 agent 推荐 **不应该** 被当成可信输入

### 节点 3：选 3（skill 化）被否决的瞬间

`compress-codex-agents-md` 设计 root 的 OpenSpec boundary 段时，出现选 3（做成 skill）：

> 把 13 行细则放 `~/.codex/skills/openspec-archive-review/SKILL.md`，root 只留 3 行指针。

好处看起来最干净：符合 Principle 3（triggered over ambient），root 行数下降最多。
用户理性地问："为什么不划算，我没懂？"

真实答案是 skill 的触发基于自然语言相似度，命中率约 70-95%。对于 "complete 要停"
这种**每次都必须命中**的短规则，85% 不够——漏一次，agent 会静默继续走。
skill 更适合**长而间歇的能力**（比如 `frontend-visual-governor`），不适合**短而关键的规则**。

**代价**：
- 没选 3 = 放弃了"未来多 repo 深度使用 OpenSpec"场景下的理论最优解
- 补偿是 ADR-0028 里写的升级路径："如果 3+ repo 进入深度使用 + 命中率阈值可接受，回来做 skill 化"
- skill 化的技术债被明确延期，不是忽略

### 节点 4：M5 "强撤回" 变"部分撤回"

第一版 evaluation.md 把 M5（intake 要求加 read-only / UI 自检类型）整条撤回，
理由写成"read-only 风险低"。codex 反馈："这是过度辩护，应该改成诚实收口。"

UI 撤回是成立的（`~/.codex/rules/web/design-quality.md` 已覆盖）。
read-only 撤回不成立——read-only 操作可以有副作用（日志、缓存、心跳、计数器）。
这次 change 不加 self-check 类型 OK，但**不等于风险不存在**。

修正：分为"UI 完全撤回" + "read-only 保留为 residual risk，等真实事故或第二次案例触发 reopen"。

**代价**：
- 不修正：治理会滑向"找理由说服自己不改" 的习惯
- 修正后：residual risk 依赖人监控 reopen trigger，没有自动探测机制
- ADR-0029 把"带 reopen trigger 的部分撤回"固化为合法姿态

## 总体代价盘点

| 项目 | 代价 |
|---|---|
| 时间 | 1 个月，从 4-25 intake 到 5-06 文件被真正碰 |
| 未选最优解 | skill 化被否（见节点 3）；line-count compression 延期 |
| 治理容忍度 | "撤回"是合法姿态（ADR-0029），但滑坡风险需要持续看管 |
| 残留风险 | M5 read-only / C3 环境变量依赖设置 / `~/.codex/` 无 git 保护 |
| 未来工作 | `phase1-repo-agents-compression` parked；successor change 做 line-count 压缩；新 repo 初始化模板（如果出现第 2 个 OpenSpec 深度使用 repo） |

## 一句话总结

**我们做的不是压缩一份文件，是把"立规矩 vs 用规矩"拆开**。
立规矩花了 1 个月，用规矩花了半天。下次类似治理问题，**先直接动手，如果卡住再回来补规则**，
比"先把规则建好再动手"快一个数量级。

## 2026-05-06 追加：预算压缩方案漂移校准

触发问题：新的 `compress-root-agents-budget` 方案一开始把
`Global Rule Routing` 抽到 `~/.codex/rule-routing.md`，并让 root `AGENTS.md`
在非 trivial 工作前加载它。用户指出：这只减少 `AGENTS.md` 行数，不减少 Codex
实际读取的整体上下文。

当前判断：这是从"降低默认上下文"漂移成了"降低单文件行数"。如果继续实施，会把
治理工程的地基从 behavior-asset abstraction routing 扭成 file-size accounting。

待验证事实：
- `~/.codex/AGENTS.md` 当前行/词/字节数，以及 `Global Rule Routing` 占比。
- 新 proposal/design 是否把成功指标写成 line-count，而不是 loaded-context count。
- 方案里的 load pointer 是否会让抽出的内容在默认路径上仍被读取。
- 哪些规则必须 ambient 常驻，哪些只能 trigger-gated 加载。

已验证事实：
- `~/.codex/AGENTS.md` 当前为 283 行 / 1865 词 / 12459 字节。
- `Global Rule Routing` 当前为 30 行 / 313 词 / 2733 字节，占 root
  AGENTS 约 10.6% 行数、16.8% 词数、21.9% 字节。
- 新 proposal 明确写的是 `line-count compression`，新 design 的预算目标也是
  `AGENTS.md` 行数；没有定义默认 loaded-context count。
- 新 design 要求在非 trivial implementation / verification 前加载
  `~/.codex/rule-routing.md`。因此若照此执行，默认非 trivial 工作的实际
  loaded context 不会随 `AGENTS.md` 行数下降而等量下降。

下一步：暂停实施 root 文件改写；先把 change 的成功指标从单文件行数修正为
默认加载上下文与触发加载上下文两类证据。
