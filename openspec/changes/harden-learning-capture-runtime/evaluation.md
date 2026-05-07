## RED Baseline

Date: 2026-05-07

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Runtime trigger exists for external-source learning | repo `AGENTS.md` High-Frequency Skills does not list `.codex/skills/learning-capture/SKILL.md`. | FAIL |
| Repo/README learning has a scorecard and 75-point deep-read threshold | `.codex/skills/readme-learning-capture/SKILL.md` has an output checklist but no admission gate, scorecard, or threshold. | FAIL |
| Article learning rejects retrospective score as score-first evidence | Article scorecard requires scoring before deep reading, but current guidance does not name retrospective score as non-admission evidence. | FAIL |
| Explicit topic such as agent / harness anchors to existing wiki topic | `learning-capture` does not require checking existing wiki topic anchors before durable notes. | FAIL |
| Unclear topic becomes weekly-review candidate | `learning-capture` does not name weekly review as the outlet for weak topic matches. | FAIL |
| Batch article intake limits deep-read cost | `learning-capture` and article guidance do not explicitly say batch intake defaults to triage before deep reading. | FAIL |

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Runtime trigger exists for external-source learning | repo `AGENTS.md` High-Frequency Skills lists `.codex/skills/learning-capture/SKILL.md`. | PASS |
| Repo/README learning has a scorecard and 75-point deep-read threshold | `readme-learning-capture` now points to `references/scorecard.md` and records 75+ / 60-74 / below-60 bands. | PASS |
| Article learning rejects retrospective score as score-first evidence | Article skill and scorecard require retrospective scores to be marked and excluded from score-first admission evidence. | PASS |
| Explicit topic such as agent / harness anchors to existing wiki topic | `learning-capture` and routing reference require checking existing topic anchors when the user names a topic or source strongly matches index/title/path. | PASS |
| Unclear topic becomes weekly-review candidate | `learning-capture` and routing reference require weak matches to remain weekly-review candidates. | PASS |
| Batch article intake limits deep-read cost | `learning-capture` pressure scenarios and hard rules require batch triage before deep reading; module thresholds govern deep-read. | PASS |
| Output routing remains separate from runtime trigger | `AGENTS.md` lists `learning-capture` under High-Frequency Skills and keeps `Output Routing` as destination rules. | PASS |

## Residual Risks

- The pressure evidence is static/manual, not multi-session rollout proof.
- Weekly review is defined as a candidate outlet but not automated.
- Existing historical learning pages may still contain retrospective scores or
  weak source grounding until reviewed separately.
- The current change does not migrate wiki directory structure.
