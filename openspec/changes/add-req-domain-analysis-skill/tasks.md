# Tasks

- [x] 1. Add OpenSpec spec for req-domain-analysis behavior.
- [x] 2. Add `.codex/skills/req-domain-analysis/SKILL.md`.
- [x] 3. Update `.codex/skills/req-agent/SKILL.md` worker routing.
- [x] 4. Add behavior evaluation evidence with pressure scenarios, RED baseline, GREEN result, residual risks, and prior-art dedupe.
- [x] 5. Run behavior-asset validation.
- [x] 6. Run OpenSpec validation.
- [x] 7. Record verification results.

## Verification

- RED baseline:
  - `test -e .codex/skills/req-domain-analysis/SKILL.md; echo $?` -> `1`
  - `rg -n "req-domain-analysis|req-scope|Worker routing|domain" .codex/skills/req-agent/SKILL.md .codex/skills/req-intake/SKILL.md .codex/skills/req-scope/SKILL.md` -> `req-agent` routed domain work directly to `req-scope`.
- GREEN route evidence:
  - `sed -n '1,220p' .codex/skills/req-domain-analysis/SKILL.md` -> new worker skill is readable.
  - `sed -n '30,55p' .codex/skills/req-agent/SKILL.md` -> route now includes `req-domain-analysis` between `req-intake` and `req-scope`.
  - `rg -n "req-domain-analysis|req-scope|req-intake" .codex/skills/req-agent/SKILL.md .codex/skills/req-domain-analysis/SKILL.md` -> parent and worker references present.
- `openspec validate add-req-domain-analysis-skill --strict` -> valid.
- `python3 scripts/check_behavior_assets.py` -> non-zero because unrelated active change `initialize-llm-wiki-seed-repo` has missing behavior-asset evaluation fields. No errors were reported for `add-req-domain-analysis-skill`.

## Proof Boundary

This change proves local skill publication, parent-route update, and
behavior-evaluation evidence. It does not prove broad multi-session runtime
rollout and does not repair unrelated behavior-asset validation failures.
