---
canonical_object: learning-source-routing-gap
artifact_type: explore-trace
related_objects:
- learning-capture-routing
- example-driven-capture
- obsidian-wiki-reference-gap-review
derived_from:
- wiki/index.md
- wiki/ops/learning-capture-routing.md
- wiki/ops/example-driven-wiki-capture.md
- .codex/skills/learning-capture/SKILL.md
- .codex/skills/readme-learning-capture/SKILL.md
---

# learning-source-routing-gap / explore-trace

## Trigger

User asked why original learning material handled during `$openspec-explore`
does not enter `wiki/sources`.

## Explore Boundary

This is `$openspec-explore`: thinking and requirement shaping only.

No routing rule, skill, source page, or OpenSpec change has been implemented in
this trace.

## Current Read

Current repository guidance separates:

```text
wiki/sources
  raw upstream evidence

wiki/ops
  workflow learning, governance learning, traces, retros, decisions-in-progress
```

`readme-learning-capture` currently requires preserving source URL, reused /
modified / rejected / repo target, and adaptation boundary. It does not require
creating a separate `wiki/sources` record for the external repo or README text.

`example-driven-wiki-capture` also says not every external link gets a new page.
It requires a wiki record when reusable learning has already been extracted, but
its default route for workflow/governance learning is `wiki/ops`.

## Working Answer

The original source does not enter `wiki/sources` today because the current
rule optimizes for learning capture, not source intake:

```text
external repo / README
  -> learning admission + score
  -> ops learning note with source URL and adaptation boundary
  -> no automatic source mirror
```

This prevents turning every external link into a source page, but it creates a
gap for high-value deep-read sources: there is no local source-layer artifact
that records the original source grounding, access shape, and preserved excerpt
boundary.

## Gap

For deep-read learning sources, current routing should probably become:

```text
external source
  -> wiki/sources/<source-record>.md
       source metadata, access date, source class, retrieved paths,
       short compliant excerpt/summary, source boundary
  -> wiki/ops/<learning-note>.md
       reused / modified / rejected / repo target / next step
```

The source record should not copy full copyrighted or large external content.
It should preserve enough provenance to make the learning note auditable.

## Open Question

Should this become a default for all deep-read learning sources scoring 75+,
or only when the source is expected to influence product planning, skills,
OpenSpec, report output, or future runtime behavior?

## Non-Decisions

- No source page is created in this trace.
- No skill routing rule is changed in this trace.
- No OpenSpec proposal is opened in this trace.
