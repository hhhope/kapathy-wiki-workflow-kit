"""Check that inline copies preserve their source SVG's labels and node metadata."""

import re
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
INLINE = re.compile(r'<svg\b[^>]*data-diagram-source="([^"]+)"[^>]*>.*?</svg>', re.S)
SVG = "{http://www.w3.org/2000/svg}"


def signature(source):
    root = ElementTree.fromstring(source)
    labels = tuple("".join(node.itertext()) for node in root.iter(SVG + "text"))
    nodes = tuple(
        tuple(node.get(key) for key in ("data-node", "aria-label", "data-title", "data-detail"))
        for node in root.iter()
        if "atlas-diagram-node" in node.get("class", "").split()
    )
    return labels, nodes


def main():
    sources = {}
    copies = 0
    errors = []
    for page in sorted(ROOT.rglob("*.html")):
        for match in INLINE.finditer(page.read_text()):
            source = (page.parent / match[1]).resolve()
            if source not in sources:
                sources[source] = signature(source.read_text())
            if signature(match[0]) != sources[source]:
                errors.append(f"{page.relative_to(ROOT)}: {match[1]}")
            copies += 1
    if not copies or errors:
        raise SystemExit("Diagram sync failed:\n" + "\n".join(errors))
    print(f"{copies} inline copies match {len(sources)} SVG sources.")


if __name__ == "__main__":
    main()
