---
layer: ops
domain: wiki
ops_area: learning-capture
canonical_object: example-driven-wiki-capture
artifact_type: method
---

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

## 过程校准：Anthropic prompt engineering gate（2026-05-05）

### time

2026-05-05

### source

- `https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering`
- `https://platform.claude.com/docs/en/test-and-evaluate/define-success`

### process

本轮先把 Anthropic prompt engineering 文档抽成一个候选判断：

> 改 behavior asset 前，先说明成功标准、失败样例和验证方法；如果问题不受规则/提示词控制，不要通过改 governance 文本解决。

初始处理只把这个判断写进
`openspec/changes/decide-root-governance-alignment/evaluation.md`，没有同步进入
wiki。用户指出“学了东西也没进 wiki”“这个过程也没进”，暴露了一个执行偏差：

- `evaluation.md` 可以证明 active change 内部做过验证；
- 但只写 `evaluation.md` 不等于完成 example-driven capture；
- 当对话已经抽出可复用学习时，wiki 仍然需要保留 source、取舍、未形式化内容和下一步。

### what_reused

复用 Anthropic 的前置门槛：先有 success criteria、empirical tests、初版 prompt，再做 prompt engineering。映射到本仓库，就是先证明问题可由 behavior wording 控制，再改 `AGENTS.md`、`rules/` 或 `skills/`。

### what_modified

没有把 Anthropic 文档直接升级成仓库规则；只把它改写成当前治理设计的候选 review heuristic，并先放在 active change 的 evaluation 里验证。

### what_not_formalized

- 没有新建单独的 Anthropic wiki 页面；
- 没有把 heuristic 写进 `spec.md SHALL`；
- 没有改 root dotfiles、repo `AGENTS.md`、`rules/` 或 `skills/`；
- 没有把它提升成 method、ADR 或 skill。

### repo_target

- 当前 evidence：`openspec/changes/decide-root-governance-alignment/evaluation.md`
- 当前 wiki 留痕：本节
- 后续若继续验证：可进入 behavior-asset governance 的 method / rule / skill 候选，但必须另走 OpenSpec 或 archive review。

### next_step

下一次遇到外部参考时，执行顺序应是：

1. 先判断是否已经抽出可复用学习；
2. 如果只是原始链接，不新建 wiki；
3. 如果已经抽出学习，至少更新对应 `wiki/ops` 记录；
4. 如果还需要验证，把验证证据放进 active change 的 `evaluation.md`；
5. 最终回复必须同时说明：wiki 落点、验证落点、尚未形式化的内容。

## 过程校准：cross-agent meta-review loop（2026-05-05）

### time

2026-05-05

### source

- 本轮对话中的 Claude 验证方法推荐
- 本轮对话中的 Codex review brief 草稿
- `openspec/changes/decide-root-governance-alignment/evaluation.md`
- `wiki/ops/behavior-asset-governance-design-trace.md` §13

### process

本轮出现了一个二阶偏差：原本要验证的是 `behavior-asset abstraction routing`，但验证问题一度把真实需求压缩成 `skill gate`。用户要求用另一个 agent 做背靠背复核，先检查推荐本身，再检查修正是否如实落入 `evaluation.md`。

审计链：

1. Claude 给出验证方法和 Codex review brief。
2. Codex 复核后给出五项判决：`PARTIAL / FAIL / PARTIAL / PASS / PARTIAL`，总体忠实度为中。
3. Claude 将偏差和修正写入 `evaluation.md` 的 `Skill-gate vs. Abstraction-routing Meta-review` 小节。
4. Codex 再次复核落盘内容，五项均为 `FAITHFUL`，落盘忠实度为高。

### what_reused

复用的是交叉复核流程：先审查推荐是否偏离目标，再审查修正是否忠实落盘。该流程保护的不是某条具体规则，而是防止 agent 在验证阶段把 `behavior-asset abstraction routing` 偷换成单一 `skill` 出口。

### what_modified

把原来的 skill-subject 验证口径改成 routing-subject 口径：

- 回溯样本从“最近写过的 skill”改成“最近被注意到的重复行为”；
- 前向触发从“我要写 skill”改成“我遇到重复行为”；
- 验收轴从“是否帮助决定 skill”改成“是否能在 root / repo / rules / skills / wiki / ADR / OpenSpec / do-not-sink 之间分流”。

### what_not_formalized

- 没有把 `do-not-sink` 写成已接受的 Pattern Catalog 第八类；
- 没有新增 checklist、rule、skill 或 method；
- 没有修改 `design.md`、`spec.md` 或 design trace 正文；
- 没有拍板 D1 / D2 / D3。

### repo_target

- 当前 evidence：`openspec/changes/decide-root-governance-alignment/evaluation.md`
- 当前 wiki 留痕：本节
- 受保护边界：`wiki/ops/behavior-asset-governance-design-trace.md` §13 anti-drift

### next_step

后续如果继续验证当前治理设计，问题主语必须是“重复行为如何分流”，不是“是否要写 skill”。若再出现 skill-subject 验证题，先按本节审计链复核目标是否被偷换，再决定是否进入 `evaluation.md`。
