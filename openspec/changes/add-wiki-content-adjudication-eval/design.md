# Design: wiki content adjudication eval

## Pipeline Position

The new layer sits after content enrichment preview and before any approved
structure write:

```text
content enrichment preview
  -> content adjudication
  -> adjudication eval
  -> review package
  -> explicit approved frontmatter write
```

## Inputs

- `build_enrichment_preview(root)` output
- page path
- current frontmatter
- suggested frontmatter
- suggested relations
- evidence
- taxonomy config

## Outputs

The package contains:

- `candidate_set`: raw enrichment entries
- `full_detail_set`: one detail per page with candidate, judgment, risks,
  rejected candidates, and evidence
- `agent_judgment_set`: compact per-page judgments
- `taxonomy_candidate_set`: candidate taxonomy values that are not known in the
  YAML config
- `review_focus_set`: high-risk or user-confirmation items with refs back to
  `full_detail_set`
- `drift_trace_set`: entries that explain where drift or governance risk begins
- `eval_result`: passed/errors/warnings and missing evidence or missed risk
  diagnostics

## Judgment Model

Judgment states:

- `accept`: existing or strongly evidenced candidate with no unresolved risk
- `likely`: evidenced candidate that is probably correct but still useful to
  review
- `reject`: candidate is weak, conflicted, or outside the layer boundary
- `needs_user_confirmation`: taxonomy, ADR, drift, OpenSpec, or conflict risk
  needs human decision

Risk flags:

- `taxonomy_candidate`
- `domain_conflict`
- `relation_weak_evidence`
- `adr_risk`
- `drift_risk`
- `openspec_required`
- `agent_uncertain`

## Eval Rules

Eval fails if:

- a judgment has no evidence
- a candidate with `domain: unclassified` lacks `agent_uncertain`
- an unknown domain is not surfaced in `taxonomy_candidate_set`
- ADR pages are not marked with ADR evidence/risk
- drift/retro/reanchor pages are not marked with drift evidence/risk
- `safe_to_apply_frontmatter` is true while unresolved review risks remain

Eval may warn if:

- a relation candidate has weak evidence
- a candidate remains likely but review focus is omitted

## Runtime Boundaries

| Surface | Role | Boundary |
| --- | --- | --- |
| adjudication package | judges candidates and creates review sets | does not write pages |
| adjudication eval | checks judgment evidence and missed risks | does not approve writes |
| status | summarizes adjudication health | does not write pages |
| apply | previews review package context | does not decide semantic truth |
| react | routes intent to adjudication/eval | does not write structure |

## Verification

Verification should prove:

- full details and focused review sets are both produced
- focus entries link back to full detail entries
- taxonomy candidates are exposed when candidates are outside known YAML values
- drift and ADR risks are surfaced
- eval fails on missing evidence or unsafe apply decisions
- runtime skill docs preserve preview/review-only boundaries
