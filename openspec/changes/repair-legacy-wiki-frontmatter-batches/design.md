# Design: repair legacy wiki frontmatter batches

## Approach

Use the already-implemented repair stack:

- `scripts/wiki_gate_precheck.py` for target and whole-wiki evidence.
- `scripts/build_wiki_frontmatter_repair.py` for batch selection and approved
  field application.
- `wiki/config/frontmatter-taxonomy.yaml` as the only taxonomy authority.

The repair is intentionally batch-oriented. A batch is safe only when the
approved field values are explicit. Exact precheck hints may be applied as-is.
Fields without exact hints require either a deterministic path-based rule in
the task or manual approval in the batch evidence.

## Initial Batch

The first planner run returned:

- `source_blocking_count`: 916
- `selected_count`: 10
- `review_needed_count`: 10
- selected paths: `wiki/adr/0001` through `wiki/adr/0010`

For these ADR pages, precheck gives exact values:

- `layer: adr`
- `domain: none`

The missing `canonical_object` can be derived from the ADR filename stem after
the numeric prefix because the filename is the repository's stable ADR object
identifier. The missing `artifact_type` is `adr`.

## Batch Rules

- Do not modify page body text.
- Do not add or change relation fields.
- Do not edit taxonomy config or checker logic.
- Do not apply fields for pages whose path/content does not identify the value
  clearly.
- Prefer small commits per verified batch.
- Preserve nonzero whole-wiki gate results as residual debt rather than hiding
  them.

## Verification

For each batch:

1. Run `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
   before applying.
2. Apply only approved frontmatter fields.
3. Run the same target precheck after applying.
4. Run a whole-wiki frontmatter precheck and record residual blocker counts.
5. Re-run medical recovery/status only after an explicit batch or cleanup
   milestone.
