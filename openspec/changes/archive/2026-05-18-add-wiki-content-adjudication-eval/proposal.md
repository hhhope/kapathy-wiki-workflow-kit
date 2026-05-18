# Proposal: wiki content adjudication eval

## Summary

Add an adjudication and eval layer after wiki content enrichment preview so
candidate frontmatter and relation suggestions become auditable review packages
instead of raw candidate dumps.

## Problem

`wiki_content_enrichment` currently produces candidate suggestions for
`wiki/ops` and `wiki/adr`, but it does not:

- preserve a full review detail set for drift tracing
- provide an agent judgment for each candidate
- separate user-focused review risks from full details
- identify taxonomy candidates that are not already in the YAML config
- evaluate whether the judgment has evidence or missed governance risks

This leaves the user reviewing a flat candidate list and makes it hard to see
where ADR, drift, taxonomy, or OpenSpec risks entered the workflow.

## Scope

In scope:

- deterministic adjudication package generation for `wiki/ops` and `wiki/adr`
- `full_detail_set`
- `agent_judgment_set`
- `taxonomy_candidate_set`
- `review_focus_set`
- `drift_trace_set`
- an eval result that rejects missing evidence and missed risk flags
- status/apply/react surfaces that expose adjudication as review/eval output

Out of scope:

- directly writing frontmatter
- mutating `wiki/config/frontmatter-taxonomy.yaml`
- generating or applying MOC pages
- graph UI
- query engine
- change queue
- marking unrelated OpenSpec work complete

## Success Criteria

- A content enrichment run can produce a review package with both full details
  and focused user-review risks.
- The review package can preserve rejected candidates and judgment reasons.
- Taxonomy candidates are surfaced as candidates, not silently promoted.
- Eval can fail when a risky judgment lacks evidence or misses required risk
  flags.
- Runtime command surfaces keep the boundary: preview and review only, no direct
  structure writes.
