## Context

This repository already has rules for `inbox/` routing, source pages, ops escalation, and project-management weekly handling. What it lacks is a stable collaboration contract for the common case where the user drops materials into the repo and expects Codex to process them without re-confirming the whole workflow.

The recent failure mode was not classification. It was stopping too early:

- intake pages were created with placeholder summary text
- source pages were created without actual extracted conclusions
- the user had to re-explain that "processing" should include real summarization and action extraction

This is a cross-cutting workflow change because it affects:

- inbox intake behavior
- source summarization expectations
- ops escalation defaults
- future visual-material handling for `html/h5/preview`

## Goals / Non-Goals

**Goals:**

- Define the default processing chain after new materials are dropped into the repo.
- Require readable `source` outputs by default for meeting notes, transcripts, reports, and attachments.
- Define incremental behavior so repeated runs do not redo already processed materials unnecessarily.
- Define the narrow set of cases where Codex should ask the user instead of proceeding.

**Non-Goals:**

- Implement all future automation for material processing.
- Force every material into `reports` output.
- Automatically modify every visual artifact without an explicit fork-point decision.
- Change team-wide global Codex behavior outside this repository.

## Decisions

### Decision: Source summarization is the default completion bar

The change defines that material processing is not complete when only a placeholder draft exists. For source-oriented materials, default completion means the page includes a Chinese summary plus extracted conclusions, risks, and follow-up items when available.

Alternative considered:
- Treat intake creation as sufficient baseline.
  - Rejected because it preserves traceability but fails the user's actual expectation of "go process this".

### Decision: Ops output is conditional but proactive

The system should not always stop at `source`. If a material already contains owners, deadlines, blockers, or concrete follow-up actions, Codex should continue into `intake` and, when justified, `reminder`.

Alternative considered:
- Require the user to explicitly request ops extraction.
  - Rejected because it recreates the repeated workflow confirmation that this change is meant to eliminate.

### Decision: Visual artifacts create a single clarification fork

Visual assets such as `html`, `h5`, and `preview` files have materially different output costs from ordinary wiki-only synchronization. The design therefore keeps one narrow clarification boundary: Codex should ask whether to update the visual file itself when that intent is not explicit.

Alternative considered:
- Always update the visual artifact automatically.
  - Rejected because it is a higher-cost and potentially user-visible mutation.
- Always avoid touching the visual artifact unless explicitly told.
  - Rejected because some requests clearly imply the visual companion should be updated.

### Decision: Incremental handling is keyed by source lineage, not full reruns

The design uses existing source lineage such as `source_path` to determine whether a material has already been processed. Existing pages should be updated or skipped based on lineage and completeness instead of regenerating the whole inbox set.

Alternative considered:
- Re-run full intake each time and rely on human cleanup.
  - Rejected because it creates duplicate work, noisy drafts, and link drift.

## Risks / Trade-offs

- [Risk] "Readable summary" can still be interpreted too loosely. → Mitigation: tie the default bar to Chinese summary plus extracted conclusions, risks, and follow-up items when present in the material.
- [Risk] Incremental updates may preserve earlier weak conclusions. → Mitigation: require new, richer material to update existing pages rather than silently leaving low-quality placeholders untouched.
- [Risk] The single clarification boundary for visual artifacts may still be missed in edge cases. → Mitigation: document `html/h5/preview` explicitly as the canonical fork-point.
- [Risk] Some material types sit between evidence and deliverable. → Mitigation: keep `reports` conditional and treat `source` as the default landing layer unless the user clearly asks for a deliverable.

## Migration Plan

1. Create OpenSpec artifacts for the new collaboration-defaults change.
2. Add the new capability spec for default material processing.
3. Add a delta spec for the repository AI workflow to make collaboration defaults explicit.
4. Align wiki workflow documentation and local collaboration guidance with the spec.
5. Use the new change as the reference point for any follow-up automation or implementation work.

## Open Questions

- Whether the repository should eventually promote the local collaboration draft skill into a writable shared skill location.
- Whether future apply work should treat meeting-note summarization and visual-artifact branching as separate implementation slices.
