# LLM-WIKI Seed Repo Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a reproducible seed repository for `hhhope/LLM-WIKI` from the current repo's real wiki runtime, skills, config, scripts, and sanitized examples.

**Architecture:** Add a manifest-driven seed builder in this repository, use it to populate a target checkout, and verify the target with a dedicated seed verifier plus the migrated wiki runtime scripts. The builder copies allowlisted system files, creates required empty runtime directories, writes sanitized seed examples, and leaves README polishing for a later phase.

**Tech Stack:** Python 3.12 stdlib plus the current repo's existing Python scripts; pytest/unittest-style tests; git for source and target repository review.

---

## Design Inputs

- Spec: `docs/superpowers/specs/2026-05-19-llm-wiki-seed-repo-migration-design.md`
- Current root: `/mnt/d/cloud/account-meeting-lore`
- Default target root for local execution: `/mnt/d/cloud/LLM-WIKI`
- External repo: `https://github.com/hhhope/LLM-WIKI`

## File Structure

Create these implementation files in the current repository:

```text
scripts/llm_wiki_seed_manifest.py
scripts/build_llm_wiki_seed.py
scripts/verify_llm_wiki_seed.py
tests/test_llm_wiki_seed_manifest.py
tests/test_llm_wiki_seed_builder.py
```

Responsibilities:

- `scripts/llm_wiki_seed_manifest.py`: one allowlist for copied files, copied directories, created directories, generated root files, generated sanitized sample files, and excluded path fragments.
- `scripts/build_llm_wiki_seed.py`: deterministic seed generator; refuses dirty non-empty targets unless `--force` is passed; copies allowlisted paths; writes generated files; never copies excluded paths.
- `scripts/verify_llm_wiki_seed.py`: structural verifier for a generated target; asserts required paths exist, excluded paths do not exist, and core seed files contain expected public/sanitized markers.
- `tests/test_llm_wiki_seed_manifest.py`: validates manifest coverage for required skills, config, scripts, and exclusions.
- `tests/test_llm_wiki_seed_builder.py`: validates dry-run and actual generation into `tmp_path` without touching the external repository.

Generated target shape:

```text
LLM-WIKI/
  README.md
  AGENTS.md
  PROJECT.md
  .codex/skills/...
  wiki/config/...
  wiki/sources/...
  wiki/examples/...
  wiki/ops/...
  wiki/adr/...
  wiki/status/...
  wiki/templates/
  wiki/evals/
  wiki/moc/
  scripts/...
```

---

### Task 1: Add Manifest Test And Manifest Module

**Files:**

- Create: `tests/test_llm_wiki_seed_manifest.py`
- Create: `scripts/llm_wiki_seed_manifest.py`

- [ ] **Step 1: Write failing manifest coverage tests**

Create `tests/test_llm_wiki_seed_manifest.py`:

```python
from __future__ import annotations

from scripts import llm_wiki_seed_manifest as manifest


def test_seed_manifest_includes_real_wiki_skill_surface() -> None:
    required_skill_dirs = {
        ".codex/skills/learning-capture",
        ".codex/skills/readme-learning-capture",
        ".codex/skills/material-collaboration-defaults",
        ".codex/skills/public-report-quality-gate",
        ".codex/skills/wiki-status",
        ".codex/skills/wiki-manifest",
        ".codex/skills/wiki-query",
        ".codex/skills/wiki-react",
        ".codex/skills/wiki-apply",
        ".codex/skills/wiki-scorecard",
        ".codex/skills/wiki-frontmatter-taxonomy",
        ".codex/skills/wiki-medical-agent",
        ".codex/skills/wiki-doctor",
        ".codex/skills/wiki-review-decisions",
        ".codex/skills/wiki-confirm",
        ".codex/skills/wiki-treatment",
        ".codex/skills/wiki-surgery",
        ".codex/skills/wiki-recovery",
        ".codex/skills/openspec-router",
        ".codex/skills/openspec-apply-change",
    }

    copied_dirs = set(manifest.COPY_DIRS)

    assert required_skill_dirs <= copied_dirs


def test_seed_manifest_includes_config_and_runtime_scripts() -> None:
    required_files = {
        "wiki/config/frontmatter-taxonomy.yaml",
        "wiki/config/behavior-asset-evaluation.yaml",
        "scripts/check_wiki_frontmatter.py",
        "scripts/build_wiki_status.py",
        "scripts/extract_wiki_graph.py",
        "scripts/analyze_wiki_relations.py",
        "scripts/score_wiki_semantics.py",
        "scripts/derive_wiki_utilization.py",
        "scripts/build_wiki_runtime_context.py",
        "scripts/derive_runtime_auto_routing.py",
        "scripts/build_runtime_context_injection.py",
        "scripts/derive_self_directed_execution.py",
        "scripts/build_wiki_medical_agent.py",
        "scripts/build_wiki_medical_case.py",
        "scripts/build_wiki_review_decisions.py",
        "scripts/build_wiki_treatment.py",
        "scripts/build_wiki_surgery.py",
        "scripts/build_wiki_recovery.py",
        "scripts/wiki_medical_agent.py",
        "scripts/wiki_medical_case.py",
        "scripts/wiki_review_decisions.py",
        "scripts/wiki_treatment.py",
        "scripts/wiki_surgery.py",
        "scripts/wiki_recovery.py",
    }

    copied_files = set(manifest.COPY_FILES)

    assert required_files <= copied_files


def test_seed_manifest_rejects_archive_dump_paths() -> None:
    forbidden_fragments = {
        "inbox/",
        "logs/",
        "wiki/.obsidian",
        "wiki/reports/reports.zip",
        "wiki/reports/*.zip",
        "openspec/changes/archive",
    }

    assert forbidden_fragments <= set(manifest.EXCLUDE_FRAGMENTS)
    assert all("concepts" not in path for path in manifest.CREATE_DIRS)
    assert all("entities" not in path for path in manifest.CREATE_DIRS)
```

- [ ] **Step 2: Run manifest test to verify it fails**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_manifest.py -q
```

Expected:

```text
ModuleNotFoundError: No module named 'scripts.llm_wiki_seed_manifest'
```

- [ ] **Step 3: Add manifest module**

Create `scripts/llm_wiki_seed_manifest.py`:

```python
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
    "wiki/reports/*.zip",
    "wiki/reports/reports.zip",
    "openspec/changes/archive",
    ".idea/",
    ".obsidian/",
    ".venv-",
    ".claude/",
]

GENERATED_TEXT_FILES = {
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
---

# Ops

Workflow traces, runtime models, and medical-loop records live here.
""",
    "wiki/adr/index.md": """---
layer: adr
domain: none
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
status: seed
---

# LLM-WIKI Core Product Contract

Capture once. Compile once. Retrieve cheaply. Apply safely.
""",
    "wiki/ops/llm-wiki-self-evolution-medical-loop.md": """---
layer: ops
domain: wiki
ops_area: wiki-runtime
status: seed
---

# LLM-WIKI Self-Evolution Medical Loop

doctor diagnoses; review confirms; treatment or surgery writes; recovery
proves; archive preserves.
""",
    "wiki/adr/0001-seed-repo-boundaries.md": """---
layer: adr
domain: none
status: accepted
---

# ADR-0001 Seed Repo Boundaries

This repository copies the system, not the history. Historical private material
and full medical-loop records stay out of the initial seed.
""",
}
```

- [ ] **Step 4: Run manifest tests to verify they pass**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_manifest.py -q
```

Expected:

```text
3 passed
```

- [ ] **Step 5: Commit manifest slice**

Run:

```bash
git status --short
git add scripts/llm_wiki_seed_manifest.py tests/test_llm_wiki_seed_manifest.py
git commit -m "feat: define llm wiki seed manifest"
```

Expected commit includes only the two files above.

---

### Task 2: Add Seed Builder And Builder Tests

**Files:**

- Create: `tests/test_llm_wiki_seed_builder.py`
- Create: `scripts/build_llm_wiki_seed.py`
- Modify: `scripts/llm_wiki_seed_manifest.py`

- [ ] **Step 1: Write failing builder tests**

Create `tests/test_llm_wiki_seed_builder.py`:

```python
from __future__ import annotations

from pathlib import Path

from scripts.build_llm_wiki_seed import build_seed


def test_build_seed_creates_required_structure(tmp_path: Path) -> None:
    target = tmp_path / "LLM-WIKI"

    build_seed(target, force=False)

    assert (target / "PROJECT.md").exists()
    assert (target / "AGENTS.md").exists()
    assert (target / "README.md").exists()
    assert (target / ".codex/skills/wiki-status/SKILL.md").exists()
    assert (target / ".codex/skills/learning-capture/SKILL.md").exists()
    assert (target / "wiki/config/frontmatter-taxonomy.yaml").exists()
    assert (target / "wiki/ops/wiki-medical-cases/.gitkeep").exists()
    assert (target / "scripts/build_wiki_status.py").exists()


def test_build_seed_writes_sanitized_examples(tmp_path: Path) -> None:
    target = tmp_path / "LLM-WIKI"

    build_seed(target, force=False)

    source = (target / "wiki/sources/lixiang-interview-reading-sanitized.md").read_text(
        encoding="utf-8"
    )
    medical = (target / "wiki/ops/llm-wiki-self-evolution-medical-loop.md").read_text(
        encoding="utf-8"
    )

    assert "Sanitized seed note" in source
    assert "doctor diagnoses; review confirms" in medical
    assert "account-meeting-lore" not in source
    assert "report-wiki-portfolio" not in source


def test_build_seed_refuses_non_empty_target_without_force(tmp_path: Path) -> None:
    target = tmp_path / "LLM-WIKI"
    target.mkdir()
    (target / "existing.txt").write_text("keep", encoding="utf-8")

    try:
        build_seed(target, force=False)
    except SystemExit as exc:
        assert "Target directory is not empty" in str(exc)
    else:
        raise AssertionError("build_seed should refuse non-empty target")
```

- [ ] **Step 2: Run builder tests to verify they fail**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_builder.py -q
```

Expected:

```text
ModuleNotFoundError: No module named 'scripts.build_llm_wiki_seed'
```

- [ ] **Step 3: Add seed builder**

Create `scripts/build_llm_wiki_seed.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from scripts import llm_wiki_seed_manifest as manifest


REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the LLM-WIKI seed repository.")
    parser.add_argument("--target-dir", required=True, help="Target directory to populate.")
    parser.add_argument("--force", action="store_true", help="Replace existing target content.")
    return parser.parse_args()


def ensure_target(target: Path, force: bool) -> None:
    if target.exists() and any(target.iterdir()):
        if not force:
            raise SystemExit(f"Target directory is not empty: {target}")
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)


def copy_file(rel_path: str, target: Path) -> None:
    source = REPO_ROOT / rel_path
    if not source.exists():
        raise SystemExit(f"Missing source file: {rel_path}")
    destination = target / rel_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_dir(rel_path: str, target: Path) -> None:
    source = REPO_ROOT / rel_path
    if not source.exists():
        raise SystemExit(f"Missing source directory: {rel_path}")
    destination = target / rel_path
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def create_dirs(target: Path) -> None:
    for rel_path in manifest.CREATE_DIRS:
        directory = target / rel_path
        directory.mkdir(parents=True, exist_ok=True)
        write_text(directory / ".gitkeep", "")


def write_generated_files(target: Path) -> None:
    for rel_path, text in manifest.GENERATED_TEXT_FILES.items():
        write_text(target / rel_path, text)
    for rel_path, text in manifest.GENERATED_SAMPLE_FILES.items():
        write_text(target / rel_path, text)


def assert_no_excluded_paths(target: Path) -> None:
    forbidden_exact = [
        "inbox",
        "logs",
        "wiki/.obsidian",
        "wiki/reports/reports.zip",
        "openspec/changes/archive",
    ]
    for rel_path in forbidden_exact:
        if (target / rel_path).exists():
            raise SystemExit(f"Excluded path was created: {rel_path}")


def build_seed(target: Path, force: bool) -> None:
    target = target.resolve()
    ensure_target(target, force)
    for rel_path in manifest.COPY_DIRS:
        copy_dir(rel_path, target)
    for rel_path in manifest.COPY_FILES:
        copy_file(rel_path, target)
    create_dirs(target)
    write_generated_files(target)
    assert_no_excluded_paths(target)


def main() -> int:
    args = parse_args()
    build_seed(Path(args.target_dir), force=args.force)
    print(f"Built LLM-WIKI seed at {Path(args.target_dir).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run builder tests to verify they pass**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_manifest.py tests/test_llm_wiki_seed_builder.py -q
```

Expected:

```text
6 passed
```

- [ ] **Step 5: Run a dry local generation into `/tmp`**

Run:

```bash
python3 scripts/build_llm_wiki_seed.py --target-dir /tmp/llm-wiki-seed-dryrun --force
```

Expected:

```text
Built LLM-WIKI seed at /tmp/llm-wiki-seed-dryrun
```

- [ ] **Step 6: Inspect generated dry-run top-level paths**

Run:

```bash
find /tmp/llm-wiki-seed-dryrun -maxdepth 2 -type d | sort | sed -n '1,80p'
```

Expected includes:

```text
/tmp/llm-wiki-seed-dryrun/.codex
/tmp/llm-wiki-seed-dryrun/.codex/skills
/tmp/llm-wiki-seed-dryrun/scripts
/tmp/llm-wiki-seed-dryrun/wiki
/tmp/llm-wiki-seed-dryrun/wiki/config
/tmp/llm-wiki-seed-dryrun/wiki/ops
/tmp/llm-wiki-seed-dryrun/wiki/sources
/tmp/llm-wiki-seed-dryrun/wiki/status
```

- [ ] **Step 7: Commit builder slice**

Run:

```bash
git status --short
git add scripts/build_llm_wiki_seed.py scripts/llm_wiki_seed_manifest.py tests/test_llm_wiki_seed_builder.py
git commit -m "feat: build llm wiki seed repository"
```

Expected commit includes only the builder, updated manifest if needed, and builder test.

---

### Task 3: Add Seed Verifier

**Files:**

- Create: `scripts/verify_llm_wiki_seed.py`
- Modify: `tests/test_llm_wiki_seed_builder.py`

- [ ] **Step 1: Add verifier test**

Append to `tests/test_llm_wiki_seed_builder.py`:

```python
from scripts.verify_llm_wiki_seed import verify_seed


def test_verify_seed_accepts_generated_seed(tmp_path: Path) -> None:
    target = tmp_path / "LLM-WIKI"

    build_seed(target, force=False)
    result = verify_seed(target)

    assert result == 0
```

- [ ] **Step 2: Run verifier test to verify it fails**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_builder.py::test_verify_seed_accepts_generated_seed -q
```

Expected:

```text
ModuleNotFoundError: No module named 'scripts.verify_llm_wiki_seed'
```

- [ ] **Step 3: Add verifier script**

Create `scripts/verify_llm_wiki_seed.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_PATHS = [
    "PROJECT.md",
    "AGENTS.md",
    "README.md",
    ".codex/skills/learning-capture/SKILL.md",
    ".codex/skills/public-report-quality-gate/SKILL.md",
    ".codex/skills/wiki-status/SKILL.md",
    ".codex/skills/wiki-query/SKILL.md",
    ".codex/skills/wiki-react/SKILL.md",
    ".codex/skills/wiki-medical-agent/SKILL.md",
    ".codex/skills/wiki-doctor/SKILL.md",
    ".codex/skills/wiki-treatment/SKILL.md",
    ".codex/skills/wiki-surgery/SKILL.md",
    ".codex/skills/wiki-recovery/SKILL.md",
    "wiki/index.md",
    "wiki/config/frontmatter-taxonomy.yaml",
    "wiki/config/behavior-asset-evaluation.yaml",
    "wiki/sources/llm-wiki-method-reading.md",
    "wiki/sources/lixiang-interview-reading-sanitized.md",
    "wiki/examples/interview-deep-reading-board.md",
    "wiki/ops/llm-wiki-core-product-contract.md",
    "wiki/ops/llm-wiki-self-evolution-medical-loop.md",
    "wiki/adr/0001-seed-repo-boundaries.md",
    "wiki/status/wiki-status.md",
    "scripts/check_wiki_frontmatter.py",
    "scripts/build_wiki_status.py",
    "scripts/extract_wiki_graph.py",
    "scripts/build_wiki_medical_agent.py",
    "scripts/build_wiki_medical_case.py",
    "scripts/build_wiki_review_decisions.py",
]

FORBIDDEN_PATHS = [
    "inbox",
    "logs",
    "wiki/.obsidian",
    "wiki/reports/reports.zip",
    "openspec/changes/archive",
]

REQUIRED_TEXT = {
    "README.md": ["Runnable seed repository", "README minimal"],
    "AGENTS.md": [".codex/skills/", "medical loop", "README"],
    "wiki/sources/lixiang-interview-reading-sanitized.md": ["Sanitized seed note"],
    "wiki/ops/llm-wiki-self-evolution-medical-loop.md": [
        "doctor diagnoses; review confirms"
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify an LLM-WIKI seed repo.")
    parser.add_argument("--target-dir", default=".", help="Seed repository path.")
    return parser.parse_args()


def verify_seed(target: Path) -> int:
    target = target.resolve()
    missing = [path for path in REQUIRED_PATHS if not (target / path).exists()]
    forbidden = [path for path in FORBIDDEN_PATHS if (target / path).exists()]
    text_failures: list[str] = []
    for rel_path, markers in REQUIRED_TEXT.items():
        content = (target / rel_path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                text_failures.append(f"{rel_path}: missing {marker}")

    if missing or forbidden or text_failures:
        if missing:
            print("Missing required seed paths:")
            for path in missing:
                print(f"- {path}")
        if forbidden:
            print("Forbidden paths present:")
            for path in forbidden:
                print(f"- {path}")
        if text_failures:
            print("Seed marker failures:")
            for failure in text_failures:
                print(f"- {failure}")
        return 1

    print("LLM-WIKI seed verification passed.")
    return 0


def main() -> int:
    args = parse_args()
    return verify_seed(Path(args.target_dir))


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run verifier tests**

Run:

```bash
python3 -m pytest tests/test_llm_wiki_seed_manifest.py tests/test_llm_wiki_seed_builder.py -q
```

Expected:

```text
7 passed
```

- [ ] **Step 5: Verify dry-run seed**

Run:

```bash
python3 scripts/verify_llm_wiki_seed.py --target-dir /tmp/llm-wiki-seed-dryrun
```

Expected:

```text
LLM-WIKI seed verification passed.
```

- [ ] **Step 6: Commit verifier slice**

Run:

```bash
git status --short
git add scripts/verify_llm_wiki_seed.py tests/test_llm_wiki_seed_builder.py
git commit -m "feat: verify llm wiki seed repository"
```

Expected commit includes only the verifier and updated builder test.

---

### Task 4: Generate Target Repository Locally

**Files:**

- Write target repository files under `/mnt/d/cloud/LLM-WIKI`
- Do not modify current repo files in this task

- [ ] **Step 1: Check target repository path**

Run:

```bash
ls -la /mnt/d/cloud/LLM-WIKI
```

Expected if already cloned/new:

```text
.git
```

If the directory does not exist, clone it:

```bash
git clone https://github.com/hhhope/LLM-WIKI /mnt/d/cloud/LLM-WIKI
```

Expected:

```text
Cloning into '/mnt/d/cloud/LLM-WIKI'...
```

- [ ] **Step 2: Inspect target branch and status**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI status --short
git -C /mnt/d/cloud/LLM-WIKI branch --show-current
git -C /mnt/d/cloud/LLM-WIKI log -1 --oneline
```

Expected:

```text
main
```

For a newly created empty repo, `git log -1 --oneline` may fail because no commit exists. If it fails with no commits, record that in the execution note and continue.

- [ ] **Step 3: Generate seed into target**

Run:

```bash
python3 scripts/build_llm_wiki_seed.py --target-dir /mnt/d/cloud/LLM-WIKI --force
```

Expected:

```text
Built LLM-WIKI seed at /mnt/d/cloud/LLM-WIKI
```

- [ ] **Step 4: Verify target structure**

Run:

```bash
python3 scripts/verify_llm_wiki_seed.py --target-dir /mnt/d/cloud/LLM-WIKI
```

Expected:

```text
LLM-WIKI seed verification passed.
```

- [ ] **Step 5: Inspect target status**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI status --short
```

Expected includes generated seed paths such as:

```text
?? .codex/
?? AGENTS.md
?? PROJECT.md
?? README.md
?? scripts/
?? wiki/
```

Do not commit target repo yet.

---

### Task 5: Run Minimal Runtime Verification In Target

**Files:**

- Target repository: `/mnt/d/cloud/LLM-WIKI`
- Generated status artifacts may be modified under `/mnt/d/cloud/LLM-WIKI/wiki/status/`
- Generated medical-loop preview records may be modified under `/mnt/d/cloud/LLM-WIKI/wiki/ops/`

- [ ] **Step 1: Run taxonomy checker in target**

Run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

from `/mnt/d/cloud/LLM-WIKI`.

Expected:

```text
Command exits 0. Output may be empty.
```

The checker may exit non-zero if the copied taxonomy still contains repo-specific legacy rules that conflict with the minimal seed. If it fails, capture the first 40 lines and fix only seed pages or seed taxonomy, not private source history.

- [ ] **Step 2: Build wiki status in target**

Run:

```bash
python3 scripts/build_wiki_status.py
```

from `/mnt/d/cloud/LLM-WIKI`.

Expected creates or updates:

```text
wiki/status/wiki-status.md
wiki/status/manifest.json
```

- [ ] **Step 3: Run graph extraction and relation analysis**

Run:

```bash
python3 scripts/extract_wiki_graph.py > /tmp/llm-wiki-seed-graph.json
python3 scripts/analyze_wiki_relations.py > /tmp/llm-wiki-seed-relations.json
```

from `/mnt/d/cloud/LLM-WIKI`.

Expected:

```text
/tmp/llm-wiki-seed-graph.json
/tmp/llm-wiki-seed-relations.json
```

- [ ] **Step 4: Run scorecard and utilization**

Run:

```bash
python3 scripts/score_wiki_semantics.py > /tmp/llm-wiki-seed-scorecard.json
python3 scripts/derive_wiki_utilization.py /tmp/llm-wiki-seed-scorecard.json > /tmp/llm-wiki-seed-utilization.json
```

from `/mnt/d/cloud/LLM-WIKI`.

Expected:

```text
/tmp/llm-wiki-seed-scorecard.json
/tmp/llm-wiki-seed-utilization.json
```

- [ ] **Step 5: Run medical-loop preview commands**

Run:

```bash
python3 scripts/build_wiki_medical_agent.py
python3 scripts/build_wiki_medical_case.py
python3 scripts/build_wiki_review_decisions.py
```

from `/mnt/d/cloud/LLM-WIKI`.

Expected:

```text
Each command exits 0. Output may be empty.
```

If these commands require explicit input flags, record the exact missing argument error and add seed-safe default invocation support in the current repo scripts before regenerating the target.

- [ ] **Step 6: Inspect target git status**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI status --short
```

Expected includes generated seed files and any status/medical preview artifacts from verification.

---

### Task 6: Commit Current Repo Tooling, Then Commit Target Seed

**Files:**

- Current repo commits already created in Tasks 1-3
- Target repo generated files under `/mnt/d/cloud/LLM-WIKI`

- [ ] **Step 1: Verify current repo latest commit and status**

Run in `/mnt/d/cloud/account-meeting-lore`:

```bash
git status --short
git log -1 --oneline
```

Expected:

```text
<latest seed-tooling commit>
```

Existing unrelated wiki/report/inbox changes may remain. Do not stage them.

- [ ] **Step 2: Review target diff summary**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI diff --stat
git -C /mnt/d/cloud/LLM-WIKI status --short
```

Expected: all target files are part of the seed migration.

- [ ] **Step 3: Commit target seed**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI add AGENTS.md PROJECT.md README.md .codex scripts wiki
git -C /mnt/d/cloud/LLM-WIKI commit -m "feat: initialize llm wiki seed"
```

Expected:

```text
[main <hash>] feat: initialize llm wiki seed
```

If the target repo has no first commit yet, this command creates the initial commit.

- [ ] **Step 4: Report push boundary**

Run:

```bash
git -C /mnt/d/cloud/LLM-WIKI status --short
git -C /mnt/d/cloud/LLM-WIKI log -1 --oneline
```

Expected:

```text
feat: initialize llm wiki seed
```

Do not push until the user explicitly approves the push.

---

## Self-Review

Spec coverage:

- Migration boundary is covered by Tasks 1-4.
- Real skill surface preservation is covered by Task 1 tests and manifest.
- Config and script migration is covered by Task 1 tests and manifest.
- Sanitized half-real examples are covered by Task 2 builder tests and generated sample files.
- Minimal verification is covered by Tasks 3 and 5.
- README polishing is explicitly deferred in generated `README.md` and the plan.

Blocked-term scan:

- The plan does not contain unresolved work markers.
- Quiet commands have explicit expected-exit wording; failures require captured stderr and narrow seed-safe fixes.

Scope boundary:

- The plan does not migrate private inbox, logs, report bundles, full medical history, or OpenSpec archive history.
- The plan does not rename the real wiki skill surface into generic `ingest/query/lint` skills.
- The plan does not push to GitHub without explicit user approval.
