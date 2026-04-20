# 分歧管理 Replay Harness

这页不是新的 runtime 规则，而是一个可复用的验证框架。

用途只有一个：

当仓库想验证“分歧管理方法”是否真的保住了校准价值时，用同一组字段去 replay 一段真实分歧。

## 适用边界

适用于：

- 流程级分歧
- 目标校准型分歧
- 方法自身可能变成压缩器的分歧
- 阶段边界或 scope 边界分歧

不适用于：

- 纯事实问答
- 没有明显纠偏压力的普通讨论
- 只剩结论、已经没有可回放过程的材料

## 最小 Replay 字段

每次 replay 至少保留：

- `thread_label`
- `disagreement_shape`
- `rejected_framing`
- `correction_pressure`
- `redirection_moment`
- `clarity_state`
- `protected_target`
- `red_baseline`
- `green_result`
- `residual_risk`

## 可执行检查

仓库现在提供了一个最小可执行检查器：

- `scripts/disagreement_replay_check.py`

它做的不是语义理解，而是结构校验。

它会检查：

- 必填字段是否存在
- 字段类型是否符合最小 replay 合同
- 4 个必需 pass-condition 是否显式存在且为 `true`

运行方式：

```bash
python3 scripts/disagreement_replay_check.py scripts/examples/disagreement_stage_boundary_replay.json
```

这个脚本通过，只代表：

- replay 记录满足了最小可执行合同

不代表：

- 底层分歧已经被自动语义验证
- rollout proof 已经成立

## 通过标准

一次 replay 只有同时满足下面这些，才算通过：

1. 比基线多保住了分歧的演变，而不只是终点结论
2. 没把更漂亮的方法语言误当成更高保真度
3. 仍然允许 `I haven't seen it clearly yet`
4. 明确写出 replay proof 不是 rollout proof

## 常见失败方式

- 太快总结，只剩 endpoint
- 把治理解释当成主问题
- 把更高层抽象当成自动更优
- 为了套 harness 字段而重塑原始材料

## 一句话判断

`Replay harness 的作用不是证明方法很漂亮，而是证明它比旧 framing 少丢了多少校准价值。`
