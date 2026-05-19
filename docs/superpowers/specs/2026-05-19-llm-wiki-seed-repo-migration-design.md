# LLM-WIKI Seed Repo Migration Design

## Status

Draft approved in chat for design-spec capture. README prose is intentionally
deferred until after migration and minimal verification are planned.

## Goal

Create a seed repository for `hhhope/LLM-WIKI` from the current
`report-wiki-portfolio` system.

The target is not a standalone starter-kit product and not a full archive dump.
It is a runnable seed repository that preserves the current LLM-Wiki workflow
surface:

```text
source capture -> structured wiki -> routing and retrieval -> output gates
-> status / graph / scorecard -> medical-loop maintenance
```

## Source Context

Current repository:

- `PROJECT.md` defines `report-wiki-portfolio` as an OpenSpec-governed
  markdown knowledge base.
- `README.md` already describes layered wiki runtime surfaces and states that
  README is orientation, not runtime authority.
- `.codex/skills/` contains the real repo-local skill surface, including
  learning capture, output gates, wiki runtime skills, and medical-loop skills.
- `wiki/config/` contains frontmatter and behavior-asset configuration.
- `scripts/` contains the current check, status, graph, runtime-context, and
  medical-loop machinery.
- `wiki/ops/karpathy-llm-wiki-reading-notes.md`,
  `wiki/ops/llm-wiki-core-product-contract.md`, and
  `wiki/ops/llm-wiki-self-evolution-medical-loop.md` provide local conceptual
  grounding for the seed.
- `wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md`
  and `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`
  provide a public-source example shape that can be sanitized.

External reference:

- Public LLM Wiki examples use the raw sources / wiki / schema model and
  operations such as ingest, query, and lint.
- The seed repo should preserve that model, but it should not replace the
  current repo's more specific skill surface with generic `ingest`, `query`,
  `lint`, and `medical-agent` placeholders.

## Non-Goals

- Do not write final README prose in this phase.
- Do not migrate private inbox, logs, report zips, full historical medical
  records, or internal business artifacts.
- Do not build a productized CLI such as `llm-wiki init/ingest/query/lint`.
- Do not claim automatic repair or full live ingest support.
- Do not copy the current repository history into the seed repo.
- Do not simplify the real skill surface into invented generic skill names.

## Migration Strategy

Use the current repo as the system master and evidence source.
Use `hhhope/LLM-WIKI` as the external seed repository.

Migration rule:

```text
copy the system, not the history
preserve the workflow, sanitize the evidence
ship a seed repo, not an archive dump
```

## Required Seed Files

### Root

Copy or adapt:

```text
AGENTS.md
PROJECT.md
README.md
```

README is included as a file target but final copywriting is deferred. During
the migration phase it can stay minimal and point readers to `AGENTS.md`,
`.codex/skills/`, `wiki/config/`, and `scripts/`.

### Skills

Preserve the repo-local Codex skill surface under `.codex/skills/`.

Required groups:

```text
.codex/skills/
  clarify-before-acting/
  verify-before-claiming/
  surgical-changes/
  simplicity-first/

  learning-capture/
  readme-learning-capture/
  material-collaboration-defaults/
  meeting-note-output/
  public-report-quality-gate/
  interview-deep-reading-board/
  project-management-weekly-skill/
  weixin-reader/

  openspec-router/
  openspec-propose/
  openspec-apply-change/
  openspec-archive-change/
  openspec-explore/

  wiki-status/
  wiki-manifest/
  wiki-inbox/
  wiki-query/
  wiki-route/
  wiki-context/
  wiki-scorecard/
  wiki-graph/
  wiki-apply/
  wiki-react/
  wiki-frontmatter-taxonomy/
  wiki-queue/
  wiki-explore/

  wiki-medical-agent/
  wiki-doctor/
  wiki-review-decisions/
  wiki-confirm/
  wiki-treatment/
  wiki-surgery/
  wiki-recovery/
```

Do not replace these with generic `skills/ingest`, `skills/query`,
`skills/lint`, or `skills/medical-agent` directories.

### Wiki Config

Copy:

```text
wiki/config/frontmatter-taxonomy.yaml
wiki/config/behavior-asset-evaluation.yaml
```

These files are required because they make wiki pages checkable. Without them,
agents can write markdown but cannot maintain structured wiki state.

### Scripts

Copy the minimal runnable set needed for status, taxonomy, graph, runtime
context, and medical-loop previews:

```text
scripts/check_wiki_frontmatter.py
scripts/build_wiki_status.py
scripts/extract_wiki_graph.py
scripts/analyze_wiki_relations.py
scripts/score_wiki_semantics.py
scripts/derive_wiki_utilization.py
scripts/summarize_wiki_scorecard.py
scripts/build_wiki_runtime_context.py
scripts/derive_runtime_auto_routing.py
scripts/resolve_runtime_context_sources.py
scripts/build_runtime_context_injection.py
scripts/derive_self_directed_execution.py
scripts/build_wiki_medical_agent.py
scripts/build_wiki_medical_case.py
scripts/build_wiki_review_decisions.py
scripts/build_wiki_treatment.py
scripts/build_wiki_surgery.py
scripts/build_wiki_recovery.py
scripts/wiki_status_render.py
scripts/wiki_medical_agent.py
scripts/wiki_medical_case.py
scripts/wiki_review_decisions.py
scripts/wiki_treatment.py
scripts/wiki_surgery.py
scripts/wiki_recovery.py
```

If any script imports local helper modules, include those helpers in the same
migration slice rather than rewriting script internals during the design phase.

## Wiki Seed Shape

Preserve the current directory model:

```text
wiki/
  index.md
  config/
  sources/
  domains/
  timeline/
  reports/
  examples/
  ops/
    wiki-doctor-runs/
    wiki-medical-cases/
    wiki-review-decisions/
    wiki-treatment-runs/
    wiki-surgery-runs/
    wiki-recovery-runs/
  adr/
  status/
  templates/
  evals/
  moc/
```

Do not switch to a generic `concepts/` and `entities/` layout in the seed.
Those names may be useful in other LLM Wiki projects, but they are not the
current system's directory contract.

## Sample Content Policy

Use half-real examples:

- Preserve public-source names and method names when they are already public,
  such as LLM-Wiki, Li Xiang / Luo Yonghao interview references, and the
  medical-loop vocabulary.
- Sanitize internal project details, private meeting content, customer names,
  business metrics, report packages, and local governance history.
- Keep examples small enough to explain the workflow without turning the seed
  repo into the original repository's archive.

Minimum sample set:

```text
wiki/sources/llm-wiki-method-reading.md
wiki/sources/lixiang-interview-reading-sanitized.md
wiki/examples/interview-deep-reading-board.md
wiki/ops/llm-wiki-core-product-contract.md
wiki/ops/llm-wiki-self-evolution-medical-loop.md
wiki/adr/0001-seed-repo-boundaries.md
wiki/status/wiki-status.md
```

Medical-loop history directories should exist, but each should contain at most
one synthetic or sanitized record in the initial seed.

## Exclusions

Exclude:

```text
inbox/
logs/
wiki/.obsidian/
wiki/reports/*.zip
wiki/reports/reports.zip
large report HTML/image asset bundles
full wiki-doctor run history
full wiki-review-decisions history
full wiki-treatment/surgery/recovery history
full OpenSpec archive history
private Feishu or meeting-source materials
local editor/tool state such as .idea/, .obsidian/, .venv-*, .claude/
```

OpenSpec material can be migrated later as a minimal lifecycle example, but the
seed repo should not start by copying the entire current OpenSpec history.

## Minimal Verification

The first seed is acceptable when these checks run in the target repository
against the migrated files and seed content:

```bash
python3 scripts/check_wiki_frontmatter.py
python3 scripts/build_wiki_status.py
python3 scripts/extract_wiki_graph.py
python3 scripts/analyze_wiki_relations.py
python3 scripts/score_wiki_semantics.py
python3 scripts/derive_wiki_utilization.py
python3 scripts/build_wiki_medical_agent.py
python3 scripts/build_wiki_medical_case.py
python3 scripts/build_wiki_review_decisions.py
```

Verification proves only:

- directory structure is present;
- seed pages satisfy the taxonomy well enough for the checker;
- status and graph surfaces can be regenerated;
- scorecard/utilization scripts can inspect seed content;
- medical-loop preview scripts can run without requiring full historical data.

Verification does not prove:

- automatic repair;
- full ingest automation;
- production-grade CLI behavior;
- public README quality;
- complete compatibility for all downstream agents.

## Implementation Plan Handoff

After the user approves this written spec, transition to a separate
implementation plan. The implementation plan should:

1. inventory script imports and helper dependencies;
2. define an allowlist copy manifest;
3. define sanitization rules for sample pages;
4. create or populate the external seed repository;
5. run the minimal verification commands in the target repository;
6. defer README polishing until the copied system passes minimal verification.

