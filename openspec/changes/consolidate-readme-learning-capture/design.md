# Design: consolidate README learning capture

## Approach

Treat `learning-capture` as the only runtime entry for external-source learning.
Repo/README-specific behavior remains as module references under:

```text
.codex/skills/learning-capture/references/repo-readme.md
.codex/skills/learning-capture/references/repo-readme-scorecard.md
.codex/skills/learning-capture/references/repo-readme-pressure-scenarios.md
```

The old `readme-learning-capture` directory is removed from the active skill
surface. This mirrors the prior article-learning consolidation pattern: retire
the duplicated runtime trigger, preserve the useful module gates.

## Verification Strategy

- Add a regression test that fails while the active README skill directory or
  active references still exist.
- Verify repo/README scorecard and pressure-scenario content moved under the
  learning-capture module.
- Run behavior-asset evaluation because this is a semantic skill-surface
  change.
- Run OpenSpec validation.

## Boundaries

- Do not rewrite historical `wiki/ops` records just because they mention the old
  skill name.
- Do not change general learning-capture routing beyond the repo/README module.
- Do not edit external target repositories.
