# Evaluation: default medical loop records

## Behavior Replay

- Input or situation shape: user invokes `wiki-doctor` or `wiki-confirm` as a
  medical-loop stage.
- Trigger condition: diagnosis or confirmation is requested, including Chinese
  stage language such as `诊断` or `确诊`.
- Expected route or stop behavior: the stage writes a complete repo-visible
  record by default, then reports a compact stdout summary and path.
- Repo-visible artifact: diagnosis records under `wiki/ops/wiki-doctor-runs/`
  and confirmation records under `wiki/ops/wiki-review-decisions/`.
- Expected output or non-output: stdout is a summary, not the source of record;
  `--stdout-json-only` is required for non-writing JSON inspection.
- Promotion or non-promotion boundary: records do not approve treatment,
  surgery, frontmatter, taxonomy, relation, MOC, ADR, or OpenSpec changes.
- Residual risk or proof boundary: records are deterministic routing evidence;
  human confirmation is still needed before treatment or surgery.

## RED Baseline

To be filled during implementation.

## GREEN Result

To be filled during implementation.

## Prior-Art / Common-Rule Dedupe

To be filled before completion because this change semantically updates
repo-local behavior assets.
