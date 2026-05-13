from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RULE = ROOT / "rules/go/engineering-security.md"
AGENTS = ROOT / "AGENTS.md"
LEARNING = ROOT / "wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md"


class GoEngineeringSecurityRulesTest(unittest.TestCase):
    def test_go_rule_exists_with_user_confirmed_stack(self) -> None:
        content = RULE.read_text(encoding="utf-8")

        for phrase in [
            "go 1.25.1",
            "github.com/gin-gonic/gin",
            "gin-contrib",
            "go-playground/validator",
            "GORM",
            "go-redis",
        ]:
            self.assertIn(phrase, content)

    def test_go_tool_fix_is_migration_scoped_not_daily_lint(self) -> None:
        content = RULE.read_text(encoding="utf-8")

        self.assertIn("go tool fix", content)
        self.assertIn("not a daily formatter, linter, or cleanup command", content)
        self.assertIn("go tool fix -help", content)
        self.assertIn("go tool fix -diff", content)
        self.assertIn("gofmt", content)
        self.assertIn("goimports", content)

    def test_agents_routes_go_work_to_compact_rule_not_full_wordlist(self) -> None:
        content = AGENTS.read_text(encoding="utf-8")

        self.assertIn("rules/go/engineering-security.md", content)
        self.assertIn(
            "Go 1.25.1 + Gin + gin-contrib + validator + GORM + go-redis",
            content,
        )
        self.assertLessEqual(content.count("go tool fix"), 2)

    def test_source_learning_is_compressed_and_rejects_framework_ranking_as_rule(self) -> None:
        content = LEARNING.read_text(encoding="utf-8")

        self.assertIn("does not copy article bodies", content)
        self.assertIn("Rejected as hard rule; user-confirmed stack wins", content)
        self.assertIn("go1.22.2", content)
        self.assertIn("go 1.25.1", content)
        self.assertIn("Source Set", content)


if __name__ == "__main__":
    unittest.main()
