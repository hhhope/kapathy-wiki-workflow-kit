# AI Workflow

这个仓库把“长期知识”与“AI 辅助产物”分开管理。AI 可以帮助整理和起草，但最终结论和正式汇报仍然需要人工确认。

## 角色边界

- 项目 owner 用这套 wiki 管来源页、草稿页、周期页和汇报组装过程
- 团队成员只消费已经提炼过、可复用的稳定知识
- AI 在两侧都能参与，但项目 wiki 面向生产过程，team lore 面向复用结果

## 流程阶段

### 1. Ingestion

- 扫描固定 `inbox/` 目录中的新文件
- 将飞书文档或外部材料登记为本地来源页
- 对明显属于个人工作流输入的材料，生成 `intake` 记录而不是只生成来源页
- 记录来源链接、来源类型、owner 提示和同步状态
- 即使正文还留在外部系统，来源页也要保持可用
- 如果置信度低，只创建最小记录并列出待确认问题

### 1.5 Collaboration Defaults

- 当用户把材料交给 Codex 并说“去处理”时，默认不是只做 intake 占位，而是继续完成最小可读整理
- 默认先建或更新 `source`，并补真正的中文摘要、关键结论、风险和待办
- 如果材料里已经有明确动作、owner、截止时间或阻塞项，默认继续补 `intake / reminder`
- 对同一批材料采用增量处理：已整理的页面优先更新，不做每次全量重跑
- 不要反复向用户确认基础流程；只有在输出形态明显分叉时才问一次
- 典型分叉点是：是否需要同时更新 `html / h5 / preview` 这类可视化文件本体，而不只是同步 wiki 结论

### 2. Summarization

- 从来源页或原始材料生成中文摘要
- 把摘要写入来源页或汇报页，并明确标注 AI 生成
- 保留足够上下文，说明这份来源为什么重要

### 3. Linking

- 把来源页关联到相关的 domain、report 和 timeline 页面
- 把 intake 记录关联到 focus-thread、reminder 和需要的 source 页面
- 优先使用链接和摘要，不复制大段原文
- 当某个结论不再依赖具体周期时，把它提升到 domain 页面

### 4. Draft Assembly

- 基于来源页、主题页和周期页组装汇报草稿
- 汇报页要面向明确受众
- AI 起草内容必须保留独立审阅位置

### 4.5 Focus And Reminder

- 从 intake 和未完成事项中抽取当前主线
- 把真正需要推进的动作提升成 reminder
- 仅当事项已经是研发任务时，再生成 Codex handoff

### 5. Review

- 由人工判断 AI 摘要和草稿是否可靠
- 审核通过的结论进入长期页面
- 被否定或过时的 AI 内容要修订或删除，不能静默继承

## 未来自动化最小元数据

- `source_path`
- `source_type`
- `type`
- `domain`
- `audience`
- `knowledge_level`
- `language`
- `period`
- `source_links`
- `status`
- `updated_at`
- `ai_generated`

## 第一批自动化目标

- `inbox/` 扫描与 intake 助手
- 来源页自动登记助手
- 来源页中文摘要助手
- 周报和月报草稿组装助手
- team lore 候选晋升助手
