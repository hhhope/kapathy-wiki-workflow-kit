import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".codex/skills/wiki-review-decisions/SKILL.md"


class WikiReviewDecisionsSkillTest(unittest.TestCase):
    def test_skill_contract_markers_are_present(self) -> None:
        self.assertTrue(SKILL.exists(), "wiki-review-decisions skill must exist")

        text = SKILL.read_text(encoding="utf-8")

        required_markers = [
            "name: wiki-review-decisions",
            "description: Use when",
            "confirming, triaging, or routing `wiki-doctor` findings",
            "scripts/build_wiki_review_decisions.py",
            "python3 scripts/build_wiki_review_decisions.py",
            "--write-decision-record",
            "wiki/ops/wiki-review-decisions/",
            "accepted_candidates",
            "rejected_candidates",
            "deferred_items",
            "treatment_candidates",
            "surgery_candidates",
            "openspec_required",
            "draft review routing",
            "not approval",
            "Do not create, modify, archive, or queue OpenSpec changes.",
            "Do not mark OpenSpec tasks complete.",
            "Do not execute queued work.",
            "Do not write frontmatter.",
            "Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.",
            "Do not write relation fields.",
            "Do not write `wiki/moc` files.",
            "Do not treat draft review decisions as human approval.",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
