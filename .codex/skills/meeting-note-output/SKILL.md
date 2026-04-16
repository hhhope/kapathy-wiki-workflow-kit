---
name: meeting-note-output
description: Use when the user asks to整理会议纪要、输出会议纪要文档、同步飞书纪要，或提供会议纪要、逐字稿、录音转写并 expects a fixed meeting-minutes output rather than a loose summary.
---

# Meeting Note Output

## Overview

把会议材料变成可直接审阅和投放的会议纪要正文，不要退化成散乱摘要。

核心原则：

- 主纪要是主输出，逐字稿是补充证据
- 默认先出审阅版
- repo 内长期来源页和飞书审阅版要保持同一正文结构

## When to Use

适用于这些场景：

- 用户说“整理会议纪要”
- 用户给会议纪要、逐字稿、录音转写
- 用户要同步飞书会议纪要文档
- 用户明确嫌当前纪要写法太散、太弱、不可直接发

不适用于：

- 普通项目管理周报
- 不需要正文，只要留档一条 source 摘要
- 没有会议语境的普通文档整理

## Review-First Rule

- 默认先出审阅版
- 审阅版必须包含 `待确认` 和 `需你澄清`
- 未确认前，不直接发布正式飞书纪要
- 用户在聊天里按编号回复澄清项后，再覆盖正式版

## Main Output Contract

主纪要正文至少包含：

1. 会议主题
2. 会议时间
3. 主持人
4. 参会人员
5. 核心议题
6. 分主题正文
7. 待办事项表
8. 待确认
9. 需你澄清
10. 总结与后续步骤

如果会上存在方案分歧，正文必须明确：

- 最终方案
- 被否决方案
- 否决原因

如果材料强度不一致，必须显式区分：

- 原文明确
- 交叉支持
- 归纳判断
- 待确认

格式示例见：

- [meeting-note-format-example.md](references/meeting-note-format-example.md)

## Source Split

- `纪要文本`：主输出，承载结论、风险、待办
- `逐字稿`：补充输出，承载争议点、原始推理和未收敛边界

不要把逐字稿原文直接冲进主纪要。

## Delivery Order

默认顺序：

1. 先识别会议主题、时间、参会人和核心议题
2. 产出固定结构的审阅版正文
3. 在 repo 中更新对应 `wiki/sources` 纪要页
4. 如用户要求或该流程默认包含飞书纪要交付，再创建或更新飞书审阅版
5. 保持飞书审阅版与 repo 主纪要正文一致

## Repo Pattern

当前 repo 的固定约束：

- [AGENTS.md](../../../AGENTS.md)
- [会议纪要来源页模板](../../../wiki/templates/meeting-note-source-template.md)

参考样例：

- [20260415100517-转写-yan的快速会议-纪要文本-1.md](../../../wiki/sources/20260415100517-转写-yan的快速会议-纪要文本-1.md)
- [20260415100517-转写-yan的快速会议-逐字稿文本-1.md](../../../wiki/sources/20260415100517-转写-yan的快速会议-逐字稿文本-1.md)

## Common Mistakes

- 只写“中文摘要”
- 只列 bullets，不形成纪要正文
- 把 `Source Metadata`、`Reused By`、`English Notes` 这类 wiki 辅助段当作飞书主纪要正文
- 不写被否决方案
- 不把待办整理成表格
- 让逐字稿和纪要写成重复内容
- 只更新 repo，不补飞书审阅版
- 未列出 `待确认` 和 `需你澄清` 就直接发正式版
