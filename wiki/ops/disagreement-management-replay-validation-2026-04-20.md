---
layer: ops
domain: wiki
ops_area: agent-governance
canonical_object: disagreement-management-replay-validation
artifact_type: method
---

# 分歧管理 Replay 验证 2026-04-20

这页记录在方法正式化之后追加的一轮 replay 验证。

## 本轮选择的分歧类型

- `stage-boundary disagreement`

这轮分歧不是在争：

- `ADR`
- `wiki`
- `TDD`
- 或方法术语本身

而是在争：

- 什么时候该停止继续补 design
- 什么时候该切到 pressure test / TDD
- 怎样避免“便宜地扩 scope”

这是不同于前两轮的第三种分歧形状。

## Replay 字段

- `thread_label`
  - design stop vs validation start
- `disagreement_shape`
  - stage-boundary / scope-boundary disagreement
- `rejected_framing`
  - 把当前问题继续当成 design 扩写
  - 一边分析一边顺手修症状
- `correction_pressure`
  - `不要着急做`
  - `不要再出现便宜个scope的扩散`
  - `先把task确认好一步一步做`
  - `设计做完就做压力测试和TDD`
- `redirection_moment`
  - 讨论从“还要不要继续补定义”转向“什么时候 design 已经够了，应该进入 validation`
- `clarity_state`
  - 在中段并没有新的更深定义缺口，真正缺的是阶段切换边界
- `protected_target`
  - 保护方法设计不被无限延长，强制进入验证面

## RED Baseline

旧的失败方式会是：

- 继续补设计概念
- 再加一层新术语
- 一边说要做 TDD，一边继续停留在 design
- 最后 scope 再次漂移

这类 RED 的问题不在于结论错，而在于：

- 不能及时从“定义问题”切到“验证问题”
- 让 design 成为新的拖延容器

## GREEN Result

这轮 after 行为做对的地方是：

- 明确把 design 视为已足够稳定
- 把接下来工作重排成：
  - pressure scenarios
  - RED/GREEN
  - additional replay / harness validation
- 没再把 runtime automation 或新治理层混进来
- 最终把新工作单独开成 replay / harness validation change，而不是继续塞回上一条已归档 change

## Residual Risks

- 这轮 replay 仍然主要依赖操作者识别“该停设计了”
- 还没有自动标准去判断何时 design 饱和
- 如果未来操作者更偏爱概念工作，仍可能重犯同类漂移

## 本轮结论

这轮 replay 证明了一件额外的事：

`分歧管理方法` 不只适用于“争什么对象”，也适用于“什么时候该停止解释，开始验证”。

这让方法的适用面从：

- governance-shaped disagreement
- method self-compression disagreement

扩到：

- stage-boundary disagreement
