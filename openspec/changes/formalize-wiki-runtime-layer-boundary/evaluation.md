# Evaluation: wiki runtime layer boundary

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: owns repo-local hard stops and routing defaults, but should not
  carry the detailed runtime layer model.
- `PROJECT.md`: defines OpenSpec and wiki as durable knowledge layers.
- `wiki/ops/wiki-runtime-layer-contract.md`: already states the broad layer
  contract for skills, decision traces, observation tools, boundaries, eval,
  and lifecycle gates.
- `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`: records the
  incident where the layers were confused.
- `openspec/specs/wiki-self-directed-execution/spec.md`: owns bounded
  self-directed execution output, not repair execution.
- `openspec/changes/improve-wiki-routing-diagnostics/design.md`: names repair
  routes as diagnostic route labels.
- `openspec/changes/introduce-wiki-react-decision-trace-eval/design.md`: owns
  the decision-trace eval contract.

Classification:

- Owns: ADR-0033 owns the stable decision that wiki runtime layers must not
  substitute for each other.
- References: existing runtime layer contract, decision-trace eval design,
  self-directed execution design, and routing diagnostics design provide the
  source material.
- Rejects: the 2026-05-14 incident is not promoted wholesale into ADR; only the
  stable layer boundary is promoted.

## Pressure Scenarios

Positive trigger scenario:

- Input or situation shape: user asks whether EVAL should fix a wiki runtime
  problem and mentions `/wiki:apply` repair routes.
- Trigger condition: the explanation may substitute routing, trace validation,
  apply preview, repair labels, or OpenSpec lifecycle for each other.
- Expected route or stop behavior: explain each layer's ownership separately
  and state that runtime or workflow behavior changes still route through
  OpenSpec.
- Expected output: a boundary explanation that cites `$wiki-react`, eval,
  `/wiki:apply`, repair-route labels, and OpenSpec as separate layers.

Negative should-not-trigger scenario:

- Input or situation shape: user asks only for current graph node counts or
  status summary.
- Expected route or stop behavior: use `/wiki:graph` or `/wiki:status`; do not
  force a full layer-boundary explanation.
- Expected output: structural or status summary only.

Parent gate preservation:

- `$wiki-react` remains the explicit router and decision-trace entrypoint.
- Trace eval remains validation only.
- `/wiki:apply` remains preview only.
- OpenSpec remains lifecycle owner for behavior changes.
- The brainstorming drift trace remains incident evidence, not the ADR itself.

## RED Baseline

Before this change, the broad runtime layer contract existed but the disputed
boundary was not decision-recorded in one stable ADR.

Observed failure:

- repair-route labels were described as if executable repair infrastructure
  existed
- trace eval was used as if it proved a repair path
- `/wiki:apply` was treated as if it could execute repairs
- OpenSpec lifecycle was blurred with preview and validation surfaces

## GREEN Result

After this change:

- `wiki/ops/wiki-runtime-react-eval-apply-boundary-distill-2026-05-14.md`
  preserves the explanation and correction context.
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md` records the stable
  decision.
- `openspec/changes/formalize-wiki-runtime-layer-boundary/specs/wiki-runtime-layer-boundary/spec.md`
  defines SHALL-level requirements for layer separation.
- `wiki/adr/index.md` links ADR-0033.

## Behavior Replay Evidence

Input or situation shape:

```text
User asks whether $wiki-react, EVAL, /wiki:apply, repair routes, and OpenSpec
are being confused while discussing wiki runtime repair.
```

Trigger condition:

```text
The answer would otherwise treat one runtime layer's output as proof of another
runtime layer's capability.
```

Expected route:

```text
Explain layer ownership:
$wiki-react routes and emits decision_trace.
eval validates traces only.
/wiki:apply previews bounded suggestions.
repair-route labels classify diagnostics.
OpenSpec owns lifecycle and capability changes.
```

Repo-visible artifact future agents should read:

```text
wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md
wiki/ops/wiki-runtime-react-eval-apply-boundary-distill-2026-05-14.md
```

Expected output:

- a layer-by-layer boundary explanation
- no claim that eval fixes repairs
- no claim that `/wiki:apply` executes repairs
- no claim that route labels prove implementation exists

Expected non-output:

- no runtime script changes
- no skill changes
- no AGENTS changes
- no reopening of `improve-wiki-routing-diagnostics`

Promotion or non-promotion boundary:

The stable boundary is promoted to ADR-0033. The drift incident remains in
`wiki/ops` as evidence and is not itself the ADR decision.

Proof boundary:

This evaluation proves that the stable decision and supporting distill exist. It
does not prove new runtime enforcement or executable repair infrastructure.

## Residual Risks

- Agents may still need to read ADR-0033 or the ops distill to apply the
  boundary in conversation.
- This change does not add a machine-readable repair-route schema.
- This change does not modify `/wiki:apply` output or eval behavior.

## Verification Commands

Run:

```bash
openspec validate formalize-wiki-runtime-layer-boundary --strict
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/wiki-runtime-react-eval-apply-boundary-distill-2026-05-14.md
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md
python3 scripts/check_behavior_assets.py
```

Expected:

- OpenSpec validation passes.
- Frontmatter precheck may report existing whole-wiki debt, but both new target
  pages report `target.entry_count: 0`.
- Behavior asset checker passes.

Observed on 2026-05-14:

- `openspec validate formalize-wiki-runtime-layer-boundary --strict`: passed
  with `Change 'formalize-wiki-runtime-layer-boundary' is valid`. The command
  also printed non-blocking PostHog network flush errors.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/wiki-runtime-react-eval-apply-boundary-distill-2026-05-14.md`:
  exited non-zero because of existing whole-wiki frontmatter debt, with
  `blocking_count: 767`; the new target reported `target.entry_count: 0`.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`:
  exited non-zero because of existing whole-wiki frontmatter debt, with
  `blocking_count: 767`; the new target reported `target.entry_count: 0`.
- `python3 scripts/check_behavior_assets.py`: passed with exit code 0.
