from __future__ import annotations

COPY_FILES = [
    "wiki/config/frontmatter-taxonomy.yaml",
    "wiki/config/behavior-asset-evaluation.yaml",
    "scripts/check_wiki_frontmatter.py",
    "scripts/build_wiki_status.py",
    "scripts/extract_wiki_graph.py",
    "scripts/analyze_wiki_relations.py",
    "scripts/score_wiki_semantics.py",
    "scripts/derive_wiki_utilization.py",
    "scripts/summarize_wiki_scorecard.py",
    "scripts/build_wiki_runtime_context.py",
    "scripts/derive_runtime_auto_routing.py",
    "scripts/resolve_runtime_context_sources.py",
    "scripts/build_runtime_context_injection.py",
    "scripts/derive_self_directed_execution.py",
    "scripts/build_wiki_medical_agent.py",
    "scripts/build_wiki_medical_case.py",
    "scripts/build_wiki_review_decisions.py",
    "scripts/build_wiki_treatment.py",
    "scripts/build_wiki_surgery.py",
    "scripts/build_wiki_recovery.py",
    "scripts/wiki_status_render.py",
    "scripts/wiki_medical_agent.py",
    "scripts/wiki_medical_case.py",
    "scripts/wiki_review_decisions.py",
    "scripts/wiki_treatment.py",
    "scripts/wiki_surgery.py",
    "scripts/wiki_recovery.py",
    "scripts/wiki_content_adjudication.py",
    "scripts/wiki_content_enrichment.py",
    "scripts/wiki_moc_projection.py",
    "scripts/wiki_moc_lifecycle.py",
    "scripts/wiki_product_status.py",
    "scripts/build_wiki_moc_projection.py",
]

COPY_DIRS = [
    ".codex/skills/clarify-before-acting",
    ".codex/skills/verify-before-claiming",
    ".codex/skills/surgical-changes",
    ".codex/skills/simplicity-first",
    ".codex/skills/learning-capture",
    ".codex/skills/readme-learning-capture",
    ".codex/skills/material-collaboration-defaults",
    ".codex/skills/meeting-note-output",
    ".codex/skills/public-report-quality-gate",
    ".codex/skills/interview-deep-reading-board",
    ".codex/skills/project-management-weekly-skill",
    ".codex/skills/weixin-reader",
    ".codex/skills/openspec-router",
    ".codex/skills/openspec-propose",
    ".codex/skills/openspec-apply-change",
    ".codex/skills/openspec-archive-change",
    ".codex/skills/openspec-explore",
    ".codex/skills/wiki-status",
    ".codex/skills/wiki-manifest",
    ".codex/skills/wiki-inbox",
    ".codex/skills/wiki-query",
    ".codex/skills/wiki-route",
    ".codex/skills/wiki-context",
    ".codex/skills/wiki-scorecard",
    ".codex/skills/wiki-graph",
    ".codex/skills/wiki-apply",
    ".codex/skills/wiki-react",
    ".codex/skills/wiki-frontmatter-taxonomy",
    ".codex/skills/wiki-queue",
    ".codex/skills/wiki-explore",
    ".codex/skills/wiki-medical-agent",
    ".codex/skills/wiki-doctor",
    ".codex/skills/wiki-review-decisions",
    ".codex/skills/wiki-confirm",
    ".codex/skills/wiki-treatment",
    ".codex/skills/wiki-surgery",
    ".codex/skills/wiki-recovery",
]

CREATE_DIRS = [
    "wiki/sources",
    "wiki/domains",
    "wiki/timeline",
    "wiki/reports",
    "wiki/examples",
    "wiki/ops/wiki-doctor-runs",
    "wiki/ops/wiki-medical-cases",
    "wiki/ops/wiki-review-decisions",
    "wiki/ops/wiki-treatment-runs",
    "wiki/ops/wiki-surgery-runs",
    "wiki/ops/wiki-recovery-runs",
    "wiki/adr",
    "wiki/status",
    "wiki/templates",
    "wiki/evals",
    "wiki/moc",
]

EXCLUDE_FRAGMENTS = [
    "inbox/",
    "logs/",
    "wiki/.obsidian",
    "wiki/reports/reports.zip",
    "openspec/changes/archive",
    ".idea/",
    ".obsidian/",
    ".venv-",
    ".claude/",
]

EXCLUDE_GLOBS = [
    "wiki/reports/*.zip",
]

GENERATED_TEXT_FILES = {
    ".gitignore": """__pycache__/
*.py[cod]
.pytest_cache/
.venv/
.DS_Store
""",
    "PROJECT.md": """---
project: llm-wiki
status: active
owner: hhhope
source_of_truth: wiki-seed
---

# LLM-WIKI

This seed repository starts from a runnable LLM-maintained wiki system. README
polishing is deferred until migration and minimal verification pass.
""",
    "README.md": """# LLM-WIKI

Runnable seed repository for an agent-maintained Markdown wiki.

This first migration intentionally keeps README minimal. The verified system
surface lives in `AGENTS.md`, `.codex/skills/`, `wiki/config/`, `wiki/`, and
`scripts/`.
""",
    "AGENTS.md": """# LLM-WIKI Agent Entry

Use this repository as an LLM-maintained wiki seed.

- Read `PROJECT.md` first.
- Use `.codex/skills/` for workflow routing.
- Use `wiki/config/frontmatter-taxonomy.yaml` before creating wiki pages.
- Preserve source evidence in `wiki/sources/`.
- Use the medical loop for wiki maintenance: doctor, review, treatment,
  surgery, recovery.
- Do not treat README as runtime authority.
""",
}

GENERATED_SAMPLE_FILES = {
    "wiki/index.md": """---
layer: status
domain: none
---

# LLM-WIKI Index

- [Sources](sources/index.md)
- [Domains](domains/index.md)
- [Timeline](timeline/index.md)
- [Reports](reports/index.md)
- [Examples](examples/index.md)
- [Ops](ops/index.md)
- [ADR](adr/index.md)
- [Status](status/wiki-status.md)
""",
    "wiki/sources/index.md": """---
layer: sources
domain: none
source_type: index
---

# Sources

Raw and source-derived records enter here before being compiled into wiki pages.
""",
    "wiki/domains/index.md": """---
layer: domains
domain: none
---

# Domains

Durable topic and business-domain understanding lives here.
""",
    "wiki/timeline/index.md": """---
layer: timeline
domain: none
---

# Timeline

Period-based views and evolution records live here.
""",
    "wiki/reports/index.md": """---
layer: reports
domain: none
---

# Reports

Reader-facing drafts and output records live here.
""",
    "wiki/examples/index.md": """---
layer: examples
domain: none
---

# Examples

Validated output shapes and sanitized examples live here.
""",
    "wiki/ops/index.md": """---
layer: ops
domain: none
ops_area: wiki-runtime
canonical_object: wiki-ops-index
artifact_type: index
---

# Ops

Workflow traces, runtime models, and medical-loop records live here.
""",
    "wiki/adr/index.md": """---
layer: adr
domain: none
canonical_object: adr-index
artifact_type: index
---

# ADR

Stable decisions for this seed repository.
""",
    "wiki/status/wiki-status.md": """---
layer: status
domain: none
---

# Wiki Status

Initial seed status. Regenerate with `python3 scripts/build_wiki_status.py`.
""",
    "wiki/sources/llm-wiki-method-reading.md": """---
layer: sources
domain: wiki
source_type: public-method-reference
status: seed
---

# LLM-Wiki Method Reading

Sanitized seed note: raw sources are preserved as evidence, while agents compile
durable Markdown wiki pages for later retrieval and maintenance.
""",
    "wiki/sources/lixiang-interview-reading-sanitized.md": """---
layer: sources
domain: product-engineering-collaboration
source_type: public-interview-reference
status: sanitized-seed
---

# Li Xiang Interview Reading Sanitized

Sanitized seed note preserving the public-source learning shape without private
project details.
""",
    "wiki/examples/interview-deep-reading-board.md": """---
layer: examples
domain: public-report-output
status: sanitized-seed
---

# Interview Deep Reading Board Example

Seed example for an interview reading board. It preserves output shape, not a
full transcript.
""",
    "wiki/ops/llm-wiki-core-product-contract.md": """---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: llm-wiki-core-product-contract
artifact_type: product-contract
status: seed
---

# LLM-WIKI Core Product Contract

Capture once. Compile once. Retrieve cheaply. Apply safely.
""",
    "wiki/ops/llm-wiki-self-evolution-medical-loop.md": """---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: llm-wiki-self-evolution-medical-loop
artifact_type: ops-model
status: seed
---

# LLM-WIKI Self-Evolution Medical Loop

doctor diagnoses; review confirms; treatment or surgery writes; recovery
proves; archive preserves.
""",
    "wiki/adr/0001-seed-repo-boundaries.md": """---
layer: adr
domain: none
canonical_object: seed-repo-boundaries
artifact_type: adr
status: accepted
---

# ADR-0001 Seed Repo Boundaries

This repository copies the system, not the history. Historical private material
and full medical-loop records stay out of the initial seed.
""",
}
