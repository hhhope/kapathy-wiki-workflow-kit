from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from coverage_model import evaluate_gate


RESULT_STATUSES = {"satisfied", "issue", "not_applicable", "blocked"}
REQUIRED_RESULT_FIELDS = {
    "check_id",
    "status",
    "conclusion",
    "evidence_refs",
    "risk",
    "unresolved_questions",
    "linked_diff_units",
}
REQUIRED_WAIVER_FIELDS = {"owner", "reason", "expiry", "affected_checks", "residual_risk"}
HIGH_SEVERITIES = {"critical", "severe", "high", "严重", "高"}


def _blocked_result(raw: dict[str, Any], reason: str) -> dict[str, Any]:
    result = dict(raw)
    result["status"] = "blocked"
    result["conclusion"] = reason
    result.setdefault("evidence_refs", [])
    result.setdefault("risk", "high")
    result.setdefault("unresolved_questions", [])
    result.setdefault("linked_diff_units", [])
    return result


def _normalize_result(raw: dict[str, Any]) -> dict[str, Any]:
    missing = sorted(REQUIRED_RESULT_FIELDS - set(raw))
    if missing:
        return _blocked_result(raw, f"checker result missing fields: {', '.join(missing)}")
    if raw.get("status") not in RESULT_STATUSES:
        return _blocked_result(raw, f"invalid checker status: {raw.get('status')}")
    if raw["status"] != "blocked" and not raw.get("evidence_refs"):
        return _blocked_result(raw, "checker result missing evidence_refs")
    return dict(raw)


def _valid_waiver(raw: dict[str, Any]) -> bool:
    return not (REQUIRED_WAIVER_FIELDS - set(raw)) and bool(raw.get("affected_checks"))


def _issue_from_result(index: int, result: dict[str, Any]) -> dict[str, Any]:
    return {
        "CR-ID": f"CR-COVERAGE-{index:03d}",
        "source_worker": "coverage_gate",
        "severity": "high" if result.get("risk") == "high" else "medium",
        "category": "coverage_check",
        "title": result.get("conclusion") or "coverage check did not close",
        "evidence": result.get("evidence_refs", []),
        "impact": "; ".join(result.get("unresolved_questions", [])),
        "required_action": "Close the required check or record an explicit waiver.",
        "owner": "",
        "blocking": result.get("risk") == "high" or result.get("status") == "blocked",
        "status": "open",
        "related_files": [],
        "related_commits": [],
        "related_diff_units": result.get("linked_diff_units", []),
        "related_review_groups": result.get("review_group_ids", []),
    }


def _normalize_confirmed_issue(index: int, issue: dict[str, Any]) -> dict[str, Any]:
    evidence = issue.get("evidence_refs") or issue.get("evidence") or []
    linked_checks = issue.get("linked_check_ids") or issue.get("related_checks") or []
    linked_units = issue.get("linked_diff_unit_ids") or issue.get("related_diff_units") or []
    severity = str(issue.get("severity") or "high").lower()
    return {
        "CR-ID": issue.get("CR-ID") or f"CR-MANUAL-{index:03d}",
        "source_worker": issue.get("source_worker") or "manual_review",
        "severity": severity,
        "category": issue.get("category") or "manual_review",
        "title": issue.get("title") or "confirmed CR issue",
        "evidence": evidence,
        "impact": issue.get("impact") or "",
        "required_action": issue.get("required_action") or "Resolve the confirmed issue or record an explicit waiver.",
        "owner": issue.get("owner") or "",
        "blocking": bool(issue.get("blocking", severity in HIGH_SEVERITIES)),
        "status": issue.get("status") or "open",
        "related_files": issue.get("related_files") or [],
        "related_commits": issue.get("related_commits") or [],
        "related_diff_units": linked_units,
        "related_review_groups": issue.get("related_review_groups") or [],
        "related_checks": linked_checks,
        "manual_review_gap": not linked_checks and not linked_units,
    }


def _checker_results_from_confirmed_issue(issue: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = issue.get("evidence", [])
    linked_units = issue.get("related_diff_units", [])
    linked_checks = issue.get("related_checks", [])
    severity = str(issue.get("severity") or "").lower()
    risk = "high" if issue.get("blocking") or severity in HIGH_SEVERITIES else "medium"
    status = "issue" if linked_checks else "blocked"
    check_ids = linked_checks or [f"manual-review-gap-{issue.get('CR-ID')}"]
    return [
        {
            "check_id": check_id,
            "status": status,
            "conclusion": issue.get("title") or "confirmed CR issue",
            "evidence_refs": evidence,
            "risk": risk,
            "unresolved_questions": [] if linked_checks else ["confirmed issue is not linked to a coverage check"],
            "linked_diff_units": linked_units,
            "issue_id": issue.get("CR-ID"),
        }
        for check_id in check_ids
    ]


def apply_confirmed_issues(
    result: dict[str, Any],
    confirmed_issues: list[dict[str, Any]],
) -> dict[str, Any]:
    updated = copy.deepcopy(result)
    normalized_issues = [
        _normalize_confirmed_issue(index, issue)
        for index, issue in enumerate(confirmed_issues, 1)
    ]
    new_checker_results: list[dict[str, Any]] = []
    for issue in normalized_issues:
        new_checker_results.extend(_checker_results_from_confirmed_issue(issue))

    normalized_results = [_normalize_result(raw) for raw in [*updated.get("checker_results", []), *new_checker_results]]
    updated["checker_results"] = normalized_results
    checks_by_id = {check["id"]: check for check in updated.get("checks", [])}
    for checker_result in normalized_results:
        check = checks_by_id.get(checker_result.get("check_id"))
        if check:
            check["status"] = checker_result["status"]

    existing_issues = [dict(item) for item in updated.get("issues", [])]
    existing_ids = {item.get("CR-ID") for item in existing_issues}
    for issue in normalized_issues:
        if issue.get("CR-ID") not in existing_ids:
            existing_issues.append(issue)
            existing_ids.add(issue.get("CR-ID"))
    updated["issues"] = existing_issues
    updated["gate"] = evaluate_gate(
        updated.get("state", {}),
        updated.get("diff_units", []),
        updated.get("checks", []),
        updated.get("checker_results", []),
    )
    return updated


def apply_checker_results(
    result: dict[str, Any],
    checker_results: list[dict[str, Any]],
    waivers: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    updated = copy.deepcopy(result)
    normalized = [_normalize_result(raw) for raw in checker_results]
    updated["checker_results"] = normalized
    checks_by_id = {check["id"]: check for check in updated["checks"]}
    for checker_result in normalized:
        check = checks_by_id.get(checker_result.get("check_id"))
        if check:
            check["status"] = checker_result["status"]
    updated["issues"] = [
        _issue_from_result(index, item)
        for index, item in enumerate(normalized, 1)
        if item.get("status") in {"issue", "blocked"}
    ]
    updated["waivers"] = [dict(item) for item in waivers or [] if _valid_waiver(item)]
    for waiver in updated["waivers"]:
        for check_id in waiver["affected_checks"]:
            if check_id in checks_by_id:
                checks_by_id[check_id]["status"] = "waived"
    updated["gate"] = evaluate_gate(
        updated.get("state", {}),
        updated["diff_units"],
        updated["checks"],
        updated["checker_results"],
    )
    return updated


def manual_checker_fallback(check: dict[str, Any], reason: str) -> dict[str, Any]:
    return {
        "check_id": check.get("id"),
        "status": "blocked",
        "conclusion": reason,
        "evidence_refs": [],
        "risk": "high",
        "unresolved_questions": [reason],
        "linked_diff_units": check.get("diff_unit_ids", []),
    }


def run_money_unit_checker(
    result: dict[str, Any],
    consumer_evidence: list[dict[str, Any] | str] | None = None,
) -> list[dict[str, Any]]:
    evidence = consumer_evidence or []
    money_checks = [check for check in result.get("checks", []) if check.get("rule_id") == "money"]
    if not money_checks:
        return []
    group_ids_by_unit: dict[str, list[str]] = {}
    for group in result.get("review_groups", []):
        if group.get("rule_id") != "money":
            continue
        for unit_id in group.get("linked_diff_units", []):
            group_ids_by_unit.setdefault(unit_id, []).append(group.get("id"))

    def review_group_ids(check: dict[str, Any]) -> list[str]:
        ids: list[str] = []
        for unit_id in check.get("diff_unit_ids", []):
            for group_id in group_ids_by_unit.get(unit_id, []):
                if group_id and group_id not in ids:
                    ids.append(group_id)
        return ids

    if not evidence:
        return [
            {
                "check_id": check.get("id"),
                "status": "blocked",
                "conclusion": "money/unit check missing affected consumer evidence",
                "evidence_refs": [],
                "risk": "high",
                "unresolved_questions": [
                    "Affected consumer evidence is required, for example QueryBalanceHandle downstream conversion.",
                ],
                "linked_diff_units": check.get("diff_unit_ids", []),
                "review_group_ids": review_group_ids(check),
            }
            for check in money_checks
        ]

    evidence_refs = [str(item) for item in evidence]
    return [
        {
            "check_id": check.get("id"),
            "status": "satisfied",
            "conclusion": "money/unit check closed with unit chain and affected consumer evidence",
            "evidence_refs": evidence_refs,
            "risk": "low",
            "unresolved_questions": [],
            "linked_diff_units": check.get("diff_unit_ids", []),
            "review_group_ids": review_group_ids(check),
        }
        for check in money_checks
    ]


def blocked_case_result(reason: str) -> dict[str, Any]:
    result = {
        "state": {"stage": "blocked", "coverage_counters": {}},
        "diff_units": [],
        "facts": [],
        "review_groups": [],
        "checks": [
            {
                "id": "check-blocked-case",
                "rule_id": "coverage_gate",
                "diff_unit_ids": [],
                "title": reason,
                "required": True,
                "status": "blocked",
            }
        ],
        "checker_results": [manual_checker_fallback({"id": "check-blocked-case", "diff_unit_ids": []}, reason)],
        "issues": [],
        "waivers": [],
    }
    result["gate"] = {"decision": "blocked", "reasons": [reason]}
    return result


def invalidate_stale_checker_results(result: dict[str, Any]) -> dict[str, Any]:
    updated = copy.deepcopy(result)
    state = updated.get("state", {})
    basis_keys = ["range_hash", "config_hash", "diff_ledger_hash", "agent_version"]
    invalidated = []
    for checker_result in updated.get("checker_results", []):
        stale = any(state.get(key) and checker_result.get(key) != state.get(key) for key in basis_keys)
        invalidated.append(
            _blocked_result(checker_result, "stale checker result basis")
            if stale else checker_result
        )
    updated["checker_results"] = invalidated
    updated["gate"] = evaluate_gate(
        state,
        updated["diff_units"],
        updated["checks"],
        updated["checker_results"],
    )
    return updated


def render_report(result: dict[str, Any]) -> str:
    units = result.get("diff_units", [])
    checks = result.get("checks", [])
    gate = result.get("gate", {})
    status_counts = {}
    for check in checks:
        status_counts[check.get("status", "unknown")] = status_counts.get(check.get("status", "unknown"), 0) + 1
    rules = sorted({check.get("rule_id") for check in checks if check.get("rule_id")})
    lines = [
        "# CR Coverage Gate",
        "",
        f"Gate Decision: `{gate.get('decision', 'blocked')}`",
        f"Gate Reasons: {', '.join(gate.get('reasons', [])) or 'none'}",
        "",
        "## Coverage",
        f"- Files: {sum(1 for unit in units if unit.get('unit_type') == 'file')}",
        f"- Hunks: {sum(1 for unit in units if unit.get('unit_type') in {'hunk', 'child_hunk'})}",
        f"- Special Units: {sum(1 for unit in units if unit.get('unit_type') == 'special')}",
        f"- Checks: {len(checks)} ({status_counts})",
        f"- Rules Triggered: {', '.join(rules) or 'none'}",
        f"- Review Groups: {len(result.get('review_groups', []))}",
        f"- Waivers: {len(result.get('waivers', []))}",
        "",
        "## Checks by Rule",
    ]
    by_rule = _check_counts_by_rule(checks)
    if not by_rule:
        lines.append("- none")
    for rule_id, statuses in sorted(by_rule.items()):
        lines.append(
            f"- {rule_id}: "
            f"open={statuses.get('open', 0)}, "
            f"blocked={statuses.get('blocked', 0)}, "
            f"satisfied={statuses.get('satisfied', 0)}, "
            f"issue={statuses.get('issue', 0)}, "
            f"not_applicable={statuses.get('not_applicable', 0)}, "
            f"waived={statuses.get('waived', 0)}"
        )
    lines.extend([
        "",
        "## Issues",
    ])
    issues = result.get("issues", [])
    if not issues:
        lines.append("- none")
    for issue in issues:
        lines.append(f"- {issue.get('CR-ID')}: {issue.get('title')} [blocking={issue.get('blocking')}]")
    return "\n".join(lines) + "\n"


def _check_counts_by_rule(checks: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for check in checks:
        rule_id = check.get("rule_id") or "unknown"
        status = check.get("status") or "unknown"
        counts.setdefault(rule_id, {})
        counts[rule_id][status] = counts[rule_id].get(status, 0) + 1
    return counts


def _normalize_report_profile(report_profile: str) -> str:
    normalized = report_profile.lower().replace("-", "_")
    aliases = {
        "plugin": "plugin_plain",
        "plain": "plugin_plain",
        "repo": "repo_existing",
        "repository": "repo_existing",
    }
    return aliases.get(normalized, normalized)


def _read_reference_report(reference_report_path: str | None) -> str:
    if not reference_report_path:
        return ""
    path = Path(reference_report_path)
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _repo_existing_prefix(project: str, report_target: str, reference_text: str) -> list[str]:
    if not reference_text:
        return []

    lines: list[str] = []
    if reference_text.startswith("---"):
        lines.extend(
            [
                "---",
                f"title: 代码评审报告 — {project} {report_target}",
                f"tags: [CR, 代码评审, {project}]",
                "---",
                "",
            ]
        )
    if "[!tip]" in reference_text:
        lines.extend(["> [!tip] 本报告可关联到 [[README|项目 CR 索引页]]", ""])
    if "标签：" in reference_text:
        lines.extend(["> 标签：`#CR` `#代码评审` `#门禁` `#Account-CR-Agent`", ""])
    return lines


def render_formal_report(
    result: dict[str, Any],
    project: str,
    report_target: str,
    report_profile: str = "plugin_plain",
    case_report_path: str | None = None,
    reference_report_path: str | None = None,
) -> str:
    gate = result.get("gate", {})
    decision = gate.get("decision", "blocked")
    reasons = ", ".join(gate.get("reasons", [])) or "none"
    profile = _normalize_report_profile(report_profile)
    reference_text = _read_reference_report(reference_report_path)
    checks = result.get("checks", [])
    issues = result.get("issues", [])
    counts = _check_counts_by_rule(checks)
    required_open_or_blocked = [
        check for check in checks
        if check.get("required") and check.get("status") in {"open", "blocked"}
    ]
    report_state = "stage_report" if required_open_or_blocked or decision == "blocked" else "complete_cr_report"
    matrix_lines = []
    for rule_id, statuses in sorted(counts.items()):
        ordered = [
            f"open={statuses.get('open', 0)}",
            f"blocked={statuses.get('blocked', 0)}",
            f"satisfied={statuses.get('satisfied', 0)}",
            f"issue={statuses.get('issue', 0)}",
            f"not_applicable={statuses.get('not_applicable', 0)}",
            f"waived={statuses.get('waived', 0)}",
        ]
        matrix_lines.append(f"- {rule_id}: " + ", ".join(ordered))
    if not matrix_lines:
        matrix_lines.append("- none")

    status_counts: dict[str, int] = {}
    for check in checks:
        status = check.get("status") or "unknown"
        status_counts[status] = status_counts.get(status, 0) + 1
    high_issue_count = sum(
        1 for issue in issues
        if str(issue.get("severity", "")).lower() in HIGH_SEVERITIES or issue.get("blocking")
    )
    blocker_lines = [
        f"- open diff units: {sum(1 for unit in result.get('diff_units', []) if unit.get('status') == 'open')}",
        f"- open required checks: {sum(1 for check in checks if check.get('required') and check.get('status') == 'open')}",
        f"- blocked checks: {sum(1 for check in checks if check.get('status') == 'blocked')}",
        f"- confirmed high/severe issues: {high_issue_count}",
        f"- gate reasons: {reasons}",
    ]
    issue_lines = []
    if issues:
        for issue in issues:
            issue_lines.append(
                f"- {issue.get('CR-ID')}: {issue.get('title')} "
                f"[severity={issue.get('severity')}, blocking={issue.get('blocking')}]"
            )
    else:
        issue_lines.append("- none")

    open_check_lines = []
    for check in required_open_or_blocked[:10]:
        unit_ids = ", ".join(check.get("diff_unit_ids", [])) or "none"
        open_check_lines.append(
            f"- {check.get('id')} [{check.get('rule_id')}] {check.get('title')} -> {unit_ids}"
        )
    if not open_check_lines:
        open_check_lines.append("- none")
    if case_report_path:
        case_dir = str(Path(case_report_path).parent)
        artifact_paths = [
            f"- Full checks list: {case_dir}/checks.jsonl",
            f"- Full diff-unit list: {case_dir}/diff-units.jsonl",
            f"- Issue registry: {case_dir}/issues.jsonl",
        ]
    else:
        artifact_paths = [
            "- Full checks list: not written",
            "- Full diff-unit list: not written",
            "- Issue registry: not written",
        ]

    artifact_line = f"Case Coverage Artifact: {case_report_path}" if case_report_path else "Case Coverage Artifact: not written"
    profile_line = f"Report Profile: {profile}"
    prefix = _repo_existing_prefix(project, report_target, reference_text) if profile == "repo_existing" else []
    return "\n".join(
        [
            *prefix,
            f"# 代码评审报告 — {project} {report_target}",
            "",
            "## 最终结论（是否可发布）",
            f"- 一句话结论：**Gate Decision: `{decision}`；Gate Reasons: {reasons}。**",
            "- 结论矩阵：",
            "",
            "| 决策项 | 结论 | 原因 |",
            "|---|---|---|",
            f"| 代码合入状态 | {decision} | {reasons} |",
            f"| 生产开关 / 发布动作 | {decision} | required checks and checker evidence decide release action |",
            f"| 宣称发布完成 | {decision} | test, UAT, rollback, and coverage evidence must close |",
            "| 后续联调 / 预发验证 | allowed when blockers are owned | does not override gate |",
            "",
            f"- {profile_line}",
            f"- {artifact_line}",
            f"- Report State: `{report_state}`",
            "",
            "## 必须补齐的阻塞项",
            "| 阻塞项 | 责任人 | 最晚完成时间 | 完成标准 |",
            "|---|---|---|---|",
            "| Close open or blocked required checks | owner TBD | before release-complete claim | coverage matrix has no unowned blocker |",
            "",
            "## 变更基本信息",
            f"- 项目：{project}",
            f"- 评审范围：{report_target}",
            "- 评审人：Codex / Account CR Agent",
            "",
            "## 评分卡（100分）",
            "### 技术质量评分",
            "- 总分：blocked until required checks close",
            "",
            "#### 技术质量评分扣分依据",
            "每个技术质量分项都必须说明扣分依据；当前报告由 coverage gate 驱动，未关闭项按阻塞处理。",
            "",
            "### CR 执行审计评分",
            "- 总分：blocked until checker closure evidence exists",
            "",
            "## CR 执行审计",
            "- coverage_gate: produced diff units, checks, and gate artifact",
            "- cr-report: rendered formal report without recalculating gate",
            "",
            "## 技术审查结果",
            *issue_lines,
            "",
            "## TODO 跟踪",
            "- Close all open or blocked required checks before release-complete claim.",
            "",
            "## 测试证据",
            "- Pending checker, replay, UAT, or blocking reason evidence.",
            "",
            "## 发布风险与回滚",
            "- Release remains blocked while gate is blocked.",
            "",
            "## Gate Blocker Sources",
            *blocker_lines,
            "",
            "## 覆盖矩阵",
            f"- Checks total: {len(checks)} ({status_counts})",
            *matrix_lines,
            "",
            "## Open Check Drilldown",
            *open_check_lines,
            *artifact_paths,
            "",
            "## 附录：Issue Registry（可选）",
            "- See normalized issue registry when available.",
            "",
            "## 处置项",
            "- Keep coverage artifact separate from this formal human CR report.",
            "",
        ]
    )
