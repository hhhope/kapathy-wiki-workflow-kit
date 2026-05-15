# Design

## Boundary

The exclusion belongs in `scripts/wiki_content_adjudication.py`, after the
content enrichment preview is built and before adjudication detail IDs are
assigned. This keeps the doctor/review-record output directories available as
repo-visible evidence while preventing them from becoming future diagnostic
inputs.

## Excluded Paths

- `wiki/ops/wiki-doctor-runs/`
- `wiki/ops/wiki-review-decisions/`

## Behavior

The package `summary.candidate_count`, `candidate_set`, `full_detail_set`,
`agent_judgment_set`, `taxonomy_candidate_set`, `review_focus_set`, and
`drift_trace_set` all operate on the filtered candidate list.

The filter is path based and deterministic. It does not infer document meaning
and does not hide ordinary `wiki/ops` or `wiki/adr` pages.

## Verification

- Add a regression test proving generated doctor/review-decision records are
  absent from adjudication candidates.
- Run the adjudication and review-decision unit tests.
- Validate this OpenSpec change in strict mode.

