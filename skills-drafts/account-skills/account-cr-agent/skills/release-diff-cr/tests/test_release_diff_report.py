import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "release_diff_report.py"


def run(cmd, cwd, check=True):
    env = os.environ.copy()
    env.update(
        {
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_COUNT": "2",
            "GIT_CONFIG_KEY_0": "commit.gpgsign",
            "GIT_CONFIG_VALUE_0": "false",
            "GIT_CONFIG_KEY_1": "core.hooksPath",
            "GIT_CONFIG_VALUE_1": os.devnull,
        }
    )
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, env=env)
    if check and proc.returncode != 0:
        raise AssertionError(proc.stderr or proc.stdout)
    return proc


class ReleaseDiffGateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="release-diff-gate-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        run(["git", "init", "-b", "master"], self.tmp)
        run(["git", "config", "user.email", "review@example.test"], self.tmp)
        run(["git", "config", "user.name", "Review Bot"], self.tmp)
        (self.tmp / "service.java").write_text("class Service { int keyType = 2; }\n", encoding="utf-8")
        run(["git", "add", "service.java"], self.tmp)
        run(["git", "commit", "-m", "baseline release"], self.tmp)
        run(["git", "tag", "release-20260601"], self.tmp)
        (self.tmp / "service.java").write_text("class Service { int keyType = 5; }\n", encoding="utf-8")
        run(["git", "commit", "-am", "fix(payment): change terminal key type"], self.tmp)
        self.base = "release-20260601"
        self.head = "HEAD"

    def test_blocking_cr_scan_issue_sets_gate_to_blocked_in_json(self):
        output = self.tmp / "report.json"
        proc = run(
            [
                "python3",
                str(SCRIPT),
                "--repo",
                str(self.tmp),
                "--from-version",
                self.base,
                "--to-version",
                self.head,
                "--format",
                "json",
                "--output",
                str(output),
            ],
            ROOT,
        )
        self.assertEqual(proc.returncode, 0)
        data = json.loads(output.read_text(encoding="utf-8"))
        self.assertTrue(data["cr_scan_issues"])
        self.assertEqual(data["cr_scan_issues"][0]["severity"], "阻塞")
        self.assertEqual(data["risk"]["gate_conclusion"], "阻塞上线")

    def test_fail_on_blocker_returns_exit_3_for_blocking_cr_scan_issue(self):
        output = self.tmp / "report.json"
        proc = run(
            [
                "python3",
                str(SCRIPT),
                "--repo",
                str(self.tmp),
                "--from-version",
                self.base,
                "--to-version",
                self.head,
                "--format",
                "json",
                "--output",
                str(output),
                "--fail-on",
                "blocker",
            ],
            ROOT,
            check=False,
        )
        self.assertEqual(proc.returncode, 3, proc.stderr + proc.stdout)

    def test_markdown_risk_level_matches_blocking_gate(self):
        output = self.tmp / "report.md"
        proc = run(
            [
                "python3",
                str(SCRIPT),
                "--repo",
                str(self.tmp),
                "--from-version",
                self.base,
                "--to-version",
                self.head,
                "--cr-output",
                str(output),
            ],
            ROOT,
        )
        self.assertEqual(proc.returncode, 0)
        text = output.read_text(encoding="utf-8")
        self.assertIn("## 发布风险与回滚", text)
        self.assertIn("- 风险等级：高", text)
        self.assertNotIn("- 风险等级：中", text)


if __name__ == "__main__":
    unittest.main()
