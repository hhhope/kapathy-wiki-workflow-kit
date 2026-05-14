import json
import tempfile
import unittest
from pathlib import Path

from scripts.eval_wiki_decision_trace import evaluate_trace_cases, load_cases, load_traces


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "wiki/evals/wiki-react-trace-cases.json"


class WikiDecisionTraceEvalTest(unittest.TestCase):
    def test_default_cases_cover_core_runtime_intents(self) -> None:
        cases = load_cases(CASES)
        case_ids = {case["id"] for case in cases}

        self.assertIn("status-inspection", case_ids)
        self.assertIn("query-context", case_ids)
        self.assertIn("frontmatter-page-repair", case_ids)
        self.assertIn("article-learning", case_ids)
        self.assertIn("article-weight-temperature", case_ids)
        self.assertIn("relation-exploration", case_ids)
        self.assertIn("execution-request", case_ids)
        self.assertIn("promotion-to-adr", case_ids)

    def test_eval_accepts_agent_trace_without_python_intent_classification(self) -> None:
        cases = [
            {
                "id": "article-weight-temperature",
                "allowed_intents": ["exploratory_scoring", "article_learning"],
                "required_actions_all": ["classify_intent"],
                "required_actions_any": ["read_scorecard_context", "read_relation_context"],
                "required_boundary": "candidate_judgment_only",
                "forbidden_actions": ["frontmatter_repair", "taxonomy_mutation", "automatic_promotion"],
                "requires_exploratory_judgments": True,
            }
        ]
        traces = [
            {
                "case_id": "article-weight-temperature",
                "input": "这篇文章权重温度怎么看",
                "intent": "exploratory_scoring",
                "evidence_object": "article",
                "risk_level": "medium",
                "actions": ["classify_intent", "read_scorecard_context"],
                "observations": {
                    "static_facts": [],
                    "exploratory_judgments": ["article_weight_candidate"],
                },
                "decision": "candidate_judgment_only",
                "boundary": "candidate_judgment_only",
                "forbidden_actions_checked": [
                    "frontmatter_repair",
                    "taxonomy_mutation",
                    "automatic_promotion",
                ],
            }
        ]

        result = evaluate_trace_cases(cases, traces)

        self.assertTrue(result.passed, result.errors)

    def test_eval_rejects_forbidden_action_even_when_intent_is_allowed(self) -> None:
        cases = [
            {
                "id": "article-weight-temperature",
                "allowed_intents": ["exploratory_scoring", "article_learning"],
                "required_actions_all": ["classify_intent"],
                "required_actions_any": ["read_scorecard_context"],
                "required_boundary": "candidate_judgment_only",
                "forbidden_actions": ["frontmatter_repair", "automatic_promotion"],
                "requires_exploratory_judgments": True,
            }
        ]
        traces = [
            {
                "case_id": "article-weight-temperature",
                "input": "这篇文章权重温度怎么看",
                "intent": "article_learning",
                "evidence_object": "article",
                "risk_level": "medium",
                "actions": ["classify_intent", "read_scorecard_context", "frontmatter_repair"],
                "observations": {
                    "static_facts": [],
                    "exploratory_judgments": ["temperature_candidate"],
                },
                "decision": "candidate_judgment_only",
                "boundary": "candidate_judgment_only",
                "forbidden_actions_checked": ["automatic_promotion"],
            }
        ]

        result = evaluate_trace_cases(cases, traces)

        self.assertFalse(result.passed)
        self.assertTrue(any("forbidden action" in error for error in result.errors))
        self.assertTrue(any("forbidden_actions_checked" in error for error in result.errors))

    def test_load_traces_accepts_json_object_with_traces_key(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            trace_path = Path(temp_dir) / "traces.json"
            trace_path.write_text(
                json.dumps({"traces": [{"case_id": "status-inspection"}]}),
                encoding="utf-8",
            )

            traces = load_traces(trace_path)

        self.assertEqual(traces, [{"case_id": "status-inspection"}])


class WikiDecisionTraceSkillReferenceTest(unittest.TestCase):
    def test_high_risk_wiki_skills_reference_decision_trace_contract(self) -> None:
        required = [
            ".codex/skills/wiki-query/SKILL.md",
            ".codex/skills/wiki-apply/SKILL.md",
            ".codex/skills/wiki-explore/SKILL.md",
            ".codex/skills/wiki-scorecard/SKILL.md",
        ]
        for rel_path in required:
            with self.subTest(path=rel_path):
                text = (ROOT / rel_path).read_text(encoding="utf-8")
                self.assertIn("wiki/ops/wiki-react-decision-trace-runtime.md", text)
                self.assertIn("decision_trace", text)


if __name__ == "__main__":
    unittest.main()
