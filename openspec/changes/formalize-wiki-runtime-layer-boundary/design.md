# Design: wiki runtime layer boundary

## Boundary Model

The repository distinguishes five responsibilities:

| Layer | Owns | Does not own |
| --- | --- | --- |
| `$wiki-react` | Explicit routing and `decision_trace` production for ambiguous or high-risk wiki requests. | Deterministic validation, repair execution, lifecycle approval. |
| `eval_wiki_decision_trace.py` | Validation of agent-produced traces against replay cases. | Natural-language intent classification, repair, OpenSpec approval. |
| `/wiki:apply` | Bounded preview of self-directed execution/context suggestions. | Direct runtime/script/skill/AGENTS mutation or repair execution. |
| Repair-route labels | Naming diagnostic repair classes such as `page-frontmatter-fix`, `taxonomy-config-fix`, `runtime-parser-fix`, and `readable-graph-fix`. | Proving that executable repair infrastructure exists. |
| OpenSpec | Lifecycle for runtime, workflow, skill, AGENTS, command behavior, and repair capability changes. | Being bypassed by routing, eval, scorecard, or apply previews. |

## Documentation Outputs

This change produces two wiki artifacts:

- `wiki/ops/wiki-runtime-react-eval-apply-boundary-distill-2026-05-14.md`
  records the source confusion and corrected model.
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md` records the stable
  decision.

The ops distill explains the incident context. The ADR records only the durable
decision and consequences.

## Relationship To Prior Work

- `wiki/ops/wiki-runtime-layer-contract.md` already describes the broad layer
  stack. This change makes the disputed boundary explicit.
- `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md` records the
  drift incident. This change extracts the stable architectural decision.
- `improve-wiki-routing-diagnostics` remains about diagnostics and command
  output. It is not reopened.

## Verification

Verification should confirm:

- OpenSpec validates the change.
- New ops and ADR pages have target-clean frontmatter.
- ADR index includes ADR-0033.
- No runtime scripts, skills, AGENTS, command docs, or completed change tasks
  are modified by this boundary formalization.
