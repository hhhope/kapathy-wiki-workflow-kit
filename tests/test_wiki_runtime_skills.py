import re
import unittest
from pathlib import Path


SKILL_SOURCE_ROOT = Path(".codex/skills")
USER_SKILL_ROOT = Path.home() / ".codex" / "skills"
PLUGIN_COMMANDS_FRAGMENT = "plugins/report-wiki-portfolio" + "/commands"
COMMANDS_WIKI_FRAGMENT = "commands/" + "wiki-"
WIKI_SLASH_FRAGMENT = "/" + "wiki:"

WIKI_SKILLS = {
    "wiki-status": ("scripts/build_wiki_status.py", "wiki/status/wiki-status.md"),
    "wiki-manifest": ("scripts/build_wiki_status.py", "wiki/status/manifest.json"),
    "wiki-inbox": ("scripts/build_wiki_status.py", "inbox/"),
    "wiki-query": (
        "scripts/build_wiki_status.py",
        "scripts/derive_runtime_auto_routing.py",
        "scripts/build_runtime_context_injection.py",
        "rg -n",
    ),
    "wiki-explore": ("wiki-query", "Evidence surface", "Enoughness judgment"),
    "wiki-graph": (
        "scripts/extract_wiki_graph.py",
        "scripts/analyze_wiki_relations.py",
        "scripts/summarize_wiki_graph.py",
        "MOC candidates",
    ),
    "wiki-scorecard": (
        "scripts/score_wiki_semantics.py",
        "scripts/derive_wiki_utilization.py",
        "scripts/summarize_wiki_scorecard.py",
    ),
    "wiki-route": (
        "scripts/resolve_runtime_context_sources.py",
        "scripts/derive_runtime_auto_routing.py",
    ),
    "wiki-context": (
        "scripts/build_wiki_runtime_context.py",
        "scripts/build_runtime_context_injection.py",
    ),
    "wiki-apply": (
        "scripts/build_runtime_context_injection.py",
        "scripts/derive_self_directed_execution.py",
        "scripts/build_wiki_content_enrichment.py",
        "scripts/build_wiki_content_adjudication.py",
        "scripts/build_wiki_moc_projection.py",
        "scripts/wiki_gate_precheck.py",
        "page-frontmatter-fix",
    ),
    "wiki-doctor": (
        "scripts/build_wiki_content_adjudication.py",
        "full_detail_set",
        "review_focus_set",
        "taxonomy_candidate_set",
        "drift_trace_set",
        "eval_result",
        "review-only",
        "--write-review-record",
        "wiki/ops/wiki-doctor-runs",
    ),
    "wiki-review-decisions": (
        "scripts/build_wiki_review_decisions.py",
        "accepted_candidates",
        "rejected_candidates",
        "deferred_items",
        "treatment_candidates",
        "surgery_candidates",
        "openspec_required",
        "--write-decision-record",
        "wiki/ops/wiki-review-decisions",
        "draft review routing",
    ),
    "wiki-queue": ("scripts/build_wiki_change_queue_preview.py",),
    "wiki-react": (
        "wiki_content_enrichment",
        "wiki_content_adjudication",
        "frontmatter_enrichment_preview_only",
        "adjudication_review_only",
        "obsidian_graph_projection",
        "preview_moc_projection",
        "explicit_moc_generator_required",
    ),
}


class WikiRuntimeSkillsTest(unittest.TestCase):
    def test_wiki_runtime_skill_sources_exist_with_plain_wiki_names(self) -> None:
        for skill_name, required_markers in WIKI_SKILLS.items():
            with self.subTest(skill=skill_name):
                skill_path = SKILL_SOURCE_ROOT / skill_name / "SKILL.md"
                self.assertTrue(skill_path.exists(), skill_path)
                content = skill_path.read_text(encoding="utf-8")
                self.assertRegex(content, rf"(?m)^name: {re.escape(skill_name)}$")
                for marker in required_markers:
                    self.assertIn(marker, content)
                self.assertNotIn("Command contract:", content)
                self.assertNotIn(PLUGIN_COMMANDS_FRAGMENT, content)
                self.assertNotIn(WIKI_SLASH_FRAGMENT, content)
                self.assertNotIn("name: report-wiki-portfolio:", content)

    def test_wiki_runtime_skills_preserve_boundaries(self) -> None:
        for skill_name in WIKI_SKILLS:
            with self.subTest(skill=skill_name):
                content = (
                    SKILL_SOURCE_ROOT / skill_name / "SKILL.md"
                ).read_text(encoding="utf-8").lower()
                self.assertIn("do not create, modify, archive, or queue openspec changes", content)
                self.assertIn("do not mark openspec tasks complete", content)
                self.assertIn("do not execute queued work", content)

    def test_readme_documents_wiki_skill_surface_not_custom_slash_runtime(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("$wiki-status", readme)
        self.assertIn("$wiki-query", readme)
        self.assertIn(".codex/skills/wiki-status/SKILL.md", readme)
        self.assertNotIn("install those directories into", readme)
        self.assertIn("Do not install this repo's `wiki-*`", readme)
        self.assertNotIn("This repo also ships a repo-local Codex plugin", readme)

    def test_active_runtime_docs_do_not_reference_slash_command_surface(self) -> None:
        active_paths = [
            Path("README.md"),
            Path("openspec/specs/wiki-runtime-skill-surface/spec.md"),
            Path("openspec/specs/wiki-status-skill/spec.md"),
        ]
        active_paths.extend(sorted(Path(".codex/skills").glob("wiki-*/SKILL.md")))
        for path in active_paths:
            with self.subTest(path=path.as_posix()):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn(PLUGIN_COMMANDS_FRAGMENT, text)
                self.assertNotIn(COMMANDS_WIKI_FRAGMENT, text)
                self.assertNotIn(WIKI_SLASH_FRAGMENT, text)

    def test_user_scope_does_not_duplicate_repo_wiki_runtime_skills(self) -> None:
        for skill_name in WIKI_SKILLS:
            with self.subTest(skill=skill_name):
                self.assertFalse(
                    (USER_SKILL_ROOT / skill_name / "SKILL.md").exists(),
                    USER_SKILL_ROOT / skill_name / "SKILL.md",
                )


if __name__ == "__main__":
    unittest.main()
