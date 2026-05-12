## Context

The user rejected the earlier hard-rule wording because it read as a local
patch for one bad output. That critique is correct: a skill should teach a
durable behavior, not memorize one page's failure vocabulary.

The durable behavior is output-shape fidelity:

1. identify the selected output shape from the user request or reference;
2. draft within that shape;
3. fail if the primary structure is replaced without explicit user approval;
4. keep production-route notes out of reader-facing content.

## Design

### Reference Output Shape Gate

The gate applies when the user or a reference artifact establishes an output
shape, including:

- article/report flow
- Feishu review document
- visual one-pager
- card/grid page
- dashboard
- image brief
- another named form

The gate records:

- selected output shape
- retained patterns
- rejected patterns
- user-approved shape changes
- replay result

### Observable Failures

The gate fails when:

- a linear article/report becomes a modular grid or repeated block system as
  the primary body without explicit user approval;
- a reference-led narrative becomes a comparison table as the primary body
  without explicit user approval;
- an image brief, H5/share page, Feishu review document, or other named form is
  changed to another form without explicit user approval;
- production instructions, image prompts, tool notes, or Hybrid routing text
  appear inside reader-facing content.

### Boundary

This gate is not a style preference. It does not ban any visual or structural
form. It only blocks silent replacement of the selected output shape and
reader-facing leakage of production notes.

Incident examples stay in pressure scenarios where they help replay the
original failure. They should not be promoted into the compact `SKILL.md` hard
rule as subjective or overly narrow vocabulary.
