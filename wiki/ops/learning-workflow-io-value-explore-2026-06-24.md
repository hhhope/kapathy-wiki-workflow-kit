---
layer: ops
domain: agent-harness
ops_area: learning-capture
canonical_object: learning-workflow-io-value-explore
artifact_type: intake
status: active
created_at: 2026-06-24
updated_at: 2026-06-24
source_path: "chat://openspec-explore/learning-workflow-io-value/2026-06-24"
source_type: conversation
trace_mode: openspec-explore
type: intake
---

# Learning Workflow IO Value Explore

## Trigger

用户指出学习类输出必须说清楚：如果材料很多、token 或篇幅有限，应显式拆解；
需要交代输入、输出、输出怎么来的、核心价值是什么、价值判断是什么。

## Focus

- 检查 `learning-capture` skill 和相关 agent / OpenSpec 资产是否已经覆盖这些要求。
- 判断当前问题是规范缺口、执行缺口，还是两者都有。
- 不直接修改 skill 或 agent 行为；如果需要行为变更，后续走 OpenSpec change。

## Working Hypotheses

- 现有 learning capture 已有 source kind、topic anchor、score、adoption boundary
  等字段，但对 `input -> processing -> output -> value judgment` 的说明合同不够硬。
- `openspec-explore` 的自由探索姿态可能与本仓库对学习输出的可追溯要求存在张力。
- 本轮 OCR repo 学习暴露的问题更像“学习结果解释层缺失”，不只是少读了一个文件。

## Open Questions

- 是否需要给学习输出增加固定的 IO/provenance/value map？
- 是否需要在 token/篇幅不足时强制先声明分解计划，而不是压缩成结论？
- 该要求应落在 `learning-capture`，还是落在更高层的 agent handoff / conversation governance？

## Next Step

读取现有 learning capture skill、references、OpenSpec specs 和相关 ops/ADR，给出
缺口判断和候选修复路径。

## Findings

### Existing Coverage

现有资产已经覆盖了这些层：

- `AGENTS.md`：外部文章、repo、README、示例作为学习 / reference /
  adaptation material 时加载 `learning-capture`。
- `learning-capture/SKILL.md`：判断是否是学习请求、证据对象是什么、是否需要
  durable capture。
- `references/routing.md`：定义 intent gate、source kind gate、topic anchor、
  batch triage 和 output contract。
- `repo-readme.md` / scorecard：要求 admission、source class、grounding、
  local objective、adaptation boundary、score-first。
- `learning-output-reuse-gate`：当学习用于 reader-facing output 时，记录 learning
  point 如何进入具体 output element。

### Gap

当前缺口不是“没有学习规范”，而是缺少一层 `learning explanation contract`：

```text
input inventory
  -> reading / routing / scoring / source-grounding steps
  -> extracted outputs
  -> derivation evidence
  -> value judgment
  -> local transfer / non-transfer boundary
```

现有 output contract 更像结果字段清单：source kind、topic anchor、what was
learned、local usefulness、adoption boundary、next target。它没有强制说明：

- 本次到底读了哪些输入，哪些没读；
- 如果输入很多，是否先拆成批次、模块或问题；
- 每个输出结论来自哪类输入；
- 输出是 source fact、local inference、candidate transfer，还是 agent 判断；
- 核心价值为什么成立；
- 价值判断的证据和扣分项是什么；
- token / 篇幅不足时，哪些部分被延后而不是被压缩掉。

### Runtime Failure Mode

本轮 OCR repo 学习暴露的失败方式：

- 回答先给了技术栈判断和对 `cr-agent` 的帮助，但没有先声明输入拆解：
  README、go.mod、package.json、CLI entry、agent loop、rules、prompt、tools、
  output schema。
- 后续补了代码质量能力，但仍让用户误以为“规范只有这一点”。
- 真实对象应是整套 review contract，而不是某个 code-quality rule。
- 这属于输出解释层失败：source grounding 做了，但没有把 grounding 转成用户可见的
  `input -> output` map。

### Skill / Agent Assessment

`learning-capture` skill 有问题，但不是入口路由问题。

- 路由层基本成立：什么时候触发、什么时候不触发、按什么 source kind 分模块。
- score/admission 层基本成立：repo/README 学习已有 admission gate 和 scorecard。
- 输出复用层基本成立：reader-facing output 有 learning-use-map。
- 缺的是 durable learning note 和聊天答复的解释合同。

`openspec-explore` 也有张力：它强调自由探索、没有固定输出，而本仓库的学习线程
需要可追溯输出。对于学习 / 治理 / agent 自进化线程，不能完全沿用“summary
optional”。如果探索对象是学习机制本身，至少应留下 trace，并说明当前是结论、
候选判断，还是待 formalize 的行为变更。

### Candidate Fix

后续如果做成 OpenSpec change，建议范围是：

- 新增或修改 `learning-capture` reference，定义 `Learning Explanation Contract`。
- 对 75+ deep-read、复杂 repo、批量来源、或会影响 skill / agent / OpenSpec 的学习，
  强制输出：
  - `Input Inventory`：读了什么、没读什么、source grounding 状态。
  - `Decomposition Plan`：材料多或 token 不够时如何拆。
  - `Output Map`：本次产出的每个结论 / 记录 / 文件。
  - `Derivation Map`：每个输出从哪些输入和判断步骤来。
  - `Value Judgment`：核心价值、评分理由、扣分项、local transfer path。
  - `Boundary`：不复用、不晋升、待验证或待 OpenSpec 的部分。
- 更新 pressure scenarios，加入 OCR 这种 repo-learning case：
  “用户追问规范是不是只有一点时，系统必须能回放入口文件、规范分层、推导链和
  价值边界。”

## Current Status

这是 explore trace，不是行为变更。当前没有修改 `learning-capture` skill、
`AGENTS.md` 或 OpenSpec spec。若要让后续会话强制执行，需要新开 scoped OpenSpec
change。
