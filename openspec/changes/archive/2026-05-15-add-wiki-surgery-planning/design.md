# Design

## Input

Surgery planning consumes:

- adjudication package details from `build_adjudication_package(root)`
- optional MOC projection plan JSON

The MOC input is optional and explicit. This keeps surgery planning independent
from any particular MOC generator implementation while still allowing MOC dry-run
work to be surfaced as surgery.

## Surgery Buckets

Adjudication details are included when they carry structural or governance
risks:

- `relation_weak_evidence` -> relation rebuild
- `drift_risk`, `adr_risk`, `openspec_required` -> governance/open change
- `taxonomy_candidate` -> taxonomy decision
- `agent_uncertain` with other surgery risk -> human surgery review

MOC entries with action `create`, `update`, or `orphan` are included as MOC
projection items. `noop` entries are excluded.

If adjudication `eval_result.passed` is false, surgery planning is blocked. The
planner reports the eval failure instead of producing surgery or MOC items.

## Write Boundary

Surgery planning never mutates patient pages. It can write only a surgery record
when explicitly requested.

The record is a review artifact, not approval to apply surgery.

## Recovery Boundary

Recovery is a follow-up layer. The surgery plan may name expected recovery
checks, but it does not run or satisfy recovery.
