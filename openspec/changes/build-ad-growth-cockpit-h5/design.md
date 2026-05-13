# Design: Ad Growth Cockpit H5

## Source And Audience

- Source: `inbox/ad-desgin.md`.
- Audience: advertisers and customer-side decision makers.
- Direction selected by user: Growth Cockpit.

The prototype should make the advertising system understandable as a live
growth-control cockpit: spend visibility, performance optimization, anomaly
handling, and report-driven next actions.

## Artifact

Create a standalone HTML file:

- `wiki/reports/ad-growth-cockpit-h5.html`

The page must open directly in a browser and use inline CSS/JavaScript only.
No external dependency, backend service, login, real API call, or asset pipeline
is required.

## Sections

1. `hero`: live cockpit with spend, conversions, ROAS, CPA, and budget signals.
2. `money-flow`: where spend goes across channels, plans, and creatives.
3. `optimization`: why performance improves through automatic bidding, budget
   allocation, creative selection, and rule-engine actions.
4. `anomalies`: how funnel drop, CPA overrun, traffic anomaly, and budget
   overrun are handled.
5. `review`: daily/weekly review, attribution, LTV, creative analysis, and next
   campaign suggestions.

## Interactions

- Navigation anchors jump between all five sections.
- KPI cards jump to related sections.
- Money-flow controls switch between channel, plan, and creative views.
- Alert cards expand to show recommended action and automation status.
- Review CTA jumps to the review section.

## Public Output Boundary

The prototype is a reviewable H5 demo, not a production product. Mock numbers
are allowed. The final record must preserve that boundary and state that there
is no Feishu sync or production rollout claim.
