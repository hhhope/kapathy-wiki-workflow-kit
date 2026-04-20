## Why

The repository already defines inbox intake, source pages, and project-management handling, but it does not define the default collaboration behavior after the user drops new materials and says "go process them". That gap caused Codex to stop at placeholder intake output instead of producing readable summaries and action extraction.

## What Changes

- Add a formal capability for material-collaboration defaults that defines the default processing chain after new materials arrive.
- Specify that meeting notes, transcripts, weekly reports, attachments, and exported files must produce readable source summaries by default instead of placeholder-only drafts.
- Specify incremental handling rules so previously processed materials are updated or skipped rather than reprocessed in full every time.
- Specify ask-once boundaries so Codex only asks the user when output paths materially diverge, such as whether to update `html/h5/preview` artifacts in addition to wiki pages.

## Capabilities

### New Capabilities
- `material-collaboration-defaults`: Default agent behavior for turning newly dropped materials into readable source records, linked ops outputs, and limited clarification prompts.

### Modified Capabilities
- `ai-report-workflow`: The workflow requirements now need an explicit collaboration-defaults stage between ingestion and summarization.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/material-collaboration-defaults/`.
- Changes the documented workflow for material processing in the repository.
- Establishes the contract for future updates to `scripts/inbox_intake.py`, wiki processing guidance, and repository-local collaboration skills.
