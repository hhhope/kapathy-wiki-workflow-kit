import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_review_decisions import (
    build_review_decision_package,
    render_review_decision_markdown,
    write_review_decision_record,
)


class WikiReviewDecisionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-review-decisions-test-"))
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

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_classifies_review_details_into_required_buckets(self) -> None:
        adjudication_package = {
            "summary": {"full_detail_count": 6},
            "full_detail_set": [
                {
                    "detail_id": "detail-accepted",
                    "path": "wiki/ops/accepted.md",
                    "judgment": {"state": "accept", "reason": "strong evidence"},
                    "risk_flags": [],
                },
                {
                    "detail_id": "detail-treatment",
                    "path": "wiki/ops/treatment.md",
                    "candidate": {
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "wiki",
                            "ops_area": "wiki-runtime",
                            "canonical_object": "treatment",
                            "artifact_type": "method",
                        }
                    },
                    "judgment": {"state": "likely", "reason": "bounded frontmatter candidate"},
                    "risk_flags": [],
                    "safe_to_apply_frontmatter": True,
                },
                {
                    "detail_id": "detail-surgery",
                    "path": "wiki/ops/relation.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "weak relation"},
                    "risk_flags": ["relation_weak_evidence"],
                },
                {
                    "detail_id": "detail-openspec",
                    "path": "wiki/ops/taxonomy.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "new taxonomy"},
                    "risk_flags": ["taxonomy_candidate"],
                },
                {
                    "detail_id": "detail-deferred",
                    "path": "wiki/ops/uncertain.md",
                    "judgment": {"state": "needs_user_confirmation", "reason": "agent uncertain"},
                    "risk_flags": ["agent_uncertain"],
                },
                {
                    "detail_id": "detail-rejected",
                    "path": "wiki/ops/rejected.md",
                    "judgment": {"state": "reject", "reason": "insufficient evidence"},
                    "risk_flags": [],
                    "rejected_candidates": [
                        {"field": "domain", "value": "auto_accept_unclassified"}
                    ],
                },
            ],
        }

        package = build_review_decision_package(
            adjudication_package,
            source_record="wiki/ops/wiki-doctor-runs/diagnosis.md",
        )

        self.assertEqual(package["source_record"], "wiki/ops/wiki-doctor-runs/diagnosis.md")
        self.assertEqual(package["summary"]["accepted_candidates_count"], 1)
        self.assertEqual(package["summary"]["treatment_candidates_count"], 1)
        self.assertEqual(package["summary"]["surgery_candidates_count"], 1)
        self.assertEqual(package["summary"]["openspec_required_count"], 1)
        self.assertEqual(package["summary"]["deferred_items_count"], 3)
        self.assertEqual(package["summary"]["rejected_candidates_count"], 1)
        self.assertEqual(package["accepted_candidates"][0]["detail_ref"], "detail-accepted")
        self.assertEqual(package["accepted_candidates"][0]["path"], "wiki/ops/accepted.md")
        self.assertEqual(package["accepted_candidates"][0]["reason"], "strong evidence")
        self.assertEqual(package["treatment_candidates"][0]["detail_ref"], "detail-treatment")
        self.assertEqual(
            package["treatment_candidates"][0]["suggested_frontmatter"]["canonical_object"],
            "treatment",
        )
        self.assertEqual(package["surgery_candidates"][0]["detail_ref"], "detail-surgery")
        self.assertEqual(package["openspec_required"][0]["detail_ref"], "detail-openspec")
        self.assertEqual(
            {item["detail_ref"] for item in package["deferred_items"]},
            {"detail-surgery", "detail-openspec", "detail-deferred"},
        )
        self.assertEqual(package["rejected_candidates"][0]["detail_ref"], "detail-rejected")
        self.assertEqual(package["rejected_candidates"][0]["risk_flags"], [])

    def test_renders_markdown_with_required_sections_and_proof_boundary(self) -> None:
        package = build_review_decision_package(
            {
                "summary": {"full_detail_count": 1},
                "full_detail_set": [
                    {
                        "detail_id": "detail-0001",
                        "path": "wiki/ops/treatment.md",
                        "judgment": {"state": "likely", "reason": "bounded frontmatter candidate"},
                        "risk_flags": [],
                        "safe_to_apply_frontmatter": True,
                    }
                ],
            },
            source_record="wiki/ops/wiki-doctor-runs/diagnosis.md",
        )

        markdown = render_review_decision_markdown(package, scan_root=self.tmpdir, limit=50)

        for heading in [
            "# wiki-confirm Confirmation Record",
            "## Source / 检查来源",
            "## Decision Rules / 确诊标准",
            "## Summary",
            "## Confirmed Buckets / 确诊分流",
            "## Accepted Candidates",
            "## Treatment Candidates",
            "## Surgery Candidates",
            "## OpenSpec Required",
            "## Deferred Items",
            "## Rejected Candidates",
            "## Abnormal Findings / 异常明细",
            "## Medical Advice / 处理建议",
            "## Proof Boundary",
            "## Next Actions",
        ]:
            self.assertIn(heading, markdown)
        self.assertIn("detail-0001 `wiki/ops/treatment.md`", markdown)
        self.assertIn("draft review routing only", markdown)
        self.assertIn("not human approval", markdown)
        self.assertIn("does not write frontmatter, taxonomy, relations, MOC, or OpenSpec state", markdown)

    def test_writes_decision_record_without_overwriting_existing_file(self) -> None:
        package = build_review_decision_package({"full_detail_set": []})
        output_dir = self.tmpdir / "records"

        first = write_review_decision_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T01:02:03+00:00",
        )
        second = write_review_decision_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T01:02:03+00:00",
        )

        self.assertEqual(first.name, "2026-05-14-010203-review-decisions.md")
        self.assertEqual(second.name, "2026-05-14-010203-review-decisions-2.md")
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())
        self.assertIn("# wiki-confirm Confirmation Record", first.read_text(encoding="utf-8"))

    def test_cli_writes_complete_confirmation_record_by_default(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        record_dir = self.tmpdir / "decision-records"
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True, exist_ok=True)
        (self.tmpdir / "wiki" / "ops" / "first-runtime-note.md").write_text(
            "# First Runtime Note\n\nThis wiki runtime note is reviewable.\n",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "second-runtime-note.md").write_text(
            "# Second Runtime Note\n\nThis wiki runtime note is also reviewable.\n",
            encoding="utf-8",
        )

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_review_decisions.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "1",
                "--source-record",
                "wiki/ops/wiki-doctor-runs/diagnosis.md",
                "--decision-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        default_payload = json.loads(default_result.stdout)

        self.assertEqual(default_payload["source_record"], "wiki/ops/wiki-doctor-runs/diagnosis.md")
        self.assertIn("decision_record_path", default_payload)
        self.assertIn("summary", default_payload)
        self.assertNotIn("full_detail_set", default_payload)
        record_path = Path(default_payload["decision_record_path"])
        self.assertEqual(record_path.parent, record_dir.resolve())
        self.assertTrue(record_path.exists())
        record_text = record_path.read_text(encoding="utf-8")
        self.assertIn("# wiki-confirm Confirmation Record", record_text)
        self.assertIn("## Decision Rules / 确诊标准", record_text)
        self.assertIn("## Confirmed Buckets / 确诊分流", record_text)
        self.assertIn("## Abnormal Findings / 异常明细", record_text)
        self.assertIn("## Medical Advice / 处理建议", record_text)
        self.assertIn("second-runtime-note.md", record_text)

    def test_cli_stdout_json_only_preserves_non_writing_confirmation_debug_mode(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        record_dir = self.tmpdir / "decision-records"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_review_decisions.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "0",
                "--source-record",
                "wiki/ops/wiki-doctor-runs/diagnosis.md",
                "--stdout-json-only",
                "--decision-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["source_record"], "wiki/ops/wiki-doctor-runs/diagnosis.md")
        self.assertNotIn("decision_record_path", payload)
        self.assertIn("deferred_items", payload)
        self.assertFalse(record_dir.exists())


if __name__ == "__main__":
    unittest.main()
