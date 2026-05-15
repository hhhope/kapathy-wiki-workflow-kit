---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: llm-wiki-self-evolution
artifact_type: ops-model
created_at: 2026-05-14
derived_from:
  - docs/superpowers/specs/2026-05-14-llm-wiki-self-evolution-design.md
  - openspec/changes/formalize-llm-wiki-medical-loop
status: draft
title: LLM-WIKI 自进化医疗闭环
---

# LLM-WIKI 自进化医疗闭环

## 一句话

LLM-WIKI 自进化不是 `doctor -> 自动改 wiki`，而是：

```text
体检 -> 诊断 -> 确诊 -> 治疗 -> 手术 -> 复查 -> 归档
```

英文工作名：

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

## 分工

- `checkup / 体检`：看 wiki 健康状态，例如 frontmatter、taxonomy、graph、status、MOC dry-run。
- `doctor / 诊断`：生成诊断病历，不写结构，不批准修复。
- `review / 确诊`：人确认哪些是误报、哪些可治疗、哪些要手术、哪些要 OpenSpec。
- `treatment / 治疗`：小范围、低风险、明确确认后的修复。
- `surgery / 手术`：大范围结构性修复，例如批量 frontmatter、关系重建、MOC 投影、ADR 或治理漂移。
- `recovery / 复查`：修复后重新跑 checker、doctor、graph、status、MOC dry-run。
- `archive / 归档`：把诊断、确认、修复、复查串成后续 agent 可读的病历链。

## 硬边界

```text
doctor diagnoses; review confirms; treatment or surgery writes; recovery proves;
archive preserves.
```

对应中文：

```text
医生只诊断；病人确认病情；治疗或手术才写入；复查才证明；归档才沉淀。
```

## 当前 wiki-doctor 结果怎么解释

当前详细诊断记录显示：

- 153 个候选
- 144 个 review-focus 条目
- 71 个 drift/governance 风险
- 112 个关系证据 warning
- 9 个 safe frontmatter 候选

这个整体是 `surgery candidate / 手术候选`。原因是范围大，并且牵涉治理、
关系证据、ADR、OpenSpec 和 MOC 边界。

但其中少量已经确认且低风险的条目，可以在后续 `review-decision` 工作流存在
后拆成 `treatment batch / 治疗批次`。

## 升级规则

- `safe_to_apply_frontmatter=true` 只表示可以进入治疗候选，不是自动批准。
- `relation_weak_evidence` 不能批量接受。
- `openspec_required` 不能通过治疗绕过。
- drift、retro、reanchor、runtime behavior 相关条目不能当普通 markdown 修补。
- MOC 写入属于结构投影写入，需要明确批准或后续 OpenSpec。

## 后续拆分

建议顺序：

1. `formalize-llm-wiki-medical-loop`
2. `add-wiki-review-decisions`
3. `add-wiki-treatment-workflow`
4. `add-wiki-surgery-workflow`
5. `add-wiki-recovery-records`

本页只记录总模型，不授权自动修复。
