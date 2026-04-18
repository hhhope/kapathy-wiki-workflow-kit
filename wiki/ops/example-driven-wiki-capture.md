# 例子驱动的 Wiki 留痕

这页定义什么情况下，agent 不应只停在“分析了一个外部例子”，而应把已经提炼出的学习结果写成 repo-visible 记录。

## 核心判断

如果用户给了外部 repo、README、文章，或者直接在聊天里给了具体例子，而且对话已经提炼出可复用的做法、修改点或缺口，那么默认动作不是停在聊天总结，而是写一条 wiki 记录。

关键不在“有没有链接”，而在“有没有已经提炼出的可复用学习”。

## 触发条件

下面这些组合出现时，默认进入例子驱动留痕：

- 有外部 repo / README / 文章 / 明确例子
- 对话已经明确了：
  - 我们复用了什么
  - 我们改了什么
  - 我们没接受什么，或者还没 formalize 什么
  - 下一步是什么

## 最小记录字段

例子驱动的学习记录至少要保留：

- `time`
- `source`
- `what_reused`
- `what_modified`
- `what_not_formalized`
- `repo_target`
- `next_step`

推荐补充：

- 原话摘录
- 这件事为什么影响当前 repo
- 后续是否值得晋升成 skill、template、ADR 或 team lore 候选

## 路由边界

不是所有例子驱动记录都落到同一层。

默认边界：

- `wiki/ops`
  - 例子影响了当前 repo 的 workflow、governance、运行方式
- `wiki/examples`
  - 例子更像验证过的输出样例，未来要复用其产出形状
- `wiki/team-lore-candidates.md`
  - 项目页已经写好，而且看起来具备跨项目复用潜力

## 默认动作

如果路线已经清楚，agent 应在同一轮中完成留痕，而不是等用户再补一句“写进 wiki”。

## 非目标

第一版不做这些事：

- 不为每个外部链接都新建页面
- 不自动把例子学习升级成 skill
- 不自动把例子学习升级成 template
- 不绕过项目 wiki 直接写 team lore
