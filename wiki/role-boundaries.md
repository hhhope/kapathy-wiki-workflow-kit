# Role Boundaries

用“角色”来判断内容该留在项目 wiki，还是进入 team lore，而不是先按仓库位置去想。

## 谁使用项目 Wiki

- 项目 owner：管理来源材料、草稿、周期页和 AI 辅助整理结果
- 项目参与者：查看证据、补充上下文、修正汇报输出
- AI 助手：基于项目内材料做分类、摘要、关联和草稿生成

这一层通常是工作层，允许保留操作性内容和阶段性内容。

## 谁使用 Team Lore

- 当前项目之外的团队成员：需要复用方法、模板、原则和坑点
- 未来的项目 owner：需要不依赖当前项目背景的稳定经验
- 团队级 AI 助手：回答跨项目的复用型问题

这一层只能放去项目化之后仍然成立的内容。

## 判断规则

先问一句：

`这页主要是在帮助当前交付，还是在帮助别人以后复用？`

- 服务当前交付：留在项目 wiki
- 服务后续复用：进入 team lore 候选流程

## 元数据建议含义

- `audience: self` 表示个人工作笔记
- `audience: project` 表示项目参与者
- `audience: management` 表示汇报消费方
- `audience: team` 表示跨项目复用对象

- `knowledge_level: working` 表示工作材料、来源页、草稿页、周期页
- `knowledge_level: reusable` 表示稳定模式、模板、原则、已验证经验

## 默认映射

- 来源页：`project + working`
- 周期页：`project + working`
- 汇报草稿：`management` 或 `project` + `working`
- 主题知识页：默认 `project + reusable`，提炼后才考虑切到 `team`

## 晋升规则

不要因为“看起来有用”就直接放进 team lore。只有满足下面条件才进入晋升：

- 结论已经在真实工作里验证过
- 去掉项目私有背景后仍然成立
- 能服务当前周期之外的复用
- 能归入 `principle / pitfall / workflow / template / pattern` 之一
