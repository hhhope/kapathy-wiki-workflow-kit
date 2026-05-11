# Design

## Decision

Keep the repo-local marketplace install flow, but make the plugin package match
Codex's local marketplace shape:

```json
{"source": "local", "path": "./plugins/report-wiki-portfolio"}
```

The plugin root is now `plugins/report-wiki-portfolio/`, with its own
`.codex-plugin/plugin.json` and `commands/*.md`. This follows the same shape as
the local curated plugin marketplace, where every plugin entry points at a child
directory under `./plugins/`.

## Validation

Validation will cover:

- contract test failure before implementation, proving `"."`, `"./"`, and
  `"./."` are not accepted expectations for this repo-local plugin
- JSON parse checks for `.agents/plugins/marketplace.json`
- targeted marketplace and command tests
- `openspec validate fix-repo-plugin-local-source-path --strict`
- runtime loader evidence checks from `~/.codex/log/codex-tui.log`

## Boundary

This fix only repairs discovery of the existing repo plugin and moves the plugin
package into Codex's expected marketplace directory shape. It does not add
plugin authentication, new command behavior, new wiki runtime capabilities, or
any publish/archive automation.
