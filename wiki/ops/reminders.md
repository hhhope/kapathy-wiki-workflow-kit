# 提醒面板

这页只保留可执行提醒，不等于原始输入列表。

## 使用规则

- 一条提醒必须有明确动作，不能只是模糊想法
- 一条提醒至少关联一个主线、intake 或来源页
- stale 项需要显式标记，不能静默堆积
- 不是研发任务的事项，不要直接升级成 Codex handoff

## 当前提醒

### 补齐个人操作系统样例链路

- 状态：open
- 优先级：high
- 下一步：创建 intake、focus-thread、reminder、codex-handoff 的样例记录
- 关联主线：[主线面板](main-thread.md)
- stale 状态：fresh
- 是否适合升级为 Codex 任务：no

### 设计研发任务派发规则

- 状态：open
- 优先级：medium
- 下一步：明确什么条件下 reminder 可以升级成 Codex handoff
- 关联主线：[主线面板](main-thread.md)
- stale 状态：fresh
- 是否适合升级为 Codex 任务：yes，前提是上下文和验收标准已经明确

## Stale 区

当提醒满足以下任一条件时，应进入 stale 视图：

- 长时间没有进展
- 已经失去关联主线
- 内容不清楚，无法继续执行

## English Notes

如果需要保留英文提醒说明，放在独立附录里。
