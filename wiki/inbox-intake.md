# Inbox Intake

这页定义 agent 应如何处理放进固定 `inbox/` 目录的文件。

## 固定入口

- 原始投递目录：`inbox/`
- 项目内长期知识层：`wiki/`
- team lore 晋升缓冲区：`wiki/team-lore-candidates.md`

## Intake 契约

对于 `inbox/` 中的每一个新文件，agent 至少要产出：

1. 一个来源页或目标去向判断
2. 一组分类元数据
3. 相关页面链接建议
4. 低置信度时的待确认问题

## 必填分类字段

- `source_path`：文件在 `inbox/` 下的原始路径
- `source_type`：`note / doc / report / image / attachment / other`
- `audience`：`self / project / management / team`
- `knowledge_level`：`working / reusable`
- `domain`：推测的业务主题
- `period`：推测的时间周期，或 `evergreen`
- `suggested_targets`：建议关联的 domain、report、timeline 或 candidate 页面
- `confidence`：`high / medium / low`
- `language`：默认 `zh-CN`，如果原文主要是英文，也要先产出中文摘要

## 路由规则

### 路由到 Source 页面

当文件属于原始证据、上游输入或外部材料留痕时，优先进入来源页。

典型例子：
- 会议纪要
- 飞书导出文档
- 与汇报有关的截图
- 支撑材料附件

### 路由到 Report 流程

当文件已经接近面向受众的汇报输出时，优先进入 report 组装流程。

典型例子：
- 管理层周报草稿
- 月度总结提纲
- 复盘草稿

### 路由到 Team Lore Candidate

当材料看起来具有跨项目复用价值，但还没有提炼完成时，先进入候选池。

典型例子：
- 可复用汇报模板
- 稳定的总结流程
- 已验证的坑点或原则

## 置信度规则

- `high`：主题和目标位置清晰，可以安全创建或更新 wiki 页面
- `medium`：大致可判断，但要显式标注假设
- `low`：只创建最小来源记录，并列出待人工确认项

## 语言规则

- wiki 主内容以中文为准。
- 英文材料先生成中文摘要，再决定是否保留英文独立附录。
- 不要把英文原文直接混写进中文摘要段落。
- 如需保留英文原文，放到独立的 `English Notes` 或 `原文摘录` 区块。

## 非目标

- 不要仅凭 `inbox/` 文件就直接写入 team lore。
- 不要用新投递的原始文件覆盖已经确认过的 wiki 结论。
- 不要在 intake 阶段过早抹掉项目上下文。
