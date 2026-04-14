# Personal Ops 总览

这一层不是长期专题知识，而是个人工作流的操作层。

## 页面类型

- `intake`：新输入、新行为、新事件的落地点
- `focus-thread`：当前主线与正在推进的关键主题
- `reminder`：待办、提醒、阻塞和 stale 项
- `codex-handoff`：已经成熟到可以交给 Codex 执行的研发任务

## 当前入口

- [主线面板](main-thread.md)
- [提醒面板](reminders.md)
- [Codex Handoff 规则](codex-handoff-rules.md)

## 样例链路

- [sample-intake](sample-intake.md)
- [sample-focus-thread](sample-focus-thread.md)
- [sample-reminder](sample-reminder.md)
- [sample-codex-handoff](sample-codex-handoff.md)

## 推荐流转

1. 新材料或新行为先进入 intake。
2. agent 判断它是否关联现有主线或待办。
3. 真正需要推进的事项进入 reminder。
4. 明确属于研发执行的待办，再晋升为 Codex handoff。

## 约束

- intake 是入口，不等于主线
- reminder 是动作层，不等于来源页
- Codex handoff 只接收研发任务，不接收泛化待办
