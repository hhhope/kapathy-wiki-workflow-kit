import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.dialogue_agent_drift import build_dialogue_drift_report, classify_dialogue_drift_page


class DialogueAgentDriftTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="dialogue-drift-test-"))
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _write_ops_page(self, name: str, body: str, frontmatter: str = "") -> Path:
        path = self.tmpdir / "wiki" / "ops" / name
        text = body
        if frontmatter:
            text = f"---\n{frontmatter.strip()}\n---\n\n{body}"
        path.write_text(text, encoding="utf-8")
        return path

    def test_classifies_dialogue_disagreement_from_rejected_framing(self) -> None:
        path = self._write_ops_page(
            "visual-disagreement-retro.md",
            """# Visual Disagreement Retro

## Rejected Framing

The user rejected the framing that this was just an image export issue.

## Corrected Framing

The live conversation was calibrating who owns the output mode decision.
""",
        )

        item = classify_dialogue_drift_page(self.tmpdir, path)

        self.assertEqual(item["proposed_bucket"], "dialogue-disagreement")
        self.assertEqual(item["recommended_next_action"], "defer-cleanup")
        self.assertIn("Rejected Framing", item["evidence"])

    def test_classifies_agent_drift_from_route_failure(self) -> None:
        path = self._write_ops_page(
            "visual-output-routing-drift-explore.md",
            """# Visual Output Routing Drift

The agent followed the wrong route and selected H5/SVG after the user asked
for image model quality. This records an output-mode boundary failure.
""",
            """
canonical_object: visual-output-routing-drift
artifact_type: intake
status: exploring
""",
        )

        item = classify_dialogue_drift_page(self.tmpdir, path)

        self.assertEqual(item["proposed_bucket"], "agent-drift")
        self.assertEqual(item["recommended_next_action"], "openspec-candidate")
        self.assertIn("wrong route", item["evidence"])

    def test_classifies_reanchor_trace_from_continuation_stop(self) -> None:
        path = self._write_ops_page(
            "live-conversation-reanchor-gate-retro.md",
            """# Live Conversation Reanchor Gate

When the work drifts away from the last confirmed requirement, continuation
must stop and re-anchor before implementation resumes.
""",
            """
canonical_object: live-conversation-reanchor-gate
artifact_type: retro
""",
        )

        item = classify_dialogue_drift_page(self.tmpdir, path)

        self.assertEqual(item["proposed_bucket"], "reanchor-trace")
        self.assertEqual(item["recommended_next_action"], "no-op")
        self.assertIn("re-anchor", item["evidence"])

    def test_classifies_supporting_examples_without_treating_them_as_incidents(self) -> None:
        path = self._write_ops_page(
            "sample-disagreement-retro.md",
            """# Disagreement Retro Sample

This sample shows how rejected framing and correction pressure should be
recorded.
""",
            """
artifact_type: sample
status: draft
""",
        )

        item = classify_dialogue_drift_page(self.tmpdir, path)

        self.assertEqual(item["proposed_bucket"], "supporting-example")
        self.assertEqual(item["recommended_next_action"], "no-op")
        self.assertIn("sample", item["evidence"])

    def test_rejects_project_management_and_learning_drift_mentions(self) -> None:
        weekly = self._write_ops_page(
            "nirvana-weekly-intake.md",
            """# Nirvana Weekly Intake

This weekly project update tracks milestone drift, current progress, owner,
risks, and next actions.
""",
            """
domain: nirvana-project
artifact_type: intake
""",
        )
        learning = self._write_ops_page(
            "agent-harness-learning.md",
            """# Agent Harness Reading Notes

These reading notes mention drift as a general lesson from a source article.
""",
            """
artifact_type: reading-notes
""",
        )

        weekly_item = classify_dialogue_drift_page(self.tmpdir, weekly)
        learning_item = classify_dialogue_drift_page(self.tmpdir, learning)

        self.assertEqual(weekly_item["proposed_bucket"], "not-dialogue-drift")
        self.assertEqual(weekly_item["recommended_next_action"], "defer-cleanup")
        self.assertIn("project-management", weekly_item["evidence"])
        self.assertEqual(learning_item["proposed_bucket"], "not-dialogue-drift")
        self.assertIn("learning", learning_item["evidence"])

    def test_report_is_review_only_and_summarizes_buckets(self) -> None:
        self._write_ops_page(
            "sample-disagreement-retro.md",
            "# Sample\n\nThis sample shows disagreement handling.",
            "artifact_type: sample",
        )
        self._write_ops_page(
            "route-drift.md",
            "# Route Drift\n\nThe agent followed the wrong route.",
        )

        report = build_dialogue_drift_report(self.tmpdir)

        self.assertEqual(report["mode"], "dialogue_agent_drift_trace_review")
        self.assertEqual(report["summary"]["supporting-example"], 1)
        self.assertEqual(report["summary"]["agent-drift"], 1)
        self.assertIn("does not write frontmatter", " ".join(report["proof_boundary_notes"]))

    def test_default_scan_skips_generated_medical_runtime_records(self) -> None:
        runtime_dir = self.tmpdir / "wiki" / "ops" / "wiki-treatment-runs"
        runtime_dir.mkdir(parents=True)
        generated = runtime_dir / "generated-treatment.md"
        generated.write_text(
            "# Generated Treatment\n\nThis replay sample records disagreement evidence.",
            encoding="utf-8",
        )

        report = build_dialogue_drift_report(self.tmpdir)

        self.assertEqual(report["items"], [])

    def test_current_medical_loop_candidates_replay_expected_buckets(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        candidates = [
            {
                "detail_ref": "detail-0097",
                "path": "wiki/ops/sample-disagreement-retro.md",
            },
            {
                "detail_ref": "detail-0108",
                "path": "wiki/ops/visual-output-routing-drift-explore-2026-05-11.md",
            },
            {
                "detail_ref": "detail-0081",
                "path": "wiki/ops/nirvana-weekly-intake-2026-04-13.md",
            },
        ]

        report = build_dialogue_drift_report(repo_root, candidates=candidates)
        by_ref = {item["detail_ref"]: item for item in report["items"]}

        self.assertEqual(by_ref["detail-0097"]["proposed_bucket"], "supporting-example")
        self.assertEqual(by_ref["detail-0108"]["proposed_bucket"], "agent-drift")
        self.assertEqual(by_ref["detail-0081"]["proposed_bucket"], "not-dialogue-drift")

    def test_cli_emits_json_without_writing_pages(self) -> None:
        path = self._write_ops_page(
            "route-drift.md",
            "# Route Drift\n\nThe agent followed the wrong route.",
        )
        before = path.read_text(encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve().parents[1] / "scripts" / "build_dialogue_agent_drift.py"),
                "--root",
                str(self.tmpdir),
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["summary"]["agent-drift"], 1)
        self.assertEqual(path.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
