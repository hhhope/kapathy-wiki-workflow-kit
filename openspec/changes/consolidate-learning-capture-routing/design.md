## Design

Learning capture becomes a domain-router skill with module references, not a
replacement for the existing material-specific skills.

## Skill Shape

`learning-capture/SKILL.md` stays compact and owns only:

- when a request is learning
- when it is not learning
- what learning extracts
- which module to load next

Detailed workflow remains in references:

- `routing.md`: intent and material routing
- `article.md`: source-grounded article learning
- `repo-readme.md`: repository and README adaptation learning
- `example-reference.md`: structure / writing / output-shape references
- `pressure-scenarios.md`: trigger and non-trigger validation

## Routing Model

The first decision is user intent:

- learning intent: deep-read, learn capability, score, write wiki, extract
  reusable method, decide reuse / adapt / reject, or produce SOP
- non-learning intent: fact lookup, latest news, raw fetch, short abstract, or
  one-off digestion with no local reuse

The second decision is evidence object:

- article / blog / paper / WeChat post: article module
- GitHub / GitLab repo or README: repo-readme module
- concrete output, writing, visual, structure, or method example:
  example-reference module

## Compatibility Model

Existing skills remain valid triggers:

- `article-learning-capture` continues to handle article-specific workflows.
- `readme-learning-capture` continues to handle GitHub/GitLab README and repo
  workflows.

Both skills point back to `learning-capture` for general intent routing. This
keeps old triggers working while giving future agents a single first question:
"is this learning, and what object is being learned from?"

## Evidence Boundary

The domain router does not weaken existing gates. Module references retain the
strictest local requirements:

- article learning still requires source class, source grounding, score-first
  triage, copyright boundary, and promotion boundary
- repo-readme learning still preserves reused / modified / rejected /
  not-yet-formalized / repo target
- example-reference learning still preserves adaptation boundary and routes to
  the lowest durable repository layer

## Simplicity Boundary

This change intentionally avoids a larger framework:

- no dispatcher code
- no source ingestion automation
- no deletion of existing skills
- no new wiki page type
- no bulk rewrite of existing learning pages
