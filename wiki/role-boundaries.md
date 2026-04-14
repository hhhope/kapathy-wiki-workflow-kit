# Role Boundaries

Use roles to decide where content belongs before deciding whether it should enter team lore.

## Who Uses Project Wiki

- Project owner: manages source material, active drafts, period notes, and AI-assisted assembly.
- Project participants: review evidence, contribute context, and refine report outputs inside the project.
- AI assistant: helps classify, summarize, link, and draft based on project-local material.

These pages are usually operational and belong in this repository.

## Who Uses Team Lore

- Team members outside the current project: need reusable methods, templates, principles, and pitfall avoidance.
- Future project owners: need stable guidance without project-specific noise.
- AI assistant at team level: answers cross-project questions from already distilled knowledge.

These pages should only contain content that still makes sense after project details are stripped away.

## Decision Rule

Ask one question first:

`Is this page mainly helping us deliver the current report, or helping others reuse a stable lesson later?`

- Current delivery: keep it in project wiki
- Stable reuse: prepare it for team lore

## Suggested Metadata Meanings

- `audience: self` for personal working notes
- `audience: project` for project participants
- `audience: management` for report consumers
- `audience: team` for cross-project reuse

- `knowledge_level: working` for operational material, sources, drafts, and period pages
- `knowledge_level: reusable` for stable patterns, templates, principles, and validated lessons

## Default Mapping

- Source pages: `project` + `working`
- Timeline pages: `project` + `working`
- Report drafts: `management` or `project` + `working`
- Domain knowledge pages: `project` + `reusable` by default, switch to `team` only after distillation

## Promotion Rule

Do not move a page into team lore just because it is useful once. Promote it only when:

- the conclusion has been validated in real use
- project-only context can be removed without losing meaning
- the result is useful outside this single reporting cycle
- the content fits one of: principle, pitfall, workflow, template, or reusable pattern
