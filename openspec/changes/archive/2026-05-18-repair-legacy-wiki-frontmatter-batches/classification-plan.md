# Classification Plan: remaining legacy frontmatter blockers

## Current Snapshot

Command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `blocking_count`: 709
- blocked page count: 165
- no remaining page is `layer`-only
- remaining work requires domain, ops area, identity, source index, or cleanup
  decisions before more fields are applied

## Route Groups

| Group | Pages | Action |
| --- | ---: | --- |
| `SOURCE_DOMAIN_LAYER` | 5 | Proposed deterministic source batch after approval |
| `SOURCE_UNCLASSIFIED_FLAG` | 3 | Proposed uncertainty batch after approval |
| `REPORT_DOMAIN_LAYER` | 1 | Proposed deterministic report batch after approval |
| `INDEX_PAGE_DECISION` | 7 | Needs explicit index-domain policy decision |
| `ROOT_PUBLIC_PAGE_DECISION` | 15 | Needs page-by-page domain/layer decision |
| `TEMPLATE_DECISION` | 1 | Needs template policy decision |
| `MNT_MIRROR_REVIEW` | 2 | Needs cleanup/exclusion decision, not frontmatter repair first |
| `OPS_AREA_DOMAIN_ONLY` | 44 | Needs ops-area/domain mapping approval |
| `OPS_FORBIDDEN_DOMAIN_REMAP` | 37 | Needs replacement for forbidden `domain: personal-ops` |
| `OPS_IDENTITY_REBUILD` | 50 | Needs canonical/artifact rebuild approval |

## Proposed Batches

### Batch 7: Sources With Existing Source Identity

Scope:

- `wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md`
- `wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md`
- `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md`
- `wiki/sources/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md`
- `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`

Proposed fields:

- `layer: sources`
- `domain: product-engineering-collaboration`

Reason:

- Paths are under `wiki/sources`.
- Existing `source_type`, `canonical_object`, and `artifact_type` already
  identify them as source evidence for the product-engineering collaboration
  material.

### Batch 8: Unclassified Meeting Sources

Scope:

- `wiki/sources/20260415100517-转写-yan的快速会议-纪要文本-1.md`
- `wiki/sources/20260415100517-转写-yan的快速会议-逐字稿文本-1.md`
- `wiki/sources/文字转写-呼呼的快速会议-276823523.md`

Proposed fields:

- `layer: sources`
- keep `domain: unclassified`
- add `classification_needed: true`

Reason:

- The taxonomy requires `classification_needed: true` when `domain:
  unclassified`.
- These pages are raw meeting-note sources and should not invent a business
  domain from filenames.

### Batch 9: Single Product Report

Scope:

- `wiki/reports/agentic-product-engineering-collaboration-management-report.md`

Proposed fields:

- `layer: reports`
- `domain: product-engineering-collaboration`

Reason:

- Existing `canonical_object` is `agentic-product-engineering-collaboration`
  and `artifact_type` is `report`.

### Batch 10: Index Pages

Scope:

- `wiki/domains/index.md`
- `wiki/examples/index.md`
- `wiki/index.md`
- `wiki/reports/index.md`
- `wiki/sources/index.md`
- `wiki/status/index.md`
- `wiki/timeline/index.md`

Decision needed:

- Whether index pages use `domain: none` as structural navigation pages.
- Whether `wiki/sources/index.md` should use `source_type: index`.

Do not apply before approval:

- `wiki/config/frontmatter-taxonomy.yaml` has a `wiki/domains` path policy
  named `required_real_domain`, so `wiki/domains/index.md` needs an explicit
  exception or accepted local convention before applying `domain: none`.

### Batch 11: Root And Public Pages

Scope shape:

- root pages such as `wiki/ai-chat-workflow-installer.md`,
  `wiki/ai-workflow.md`, `wiki/inbox-intake.md`, `wiki/language-policy.md`,
  `wiki/role-boundaries.md`, and `wiki/team-lore-candidates.md`
- report pages without domain/layer, including `team-knowledge-base-*`,
  `ai-chat-workflow-installer-feishu-share.md`, and
  `nirvana-handover-account-owner.md`
- `wiki/timeline/2026-04-20-agent-readable-wiki-evolution.md`

Decision needed:

- Confirm per-page domain (`ai-workflow`, `wiki`, `report-workflow`,
  `nirvana-project`, or another known taxonomy value).
- Confirm whether root wiki guidance pages should use `layer: ops`,
  `layer: reports`, `layer: timeline`, or a structural index convention.

### Batch 12: Mirror Paths

Scope:

- `wiki/mnt/d/cloud/account-meeting-lore/openspec/changes/archive/2026-04-18-formalize-example-driven-wiki-capture.md`
- `wiki/mnt/d/cloud/account-meeting-lore/wiki/ops/agent-governance-gate-gap-explore-2026-04-18.md`

Decision needed:

- Treat these as accidental mirrored paths and remove/exclude them through a
  cleanup workflow, or explicitly classify them.

Do not repair as normal wiki pages before this cleanup decision.

### Batch 13: Ops Pages With Existing Identity

Scope:

- 44 `wiki/ops` pages already have `canonical_object` and `artifact_type`.

Required fields:

- `layer: ops`
- `domain`
- `ops_area`

Suggested mapping buckets:

- wiki runtime pages: `domain: wiki`, `ops_area: wiki-runtime`
- report gate / public output pages: `domain: public-report-output` or
  `product-engineering-collaboration`, `ops_area: report-quality`
- learning notes: relevant real domain, `ops_area: learning-capture`
- workflow traces and drift/explore pages: relevant real domain or
  `unclassified`, `ops_area: workflow-trace`
- source intake pages: relevant real domain or `unclassified`,
  `ops_area: source-intake`

Do not apply before approval:

- `ops_area` is not derivable from path alone for all pages.

### Batch 14: Forbidden `personal-ops` Remap

Scope:

- 37 `wiki/ops` pages currently use forbidden `domain: personal-ops`.

Decision needed:

- Replace with a real taxonomy domain when clear.
- Use `domain: unclassified` plus `classification_needed: true` when the page
  should stay unresolved.
- Never keep `domain: personal-ops`.

Suggested mapping buckets:

- agent governance / rules / Codex behavior: likely `domain: wiki`,
  `ops_area: agent-governance`
- wiki-readable or wiki-runtime assets: likely `domain: wiki`,
  `ops_area: wiki-runtime`
- learning intake/notes: likely `ops_area: learning-capture`, with domain from
  content
- samples: likely `domain: none` or `unclassified`, but this needs a sample-page
  convention decision

### Batch 15: Ops Identity Rebuild

Scope:

- 50 `wiki/ops` pages are missing `canonical_object` and/or `artifact_type`.

Decision needed:

- Confirm whether canonical object may be derived from filename stem.
- Confirm artifact type source of truth: existing `type`, folder name, filename
  suffix, or manual classification.

Suggested sub-batches:

- wiki doctor / treatment / recovery / surgery run records
- wiki review decision records
- Nirvana intake/reminder records
- disagreement / reanchor / project-management method pages
- sample pages
- raw meeting intake pages with `domain: unclassified`

## Stop Conditions

- Do not apply any remaining frontmatter fields until the relevant batch is
  explicitly approved.
- Do not edit relation fields.
- Do not edit taxonomy config or checker logic in this change.
- Do not treat `wiki/mnt` mirror paths as ordinary pages before the cleanup
  decision.
