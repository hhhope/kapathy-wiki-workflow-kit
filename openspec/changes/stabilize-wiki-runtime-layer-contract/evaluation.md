# Evaluation: stabilize wiki runtime layer contract

## Scope

This evaluation covers the repo-visible wiki runtime layer contract, README
runtime usage model, active spec naming cleanup, and anti-drift checks.

## Prior-Art / Common-Rule Dedupe

- Existing repo `AGENTS.md` owns the wiki runtime stack table, OpenSpec
  lifecycle boundary, behavior replay gate, and frontmatter taxonomy gate.
- Existing `.codex/skills/wiki-*` files own concrete skill trigger behavior.
- Existing scripts own deterministic observations and validation.
- This change does not restate full taxonomy vocabulary, add new routing
  algorithms, restore plugin runtime, or promote obsolete slash command runtime.
- This change owns only the missing layer contract and README usage map that
  connects the already-existing layers.

## Pressure Scenarios

| Scenario | Expected behavior |
|---|---|
| User asks for current wiki health | Use `wiki-status`; do not route through repair by default. |
| User asks for ambiguous or high-risk wiki repair | Use `wiki-react` as explicit router and emit `decision_trace` before action. |
| User asks whether evidence is strong enough | Use `wiki-scorecard` as observation; do not treat it as behavior approval. |
| Runtime behavior change is proposed | OpenSpec owns workflow/runtime change lifecycle. |
| Python precheck returns facts | Treat output as observation or validation, not natural-language intent classification. |

## RED Baseline

Before the README and layer contract were aligned, the new anti-drift test
failed because:

- `wiki/ops/wiki-runtime-layer-contract.md` did not expose all exact layer and
  gate contract markers.
- README did not contain machine-checkable skill-use mapping such as
  `status -> wiki-status` and `uncertain/high-risk -> wiki-react`.
- Active OpenSpec spec paths still contained obsolete `slash-command` naming.

## GREEN Result

The implementation adds:

- `wiki/ops/wiki-runtime-layer-contract.md` with an ASCII architecture diagram
  and six explicit layers.
- README sections for wiki runtime architecture and skill selection.
- Active spec renames from obsolete slash-command paths to skill-surface paths.
- `tests/test_wiki_runtime_layer_contract.py` to keep the contract from drifting.

## Behavior Replay Evidence

Input shape:

- User asks what the wiki runtime architecture is, how to use it, and why
  `wiki-react`, `wiki-status`, `wiki-apply`, scorecard, eval, and OpenSpec keep
  drifting.

Trigger condition:

- The request concerns repo-default wiki runtime behavior and active runtime
  naming.

Expected route:

- Start from README and `wiki/ops/wiki-runtime-layer-contract.md`.
- Use direct domain skills when the requested surface is already clear.
- Use `wiki-react` only when ambiguity, risk, or cross-boundary action requires
  explicit routing and `decision_trace`.

Expected non-route:

- Do not claim obsolete slash/plugin runtime as the current entrypoint.
- Do not let Python prechecks replace intent routing.
- Do not let scorecard, trace eval, behavior checker, or OpenSpec substitute
  for each other.

Repo-visible artifact future agents should read:

- `README.md`
- `wiki/ops/wiki-runtime-layer-contract.md`
- `openspec/specs/wiki-runtime-skill-surface/spec.md`
- `openspec/specs/wiki-status-skill/spec.md`

Proof boundary:

- This change documents and gates the current architecture.
- It does not add new runtime capability, change scorecard algorithms, change
  eval case semantics, or repair historical frontmatter drift.

## Verification

- `python3 -m unittest tests.test_wiki_runtime_layer_contract`
  - Result: `Ran 4 tests ... OK`
- `python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_wiki_decision_trace_eval tests.test_wiki_graph_extraction_identity`
  - Result: `Ran 23 tests ... OK`
- `python3 -m unittest tests.test_wiki_runtime_layer_contract tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_wiki_decision_trace_eval tests.test_wiki_graph_extraction_identity`
  - Result: `Ran 27 tests ... OK`
- `find openspec/specs -path '*slash-command*' -print`
  - Result: no output
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/wiki-runtime-layer-contract.md`
  - Result: non-zero because full repo historical drift still has
    `blocking_count: 769`
  - Target result: `entry_count: 0` for `wiki/ops/wiki-runtime-layer-contract.md`
- `python3 scripts/check_behavior_assets.py`
  - Result: exit 0
- `openspec validate stabilize-wiki-runtime-layer-contract --strict`
  - Result: valid
  - Note: PostHog telemetry DNS flush emitted `EAI_AGAIN` after validation; it
    did not change the valid result.

## Residual Risks

- Full frontmatter taxonomy still fails on legacy pages outside this change.
- The architecture is now documented and tested, but future semantic skill
  changes still need their own behavior replay and evaluation evidence.
