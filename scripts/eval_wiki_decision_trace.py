#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "wiki/evals/wiki-react-trace-cases.json"


@dataclass(frozen=True)
class EvalResult:
    passed: bool
    errors: list[str]


def _load_json(path: Path | str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_cases(path: Path | str = DEFAULT_CASES) -> list[dict[str, Any]]:
    payload = _load_json(path)
    if isinstance(payload, dict):
        cases = payload.get("cases")
    else:
        cases = payload
    if not isinstance(cases, list):
        raise ValueError("case file must be a list or an object with a cases list")
    return [case for case in cases if isinstance(case, dict)]


def load_traces(path: Path | str) -> list[dict[str, Any]]:
    payload = _load_json(path)
    if isinstance(payload, dict):
        traces = payload.get("traces")
    else:
        traces = payload
    if not isinstance(traces, list):
        raise ValueError("trace file must be a list or an object with a traces list")
    return [trace for trace in traces if isinstance(trace, dict)]


def evaluate_trace_cases(
    cases: list[dict[str, Any]],
    traces: list[dict[str, Any]],
) -> EvalResult:
    traces_by_case = {str(trace.get("case_id")): trace for trace in traces}
    errors: list[str] = []

    for case in cases:
        case_id = str(case.get("id") or "")
        if not case_id:
            errors.append("case is missing id")
            continue

        trace = traces_by_case.get(case_id)
        if trace is None:
            errors.append(f"{case_id}: missing trace")
            continue

        errors.extend(_evaluate_case(case, trace))

    return EvalResult(passed=not errors, errors=errors)


def _evaluate_case(case: dict[str, Any], trace: dict[str, Any]) -> list[str]:
    case_id = str(case["id"])
    errors: list[str] = []

    for field in [
        "case_id",
        "input",
        "intent",
        "evidence_object",
        "risk_level",
        "actions",
        "observations",
        "decision",
        "boundary",
        "forbidden_actions_checked",
    ]:
        if field not in trace:
            errors.append(f"{case_id}: trace missing required field {field}")

    allowed_intents = {str(intent) for intent in _as_list(case.get("allowed_intents"))}
    if allowed_intents and str(trace.get("intent")) not in allowed_intents:
        errors.append(
            f"{case_id}: intent {trace.get('intent')!r} not in allowed_intents {sorted(allowed_intents)}"
        )

    required_boundary = case.get("required_boundary")
    if required_boundary and trace.get("boundary") != required_boundary:
        errors.append(
            f"{case_id}: boundary {trace.get('boundary')!r} != required_boundary {required_boundary!r}"
        )

    actions = {str(action) for action in _as_list(trace.get("actions"))}
    checked = {str(action) for action in _as_list(trace.get("forbidden_actions_checked"))}

    for action in _as_list(case.get("required_actions_all")):
        if str(action) not in actions:
            errors.append(f"{case_id}: missing required action {action}")

    required_any = [str(action) for action in _as_list(case.get("required_actions_any"))]
    if required_any and not any(action in actions for action in required_any):
        errors.append(f"{case_id}: missing one of required_actions_any {required_any}")

    forbidden = [str(action) for action in _as_list(case.get("forbidden_actions"))]
    for action in forbidden:
        if action in actions:
            errors.append(f"{case_id}: forbidden action {action} was present")
        if action not in checked:
            errors.append(f"{case_id}: forbidden_actions_checked missing {action}")

    observations = trace.get("observations") if isinstance(trace.get("observations"), dict) else {}
    static_facts = _as_list(observations.get("static_facts"))
    exploratory = _as_list(observations.get("exploratory_judgments"))

    if case.get("requires_static_facts") and not static_facts:
        errors.append(f"{case_id}: requires static_facts observation")
    if case.get("requires_exploratory_judgments") and not exploratory:
        errors.append(f"{case_id}: requires exploratory_judgments observation")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate wiki decision traces against replay cases.")
    parser.add_argument("--cases", default=DEFAULT_CASES)
    parser.add_argument("--traces", required=True)
    parser.add_argument("--json-output")
    args = parser.parse_args()

    result = evaluate_trace_cases(load_cases(args.cases), load_traces(args.traces))
    payload = {"passed": result.passed, "errors": result.errors}
    if args.json_output:
        Path(args.json_output).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if result.errors:
        for error in result.errors:
            print(f"ERROR {error}", file=sys.stderr)
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
