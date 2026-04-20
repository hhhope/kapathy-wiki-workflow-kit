# ADR-0005 Incremental Refresh Over Full Reprocessing

- Status: proposed
- Date: 2026-04-15

## Context

当前仓库已经定义了 intake、source 和项目管理周推进处理，但还没有正式的状态驱动刷新模型。没有这套模型时，agent 很容易退化成“每次都全量重做”。

## Decision

后续设计优先引入增量刷新语义，而不是默认全量重做。

至少要能区分：

- 未整理
- 已整理
- 需刷新
- 已过期 / 可能误导

## Consequences

- 这条 ADR 当前还是 `proposed`
- 需要后续 change 决定具体状态模型放在哪一层以及如何驱动处理
