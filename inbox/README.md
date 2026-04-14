# Inbox

Drop raw files here for agent-driven intake.

## Intended Use

- Put newly exported documents, notes, screenshots, or attachments into this folder.
- Keep the original filenames when possible.
- Treat this directory as the landing zone, not the final knowledge location.

## Agent Intake Expectation

When an agent scans this folder, it should:

1. Identify file type and likely source class.
2. Extract enough context to classify audience, domain, and period.
3. Create or update a source page under `wiki/sources/`.
4. Link the source to relevant domain, timeline, and report pages.
5. Add uncertain items to a manual review section instead of guessing.

## Typical Outcomes

- Feishu export or note file -> source page
- Periodic report draft -> report page or report candidate
- Stable method or template -> team lore candidate, not direct promotion

## Guardrails

- Do not delete raw files from `inbox/` automatically.
- Do not write directly into team lore from inbox intake.
- If confidence is low, keep the result in project wiki with `knowledge_level: working`.
