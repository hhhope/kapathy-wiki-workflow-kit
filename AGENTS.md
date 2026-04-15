# Repo Instructions

This file adds repository-specific constraints for `report-wiki-portfolio`.

## OpenSpec Trigger

- Treat changes to repository-default workflow, collaboration behavior, routing defaults, escalation boundaries, or default output rules as OpenSpec-level changes.
- For these changes, create or select an active OpenSpec change before editing `wiki/`, `scripts/`, `skills-drafts/`, or other repository guidance files.
- Do not ship temporary wiki-only or skill-draft-only fixes first and backfill OpenSpec later.
- If the user asks to change how Codex should usually behave in this repository, assume it is a workflow change unless the request is explicitly limited to one page or one one-off run.

## Decision Observability

- For workflow-level changes, record stable decisions in `wiki/adr/` rather than leaving the rationale only in chat history.
- If the work is interrupted, blocked, or leaves an unresolved branch, write a checkpoint note in the active change artifacts or linked repo guidance before stopping.
- A valid checkpoint must state:
  - what was decided
  - what is still open
  - what the next action is
- Do not claim a future “tighter process” unless the new constraint is written into repo-visible artifacts.
- OpenSpec change artifacts still own current scope, task progress, and interruption checkpoints; `wiki/adr/` owns stable project decisions.

## Scope Of Policy

- Repository-default collaboration policy belongs in this repo first, not in global instructions by default.
- Only promote a policy to global guidance when it has been shown to generalize beyond this repository's material-processing workflow.

## Material Processing Default

- When the user drops materials and asks Codex to process them, do not stop at placeholder intake output.
- Default completion means readable `source` output first, then linked `ops` output when the material contains action signals.
- Ask the user only at real output fork-points, such as whether to update `html/h5/preview` artifacts in addition to wiki records.

## Meeting Note Output

- When handling meeting notes or transcripts, use the repository's fixed meeting-note format rather than a generic summary layout.
- The main meeting-note output must include: meeting metadata, core agenda, numbered topic sections, explicit final/rejected options when applicable, a structured action-item table, and a closing summary.
- Treat note text as the primary output and transcript text as supporting evidence for disputes or rationale.
