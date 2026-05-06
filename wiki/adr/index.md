# ADR Index

这层记录项目级稳定决策，不记录一次性任务过程，也不记录事件日志。

## 使用边界

- `OpenSpec change`：记录本次变更做什么、怎么做、做到哪
- `ADR`：记录跨 change 仍然成立的稳定决策
- `Retro / logs`：记录偏差、失败、事件和复盘证据

## 当前 ADR

- [ADR-0001 Repository-Default Workflow Changes Require OpenSpec](0001-repository-default-workflow-changes-require-openspec.md)
- [ADR-0002 Stable Decisions Live In Wiki ADR](0002-stable-decisions-live-in-wiki-adr.md)
- [ADR-0003 Retros Stay Separate From ADRs](0003-retros-stay-separate-from-adrs.md)
- [ADR-0004 Agent Self-Evolution Over Skill Governance](0004-agent-self-evolution-over-skill-governance.md)
- [ADR-0005 Incremental Refresh Over Full Reprocessing](0005-incremental-refresh-over-full-reprocessing.md)
- [ADR-0006 Formal Project-Local Skills Over Draft Skill Docs](0006-formal-project-local-skills-over-drafts.md)
- [ADR-0007 Archive Review Before Archive](0007-archive-review-before-archive.md)
- [ADR-0008 Human Governance Before Self-Evolution Promotion](0008-human-governance-before-self-evolution-promotion.md)
- [ADR-0026 Retire Draft Skills As Runtime Surface](0026-retire-draft-skills-as-runtime-surface.md)
- [ADR-0027 Repo Phase0 Before Repo AGENTS Migration](0027-repo-phase0-before-repo-agents-migration.md)
- [ADR-0009 Explore Trace Before OpenSpec Explore](0009-explore-trace-before-openspec-explore.md)
- [ADR-0010 Shared Skill Authoring Contract Before Repo-Local Overrides](0010-shared-skill-authoring-contract-before-repo-local-overrides.md)
- [ADR-0011 Canonical AI Chat Installer Source With Platform Adapters](0011-canonical-ai-chat-installer-source-with-platform-adapters.md)
- [ADR-0012 Disagreement Management Before Conclusion Promotion](0012-disagreement-management-before-conclusion-promotion.md)
- [ADR-0013 Agent-Readable Wiki Naming Before Graph Growth](0013-agent-readable-wiki-naming-before-graph-growth.md)
- [ADR-0014 Agent-Readable Wiki Frontmatter Before Graph Automation](0014-agent-readable-wiki-frontmatter-before-graph-automation.md)
- [ADR-0015 Agent-Readable Wiki Graph Extraction After Structure](0015-agent-readable-wiki-graph-extraction-after-structure.md)
- [ADR-0016 Agent-Readable Wiki Relation Analysis After Extraction](0016-agent-readable-wiki-relation-analysis-after-extraction.md)
- [ADR-0017 Agent-Readable Wiki Semantic Scoring After Relation Analysis](0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md)
- [ADR-0018 Agent-Readable Wiki Utilization Layer After Semantic Scoring](0018-agent-readable-wiki-utilization-layer-after-semantic-scoring.md)
- [ADR-0019 Agent-Readable Wiki Runtime Context After Utilization](0019-agent-readable-wiki-runtime-context-after-utilization.md)
- [ADR-0020 Agent-Readable Wiki Runtime Context Source Integration After Runtime Context](0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md)
- [ADR-0021 Agent-Readable Wiki Runtime Auto Routing After Source Integration](0021-agent-readable-wiki-runtime-auto-routing-after-source-integration.md)
- [ADR-0022 Agent-Readable Wiki Context Injection After Runtime Auto Routing](0022-agent-readable-wiki-context-injection-after-runtime-auto-routing.md)
- [ADR-0023 Agent-Readable Wiki Self-Directed Execution After Context Injection](0023-agent-readable-wiki-self-directed-execution-after-context-injection.md)
- [ADR-0024 Live Conversation Re-Anchor Before Continued Implementation](0024-live-conversation-reanchor-before-continued-implementation.md)
- [ADR-0025 Readable Views Before Further Runtime Expansion](0025-readable-views-before-further-runtime-expansion.md)
- [ADR-0028 Root AGENTS Archive-Review Semantics Stay as Generic Top-Level Rules With Repo-Owned Detail](0028-root-agents-archive-review-generic-with-repo-detail.md)
- [ADR-0029 Intake Retractions Are Legitimate With Explicit Reopen Triggers](0029-intake-retractions-legitimate-with-reopen-triggers.md)

## 非目标

- 不把所有 `design.md` 都复制成 ADR
- 不把复盘页当 ADR
- 不直接把项目 ADR 写进 team lore
