import shutil
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_content_adjudication import (
    build_adjudication_package,
    evaluate_adjudication_package,
)


class WikiContentAdjudicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-adjudication-test-"))
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)
        (self.tmpdir / "wiki" / "adr").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - none
      - unclassified
      - wiki
      - report-workflow
  ops_area:
    allowed:
      - agent-governance
      - wiki-runtime
      - workflow-trace
strict_gate:
  enabled: true
  rule_sets: {}
""",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_builds_full_detail_and_focus_review_sets(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "runtime-boundary-drift-retro.md").write_text(
            """# Runtime Boundary Drift

This drift retro records a wiki-react eval apply boundary mismatch.
""",
            encoding="utf-8",
        )

        package = build_adjudication_package(self.tmpdir)

        self.assertEqual(package["summary"]["candidate_count"], 1)
        self.assertEqual(len(package["candidate_set"]), 1)
        self.assertEqual(len(package["full_detail_set"]), 1)
        detail = package["full_detail_set"][0]
        self.assertEqual(detail["detail_id"], "detail-0001")
        self.assertIn("drift_risk", detail["risk_flags"])
        self.assertEqual(detail["judgment"]["state"], "needs_user_confirmation")
        self.assertTrue(detail["judgment"]["evidence"])
        self.assertGreaterEqual(len(package["review_focus_set"]), 1)
        self.assertEqual(package["review_focus_set"][0]["detail_ref"], "detail-0001")
        self.assertIn("detail-0001", package["drift_trace_set"][0]["detail_ref"])

    def test_surfaces_unknown_domain_as_taxonomy_candidate(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "agent-runtime-method.md").write_text(
            """---
layer: ops
domain: agent-runtime
ops_area: agent-governance
canonical_object: agent-runtime
artifact_type: method
---

# Agent Runtime
""",
            encoding="utf-8",
        )

        package = build_adjudication_package(self.tmpdir)

        self.assertEqual(
            package["taxonomy_candidate_set"],
            [
                {
                    "field": "domain",
                    "value": "agent-runtime",
                    "detail_refs": ["detail-0001"],
                    "reason": "value absent from wiki/config/frontmatter-taxonomy.yaml",
                }
            ],
        )
        detail = package["full_detail_set"][0]
        self.assertIn("taxonomy_candidate", detail["risk_flags"])
        self.assertFalse(detail["safe_to_apply_frontmatter"])

    def test_excludes_generated_review_and_treatment_artifacts_from_candidates(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "ordinary-runtime-note.md").write_text(
            """# Ordinary Runtime Note

This ordinary wiki runtime note remains reviewable.
""",
            encoding="utf-8",
        )
        doctor_dir = self.tmpdir / "wiki" / "ops" / "wiki-doctor-runs"
        decision_dir = self.tmpdir / "wiki" / "ops" / "wiki-review-decisions"
        treatment_dir = self.tmpdir / "wiki" / "ops" / "wiki-treatment-runs"
        doctor_dir.mkdir(parents=True)
        decision_dir.mkdir(parents=True)
        treatment_dir.mkdir(parents=True)
        (doctor_dir / "2026-05-14-010203-review.md").write_text(
            """# wiki-doctor Review Record

This generated diagnosis record mentions wiki runtime drift and governance.
""",
            encoding="utf-8",
        )
        (decision_dir / "2026-05-15-010203-review-decisions.md").write_text(
            """# wiki-review-decisions Draft Record

This generated decision sheet mentions treatment candidates and OpenSpec.
""",
            encoding="utf-8",
        )
        (treatment_dir / "2026-05-15-010203-treatment.md").write_text(
            """# wiki-treatment Record

This generated treatment record mentions applied frontmatter.
""",
            encoding="utf-8",
        )

        package = build_adjudication_package(self.tmpdir)

        paths = [detail["path"] for detail in package["full_detail_set"]]
        self.assertEqual(package["summary"]["candidate_count"], 1)
        self.assertEqual(paths, ["wiki/ops/ordinary-runtime-note.md"])
        self.assertEqual(
            [entry["path"] for entry in package["candidate_set"]],
            ["wiki/ops/ordinary-runtime-note.md"],
        )

    def test_eval_fails_when_risky_detail_has_no_evidence(self) -> None:
        package = {
            "full_detail_set": [
                {
                    "detail_id": "detail-0001",
                    "path": "wiki/ops/drift-retro.md",
                    "risk_flags": ["drift_risk"],
                    "judgment": {"state": "needs_user_confirmation", "evidence": []},
                    "safe_to_apply_frontmatter": False,
                }
            ],
            "taxonomy_candidate_set": [],
            "review_focus_set": [{"detail_ref": "detail-0001"}],
        }

        result = evaluate_adjudication_package(package)

        self.assertFalse(result["passed"])
        self.assertIn("detail-0001: judgment missing evidence", result["errors"])

    def test_eval_fails_when_unresolved_risk_is_marked_safe_to_apply(self) -> None:
        package = {
            "full_detail_set": [
                {
                    "detail_id": "detail-0001",
                    "path": "wiki/ops/domain-drift.md",
                    "risk_flags": ["taxonomy_candidate"],
                    "judgment": {"state": "needs_user_confirmation", "evidence": ["domain absent"]},
                    "safe_to_apply_frontmatter": True,
                }
            ],
            "taxonomy_candidate_set": [
                {"field": "domain", "value": "agent-runtime", "detail_refs": ["detail-0001"]}
            ],
            "review_focus_set": [{"detail_ref": "detail-0001"}],
        }

        result = evaluate_adjudication_package(package)

        self.assertFalse(result["passed"])
        self.assertIn(
            "detail-0001: safe_to_apply_frontmatter true with unresolved risks",
            result["errors"],
        )

    def test_renders_wiki_doctor_review_record_markdown(self) -> None:
        from scripts.wiki_doctor_review_records import render_review_record_markdown

        package = {
            "generated_at": "2026-05-14T12:46:28+00:00",
            "summary": {
                "candidate_count": 2,
                "full_detail_count": 2,
                "review_focus_count": 1,
                "taxonomy_candidate_count": 1,
                "drift_trace_count": 1,
            },
            "taxonomy_candidate_set": [
                {
                    "field": "domain",
                    "value": "agent-runtime",
                    "detail_refs": ["detail-0001"],
                    "reason": "value absent from wiki/config/frontmatter-taxonomy.yaml",
                }
            ],
            "drift_trace_set": [
                {
                    "detail_ref": "detail-0002",
                    "path": "wiki/ops/runtime-drift-retro.md",
                    "risk_flags": ["drift_risk"],
                    "reason": "governance or drift signal requires explicit review",
                }
            ],
            "eval_result": {
                "passed": False,
                "errors": ["detail-0001: judgment missing evidence"],
                "warnings": ["detail-0002: relation candidate needs reviewed evidence"],
            },
            "proof_boundary_notes": [
                "Content adjudication is deterministic review output only.",
                "It does not write frontmatter.",
            ],
        }

        markdown = render_review_record_markdown(package, scan_root=self.tmpdir, limit=50)

        self.assertIn("# wiki-doctor Review Record", markdown)
        self.assertIn("- Generated at: 2026-05-14T12:46:28+00:00", markdown)
        self.assertIn(f"- Scan root: `{self.tmpdir}`", markdown)
        self.assertIn("- Detail limit: 50", markdown)
        self.assertIn("- candidate_count: 2", markdown)
        self.assertIn("- eval_passed: False", markdown)
        self.assertIn("- eval_error_count: 1", markdown)
        self.assertIn("- eval_warning_count: 1", markdown)
        self.assertIn("## Taxonomy Candidates", markdown)
        self.assertIn("domain=`agent-runtime`", markdown)
        self.assertIn("## Drift Traces", markdown)
        self.assertIn("runtime-drift-retro.md", markdown)
        self.assertIn("## Eval Errors", markdown)
        self.assertIn("judgment missing evidence", markdown)
        self.assertIn("## Eval Warnings", markdown)
        self.assertIn("relation candidate needs reviewed evidence", markdown)
        self.assertIn("## Proof Boundary", markdown)
        self.assertIn("This record is diagnosis only.", markdown)
        self.assertIn("## Next Review Actions", markdown)
        self.assertIn("Human review:", markdown)
        self.assertIn("Discard:", markdown)
        self.assertIn("OpenSpec candidate:", markdown)
        self.assertIn("Later explicit repair:", markdown)

    def test_writes_review_record_without_overwriting_existing_file(self) -> None:
        from scripts.wiki_doctor_review_records import write_review_record

        package = {
            "summary": {},
            "taxonomy_candidate_set": [],
            "drift_trace_set": [],
            "eval_result": {"passed": True, "errors": [], "warnings": []},
            "proof_boundary_notes": [],
        }
        output_dir = self.tmpdir / "records"

        first = write_review_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T01:02:03+00:00",
        )
        second = write_review_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T01:02:03+00:00",
        )

        self.assertEqual(first.name, "2026-05-14-010203-review.md")
        self.assertEqual(second.name, "2026-05-14-010203-review-2.md")
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())
        self.assertIn("# wiki-doctor Review Record", first.read_text(encoding="utf-8"))

    def test_cli_writes_review_record_only_when_explicitly_requested(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        record_dir = self.tmpdir / "review-records"

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_content_adjudication.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "0",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        default_payload = json.loads(default_result.stdout)

        self.assertNotIn("review_record_path", default_payload)
        self.assertFalse(record_dir.exists())

        write_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_content_adjudication.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "0",
                "--write-review-record",
                "--review-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        write_payload = json.loads(write_result.stdout)

        self.assertIn("review_record_path", write_payload)
        record_path = Path(write_payload["review_record_path"])
        self.assertEqual(record_path.parent, record_dir.resolve())
        self.assertTrue(record_path.exists())
        self.assertIn("This record is diagnosis only.", record_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
