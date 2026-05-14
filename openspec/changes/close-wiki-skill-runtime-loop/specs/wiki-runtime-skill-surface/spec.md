## Purpose

Define the current repo-local wiki runtime as a self-contained skill surface.

## ADDED Requirements

### Requirement: Wiki runtime SHALL be owned by repo-local skills

The current wiki runtime SHALL be discoverable and executable from
`.codex/skills/wiki-*` without opening slash command contract files.

#### Scenario: Agent reads a wiki skill

- **WHEN** an agent opens `.codex/skills/wiki-status/SKILL.md` or another
  repo-local wiki skill
- **THEN** the skill SHALL name the scripts, artifacts, summary fields, and
  boundaries needed to execute that runtime surface
- **AND** it SHALL NOT require `plugins/report-wiki-portfolio/commands`.

### Requirement: Active slash command contracts SHALL be removed

The repository SHALL remove active slash command contract files from
`commands/` and `plugins/report-wiki-portfolio/commands/`.

#### Scenario: Current runtime files are inspected

- **WHEN** active runtime docs, skills, and tests are inspected
- **THEN** they SHALL NOT present `/wiki:*` as a current executable entrypoint
- **AND** archived OpenSpec records MAY retain historical references.

### Requirement: Wiki apply SHALL route frontmatter repair through precheck hints

The wiki apply skill SHALL describe page frontmatter repair as a bounded route
through the compact frontmatter precheck.

#### Scenario: Page frontmatter repair is needed

- **WHEN** a page path is explicit
- **THEN** the repair route SHALL use
  `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
- **AND** agents SHALL use `target.repair_hints` before opening full taxonomy
  configuration.
