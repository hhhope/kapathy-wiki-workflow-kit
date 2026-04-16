from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.repo_policy_check import find_draft_skill_violations


@dataclass(frozen=True)
class HealthCheckResult:
    name: str
    passed: bool
    details: list[str]


def run_health_checks(repo_root: Path) -> list[HealthCheckResult]:
    violations = [path.as_posix() for path in find_draft_skill_violations(repo_root)]
    return [
        HealthCheckResult(
            name="draft-skill-runtime-surface",
            passed=not violations,
            details=violations,
        )
    ]


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
