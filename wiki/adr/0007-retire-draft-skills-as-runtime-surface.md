# ADR-0007 Retire Draft Skills As Runtime Surface

- Status: accepted
- Date: 2026-04-16

## Context

仓库已经确认 `.codex/skills/` 才是项目级正式 skill 的发布面，但 `skills-drafts/` 里仍然保留了活的 `SKILL.md` 文件。这会继续制造一种错误信号：看起来仓库“已经有这个 skill”，但 future session 并不会把 draft 路径当成正式可用能力。

仅靠聊天说明或局部 AGENTS 文案不够，因为问题不是“有没有写流程”，而是“发布面是否唯一且可验证”。

## Decision

本仓库后续采用更硬的约束：

- `skills-drafts/` 不再承载活的运行时 `SKILL.md`
- workflow-level skill change 完成前，草稿 skill 必须二选一：
  - 正式发布到 `.codex/skills/<skill-name>/SKILL.md`
  - 明确退役，不再宣称可复用
- 不能同时长期保留一个正式 skill 和一个同名 draft `SKILL.md` 作为双发布面

## Consequences

- `skills-drafts/` 可以继续作为探索或设计目录，但不能再被误认成上线能力
- future session 的 repo-local workflow 复用只认 `.codex/skills/`
- OpenSpec 验收需要检查两件事：
  - 正式 skill 已发布
  - draft `SKILL.md` 已迁移或退役
