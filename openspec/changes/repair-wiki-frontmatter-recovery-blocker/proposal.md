# Proposal: repair wiki frontmatter recovery blocker

## Summary

Create a bounded repair path for the wiki medical-loop recovery blocker caused
by the strict whole-wiki frontmatter gate. The change will turn the current
frontmatter precheck failure into auditable batches with target-level evidence,
so the medical loop can distinguish fixed treatment targets from remaining
legacy repository debt.

## Problem

The latest wiki medical treatment run applied all 10 approved treatment
candidates successfully, but recovery still routes to `blocked` because
`frontmatter_precheck` fails at the whole-wiki level.

Current observed state:

- Treatment apply: `applied_count=10`, `blocked_count=0`.
- Recovery: `passed=false`, `next_route=blocked_by_recovery_findings`.
- Frontmatter precheck: 910 blocking entries across legacy `wiki/adr` and
  `wiki/ops` pages.
- The 10 treatment target pages each have target-level `entry_count=0`.

Without a scoped repair path, the medical loop cannot tell whether a treatment
failed, a target remains invalid, or unrelated historical debt is blocking
archive readiness.

## Scope

In scope:

- Add a bounded frontmatter recovery repair workflow for strict-gate blockers.
- Produce batch inputs from the existing precheck report and enrichment preview.
- Repair only explicitly selected pages or configured batches.
- Preserve target-level precheck evidence before and after each batch.
- Keep whole-wiki failure visible when unrelated legacy debt remains.
- Update medical-loop recovery interpretation so target-clean treatment runs do
  not get confused with unrelated repository-wide blockers.

Out of scope:

- Blind full-repository frontmatter migration.
- Changing taxonomy vocabulary, scoring formulas, or checker semantics.
- Writing relation fields, MOC projections, ADR decisions, or OpenSpec lifecycle
  state from the repair workflow.
- Archiving the active medical case.
- Reverting unrelated dirty worktree changes.

## Success Criteria

- A contributor can select a small repair batch from current gate evidence.
- Each repaired page has before/after `wiki_gate_precheck --target` evidence.
- The workflow reports remaining whole-wiki blockers without hiding them.
- The medical-loop case can record whether treatment targets are clean even
  when repository-wide frontmatter debt remains.
- Verification includes focused tests and a strict frontmatter precheck report
  showing the residual blocker boundary.
