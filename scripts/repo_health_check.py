from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.repo_policy_check import find_draft_skill_violations

REQUIRED_EVALUATION_SECTIONS = (
    "## Pressure Scenarios",
    "## RED Baseline",
    "## GREEN Result",
    "## Residual Risks",
)


@dataclass(frozen=True)
class HealthCheckResult:
    name: str
    passed: bool
    details: list[str]


def run_health_checks(repo_root: Path) -> list[HealthCheckResult]:
    draft_skill_violations = [path.as_posix() for path in find_draft_skill_violations(repo_root)]
    skill_evaluation_violations = find_skill_evaluation_evidence_violations(repo_root)
    return [
        HealthCheckResult(
            name="draft-skill-runtime-surface",
            passed=not draft_skill_violations,
            details=draft_skill_violations,
        ),
        HealthCheckResult(
            name="skill-evaluation-evidence",
            passed=not skill_evaluation_violations,
            details=skill_evaluation_violations,
        ),
    ]


def find_skill_evaluation_evidence_violations(repo_root: Path) -> list[str]:
    changes_root = repo_root / "openspec" / "changes"
    if not changes_root.exists():
        return []

    violations: list[str] = []
    for change_dir in sorted(path for path in changes_root.iterdir() if path.is_dir() and path.name != "archive"):
        if not _change_references_formal_skills(change_dir):
            continue
        evaluation_path = change_dir / "evaluation.md"
        if not evaluation_path.exists():
            violations.append(change_dir.relative_to(repo_root).as_posix())
            continue

        content = evaluation_path.read_text(encoding="utf-8")
        if any(section not in content for section in REQUIRED_EVALUATION_SECTIONS):
            violations.append(change_dir.relative_to(repo_root).as_posix())
    return violations


def _change_references_formal_skills(change_dir: Path) -> bool:
    for path in change_dir.rglob("*.md"):
        if path.name == "evaluation.md":
            continue
        if ".codex/skills/" in path.read_text(encoding="utf-8"):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run repository health checks.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root to inspect. Defaults to the current directory.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    results = run_health_checks(repo_root)

    failed = False
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.name}")
        for detail in result.details:
            print(f"  {detail}")
        failed = failed or not result.passed

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
