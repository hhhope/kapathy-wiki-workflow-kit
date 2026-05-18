# Design: wiki content adjudication skill

## Model

The new skill is a compact wrapper around the existing adjudication runtime.
It does not own the adjudication model; it points to:

- `scripts/build_wiki_content_adjudication.py`
- `scripts/wiki_content_adjudication.py`
- `wiki/evals/wiki-react-trace-cases.json`

## Trigger

Use when the user asks to inspect, judge, review, or audit content enrichment
candidates, especially:

- full detail set
- review focus set
- taxonomy candidate set
- drift trace set
- adjudication eval result

## Boundary

The skill is review-only:

- no frontmatter writes
- no taxonomy mutation
- no MOC writes
- no OpenSpec lifecycle changes
- no queued work execution

## Relationship To Existing Skills

- `wiki-react` remains the route classifier and decision-trace entry.
- `wiki-apply` remains the bounded execution/context preview.
- `wiki-content-adjudication` is the direct review-package inspection entry.
