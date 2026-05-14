import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.build_wiki_status import build_manifest, render_status_markdown, write_status_outputs


class WikiStatusTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-status-test-"))
        (self.tmpdir / "wiki" / "sources").mkdir(parents=True)
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "inbox").mkdir(parents=True)
        (self.tmpdir / "openspec" / "changes").mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_manifest_marks_inbox_files_without_source_record_as_pending(self) -> None:
        represented = self.tmpdir / "inbox" / "represented.txt"
        pending = self.tmpdir / "inbox" / "pending.txt"
        represented.write_text("already captured", encoding="utf-8")
        pending.write_text("needs source page", encoding="utf-8")
        (self.tmpdir / "wiki" / "sources" / "represented.md").write_text(
            """---
title: Represented
source_path: inbox/represented.txt
source_type: note
status: draft
---

# Represented
""",
            encoding="utf-8",
        )

        manifest = build_manifest(self.tmpdir)

        inbox_by_path = {item["path"]: item for item in manifest["inbox_files"]}
        self.assertTrue(inbox_by_path["inbox/represented.txt"]["represented_by_source"])
        self.assertFalse(inbox_by_path["inbox/pending.txt"]["represented_by_source"])
        self.assertEqual(manifest["summary"]["pending_inbox_count"], 1)

    def test_manifest_summarizes_active_and_complete_openspec_changes(self) -> None:
        active_dir = self.tmpdir / "openspec" / "changes" / "active-change"
        complete_dir = self.tmpdir / "openspec" / "changes" / "complete-change"
        active_dir.mkdir()
        complete_dir.mkdir()
        (active_dir / "tasks.md").write_text(
            "- [x] done\n- [ ] pending\n",
            encoding="utf-8",
        )
        (complete_dir / "tasks.md").write_text(
            "- [x] done\n- [x] also done\n",
            encoding="utf-8",
        )

        manifest = build_manifest(self.tmpdir)

        changes = {item["change_id"]: item for item in manifest["openspec_changes"]}
        self.assertEqual(changes["active-change"]["state"], "active")
        self.assertEqual(changes["active-change"]["done_tasks"], 1)
        self.assertEqual(changes["complete-change"]["state"], "complete")
        self.assertEqual(manifest["summary"]["active_change_count"], 1)
        self.assertEqual(manifest["summary"]["complete_change_count"], 1)

    def test_writes_manifest_and_status_report(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "sample.md").write_text(
            """---
canonical_object: sample
artifact_type: note
---

# Sample
""",
            encoding="utf-8",
        )

        output_dir = self.tmpdir / "wiki" / "status"
        manifest_path, status_path = write_status_outputs(self.tmpdir, output_dir)

        self.assertTrue(manifest_path.exists())
        self.assertTrue(status_path.exists())
        status_text = status_path.read_text(encoding="utf-8")
        self.assertIn("# Wiki Status", status_text)
        self.assertIn("wiki/ops", status_text)
        self.assertIn("Next Actions", status_text)

    def test_status_report_lists_pending_inbox_files(self) -> None:
        (self.tmpdir / "inbox" / "new-material.txt").write_text("raw", encoding="utf-8")

        status_text = render_status_markdown(build_manifest(self.tmpdir))

        self.assertIn("Pending Inbox Files", status_text)
        self.assertIn("inbox/new-material.txt", status_text)

    def test_manifest_ignores_inbox_readme(self) -> None:
        (self.tmpdir / "inbox" / "README.md").write_text("usage notes", encoding="utf-8")

        manifest = build_manifest(self.tmpdir)

        self.assertEqual(manifest["summary"]["inbox_file_count"], 0)
        self.assertEqual(manifest["summary"]["pending_inbox_count"], 0)
        self.assertEqual(manifest["pending_inbox_files"], [])

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

    def test_product_status_unresolved_items_include_complete_openspec_changes(self) -> None:
        complete_dir = self.tmpdir / "openspec" / "changes" / "complete-change"
        complete_dir.mkdir()
        (complete_dir / "tasks.md").write_text(
            "- [x] done\n- [x] also done\n",
            encoding="utf-8",
        )

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

    def test_manifest_and_status_report_surface_domain_taxonomy_health(self) -> None:
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - none
      - unclassified
    forbidden:
      - personal-ops
severity:
  forbidden_domain: error
""",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "domain-drift.md").write_text(
            """---
layer: ops
domain: personal-ops
ops_area: agent-governance
canonical_object: domain-drift
artifact_type: retro
---

# Domain Drift
""",
            encoding="utf-8",
        )

        manifest = build_manifest(self.tmpdir)
        health = manifest["domain_taxonomy_health"]

        self.assertEqual(health["status"], "drift")
        self.assertEqual(health["summary"]["error"], 1)
        self.assertEqual(health["entries"][0]["kind"], "forbidden_domain")
        self.assertEqual(health["entries"][0]["path"], "wiki/ops/domain-drift.md")

        status_text = render_status_markdown(manifest)
        self.assertIn("## Domain Taxonomy Health", status_text)
        self.assertIn("forbidden_domain", status_text)
        self.assertIn("wiki/ops/domain-drift.md", status_text)

    def test_manifest_and_status_report_surface_empty_parsed_relation_fields(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "empty-relation.md").write_text(
            """---
canonical_object: empty-relation
artifact_type: retro
related_objects:
---

# Empty Relation
""",
            encoding="utf-8",
        )

        manifest = build_manifest(self.tmpdir)
        health = manifest["graph_parse_health"]

        self.assertEqual(health["status"], "drift")
        self.assertEqual(health["summary"]["total"], 1)
        self.assertEqual(
            health["entries"][0],
            {
                "type": "graph_parse_health",
                "path": "wiki/ops/empty-relation.md",
                "fields": ["related_objects"],
                "problem": "raw relation frontmatter exists, but parsed relation value is empty",
                "repair_route": "runtime-parser-fix",
            },
        )

        status_text = render_status_markdown(manifest)
        self.assertIn("## Graph Parse Health", status_text)
        self.assertIn("runtime-parser-fix", status_text)
        self.assertIn("wiki/ops/empty-relation.md", status_text)

    def test_indented_relation_lists_are_parsed_as_relation_coverage(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "indented-relation.md").write_text(
            """---
canonical_object: indented-relation
artifact_type: retro
derived_from:
  - wiki/ops/source-page.md
related_objects:
  - wiki-frontmatter-model
---

# Indented Relation
""",
            encoding="utf-8",
        )

        manifest = build_manifest(self.tmpdir)

        self.assertEqual(
            manifest["product_status"]["relation_coverage"],
            {"with_relations": 1, "missing_relations": 0},
        )
        self.assertEqual(manifest["graph_parse_health"]["status"], "pass")
        self.assertEqual(manifest["graph_parse_health"]["entries"], [])


if __name__ == "__main__":
    unittest.main()
