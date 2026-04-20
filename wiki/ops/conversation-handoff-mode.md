---
canonical_object: conversation-handoff
artifact_type: method
formalizes:
- conversation-handoff
---

# conversation-handoff / method

这页定义什么情况下，agent 不应继续把当前对话当成普通问答，而应切换到“围绕同一北极星持续承接”的工作模式。

## 核心判断

当用户反复把讨论拉回同一个目标时，当前对话就不再只是离散问答，而是一个应被持续承接的话题。

这时候默认动作不是“再答一个局部问题”，而是进入 `handoff mode`。

## 进入 handoff mode 的信号

下面这些信号越多，越说明当前话题应被承接：

- 用户反复纠正当前 framing，把讨论拉回同一个目标
- 用户否掉局部修补，继续强调更大的系统目标
- 用户明确说这件事要记住、要复盘、要形成后续规则
- 话题已经在同一会话里连续讨论超过 2 轮
- 讨论已经从“答案对不对”转成“流程、边界、运行机制该怎么定”

注意：

- `同一话题超过 2 轮` 是强信号
- 但不是唯一信号
- 真正更高优先级的判断是：用户是否持续把对话拉回同一个北极星

## handoff mode 至少要维护什么

进入 handoff mode 后，agent 至少要持续维护这些槽位：

- `north_star`
  - 当前反复牵引讨论的目标
- `constraints`
  - 当前边界、不能做什么、希望保留什么
- `failure_modes`
  - 用户最不能接受的失败方式
- `preferences`
  - 当前暴露出来的协作偏好
- `disagreements`
  - 当前仍在争论的流程、边界或定义问题
- `open_questions`
  - 还没收口的关键问题
- `candidate_practices`
  - 讨论里浮现的候选规则、候选最佳实践
- `repo_targets`
  - 当前话题最终应该沉淀到哪里

## repo 落点边界

handoff mode 不等于所有内容都进同一种记录。

默认边界：

- `trace / intake`
  - 话题已经明确打开，需要 ops 层连续承接
- `retro`
  - 话题暴露了规则漂移、执行落空、流程争论、反复纠偏
- `ADR`
  - 话题已经形成稳定决策，应该跨 change 保留
- `OpenSpec change`
  - 话题已经变成 scoped workflow / implementation 变更
- `archive-review.md`
  - 话题专门在讨论某个当前 change 是否 archive-ready

## 第一版非目标

第一版 handoff mode 不做这些事：

- 不自动改 `.codex/skills/*`
- 不自动改 `AGENTS.md`
- 不自动把所有反复话题升级成 `ADR`
- 不承担整个 `archive review` gate
- 不替代正式的 `proposal / design / tasks`

## 一句话判断

`只要用户在当前会话里反复把讨论拉回同一个目标，系统就应该知道这已经不是普通聊天，而是一个需要持续承接的话题。`
