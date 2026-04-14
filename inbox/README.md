# Inbox

把原始文件放到这里，供 agent 自动 intake。

## 用途

- 新导出的文档、笔记、截图、附件统一先放进这个目录
- 尽量保留原始文件名
- 这里是投递区，不是最终知识落点

## Agent Intake 预期

当 agent 扫描这个目录时，应该：

1. 识别文件类型和可能的来源类别
2. 提取足够上下文来判断 audience、domain 和 period
3. 在 `wiki/sources/` 下创建或更新来源页
4. 把来源页关联到相关的 domain、timeline 和 report 页面
5. 对低置信度内容输出待人工确认项，而不是强行猜测

## 常见去向

- 飞书导出或会议笔记 -> source 页面
- 周报或月报草稿 -> report 页面或 report 候选
- 稳定方法或模板 -> team lore candidate，而不是直接晋升

## Guardrails

- 不要自动删除 `inbox/` 中的原始文件
- 不要从 intake 直接写入 team lore
- 如果置信度低，先留在项目 wiki，并标记 `knowledge_level: working`
