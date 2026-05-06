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
updated_at: 2026-05-05
ai_generated: true
derived_from:
  - wiki/ops/behavior-asset-governance-design-trace.md
  - openspec/changes/decide-root-governance-alignment/design.md
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
related_objects:
  - codex-global-agents-md
  - agents-governance-drift
  - root-governance-alignment
notes_scope: 英文 design-trace 的中文入口。承载治理模型的中文版摘要、主线、三个
  待拍板决定，以及当前 in-flight change 的收敛状态。完整推导、外部引用、历史修订
  记录请看英文 trace。
---

# 行为资产治理 · 中文摘要

本页是英文 design-trace 的中文入口。**完整内容在
[behavior-asset-governance-design-trace.md](behavior-asset-governance-design-trace.md)**，
该文依据 `wiki/language-policy.md` 新增的 design-trace 英文豁免保留英文。

本页只保留三件事：治理模型一页 · 当前主线 · 三个待拍板决定。

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

## 2. 当前主线（2026-05-05 锁定）

> 三个决定 → 归档 `decide-root-governance-alignment` → 解决 Phase 1 歧义 → 关停或合并其他 in-flight change → 再开一个真的修改 `~/.codex/AGENTS.md` 的 change。

### State snapshot（2026-05-05）

- 英文 trace 内部一致，`openspec validate decide-root-governance-alignment --strict` 通过
- 治理模型（六原则 + 四层目录 + 六步流程 + 三条证据通道）已完全由 class A / B 来源支持；内容已经 ready，只差评审决定
- `openspec list --json` 看到 4 个 in-progress changes，但只有 `decide-root-governance-alignment` 在过去两周里推进到 30/47。`phase1-repo-agents-compression` (0/10)、`decide-no-repo-local-commit-hook` (0/7)、`close-agents-governance-candidate-materials` (0/8) 自 2026-04-21 起未动
- `~/.codex/AGENTS.md` 仍为 281 行；4 个 in-flight change 没有任何一个真正动过行为文件

## 3. 三个待拍板决定

| ID | 需要拍板的问题 | 推荐 |
|---|---|---|
| **D1** | 是否把六原则 + 四层目录 + 六步流程作为本仓库的治理模型？ | **采纳**。每条原则都有 class A 或 B 来源；四层模型是参考文献收敛的共识；六步流程是从原则 1–6 可推导的最小闭环。 |
| **D2** | Pattern Catalog 五字段声明在 `spec.md` 里用 `SHOULD` 还是 `SHALL`？ | **保留 `SHOULD`**。至少在实际落地三个新 pattern 之后，再考虑升 `SHALL`。先保留作者在不适用字段时省略的空间。 |
| **D3** | `SKILL.md` 的 rule 依赖声明是必填还是可选？ | **可选（opt-in）**。与原则 3（触发式优先）一致：如果 skill 没有声明 rule 依赖，就不加载任何 rule。设为必填会让现存所有 `SKILL.md` 文件立即失效。 |

三个决定一次通过，以下 tasks 连带关闭：2.1–2.4、3.7、3a.5、3b.8、3b.9、3b.15、3b.16、3b.17。

## 4. Phase 1 歧义（归档前必须解决）

"Phase 1" 在仓库历史里有两个不兼容的定义，归档评审必须选一个、明确撤回另一个：

- **intake §12 的阶段建议**：Phase 1 = 做人工版 harness 模板，不写 checker，不改行为文件。
- **OpenSpec change `phase1-repo-agents-compression`**：Phase 1 = 压缩 repo `AGENTS.md`。

两个定义不能共存。design-trace 当前隐含采用 intake 的定义。如果归档评审确认 intake 定义，`phase1-repo-agents-compression` 需要改名或重新 scope；反之则 intake 的阶段建议需要补一条撤回注记。

## 5. 反漂移约束（为什么不再打磨这篇文档）

- **不再 copy-edit** `design.md` / `spec.md` / 英文 trace / 本页。`decide-root-governance-alignment` 归档评审之前，任何"再润一下"都算漂移不算进步。
- **治理设计 change 同时只能有一个在进行**。当前 4 个并行的 in-flight change 本身就是漂移症状——正好是这个 change 原本想解决的 root AGENTS 增长模式的镜像。
- **撤回的数字保持撤回**。intake §11 已把"openai/codex 40 行"从目标降级为观察。任何 Phase 1 / Phase 2 讨论若再度引入 root AGENTS.md 的目标行数，需要新的、已验证的来源才接受。

## 6. 详细内容在哪

- 推导细节、六原则的外部来源引用、Pattern Catalog 五字段、Self-Check 四栏、三张 ASCII 图、2026-05-04 七项 codex-review 补丁、反漂移主线的完整说明：
  [wiki/ops/behavior-asset-governance-design-trace.md](behavior-asset-governance-design-trace.md)
- 原始诊断与阶段建议：
  [wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md](codex-global-agents-md-diagnosis-intake-2026-04-25.md)
- 活动中的 OpenSpec change：
  `openspec/changes/decide-root-governance-alignment/`
