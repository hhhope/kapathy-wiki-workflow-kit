import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / ".codex/skills"


class WikiMedicalLoopSkillsTest(unittest.TestCase):
    def read_skill(self, skill_name: str) -> str:
        path = SKILL_ROOT / skill_name / "SKILL.md"
        self.assertTrue(path.exists(), path)
        return path.read_text(encoding="utf-8")

    def test_user_facing_stage_skills_exist_with_medical_loop_labels(self) -> None:
        required = {
            "wiki-confirm": [
                "name: wiki-confirm",
                "description: Use when",
                "确诊",
                "scripts/build_wiki_review_decisions.py",
                "--write-decision-record",
                "wiki/ops/wiki-review-decisions/",
                "default writes a complete confirmation record",
                "stdout summary",
                "draft routing, not approval",
                "Do not write frontmatter.",
                "Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.",
                "Do not write relation fields.",
                "Do not write `wiki/moc` files.",
            ],
            "wiki-treatment": [
                "name: wiki-treatment",
                "description: Use when",
                "治疗",
                "scripts/build_wiki_treatment.py",
                "--approved-domain",
                "--approved-detail",
                "--apply",
                "defaults to dry-run",
                "explicit human approval",
                "Do not write relation fields.",
                "Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.",
                "Do not write `wiki/moc` files.",
            ],
            "wiki-surgery": [
                "name: wiki-surgery",
                "description: Use when",
                "手术",
                "scripts/build_wiki_surgery.py",
                "--write-surgery-record",
                "plan-only",
                "relation_weak_evidence",
                "drift_risk",
                "openspec_required",
                "Do not write frontmatter.",
                "Do not write relation fields.",
                "Do not write `wiki/moc` files.",
                "Do not create, modify, archive, or queue OpenSpec changes.",
            ],
            "wiki-recovery": [
                "name: wiki-recovery",
                "description: Use when",
                "复查",
                "scripts/build_wiki_recovery.py",
                "--write-recovery-record",
                "blocked_by_recovery_findings",
                "archive-ready",
                "does not apply treatment or surgery",
                "Do not write frontmatter.",
                "Do not write relation fields.",
                "Do not write `wiki/moc` files.",
            ],
        }

        for skill_name, markers in required.items():
            with self.subTest(skill=skill_name):
                text = self.read_skill(skill_name)
                for marker in markers:
                    self.assertIn(marker, text)

    def test_wiki_doctor_exposes_next_stage_skill_sequence(self) -> None:
        text = self.read_skill("wiki-doctor")

        required_markers = [
            "wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery",
            "诊断",
            "确诊",
            "default writes a complete diagnosis record",
            "stdout summary",
            "治疗",
            "手术",
            "复查",
            "Use `wiki-confirm`",
            "Use `wiki-treatment`",
            "Use `wiki-surgery`",
            "Use `wiki-recovery`",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_wiki_review_decisions_is_legacy_alias_for_confirm(self) -> None:
        text = self.read_skill("wiki-review-decisions")

        required_markers = [
            "legacy compatibility alias",
            "Prefer `wiki-confirm`",
            "name: wiki-review-decisions",
            "scripts/build_wiki_review_decisions.py",
            "Do not write frontmatter.",
            "Do not treat draft review decisions as human approval.",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
