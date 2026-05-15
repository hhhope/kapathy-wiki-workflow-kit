# Evaluation: add wiki review decisions

## Pressure Scenarios

### Positive: doctor diagnosis needs confirmation

- Input or situation shape: user asks to turn `wiki-doctor` findings into a
  confirmation sheet.
- Trigger condition: the request mentions confirm, review decision, 确诊,
  route, treatment candidate, or surgery candidate for doctor output.
- Expected route: use `wiki-review-decisions` and generate a draft decision
  record under `wiki/ops/wiki-review-decisions/` only when explicitly asked.
- Repo-visible artifact: `.codex/skills/wiki-review-decisions/SKILL.md` and
  `wiki/ops/wiki-review-decisions/*-review-decisions.md`.
- Expected output: draft buckets with detail refs and proof boundary.
- Promotion or non-promotion boundary: the record does not promote candidates
  into writes; treatment and surgery remain later workflows.
- Proof boundary: the record is routing evidence, not human approval.

### Negative should-not-trigger: user asks to repair frontmatter directly

- Input or situation shape: user asks to write frontmatter, taxonomy config,
  relation fields, MOC, ADR, AGENTS, or OpenSpec lifecycle state.
- Trigger condition: the request is write-capable repair rather than diagnosis
  confirmation.
- Expected route: do not use `wiki-review-decisions` as the repair executor;
  route to the appropriate later approved workflow or OpenSpec change.
- Repo-visible artifact: no review-decision record is required unless the user
  first asks to triage doctor findings.
- Expected output: boundary explanation or later workflow selection.
- Promotion or non-promotion boundary: `wiki-review-decisions` cannot promote
  diagnosis into writes.
- Proof boundary: repair proof must come from later treatment, surgery, or
  recovery workflows.

## RED Baseline

- Before this change, no `.codex/skills/wiki-review-decisions/SKILL.md` exists.
- Before this change, no `scripts/build_wiki_review_decisions.py` CLI exists.
- Before this change, no repo-visible review-decision record writer exists.

## GREEN Result

- To be updated after tests and validation run.

## Prior-Art / Common-Rule Dedupe

Scanned:

- Repo `AGENTS.md`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `openspec/changes/formalize-llm-wiki-medical-loop`
- `.codex/skills/wiki-doctor/SKILL.md`

Owns:

- `wiki-review-decisions` owns only the review/confirmation routing stage that
  converts doctor output into draft decision records.

References:

- `wiki-doctor` remains the diagnosis surface.
- The medical-loop OpenSpec remains the lifecycle vocabulary owner.
- Repo OpenSpec and AGENTS gates remain the lifecycle and workflow-change owner.

Rejects:

- This change rejects adding treatment, surgery, recovery, or direct wiki repair
  behavior to the review-decision skill.

## Residual Risks

- Local pressure evidence is the minimum gate; broader multi-session rollout
  proof remains future evidence.
- Review-decision records are draft routing artifacts until a human confirms
  them.
- Treatment and surgery execution still require separate changes.
