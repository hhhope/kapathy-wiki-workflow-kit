"""Static acceptance checks for the R&D digital-employee H5."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "wiki/reports/rd-digital-employee-profile-v1-h5.html"
EXPECTED_PAGE_IDS = {f"page-{number:02d}" for number in range(1, 7)}
REQUIRED_PHRASES = (
    "Agent 是什么",
    "研发 Agent",
    "Orchestration",
    "SOP",
    "状态机",
    "Human on the Loop",
    "A2",
    "A3",
    "使用场景",
    "如何考核",
    "数字员工的一天",
)
RESOURCE_ATTRIBUTES = {
    "audio": ("src",),
    "embed": ("src",),
    "iframe": ("src",),
    "img": ("src",),
    "image": ("href", "xlink:href"),
    "object": ("data",),
    "script": ("src",),
    "source": ("src",),
    "track": ("src",),
    "use": ("href", "xlink:href"),
    "video": ("src",),
}
RESOURCE_LINK_RELS = {"icon", "manifest", "mask-icon", "modulepreload", "preload", "stylesheet"}


class H5Parser(HTMLParser):
    """Collect only the structural data the static contract needs."""

    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.chapters: list[str | None] = []
        self.content_pages: list[str | None] = []
        self.stylesheets: list[str] = []
        self.scripts: list[str] = []
        self.images: list[str] = []
        self.resource_urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        attributes = dict(attrs)
        if "data-chapter" in attributes:
            self.chapters.append(attributes["data-chapter"])
        if "data-content-page" in attributes:
            self.content_pages.append(attributes.get("id"))
        if tag == "link" and "stylesheet" in (attributes.get("rel") or "").lower():
            if attributes.get("href"):
                self.stylesheets.append(attributes["href"])
        if tag == "link":
            rels = set((attributes.get("rel") or "").lower().split())
            if attributes.get("href") and rels & RESOURCE_LINK_RELS:
                self.resource_urls.append(attributes["href"])
        else:
            for attribute in RESOURCE_ATTRIBUTES.get(tag, ()):
                if attributes.get(attribute):
                    self.resource_urls.append(attributes[attribute])
        if tag == "script" and attributes.get("src"):
            self.scripts.append(attributes["src"])
        if tag == "img" and attributes.get("src"):
            self.images.append(attributes["src"])


def is_local_relative(resource: str) -> bool:
    """Return whether a resource has no scheme, host, or root-relative path."""

    parsed = urlparse(resource)
    return not parsed.scheme and not parsed.netloc and not resource.startswith(("/", "\\"))


def is_external_http_resource(resource: str) -> bool:
    """Return whether a resource uses HTTP(S), including protocol-relative URLs."""

    normalized = resource.strip()
    return normalized.startswith("//") or urlparse(normalized).scheme.lower() in {"http", "https"}


def main() -> int:
    if not HTML_PATH.is_file():
        print("FAIL: missing HTML")
        return 1

    html = HTML_PATH.read_text(encoding="utf-8")
    parser = H5Parser()
    parser.feed(html)
    parser.close()
    failures: list[str] = []

    if len(parser.chapters) != 2:
        failures.append(f"expected 2 data-chapter elements, found {len(parser.chapters)}")
    if len(parser.content_pages) != 6:
        failures.append(
            f"expected 6 data-content-page elements, found {len(parser.content_pages)}"
        )
    if set(parser.content_pages) != EXPECTED_PAGE_IDS:
        failures.append("content-page IDs must be page-01 through page-06")
    for tag in ("main", "nav", "section"):
        if tag not in parser.tags:
            failures.append(f"missing <{tag}>")

    if not parser.images:
        failures.append("missing infographic image")
    else:
        for image in parser.images:
            if not is_local_relative(image):
                failures.append(f"infographic image is not local relative: {image}")
            elif not (HTML_PATH.parent / image).is_file():
                failures.append(f"missing infographic image: {image}")

    for label, resources in (("CSS", parser.stylesheets), ("JS", parser.scripts)):
        if not resources:
            failures.append(f"missing local {label}")
        for resource in resources:
            if not is_local_relative(resource):
                failures.append(f"{label} is not local relative: {resource}")

    for resource in parser.resource_urls:
        if is_external_http_resource(resource):
            failures.append(f"external resource dependency: {resource}")
    for phrase in REQUIRED_PHRASES:
        if phrase not in html:
            failures.append(f"missing required phrase: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: rd-digital-employee-profile-v1-h5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
