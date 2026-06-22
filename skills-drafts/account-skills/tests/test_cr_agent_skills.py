import unittest
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def read_skill(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


class CRAgentSkillPackageTest(unittest.TestCase):
    def test_cr_agent_entry_contract(self):
        text = read_skill("cr-agent")
        for marker in [
            "single normal user-facing entry point",
            "Intent",
            "CR Case",
            "CR Type",
            "Range",
            "Allowed Action",
            "Blocked Action",
            "Next Action",
            "Evidence",
            "Do not treat feature-branch CR as release CR",
        ]:
            self.assertIn(marker, text)

    def test_cr_agent_persists_reports_when_repo_has_cr_directory(self):
        text = read_skill("cr-agent")
        for marker in [
            "Persisted CR Output",
            "repo has a `CR/` directory",
            "write the CR report into that directory",
            "Blocked Persistence",
        ]:
            self.assertIn(marker, text)

    def test_worker_skill_package_exists(self):
        for name in [
            "cr-intake",
            "cr-branch-governance",
            "cr-diff",
            "cr-scope",
            "cr-technical-review",
            "cr-evidence",
            "cr-issues",
            "cr-gate",
            "cr-report",
            "cr-replay",
        ]:
            self.assertTrue((SKILLS / name / "SKILL.md").exists(), name)

    def test_gate_and_issues_contracts_are_explicit(self):
        issues = read_skill("cr-issues")
        for marker in ["CR-ID", "source_worker", "severity", "blocking", "status", "related_commits"]:
            self.assertIn(marker, issues)

        gate = read_skill("cr-gate")
        for marker in [
            "any open blocking issue",
            "wrong baseline",
            "feature-branch CR presented as release gate",
            "mainline direct commit without approval",
            "production commit not covered by UAT",
            "DDL or data repair without rollback",
            "missing quality score rationale",
            "logs, metrics, traces, dashboards",
            "real-time alerts, report/batch alerts",
            "owner, threshold, routing, and runbook",
            "unmaintainable change boundary",
        ]:
            self.assertIn(marker, gate)

    def test_technical_review_keeps_technical_cr_primary(self):
        text = read_skill("cr-technical-review")
        for marker in [
            "main technical reviewer path",
            "cr-correctness",
            "cr-robustness",
            "cr-security",
            "cr-architecture",
            "cr-data",
            "cr-integration",
            "cr-observability",
            "cr-testability",
            "cr-tech-debt",
            "logs, metrics, traces, dashboards",
            "real-time alerts, report/batch alerts",
            "SLI/SLO or business KPI signals",
            "change size, ownership, modularity, coupling",
            "duplication, dead code, complexity",
            "Sonar-style code smells",
            "security and business-risk findings",
            "Do not stop at only the first blocking issue",
        ]:
            self.assertIn(marker, text)

    def test_report_requires_issue_ledger_and_todo_persistence(self):
        text = read_skill("cr-report")
        for marker in [
            "Persisted CR Output",
            "technical quality scorecard",
            "CR execution audit showing which CR workers/skills produced evidence",
            "TODO ledger",
            "Report Path",
            "references/chinese-cr-report-template.md",
            "style evidence, not as",
            "runtime dependency",
            "最终结论（是否可发布）",
            "评分卡（100分）",
            "技术质量评分",
            "CR 执行审计评分",
            "CR 执行审计",
            "Scoring rationale is mandatory",
            "每个技术质量分项都必须说明扣分依据",
            "logs / metrics / traces",
            "实时告警 / 报表或批处理告警",
            "复杂度 / 重复 / 死代码 / 耦合",
            "技术审查结果",
            "TODO 跟踪",
            "same project/date report already exists",
            "overwrite or update that same",
            "idempotent by TODO-ID",
        ]:
            self.assertIn(marker, text)
        template = SKILLS / "cr-report" / "references" / "chinese-cr-report-template.md"
        self.assertTrue(template.exists())
        template_text = template.read_text(encoding="utf-8")
        for marker in ["技术质量评分", "CR 执行审计评分", "| cr-report | Y | Y |"]:
            self.assertIn(marker, template_text)

    def test_evidence_tracks_static_analysis_and_runtime_gaps(self):
        text = read_skill("cr-evidence")
        for marker in [
            "Sonar or static-analysis status",
            "security scan evidence",
            "raw upstream callback or API samples",
        ]:
            self.assertIn(marker, text)

    def test_existing_skills_declare_cr_agent_provider_roles(self):
        release = read_skill("release-diff-cr")
        self.assertIn("first `cr-diff` provider", release)
        self.assertIn("Blocking CR scan issues are gate inputs", release)

        code_review = read_skill("code-review")
        self.assertIn("first `cr-technical-review`", code_review)
        self.assertIn("does not own CR lifecycle state", code_review)

    def test_cr_replay_fixture_validates(self):
        import subprocess

        script = SKILLS / "cr-agent" / "scripts" / "eval_cr_replay.py"
        fixture = SKILLS / "cr-agent" / "replay" / "mandao-customer-keytype.json"
        proc = subprocess.run(["python3", str(script), str(fixture)], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        self.assertIn("validated 1 replay fixture", proc.stdout)

    def test_cr_replay_rejects_weak_fixture(self):
        import subprocess

        script = SKILLS / "cr-agent" / "scripts" / "eval_cr_replay.py"
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "weak.json"
            fixture.write_text(
                """
{
  "id": "weak",
  "input_situation": "shape is incomplete",
  "triggered_workers": "cr-gate",
  "expected_issues": [],
  "expected_gate": "blocked",
  "proof_boundary": "none",
  "residual_risk": "none"
}
""".strip(),
                encoding="utf-8",
            )
            proc = subprocess.run(["python3", str(script), str(fixture)], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 1, proc.stderr + proc.stdout)
        self.assertIn("triggered_workers must be a non-empty list", proc.stderr)
        self.assertIn("expected_issues must be a non-empty list", proc.stderr)

    def test_cr_replay_reports_missing_fixture_without_traceback(self):
        import subprocess

        script = SKILLS / "cr-agent" / "scripts" / "eval_cr_replay.py"
        fixture = SKILLS / "cr-agent" / "replay" / "missing.json"
        proc = subprocess.run(["python3", str(script), str(fixture)], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 1, proc.stderr + proc.stdout)
        self.assertIn("cannot read fixture", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
