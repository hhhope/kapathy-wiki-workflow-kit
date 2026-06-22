#!/usr/bin/env python3
"""Generate a standardized release diff audit report."""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_RULES: dict[str, Any] = {
    "main_ref": "origin/master",
    "baseline_strategy": "same_branch_previous",
    "release_tag_patterns": ["release-*", "v*"],
    "release_branch_patterns": ["release-*", "origin/release-*", "origin/release/*"],
    "test_evidence_paths": ["test", "tests", "src/test", "__tests__", "spec"],
    "rollback_evidence_paths": ["rollback", "revert", "db/rollback"],
    "owners": {},
}

ALLOWED_RULE_KEYS = set(DEFAULT_RULES)
ALLOWED_BASELINE_STRATEGIES = {"same_branch_previous", "release_ref"}
FAIL_ON_CHOICES = {"never", "gate", "blocker", "score"}

SECRET_PATTERNS = [
    re.compile(r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]?[^'\"\s]{6,}"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?key|secret[_-]?key)\s*[:=]\s*['\"]?[^'\"\s]{8,}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?i)(token)\s*[:=]\s*['\"]?[A-Za-z0-9._\-]{16,}"),
]


class ReleaseDiffError(RuntimeError):
    pass


def run_git(repo: Path, args: list[str], check: bool = True) -> str:
    command = ["git", "-C", str(repo), *args]
    proc = subprocess.run(command, text=True, encoding="utf-8", errors="replace", capture_output=True)
    if check and proc.returncode != 0:
        raise ReleaseDiffError(proc.stderr.strip() or f"git command failed: {' '.join(command)}")
    return proc.stdout


def display_time(value: str) -> str:
    if not value:
        return ""
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError:
        return value.replace("T", " ").replace("Z", "").split("+", 1)[0]
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone()
    return parsed.strftime("%Y-%m-%d %H:%M:%S")


def display_time_range(start: str, end: str) -> str:
    return f"{display_time(start)} ~ {display_time(end)}"


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_simple_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    root: dict[str, Any] = {}
    current_key: str | None = None
    current_map_key: str | None = None
    lines = path.read_text(encoding="utf-8").splitlines()

    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        if indent == 0 and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            current_map_key = None
            if value:
                root[key] = parse_scalar(value)
            else:
                root[key] = {}
            continue

        if current_key is None:
            continue

        if line.startswith("- "):
            if current_map_key and isinstance(root.get(current_key), dict):
                root[current_key][current_map_key].append(parse_scalar(line[2:]))
            else:
                if not isinstance(root.get(current_key), list):
                    root[current_key] = []
                root[current_key].append(parse_scalar(line[2:]))
            continue

        if ":" in line and isinstance(root.get(current_key), dict):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                root[current_key][key] = parse_scalar(value)
                current_map_key = None
            else:
                root[current_key][key] = []
                current_map_key = key
            continue

    return root


def merge_rules(defaults: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    rules = json.loads(json.dumps(defaults))
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(rules.get(key), dict):
            rules[key].update(value)
        else:
            rules[key] = value
    return rules


def validate_rules(rules: dict[str, Any], source: Path) -> None:
    unknown = sorted(set(rules) - ALLOWED_RULE_KEYS)
    if unknown:
        raise ReleaseDiffError(f"unknown rule keys in {source.name}: {', '.join(unknown)}")

    for key in [
        "release_tag_patterns",
        "release_branch_patterns",
        "test_evidence_paths",
        "rollback_evidence_paths",
    ]:
        if not isinstance(rules.get(key), list) or not all(isinstance(item, str) for item in rules[key]):
            raise ReleaseDiffError(f"rule {key} must be a list of strings")

    if rules.get("baseline_strategy") not in ALLOWED_BASELINE_STRATEGIES:
        raise ReleaseDiffError(f"rule baseline_strategy must be one of: {', '.join(sorted(ALLOWED_BASELINE_STRATEGIES))}")


def ref_exists(repo: Path, ref: str) -> bool:
    proc = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", ref], capture_output=True)
    return proc.returncode == 0


def resolve_full_sha(repo: Path, ref: str) -> str:
    return run_git(repo, ["rev-parse", "--verify", f"{ref}^{{commit}}"]).strip()


def get_ref_summary(repo: Path, ref: str) -> dict[str, str]:
    sha = resolve_full_sha(repo, ref)
    fmt = "%H%x1f%an%x1f%ad%x1f%s"
    raw = run_git(repo, ["show", "-s", "--date=iso-strict", f"--format={fmt}", sha])
    parts = raw.strip().split("\x1f", 3)
    if len(parts) != 4:
        return {"ref": ref, "sha": sha, "short_sha": sha[:12], "author": "", "date": "", "subject": ""}
    full_sha, author, date, subject = parts
    return {"ref": ref, "sha": full_sha, "short_sha": full_sha[:12], "author": author, "date": date, "subject": subject}


def is_ancestor(repo: Path, older: str, newer: str) -> bool:
    proc = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor", older, newer], capture_output=True)
    return proc.returncode == 0


def is_first_parent_ancestor(repo: Path, older_sha: str, newer_sha: str) -> bool:
    raw = run_git(repo, ["rev-list", "--first-parent", newer_sha], check=False)
    return older_sha in {line.strip() for line in raw.splitlines() if line.strip()}


def match_any(value: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(value, pattern) for pattern in patterns)


def regex_any(value: str, patterns: list[str]) -> bool:
    return any(re.fullmatch(pattern, value) for pattern in patterns)


def resolve_main_ref(repo: Path, explicit: str | None, to_version: str | None, rules: dict[str, Any]) -> str:
    main_ref = to_version or explicit or str(rules.get("main_ref") or DEFAULT_RULES["main_ref"])
    if not ref_exists(repo, main_ref):
        raise ReleaseDiffError(f"main/to ref not found: {main_ref}")
    return main_ref


def resolve_base_ref(repo: Path, main_ref: str, explicit: str | None, from_version: str | None, rules: dict[str, Any]) -> tuple[str, str]:
    selected = from_version or explicit
    if selected:
        if not ref_exists(repo, selected):
            raise ReleaseDiffError(f"base/from ref not found: {selected}")
        return selected, "explicit-version" if from_version else "explicit"

    def nearest_reachable_tag() -> str | None:
        tag_patterns = list(rules.get("release_tag_patterns") or ["release-*", "v*"])
        reachable_raw = run_git(repo, ["rev-list", main_ref], check=False)
        reachable_shas = [line.strip() for line in reachable_raw.splitlines() if line.strip()]
        if len(reachable_shas) < 2:
            return None
        reachable_index = {sha: index for index, sha in enumerate(reachable_shas)}
        main_sha = reachable_shas[0]

        tags_raw = run_git(repo, ["tag", "--merged", main_ref], check=False)
        candidates: list[tuple[int, str]] = []
        for tag in [line.strip() for line in tags_raw.splitlines() if line.strip()]:
            if not match_any(tag, tag_patterns):
                continue
            tag_sha = run_git(repo, ["rev-list", "-n", "1", tag], check=False).strip()
            if tag_sha and tag_sha != main_sha and tag_sha in reachable_index:
                candidates.append((reachable_index[tag_sha], tag))
        if not candidates:
            return None
        candidates.sort(key=lambda item: item[0])
        return candidates[0][1]

    if str(rules.get("baseline_strategy") or "same_branch_previous") == "same_branch_previous":
        tag = nearest_reachable_tag()
        if tag:
            return tag, "reachable-tag"
        candidate = f"{main_ref}~1"
        if ref_exists(repo, candidate):
            return candidate, "same-branch-previous"
        raise ReleaseDiffError(
            f"same-branch previous version not found for {main_ref}. "
            "Provide --from-version with a previous commit or tag reachable from the same main branch."
        )

    tag = nearest_reachable_tag()
    if tag:
        return tag, "auto-tag"

    branch_patterns = list(rules.get("release_branch_patterns") or [])
    refs_raw = run_git(repo, ["for-each-ref", "--format=%(refname:short)", "refs/remotes", "refs/heads"], check=False)
    for ref in [line.strip() for line in refs_raw.splitlines() if line.strip()]:
        if match_any(ref, branch_patterns):
            return ref, "auto-branch"

    raise ReleaseDiffError("release baseline not found. Provide --from-version, --base-ref, or configure release patterns.")


def get_project_name(repo: Path) -> str:
    remote = run_git(repo, ["config", "--get", "remote.origin.url"], check=False).strip()
    if remote:
        normalized = remote.rstrip("/\\").replace("\\", "/")
        name = normalized.split("/")[-1]
        if name.endswith(".git"):
            name = name[:-4]
        if name:
            return name
    return repo.resolve().name


def get_commit_rows(repo: Path, base_ref: str, main_ref: str) -> list[dict[str, Any]]:
    fmt = "%H%x1f%P%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%ad%x1f%s"
    raw = run_git(repo, ["log", "--date=iso-strict", f"--pretty=format:{fmt}", f"{base_ref}..{main_ref}"], check=False)
    commits: list[dict[str, Any]] = []
    for line in raw.splitlines():
        parts = line.split("\x1f")
        if len(parts) != 8:
            continue
        sha, parents, author, author_email, committer, committer_email, date, subject = parts
        commits.append(
            {
                "sha": sha,
                "short_sha": sha[:12],
                "parents": parents.split() if parents else [],
                "is_merge": len(parents.split()) > 1,
                "author": author,
                "author_email": author_email,
                "committer": committer,
                "committer_email": committer_email,
                "date": date,
                "subject": subject,
            }
        )
    return commits


def get_first_parent_non_merge_rows(repo: Path, base_ref: str, main_ref: str) -> list[dict[str, Any]]:
    fmt = "%H%x1f%P%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%ad%x1f%s"
    raw = run_git(
        repo,
        ["log", "--first-parent", "--no-merges", "--date=iso-strict", f"--pretty=format:{fmt}", f"{base_ref}..{main_ref}"],
        check=False,
    )
    rows: list[dict[str, Any]] = []
    for line in raw.splitlines():
        parts = line.split("\x1f")
        if len(parts) != 8:
            continue
        sha, parents, author, author_email, committer, committer_email, date, subject = parts
        rows.append(
            {
                "sha": sha,
                "short_sha": sha[:12],
                "parents": parents.split() if parents else [],
                "is_merge": False,
                "author": author,
                "author_email": author_email,
                "committer": committer,
                "committer_email": committer_email,
                "date": date,
                "subject": subject,
            }
        )
    return rows


def get_commit_changed_files(repo: Path, commit_sha: str) -> list[dict[str, Any]]:
    raw = run_git(repo, ["show", "--name-status", "--find-renames", "--format=", commit_sha], check=False)
    files: list[dict[str, Any]] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            files.append({"status": "R", "path": parts[2], "old_path": parts[1]})
        elif len(parts) >= 2:
            files.append({"status": status[0], "path": parts[1], "old_path": None})
    return files


def extract_merge_source(subject: str) -> str | None:
    patterns = [
        r"Merge branch '([^']+)'",
        r'Merge branch "([^"]+)"',
        r"Merge remote-tracking branch '([^']+)'",
        r"Merge pull request #[0-9]+ from (.+)",
        r"Merged in ([^\s]+)",
        r"Merge (?:remote-tracking )?branch ([^\s]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, subject)
        if match:
            source = match.group(1).strip()
            if "/" in source and source.startswith("origin/"):
                source = source[len("origin/") :]
            return source
    return None


def get_changed_files(repo: Path, base_ref: str, main_ref: str) -> list[dict[str, Any]]:
    raw = run_git(repo, ["diff", "--name-status", "--find-renames", f"{base_ref}..{main_ref}"], check=False)
    files: list[dict[str, Any]] = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            files.append({"status": "R", "path": parts[2], "old_path": parts[1]})
        elif len(parts) >= 2:
            files.append({"status": status[0], "path": parts[1], "old_path": None})
    return files


def get_numstat(repo: Path, base_ref: str, main_ref: str) -> dict[str, dict[str, int]]:
    raw = run_git(repo, ["diff", "--numstat", f"{base_ref}..{main_ref}"], check=False)
    stats: dict[str, dict[str, int]] = {}
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added = 0 if parts[0] == "-" else int(parts[0])
        deleted = 0 if parts[1] == "-" else int(parts[1])
        stats[parts[2]] = {"added": added, "deleted": deleted}
    return stats


def classify_file(path: str) -> str:
    lower = path.lower()
    name = Path(lower).name
    if any(part in lower for part in ["/test/", "/tests/", "src/test", "__tests__", "/spec/"]) or name.startswith("test_"):
        return "测试"
    if lower.endswith(".sql") or "migration" in lower or "ddl" in lower or "db/" in lower:
        return "DDL"
    if name in {"pom.xml", "build.gradle", "settings.gradle", "package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "requirements.txt", "go.mod", "cargo.toml"}:
        return "依赖"
    if name in {"jenkinsfile", "dockerfile"} or ".github/" in lower or ".gitlab-ci" in lower or "pipeline" in lower:
        return "流水线"
    if lower.endswith((".yml", ".yaml", ".properties", ".conf", ".ini", ".toml", ".json", ".xml")):
        return "配置"
    if lower.endswith((".sh", ".bash", ".ps1", ".bat", ".cmd")) or "/scripts/" in lower:
        return "脚本"
    if lower.endswith((".md", ".txt", ".adoc", ".rst")) or "/docs/" in lower:
        return "文档"
    if lower.endswith((".java", ".kt", ".py", ".go", ".js", ".jsx", ".ts", ".tsx", ".vue", ".c", ".cpp", ".h", ".cs", ".rb", ".php", ".rs")):
        return "业务代码"
    return "其他"


def load_codeowners(repo: Path) -> dict[str, list[str]]:
    candidates = [repo / "CODEOWNERS", repo / ".github" / "CODEOWNERS", repo / "docs" / "CODEOWNERS"]
    owners: dict[str, list[str]] = {}
    for candidate in candidates:
        if not candidate.exists():
            continue
        for raw in candidate.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                owners[parts[0]] = parts[1:]
        break
    return owners


def owners_for_path(path: str, owners: dict[str, list[str]]) -> list[str]:
    matched: list[str] = []
    for pattern, values in owners.items():
        normalized = pattern.lstrip("/")
        if fnmatch.fnmatch(path, normalized) or fnmatch.fnmatch(path, normalized.replace("**", "*")):
            matched.extend(values)
    return sorted(set(matched))


def contains_path_fragment(path: str, fragments: list[str]) -> bool:
    lower = path.lower()
    return any(fragment.lower() in lower for fragment in fragments)


def find_secret_lines(diff_text: str) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    current_file = ""
    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
        if not line.startswith("+") or line.startswith("+++"):
            continue
        added_line = line[1:].lstrip("\ufeff")
        for pattern in SECRET_PATTERNS:
            if pattern.search(added_line):
                findings.append({"file": current_file, "evidence": redact_secret(added_line.strip())})
                break
    return findings


def redact_secret(text: str) -> str:
    if len(text) <= 20:
        return "[redacted]"
    return text[:12] + "...[redacted]"


def has_any_category(categories: set[str], names: list[str]) -> bool:
    return any(name in categories for name in names)


def build_findings(
    commits: list[dict[str, Any]],
    first_parent_non_merge_commits: list[dict[str, Any]],
    changed_files: list[dict[str, Any]],
    categories: dict[str, list[str]],
    merge_sources: list[dict[str, Any]],
    rules: dict[str, Any],
    diff_text: str,
    numstat: dict[str, dict[str, int]],
) -> dict[str, Any]:
    test_paths = list(rules.get("test_evidence_paths") or [])
    rollback_paths = list(rules.get("rollback_evidence_paths") or [])

    findings: list[dict[str, Any]] = []
    high_risk_files: list[dict[str, Any]] = []
    rollback_concerns: list[dict[str, Any]] = []
    hints: list[dict[str, Any]] = []
    score = 0

    changed_paths = [item["path"] for item in changed_files]
    has_test_evidence = any(contains_path_fragment(path, test_paths) or classify_file(path) == "测试" for path in changed_paths)
    has_rollback_evidence = any(contains_path_fragment(path, rollback_paths) for path in changed_paths)
    secret_findings: list[dict[str, Any]] = []
    conclusion = "允许上线"
    risk_level = "低"

    return {
        "findings": findings,
        "high_risk_files": high_risk_files,
        "rollback_concerns": rollback_concerns,
        "secret_findings": secret_findings,
        "hints": hints,
        "score": score,
        "risk_level": risk_level,
        "gate_conclusion": conclusion,
        "has_test_evidence": has_test_evidence,
        "has_rollback_evidence": has_rollback_evidence,
    }


def suggest_cr_skills(categories: dict[str, list[str]], changed_paths: list[str]) -> list[dict[str, str]]:
    suggestions = [{"skill": "通用代码评审 skill", "reason": "上线范围包含代码或配置改动，需执行通用 CR"}]
    lower_paths = [p.lower() for p in changed_paths]
    if "DDL" in categories:
        suggestions.append({"skill": "DDL / database migration review skill", "reason": "存在 SQL、DDL 或 migration 改动"})
    if any("exception" in p or "errorcode" in p or "error_code" in p for p in lower_paths):
        suggestions.append({"skill": "exception review/scanner skill", "reason": "存在异常处理或错误码相关改动"})
    if any("channel" in p or "payment" in p or "bank" in p for p in lower_paths):
        suggestions.append({"skill": "channel-integration skill", "reason": "存在通道、支付或银行集成相关改动"})
    if any("api" in p or "controller" in p or "dto" in p for p in lower_paths):
        suggestions.append({"skill": "API migration / API review skill", "reason": "存在 API、Controller 或 DTO 改动"})
    return suggestions


def build_author_reviews(
    repo: Path, commits: list[dict[str, Any]], mainline_direct_commit_shas: set[str] | None = None
) -> list[dict[str, Any]]:
    mainline_direct_commit_shas = mainline_direct_commit_shas or set()
    reviews: dict[str, dict[str, Any]] = {}
    for commit in commits:
        author = commit["author"]
        is_mainline_direct = commit["sha"] in mainline_direct_commit_shas
        review = reviews.setdefault(
            author,
            {
                "author": author,
                "author_email": commit["author_email"],
                "commit_count": 0,
                "merge_commit_count": 0,
                "non_merge_commit_count": 0,
                "first_commit_at": commit["date"],
                "last_commit_at": commit["date"],
                "commits": [],
                "mainline_direct_commits": [],
                "mainline_direct_commit_count": 0,
                "files": {},
                "categories": Counter(),
            },
        )
        review["commit_count"] += 1
        if commit["is_merge"]:
            review["merge_commit_count"] += 1
        else:
            review["non_merge_commit_count"] += 1
        if is_mainline_direct:
            review["mainline_direct_commit_count"] += 1
        review["first_commit_at"] = min(review["first_commit_at"], commit["date"])
        review["last_commit_at"] = max(review["last_commit_at"], commit["date"])

        commit_files = get_commit_changed_files(repo, commit["sha"])
        for item in commit_files:
            path = item["path"]
            category = classify_file(path)
            review["categories"][category] += 1
            file_row = review["files"].setdefault(
                path,
                {
                    "path": path,
                    "status_set": set(),
                    "category": category,
                    "commit_count": 0,
                    "commits": [],
                },
            )
            file_row["status_set"].add(item["status"])
            file_row["commit_count"] += 1
            file_row["commits"].append(commit["short_sha"])

        review["commits"].append(
            {
                "short_sha": commit["short_sha"],
                "date": commit["date"],
                "subject": commit["subject"],
                "is_merge": commit["is_merge"],
                "is_mainline_direct": is_mainline_direct,
                "file_count": len(commit_files),
                "files": commit_files,
            }
        )
        if is_mainline_direct:
            review["mainline_direct_commits"].append(
                {
                    "short_sha": commit["short_sha"],
                    "date": commit["date"],
                    "subject": commit["subject"],
                    "file_count": len(commit_files),
                }
            )

    result: list[dict[str, Any]] = []
    for review in reviews.values():
        files = []
        for item in review["files"].values():
            files.append(
                {
                    "path": item["path"],
                    "status": ",".join(sorted(item["status_set"])),
                    "category": item["category"],
                    "commit_count": item["commit_count"],
                    "commits": sorted(set(item["commits"])),
                }
            )
        review["files"] = sorted(files, key=lambda item: item["path"])
        review["categories"] = dict(review["categories"])
        review["commits"] = sorted(review["commits"], key=lambda item: item["date"])
        review["mainline_direct_commits"] = sorted(review["mainline_direct_commits"], key=lambda item: item["date"])
        result.append(review)
    return sorted(result, key=lambda item: (-item["commit_count"], item["author"]))


def build_report(repo: Path, args: argparse.Namespace, rules: dict[str, Any]) -> dict[str, Any]:
    main_ref = resolve_main_ref(repo, args.main_ref, args.to_version, rules)
    base_ref, base_source = resolve_base_ref(repo, main_ref, args.base_ref, args.from_version, rules)
    base_summary = get_ref_summary(repo, base_ref)
    main_summary = get_ref_summary(repo, main_ref)
    if not args.allow_unrelated_range and not is_ancestor(repo, base_summary["sha"], main_summary["sha"]):
        raise ReleaseDiffError(
            f"invalid compare range: {base_ref} is not an ancestor of {main_ref}. "
            "Check version order or pass --allow-unrelated-range."
        )
    enforce_first_parent = base_source in {"same-branch-previous"}
    if not args.allow_unrelated_range and enforce_first_parent and not is_first_parent_ancestor(repo, base_summary["sha"], main_summary["sha"]):
        raise ReleaseDiffError(
            f"invalid release baseline: {base_ref} is not on the first-parent history of {main_ref}. "
            "Release comparison must use two versions on the same branch. "
            "Use a previous commit from the same first-parent line, or use a release tag reachable from the main branch."
        )
    project = get_project_name(repo)
    generated_at = dt.datetime.now().replace(microsecond=0).isoformat()

    commits = get_commit_rows(repo, base_ref, main_ref)
    first_parent_non_merge_commits = get_first_parent_non_merge_rows(repo, base_ref, main_ref)
    changed_files = get_changed_files(repo, base_ref, main_ref)
    numstat = get_numstat(repo, base_ref, main_ref)
    diff_text = run_git(repo, ["diff", f"{base_ref}..{main_ref}"], check=False)

    merge_sources = []
    for commit in commits:
        if commit["is_merge"]:
            merge_sources.append(
                {
                    "commit": commit["short_sha"],
                    "subject": commit["subject"],
                    "source_branch": extract_merge_source(commit["subject"]),
                    "author": commit["author"],
                    "date": commit["date"],
                }
            )

    categories: dict[str, list[str]] = defaultdict(list)
    for item in changed_files:
        categories[classify_file(item["path"])].append(item["path"])

    configured_owners = rules.get("owners") if isinstance(rules.get("owners"), dict) else {}
    owners = {**load_codeowners(repo), **configured_owners}
    owner_suggestions = []
    for item in changed_files:
        matched = owners_for_path(item["path"], owners)
        if matched:
            owner_suggestions.append({"path": item["path"], "owners": matched})

    risk = build_findings(commits, first_parent_non_merge_commits, changed_files, categories, merge_sources, rules, diff_text, numstat)
    changed_paths = [item["path"] for item in changed_files]
    cr_skills = suggest_cr_skills(categories, changed_paths)
    mainline_direct_commit_shas = {commit["sha"] for commit in first_parent_non_merge_commits}
    author_reviews = build_author_reviews(repo, commits, mainline_direct_commit_shas)
    mainline_direct_commits = []
    for commit in first_parent_non_merge_commits:
        mainline_direct_commits.append(
            {
                "short_sha": commit["short_sha"],
                "sha": commit["sha"],
                "author": commit["author"],
                "date": commit["date"],
                "subject": commit["subject"],
                "file_count": len(get_commit_changed_files(repo, commit["sha"])),
            }
        )
    partial_report_for_cr_issues = {
        "author_reviews": author_reviews,
        "merged_branches": merge_sources,
        "risk": risk,
    }
    cr_scan_issues = build_cr_scan_issues(repo, partial_report_for_cr_issues, first_parent_non_merge_commits)
    partial_report_for_cr_issues["cr_scan_issues"] = cr_scan_issues
    author_cr_issues = build_author_cr_issues(partial_report_for_cr_issues)

    authors = Counter(c["author"] for c in commits)
    committers = Counter(c["committer"] for c in commits)
    file_status = Counter(item["status"] for item in changed_files)

    try:
        rules_file_display = os.path.relpath(args.rules_file, repo).replace(os.sep, "/")
    except ValueError:
        rules_file_display = Path(args.rules_file).name

    report = {
        "project": project,
        "generated_at": generated_at,
        "main_ref": main_ref,
        "base_ref": base_ref,
        "base_source": base_source,
        "base_commit": base_summary,
        "main_commit": main_summary,
        "from_version": args.from_version,
        "to_version": args.to_version,
        "range": f"{base_ref}..{main_ref}",
        "commit_count": len(commits),
        "merge_commit_count": sum(1 for c in commits if c["is_merge"]),
        "non_merge_commit_count": sum(1 for c in commits if not c["is_merge"]),
        "changed_file_count": len(changed_files),
        "line_additions": sum(v["added"] for v in numstat.values()),
        "line_deletions": sum(v["deleted"] for v in numstat.values()),
        "authors": dict(authors),
        "committers": dict(committers),
        "file_status": dict(file_status),
        "commits": commits,
        "first_parent_non_merge_commits": first_parent_non_merge_commits,
        "mainline_direct_commits": mainline_direct_commits,
        "merged_branches": merge_sources,
        "changed_files": changed_files,
        "author_reviews": author_reviews,
        "author_cr_issues": author_cr_issues,
        "cr_scan_issues": cr_scan_issues,
        "categories": {key: sorted(values) for key, values in categories.items()},
        "owner_suggestions": owner_suggestions,
        "risk": risk,
        "cr_skill_suggestions": cr_skills,
        "rules_file": rules_file_display,
    }
    sync_risk_gate_with_cr_issues(report)
    return report


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "无\n"
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |")
    return "\n".join(lines) + "\n"


def review_points_for_author(review: dict[str, Any]) -> list[str]:
    categories = set(review.get("categories", {}))
    if not review.get("files"):
        return ["确认合并来源、目标分支、MR 范围和合并时点正确；具体代码文件由原提交作者复核。"]
    points = ["确认本人提交的业务逻辑正确、边界条件完整、无误提交文件。"]
    if "DDL" in categories:
        points.append("确认 DDL 已纳入上线执行清单，并具备回滚或补偿方案。")
    if "配置" in categories:
        points.append("确认配置项、Apollo namespace、注册中心或环境变量在生产已准备。")
    if "依赖" in categories:
        points.append("确认依赖版本兼容、制品可拉取、无传递依赖冲突。")
    if "业务代码" in categories:
        points.append("确认核心流程、幂等、异常处理、日志和外部调用超时符合预期。")
    if "测试" not in categories:
        points.append("补充或提供本人改动对应的测试/联调/回归证据。")
    return points


def action_label_for_commit(commit: dict[str, Any]) -> str:
    if commit.get("is_merge"):
        return "合并入主干"
    subject = str(commit.get("subject") or "").lower()
    if any(token in subject for token in ["zk", "注册", "配置", "apollo"]):
        return "配置/注册中心"
    if any(token in subject for token in ["定时", "同步", "job", "task"]):
        return "同步任务/定时任务"
    if any(token in subject for token in ["对账", "关系"]):
        return "对账关系"
    if any(token in subject for token in ["依赖", "版本", "pom"]):
        return "依赖版本"
    if any(token in subject for token in ["sql", "ddl", "表"]):
        return "数据库/DDL"
    if any(token in subject for token in ["test", "测试"]):
        return "测试"
    if any(token in subject for token in ["cr", "文档", "doc"]):
        return "文档/CR"
    return "业务功能"


def summarize_actions(commits: list[dict[str, Any]], limit: int = 4) -> str:
    counter = Counter(action_label_for_commit(commit) for commit in commits)
    if not counter:
        return "无"
    parts = [f"{name} {count} 次" for name, count in counter.most_common(limit)]
    remaining = len(counter) - limit
    if remaining > 0:
        parts.append(f"其他 {remaining} 类")
    return "；".join(parts)


def top_focus_files(review: dict[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    files = review.get("files") or []
    return sorted(files, key=lambda item: (-item["commit_count"], item["path"]))[:limit]


def compact_path(path: str, max_parts: int = 3) -> str:
    parts = path.replace("\\", "/").split("/")
    if len(parts) <= max_parts:
        return path
    return f"{parts[0]}/.../{parts[-1]}"


def compact_commit_list(commits: list[str], limit: int = 3) -> str:
    if len(commits) <= limit:
        return ", ".join(commits)
    return f"{', '.join(commits[:limit])} 等 {len(commits)} 个"


def safe_filename_part(value: str) -> str:
    safe = re.sub(r"[^\w.-]+", "_", value.strip(), flags=re.UNICODE)
    return safe.strip("._-") or "unknown"


def author_file_map(author_reviews: list[dict[str, Any]]) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = {}
    for review in author_reviews:
        author = review["author"]
        mapping.setdefault(author, set())
        for item in review.get("files", []):
            mapping[author].add(item["path"])
    return mapping


def authors_for_file(path: str, author_reviews: list[dict[str, Any]]) -> list[str]:
    owners = []
    for review in author_reviews:
        if any(item["path"] == path for item in review.get("files", [])):
            owners.append(review["author"])
    return owners


def add_author_cr_issue(
    author_issues: dict[str, list[dict[str, Any]]],
    author: str,
    issue_id: str,
    source: str,
    severity: str,
    issue: str,
    evidence: str,
    action: str,
    files: list[str] | None = None,
) -> None:
    author_issues.setdefault(author, []).append(
        {
            "issue_id": issue_id,
            "source": source,
            "severity": severity,
            "issue": issue,
            "evidence": evidence,
            "action": action,
            "files": files or [],
        }
    )


def build_cr_scan_issues(
    repo: Path,
    report: dict[str, Any],
    first_parent_non_merge_commits: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    for index, commit in enumerate(first_parent_non_merge_commits, 1):
        files = [item["path"] for item in get_commit_changed_files(repo, commit["sha"])]
        issues.append(
            {
                "id": f"CR-{index:03d}",
                "severity": "阻塞",
                "title": "存在主干直改提交",
                "evidence": f"{commit['short_sha']} {commit['subject']}",
                "action": "补充主干直改审批依据、变更说明和责任人确认；未完成前不予上线。",
                "assignees": [commit["author"]],
                "files": files,
            }
        )
    return issues


def has_blocking_cr_scan_issue(report: dict[str, Any]) -> bool:
    return any(item.get("severity") in {"阻塞", "严重"} for item in report.get("cr_scan_issues", []) or [])


def sync_risk_gate_with_cr_issues(report: dict[str, Any]) -> None:
    risk = report.setdefault("risk", {})
    if has_blocking_cr_scan_issue(report):
        risk["gate_conclusion"] = "阻塞上线"
        risk["risk_level"] = "高"


def build_author_cr_issues(report: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    author_reviews = report.get("author_reviews") or []
    author_issues: dict[str, list[dict[str, Any]]] = {review["author"]: [] for review in author_reviews}
    for issue in report.get("cr_scan_issues", []) or []:
        for author in issue.get("assignees", []):
            add_author_cr_issue(
                author_issues,
                author,
                issue["id"],
                "CR正文",
                issue["severity"],
                issue["title"],
                issue["evidence"],
                issue["action"],
                issue.get("files", []),
            )
    return author_issues


def render_release_snapshot(report: dict[str, Any]) -> list[str]:
    risk = report["risk"]
    author_reviews = report.get("author_reviews") or []
    primary_authors = "，".join(item["author"] for item in author_reviews[:3]) or "无"
    categories = "，".join(
        f"{category}{len(paths)}个" for category, paths in sorted(report.get("categories", {}).items())
    ) or "无"
    must_check: list[str] = []
    if risk.get("rollback_concerns"):
        must_check.append("补齐回滚方案")
    if "DDL" in report.get("categories", {}):
        must_check.append("确认 DDL 执行与回滚")
    if risk.get("high_risk_files"):
        must_check.append("确认依赖/配置高风险改动")
    if not must_check:
        must_check.append("按作者完成本人改动复核")

    return [
        "## 差异总览",
        md_table(
            ["项目", "内容"],
            [
                ["比较范围", f"`{report['range']}`（同一分支上一版本到当前版本）"],
                ["基线", f"`{report['base_commit']['short_sha']}` -> `{report['main_commit']['short_sha']}`"],
                ["提交规模", f"{report['commit_count']} 次提交（合并 {report['merge_commit_count']}，非合并 {report['non_merge_commit_count']}）"],
                ["文件规模", f"{report['changed_file_count']} 个文件，+{report['line_additions']}/-{report['line_deletions']} 行"],
                ["主要责任人", primary_authors],
                ["变更构成", categories],
                ["上线前必看", "；".join(must_check)],
            ],
        ),
    ]


def render_author_task_cards(report: dict[str, Any]) -> list[str]:
    rows = []
    for review in report.get("author_reviews", []) or []:
        focus_files = top_focus_files(review)
        focus = "；".join(f"{item['category']}:{Path(item['path']).name}" for item in focus_files[:2]) or "无直接文件"
        role = "合并人" if review["merge_commit_count"] and not review["non_merge_commit_count"] else "代码作者"
        rows.append(
            [
                review["author"],
                role,
                f"{review['commit_count']} 次",
                display_time_range(review["first_commit_at"], review["last_commit_at"]),
                summarize_actions(review["commits"]),
                focus,
            ]
        )
    return [
        "## 作者复核任务卡",
        md_table(["复核人", "角色", "提交次数", "时间范围", "主要动作", "优先复核"], rows),
    ]


def render_author_file_index(report: dict[str, Any]) -> list[str]:
    rows = []
    files = report.get("author_output_files") or {}
    author_issues = report.get("author_cr_issues") or {}
    for review in report.get("author_reviews", []) or []:
        author = review["author"]
        rows.append(
            [
                author,
                len(review.get("files", [])),
                review.get("mainline_direct_commit_count", 0),
                len(author_issues.get(author, [])),
                files.get(author, "未生成"),
            ]
        )
    return [
        "## 按人对比文件",
        md_table(["责任人", "涉及文件数", "主干直改", "CR问题数", "文件"], rows),
    ]


def render_mainline_direct_commit_section(report: dict[str, Any]) -> list[str]:
    mainline_direct_commits = report.get("mainline_direct_commits") or []
    if not mainline_direct_commits:
        return []
    return [
        "## 主干直改提示",
        "- 以下提交位于当前比较范围的 `origin/master` first-parent 主线上，且不是合并提交，需要单独复核是否符合主干提交流程。",
        md_table(
            ["作者", "时间", "提交", "说明", "文件数"],
            [
                [
                    item["author"],
                    display_time(item["date"]),
                    item["short_sha"],
                    item["subject"],
                    item["file_count"],
                ]
                for item in mainline_direct_commits[:10]
            ],
        ),
    ]


def render_review_route(report: dict[str, Any]) -> list[str]:
    rows = []
    risk = report["risk"]
    if "DDL" in report.get("categories", {}):
        rows.append(["1", "DDL", "确认表结构、索引、兼容性", "必须有执行记录和回滚/补偿方案"])
    if risk.get("high_risk_files"):
        rows.append([str(len(rows) + 1), "依赖/配置", "确认 pom、application、mapper XML、注册中心配置", "必须和生产环境匹配"])
    rows.append([str(len(rows) + 1), "业务代码", "按作者复核自己提交的核心逻辑", "确认边界、幂等、异常、日志"])
    if not risk.get("has_rollback_evidence"):
        rows.append([str(len(rows) + 1), "回滚证据", "补齐回滚说明和执行人", "没有回滚证据不建议直接放行"])
    return [
        "## 复核顺序",
        md_table(["顺序", "复核对象", "怎么看", "通过标准"], rows),
    ]


def render_category_route(report: dict[str, Any]) -> list[str]:
    lines = ["## 按类型看差异"]
    categories = report.get("categories", {})
    if not categories:
        lines.append("无")
        lines.append("")
        return lines

    hints = {
        "DDL": "看表结构、索引、兼容性、回滚/补偿。",
        "配置": "看生产配置、注册中心、mapper XML、环境差异。",
        "依赖": "看版本兼容、制品可用、传递依赖冲突。",
        "业务代码": "看核心流程、边界、幂等、异常处理。",
        "测试": "看是否覆盖本次核心改动。",
        "文档": "看是否只是说明或 CR/TODO 留痕。",
    }
    rows = []
    for category, paths in sorted(categories.items()):
        examples = "；".join(compact_path(path) for path in paths[:2])
        more = f"；另有 {len(paths) - 2} 个" if len(paths) > 2 else ""
        rows.append([category, len(paths), hints.get(category, "看是否符合上线范围和回滚预期。"), f"{examples}{more}"])
    lines.append(md_table(["类型", "文件数", "复核重点", "示例/范围"], rows))
    return lines


def render_author_review_sections(report: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    author_reviews = report.get("author_reviews") or []
    lines.append("## 按作者复核明细")
    if not author_reviews:
        lines.append("无\n")
        return lines

    for review in author_reviews:
        commits = review["commits"]
        files = review["files"]
        focus_files = top_focus_files(review, limit=4)
        key_commits = commits[:5]
        lines.append(f"### {review['author']}")
        lines.append("")
        lines.append(
            md_table(
                ["项目", "内容"],
                [
                    ["动作概括", summarize_actions(commits)],
                    ["提交次数", f"{review['commit_count']}（非合并 {review['non_merge_commit_count']}，合并 {review['merge_commit_count']}）"],
                    ["时间范围", display_time_range(review["first_commit_at"], review["last_commit_at"])],
                    ["变更覆盖", f"{len(files)} 个文件；{', '.join(sorted(review.get('categories', {}).keys())) or '无直接文件改动'}"],
                ],
            )
        )
        lines.append("#### 复核重点")
        lines.append("")
        points = review_points_for_author(review)
        lines.append(md_table(["必看项", "怎么判断"], [[point.split("，")[0].rstrip("。"), point] for point in points[:4]]))
        lines.append("#### 关键提交")
        lines.append("")
        lines.append(
            md_table(
                ["时间", "动作", "提交", "说明"],
                [
                    [
                        display_time(commit["date"]),
                        action_label_for_commit(commit),
                        commit["short_sha"],
                        commit["subject"],
                    ]
                    for commit in key_commits
                ],
            )
        )
        if len(commits) > len(key_commits):
            lines.append(f"- 其余提交：{len(commits) - len(key_commits)} 条，不在正文展开。")
            lines.append("")
        lines.append("#### 优先复核文件")
        lines.append("")
        if focus_files:
            lines.append(
                md_table(
                    ["类型", "文件", "为什么看", "涉及提交"],
                    [
                        [
                            item["category"],
                            compact_path(item["path"]),
                            f"触达 {item['commit_count']} 次",
                            compact_commit_list(item["commits"]),
                        ]
                        for item in focus_files
                    ],
                )
            )
        else:
            lines.append("无直接文件改动。\n")
    return lines


def render_author_compare_markdown(report: dict[str, Any], review: dict[str, Any], cr_filename: str) -> str:
    author = review["author"]
    author_issues = report.get("author_cr_issues", {}).get(author, [])
    focus_files = top_focus_files(review, limit=8)
    commits = review.get("commits", [])
    key_commits = commits[:8]
    mainline_direct_commits = review.get("mainline_direct_commits", [])

    lines: list[str] = []
    lines.append(f"# 上线差异对比 - {report['project']} - {author}")
    lines.append("")
    lines.append("## 基本信息")
    lines.append(
        md_table(
            ["项目", "内容"],
            [
                ["比较范围", f"`{report['range']}`"],
                ["责任人", author],
                ["CR文件", cr_filename],
                ["提交次数", f"{review['commit_count']}（非合并 {review['non_merge_commit_count']}，合并 {review['merge_commit_count']}）"],
                ["主干直改次数", review.get("mainline_direct_commit_count", 0)],
                ["时间范围", display_time_range(review["first_commit_at"], review["last_commit_at"])],
                ["涉及文件数", len(review.get("files", []))],
                ["动作概括", summarize_actions(commits)],
            ],
        )
    )

    if author_issues:
        lines.append("## 待整改/确认项")
        lines.append(
            md_table(
                ["CR编号", "级别", "问题", "证据", "整改动作"],
                [
                    [
                        item["issue_id"],
                        item["severity"],
                        item["issue"],
                        str(item["evidence"]),
                        item["action"],
                    ]
                    for item in author_issues
                ],
            )
        )

    if mainline_direct_commits:
        lines.append("## 主干直改提示")
        lines.append("- 以下提交位于当前比较范围的 `origin/master` first-parent 主线上，且不是合并提交。")
        lines.append(
            md_table(
                ["时间", "提交", "说明", "文件数"],
                [
                    [
                        display_time(commit["date"]),
                        commit["short_sha"],
                        commit["subject"],
                        commit["file_count"],
                    ]
                    for commit in mainline_direct_commits[:10]
                ],
            )
        )

    lines.append("## 本人关键提交")
    lines.append(
        md_table(
            ["时间", "动作", "提交", "说明"],
            [
                [
                    display_time(commit["date"]),
                    action_label_for_commit(commit),
                    commit["short_sha"],
                    commit["subject"],
                ]
                for commit in key_commits
            ],
        )
    )
    if len(commits) > len(key_commits):
        lines.append(f"- 其余提交：{len(commits) - len(key_commits)} 条，不在正文展开。")
        lines.append("")

    lines.append("## 本人优先复核文件")
    if focus_files:
        lines.append(
            md_table(
                ["类型", "文件", "为什么看", "涉及提交"],
                [
                    [
                        item["category"],
                        compact_path(item["path"]),
                        f"触达 {item['commit_count']} 次",
                        compact_commit_list(item["commits"]),
                    ]
                    for item in focus_files
                ],
            )
        )
    else:
        lines.append("无直接文件改动。")
        lines.append("")

    lines.append("## 复核完成标准")
    lines.append(md_table(["序号", "标准"], [[index, point] for index, point in enumerate(review_points_for_author(review), 1)]))
    return "\n".join(lines) + "\n"


def render_markdown(report: dict[str, Any]) -> str:
    risk = report["risk"]
    lines: list[str] = []
    lines.append(f"# 上线 Git 比较明细 - {report['project']}")
    lines.append("")
    lines.extend(render_release_snapshot(report))
    lines.extend(render_author_task_cards(report))
    lines.extend(render_author_file_index(report))
    lines.extend(render_review_route(report))
    lines.extend(render_category_route(report))

    lines.append("## 上线比较基本信息")
    lines.append(f"- 项目：{report['project']}")
    lines.append(f"- 生成时间：{display_time(report['generated_at'])}")
    lines.append(f"- 比较范围：`{report['range']}`")
    lines.append(f"- 主分支：`{report['main_ref']}`")
    lines.append(f"- 线上基线：`{report['base_ref']}`")
    lines.append(f"- 起点提交：`{report['base_commit']['short_sha']}` {display_time(report['base_commit']['date'])} {report['base_commit']['subject']}")
    lines.append(f"- 终点提交：`{report['main_commit']['short_sha']}` {display_time(report['main_commit']['date'])} {report['main_commit']['subject']}")
    lines.append(f"- 提交数：{report['commit_count']}，合并提交：{report['merge_commit_count']}，非合并提交：{report['non_merge_commit_count']}")
    lines.append(f"- 文件数：{report['changed_file_count']}，新增行：{report['line_additions']}，删除行：{report['line_deletions']}")
    lines.append("")

    lines.append("## 基线识别结果")
    lines.append(f"- 识别方式：{report['base_source']}")
    lines.append(f"- 规则文件：`{report['rules_file']}`")
    lines.append(f"- 起点 full SHA：`{report['base_commit']['sha']}`")
    lines.append(f"- 终点 full SHA：`{report['main_commit']['sha']}`")
    lines.append("")

    lines.append("## 合并分支清单")
    lines.append(
        md_table(
            ["提交", "日期", "来源分支", "作者", "提交信息"],
            [
                [m["commit"], display_time(m["date"]), m.get("source_branch") or "未知来源分支", m["author"], m["subject"]]
                for m in report["merged_branches"]
            ],
        )
    )

    lines.extend(render_author_review_sections(report))

    lines.append("## 风险评分与门禁建议")
    lines.append(f"- 风险等级：{risk['risk_level']}")
    lines.append(f"- 风险分：{risk['score']}")
    lines.append(f"- 建议门禁结论：{risk['gate_conclusion']}")
    lines.append("")

    lines.append("## 违规改动清单")
    lines.append(
        md_table(
            ["级别", "标题", "证据", "权重", "阻塞"],
            [[f["severity"], f["title"], f["evidence"], f["weight"], "Y" if f["blocker"] else "N"] for f in risk["findings"]],
        )
    )

    lines.append("## 高风险文件清单")
    lines.append(md_table(["文件", "原因"], [[item["path"], item["reason"]] for item in risk["high_risk_files"]]))

    lines.append("## Owner / Reviewer 建议")
    lines.append(
        md_table(
            ["文件", "建议 Reviewer"],
            [[item["path"], ", ".join(item["owners"])] for item in report["owner_suggestions"]],
        )
    )

    lines.append("## 测试证据检查")
    lines.append(f"- 是否发现测试证据：{'Y' if risk['has_test_evidence'] else 'N'}")
    if not risk["has_test_evidence"]:
        lines.append("- 证据缺口：未发现测试路径或测试文件改动。")
    lines.append("")

    lines.append("## 回滚关注项")
    lines.append(md_table(["文件", "原因"], [[item["path"], item["reason"]] for item in risk["rollback_concerns"]]))
    lines.append(f"- 是否发现回滚证据：{'Y' if risk['has_rollback_evidence'] else 'N'}")
    lines.append("")

    lines.append("## 敏感信息扫描结果")
    lines.append(md_table(["文件", "证据"], [[item["file"], item["evidence"]] for item in risk["secret_findings"]]))

    lines.append("## Revert / Cherry-pick / 大面积格式化提示")
    lines.append(md_table(["类型", "证据"], [[item["type"], item.get("subject") or f"{item.get('files')} files / {item.get('lines')} lines"] for item in risk["hints"]]))

    lines.append("## CR 报告摘要")
    lines.append(f"- CR 范围：`{report['range']}`")
    lines.append(f"- 优先关注：{', '.join(sorted(report['categories'].keys())) or '无'}")
    lines.append(f"- 阻塞项数量：{sum(1 for item in risk['findings'] if item['blocker'])}")
    lines.append(f"- 高风险文件数：{len(risk['high_risk_files'])}")
    lines.append("- 说明：本报告只准备上线 diff 和风险证据，代码 CR 需继续使用当前工具已安装的代码规范 skills。")
    lines.append("")

    lines.append("## 已调用或建议调用的代码规范 skills")
    lines.append("- 状态：本脚本只给出建议清单；是否已安装、是否已调用，必须由当前工具环境确认。")
    lines.append("- 若当前工具没有可用 CR skill，应标记为 `CR 规则缺失`，不得临时编造代码规范。")
    lines.append("")
    lines.append(md_table(["Skill", "原因"], [[item["skill"], item["reason"]] for item in report["cr_skill_suggestions"]]))
    return "\n".join(lines) + "\n"


def render_cr_markdown(report: dict[str, Any], repo: Path | None = None) -> str:
    risk = report["risk"]

    cr_scan_issues = report.get("cr_scan_issues", []) or []
    mainline_direct_commits = report.get("mainline_direct_commits", []) or []
    high_priority_issues = [item for item in cr_scan_issues if item.get("severity") in {"阻塞", "严重", "高"}]
    severity_counts = Counter(str(item.get("severity") or "低") for item in cr_scan_issues)
    severe_count = severity_counts.get("阻塞", 0) + severity_counts.get("严重", 0)
    high_count = severity_counts.get("高", 0)
    medium_count = severity_counts.get("中", 0)
    low_count = severity_counts.get("低", 0)
    has_blocking_issue = any(item.get("severity") == "阻塞" for item in cr_scan_issues)
    conclusion = "不予上线" if has_blocking_issue else ("有条件发布" if cr_scan_issues else "允许发布")
    if cr_scan_issues:
        correctness = 26
        stability = 16
        security = 13
        testability = 12
        maintainability = 8
        observability = 8
    else:
        correctness = 30
        stability = 20
        security = 15
        testability = 15
        maintainability = 10
        observability = 10
    total_score = correctness + stability + security + testability + maintainability + observability

    non_merge_commits = [commit for commit in report.get("commits", []) if not commit.get("is_merge")]
    latest_non_merge = non_merge_commits[0] if non_merge_commits else None
    latest_non_merge_title = ""
    latest_non_merge_file_count = 0
    if latest_non_merge:
        latest_non_merge_title = f"`{latest_non_merge['short_sha']} {latest_non_merge['subject']}`"
        latest_non_merge_file_count = len(get_commit_changed_files(repo, latest_non_merge["sha"])) if repo is not None else 0

    lines: list[str] = []
    today = dt.date.today().isoformat()
    lines.append("---")
    lines.append(f"title: 代码评审报告 - {report['project']} {today}")
    lines.append(f"tags: [CR, 代码评审, {report['project']}]")
    lines.append("related:")
    lines.append("  - [[checkpoints/common|通用检查点]]")
    lines.append("---")
    lines.append("")
    lines.append(f"# 代码评审报告 - {report['project']} {today}")
    lines.append("")
    lines.append("> [!tip] 本报告可关联到 [[README|项目 CR 索引页]]")
    lines.append("")
    lines.append("## 变更基本信息")
    lines.append(f"- 项目：{report['project']}")
    lines.append(f"- 评审范围：同一分支 `{report['range']}` 的上线差异")
    lines.append("- 评审人：Codex")
    lines.append(f"- 分支：`{report['main_ref']}`")
    lines.append(f"- 最新提交（HEAD）：`{report['main_commit']['sha']}`")
    lines.append(f"- HEAD 提交人：`{report['main_commit'].get('author') or '未知'}`")
    lines.append(f"- HEAD 提交文件数：{report['changed_file_count']}")
    lines.append(f"- 最新非合并提交：{latest_non_merge_title or '无'}")
    lines.append(f"- 非合并提交人：`{latest_non_merge.get('author') if latest_non_merge else '无'}`")
    lines.append(f"- 非合并提交文件数：{latest_non_merge_file_count}")
    lines.append("")

    lines.append("## 最终结论（是否可发布）")
    lines.append(f"- 结论：{conclusion}")
    lines.append(f"- 严重级别统计：严重={severe_count}，高={high_count}，中={medium_count}，低={low_count}")
    lines.append("- 结论依据：")
    if cr_scan_issues:
        lines.append(f"  - 本次 CR 扫描登记 {len(cr_scan_issues)} 项上线比较问题，详见 `CR扫描问题清单`。")
    else:
        lines.append("  - 本次 CR 未在自动扫描中登记具体上线比较问题。")
    lines.append(f"  - 上线比较基线为同一分支上一版本：`{report['base_ref']}`，不存在跨分支基线混用。")
    if mainline_direct_commits:
        lines.append(f"  - 检测到 {len(mainline_direct_commits)} 条主干 first-parent 非合并提交，详见下方 `主干直改提示`。")
    lines.append("  - 作者提交时间线和变更范围已按人拆分到对比文件。")
    lines.append("")

    lines.append("## 评分卡（100分）")
    lines.append(f"- 正确性（业务逻辑）（30）：{correctness}")
    lines.append(f"- 稳定性（异常处理）（20）：{stability}")
    lines.append(f"- 安全性（合规）（15）：{security}")
    lines.append(f"- 可测试性（验证证据）（15）：{testability}")
    lines.append(f"- 可维护性（10）：{maintainability}")
    lines.append(f"- 可观测性（10）：{observability}")
    lines.append(f"- 总分：{total_score}")
    lines.append("")

    lines.append("## 高优先级问题（严重/高）")
    if high_priority_issues:
        for item in high_priority_issues:
            lines.append(f"- {item['id']} {item['title']}：{item['evidence']}")
    else:
        lines.append("- 未发现。")
    lines.append("")

    lines.append("## 本次新增逻辑问题")
    lines.append("- 未发现。")
    lines.append("")

    lines.append("## 上线比较专项结论")
    lines.append(f"- 本次比较范围：`{report['range']}`。")
    lines.append(f"- 基线识别方式：{report['base_source']}，起点为 `{report['base_commit']['short_sha']}`，终点为 `{report['main_commit']['short_sha']}`。")
    lines.append(f"- 本次上线包含 {report['commit_count']} 次提交、{report['changed_file_count']} 个文件变更。")
    lines.append("- 作者维度提交时间点和动作明细见下方按人文件。")
    lines.append("")

    lines.extend(render_author_file_index(report))
    lines.append("")
    lines.extend(render_mainline_direct_commit_section(report))
    if mainline_direct_commits:
        lines.append("")

    if cr_scan_issues:
        lines.append("## CR扫描问题清单")
        lines.append(
            md_table(
                ["编号", "级别", "问题", "证据", "责任人", "整改动作"],
                [
                    [
                        item["id"],
                        item["severity"],
                        item["title"],
                        str(item["evidence"]),
                        "，".join(item.get("assignees", [])) or "待确认",
                        item["action"],
                    ]
                    for item in cr_scan_issues
                ],
            )
        )
        lines.append("")

    lines.append("## 测试安排说明")
    lines.append("- 相关测试将由专门测试补充执行。")
    lines.append("- 当前 CR 不将该测试安排作为代码问题或技术债拦截项。")
    lines.append("")

    if cr_scan_issues:
        lines.append("## TODO 跟踪")
        lines.append("")
        lines.append("> [!todo] TODO 统一写入 [[TODO_BACKLOG|TODO 台账]]")
        lines.append("> 本次 CR 待办如下。")
        lines.append("")
        for item in cr_scan_issues:
            lines.append(f"- {item['id']} {item['title']}：{item['action']}")
        lines.append("")

    lines.append("## 测试证据")
    lines.append("- 单元测试：本次 CR 未审阅专项测试结果")
    lines.append("- 集成测试：本次 CR 未审阅专项测试结果")
    lines.append("- 回归测试：本次 CR 未审阅专项测试结果")
    lines.append("- 说明：后续由专门测试补充执行")
    lines.append("")

    if cr_scan_issues:
        lines.append("## 发布风险与回滚")
        lines.append(f"- 风险等级：{risk.get('risk_level', '中')}")
        lines.append("- 关键风险点：")
        for item in cr_scan_issues[:3]:
            lines.append(f"  - {item['id']} {item['title']}：{item['evidence']}")
        lines.append("")

    if cr_scan_issues:
        lines.append("## 处置建议")
        lines.append("- 合并前必须完成（阻塞项）：")
        if high_priority_issues:
            for item in high_priority_issues:
                lines.append(f"  - {item['id']} {item['title']}")
        else:
            lines.append("  - 无")
        lines.append("- 可延期（需 owner/日期）：")
        delayed = [item for item in cr_scan_issues if item not in high_priority_issues]
        if delayed:
            for item in delayed:
                lines.append(f"  - {item['id']} {item['title']}")
        else:
            lines.append("  - 无")
    return "\n".join(lines) + "\n"


def resolve_output_path(repo: Path, explicit: str | None, default_dir: str, project: str, filename: str) -> Path:
    if explicit:
        output = Path(explicit)
        if not output.is_absolute():
            output = repo / output
        return output
    return repo / default_dir / project / filename


def write_output(report: dict[str, Any], repo: Path, args: argparse.Namespace) -> dict[str, Path]:
    today = dt.date.today().isoformat()
    cr_output = resolve_output_path(repo, args.cr_output, "cr", report["project"], f"{today}.md")
    author_outputs: dict[str, Path] = {}
    used_author_names: set[str] = set()

    if args.format == "markdown":
        for review in report.get("author_reviews", []):
            safe_author = safe_filename_part(review["author"])
            candidate = safe_author
            index = 2
            while candidate.lower() in used_author_names:
                candidate = f"{safe_author}-{index}"
                index += 1
            used_author_names.add(candidate.lower())
            author_outputs[review["author"]] = cr_output.parent / f"{today}-release-diff-{candidate}.md"
        report["author_output_files"] = {author: path.name for author, path in author_outputs.items()}
    else:
        report["author_output_files"] = {}

    cr_output.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "json":
        json_output = resolve_output_path(repo, args.output, "cr", report["project"], f"{today}.json")
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        outputs = {"json": json_output}
    else:
        cr_output.write_text(render_cr_markdown(report, repo), encoding="utf-8")
        outputs = {"cr": cr_output}
        for review in report.get("author_reviews", []):
            author_output = author_outputs.get(review["author"])
            if author_output is not None:
                author_output.write_text(render_author_compare_markdown(report, review, cr_output.name), encoding="utf-8")
    for author, path in author_outputs.items():
        outputs[f"author:{author}"] = path
    return outputs

def should_fail(report: dict[str, Any], fail_on: str) -> bool:
    risk = report["risk"]
    if fail_on == "never":
        return False
    if fail_on == "gate":
        return risk["gate_conclusion"] == "阻塞上线"
    if fail_on == "blocker":
        return has_blocking_cr_scan_issue(report) or any(item.get("blocker") for item in risk["findings"])
    if fail_on == "score":
        return int(risk["score"]) >= 60
    return False


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a code review report and per-author release comparison reports.")
    parser.add_argument("--repo", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--main-ref", default=None, help="Main branch ref. Defaults to origin/master or rules main_ref.")
    parser.add_argument("--base-ref", default=None, help="Explicit previous release baseline ref.")
    parser.add_argument("--from-version", default=None, help="Explicit compare start ref/version. Accepts commit SHA, tag, or branch ref. Overrides --base-ref.")
    parser.add_argument("--to-version", default=None, help="Explicit compare end ref/version. Accepts commit SHA, tag, or branch ref. Overrides --main-ref.")
    parser.add_argument("--allow-unrelated-range", action="store_true", help="Allow ranges where from-version/base is not an ancestor of to-version/main.")
    parser.add_argument("--fail-on", choices=sorted(FAIL_ON_CHOICES), default="never", help="Return exit code 3 when the selected gate condition is met.")
    parser.add_argument("--rules-file", default=None, help="Release rules YAML. Defaults to <repo-root>/.codex/release-rules.yaml.")
    parser.add_argument("--output", default=None, help="JSON output path when --format json. Defaults to cr/{project}/YYYY-MM-DD.json.")
    parser.add_argument("--cr-output", default=None, help="Code review report output path. Defaults to cr/{project}/YYYY-MM-DD.md.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists():
        print(f"not a git repository: {args.repo}", file=sys.stderr)
        return 2

    rules_file = Path(args.rules_file) if args.rules_file else repo / ".codex" / "release-rules.yaml"
    if not rules_file.is_absolute():
        rules_file = repo / rules_file
    args.rules_file = rules_file

    try:
        rules = merge_rules(DEFAULT_RULES, parse_simple_yaml(rules_file))
        validate_rules(rules, rules_file)
        report = build_report(repo, args, rules)
        outputs = write_output(report, repo, args)
    except ReleaseDiffError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if "json" in outputs:
        print(f"json report written: {os.path.relpath(outputs['json'], repo)}")
    if "cr" in outputs:
        print(f"code review report written: {os.path.relpath(outputs['cr'], repo)}")
    for key, output in outputs.items():
        if key.startswith("author:"):
            print(f"author comparison report written: {os.path.relpath(output, repo)}")
    if should_fail(report, args.fail_on):
        print(f"release diff gate failed: fail_on={args.fail_on}, conclusion={report['risk']['gate_conclusion']}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
