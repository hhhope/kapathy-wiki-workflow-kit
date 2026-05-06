---
title: 行为资产治理 / 中文摘要
type: summary
canonical_object: behavior-asset-governance
artifact_type: summary
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: candidate
updated_at: 2026-05-06
ai_generated: true
derived_from:
  - wiki/ops/behavior-asset-governance-design-trace.md
  - openspec/changes/decide-root-governance-alignment/design.md
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/agents-governance-281-compression-retro-2026-05-06.md
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
related_objects:
  - codex-global-agents-md
  - agents-governance-drift
  - root-governance-alignment
notes_scope: 英文 design-trace 的中文入口。承载治理模型的中文版摘要、主线、三个
  已采纳决定、post-archive 实施校准，以及当前 active change 的防漂移验收口径。
  完整推导、外部引用、历史修订记录请看英文 trace；post-archive 校准看 retro
  与当前 OpenSpec change。
---

# 行为资产治理 · 中文摘要

本页是英文 design-trace 的中文入口。**完整内容在
[behavior-asset-governance-design-trace.md](behavior-asset-governance-design-trace.md)**，
该文依据 `wiki/language-policy.md` 新增的 design-trace 英文豁免保留英文。

本页只保留四件事：治理模型一页 · Harness Engineering 学到什么 · 当前目标 · 资产更新判断。

## 1. 治理模型一页

### 四层分工（每层只做自己的事）

| 层 | 管什么 | 不管什么 |
|---|---|---|
| Root AGENTS (`~/.codex/AGENTS.md`) | 跨仓库安全底线：destructive git、external call、dirty tree 等硬拦截 | 单仓库策略 |
| Repo AGENTS (`<repo>/AGENTS.md`) | 本仓库策略、OpenSpec 触发条件、工作流路由、skill 授权合约 | 覆盖 root 安全底线 |
| `rules/`（常驻） | 按工种匹配加载的约束（Python / Web / Common 等） | 任务编排 |
| `skills/`（触发） | `/name` 或明确意图触发时才生效的 `SKILL.md` 合约 | 在没有 carve-out 的情况下覆盖 repo AGENTS |

三条证据通道与四层正交：

- **OpenSpec change**：生命周期容器（proposal / design / tasks / archive）
- **evaluation.md**：变动前后行为证据（Before / After / Residual Risks）
- **replay-harness**：仅当 skill 的触发或拒绝语义发生变化时使用，其他情形不需要

### 六原则

1. 每条行为规则只在一层有 source of truth；其他层引用不复制
2. 加载顺序 ≠ 权威顺序：就近加载不等于具有更高优先级
3. 触发式优先于常驻式：`skills/` 不默认加载，`rules/` 按工种命中才加载
4. 指令 budget 有限：root AGENTS 是跨仓库共享资源，别把仓库规则塞进去
5. 证据先于运行时变更：行为修改需要 `evaluation.md` 中的前后对比；harness 只在触发/拒绝语义变化时加
6. Candidate 与 decided 可见：未被评审接受的规则写 `candidate`；spec 里 `SHALL` / `MUST` 仅在评审通过后使用

### 六步最小流程

声明目标层 → 查 source of truth → 查权威链（覆盖别层需要 carve-out，否则驳回）→ 按语义权重选落点 → 记录证据 → 过 self-check。

落点选择矩阵：

| 情形 | 落点 |
|---|---|
| 改 root AGENTS，或改 skill 的触发 / 拒绝语义 | OpenSpec change 必走 |
| 改 repo AGENTS | OpenSpec change 或 ADR / retro |
| 纯文字 / 路由整理 | 直改，可附 `evaluation.md` |

## 2. Harness Engineering 学到什么

这轮真正学到的不是"多引用几篇最佳实践"，而是：**外部文章只有转成
本地 failure mode、验收门和可恢复的 agent 工作环境，才会对治理有帮助。**

正确吸收路径：

`article insight → local failure mode → RED scenario → GREEN behavior → evaluation evidence`

要落地的 best practice 必须可量化、可复核，并绑定证据。允许的证据只有三类：

- 外部文档内容：有 URL、发布日期或访问日期、具体段落/行号、能支撑的结论边界
- 本地 demo / fixture：有 RED/GREEN、输入输出、运行命令或人工回放记录
- git 类项目对照：有仓库/commit/path、可复查的结构或行为差异

没有证据的说法只能是 `candidate observation`，不能写进 root `AGENTS.md`、
spec `SHALL`、skill hard rule，或作为 archive-ready 结论。

### 可复核证据表（2026-05-06）

| 来源 | 证据形态 | 可支撑的窄结论 | 本地采纳边界 |
|---|---|---|---|
| OpenAI, `Harness engineering: leveraging Codex in an agent-first world`, `https://openai.com/index/harness-engineering/` L80-L91 | 外部文档 | `AGENTS.md` 应更像地图 / 目录，而不是大型手册；仓库知识应落在结构化 source of record。 | 采纳为目标口径：root `AGENTS.md` 只做地图；细节只有成为可检查 source-of-record artifact 时才搬出，而不是藏进默认上下文。 |
| OpenAI harness engineering L231-L239 | 外部文档 | 只有文档不够；需要严格边界和机械不变量来防止架构漂移。 | 只作为后续自动化候选；当前 change 可以声明边界，但不新增 lint / checker。 |
| OpenAI harness engineering L283-L290 | 外部文档 | agent 会复制既有模式，漂移会累积；持续清理优于周期性人工清理。 | 采纳为 residual-risk 视角：root 治理不能留下吸引 agent 继续复制的坏样例；自动清理不在当前范围。 |
| Anthropic, `Scaling Managed Agents`, `https://www.anthropic.com/engineering/managed-agents` L17-L25 | 外部文档 | harness 会编码会过期的假设；稳定接口应比实现细节更长寿。 | 采纳为分类口径：root 保留项必须是 hard stop、稳定 source pointer、触发式细节，或明确 candidate assumption。 |
| Anthropic Managed Agents L35-L43 | 外部文档 | session / harness / sandbox 解耦能提高恢复性并隔离凭证。 | 只作类比：root 治理要保留恢复 artifact 和 source pointer；不改本仓库 sandbox / tool 架构。 |
| Claude, `Common workflow patterns for AI agents`, `https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them` L278-L299 | 外部文档 | workflow 用 checkpoint 和边界塑造 agent 自主性；先用最简单流程，只有可测需求才升级。 | 采纳：当前保持顺序流；不因为文章存在就加 parallel agents 或 evaluator-optimizer loop。 |
| Claude, `Building agents with the Claude Agent SDK`, `https://claude.com/blog/building-agents-with-the-claude-agent-sdk` L380-L388 | 外部文档 | 改进 agent 要研究失败，并问它是否有正确信息、规则、工具和 eval set。 | 采纳：root 改写必须绑定本地 failure mode 和验证方法，不能只说“最佳实践”。 |
| Anthropic, `Harness design for long-running application development`, `https://www.anthropic.com/engineering/harness-design-long-running-apps` L31-L47 | 外部文档 | generator / evaluator 角色分离，按明确标准评分，尤其适合主观质量。 | 只作为未来 review / evaluator loop 候选；当前只记录标准，不新增 evaluator agent。 |
| Anthropic harness design L115-L122 | 外部文档 | evaluator logs 和细粒度标准能让失败更可行动，但 evaluator 判断仍需人类校准。 | 采纳为 evaluation 质量警告：RED/GREEN 要说明 failure 为什么公平，不声称自动 evaluator 已可靠。 |
| Anthropic, `Demystifying evals for AI agents`, `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents` L202-L211 | 外部文档 | agent eval 应在真实或 sandboxed 环境中评结果，并按任务选择工具。 | 只作为未来 runtime proof 候选；当前 root-context change 只用文档和人工证据。 |
| Anthropic evals L244-L263 | 外部文档 | eval 环境应隔离；grader 应偏向 outcome grading、partial credit 和 transcript review。 | 采纳：评估 agent 是否找到正确 source、验证行为、留下恢复证据；不强制唯一操作路径。 |
| Anthropic, `Effective harnesses for long-running agents`, `https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents` L73-L101 | 外部文档 | 长任务 agent 需要 startup bearings、progress artifacts、先跑基础测试、结束时留下进度。 | 采纳为 agent-legibility 口径：下一轮 agent 必须知道去哪读、怎么验证、哪个 artifact 保留恢复点。 |
| Anthropic, `A diff tool for AI`, `https://www.anthropic.com/research/diff-tool` L18-L23 and L67-L69 | 外部文档 | 传统 eval 抓已知风险；diff 能帮助发现行为差异，而不是从头审计一切。 | 采纳为比较原则：review 改变的行为和证据差异，不重新审整个治理语料库。 |

当前失败案例：

| 输入 | 错误吸收 | 正确吸收 |
|---|---|---|
| Anthropic prompt engineering | 又写一条治理规则 | 先声明 success criteria、失败样例、验证方法 |
| OpenAI harness engineering | 把 `AGENTS.md` 当百科压缩 | 把 `AGENTS.md` 当地图，repo/wiki/OpenSpec 做 source of record |
| Progressive disclosure / dynamic loading | 把长表搬到另一个文件 | 默认不加载；只有任务触发后才加载细节 |
| Managed Agents | 把当前 harness 假设固化成规则 | 稳定接口优先；假设会随模型能力变化而过期 |
| Workflow patterns | 一上来加多 agent / evaluator | 先用最简单顺序流；只有可测收益时才升级 |
| Context cost / instruction budget | 追 `AGENTS.md` 行数 | 区分 default loaded context 与 triggered loaded context |
| Evals / diff / long-running harness | 建一个 harness 文档 | 用 RED/GREEN、运行记录、差异对比和恢复点拦住看似合理但无效的方案 |

必须拦住的 RED 场景：

```text
RED: 把 Global Rule Routing 从 AGENTS.md 抽到 rule-routing.md，
但 AGENTS.md 要求非 trivial 工作默认加载 rule-routing.md。
Expected: FAIL。
Reason: 单文件行数下降，实际 loaded context 没有按目标下降。
```

因此，后续行为资产治理的成功指标不能只看行数。至少要看：

- default loaded context
- triggered loaded context
- drift prevention
- routing correctness
- evaluation evidence quality
- agent legibility：下一轮 agent 是否能知道去哪读、怎么验证、何时停
- recoverability：中断后是否能从 repo-visible artifact 恢复，而不是靠聊天记忆

### 文章校准后的目标

当前目标不是"让 root AGENTS 更短"，而是：

> 把 root `AGENTS.md` 治理成 agent-legible map：默认上下文只保留硬拦截、路由原则和 source-of-record 指针；具体知识、验证方法和恢复状态必须在 repo-visible artifacts 中可检索、可验证、可更新。

这意味着：

- `AGENTS.md` 是地图，不是手册。
- wiki / OpenSpec / evaluation 是系统记录，不是附属说明。
- harness 是反馈闭环：gather context → act → verify → leave artifact。
- eval 评的是产物和可恢复性，不强制规定唯一操作路径。
- 新增治理规则前，先问它是否替代、缩短、移走了旧文本，或者是否是必须常驻的 hard stop。

## 3. 当前主线（2026-05-06）

`decide-root-governance-alignment` 已归档；`compress-codex-agents-md` 已归档。
当前 active successor 是 `compress-root-agents-budget`，但它的原始目标漂移了：
从"治理 root context 防漂移"滑成了"压缩 `AGENTS.md` 行数"。经过这批
harness / managed agents / evals 文章校准后，目标进一步收敛为
**agent-legible governance harness**：让 agent 能从短入口找到正确 source，
按触发加载细节，完成后留下可恢复证据。

最新实测：

- `~/.codex/AGENTS.md` 当前为 283 行 / 1865 词 / 12459 字节
- `Global Rule Routing` 为 30 行 / 313 词 / 2733 字节，占 root AGENTS
  约 10.6% 行数、16.8% 词数、21.9% 字节
- 如果把它搬到 `rule-routing.md` 但仍默认加载，实际上下文不会等量下降

当前 next action：先修正 `compress-root-agents-budget` 的成功标准，再决定是否改
`~/.codex/AGENTS.md`。实施前必须先过三个判断：

- 是否减少默认误导，而不只是减少行数？
- 是否提升 agent legibility，而不只是增加文档？
- 是否留下下一轮可恢复证据，而不依赖当前聊天上下文？

## 4. 已采纳决定

| ID | 问题 | 结果 |
|---|---|---|
| **D1** | 是否把六原则 + 四层目录 + 六步流程作为本仓库的治理模型？ | **采纳**。 |
| **D2** | Pattern Catalog 五字段声明在 `spec.md` 里用 `SHOULD` 还是 `SHALL`？ | **保留 `SHOULD`**。至少在实际落地三个新 pattern 之后，再考虑升 `SHALL`。先保留作者在不适用字段时省略的空间。 |
| **D3** | `SKILL.md` 的 rule 依赖声明是必填还是可选？ | **可选（opt-in）**。与原则 3（触发式优先）一致：如果 skill 没有声明 rule 依赖，就不加载任何 rule。设为必填会让现存所有 `SKILL.md` 文件立即失效。 |

## 5. 资产更新判断

| 资产 | 是否更新 | 原因 |
|---|---|---|
| `behavior-asset-governance-zh.md` | 是 | 中文入口要承载 post-archive 实施校准 |
| `behavior-asset-governance-design-trace.md` | 否 | 归档设计 trace，不承载新实施校准；继续改正文会重开 §13 漂移 |
| `agents-governance-281-compression-retro-2026-05-06.md` | 已更新 | 已记录 line-count → loaded-context 漂移和实测数据 |
| `compress-root-agents-budget` | 是 | 当前 active change 的目标和验收指标需要修正 |
| `~/.codex/AGENTS.md` | 暂不改 | 先修验收门，再实施 root context 治理 |

## 6. 反漂移约束

- 不把 post-archive 学习回写成旧 design-trace 正文。
- 不把文章引用当成治理有效性的证据；必须有可复核证据，并在本地形成
  RED/GREEN、demo/fixture、或 git 项目对照。
- 不用单文件行数替代 loaded-context 证据。
- 不通过新增 checklist / skill / rule 来无限增殖治理；新增治理必须替代、缩短、移走旧文本，或证明它是 always-on hard stop。

## 7. 详细内容在哪

- 推导细节、六原则的外部来源引用、Pattern Catalog 五字段、Self-Check 四栏、三张 ASCII 图、2026-05-04 七项 codex-review 补丁、反漂移主线的完整说明：
  [wiki/ops/behavior-asset-governance-design-trace.md](behavior-asset-governance-design-trace.md)
- 原始诊断与阶段建议：
  [wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md](codex-global-agents-md-diagnosis-intake-2026-04-25.md)
- post-archive 压缩漂移实测：
  [wiki/ops/agents-governance-281-compression-retro-2026-05-06.md](agents-governance-281-compression-retro-2026-05-06.md)
- 当前 active OpenSpec change：
  `openspec/changes/compress-root-agents-budget/`
