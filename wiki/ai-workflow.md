# AI Workflow

This repository separates durable knowledge from AI-generated assistance. AI can help prepare content, but final knowledge and report output still require human review.

## Role Boundary

- Project owners use this wiki as a working layer for sources, drafts, period pages, and active report assembly.
- Team members should consume only reusable knowledge that has been distilled out of project-specific material.
- AI helps in both places, but the project wiki is for production work while team lore is for proven, reusable patterns.

## Workflow Stages

### 1. Ingestion

- Register a Feishu or external document as a local source page.
- Record source link, source class, owner hint, and sync state.
- Keep the source valid even when the body remains external.

### 2. Summarization

- Generate a short AI summary from the source page or source body.
- Store the result inside the source or report page with clear AI labeling.
- Preserve enough context to understand why the source matters.

### 3. Linking

- Connect the source page to relevant domain, report, and timeline pages.
- Prefer links and summaries over duplicated raw content.
- Promote stable knowledge into domain pages when it stops being period-specific.

### 4. Draft Assembly

- Build report drafts from upstream source, domain, and timeline pages.
- Keep draft pages audience-specific.
- Mark AI-drafted sections clearly and leave a review checkpoint.

### 5. Review

- Human reviewers decide whether AI summaries and drafts are accurate enough to retain.
- Approved conclusions stay in durable pages.
- Rejected or stale AI text should be revised or removed instead of being silently inherited.

## Minimum Metadata For Future Automation

- `type`
- `domain`
- `audience`
- `knowledge_level`
- `period`
- `source_links`
- `status`
- `updated_at`
- `ai_generated`

## First Automation Targets

- Feishu source registration helper
- Summary generation helper for source pages
- Draft assembly helper for weekly and monthly reports
- Candidate promotion helper for team lore handoff
