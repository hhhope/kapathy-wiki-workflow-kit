## Context

The repo already emits a generated wiki manifest and status report. Today that
surface counts wiki pages, source records, inbox representation, and OpenSpec
task state. It answers "what is visible" but not "what product state does this
object represent?"

The product alignment trace named the missing contract:

```text
object type
target state
evidence required
score type
source layer
readiness label
next status transition
```

This change should add the smallest computable version of that contract.

## Design

### Product Status Contract

Define a compact vocabulary:

| Field | Purpose |
|---|---|
| `object_type` | Classifies the product object as source, learning, structure, output, behavior, status, or governance. |
| `target_state` | Names the intended product state when it is explicitly declared or conservatively derived. |
| `source_layer` | Names the layer that currently owns the evidence: inbox, source, ops, report, spec, archive, or generated status. |
| `readiness_label` | Classifies the object as `invalid`, `draft-only`, `blocked`, `unresolved`, `review-ready`, or `accepted`. |
| `evidence_required` | Names the evidence class needed before a higher readiness label is allowed. |
| `score_type` | Distinguishes no score, diagnostic score, admission score, quality score, or behavior replay result. |
| `status_transition` | Names the next expected movement through the product backbone. |

The contract is strict by default:

- unclear target -> `invalid` or `draft-only`;
- clear target with missing evidence -> `blocked`;
- unresolved routing or ownership pressure -> `unresolved`;
- hard gate failure -> no quality score, only diagnostics;
- future behavior claim -> replay evidence or no behavior-ready claim.

### Minimal Status Computation

The first implementation should infer only conservative fields from already
available repository data:

- wiki section and frontmatter for object type, source layer, identity, and
  explicit relation coverage;
- `source_path` representation for source evidence;
- OpenSpec task state for governance readiness;
- existing status fields when present;
- pending inbox and complete active-dir changes as blocked or action-needed
  pressure.

Do not invent semantic readiness from prose. If a field cannot be inferred from
explicit structure, mark it as `unknown` and include a reason.

### Manifest Shape

Add a top-level `product_status` object to `wiki/status/manifest.json`:

```json
{
  "contract_version": "1",
  "object_type_counts": {},
  "readiness_counts": {},
  "source_layer_counts": {},
  "identity_coverage": {},
  "relation_coverage": {},
  "unresolved_items": []
}
```

`unresolved_items` should be a short, bounded list of visible blockers or
inspection prompts, such as pending inbox files, complete unarchived OpenSpec
changes, missing explicit identity, missing explicit relations, and unknown
readiness pressure.

### Markdown Status Shape

Add a `Product Status` section to `wiki/status/wiki-status.md` with:

- contract version;
- object type counts;
- readiness counts;
- source layer counts;
- identity and relation coverage;
- unresolved items or "None".

The status report remains a visibility artifact. It does not open, modify, or
archive OpenSpec changes, and it does not execute queued work.

## Testing

Add focused tests around `scripts/build_wiki_status.py`:

- manifest includes `product_status.contract_version`;
- representative source records count as `source`;
- pending inbox files create unresolved product-status items;
- complete OpenSpec changes create archive-review pressure;
- rendered markdown includes the `Product Status` section.

## Non-Goals

- Do not implement graph UI or whole-wiki semantic scoring.
- Do not implement a graph export or relation-analysis rewrite.
- Do not change public report quality gate behavior.
- Do not change learning-capture admission rules.
- Do not build an autonomous task queue.
- Do not clean unrelated dirty worktree material.
- Do not claim product readiness from prose-only inference.
