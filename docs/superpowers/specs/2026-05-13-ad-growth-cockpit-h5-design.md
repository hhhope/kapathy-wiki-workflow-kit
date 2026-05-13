# Ad Growth Cockpit H5 Prototype Design

## Source

- Input file: `inbox/ad-desgin.md`
- Source shape: dense advertising delivery system design, architecture notes,
  PRD sections, module diagrams, and sequence diagrams.
- Target artifact: customer-facing H5 prototype demo.

## Audience

Primary audience: advertisers and customer-side decision makers.

The H5 should help a prospective advertiser quickly understand what the product
does for them: control spend, see performance, respond to anomalies, and improve
future campaigns. It should not read like an internal technical PRD.

## Design Direction

Selected visual direction: **Growth Cockpit**.

The page should feel like a polished SaaS product demo centered on a real-time
advertising growth cockpit. It should show live operational confidence rather
than a static architecture document.

Core narrative:

> From delivery, monitoring, optimization, and anomaly handling to review, the
> advertiser gets one real-time growth cockpit.

## Page Structure

The H5 prototype has five sections:

1. **Hero Cockpit**
   - Lead with a full-screen dashboard-like first viewport.
   - Show mock live KPIs: spend, conversions, ROAS, CPA, budget utilization.
   - Include a short customer promise: real-time control over advertising growth.

2. **Where The Money Goes**
   - Show cross-channel spend and performance distribution.
   - Use mock channels such as 巨量引擎, 腾讯广告, Google Ads, 自营流量.
   - Let users switch or highlight channel, plan, and creative views.

3. **Why Performance Improves**
   - Convert technical modules into four customer-visible optimization actions:
     automatic bidding, dynamic budget allocation, creative selection, and rule
     engine actions.
   - Avoid showing backend architecture as the main story.

4. **How Anomalies Are Handled**
   - Show funnel drop, CPA overrun, traffic anomaly, and budget overrun alerts.
   - Each alert expands into a recommended action and automation status.

5. **Review And Next Campaign**
   - Show daily/weekly report, attribution, LTV, creative analysis, and next-step
     suggestions.
   - End with a prototype CTA such as “查看本周投放复盘”.

## Interaction Design

Prototype interactions should be real front-end behavior using mock data:

- Section navigation: top or side navigation jumps between the five sections.
- KPI card click: clicking CPA, ROAS, spend, or conversion cards jumps or scrolls
  to the related explanation section.
- Channel view toggles: users can switch between channel, plan, and creative
  views in the money-flow section.
- Alert cards: clicking an anomaly expands recommended actions.
- Report CTA: jumps to the review section.
- Mobile behavior: vertical scroll first, compact sticky navigation, tap-friendly
  cards.
- Desktop behavior: scroll with anchored navigation, wide dashboard composition.

Non-interactions:

- No login.
- No backend.
- No real media API calls.
- No editable campaign creation workflow.
- No Feishu sync.

## Visual System

Use a polished operational SaaS style:

- Deep neutral background with restrained cyan, green, amber, and violet accents.
- Dense but readable dashboard cards.
- Subtle motion for live status, metric changes, and alert expansion.
- Charts implemented with CSS/SVG or lightweight inline structures, not external
  chart dependencies.
- Professional product tone, not a marketing landing page full of generic hero
  claims.

Avoid:

- A pure architecture diagram page.
- A module-by-module PRD dump.
- Decorative visuals that do not explain spend, performance, optimization, or
  risk handling.
- One-note purple/blue gradient dominance.

## Content Mapping

Map source material into customer-visible concepts:

| Source PRD Area | H5 Customer Translation |
|---|---|
| 投流方模块 | Budget, strategy, monitoring, and review controls |
| 流量方模块 | Channel and placement performance visibility |
| 平台模块 | ROI, funnel, and anomaly analysis |
| 广告核心系统 | Cross-media account and campaign operations |
| 规则引擎 | No-code optimization and automated actions |
| 财务管理 | Spend, budget, recharge, and billing confidence |
| 数据埋点与三方对接 | Attribution and conversion feedback |
| 数据报表与实时监控 | Real-time dashboard and report loop |

## Output Path

Recommended prototype output:

- `wiki/reports/ad-growth-cockpit-h5.html`

The file should be a standalone HTML document that can be opened directly in a
browser. If the implementation needs local assets, keep them in a sibling folder
with stable relative paths.

## Verification

Minimum verification before claiming complete:

- Open the generated HTML in a browser or local server.
- Check mobile and desktop widths.
- Verify section navigation jumps.
- Verify KPI card click behavior.
- Verify channel view toggles.
- Verify alert expansion.
- Verify report CTA jump.
- Run `git diff --check`.

## Boundary

This is a prototype demo, not a production product. Mock numbers and demo
interactions are acceptable, but the story and interaction flow must feel useful
to an advertiser evaluating the product.

Because this is a reader-facing H5/share artifact, implementation must route
through the public report quality gate before any review-ready claim.
