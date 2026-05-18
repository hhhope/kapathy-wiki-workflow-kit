---
canonical_object: wiki-graph-extraction
artifact_type: method
layer: ops
domain: wiki
ops_area: wiki-runtime
related_objects:
- wiki-frontmatter-model
- wiki-naming-model
- wiki-relation-analysis
formalizes:
- wiki-graph-extraction
---

# Agent-Readable Wiki Graph Extraction

这页定义当前仓库在演变型页面上的最小 graph extraction workflow。

目标不是做完整图谱产品，而是先把已 formalize 的对象和关系提取成 machine-readable artifact，方便 agent 低成本查看。

## 依赖顺序

graph extraction 明确是下游层，必须建立在下面两层之后：

1. `canonical object / artifact type` 命名模型
2. 最小 frontmatter 与 typed relation fields 模型

先稳定命名和结构字段，再做 extraction。

## 覆盖范围

第一版只提取这些层：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

## 最小输出合同

extractor 至少输出：

- `nodes`
- `edges`
- `warnings`

### Node 形状

每个 node 至少保留：

- `page_path`
- `canonical_object`
- `artifact_type`
- `source_layer`

### Edge 形状

每个 edge 至少保留：

- `source_page_path`
- `relation_type`
- `target`

## 支持的关系字段

第一版支持提取：

- `related_objects`
- `derived_from`
- `validates`
- `formalizes`

如果存在，也允许保留：

- `supersedes`
- `replaces`

## 当前 extractor 边界

当前 extractor 的默认策略是：

- 优先吃 shared frontmatter fields
- 对已经 formalize 的对象族允许有限 resolver
- 解析不了身份的页面只发 warning，不做语义猜测

这意味着：

- 这是结构提取，不是语义图谱
- `warnings` 是预期输出的一部分
- 不应把通过 extraction 说成“全仓图谱已经完成”

## 运行方式

```bash
python3 scripts/extract_wiki_graph.py
```

生成 sample artifact：

```bash
python3 scripts/extract_wiki_graph.py > scripts/examples/agent_readable_wiki_graph_sample.json
```

## 当前非目标

第一版不做这些事：

- 不做 graph viewer
- 不做 graph scoring
- 不做旧页批量补字段
- 不把 unresolved page 强行推断成有身份节点

## 一句话判断

`先把对象和 typed relation 提出来，再谈图谱体验。`
