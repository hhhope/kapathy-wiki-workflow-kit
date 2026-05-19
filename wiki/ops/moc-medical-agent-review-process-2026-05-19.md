---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: medical-agent-moc-surgery-preview
artifact_type: process
ai_generated: true
created_at: 2026-05-19
derived_from:
  - openspec/specs/wiki-medical-agent/spec.md
  - openspec/specs/obsidian-moc-projection/spec.md
  - wiki/ops/moc-apply-review-2026-05-18.md
  - scripts/build_wiki_medical_agent.py
  - scripts/build_wiki_moc_projection.py
language: zh-CN
related_objects:
  - obsidian-moc-projection
  - wiki-medical-agent
  - wiki-runtime-layer-contract
status: active
title: MOC medical-agent review process
type: process
updated_at: 2026-05-19
---

# MOC medical-agent review process

## 结论

MOC 的正常入口是 `wiki-medical-agent`，不是直接让用户跑 MOC generator。

用户表达 MOC 审查、MOC preview、Obsidian 知识地图预览、knowledge-map review
时，流程应先进入 medical-agent，由它完成意图识别、active case 校验和
surgery preview。底层 `build_wiki_moc_projection.py` 只是 worker / 调试工具，
不作为普通用户入口。

## 正常入口

用户说：

```text
$report-wiki-portfolio:wiki-medical-agent MOC 审查
```

或：

```text
走 medical-agent 看 MOC preview
```

agent 内部执行：

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "MOC 审查"
```

响应必须回到 medical-agent 的固定字段：

| 字段 | 含义 |
| --- | --- |
| Intent | 是否识别为 `moc_surgery_preview` |
| Case | 当前 active medical case |
| State | case 当前状态 |
| Allowed action | 是否允许 `preview_moc_surgery_plan` |
| Blocked action | 没有 active case 或多 active case 时的阻塞原因 |
| Next Action | 下一步是否进入 `review_moc_surgery_preview` |

## 当前运行结果

2026-05-19 的 medical-agent 预览结果：

| 指标 | 值 |
| --- | --- |
| intent | `moc_surgery_preview` |
| case | `wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md` |
| state | `archive_ready` |
| allowed_action | `preview_moc_surgery_plan` |
| next_action | `review_moc_surgery_preview` |
| candidate_count | 187 |
| create_count | 187 |
| update_count | 0 |
| noop_count | 0 |
| orphan_count | 0 |

抽样候选：

| 候选 | 路径 | link_count |
| --- | --- | ---: |
| domain-account-clearing | `wiki/moc/domain-account-clearing.md` | 1 |
| domain-agent-harness | `wiki/moc/domain-agent-harness.md` | 6 |
| domain-agentic-collaboration | `wiki/moc/domain-agentic-collaboration.md` | 1 |
| domain-ai-workflow | `wiki/moc/domain-ai-workflow.md` | 1 |
| domain-nirvana | `wiki/moc/domain-nirvana.md` | 3 |

## 审查流程

1. 用户从 `wiki-medical-agent` 入口发起 MOC 审查。
2. medical-agent 分类为 `moc_surgery_preview`。
3. medical-agent 校验 active case：
   - 没有 active case：阻塞为 `no_active_case`，下一步 `diagnose`。
   - 多个 active case：阻塞为 `multiple_active_cases`，下一步 `select_active_case`。
   - 一个 active case：允许 `preview_moc_surgery_plan`。
4. medical-agent 生成 MOC dry-run plan，并传入 surgery preview。
5. 用户审查 `moc_projection` 和 `surgery_preview`。
6. 如果只是在看过程，到 `review_moc_surgery_preview` 停止。
7. 如果要真正写 `wiki/moc`，必须另行显式批准 MOC apply 工作流。

## 底层工具边界

可以由 agent 在内部调用：

```bash
python3 scripts/build_wiki_moc_projection.py
```

用途是查看完整 dry-run JSON。它不写 `wiki/moc`。

不应作为普通入口直接建议：

```bash
python3 scripts/build_wiki_moc_projection.py --apply
```

`--apply` 会创建或更新 `wiki/moc/*.md`，只能在 medical-agent 审查完成后，
由用户明确批准进入 MOC apply workflow 时执行。

## 不做什么

- 不让 status、graph、recovery 或 archive review 隐式写 `wiki/moc`。
- 不把 MOC projection 当成 treatment candidate。
- 不通过 `Confirmed Decisions` 自动执行 MOC 写入。
- 不把底层 generator 当成用户正常入口。
- 不在没有 active case 校验时生成 MOC surgery preview。

## Proof Boundary

本文档记录的是 MOC 通过 `wiki-medical-agent` 进入审查的过程。
它不证明 Obsidian UI 效果，不批准 MOC apply，也没有生成任何 `wiki/moc`
页面。
