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


if __name__ == "__main__":
    unittest.main()
