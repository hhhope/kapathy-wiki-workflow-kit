## Why

The `agentic-product-engineering-collaboration` source pool is broad but stops
short of the user's new target: test whether the thread can reach 300 sources.

Current local evidence shows:

- the source map records 43 curated items;
- the broad scan records 88 leads;
- the public timeline records 95 entries;
- the podcast/video pool records 36 leads;
- URL extraction across the relevant files finds 252 unique URLs.

That is enough to show feasibility, but not enough to claim a 300-source pool.
The report gate also already warns that source-pool size is not the same as
publication-ready evidence.

## What Changes

- Add a bounded source-hardening pass for
  `agentic-product-engineering-collaboration`.
- Extend the source pool to at least 300 unique URL leads.
- Preserve source classes such as `primary`, `research`, `secondary`,
  `candidate`, `primary-interview`, and `transcript-needed`.
- Update the evidence matrix and report gate review so they distinguish:
  - 300 source leads;
  - unique URL count;
  - load-bearing citation candidates;
  - publication blockers.

## Non-Goals

- Do not claim "all public sources" or "全网".
- Do not claim 300 publication-grade sources.
- Do not publish or sync the report to Feishu.
- Do not repair H5 visuals or report prose in this change.
- Do not promote a new workflow behavior or skill rule.

## Impact

- Updates `wiki/sources/agentic-product-engineering-collaboration-*`.
- Updates source-hardening evidence under `wiki/ops`.
- Updates report gate review only for evidence/readiness status.
- Adds an OpenSpec source-hardening spec for this bounded content object.
