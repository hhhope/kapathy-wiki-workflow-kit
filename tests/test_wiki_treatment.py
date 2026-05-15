import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.extract_wiki_graph import parse_frontmatter
from scripts.wiki_treatment import (
    apply_treatment_plan,
    build_treatment_plan,
    render_treatment_record_markdown,
    write_treatment_record,
)


class WikiTreatmentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-treatment-test-"))
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _package(self) -> dict:
        return {
            "full_detail_set": [
                {
                    "detail_id": "detail-safe",
                    "path": "wiki/ops/safe.md",
                    "candidate": {
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "wiki",
                            "ops_area": "wiki-runtime",
                            "canonical_object": "safe",
                            "artifact_type": "method",
                        }
                    },
                    "judgment": {"state": "accept", "reason": "strong evidence"},
                    "risk_flags": [],
                    "safe_to_apply_frontmatter": True,
                },
                {
                    "detail_id": "detail-unapproved",
                    "path": "wiki/ops/unapproved.md",
                    "candidate": {
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "report-workflow",
                            "ops_area": "report-quality",
                            "canonical_object": "unapproved",
                            "artifact_type": "method",
                        }
                    },
                    "judgment": {"state": "accept", "reason": "strong evidence"},
                    "risk_flags": [],
                    "safe_to_apply_frontmatter": True,
                },
                {
                    "detail_id": "detail-risky",
                    "path": "wiki/ops/risky.md",
                    "candidate": {
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "wiki",
                            "ops_area": "wiki-runtime",
                            "canonical_object": "risky",
                            "artifact_type": "method",
                        }
                    },
                    "judgment": {"state": "needs_user_confirmation", "reason": "weak relation"},
                    "risk_flags": ["relation_weak_evidence"],
                    "safe_to_apply_frontmatter": False,
                },
            ]
        }

    def test_builds_plan_only_for_approved_safe_candidates(self) -> None:
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})

        self.assertEqual(plan["summary"]["treatment_item_count"], 1)
        self.assertEqual(plan["treatment_items"][0]["detail_ref"], "detail-safe")
        self.assertEqual(plan["treatment_items"][0]["approval"], "domain:wiki")
        skipped = {item["detail_ref"]: item["reason"] for item in plan["skipped_items"]}
        self.assertEqual(skipped["detail-unapproved"], "missing explicit domain or detail approval")
        self.assertEqual(skipped["detail-risky"], "detail is not a safe frontmatter treatment candidate")
        self.assertIn("does not write relations", " ".join(plan["proof_boundary_notes"]))

    def test_builds_plan_for_explicit_detail_approval(self) -> None:
        plan = build_treatment_plan(
            self._package(),
            approved_detail_refs={"detail-unapproved"},
        )

        self.assertEqual(plan["summary"]["treatment_item_count"], 1)
        self.assertEqual(plan["treatment_items"][0]["detail_ref"], "detail-unapproved")
        self.assertEqual(plan["treatment_items"][0]["approval"], "detail:detail-unapproved")

    def test_apply_treatment_plan_is_dry_run_by_default(self) -> None:
        page = self.tmpdir / "wiki" / "ops" / "safe.md"
        page.write_text("# Safe\n", encoding="utf-8")
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})

        result = apply_treatment_plan(self.tmpdir, plan, apply=False)

        self.assertEqual(result["summary"]["applied_count"], 0)
        self.assertEqual(result["summary"]["dry_run_count"], 1)
        self.assertEqual(page.read_text(encoding="utf-8"), "# Safe\n")

    def test_apply_treatment_plan_writes_only_suggested_frontmatter_when_explicit(self) -> None:
        page = self.tmpdir / "wiki" / "ops" / "safe.md"
        page.write_text("# Safe\n", encoding="utf-8")
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})

        result = apply_treatment_plan(self.tmpdir, plan, apply=True)

        self.assertEqual(result["summary"]["applied_count"], 1)
        meta, body = parse_frontmatter(page.read_text(encoding="utf-8"))
        self.assertEqual(meta["layer"], "ops")
        self.assertEqual(meta["domain"], "wiki")
        self.assertEqual(meta["ops_area"], "wiki-runtime")
        self.assertEqual(meta["canonical_object"], "safe")
        self.assertEqual(meta["artifact_type"], "method")
        self.assertNotIn("related_objects", meta)
        self.assertIn("# Safe", body)

    def test_apply_treatment_plan_blocks_missing_targets(self) -> None:
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})

        result = apply_treatment_plan(self.tmpdir, plan, apply=True)

        self.assertEqual(result["summary"]["applied_count"], 0)
        self.assertEqual(result["summary"]["blocked_count"], 1)
        self.assertEqual(result["results"][0]["status"], "blocked")
        self.assertEqual(result["results"][0]["reason"], "target file does not exist")

    def test_writes_treatment_record_without_overwriting_existing_file(self) -> None:
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})
        result = {"summary": {"applied_count": 0, "dry_run_count": 1}, "results": []}
        output_dir = self.tmpdir / "records"

        first = write_treatment_record(
            plan,
            result,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )
        second = write_treatment_record(
            plan,
            result,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )

        self.assertEqual(first.name, "2026-05-15-010203-treatment.md")
        self.assertEqual(second.name, "2026-05-15-010203-treatment-2.md")
        markdown = first.read_text(encoding="utf-8")
        self.assertIn("# wiki-treatment Record", markdown)
        self.assertIn("detail-safe", markdown)

    def test_renders_record_with_proof_boundary(self) -> None:
        plan = build_treatment_plan(self._package(), approved_domains={"wiki"})
        markdown = render_treatment_record_markdown(
            plan,
            {"summary": {"applied_count": 0, "dry_run_count": 1}, "results": []},
            scan_root=self.tmpdir,
        )

        self.assertIn("## Treatment Items", markdown)
        self.assertIn("## Skipped Items", markdown)
        self.assertIn("## Proof Boundary", markdown)
        self.assertIn("does not write relations", markdown)

    def test_cli_defaults_to_dry_run_json_and_writes_record_only_when_requested(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - wiki
  ops_area:
    allowed:
      - wiki-runtime
strict_gate:
  enabled: true
  rule_sets: {}
""",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "safe-method.md").write_text(
            """---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: safe-method
artifact_type: method
---

# Safe Method

This page documents wiki runtime behavior.
""",
            encoding="utf-8",
        )
        record_dir = self.tmpdir / "treatment-records"

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_treatment.py",
                "--root",
                str(self.tmpdir),
                "--approved-domain",
                "wiki",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        default_payload = json.loads(default_result.stdout)

        self.assertFalse(default_payload["applied"])
        self.assertGreaterEqual(default_payload["plan"]["summary"]["treatment_item_count"], 1)
        self.assertFalse(record_dir.exists())

        write_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_treatment.py",
                "--root",
                str(self.tmpdir),
                "--approved-domain",
                "wiki",
                "--write-treatment-record",
                "--treatment-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        write_payload = json.loads(write_result.stdout)

        self.assertIn("treatment_record_path", write_payload)
        self.assertTrue(Path(write_payload["treatment_record_path"]).exists())


if __name__ == "__main__":
    unittest.main()
