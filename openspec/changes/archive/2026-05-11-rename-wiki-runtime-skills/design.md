# Design: Wiki Runtime Skills

## Runtime Finding

`codex app-server` `skills/list` shows repo-local skills in this trusted
project with the project namespace, for example
`report-wiki-portfolio:openspec-explore`. A repo-local `.codex/skills/wiki-*`
file would therefore still be exposed with the same project prefix.

User-scope skills under `$CODEX_HOME/skills` are the stable way to expose plain
names such as `wiki-status`.

## Shape

The repository will keep installable source copies under:

```text
plugins/report-wiki-portfolio/skills/wiki-*/SKILL.md
```

Each skill:

- uses frontmatter `name: wiki-*`
- points to the matching repo command contract under
  `plugins/report-wiki-portfolio/commands/wiki-*.md`
- preserves the existing runtime boundaries:
  no OpenSpec create/modify/archive, no task completion, no hidden semantic
  search, and no execution of queued work

The working user install is a mechanical copy to:

```text
/home/yan/.codex/skills/wiki-*/SKILL.md
```

## Non-Goals

- Do not add more slash command workarounds.
- Do not add repo-local `.codex/skills/wiki-*` entries that would create
  `report-wiki-portfolio:wiki-*` duplicates.
- Do not change runtime scripts or generated wiki artifacts.
- Do not archive the previous plugin changes in this change.

## Verification

- Unit tests check the source skill names and README surface.
- Real `codex app-server` `skills/list` checks the installed user-scope names.
- `openspec validate rename-wiki-runtime-skills --strict` checks the change
  contract.
