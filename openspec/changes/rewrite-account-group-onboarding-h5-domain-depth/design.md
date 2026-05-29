# Design: Account Group Onboarding H5 Domain Rewrite

## Approach

The rewrite keeps the approved chapter order but changes the depth standard.
The H5 must stop reading like a generic newcomer guide and start reading like
an account-domain engineering map.

## Content Model

The page has fifteen screens:

1. Cover.
2. Account-group engineering boundary.
3. Account capability map.
4. System architecture.
5. Core business chain.
6. Business objects.
7. Typical problems.
8. Active project entries.
9. Technical planning.
10. AI collaboration system.
11. AI Coding maturity.
12. Three-day and first-week path.
13. 30/60/90 growth path.
14. Task pool and gained capabilities.
15. Closing.

## Visual Model

- Capability map: dense node graph with grouped capability clusters.
- System architecture: layered stack from entrance to data and external
  connections.
- Core chain: horizontal or wrapped flow with domain checkpoints.
- Project entries: cards with domain position, what changes, newcomer task, and
  trained capability.
- AI sections: engineering workflow cards tied to account-domain work.

## Sensitive Boundary

The H5 may name business products and capability names, but must not include
personal contacts, credentials, internal test URLs, group QR codes, Feishu
source URLs, token strings, or account-opening access instructions.

## Verification

Verification must include HTML parser, revised source-to-screen coverage,
required content grep, excluded capability grep, sensitive-info grep, desktop
screenshot, mobile screenshot, and `git diff --check`.
