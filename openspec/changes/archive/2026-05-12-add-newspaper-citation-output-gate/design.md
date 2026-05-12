## Context

Existing gates distinguish two internal artifacts:

- source maps: which sources support which claims;
- learning use maps: which learned patterns shaped the output.

Those maps are process evidence. They do not guarantee that a reader-facing
newspaper, H5, or share package shows a citation route to the reader.

Newspaper-style outputs need a stricter surface because they combine narrative,
visual panels, evidence tables, and shareable screenshots. A reader may consume
the HTML, exported images, or share package without opening the internal wiki
source map.

## Decision

Add a Newspaper Citation Surface Gate.

For newspaper-style public drafts and H5/share packages, the gate requires a
reader-visible citation surface before review-ready, publish, sync, or share
claims. The citation surface may be a source note section, footnote block,
panel-level citation row, appendix, or linked source index, but it must be
visible from the output path the reader receives.

## Citation Surface Contract

The citation surface records:

- output artifact path;
- source map artifact path;
- load-bearing claim or visual panel;
- public citation target for that claim or panel;
- source class such as primary, secondary, practitioner, transcript mirror, or
  candidate;
- boundary note when the citation is not strong enough for a hard fact claim.

## Internal Evidence vs Reader Citation

Learning use maps remain internal process evidence. They can explain why a
source changed structure, visual grammar, proof style, or boundary wording.

Reader-visible citations are separate. They explain why a reader should trust a
claim, number, company example, or visualized evidence relationship in the
newspaper.

The same source can appear in both maps, but the purpose must be explicit.

## Reference Case

Use the AI Agent Product Engineering Collaboration newspaper as the first replay
case:

- output: `wiki/reports/agentic-product-engineering-collaboration-newspaper.html`
- gate review:
  `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`
- source map:
  `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`
- report index citation:
  `wiki/reports/index.md` lists the H5 as "draft H5 newspaper for the
  AI-agent-era product-engineering collaboration thesis, debate map, timeline,
  company camps, and local operating principles"

## Boundaries

- This gate does not require every sentence to carry a citation.
- This gate does not turn internal wiki paths into public citation text by
  default.
- This gate does not allow weak secondary material to become hard evidence.
- This gate does not publish or repair the current newspaper automatically.
- If the user asks for a private worklog only, this gate does not apply.
