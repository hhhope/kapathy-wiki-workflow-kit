---
title: wiki-readable-views-validation / replay-harness
canonical_object: wiki-readable-views-validation
artifact_type: replay-harness
related_objects:
  - wiki-readable-views
validates:
  - wiki-readable-views
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
updated_at: 2026-04-20
ai_generated: true
---

# wiki-readable-views-validation / replay-harness

这页定义 `wiki-readable-views` 的最小可执行验证合同。

用途很窄：

- 证明三个阅读视图已经形成一个最小 bundle
- 证明索引入口已经接上
- 不把这种 proof 夸大成语义理解 proof

## 最小 Validation 字段

- `bundle_label`
- `timeline_view`
- `artifact_grouping_view`
- `relation_reading_view`
- `required_indexes`
- `red_baseline`
- `green_result`
- `residual_risk`

## 可执行检查

仓库现在提供：

- `scripts/check_wiki_readable_views.py`

运行方式：

```bash
python3 scripts/check_wiki_readable_views.py scripts/examples/wiki_readable_views_validation_sample.json
```

## 通过标准

检查器通过，只代表：

- 三个阅读视图文件存在
- 必需的索引文件存在
- validation record 满足最小结构合同

不代表：

- 时间线写法已经最优
- artifact grouping 已经覆盖所有旧页
- relation reading 已经等于图谱产品

## 一句话判断

`这个 harness 证明阅读视图 bundle 已经结构成立，不证明阅读体验已经被语义验证。`
