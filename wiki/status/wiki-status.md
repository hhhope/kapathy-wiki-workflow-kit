---
layer: status
domain: none
canonical_object: wiki-status
artifact_type: generated-status
status: generated
---

# Wiki Status

Generated at: `2026-05-14T09:41:41.991896+00:00`

## Summary

| Metric | Value |
| --- | --- |
| Wiki pages | 215 |
| Source records | 18 |
| Inbox files | 12 |
| Pending inbox files | 1 |
| Active OpenSpec changes | 0 |
| Complete active-dir changes | 16 |

## Wiki Sections

| Section | Pages |
| --- | --- |
| wiki/adr | 34 |
| wiki/domains | 2 |
| wiki/examples | 7 |
| wiki/ops | 118 |
| wiki/reports | 15 |
| wiki/root | 7 |
| wiki/sources | 19 |
| wiki/templates | 10 |
| wiki/timeline | 3 |

## Product Status

Contract version: `1`

### Object Types

| Object Type | Count |
| --- | --- |
| behavior | 5 |
| governance | 50 |
| output | 15 |
| source | 19 |
| unknown | 142 |

### Readiness

| Readiness | Count |
| --- | --- |
| accepted | 2 |
| draft-only | 213 |

### Source Layers

| Source Layer | Count |
| --- | --- |
| ops | 118 |
| report | 15 |
| source | 19 |
| spec | 50 |
| unknown | 29 |

### Identity Coverage

| Metric | Value |
| --- | --- |
| With identity | 97 |
| Missing identity | 118 |

### Relation Coverage

| Metric | Value |
| --- | --- |
| With relations | 97 |
| Missing relations | 118 |

### Unresolved Product Status Items

- `inbox/ad-desgin.md`: pending_inbox (blocked -> evidence_collection)
- `add-brainstorming-drift-wiki-trace`: complete_openspec_change (unresolved -> archive_review)
- `add-frontmatter-gate-precheck`: complete_openspec_change (unresolved -> archive_review)
- `add-go-engineering-security-rules`: complete_openspec_change (unresolved -> archive_review)
- `build-ad-growth-cockpit-h5`: complete_openspec_change (unresolved -> archive_review)
- `build-ad-platform-operational-prototype`: complete_openspec_change (unresolved -> archive_review)
- `close-wiki-skill-runtime-loop`: complete_openspec_change (unresolved -> archive_review)
- `enforce-whole-wiki-frontmatter-gate`: complete_openspec_change (unresolved -> archive_review)
- `formalize-wiki-runtime-layer-boundary`: complete_openspec_change (unresolved -> archive_review)
- `harden-behavior-asset-evaluation-gate`: complete_openspec_change (unresolved -> archive_review)
- `improve-wiki-routing-diagnostics`: complete_openspec_change (unresolved -> archive_review)
- `introduce-wiki-react-decision-trace-eval`: complete_openspec_change (unresolved -> archive_review)
- `normalize-go-rule-dedupe-gate`: complete_openspec_change (unresolved -> archive_review)
- `route-repo-public-artifacts-through-agent-intent`: complete_openspec_change (unresolved -> archive_review)
- `solidify-go-rule-official-sources`: complete_openspec_change (unresolved -> archive_review)
- `stabilize-wiki-frontmatter-taxonomy`: complete_openspec_change (unresolved -> archive_review)
- `stabilize-wiki-runtime-layer-contract`: complete_openspec_change (unresolved -> archive_review)

## Domain Taxonomy Health

Status: `drift`
Config: `wiki/config/frontmatter-taxonomy.yaml`

| Severity | Count |
| --- | --- |
| error | 767 |
| warn | 2 |
| info | 0 |
| total | 769 |

### Taxonomy Drift Samples

- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `missing_required_field`: Rule `whole_wiki` requires `layer` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`.
- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `missing_required_field`: Rule `whole_wiki` requires `domain` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`.
- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `missing_required_field`: Rule `adr_pages` requires `canonical_object` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`.
- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `missing_required_field`: Rule `adr_pages` requires `artifact_type` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`.
- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `unexpected_field_value`: Rule `adr_pages` expects `layer: adr` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`, got `None`.
- `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md` `error` `unexpected_field_value`: Rule `adr_pages` expects `domain: none` for `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`, got `None`.
- `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md` `error` `missing_required_field`: Rule `whole_wiki` requires `layer` for `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`.
- `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md` `error` `missing_required_field`: Rule `whole_wiki` requires `domain` for `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`.
- `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md` `error` `missing_required_field`: Rule `adr_pages` requires `canonical_object` for `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`.
- `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md` `error` `missing_required_field`: Rule `adr_pages` requires `artifact_type` for `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`.

## Frontmatter Strict Gate

| Metric | Value |
| --- | --- |
| Enabled | True |
| Passed | False |
| Blocking entries | 767 |
| Score | 0 / 100 |

## Frontmatter Scorecard

| Dimension | Weight | Findings | Points Lost | Passed |
| --- | --- | --- | --- | --- |
| completeness | 40 | 414 | 40 | False |
| taxonomy_validity | 25 | 233 | 25 | False |
| identity_coverage | 20 | 122 | 20 | False |
| relation_shape | 15 | 0 | 0 | True |

## Graph Parse Health

Status: `pass`

| Metric | Value |
| --- | --- |
| Suspicious relation pages | 0 |

### Graph Parse Samples

- None

## Pending Inbox Files

- `inbox/ad-desgin.md`

## OpenSpec Changes

| Change | State | Tasks | Path |
| --- | --- | --- | --- |
| add-brainstorming-drift-wiki-trace | complete | 5/5 | openspec/changes/add-brainstorming-drift-wiki-trace/tasks.md |
| add-frontmatter-gate-precheck | complete | 6/6 | openspec/changes/add-frontmatter-gate-precheck/tasks.md |
| add-go-engineering-security-rules | complete | 5/5 | openspec/changes/add-go-engineering-security-rules/tasks.md |
| build-ad-growth-cockpit-h5 | complete | 4/4 | openspec/changes/build-ad-growth-cockpit-h5/tasks.md |
| build-ad-platform-operational-prototype | complete | 5/5 | openspec/changes/build-ad-platform-operational-prototype/tasks.md |
| close-wiki-skill-runtime-loop | complete | 6/6 | openspec/changes/close-wiki-skill-runtime-loop/tasks.md |
| enforce-whole-wiki-frontmatter-gate | complete | 7/7 | openspec/changes/enforce-whole-wiki-frontmatter-gate/tasks.md |
| formalize-wiki-runtime-layer-boundary | complete | 6/6 | openspec/changes/formalize-wiki-runtime-layer-boundary/tasks.md |
| harden-behavior-asset-evaluation-gate | complete | 8/8 | openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md |
| improve-wiki-routing-diagnostics | complete | 7/7 | openspec/changes/improve-wiki-routing-diagnostics/tasks.md |
| introduce-wiki-react-decision-trace-eval | complete | 7/7 | openspec/changes/introduce-wiki-react-decision-trace-eval/tasks.md |
| normalize-go-rule-dedupe-gate | complete | 3/3 | openspec/changes/normalize-go-rule-dedupe-gate/tasks.md |
| route-repo-public-artifacts-through-agent-intent | complete | 5/5 | openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md |
| solidify-go-rule-official-sources | complete | 3/3 | openspec/changes/solidify-go-rule-official-sources/tasks.md |
| stabilize-wiki-frontmatter-taxonomy | complete | 9/9 | openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md |
| stabilize-wiki-runtime-layer-contract | complete | 6/6 | openspec/changes/stabilize-wiki-runtime-layer-contract/tasks.md |

## Next Actions

- Create or link source records for pending inbox files.
- Review complete active-directory OpenSpec changes for archive readiness.
