# Lore Skill Change Eval

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This file records the required before/after evidence for the semantic Lore skill refactor.

Limitation:
- Single-session evaluation only
- No subagent or multi-session adversarial run was performed in this repo
- Results below prove documentation and gate behavior, not full runtime retrieval quality

---

## Behavior expected to change

1. Lore should stop competing with OpenSpec for lifecycle ownership
2. Lore should move from flat `LORE.md` memory to wiki-oriented memory
3. Skill edits should require explicit writing-skills / TDD evidence

---

## RED — Baseline before the refactor

### Scenario A — Lifecycle conflict

Prompt shape:
- large project task
- lore available
- OpenSpec available

Baseline behavior observed in the prior Lore wording:
- Lore still defined `req close` and `project close`
- Lore still centered task-start retrieval around `LORE.md`
- The skill text itself did not establish `tasks.md` as the only task-progress truth source

Why this is a fail:
- the agent could reasonably treat Lore as a competing lifecycle owner
- scope closure and progress truth were ambiguous

### Scenario B — Skill-change gate missing

Baseline behavior observed in the prior hook:
- changing `skills/*/SKILL.md` did not require any staged eval asset
- a semantic skill edit could be committed without before/after evidence

Why this is a fail:
- violates `writing-skills` and `development-workflow` requirements
- relies on author discipline instead of a gate

---

## GREEN — After the refactor

### Scenario A — Lifecycle split clarified

Observed after change:
- `skills/lore/SKILL.md` states:
  - OpenSpec owns `explore / propose / apply / archive`
  - Lore owns `query / log / synthesize / lint / reuse`
- `tasks.md` is explicitly defined as the only task-progress truth source
- `req close` / `project close` are no longer part of the active Lore workflow

Result:
- pass for wording-level lifecycle separation

### Scenario B — Skill-change gate added

Observed after change:
- `skills/lore/references/pre-commit` now blocks staged `skills/*/SKILL.md` edits unless a staged eval asset also exists
- accepted evidence patterns include:
  - `evals/*`
  - `references/*EVAL*`
  - `references/*BASELINE*`
  - `references/*TDD*`
  - `references/*PRESSURE*`

Result:
- pass for repository hook gate at the documentation/template layer

### Scenario C — Weekly review metrics made explicit

Observed after change:
- `skills/lore/SKILL.md` now requires weekly review to emit:
  - reviewed logs
  - absorbed logs
  - discarded logs
  - `absorbed-to` completion rate
  - absorption success rate
  - destination page-type distribution
- `skills/lore/evals/PRESSURE-RESULTS.md` now records those metrics from a 10-log corpus run

Result:
- pass for weekly-review metrics as a measurable Lore-owned output

---

## REFACTOR notes

Remaining gaps:
- no live OpenSpec fixture in this repo, so gate behavior is not yet tested against real apply/archive commands
- no retrieval corpus, so recall/noise metrics remain unproven
- no multi-session adversarial pressure test was run
 - pressure results are corpus-driven and command-level, not a blind multi-session live-agent run

Next stronger validation:
1. add a minimal fixture wiki corpus
2. add a fixture OpenSpec change tree
3. run the same scenarios as command-level tests
4. make weekly review report mandatory metrics explicit and measurable
