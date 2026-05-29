# req-agent installer

Minimal installer package for the requirements-agent workflow.

## NPM-Style Install

From a local package directory:

```bash
npm install -g /path/to/req-agent-installer
req-agent-install /path/to/target-repo --mode codex-repo --verify
```

From a packed tarball:

```bash
npm install -g /path/to/report-wiki-req-agent-installer-0.1.0.tgz
req-agent-install /path/to/target-repo --mode codex-repo --verify
```

`codex-repo` is repo-local Codex installation. It writes `.codex/skills/req-*`
inside the target repository and also installs the required Python scripts,
taxonomy YAML, tests, and OpenSpec audit docs. A global Codex skill-only install
is not enough for this workflow because the skills depend on repo-local runtime
files.

## Direct Install

From the target repository root:

```bash
bash /path/to/req-agent-installer/install.sh .
```

To verify after install:

```bash
bash /path/to/req-agent-installer/install.sh . --verify
```

If the target already has different files at the same paths, the installer
stops before overwriting. To replace them intentionally:

```bash
bash /path/to/req-agent-installer/install.sh . --force
```

## What It Installs

- Codex skills: `.codex/skills/req-*`
- Requirements Python helpers: `scripts/*requirements*.py`
- Requirements taxonomy: `requirements/config/requirements-taxonomy.yaml`
- Verification tests: `tests/test_req_agent_skills.py`,
  `tests/test_requirements_analysis_agent.py`
- Audit docs: `openspec/changes/req-agent/`

## Requirements

- `python3`
- `PyYAML` importable as `yaml`
- Optional: `openspec` CLI for OpenSpec validation

Normal usage after install:

```text
$report-wiki-portfolio:req-agent <requirement material or question>
```

Do not ask users to call the worker skills or Python scripts directly as the
normal path.
