# Design

## Runtime Boundary

The repository cannot rely on editing third-party plugin skills. The repo-local
contract owns the bridge from PM/product-discovery analysis to wiki records.

The route applies when the user invokes PM/product-discovery style work and at
least one of these signals is present:

- explicit wiki recording intent
- durable memory or "record this" intent
- reuse in later PRD, report, OpenSpec, or product strategy work
- correction that prior PM/product-discovery output should have been captured

The route does not apply to one-off product questions, quick market framing, or
latest-news lookup with no local reuse or wiki intent.

## Wiki Output Shape

Captured product-discovery notes default to `wiki/ops/` because they preserve
working assumptions, opportunity framing, and validation plans rather than raw
upstream source evidence.

If the PM/product-discovery work is grounded in external articles, repos,
papers, or examples, `learning-capture` remains the parent gate for the source
learning portion. The product-discovery capture can reference that learning
record, but must not replace source grounding.

If the output becomes reader-facing or repo-public, `public-report-quality-gate`
still applies. If wiki frontmatter is created or edited,
`wiki-frontmatter-taxonomy` still applies.

## Skill Shape

Add `.codex/skills/product-discovery-wiki-capture/SKILL.md` as a compact
repo-local bridge skill.

The skill owns:

- trigger conditions for PM/product-discovery durable capture
- output target boundary
- parent-gate preservation
- minimum capture fields
- non-trigger cases

Minimum capture fields:

- source prompt or situation
- product discovery route used
- target segment / ICP
- opportunity framing
- assumptions and risks
- validation experiments
- what was not formalized
- next step

## Proof Boundary

Tests and evaluation prove repo-visible routing and replay behavior. They do not
prove every future AI client will load the repo-local bridge unless it honors
repo `AGENTS.md` and skill routing.
