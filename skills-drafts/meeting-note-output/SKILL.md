---
name: meeting-note-output
description: Use when the user asks to整理会议纪要、输出会议纪要文档、同步飞书纪要，或提供会议纪要/逐字稿并 expects a fixed meeting-minutes format rather than a loose summary
---

# Meeting Note Output

## Overview

这个 skill 约束会议纪要的固定输出格式。目标不是“写一个摘要”，而是产出可直接消费的纪要正文。

优先输出会议纪要，不要先写松散的摘要段落。

## When to Use

- 用户说“整理会议纪要”
- 用户给会议纪要、逐字稿、录音转写
- 用户要同步飞书会议纪要文档
- 用户明确嫌当前纪要写法太散、太弱、不可直接发

## Output Contract

会议纪要正文默认使用下面的结构：

1. 会议主题
2. 会议时间
3. 主持人
4. 参会人员
5. 核心议题
6. 分主题正文
7. 待办事项表
8. 总结与后续步骤

如果会上出现方案分歧，正文必须明确：

- 最终方案
- 被否决方案
- 否决原因

## Source Split

- `纪要文本`：主输出，承载结论、风险、待办
- `逐字稿`：补充输出，承载争议点、原始推理和未收敛边界

不要把逐字稿内容原样冲进主纪要。

## Required Sections

从 [`references/meeting-note-format-example.md`](references/meeting-note-format-example.md) 读取示例格式并按其结构组织。

主纪要至少覆盖：

- 会议基本信息
- 核心议题
- 每个主题下的结论与规则
- 风险点
- 待办事项表
- 总结与后续步骤

## Common Mistakes

- 只写“中文摘要”
- 只列 bullet，不形成纪要正文
- 不写被否决方案
- 不把待办整理成表格
- 让逐字稿和纪要写成重复内容
