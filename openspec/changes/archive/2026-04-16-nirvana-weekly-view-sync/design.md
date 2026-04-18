## Context

The Nirvana weekly PM loop has already produced:

- one weekly source page
- one intake page
- one reminder page

But the user provided additional facts after the first pass:

- membership alignment has already been discussed and clarified
- profit-sharing launch timing is now anchored to May, with HuiShouQian starting in June
- Nirvana profit-sharing product work is now explicitly carried by 曹阳 because of core profit-sharing demand, and related requirements need re-review
- gateway external access method and commercial scope remain unresolved
- protocol-payment related settlement, billing, notifications, order updates, and reconciliation are not closed yet

The user also asked to keep the weekly HTML view updated and archived, because the HTML will change week by week.

## Goals / Non-Goals

**Goals:**

- Update the current weekly Nirvana records with the clarified facts.
- Create a dedicated source page for the weekly HTML preview file.
- Make the weekly archive pattern explicit: one HTML source per week.

**Non-Goals:**

- Convert the HTML into a new rendered wiki page.
- Build automatic weekly HTML versioning.
- Create Codex handoff tasks from these updates.

## Decisions

### Decision: Treat the HTML preview as a weekly source, not as a replacement for the spreadsheet

The spreadsheet remains the structured PM source. The HTML preview is a weekly visual companion source that adds gantt, capability-map, and technical-construction framing.

### Decision: Update the intake and reminder pages with clarified facts

The user's new facts materially affect:

- current judgment
- risk wording
- next actions

So they belong in the intake and reminder, not only in a source appendix.

### Decision: Preserve a week-specific naming pattern

The HTML source will be named with the same week pattern as the weekly report so future weeks can be archived independently.

## Risks / Trade-offs

- [Risk] The HTML preview may contain planning views that run ahead of the weekly report. → Mitigation: label it as a visual companion source, not the sole truth source.
- [Risk] User-provided clarifications may outpace file contents. → Mitigation: treat them as explicit weekly alignment facts and record them transparently in the weekly pages.
- [Risk] Weekly HTMLs may accumulate quickly. → Mitigation: keep them lightweight as source records with summary and lineage only.

## Migration Plan

1. Create and validate the change artifacts.
2. Add the weekly HTML source page.
3. Update the Nirvana weekly source page with the clarified facts and HTML linkage.
4. Update the intake and reminder pages with the refined progress and risk wording.
5. Update source navigation so the new HTML source is discoverable.
6. Verify the weekly record now preserves both spreadsheet and HTML context.
