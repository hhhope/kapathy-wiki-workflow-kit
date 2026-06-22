## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Treat graphify as a code-topology layer, not a durable truth source
- Use OpenSpec for process questions such as proposal/design/tasks/progress
- Use Lore first for durable rules, pitfalls, principles, and stable boundaries
- Use graphify when the question is about code entry points, neighbors, bridges, or likely structure paths
- For mixed rule + code questions, use Lore first and graphify second
- Before answering code-structure questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` to keep the graph current
