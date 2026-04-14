# Inbox Intake

This page defines how agents should process files dropped into the fixed `inbox/` folder.

## Fixed Entry Point

- Raw landing folder: `inbox/`
- Durable knowledge target: `wiki/`
- Team-level promotion staging: `wiki/team-lore-candidates.md`

## Intake Contract

For each new file under `inbox/`, the agent should produce:

1. A source record or draft destination decision
2. Classification metadata
3. Related page links
4. Any unresolved questions or low-confidence flags

## Required Classification Fields

- `source_path`: original file path under `inbox/`
- `source_type`: note / doc / report / image / attachment / other
- `audience`: self / project / management / team
- `knowledge_level`: working / reusable
- `domain`: likely business topic
- `period`: likely time bucket or `evergreen`
- `suggested_targets`: domain, report, timeline, or candidate pages to update
- `confidence`: high / medium / low

## Routing Rules

### Route To Source Page

Use a source page when the file is raw evidence, upstream input, or external-material capture.

Examples:
- Meeting notes
- Feishu exports
- Screenshots with reporting context
- Supporting attachments

### Route To Report Workflow

Use report linkage when the file is already close to an audience-facing output.

Examples:
- Weekly management update draft
- Monthly summary deck notes
- Review or recap draft

### Route To Team Lore Candidate

Use the candidate list when the material looks reusable across projects but still needs distillation.

Examples:
- Reusable reporting template
- Stable summarization workflow
- Validated pitfall or operating principle

## Confidence Rule

- `high`: clear domain and destination, safe to create or update linked wiki pages
- `medium`: likely classification, but agent should mark assumptions
- `low`: create only a minimal source record and list manual review questions

## Non-Goals

- Do not assume team lore promotion from inbox alone.
- Do not overwrite approved wiki conclusions using newly dropped raw files.
- Do not erase project context during early intake.
