# Evaluation: formalize LLM-WIKI medical loop

## Behavior Replay

### Scenario: Future agent sees doctor output and user says to repair

- Input shape: user asks to act on a `wiki-doctor` diagnosis record.
- Trigger condition: diagnosis output contains review-focus, relation evidence,
  governance, ADR, MOC, or OpenSpec-sensitive findings.
- Expected route: explain that doctor is diagnosis-only and route to review,
  treatment, or surgery depending on confirmed scope.
- Repo-visible artifact: `wiki/ops/llm-wiki-self-evolution-medical-loop.md`.
- Expected non-output: no automatic frontmatter, taxonomy, relation, MOC, ADR,
  AGENTS, skill, or OpenSpec lifecycle mutation from diagnosis alone.
- Promotion boundary: execution capability requires later OpenSpec changes.
- Residual risk: the model gives vocabulary and boundaries, not executable
  enforcement.

### Scenario: Future agent sees 9 safe frontmatter candidates

- Input shape: doctor output reports `safe_to_apply_frontmatter=true` on a small
  subset.
- Trigger condition: user asks whether those can be fixed.
- Expected route: classify them as treatment candidates only after human review
  confirmation.
- Repo-visible artifact: future `wiki-review-decisions` record; not created by
  this change.
- Expected non-output: no automatic write from the safe flag alone.
- Promotion boundary: `add-wiki-review-decisions` and
  `add-wiki-treatment-workflow` must define the execution path.
- Residual risk: until those changes exist, the safe candidates remain
  diagnosis material.

### Scenario: Future agent sees broad governance and relation drift

- Input shape: doctor output reports high-volume weak relation evidence, drift,
  ADR, or OpenSpec-required reasons.
- Trigger condition: user says this is a large range and asks whether it is
  surgery.
- Expected route: classify as a surgery candidate and create or select a later
  OpenSpec plan before structural writes.
- Repo-visible artifact: future surgery OpenSpec change; not created by this
  change.
- Expected non-output: no batch relation acceptance or MOC projection write.
- Promotion boundary: `add-wiki-surgery-workflow` must define batching,
  no-touch zones, rollback, and recovery evidence.
- Residual risk: this change does not implement surgery planning templates.

## Prior-Art / Common-Rule Dedupe

- Repo `AGENTS.md` already owns workflow-change gating and OpenSpec lifecycle.
  This change references that boundary and does not restate git or health-check
  rules.
- ADR-0033 already separates wiki-react, eval, apply, repair labels, and
  OpenSpec. This change preserves that boundary and adds only the broader
  medical-loop vocabulary.
- `wiki-doctor` review records already define diagnosis evidence. This change
  does not change the skill; it places doctor in the larger lifecycle.
- `wiki-self-directed-execution` already defines bounded execution guidance.
  This change does not claim unrestricted autonomy or execution proof.

## Validation

- `openspec validate formalize-llm-wiki-medical-loop --strict`
  - Result: pass. OpenSpec reported `Change
    'formalize-llm-wiki-medical-loop' is valid` and exited 0. PostHog DNS flush
    warnings for `edge.openspec.dev` were telemetry-only.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/llm-wiki-self-evolution-medical-loop.md`
  - Result: bounded expected failure from pre-existing whole-wiki drift. The
    command exited 1 with `blocking_count: 780`, while the target page summary
    reported `entry_count: 0` and `entries: []`, so no blocker was reported for
    `wiki/ops/llm-wiki-self-evolution-medical-loop.md`.

## Residual Risks

- This change formalizes vocabulary and boundaries only.
- Review-decision, treatment, surgery, and recovery records still need separate
  OpenSpec changes.
- Existing whole-wiki frontmatter drift may still make broad frontmatter checks
  fail outside this change.
