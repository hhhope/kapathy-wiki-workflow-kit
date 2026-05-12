# Product Status Contract Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `Superpowers:subagent-driven-development` when the user explicitly asks for parallel/subagent execution, otherwise use `Superpowers:executing-plans`. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the smallest computable product-status contract in the existing wiki status manifest and Markdown report.

**Architecture:** Keep `scripts/build_wiki_status.py` as orchestration only. Extract product-status computation to `scripts/wiki_product_status.py` and Markdown rendering to `scripts/wiki_status_render.py`, because `scripts/build_wiki_status.py` is already near the Python large-file guardrail.

**Tech Stack:** Python standard library, `unittest`, existing `scripts.extract_wiki_graph.parse_frontmatter`, OpenSpec CLI.

---

## File Structure

- Create: `scripts/wiki_product_status.py`
  - Owns contract constants, conservative classification, coverage counts, and unresolved item creation.
- Create: `scripts/wiki_status_render.py`
  - Owns Markdown table helpers and `render_status_markdown`.
- Modify: `scripts/build_wiki_status.py`
  - Keeps collection, manifest assembly, output writing, and CLI.
  - Preserves explicit identity/relation metadata in page records.
  - Calls `build_product_status`.
  - Imports `render_status_markdown` for backwards-compatible callers.
- Modify: `tests/test_wiki_status.py`
  - Adds integration tests for manifest and Markdown surface.
- Create: `tests/test_wiki_product_status.py`
  - Adds focused contract/helper tests when implementation logic grows beyond integration coverage.
- Modify generated: `wiki/status/manifest.json`
- Modify generated: `wiki/status/wiki-status.md`
- Do not touch unrelated dirty wiki/report/inbox files during this change.

## Task 1: RED Tests For Product Status Contract

**Files:**
- Modify: `tests/test_wiki_status.py`

- [ ] **Step 1: Add contract skeleton RED test**

Append this test method inside `WikiStatusTest`:

```python
    def test_manifest_includes_product_status_contract_version(self) -> None:
        manifest = build_manifest(self.tmpdir)
        product_status = manifest["product_status"]

        self.assertEqual(product_status["contract_version"], "1")
        self.assertEqual(product_status["object_type_counts"], {})
        self.assertEqual(product_status["readiness_counts"], {})
        self.assertEqual(product_status["source_layer_counts"], {})
        self.assertEqual(
            product_status["identity_coverage"],
            {"with_identity": 0, "missing_identity": 0},
        )
        self.assertEqual(
            product_status["relation_coverage"],
            {"with_relations": 0, "missing_relations": 0},
        )
        self.assertEqual(product_status["unresolved_items"], [])
```

- [ ] **Step 2: Add source classification RED test**

```python
    def test_product_status_counts_source_records_as_source_objects(self) -> None:
        (self.tmpdir / "wiki" / "sources" / "captured.md").write_text(
            """---
title: Captured
source_path: inbox/captured.txt
source_type: note
status: draft
---

# Captured
""",
            encoding="utf-8",
        )

        product_status = build_manifest(self.tmpdir)["product_status"]

        self.assertEqual(product_status["object_type_counts"]["source"], 1)
        self.assertEqual(product_status["source_layer_counts"]["source"], 1)
        self.assertEqual(product_status["readiness_counts"]["draft-only"], 1)
```

- [ ] **Step 3: Add identity/relation coverage RED test**

```python
    def test_product_status_counts_identity_and_relation_frontmatter_coverage(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "linked.md").write_text(
            """---
canonical_object: linked-object
artifact_type: method
related_objects:
- source-object
---

# Linked
""",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "loose.md").write_text("# Loose\n", encoding="utf-8")

        product_status = build_manifest(self.tmpdir)["product_status"]

        self.assertEqual(
            product_status["identity_coverage"],
            {"with_identity": 1, "missing_identity": 1},
        )
        self.assertEqual(
            product_status["relation_coverage"],
            {"with_relations": 1, "missing_relations": 1},
        )
```

- [ ] **Step 4: Run RED verification**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_wiki_status.WikiStatusTest.test_manifest_includes_product_status_contract_version \
  tests.test_wiki_status.WikiStatusTest.test_product_status_counts_source_records_as_source_objects \
  tests.test_wiki_status.WikiStatusTest.test_product_status_counts_identity_and_relation_frontmatter_coverage
```

Expected: `KeyError: 'product_status'`.

- [ ] **Step 5: Commit RED tests only**

```bash
git add tests/test_wiki_status.py
git commit -m "test: cover product status contract"
```

## Task 2: RED Tests For Unresolved Items And Markdown

**Files:**
- Modify: `tests/test_wiki_status.py`

- [ ] **Step 1: Add pending inbox unresolved RED test**

```python
    def test_product_status_unresolved_items_include_pending_inbox_files(self) -> None:
        (self.tmpdir / "inbox" / "new-material.txt").write_text("raw", encoding="utf-8")

        unresolved = build_manifest(self.tmpdir)["product_status"]["unresolved_items"]

        self.assertIn(
            {
                "type": "pending_inbox",
                "path": "inbox/new-material.txt",
                "readiness_label": "blocked",
                "status_transition": "evidence_collection",
            },
            unresolved,
        )
```

- [ ] **Step 2: Add complete OpenSpec unresolved RED test**

```python
    def test_product_status_unresolved_items_include_complete_openspec_changes(self) -> None:
        complete_dir = self.tmpdir / "openspec" / "changes" / "complete-change"
        complete_dir.mkdir()
        (complete_dir / "tasks.md").write_text("- [x] done\n- [x] also done\n", encoding="utf-8")

        product_status = build_manifest(self.tmpdir)["product_status"]

        self.assertEqual(product_status["object_type_counts"]["governance"], 1)
        self.assertEqual(product_status["source_layer_counts"]["spec"], 1)
        self.assertIn(
            {
                "type": "complete_openspec_change",
                "change_id": "complete-change",
                "readiness_label": "unresolved",
                "status_transition": "archive_review",
            },
            product_status["unresolved_items"],
        )
```

- [ ] **Step 3: Add Markdown RED test**

```python
    def test_status_report_renders_product_status_section(self) -> None:
        (self.tmpdir / "inbox" / "new-material.txt").write_text("raw", encoding="utf-8")

        status_text = render_status_markdown(build_manifest(self.tmpdir))

        self.assertIn("## Product Status", status_text)
        self.assertIn("Contract version: `1`", status_text)
        self.assertIn("Object Types", status_text)
        self.assertIn("Readiness", status_text)
        self.assertIn("Source Layers", status_text)
        self.assertIn("Identity Coverage", status_text)
        self.assertIn("Relation Coverage", status_text)
        self.assertIn("Unresolved Product Status Items", status_text)
        self.assertIn("inbox/new-material.txt", status_text)
```

- [ ] **Step 4: Run RED verification**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_wiki_status.WikiStatusTest.test_product_status_unresolved_items_include_pending_inbox_files \
  tests.test_wiki_status.WikiStatusTest.test_product_status_unresolved_items_include_complete_openspec_changes \
  tests.test_wiki_status.WikiStatusTest.test_status_report_renders_product_status_section
```

Expected: `KeyError: 'product_status'` or missing `## Product Status`.

- [ ] **Step 5: Commit RED tests only**

```bash
git add tests/test_wiki_status.py
git commit -m "test: cover product status unresolved surface"
```

## Task 3: Product Status Computation Module

**Files:**
- Create: `scripts/wiki_product_status.py`
- Modify: `scripts/build_wiki_status.py`
- Test: `tests/test_wiki_status.py`

- [ ] **Step 1: Create `scripts/wiki_product_status.py`**

Required public functions:

```python
def relation_fields_from_meta(meta: dict[str, object]) -> dict[str, object]:
    ...


def build_product_status(
    pages: list[dict[str, object]],
    inbox_files: list[dict[str, object]],
    openspec_changes: list[dict[str, object]],
) -> dict[str, object]:
    ...
```

Required contract shape:

```python
{
    "contract_version": "1",
    "object_type_counts": {},
    "readiness_counts": {},
    "source_layer_counts": {},
    "identity_coverage": {"with_identity": 0, "missing_identity": 0},
    "relation_coverage": {"with_relations": 0, "missing_relations": 0},
    "unresolved_items": [],
}
```

- [ ] **Step 2: Conservative classification rules**

- `wiki/sources/*` -> object type `source`, source layer `source`.
- `wiki/reports/*` -> object type `output`, source layer `report`.
- `wiki/status/*` -> object type `status`, source layer `generated_status`.
- `wiki/adr/*` and OpenSpec changes -> object type `governance`, source layer `spec`.
- `wiki/ops/*` -> object type `behavior` only when explicit `artifact_type` contains `replay`, `validation`, or `evaluation`; otherwise `unknown`.
- `status: accepted` -> readiness `accepted`.
- `status: draft`, `candidate`, `active`, or missing -> readiness `draft-only`.
- Pending inbox file -> unresolved item with type `pending_inbox`, readiness `blocked`, transition `evidence_collection`.
- Complete active-dir OpenSpec change -> unresolved item with type `complete_openspec_change`, readiness `unresolved`, transition `archive_review`.

- [ ] **Step 3: Preserve explicit relation metadata in page records**

In `_collect_wiki_pages`, keep relation fields from frontmatter:

```python
"related_objects": meta.get("related_objects"),
"related_sources": meta.get("related_sources"),
"derived_from": meta.get("derived_from"),
"validates": meta.get("validates"),
"related_focus_threads": meta.get("related_focus_threads"),
"related_reminders": meta.get("related_reminders"),
```

- [ ] **Step 4: Add product status to manifest**

In `build_manifest`, add:

```python
product_status = build_product_status(pages, inbox_files, changes)
```

and return top-level:

```python
"product_status": product_status,
```

- [ ] **Step 5: Run focused GREEN verification**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_wiki_status.WikiStatusTest.test_manifest_includes_product_status_contract_version \
  tests.test_wiki_status.WikiStatusTest.test_product_status_counts_source_records_as_source_objects \
  tests.test_wiki_status.WikiStatusTest.test_product_status_counts_identity_and_relation_frontmatter_coverage \
  tests.test_wiki_status.WikiStatusTest.test_product_status_unresolved_items_include_pending_inbox_files \
  tests.test_wiki_status.WikiStatusTest.test_product_status_unresolved_items_include_complete_openspec_changes
```

Expected: product-status manifest tests pass.

- [ ] **Step 6: Commit computation module and manifest wiring**

```bash
git add scripts/wiki_product_status.py scripts/build_wiki_status.py tests/test_wiki_status.py
git commit -m "feat: add product status manifest contract"
```

## Task 4: Markdown Rendering Module

**Files:**
- Create: `scripts/wiki_status_render.py`
- Modify: `scripts/build_wiki_status.py`
- Test: `tests/test_wiki_status.py`

- [ ] **Step 1: Move Markdown rendering out of `build_wiki_status.py`**

Move `_markdown_table` and `render_status_markdown` into `scripts/wiki_status_render.py`. Keep this import in `scripts/build_wiki_status.py` so existing callers and tests still work:

```python
from scripts.wiki_status_render import render_status_markdown
```

- [ ] **Step 2: Render Product Status section**

Add `## Product Status` after `## Wiki Sections` and before `## Pending Inbox Files`.

Required rendered strings:

- `Contract version: `1``
- `Object Types`
- `Readiness`
- `Source Layers`
- `Identity Coverage`
- `Relation Coverage`
- `Unresolved Product Status Items`

- [ ] **Step 3: Run focused Markdown GREEN verification**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_wiki_status.WikiStatusTest.test_status_report_renders_product_status_section
```

Expected: PASS.

- [ ] **Step 4: Run all wiki status tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_wiki_status
```

Expected: PASS.

- [ ] **Step 5: Commit rendering module**

```bash
git add scripts/wiki_status_render.py scripts/build_wiki_status.py tests/test_wiki_status.py
git commit -m "feat: render product status dashboard"
```

## Task 5: Generated Status Artifacts

**Files:**
- Modify generated: `wiki/status/manifest.json`
- Modify generated: `wiki/status/wiki-status.md`

- [ ] **Step 1: Regenerate wiki status**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_wiki_status.py
```

Expected:

```text
Wrote /mnt/d/cloud/account-meeting-lore/wiki/status/manifest.json
Wrote /mnt/d/cloud/account-meeting-lore/wiki/status/wiki-status.md
```

- [ ] **Step 2: Inspect generated artifacts**

Run:

```bash
rg -n "product_status|Product Status|Contract version|Unresolved Product Status" wiki/status/manifest.json wiki/status/wiki-status.md
```

Expected: matches in both generated files.

- [ ] **Step 3: Commit generated artifacts**

```bash
git add wiki/status/manifest.json wiki/status/wiki-status.md
git commit -m "docs: refresh wiki status product contract"
```

## Task 6: OpenSpec Task Sync And Final Verification

**Files:**
- Modify: `openspec/changes/add-product-status-contract/tasks.md`

- [ ] **Step 1: Run focused tests**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_wiki_status
```

- [ ] **Step 2: Run full tests**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```

- [ ] **Step 3: Run OpenSpec validation**

```bash
openspec validate add-product-status-contract --strict
openspec validate --all
git diff --check
```

PostHog DNS flush warnings after successful local validation are telemetry noise.

- [ ] **Step 4: Update OpenSpec tasks with verification notes**

Mark completed items in `openspec/changes/add-product-status-contract/tasks.md` and add short HTML comments with command evidence.

- [ ] **Step 5: Commit task sync**

```bash
git add openspec/changes/add-product-status-contract/tasks.md
git commit -m "docs: mark product status contract tasks complete"
```

## Self-Review

- Spec coverage: tasks cover product contract fields, wiki status manifest, Markdown report, tests, generated artifacts, and OpenSpec verification.
- Placeholder scan: no `TBD` or `TODO`; every code-changing step includes concrete tests and commands.
- Boundary check: plan does not change public-report, learning-capture, graph, Feishu, archive, or unrelated dirty material.
- File size check: plan creates `scripts/wiki_product_status.py` and `scripts/wiki_status_render.py` so `scripts/build_wiki_status.py` does not absorb new classification or rendering responsibilities.

## Execution Choice

The OpenSpec change is active and this plan is change-local. Because the user explicitly requested parallel work, use `Superpowers:subagent-driven-development` for implementation if continuing now. If the user wants fewer moving parts, use inline execution with `Superpowers:executing-plans`.
