## Context

The user asked for TDD and pressure testing after the readable views were added.
That has not happened yet.

The missing proof is not semantic correctness of every reading judgment. The
missing proof is that the repository can structurally prove:

- the three required reading views exist
- the expected index entry points point to them
- the change stayed inside the reading layer and did not mutate
  `openspec-explore`

This change should reuse the repository's existing executable-replay style
instead of inventing a broad new framework.

## Goals / Non-Goals

**Goals**

- add a minimal executable validation contract for `wiki-readable-views`
- record explicit RED/GREEN evidence
- keep proof boundaries narrow and honest

**Non-Goals**

- do not validate semantic usefulness automatically
- do not add graph or dashboard generation
- do not modify the three readable-view pages themselves unless validation
  requires a reference path correction
- do not reopen `openspec-explore`

## Decisions

### Decision: Validate the readable-view bundle structurally

The checker should fail if any of these are missing:

- timeline view page
- artifact-grouping view page
- relation-reading view page
- expected wiki index entry points

Alternative considered:
- validate the views only by reading the wiki manually.
  - Rejected because the user explicitly asked for TDD and pressure testing.

### Decision: Keep the checker bounded to repository-local presence and links

The checker should not try to decide whether the views are "good enough"
semantically. It should prove only that the first-pass reading bundle exists and
is wired in.

Alternative considered:
- attempt semantic scoring of the views.
  - Rejected because that would create another analysis layer instead of
    validating the current one.

### Decision: Use the real readable-view pages as the first replay record

The first validation record should use the real pages and index files produced
by the readable-views change.

## Validation Contract

Minimum record fields:

- `bundle_label`
- `timeline_view`
- `artifact_grouping_view`
- `relation_reading_view`
- `required_indexes`
- `red_baseline`
- `green_result`
- `residual_risk`

Required pass checks:

- `timeline_view_present`
- `artifact_grouping_present`
- `relation_reading_present`
- `index_links_present`
- `no_openspec_explore_mutation_claim`

## Pressure Scenarios

### Scenario 1: One required reading view is missing

The checker must fail.

### Scenario 2: View pages exist but indexes do not point to them

The checker must fail.

### Scenario 3: All required pages and index links exist

The checker should pass structurally, while still stating proof boundaries.
