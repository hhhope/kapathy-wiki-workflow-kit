---
layer: ops
domain: none
ops_area: report-quality
canonical_object: ad-growth-cockpit-h5
artifact_type: report-gate-review
created: 2026-05-13
kind: report-gate-review
status: prototype-verified
target: wiki/reports/ad-growth-cockpit-h5.html
---

# ad-growth-cockpit-h5 / report-gate-review

## Review Target

Target: `wiki/reports/ad-growth-cockpit-h5.html`

Destination: repo-local standalone H5 prototype.

Scope: convert `inbox/ad-desgin.md` into a customer-facing Growth Cockpit demo
for advertisers and customer-side decision makers.

Non-scope: No Feishu sync, no production rollout, no backend service, no login,
no real media-platform API, and no real campaign data.

## Reviewer Routing

Reviewer routing: required for reader-facing H5 prototype.

Signals:

| Signal | Result |
|---|---|
| Reader-facing H5/share artifact | true |
| Source PRD needs audience rewrite | true |
| Visual/interface judgment required | true |
| Public publication or Feishu sync requested | false |

Template status: user selected Growth Cockpit visual direction for a
customer/advertiser demo.

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | advertisers and customer-side decision makers |
| Reader decision or action | Understand whether the product can control spend, optimize performance, handle delivery anomalies, and support the next campaign review loop. |
| Main line | A single real-time Growth Cockpit connects delivery, spend visibility, optimization, anomaly response, and campaign review. |
| Non-goals | No internal PRD dump. No production claim. No Feishu sync. No real ad-platform integration. |
| User-owned judgments | Audience choice: customer/advertiser demo. Visual direction: Growth Cockpit. Prototype-level jump interactions are enough for this run. |
| Agent-allowed work | Compress the source design into a reader-facing prototype, use mock data, implement local demo interactions, and record the proof boundary. |

## Reference Structure Map

| Field | Result |
|---|---|
| Source | `inbox/ad-desgin.md` advertising delivery system design. |
| Reader job | Quickly see what the system does for advertiser growth operations. |
| Page group | One standalone H5 prototype. |
| Reading path | Hero cockpit -> money flow -> optimization -> anomalies -> review. |
| Visual logic | Dashboard-first SaaS cockpit with KPI cards, spend/performance distribution, optimization actions, anomaly cards, and review loop. |
| Writing standard | Customer-facing Chinese product-demo language, not internal module-by-module PRD prose. |
| Reuse boundary | Source modules are translated into customer-visible capabilities; mock numbers are illustrative only. |

Reference Structure Gate: PASS for prototype. The source-to-reader translation is
explicit and does not claim publication-grade evidence.

## Reference Output Shape

Selected output shape: standalone H5 customer demo.

Retained patterns:

- Live dashboard first viewport.
- Five-section anchored narrative.
- Clickable KPI, view-toggle, alert-expansion, and review CTA interactions.

Rejected patterns:

- Architecture-diagram-first page.
- Dense PRD outline.
- Backend workflow simulator.

Reference Output Shape Gate: PASS for prototype.

## Learning Use Map

No external learned reference is promoted by this output. Existing repo H5
examples were used only as local format inspiration, not as source evidence.

Learning Use Gate: NOT APPLICABLE.

## Section And Paragraph Drift Review

| Section | Objective | Mainline fit | Drift risk | Action |
|---|---|---:|---:|---|
| Hero cockpit | Establish one real-time growth-control surface. | 5 | 0 | Retain. |
| Money flow | Show where spend and performance move by channel, plan, and creative. | 5 | 0 | Retain. |
| Optimization | Translate technical modules into advertiser-visible improvement actions. | 5 | 0 | Retain. |
| Anomalies | Show how delivery risks are detected and handled. | 5 | 0 | Retain. |
| Review | Close the campaign loop with attribution, LTV, creative analysis, and next action. | 5 | 0 | Retain. |

Paragraph Drift Gate: PASS for prototype.

## Judgment Ledger

| Judgment | Source Class | Status | Required Action |
|---|---|---|---|
| Customer/advertiser audience | User choice | confirmed | None. |
| Growth Cockpit direction | User choice | confirmed | None. |
| Mock KPI numbers | Agent-created demo data | prototype only | Do not treat as real campaign data. |
| Channel names and capability labels | Source-derived translation | prototype only | Verify with product owner before production or sales use. |
| No Feishu sync | Explicit boundary | confirmed | Keep local unless user asks for sync later. |

## Hard Gate Results

| Gate | Result | Note |
|---|---|---|
| Reader intent | PASS | Audience and reader action are explicit. |
| Reference/output shape | PASS | H5 cockpit shape matches selected direction. |
| Narrative drift | PASS | Sections support the cockpit main line. |
| Judgment ownership | PASS | User choices and agent mock data are separated. |
| Visual output | PASS | Desktop and mobile screenshots generated after loading a local CJK fontconfig; text renders and layout is readable. |
| Publish gate | NOT APPLICABLE | No Feishu sync or production publication requested. |

## Scorecard

Prototype score: 88 / 100.

Publication score: INVALID because no Feishu sync or external publication was
requested or verified.

## Decision

The artifact may be used as a repo-local prototype. It must not be claimed as
Feishu-synced, production-ready, or externally published.

## Residual Risks

- The prototype uses mock numbers and local static interactions only.
- Visual verification proves local render behavior, not real customer acceptance.
- Any later sales, Feishu, or production usage needs a new review/update pass.

## Local Verification

Completed on 2026-05-13:

- `python3 -m unittest tests.test_ad_growth_cockpit_h5 tests.test_public_report_quality_gate -v`: 14 tests passed.
- `python3 scripts/check_behavior_assets.py`: passed.
- `git diff --check`: passed.
- `python3 scripts/check_wiki_frontmatter.py`: failed on pre-existing legacy
  taxonomy drift (`personal-ops` and missing `classification_needed` on older
  pages); `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md` was not listed
  as drift.
- Inline JavaScript parse check: passed.
- Playwright interaction check: passed for KPI jump, spend view tab switch,
  alert expand, Escape close, review CTA jump, and mobile creative-view switch.
- Desktop screenshot: `/tmp/ad-growth-cockpit-h5-desktop.png`.
- Mobile screenshot: `/tmp/ad-growth-cockpit-h5-mobile.png`.

## Feishu Update Verification

No Feishu sync. No update command run.

## Visual Asset Boundary

The H5 is self-contained and uses inline CSS, inline JavaScript, and CSS/SVG-like
structures only. No separate image asset insertion was requested or performed.
