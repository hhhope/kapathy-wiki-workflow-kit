# Scope Drift 复盘

这页记录一次典型的实施边界偏移：OpenSpec 变更已经完成，但实现继续自然延伸到了下一阶段自动化。

## 发生了什么

- `personal-ops-agent-mvp` 的 OpenSpec 任务已经全部完成
- 变更范围本来停在 wiki 模型、规则、样例链路
- 之后又继续实现了 `scripts/inbox_intake.py` 和相关测试
- 这部分属于“自动化执行层”，已经超出原 change 的任务边界

## 为什么会发生

- 把“自然延伸的小实现”误当成原任务的一部分
- 在 `all_done` 之后没有把“停下并新建下一条 change”当成硬边界
- 原先全局 agent 规则里没有把这种场景写死成禁止项

## 这次学到的判断法

只要出现下面任一情况，就不应该继续挂在原 change 下实现：

- 新增脚本、测试、自动化入口
- 新增执行路径，而不是单纯补文档
- 新增能力不在当前 `proposal / design / tasks` 里
- 虽然很相关，但已经属于下一阶段

一句话判断：

`如果下一步不是在完成当前任务，而是在开始下一段能力，就该停。`

## 已补的全局约束

已经在全局 `~/.codex/AGENTS.md` 增加了 `OpenSpec boundary` 规则，核心要求：

- active change 一旦 `all_done` 或 `tasks.md` 全部勾完，必须立即停止实现
- 不允许继续做 “natural next steps”、自动化延伸、helper script、顺手优化
- 如果用户要继续，必须先创建或选定下一条 OpenSpec change
- 小而相邻的后续工作，也不能静默吸收到已完成 change 中

## 后续操作规范

以后遇到这类情况，固定动作应是：

1. 先确认当前 change 是否已经 `all_done`
2. 如果已完成，只能总结结果，不能继续写代码
3. 把后续想法记成 follow-up
4. 用户确认继续后，先新建下一条 OpenSpec change
5. 再在新 change 下实现

## 周会讨论建议

- 哪些“自然延伸”最容易被误判成原任务的一部分
- 哪些新增文件类型应该被默认视为 scope drift 信号
- 是否要在 repo 层再增加一条 checklist，用于收尾时强制核对“有没有新增脚本/测试/自动化”

## English Notes

Use a separate English summary here only if the team later needs to share this lesson in English.
