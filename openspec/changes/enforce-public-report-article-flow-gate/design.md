## Context

The public-report gate already requires reference structure maps, voice checks,
paragraph drift review, and judgment ownership. Those checks are necessary but
not enough for visual/article composition drift.

In the company playbook case, the facts and company judgments improved before
the page quality did. The remaining failure was structural: a reference-shaped
newspaper page still behaved like a dashboard/table report. Future agents need a
small, explicit gate that forces them to check composition style before claiming
the draft is review-ready.

## Design

### Article Flow Layout Gate

For reader-facing drafts that cite a newspaper/article/report reference, the
gate records the intended layout system:

- newspaper article flow
- card / dashboard / comparison grid
- visual one-pager
- Feishu review document
- other named reference system

When the chosen system is newspaper article flow, the draft should use:

- continuous section rhythm
- prose paragraphs
- evidence ledgers or reference lines
- numbered or consensus lines for compressed comparisons
- major section rules rather than repeated boxed cards

It should reject:

- card-wall endings
- repeated table/cell structures for prose-heavy content
- colored panel taxonomies when the reference is neutral newspaper
- prompt text, Hybrid instructions, or visual-script residue inside the report
  body

### Gate Review Evidence

Gate-review artifacts record:

- reference layout system
- retained patterns
- rejected patterns
- visual/article composition drift result
- replay notes when a draft was repaired from card/table layout to article flow

### Pressure Replay

Pressure scenarios cover the failed shape:

- a company-analysis newspaper reference becomes repeated company cards
- a final takeaway becomes a 2x2 card wall
- visual-generation prompt text leaks into the report body
- the gate review calls the draft retained even though the user rejected the
  composition

## Boundaries

- This gate does not require every report to use article flow.
- It applies only when the reference or user request calls for an article /
  newspaper report shape.
- It does not replace visual generation skills for final image assets.
- It does not make existing drafts review-ready retroactively.
