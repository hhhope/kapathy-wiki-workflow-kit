## Context

The current replay harness is durable and reusable as documentation, but not yet executable.

That creates two remaining validation weaknesses:

- replay records can drift from the expected shape without an automatic failure signal
- pass/fail criteria still depend too much on free-form human interpretation

The repository does not need a full automation system here. It needs a small checker that can validate whether a replay record satisfies the minimum executable contract.

## Goals / Non-Goals

**Goals**

- Add a small executable checker for replay records.
- Keep the checker dependency-free and repo-local.
- Validate at least one sample replay record end-to-end.
- Keep the executable checker aligned with the documented harness fields and pass conditions.

**Non-Goals**

- Do not score replay quality with NLP.
- Do not parse arbitrary chat logs automatically.
- Do not replace the human judgment still needed for replay authoring.
- Do not claim rollout proof.

## Decisions

### Decision: Validate structured replay records, not raw conversations

The executable harness should consume a structured replay record, not raw chat transcripts.

Alternative considered:
- Parse free-form markdown or chat logs directly.
  - Rejected because that would require heuristic interpretation and would overstate what the checker can prove.

### Decision: Use JSON as the executable record format

The checker should use JSON so it can run with the standard library only.

Alternative considered:
- YAML-based records.
  - Rejected because standard Python does not include YAML support, and the repository does not need that dependency.

### Decision: Keep pass/fail criteria explicit through boolean checks

The executable checker should require explicit pass-condition fields rather than pretending to infer them from prose.

Required executable checks:

- `evolution_over_endpoint`
- `no_premature_abstraction`
- `unclear_state_allowed`
- `no_rollout_claim`

Alternative considered:
- Infer pass/fail from free-form summaries.
  - Rejected because it would be fake automation.

## Minimal Executable Record Shape

Top-level fields:

- `thread_label`
- `disagreement_shape`
- `rejected_framing`
- `correction_pressure`
- `redirection_moment`
- `clarity_state`
- `protected_target`
- `red_baseline`
- `green_result`
- `residual_risk`
- `checks`

`checks` fields:

- `evolution_over_endpoint`
- `no_premature_abstraction`
- `unclear_state_allowed`
- `no_rollout_claim`

## Verification Plan

This change should prove:

1. the checker fails on malformed or incomplete replay data
2. the checker passes on a valid sample replay
3. the harness page documents the executable usage

## Risks / Trade-offs

- [Risk] The executable harness may be mistaken for semantic proof. -> Mitigation: keep the checker honest and structural.
- [Risk] JSON records may feel less convenient than free-form markdown. -> Mitigation: keep the record shape minimal and keep markdown pages as the human-readable layer.
- [Risk] Contributors may skip the explicit checks. -> Mitigation: make them required fields and fail if absent.
