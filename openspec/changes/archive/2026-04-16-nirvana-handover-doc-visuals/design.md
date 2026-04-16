## Context

The current handover document is structurally complete but still lacks two views the user explicitly needs during takeover:

- a visualized milestone drift summary aligned to the milestone node sheet
- a project team member list for alignment and follow-up routing

The document must remain Chinese-first and Feishu-compatible. That means the milestone view should use markdown-native structures that render reliably in Feishu, instead of diagram syntaxes with uncertain support.

## Goals / Non-Goals

**Goals:**

- Add a milestone-oriented visual section that compares baseline milestone nodes with current status and drift.
- Add a project team member section covering the core project roles visible in the staffing sheet.
- Keep the delivery surface consistent between the local markdown draft and the Feishu document.

**Non-Goals:**

- Rebuild a full Gantt chart or management report.
- Normalize all historical milestone date inconsistencies across spreadsheets.
- Infer missing members for blank roles such as `业务一号位` when the source sheet is empty.

## Decisions

### Decision: Use a Feishu-stable visual format

The milestone drift view will be expressed as:

- a compact visual status legend
- a milestone drift matrix with baseline dates
- textual progress bars using stable unicode blocks only when they remain readable in markdown

This avoids Mermaid or image dependencies and keeps the document editable.

### Decision: Separate milestone drift from acceptance detail

The new milestone section will sit before the detailed risk and acceptance sections. This lets the incoming owner first understand timeline drift at a glance, then read the item-level detail below.

### Decision: Add an explicit team member section near the summary

The member list will be added near the top of the document so the incoming owner can immediately see:

- project owner
- product owner(s)
- technical owner(s)
-研发
- test owner(s)
- PMO
- adjacent functions such as compliance, legal, and operations

Blank roles in the evidence will be preserved as `待补充`.

## Risks / Trade-offs

- [Risk] Milestone dates in the sheet are old planning baselines rather than current execution targets. → Mitigation: label them clearly as baseline nodes and express current status as judgment, not as claimed actual completion dates.
- [Risk] Some member roles may have changed since the spreadsheet snapshot. → Mitigation: present them as current evidence and keep a `待补充` marker where the sheet is blank.
- [Risk] A highly visual chart could break in Feishu. → Mitigation: prefer table-based visualization that degrades gracefully.

## Migration Plan

1. Create and validate the refinement change artifacts.
2. Update the local markdown handover draft with the milestone visual and member section.
3. Re-publish or update the existing Feishu handover document.
4. Verify the published content contains the two new sections.
