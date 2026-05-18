# Design: wiki content enrichment preview

## Model

The enrichment preview is a deterministic advisory layer.

Inputs:

- page path
- current frontmatter
- title/body text
- frontmatter taxonomy config
- existing canonical objects from `wiki/ops`, `wiki/adr`, `openspec/specs`,
  and `wiki/examples`

Outputs:

- `suggested_frontmatter`
- `suggested_relations`
- `confidence`
- `needs_review`
- `evidence`
- `proof_boundary_notes`

## Scope

Initial coverage is only:

- `wiki/ops/**/*.md`
- `wiki/adr/**/*.md`

Other wiki layers stay out of scope because their domain and output rules are
different.

## Candidate Rules

Deterministic signals:

- path determines `layer`
- ADR path determines `domain: none`
- ops content keywords and existing fields suggest `ops_area`
- taxonomy known domains constrain domain candidates
- current `canonical_object` is preserved when valid
- otherwise filename/title suffixes suggest canonical object and artifact type
- explicit mentions of existing canonical objects suggest `related_objects`
- `derived_from`, `validates`, and `formalizes` are suggested only when the
  page already has those explicit fields or clear heading/frontmatter evidence

The preview must mark medium/low confidence suggestions as `needs_review`.

## Runtime Boundary

| Surface | Role | Boundary |
| --- | --- | --- |
| content enrichment preview | suggests frontmatter and relation candidates | does not write pages |
| status | reports pages needing enrichment review | does not write pages |
| apply | previews enrichment candidates | does not write pages |
| graph/MOC | consumes reviewed frontmatter | does not classify content |

## Verification

Verification should prove:

- ops/adr pages produce candidates with evidence
- existing valid frontmatter is preserved
- missing ops fields get suggestions
- status includes enrichment health
- apply output includes enrichment preview
- eval rejects traces that write frontmatter from enrichment preview
