# Design

## Decision

Keep the existing local marketplace path:

```json
{"source": "local", "path": "./plugins/report-wiki-portfolio"}
```

Change only the installation policy:

```json
{"installation": "INSTALLED_BY_DEFAULT", "authentication": "ON_INSTALL"}
```

`AVAILABLE` is suitable for optional marketplace entries, but this repository
ships the wiki commands as repo-local operating surface. Default installation is
the smallest policy change that can make the plugin active without adding a
separate install workflow.

## Validation

Validation will cover:

- RED marketplace test against the old `AVAILABLE` policy
- GREEN targeted marketplace and command tests
- JSON parse checks for marketplace and plugin manifests
- `codex plugin marketplace add .` against the real user config
- `openspec validate install-repo-plugin-by-default --strict`

## Boundary

This change only changes activation policy. It does not add new slash commands,
rename commands, change command bodies, or modify wiki runtime scripts.
