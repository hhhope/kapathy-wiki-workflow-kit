# Proposal

## Why

The requirements checker can now validate a DDD `domain_model`, confirmed role
instances, user stories, and acceptance-function mappings, but it still treats
those layers as mostly independent. A case can become `requirements_ready` while
the readable stories and acceptance functions do not show how the taxonomy
subdomains, bounded contexts, aggregate lifecycles, context handoffs, failure
paths, and evidence paths are covered.

The `agent-subscription-payment` pressure test exposed the gap: the case had a
valid `domain_model`, yet the first story/acceptance pass was mostly owner and
workflow oriented. It became reviewable only after adding an explicit Domain
Coverage matrix and additional lifecycle stories for payment transaction,
ledger/fund state, reconciliation, split rule, platform fee, and related
acceptance functions.

`requirements/config/requirements-taxonomy.yaml` already names this expectation
in `readiness_gate_model`, but the runtime checker and case rendering do not
enforce or guide it.

## What Changes

- Add a required domain coverage contract for taxonomy v2 requirement cases.
- Extend requirements case data and rendering with a visible Domain Coverage
  section.
- Require user stories to be bound to role, subdomain/context, and aggregate
  lifecycle evidence.
- Require acceptance functions to classify observable coverage across state
  changes, context handoffs, failure paths, and evidence paths.
- Teach the checker to report a `domain_coverage_gate` in addition to
  `domain_model_gate` and `requirement_delivery_gate`.
- Update requirements workers and handoff output so future cases and OpenSpec
  drafts carry coverage evidence instead of relying on ad hoc review repair.

## What Does Not Change

- Does not mutate the requirements taxonomy vocabulary unless implementation
  finds a narrowly scoped field addition is unavoidable and separately
  documented.
- Does not migrate all historical requirements cases.
- Does not change wiki frontmatter taxonomy.
- Does not create or implement the Agent subscription payment product.
- Does not create OpenSpec drafts automatically from requirement cases.

## Source Evidence

- `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`
- `requirements/config/requirements-taxonomy.yaml`
- `scripts/check_requirements_case.py`
- `scripts/requirements_case.py`
