# Design: Refine Account H5 AI Offering And Style

## Visual Direction

Use a quiet internal technical-training style rather than a comic/poster style.
The page should feel like an engineering onboarding material: readable, dense
enough for domain learning, but not visually harsh.

Key decisions:

- Background: remove graph-paper noise and use a neutral page tone.
- Containers: reduce border width, radius, and shadow; make sections feel like
  structured panels rather than stickers.
- Cards: use a consistent left accent / light border model and avoid thick
  black outlines on every repeated item.
- Typography: keep strong headings, but reduce underline/decoration and make
  body text easier to scan.
- Visual assets: keep source-backed diagrams as the dominant proof surfaces.
  Do not replace them with decorative CSS art.

## AI Section Direction

The section should answer: "账户组能给 AI 协作提供什么?" before listing tools.

Required framing:

- Account domain map: objects, chain positions, account/accounting/balance /
  clearing / reconciliation boundaries.
- Account Harness: reusable constraints, gates, source-to-output mapping, and
  evidence retention for account-domain work.
- Source material: design docs, project reports, diagrams, reconciliation
  cases, and onboarding notes after sensitive information is filtered.
- Verification evidence: fields, states, ledger entries, balance movement,
  clearing result, reconciliation difference, screenshots, command outputs, and
  review notes.
- Human judgment: product/accounting/risk decisions remain owned by engineers;
  AI can organize, compare, draft, inspect, and verify under constraints.

## Verification

- HTML parser.
- Required AI-offering phrase grep.
- Removed rough-style / tool-first phrase grep where applicable.
- Sensitive-info grep across H5.
- Desktop and mobile screenshot inspection.
- `git diff --check`.
- `openspec validate refine-account-h5-ai-offering-style --strict`.
