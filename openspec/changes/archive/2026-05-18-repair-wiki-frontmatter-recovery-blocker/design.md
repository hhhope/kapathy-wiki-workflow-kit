# Design: repair wiki frontmatter recovery blocker

## Approach

Use the existing frontmatter taxonomy checker, precheck, and enrichment preview
as the source of repair truth. The repair workflow must not infer taxonomy
values from free text when the precheck repair hints or enrichment preview do
not provide enough evidence.

The workflow has three layers:

1. **Evidence extraction**: read the full frontmatter precheck report and group
   blockers by path, rule, field, and severity.
2. **Batch planning**: select a small explicit batch, attach repair hints or
   enrichment suggestions, and mark uncertain pages as review-needed instead of
   modifying them.
3. **Batch application and recovery evidence**: apply only approved
   frontmatter fields, then run target-level precheck for each changed page and
   whole-wiki precheck for residual blocker accounting.

## Medical-Loop Boundary

The current medical treatment targets are clean at target level. Recovery
should preserve that fact separately from the whole-wiki gate result:

- `target_frontmatter_status`: target-level pass/fail for treatment targets.
- `repository_frontmatter_status`: whole-wiki strict gate pass/fail.
- `next_action`: remains `blocked` while repository-wide debt exists, but the
  reason must identify whether blockers are target-local or repository-wide.

This avoids re-running treatment because unrelated legacy pages still fail the
strict gate.

## Repair Rules

- Use `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
  before and after each target repair.
- Use exact values from `target.repair_hints.exact_frontmatter`.
- Use `target.repair_hints.field_options` only when the page path/content and
  existing repo routing make the choice explicit.
- Use enrichment preview suggestions only when confidence is high and
  `needs_review=false`.
- Do not write relation fields during this workflow.
- Do not edit taxonomy config or checker scoring in this change.

## Data Flow

```text
whole-wiki precheck
  -> grouped blocker report
  -> explicit batch plan
  -> target precheck before
  -> frontmatter field update
  -> target precheck after
  -> whole-wiki residual report
  -> medical case recovery note
```

## Verification

- Unit tests for batch selection and target evidence rendering.
- A dry-run fixture proving uncertain pages are not modified.
- Focused target precheck for repaired pages.
- Whole-wiki precheck preserving any remaining non-zero result as residual
  repository debt.
