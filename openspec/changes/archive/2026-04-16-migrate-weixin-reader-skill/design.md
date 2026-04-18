## Context

The external skill at `~/.claude/skills/weixin-reader/` contains:

- `SKILL.md`
- `scripts/fetch_weixin.py`

Initial review shows it is usable:

- the fetch script is present
- local dependencies already exist: `playwright`, `beautifulsoup4`, `lxml`

But it is not ready for direct mirroring because:

- the description is not in the preferred Codex trigger style
- the command example hardcodes the external `~/.claude/skills/` path

This is therefore an `adapt` migration, not a plain mirror.

## Goals / Non-Goals

**Goals:**

- Localize the skill into `.codex/skills/weixin-reader/`.
- Keep the existing script behavior.
- Rewrite the skill description so it is trigger-focused and Codex-friendly.
- Replace external path references with local repo-relative usage.

**Non-Goals:**

- Rewrite the fetcher implementation.
- Add new scraping logic or browser automation features.
- Wire the skill into repo `AGENTS.md` automatically.

## Decisions

### Decision: Adapt rather than mirror

The external skill is good enough to reuse, but the trigger description and command references need local adaptation. That makes `adapt` the right migration decision.

### Decision: Keep the script local to the skill

The helper script will be copied under the local skill directory so the skill remains self-contained and no longer depends on the external `~/.claude` path.

### Decision: Preserve dependency notes

The migrated skill should still mention runtime dependencies and that Weixin pages may require verification, so users understand failure modes.

## Risks / Trade-offs

- [Risk] Weixin articles may still hit environment verification or anti-bot limits. → Mitigation: keep the skill explicit about that limitation.
- [Risk] The script may work locally today but fail in other environments without Chromium installed. → Mitigation: preserve dependency instructions.
- [Risk] Mirroring the old description style would reduce discoverability in Codex. → Mitigation: adapt the description to a proper trigger sentence.

## Migration Plan

1. Create and validate the migration change.
2. Copy and adapt the skill markdown locally.
3. Copy the helper script locally.
4. Verify the local skill exists and no longer references `~/.claude/skills/`.
