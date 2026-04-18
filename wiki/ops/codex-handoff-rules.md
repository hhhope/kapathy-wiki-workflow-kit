# Codex Handoff 规则

这页定义什么样的提醒可以升级为 Codex handoff，以及升级后应保留哪些上下文。

## 升级前提

一条 reminder 只有同时满足下面条件，才可以升级：

- 它明确属于研发任务，而不是普通跟进事项
- 目标已经清楚，不是泛泛想法
- 至少有一个来源或主线可以回溯
- 有最小验收提示，能判断 Codex 做完没有

## 不应升级的情况

- 只是提醒自己“再想想”
- 还没有明确要改什么
- 没有任何来源或上下文链接
- 实际上是运营、沟通或管理动作，不是研发执行

## 升级动作

1. 从 reminder 中提炼任务标题
2. 补齐目标、背景、验收提示
3. 链接相关 reminder、source、focus thread
4. 设置 `handoff_state`
5. 明确是否已 ready，可以交给 Codex

## 状态定义

- `draft`：还没补齐上下文
- `ready`：上下文和验收提示已足够，可交付 Codex
- `dispatched`：已经正式派发给 Codex
- `completed`：执行完成并回写结果

## 与普通提醒的边界

- reminder 关注“该不该推进”
- Codex handoff 关注“如何把研发执行交出去”

## English Notes

如需保留英文任务描述或术语，单独放在 handoff 页面自身的英文附录区块。
