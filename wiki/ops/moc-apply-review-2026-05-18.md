---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: obsidian-moc-projection
artifact_type: review
ai_generated: true
created_at: 2026-05-18
derived_from:
  - openspec/specs/obsidian-moc-projection/spec.md
  - openspec/changes/archive/2026-05-18-add-obsidian-moc-projection/evaluation.md
  - scripts/build_wiki_moc_projection.py
language: zh-CN
related_objects:
  - wiki-react-decision-trace
  - wiki-runtime-layer-contract
status: active
title: obsidian-moc-projection / apply review
type: review
updated_at: 2026-05-18
---

# obsidian-moc-projection / apply review

## 结论

MOC 在 agent 环节里，但不是默认 medical recovery 自动执行的步骤。

正确位置是：

```text
wiki-react -> graph/status -> MOC apply preview -> explicit --apply
```

medical-agent 可以报告 MOC 相关状态，也可以在 surgery route 显式接收 MOC plan。
但默认 recovery 不应该偷偷生成 `wiki/moc/*.md`，否则会把“诊断/治疗”扩大成一次
可见导航结构发布。

## 本次 Dry-run

命令：

```bash
python3 scripts/build_wiki_moc_projection.py
```

结果：

| 指标 | 数量 |
| --- | ---: |
| candidate_count | 184 |
| create_count | 184 |
| update_count | 0 |
| noop_count | 0 |
| orphan_count | 0 |

按类型：

| 类型 | 数量 |
| --- | ---: |
| domain | 11 |
| object | 169 |
| relation | 4 |

这次没有写入 MOC 文件。当前计划如果 apply，会创建 184 个 `wiki/moc/*.md`。

## 高影响候选

| 候选 | 文件 | link_count | 说明 |
| --- | --- | ---: | --- |
| `domain-wiki` | `wiki/moc/domain-wiki.md` | 113 | 最大聚合面，适合先人工抽样检查。 |
| `domain-product-engineering-collaboration` | `wiki/moc/domain-product-engineering-collaboration.md` | 15 | 与最近材料和协作方法讨论相关。 |
| `domain-agent-harness` | `wiki/moc/domain-agent-harness.md` | 6 | 与 agent harness 学习记录相关。 |
| `domain-nirvana` | `wiki/moc/domain-nirvana.md` | 3 | 业务材料聚合。 |
| `domain-nirvana-project` | `wiki/moc/domain-nirvana-project.md` | 2 | 项目管理/周报类聚合。 |
| `relation-validates` | `wiki/moc/relation-validates.md` | 9 | 关系视图，可用于检查验证链路是否可读。 |

## 边界判断

可以做：

- 继续 dry-run 和 preview。
- 抽样检查高影响候选是否可读。
- 显式批准后运行 `python3 scripts/build_wiki_moc_projection.py --apply`。
- apply 后再跑 frontmatter / graph / status 检查。

不应该做：

- 让 status、graph、apply preview、react eval 或 medical recovery 隐式写 MOC。
- 在未确认前一次性创建 184 个导航页。
- 把 MOC apply 当作 archive review 的自然尾巴。

## 下一步清单

1. 先人工抽样看 6 个高影响候选的 preview 是否符合预期。
2. 如果接受一次性生成，再显式进入 MOC apply。
3. apply 后验证：
   - `python3 scripts/build_wiki_moc_projection.py`
   - `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10`
   - `python3 scripts/summarize_wiki_graph.py --limit 3`
4. 如果 184 个页面太多，另起一个 MOC 分阶段策略：先只生成 domain MOC，再考虑 object / relation MOC。

## Proof Boundary

本 review 只证明当前 repo 的 MOC projection dry-run 计划和流程边界。
它不证明 Obsidian UI 图谱效果，也没有生成任何 `wiki/moc` 文件。
