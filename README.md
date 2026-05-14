# Report Wiki Portfolio

Markdown knowledge base for recurring reports, meeting-derived materials, and
AI-assisted report workflows.

This repository turns scattered inputs from chat, Feishu, meeting notes, inbox
files, and report drafts into durable wiki pages that can be linked, reviewed,
reused, and checked by agents.

## What This Repo Owns

- `wiki/`: durable source records, domain pages, reports, timelines, ops traces,
  templates, and generated status surfaces.
- `openspec/`: change proposals, designs, specs, task progress, and evaluation
  evidence.
- `.codex/skills/`: repo-local Codex skills that route wiki, OpenSpec, report,
  material, and taxonomy workflows.
- `scripts/`: repo-local automation for inbox intake, wiki status, graph/runtime
  summaries, scorecards, and taxonomy checks.

External systems such as Feishu are treated as source or publishing surfaces.
The durable truth lives in git-backed Markdown.

## Wiki Layers

Use the wiki by layer, not by memory:

- `wiki/sources/`: upstream evidence from inbox files, Feishu docs, meeting
  notes, attachments, and raw source summaries.
- `wiki/domains/`: durable business or topic understanding.
- `wiki/timeline/`: period-based review and reporting views.
- `wiki/reports/`: audience-facing drafts, management views, H5/share outputs,
  and report artifacts.
- `wiki/ops/`: workflow traces, retros, behavior gates, handoff notes, runtime
  methods, and agent-readable wiki surfaces.
- `wiki/adr/`: stable cross-change decisions.
- `wiki/status/`: generated status and manifest outputs.

Default flow:

```text
inbox / chat / Feishu / meeting note
  -> wiki/sources
  -> wiki/domains or wiki/timeline
  -> wiki/reports
  -> wiki/ops when the material contains workflow, governance, or action signals
```

## Frontmatter Taxonomy

Wiki frontmatter is governed by:

```text
wiki/config/frontmatter-taxonomy.yaml
.codex/skills/wiki-frontmatter-taxonomy/SKILL.md
scripts/check_wiki_frontmatter.py
```

Do not use `domain: personal-ops` for new or touched pages.

Use these fields separately:

- `layer`: where the page lives in the wiki structure.
- `domain`: real business or topic domain only.
- `ops_area`: operational or governance workflow category.
- `canonical_object`: stable object identity for graph/runtime use.
- `artifact_type`: document shape.

Examples:

```yaml
layer: ops
domain: none
ops_area: agent-governance
```

```yaml
layer: ops
domain: nirvana
ops_area: source-intake
```

```yaml
layer: ops
domain: unclassified
classification_needed: true
ops_area: source-intake
```

Before creating or modifying wiki frontmatter, load the repo-local taxonomy
skill and run the checker:

```bash
python3 scripts/check_wiki_frontmatter.py
```

The checker writes:

```text
/tmp/wiki-frontmatter-taxonomy-report.json
/tmp/wiki-frontmatter-taxonomy-report.md
```

The first rollout intentionally leaves legacy drift visible. A non-zero checker
exit can be expected until old `domain: personal-ops` pages are migrated in a
separate change.

## Common Commands

Build wiki status:

```bash
python3 scripts/build_wiki_status.py
```

Run the wiki scorecard:

```bash
python3 scripts/score_wiki_semantics.py > /tmp/wiki-semantic-scoring.json
python3 scripts/derive_wiki_utilization.py /tmp/wiki-semantic-scoring.json > /tmp/wiki-utilization.json
python3 scripts/summarize_wiki_scorecard.py --scores /tmp/wiki-semantic-scoring.json --utilization /tmp/wiki-utilization.json > /tmp/wiki-scorecard-summary.json
```

Check frontmatter taxonomy:

```bash
python3 scripts/check_wiki_frontmatter.py
```

Run targeted taxonomy tests when pytest is available:

```bash
python3 -m pytest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_frontmatter_taxonomy_skill.py tests/test_inbox_intake.py -q
```

## Codex Skills

Use repo-local skills under `.codex/skills/`. Do not install this repo's `wiki-*`
or `openspec-*` skills into root/user scope; duplicate registrations can surface
obsolete namespaces.

The current wiki runtime is the repo-local skill surface. Do not document or
invoke obsolete slash-style wiki commands as the active runtime entrypoint.

Do not reintroduce repo plugin marketplace metadata or plugin skill copies for
this runtime surface; those registrations can surface obsolete namespaces.
Specifically, keep `.agents/plugins/marketplace.json`,
`plugins/report-wiki-portfolio/.codex-plugin/plugin.json`, and
`plugins/report-wiki-portfolio/skills` absent.

The `$wiki-status` skill source is `.codex/skills/wiki-status/SKILL.md`.

High-frequency entry points:

- `$wiki-status`: refresh and summarize generated wiki status.
- `$wiki-manifest`: inspect generated source and routing manifest.
- `$wiki-inbox`: review pending inbox items.
- `$wiki-query`: bounded task-shaped context retrieval from route, context, and
  explicit search.
- `$wiki-explore`: explore a wiki-backed topic with evidence-surface checks.
- `$wiki-graph`: inspect structural graph and relation analysis.
- `$wiki-scorecard`: inspect semantic scoring and utilization diagnostics.
- `$wiki-route`: inspect runtime auto-routing suggestions.
- `$wiki-context`: inspect runtime context and context injection.
- `$wiki-apply`: inspect bounded self-directed execution suggestions.
- `$wiki-queue`: preview ready, decision-needed, and blocked wiki work.
- `$wiki-frontmatter-taxonomy`: validate wiki frontmatter taxonomy work.

Wiki runtime skills inspect and summarize. They do not create, modify, archive,
or queue OpenSpec changes unless a specific OpenSpec workflow skill is invoked
and the active change boundary allows it.

## Change Discipline

- Use OpenSpec for workflow, taxonomy, governance, skill, or structural changes.
- Stop implementation when an active OpenSpec change reaches all tasks complete.
  The default next step is archive review, not automatic archive.
- Commit only task-related files. Preserve unrelated local changes.
- Semantic edits to `.codex/skills/*` require evaluation evidence with pressure
  scenarios, RED baseline, GREEN result, and residual risks.

## Current State

The wiki has working source, ops, report, runtime, scorecard, and taxonomy-gate
surfaces. Business domain coverage is still thin and should be strengthened in
future scoped changes.
