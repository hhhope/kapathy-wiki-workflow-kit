import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_surgery import (
    build_surgery_plan,
    render_surgery_record_markdown,
    write_surgery_record,
)


class WikiSurgeryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-surgery-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _adjudication_package(self) -> dict:
        return {
            "summary": {"full_detail_count": 5},
            "full_detail_set": [
                {
                    "detail_id": "detail-relation",
                    "path": "wiki/ops/relation.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "weak relation"},
                    "risk_flags": ["relation_weak_evidence"],
                },
                {
                    "detail_id": "detail-governance",
                    "path": "wiki/ops/drift-retro.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "drift"},
                    "risk_flags": ["drift_risk", "openspec_required"],
                },
                {
                    "detail_id": "detail-taxonomy",
                    "path": "wiki/ops/taxonomy.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "new taxonomy"},
                    "risk_flags": ["taxonomy_candidate"],
                },
                {
                    "detail_id": "detail-adr",
                    "path": "wiki/adr/0001-example.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "ADR"},
                    "risk_flags": ["adr_risk"],
                },
                {
                    "detail_id": "detail-safe",
                    "path": "wiki/ops/safe.md",
                    "judgment": {"state": "accept", "reason": "safe"},
                    "risk_flags": [],
                    "safe_to_apply_frontmatter": True,
                },
            ],
        }

    def _moc_plan(self) -> dict:
        return {
            "summary": {"candidate_count": 4, "create_count": 1, "update_count": 1, "noop_count": 1, "orphan_count": 1},
            "entries": [
                {"action": "create", "kind": "domain", "key": "wiki", "path": "wiki/moc/domain-wiki.md", "link_count": 10},
                {"action": "update", "kind": "object", "key": "runtime", "path": "wiki/moc/object-runtime.md", "link_count": 3},
                {"action": "noop", "kind": "object", "key": "noop", "path": "wiki/moc/object-noop.md", "link_count": 1},
                {"action": "orphan", "kind": "unknown", "key": "old", "path": "wiki/moc/old.md", "link_count": 0},
            ],
        }

    def test_builds_surgery_plan_from_risky_adjudication_details(self) -> None:
        plan = build_surgery_plan(self._adjudication_package())

        self.assertEqual(plan["summary"]["surgery_item_count"], 4)
        self.assertEqual(plan["summary"]["relation_rebuild_count"], 1)
        self.assertEqual(plan["summary"]["governance_change_count"], 2)
        self.assertEqual(plan["summary"]["taxonomy_decision_count"], 1)
        refs = {item["detail_ref"] for item in plan["surgery_items"]}
        self.assertEqual(refs, {"detail-relation", "detail-governance", "detail-taxonomy", "detail-adr"})
        self.assertNotIn("detail-safe", refs)
        self.assertIn("does not write frontmatter", " ".join(plan["proof_boundary_notes"]))

    def test_includes_non_noop_moc_projection_items(self) -> None:
        plan = build_surgery_plan(self._adjudication_package(), moc_plan=self._moc_plan())

        self.assertEqual(plan["summary"]["moc_projection_count"], 3)
        self.assertEqual(
            {item["action"] for item in plan["moc_projection_items"]},
            {"create", "update", "orphan"},
        )
        self.assertNotIn(
            "wiki/moc/object-noop.md",
            {item["path"] for item in plan["moc_projection_items"]},
        )

    def test_blocks_planning_when_adjudication_eval_fails(self) -> None:
        package = self._adjudication_package()
        package["eval_result"] = {
            "passed": False,
            "errors": ["detail-0001: judgment missing evidence"],
        }

        plan = build_surgery_plan(package, moc_plan=self._moc_plan())

        self.assertEqual(plan["status"], "blocked")
        self.assertEqual(plan["blocked_reason"], "adjudication eval failed")
        self.assertEqual(plan["summary"]["surgery_item_count"], 0)
        self.assertEqual(plan["summary"]["moc_projection_count"], 0)
        self.assertIn("adjudication eval did not pass", " ".join(plan["proof_boundary_notes"]))

    def test_writes_surgery_record_without_overwriting_existing_file(self) -> None:
        plan = build_surgery_plan(self._adjudication_package(), moc_plan=self._moc_plan())
        output_dir = self.tmpdir / "records"

        first = write_surgery_record(
            plan,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )
        second = write_surgery_record(
            plan,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )

        self.assertEqual(first.name, "2026-05-15-010203-surgery.md")
        self.assertEqual(second.name, "2026-05-15-010203-surgery-2.md")
        self.assertIn("# wiki-surgery Plan Record", first.read_text(encoding="utf-8"))

    def test_renders_record_with_next_review_actions(self) -> None:
        markdown = render_surgery_record_markdown(
            build_surgery_plan(self._adjudication_package(), moc_plan=self._moc_plan()),
            scan_root=self.tmpdir,
        )

        self.assertIn("## Surgery Items", markdown)
        self.assertIn("## MOC Projection Items", markdown)
        self.assertIn("## Proof Boundary", markdown)
        self.assertIn("## Next Review Actions", markdown)
        self.assertIn("not surgery approval", markdown)

    def test_cli_outputs_json_and_writes_record_only_when_requested(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - wiki
      - unclassified
  ops_area:
    allowed:
      - wiki-runtime
strict_gate:
  enabled: true
  rule_sets: {}
""",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "relation-note.md").write_text(
            "# Relation Note\n\nThis page mentions wiki runtime and weak relation evidence.\n",
            encoding="utf-8",
        )
        moc_plan_path = self.tmpdir / "moc-plan.json"
        moc_plan_path.write_text(json.dumps(self._moc_plan()), encoding="utf-8")
        record_dir = self.tmpdir / "surgery-records"

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_surgery.py",
                "--root",
                str(self.tmpdir),
                "--moc-plan",
                str(moc_plan_path),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        default_payload = json.loads(default_result.stdout)

        self.assertGreaterEqual(default_payload["summary"]["surgery_item_count"], 1)
        self.assertEqual(default_payload["summary"]["moc_projection_count"], 3)
        self.assertNotIn("surgery_record_path", default_payload)
        self.assertFalse(record_dir.exists())

        write_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_surgery.py",
                "--root",
                str(self.tmpdir),
                "--moc-plan",
                str(moc_plan_path),
                "--write-surgery-record",
                "--surgery-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        write_payload = json.loads(write_result.stdout)

        self.assertIn("surgery_record_path", write_payload)
        self.assertTrue(Path(write_payload["surgery_record_path"]).exists())


if __name__ == "__main__":
    unittest.main()
