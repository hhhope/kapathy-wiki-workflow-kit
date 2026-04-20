# 汇报 Wiki 总览

这个 wiki 用来把汇报知识按稳定视角组织起来，让同一份材料可以被重复引用，而不是反复复制。

## 入口视图

- [Domains](domains/index.md)：业务专题与主题知识页
- [Reports](reports/index.md)：按汇报对象组织的产出页与草稿页
- [Timeline](timeline/index.md)：按周期组织的回顾与归档页
- [Sources](sources/index.md)：飞书文档和其他上游证据页
- [Personal Ops](ops/index.md)：个人行为落地、主线、提醒与 Codex handoff

## 推荐流转方式

1. 新材料先进入 `Sources`。
2. 再被整理、归纳并链接到相关 `Domains`。
3. 周期性内容沉淀到 `Timeline`。
4. 面向受众的汇报草稿在 `Reports` 中组装。

## 治理辅助页

- [Role Boundaries](role-boundaries.md)：判断页面是服务当前项目，还是服务团队复用
- [ADR Index](adr/index.md)：项目级稳定决策与治理边界
- [Team Lore Candidates](team-lore-candidates.md)：暂存可能晋升到 team lore 的内容
- [Inbox Intake](inbox-intake.md)：定义 agent 如何扫描并分类 `inbox/` 中的新文件
- [Language Policy](language-policy.md)：定义中文主写、英文分栏的写法规范
- [Examples](examples/index.md)：当前已验证能力的最佳实践样例
- [Agent-Readable Wiki Naming Model](ops/agent-readable-wiki-naming-model.md)：定义演变型页面的对象化命名模型
- [Agent-Readable Wiki Frontmatter](ops/agent-readable-wiki-frontmatter.md)：定义演变型页面的最小结构字段模型
- [Agent-Readable Wiki Graph Extraction](ops/agent-readable-wiki-graph-extraction.md)：定义演变型页面的最小图提取合同
- [Agent-Readable Wiki Relation Analysis](ops/agent-readable-wiki-relation-analysis.md)：定义演变型页面的最小关系分析合同
- [2026-04-20 Agent-Readable Wiki Evolution Timeline](timeline/2026-04-20-agent-readable-wiki-evolution.md)：按时间回看今天这条 wiki 主线如何推进与偏移
- [wiki-readable-views / artifact-grouping-view](ops/agent-readable-wiki-artifact-grouping.md)：按 artifact type 分组查看同类文档
- [wiki-readable-views / relation-reading-view](ops/agent-readable-wiki-relation-reading-view.md)：把 graph / relation 结构结果翻成可读层
- [Agent-Readable Wiki Semantic Scoring](ops/agent-readable-wiki-semantic-scoring.md)：定义演变型页面的最小语义评分合同
- [Agent-Readable Wiki Utilization Layer](ops/agent-readable-wiki-utilization-layer.md)：定义 agent 如何利用这些分析产物
- [Agent-Readable Wiki Runtime Context](ops/agent-readable-wiki-runtime-context.md)：定义 runtime-ready context bundle
- [Agent-Readable Wiki Runtime Context Source Integration](ops/agent-readable-wiki-runtime-context-source-integration.md)：定义 runtime context 如何解析到 repo-local source refs
- [Agent-Readable Wiki Runtime Auto Routing](ops/agent-readable-wiki-runtime-auto-routing.md)：定义 source-integrated runtime 如何转换成阅读顺序
- [Agent-Readable Wiki Context Injection](ops/agent-readable-wiki-context-injection.md)：定义 routing 结果如何转换成 injected-context bundle
- [Agent-Readable Wiki Self-Directed Execution](ops/agent-readable-wiki-self-directed-execution.md)：定义 injected-context 如何转换成 bounded execution plan

## 示例链路

可以从下面几页看一遍基础链路：

- [Feishu weekly sync source](sources/feishu-weekly-sync-sample.md)
- [Account and clearing domain](domains/account-clearing.md)
- [2026 Q2 timeline view](timeline/2026-q2.md)
- [Management weekly operations report](reports/management-weekly-ops.md)
