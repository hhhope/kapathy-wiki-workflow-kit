#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_content_enrichment import build_enrichment_preview


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview wiki content frontmatter enrichment.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    payload = build_enrichment_preview(Path(args.root).resolve())
    payload["generated_at"] = datetime.now(timezone.utc).isoformat()
    payload["mode"] = "preview"
    payload["entries"] = payload["entries"][: max(0, args.limit)]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
