from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

try:
    import jsonschema
except ImportError:  # pragma: no cover - fallback is for minimal environments.
    jsonschema = None


DEFAULT_SCHEMA = {
    "type": "object",
    "properties": {
        "settings": {
            "type": "object",
            "properties": {"oversized_hunk_line_threshold": {"type": "integer", "minimum": 1}},
            "additionalProperties": True,
        },
        "rules": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["match", "create_checks"],
                "properties": {
                    "title": {"type": "string"},
                    "match": {
                        "type": "object",
                        "properties": {"any": {"type": "array", "items": {"type": "string"}}},
                        "required": ["any"],
                    },
                    "create_checks": {
                        "type": "object",
                        "properties": {
                            "required": {"type": "array", "items": {"type": "string"}},
                            "conditional": {"type": "array", "items": {"type": "string"}},
                            "evidence": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["required"],
                    },
                },
            },
        },
    },
    "required": ["rules"],
}

DEFAULT_SETTINGS = {"oversized_hunk_line_threshold": 80}


class ConfigError(Exception):
    pass


@dataclass
class LoadedConfig:
    config: dict[str, Any]
    sources: list[str]
    config_hash: str


def ordered_union(base: list[str], extra: list[str]) -> list[str]:
    merged = list(base)
    for item in extra:
        if item not in merged:
            merged.append(item)
    return merged


def _read_yaml(path: Path, required: bool) -> dict[str, Any] | None:
    if not path.exists():
        if required:
            raise ConfigError(f"missing required global rule configuration: {path}")
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"{path}: YAML root must be an object")
    return data


def _schema(skill_dir: Path) -> dict[str, Any]:
    path = skill_dir / "rules" / "rule-schema.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return DEFAULT_SCHEMA


def _overlay_schema(schema: dict[str, Any]) -> dict[str, Any]:
    relaxed = json.loads(json.dumps(schema))
    rule = relaxed["properties"]["rules"]["additionalProperties"]
    rule.pop("required", None)
    rule["properties"]["match"].pop("required", None)
    rule["properties"]["create_checks"].pop("required", None)
    return relaxed


def _validate_config(data: dict[str, Any], schema: dict[str, Any], source: Path, required: bool) -> None:
    active_schema = schema if required else _overlay_schema(schema)
    if jsonschema is not None:
        try:
            jsonschema.validate(data, active_schema)
        except jsonschema.ValidationError as exc:
            raise ConfigError(f"{source}: invalid rule configuration: {exc.message}") from exc
    if "rules" not in data or not isinstance(data["rules"], dict):
        raise ConfigError(f"{source}: missing rules object")


def _merge_rule(rule_id: str, base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = json.loads(json.dumps(base))
    merged["match"]["any"] = ordered_union(
        merged["match"].get("any", []),
        incoming.get("match", {}).get("any", []),
    )
    for key in ["required", "conditional", "evidence"]:
        baseline = merged["create_checks"].get(key, [])
        additions = incoming.get("create_checks", {}).get(key, [])
        overlap = set(additions) & set(baseline)
        if key == "required" and overlap and not set(baseline).issubset(set(additions)):
            raise ConfigError(f"rule {rule_id} weakens global required checks")
        merged["create_checks"][key] = ordered_union(baseline, additions)
    for key, value in incoming.items():
        if key not in {"match", "create_checks"}:
            merged[key] = value
    return merged


def load_rule_config(skill_dir: Path, repo_root: Path, project: str, case_id: str) -> LoadedConfig:
    schema = _schema(skill_dir)
    paths = [
        (skill_dir / "rules" / "global.yaml", True),
        (repo_root / "CR" / project / "cr-agent.yaml", False),
        (repo_root / "CR" / project / "cases" / case_id / "cr-agent.yaml", False),
    ]
    loaded: list[tuple[Path, dict[str, Any]]] = []
    for path, required in paths:
        data = _read_yaml(path, required)
        if data is None:
            continue
        _validate_config(data, schema, path, required)
        loaded.append((path, data))

    merged = {"settings": dict(DEFAULT_SETTINGS), "rules": {}}
    for path, data in loaded:
        merged["settings"].update(data.get("settings", {}))
        for rule_id, rule in data.get("rules", {}).items():
            if rule_id in merged["rules"]:
                merged["rules"][rule_id] = _merge_rule(rule_id, merged["rules"][rule_id], rule)
            else:
                merged["rules"][rule_id] = json.loads(json.dumps(rule))
    digest = hashlib.sha256(json.dumps(merged, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return LoadedConfig(merged, [str(path) for path, _ in loaded], digest)
