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
- [ADR-0007 Retire Draft Skills As Runtime Surface](0007-retire-draft-skills-as-runtime-surface.md)

## 非目标

- 不把所有 `design.md` 都复制成 ADR
- 不把复盘页当 ADR
- 不直接把项目 ADR 写进 team lore
