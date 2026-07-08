from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".codex" / "skills"
OLD_CHANGE = ROOT / "openspec" / "changes" / "add-requirements-analysis-agent-skill-entry"
OLD_TEST = ROOT / "tests" / "test_requirements_analysis_agent_skill.py"


class ReqAgentSkillSurfaceTest(unittest.TestCase):
    def _skill_text(self, name: str) -> str:
        path = SKILLS_ROOT / name / "SKILL.md"
        self.assertTrue(path.exists(), path)
        return path.read_text(encoding="utf-8")

    def test_req_agent_is_normal_controller_entry(self) -> None:
        text = self._skill_text("req-agent")

        required_markers = [
            "name: req-agent",
            "single normal Codex-facing entry point",
            "Intent",
            "Case",
            "State",
            "Allowed Action",
            "Blocked Action",
            "Next Action",
            "Evidence",
            "scripts/build_requirements_analysis_agent.py",
            "scripts/check_requirements_case.py",
            "scripts/requirements_openspec_draft.py",
            "domain_coverage_gate",
            "detailed_design_gate",
            "current-state material package",
            "business rule position table",
            "system boundary contract table",
            "Do not ask the user to run Python as the normal path.",
        ]
        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_worker_skills_redirect_ordinary_usage_to_req_agent(self) -> None:
        expected_boundaries = {
            "req-intake": [
                "source material",
                "creates or appends to a requirements case",
                "does not decide readiness",
            ],
            "req-scope": [
                "requirements/config/requirements-taxonomy.yaml",
                "candidate_pending",
                "domain coverage obligations",
                "does not mutate taxonomy",
            ],
            "req-stories": [
                "role",
                "want",
                "benefit",
                "domain_refs",
                "context_refs",
                "aggregate_refs",
                "does not write acceptance conclusions",
            ],
            "req-acceptance": [
                "bidirectional",
                "user story",
                "acceptance function",
                "coverage_types",
                "state_change",
                "handoff",
                "failure_path",
                "evidence",
            ],
            "req-handoff": [
                "hard readiness gate",
                "domain_coverage_gate",
                "OpenSpec draft",
                "Do not continue into implementation automatically.",
            ],
        }

        for skill, markers in expected_boundaries.items():
            with self.subTest(skill=skill):
                text = self._skill_text(skill)
                self.assertIn(f"name: {skill}", text)
                self.assertIn("Ordinary use routes through `req-agent`.", text)
                self.assertIn("explicit debug or worker context", text)
                for marker in markers:
                    self.assertIn(marker, text)

    def test_domain_analysis_emits_domain_coverage_obligations(self) -> None:
        text = self._skill_text("req-domain-analysis")

        required_markers = [
            "domain coverage obligations",
            "required/in-scope subdomains",
            "bounded contexts",
            "aggregate roots",
        ]
        for marker in required_markers:
            self.assertIn(marker, text)

    def test_narrow_requirements_analysis_skill_entry_artifacts_are_retired(self) -> None:
        self.assertFalse(OLD_CHANGE.exists(), OLD_CHANGE)
        self.assertFalse(OLD_TEST.exists(), OLD_TEST)


if __name__ == "__main__":
    unittest.main()
