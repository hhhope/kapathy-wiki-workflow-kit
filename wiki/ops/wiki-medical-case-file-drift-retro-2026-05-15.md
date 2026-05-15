---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: wiki-medical-case-file
artifact_type: retro
title: wiki-medical-case-file / drift retro 2026-05-15
type: retro
language: zh-CN
status: active
created_at: 2026-05-15
ai_generated: true
derived_from:
  - chat://2026-05-15/wiki-medical-loop-surgery-record-drift
  - openspec/changes/introduce-wiki-medical-case-file
related_objects:
  - llm-wiki-self-evolution
  - brainstorming-drift-wiki-trace
  - wiki-surgery
  - wiki-confirm
notes_scope: 记录用户指出的医疗闭环病例漂移：手术记录不应变成新的事实中心，病例应是一个稳定文件
---

# wiki-medical-case-file / drift retro 2026-05-15

## Trigger

用户在 wiki 医疗闭环推进中指出两个问题：

- 手术记录不能只有脚本输出，缺少人工/agent 意图和确认口径。
- 如果 `doctor`、`confirm`、`treatment`、`surgery` 各自生成一个新中心，病例概念会不停漂移。

随后用户明确校准：

```text
要做手术这件事情，肯定是已经判断出来的，需要人复核的东西是有内容的比如doctor给的或者确诊给的，手术依据这个做
```

## Rejected Framing

被否掉的 framing 是：

```text
surgery 重新生成一个手术记录，然后让人复核这个新记录
```

这个模型会把最新脚本输出误当作当前事实源，弱化 `doctor` 和 `confirm` 已经形成的病例上下文。

## Corrected Framing

更准确的模型是：

```text
一个病例文件
  -> doctor / 诊断
  -> confirm / 确诊
  -> treatment / 治疗
  -> surgery / 手术方案
  -> recovery / 复查
  -> archive or next action / 归档或下一步
```

`doctor` 和 `confirm` 给出手术依据。`surgery` 不重新诊断；它只把已确诊内容翻译成可复核的手术方案。

## Review Target

人工真正要复核的是病例里的 `Confirmed Decisions`：

- 哪些 doctor findings 是真问题。
- 哪些进入 treatment。
- 哪些进入 surgery。
- 哪些必须 OpenSpec。
- 哪些 relation 证据不足，不能自动写。

手术复核是 fidelity check：

- 是否只处理已确认的 surgery candidates。
- 是否越权写 relation、ADR、OpenSpec、taxonomy、MOC 或 AGENTS。
- relation 项是否保留为人工证据复核。
- governance / drift / ADR 项是否路由到 OpenSpec 或治理复核。

## Current Boundary

本页不是修复批准，不授权写 frontmatter、relation 字段、taxonomy、MOC、ADR、AGENTS、skills 或 OpenSpec 状态。

本页只把本次漂移转成仓库可见证据，并把后续正式承载指向：

- `openspec/changes/introduce-wiki-medical-case-file`

## Next Action

新 OpenSpec 变更应定义 canonical case file，并让 stage records 只作为 evidence attachments。
