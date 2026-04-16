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

## High-Frequency Principles

- The repo's principle-skills layer lives under `.codex/skills/` and complements, but does not replace, repo governance or workflow skills.
- Any active change that publishes or semantically edits `.codex/skills/` must include `evaluation.md` in the change directory.
- `evaluation.md` is the behavior-proof artifact and must include: `Baseline Scenarios`, `Before Results`, `After Results`, and `Residual Risks`.
- Use `clarify-before-acting` when a request still has material ambiguity and the agent is about to silently choose an interpretation.
- Use `simplicity-first` when the solution is starting to grow speculative abstractions or future-proofing not required by the task.
- Use `surgical-changes` when the edit risks expanding into unrelated cleanup, formatting, or adjacent refactors.
- Use `verify-before-claiming` when the agent is about to say something is complete, fixed, or synced without a fresh check.

## Skill Authoring Contract

- Repo-local `.codex/skills/*` files are English-first behavior assets. Do not let the wiki's Chinese-first policy bleed into `SKILL.md`.
- Keep repo-local `SKILL.md` files compact. Put only trigger conditions, hard rules, anti-patterns, and short loading pointers in the main body.
- Move long examples, templates, or heavy format details into linked `references/` files when they would bloat trigger-time retrieval.
- Before authoring or editing a repo-local skill, read this repo `AGENTS.md` and any repo pages that define delivery boundaries for that workflow.
- If a skill affects Feishu-facing, reader-facing, or other delivery-sensitive outputs, make the repo boundary explicit in the skill or reference the governing repo document directly.

## Archive Review Default

- In this repository, when an OpenSpec change becomes `complete`, the default next action is `archive review`.
- `complete` means stop implementation; it does not mean the change is already archive-ready.
- If archive review finds an ordinary closing tail such as missing sync or final verification, keep the blocker visible in `tasks.md` and explain the reason and next action in git history.
- If archive review depends on scope ambiguity, reusable governance judgment, or context that would be hard to recover from `tasks.md` and git history alone, add `archive-review.md` inside the current change directory.
- Only archive a change after archive review passes.

## Explore Trace Default

- In this repository, every `openspec-explore` run must leave a repo-visible trace in `wiki/ops/` before the exploration continues.
- The trace reuses the existing `intake` page type instead of creating a new page type.
- If the explore request clearly continues the same topic thread, update the existing `wiki/ops/` trace instead of creating a duplicate page.
- The explore trace records the opening context for the topic; it does not replace formal OpenSpec artifacts when the work later becomes a scoped change.
- The explore trace should stay lightweight and capture at least the trigger question, current focus, current hypotheses, open questions, and next step.

## Scope Of Policy

- Repository-default collaboration policy belongs in this repo first, not in global instructions by default.
- Only promote a policy to global guidance when it has been shown to generalize beyond this repository's material-processing workflow.

## Material Processing Default

- Formal material-processing workflow publication uses `.codex/skills/material-collaboration-defaults/SKILL.md`.
- `skills-drafts/` is draft space only; workflow changes cannot stop with an active draft `SKILL.md`.
- Before a workflow-level skill change is complete, every draft skill must be either promoted into `.codex/skills/` or explicitly retired.
- When the user drops materials and asks Codex to process them, do not stop at placeholder intake output.
- Default completion means readable `source` output first, then linked `ops` output when the material contains action signals.
- Ask the user only at real output fork-points, such as whether to update `html/h5/preview` artifacts in addition to wiki records.

## Meeting Note Output

- Formal meeting-note workflow publication uses `.codex/skills/meeting-note-output/SKILL.md`.
- `skills-drafts/meeting-note-output/` is draft space only; it does not count as a formally published repo skill.
- Manual agent role templates are not a substitute for meeting-note workflow routing.
- When handling meeting notes or transcripts, use the repository's fixed meeting-note format rather than a generic summary layout.
- The main meeting-note output must include: meeting metadata, core agenda, numbered topic sections, explicit final/rejected options when applicable, a structured action-item table, and a closing summary.
- Treat note text as the primary output and transcript text as supporting evidence for disputes or rationale.
- Default to a review version first. Review versions must include `待确认` and `需你澄清`.
- Do not publish or sync a final Feishu meeting note until unresolved confirmation items are either answered or explicitly marked as pending.
