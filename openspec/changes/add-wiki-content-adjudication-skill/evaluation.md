# Evaluation: wiki content adjudication skill

## Evidence

- `python3 -m unittest tests/test_wiki_runtime_skills.py`
  - RED baseline: failed because
    `.codex/skills/wiki-content-adjudication/SKILL.md` did not exist.
  - GREEN result: passed, 5 tests.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- `openspec validate add-wiki-content-adjudication-skill --strict`
  - Result: passed.
  - Concern: OpenSpec printed PostHog network flush warnings for
    `edge.openspec.dev`, but the validation command exited successfully.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: user asks for content adjudication package | Direct skill references adjudication script and review sections | Passed |
| Negative: user wants candidates applied | Skill keeps review-only boundary and forbids frontmatter/taxonomy writes | Passed |

## RED Baseline

Input or situation shape: content adjudication runtime exists, but the only
skill routes are `wiki-react` and `wiki-apply`.

Trigger condition: user asks whether the adjudication script has a matching
skill.

Observed failure before this change: `.codex/skills/wiki-content-adjudication`
does not exist.

## GREEN Result

Expected route:

```text
wiki-content-adjudication -> build_wiki_content_adjudication.py ->
review package summary -> explicit reviewed write later
```

Repo-visible artifact:
`.codex/skills/wiki-content-adjudication/SKILL.md` and
`tests/test_wiki_runtime_skills.py`.

Expected output: a direct skill entry that explains how to inspect
`full_detail_set`, `review_focus_set`, `taxonomy_candidate_set`,
`drift_trace_set`, and `eval_result`.

Promotion or non-promotion boundary: the skill is review-only and does not
promote adjudication output into frontmatter or taxonomy config.

Proof boundary: the skill improves routing ergonomics only; it does not change
the adjudication model.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `.codex/skills/wiki-react/SKILL.md`
- `.codex/skills/wiki-apply/SKILL.md`
- `openspec/changes/add-wiki-content-adjudication-eval/design.md`

Owns:

- Direct skill entry for content adjudication review-package inspection.

References:

- Existing `wiki-react` route classifier.
- Existing `wiki-apply` preview boundary.
- Existing content adjudication runtime.

Rejects:

- Slash command surface.
- Direct structure writes.
- Duplicating the adjudication model inside the skill body.

## Parent Gate Preservation

Parent gate: this skill is a review-package inspection wrapper and preserves
the wiki runtime boundaries.

## Residual Risks

- Users may still expect the skill to apply accepted candidates; the boundary
  must stay explicit.
