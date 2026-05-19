import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_moc_projection import (
    apply_moc_plan,
    build_moc_candidates,
    build_moc_health,
    build_moc_plan,
)


class WikiMocProjectionTest(unittest.TestCase):
    CANDIDATE_ID = "relation:wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md:formalizes:wiki-frontmatter-model"

    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-moc-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def sample_graph(self) -> dict:
        return {
            "nodes": [
                {
                    "page_path": "wiki/ops/agent-readable-wiki-frontmatter.md",
                    "canonical_object": "wiki-frontmatter-model",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md",
                    "canonical_object": "wiki-frontmatter-model",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "wiki",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md",
                    "relation_type": "formalizes",
                    "target": "wiki-frontmatter-model",
                }
            ],
        }

    def valid_temperature_review(self) -> dict:
        return {
            "candidate_id": self.CANDIDATE_ID,
            "temperature": 91,
            "moc_admission": "admit",
            "rationale": "ADR formalizes the runtime model.",
            "reviewer": "test",
            "reviewed_at": "2026-05-19",
        }

    def test_builds_domain_and_object_candidates_by_default(self) -> None:
        candidates = build_moc_candidates(self.sample_graph())
        paths = {candidate.path for candidate in candidates}

        self.assertIn("wiki/moc/domain-wiki.md", paths)
        self.assertIn("wiki/moc/object-wiki-frontmatter-model.md", paths)
        self.assertNotIn("wiki/moc/relation-formalizes.md", paths)

    def test_builds_admitted_relation_candidates(self) -> None:
        admission_plan = {
            "admitted_relations": ["formalizes"],
            "counts": {
                "admitted": 1,
                "blocked": 0,
                "needs_review": 0,
                "total": 1,
            },
            "clue_windows": [],
        }
        candidates = build_moc_candidates(
            self.sample_graph(),
            admission_plan=admission_plan,
        )
        paths = {candidate.path for candidate in candidates}

        self.assertIn("wiki/moc/relation-formalizes.md", paths)

    def test_object_preview_groups_pages_by_lifecycle_not_ops_area(self) -> None:
        graph = {
            "nodes": [
                {
                    "page_path": "wiki/ops/karpathy-llm-wiki-reading-notes.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "reading-notes",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "learning-capture",
                },
                {
                    "page_path": "openspec/specs/wiki-runtime-context/spec.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "none",
                },
                {
                    "page_path": "wiki/ops/wiki-runtime-layer-contract.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "wiki-runtime",
                },
                {
                    "page_path": "wiki/ops/wiki-readable-views-validation-harness.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "replay-harness",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "workflow-trace",
                },
            ],
            "edges": [],
        }

        plan = build_moc_plan(self.tmpdir, graph)
        object_entry = next(
            entry
            for entry in plan["entries"]
            if entry["path"] == "wiki/moc/object-llm-wiki.md"
        )
        preview = object_entry["preview"]

        for heading in [
            "## Sources / Learning",
            "## Specification",
            "## Decisions",
            "## Methods / Runtime",
            "## Evidence / Replay",
        ]:
            self.assertIn(heading, preview)

        self.assertNotIn("## learning-capture", preview)
        self.assertNotIn("## workflow-trace", preview)
        self.assertEqual(object_entry["link_count"], 5)

    def test_dry_run_plan_does_not_write_files(self) -> None:
        plan = build_moc_plan(self.tmpdir, self.sample_graph())

        self.assertEqual(plan["summary"]["create_count"], 2)
        self.assertIn("temperature_admission", plan)
        self.assertEqual(plan["temperature_admission"]["admitted_relations"], [])
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())

    def test_cli_accepts_temperature_review_json_without_writing_files(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path.write_text(
            json.dumps(
                {
                    self.CANDIDATE_ID: self.valid_temperature_review()
                }
            ),
            encoding="utf-8",
        )
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            check=True,
            capture_output=True,
            text=True,
            cwd=repo_root,
        )
        output = json.loads(completed.stdout)
        paths = {entry["path"] for entry in output["entries"]}

        self.assertIn("wiki/moc/relation-formalizes.md", paths)
        self.assertEqual(output["temperature_admission"]["admitted_relations"], ["formalizes"])
        self.assertEqual(output["mode"], "dry-run")
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())

    def test_cli_rejects_single_temperature_review_object(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path.write_text(
            json.dumps(
                {
                    "candidate_id": self.CANDIDATE_ID,
                    "temperature": 91,
                    "moc_admission": "admit",
                    "rationale": "ADR formalizes the runtime model.",
                    "reviewer": "test",
                    "reviewed_at": "2026-05-19",
                }
            ),
            encoding="utf-8",
        )
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("--temperature-review", completed.stderr)
        self.assertIn("keyed mapping", completed.stderr)

    def test_cli_rejects_temperature_review_missing_required_field(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path.write_text(
            json.dumps(
                {
                    self.CANDIDATE_ID: {
                        "candidate_id": self.CANDIDATE_ID,
                        "temperature": 91,
                        "moc_admission": "admit",
                        "reviewer": "test",
                        "reviewed_at": "2026-05-19",
                    }
                }
            ),
            encoding="utf-8",
        )
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("--temperature-review", completed.stderr)
        self.assertIn("rationale", completed.stderr)

    def test_cli_rejects_temperature_review_candidate_id_mismatch(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path.write_text(
            json.dumps(
                {
                    self.CANDIDATE_ID: {
                        "candidate_id": "relation:wrong:formalizes:wiki-frontmatter-model",
                        "temperature": 91,
                        "moc_admission": "admit",
                        "rationale": "ADR formalizes the runtime model.",
                        "reviewer": "test",
                        "reviewed_at": "2026-05-19",
                    }
                }
            ),
            encoding="utf-8",
        )
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("--temperature-review", completed.stderr)
        self.assertIn("candidate_id mismatch", completed.stderr)

    def test_cli_rejects_invalid_temperature_review_values(self) -> None:
        cases = [
            ("rationale", "  ", "rationale"),
            ("reviewer", "", "reviewer"),
            ("reviewed_at", {}, "reviewed_at"),
            ("reviewed_at", "not-a-date", "reviewed_at"),
            ("temperature", "91", "temperature"),
            ("temperature", True, "temperature"),
            ("temperature", 101, "temperature"),
            ("moc_admission", "admit_relation", "moc_admission"),
        ]
        repo_root = Path(__file__).resolve().parents[1]

        for field, value, expected_stderr in cases:
            with self.subTest(field=field, value=value):
                graph_path = self.tmpdir / f"graph-{field}-{value!r}.json"
                review_path = self.tmpdir / f"review-{field}-{value!r}.json"
                review = self.valid_temperature_review()
                review[field] = value
                graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
                review_path.write_text(
                    json.dumps({self.CANDIDATE_ID: review}),
                    encoding="utf-8",
                )

                completed = subprocess.run(
                    [
                        sys.executable,
                        "scripts/build_wiki_moc_projection.py",
                        "--root",
                        str(self.tmpdir),
                        "--graph",
                        str(graph_path),
                        "--temperature-review",
                        str(review_path),
                    ],
                    capture_output=True,
                    text=True,
                    cwd=repo_root,
                )

                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("--temperature-review", completed.stderr)
                self.assertIn(expected_stderr, completed.stderr)

    def test_cli_reports_malformed_temperature_review_json(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path.write_text("{", encoding="utf-8")
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("--temperature-review", completed.stderr)

    def test_cli_reports_missing_temperature_review_file(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        review_path = self.tmpdir / "missing-review.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        repo_root = Path(__file__).resolve().parents[1]

        completed = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("--temperature-review", completed.stderr)

    def test_apply_writes_generated_moc_files(self) -> None:
        plan = apply_moc_plan(self.tmpdir, self.sample_graph())
        domain_path = self.tmpdir / "wiki" / "moc" / "domain-wiki.md"

        self.assertEqual(plan["summary"]["create_count"], 2)
        self.assertTrue(domain_path.exists())
        text = domain_path.read_text(encoding="utf-8")
        self.assertIn("<!-- BEGIN GENERATED MOC: domain=wiki -->", text)
        self.assertIn("[[agent-readable-wiki-frontmatter]]", text)

    def test_update_preserves_manual_content_outside_generated_block(self) -> None:
        apply_moc_plan(self.tmpdir, self.sample_graph())
        object_path = self.tmpdir / "wiki" / "moc" / "object-wiki-frontmatter-model.md"
        original = object_path.read_text(encoding="utf-8")
        object_path.write_text(f"Manual note\n\n{original}", encoding="utf-8")

        graph = self.sample_graph()
        graph["nodes"].append(
            {
                "page_path": "openspec/specs/wiki-frontmatter-model/spec.md",
                "canonical_object": "wiki-frontmatter-model",
                "artifact_type": "spec",
                "source_layer": "openspec/specs",
                "domain": "wiki",
            }
        )
        apply_moc_plan(self.tmpdir, graph)

        updated = object_path.read_text(encoding="utf-8")
        self.assertIn("Manual note", updated)
        self.assertIn("[[spec]]", updated)

    def test_health_reports_missing_and_then_passes_after_apply(self) -> None:
        missing = build_moc_health(self.tmpdir, self.sample_graph())
        self.assertEqual(missing["status"], "drift")
        self.assertEqual(missing["summary"]["create_count"], 2)

        apply_moc_plan(self.tmpdir, self.sample_graph())
        clean = build_moc_health(self.tmpdir, self.sample_graph())

        self.assertEqual(clean["status"], "pass")
        self.assertEqual(clean["summary"]["noop_count"], 2)


if __name__ == "__main__":
    unittest.main()
