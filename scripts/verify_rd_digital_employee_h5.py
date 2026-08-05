"""Static acceptance checks for the R&D digital-employee H5."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "wiki/reports/rd-digital-employee-profile-v1-h5.html"
EXPECTED_PAGE_IDS = {f"page-{number:02d}" for number in range(1, 7)}
REQUIRED_PHRASES = (
    "Agent 是什么",
    "固定工作流",
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
    "video": ("src", "poster"),
}
RESOURCE_LINK_RELS = {"icon", "manifest", "mask-icon", "modulepreload", "preload", "stylesheet"}
CSS_URL_PATTERN = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
CSS_IMPORT_PATTERN = re.compile(r"@import\s+(['\"])(.*?)\1", re.IGNORECASE)


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
        self.inline_styles: list[str] = []
        self._in_style_tag = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        attributes = dict(attrs)
        if attributes.get("style"):
            self.inline_styles.append(attributes["style"])
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
            if tag in {"img", "source"} and attributes.get("srcset"):
                self.resource_urls.extend(srcset_urls(attributes["srcset"]))
        if tag == "script" and attributes.get("src"):
            self.scripts.append(attributes["src"])
        if tag == "img" and attributes.get("src"):
            self.images.append(attributes["src"])
        if tag == "style":
            self._in_style_tag = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._in_style_tag = False

    def handle_data(self, data: str) -> None:
        if self._in_style_tag:
            self.inline_styles.append(data)


def is_local_relative(resource: str) -> bool:
    """Return whether a resource has no scheme, host, or root-relative path."""

    normalized = resource.strip()
    parsed = urlparse(normalized)
    return not parsed.scheme and not parsed.netloc and not normalized.startswith(("/", "\\"))


def is_external_http_resource(resource: str) -> bool:
    """Return whether a resource uses HTTP(S), including protocol-relative URLs."""

    normalized = resource.strip()
    return normalized.startswith("//") or urlparse(normalized).scheme.lower() in {"http", "https"}


def srcset_urls(srcset: str) -> list[str]:
    """Extract image candidate URLs without treating data-URL commas as separators."""

    urls: list[str] = []
    position = 0
    while position < len(srcset):
        while position < len(srcset) and srcset[position] in " ,\t\n\r\f":
            position += 1
        start = position
        while position < len(srcset) and not srcset[position].isspace():
            position += 1
        if start < position:
            urls.append(srcset[start:position].rstrip(","))
        while position < len(srcset) and srcset[position] != ",":
            position += 1
        if position < len(srcset):
            position += 1
    return urls


def css_urls(css: str) -> list[str]:
    """Return URLs used by CSS url() and quoted @import rules."""

    urls = [match.group(2).strip() for match in CSS_URL_PATTERN.finditer(css)]
    urls.extend(match.group(2).strip() for match in CSS_IMPORT_PATTERN.finditer(css))
    return urls


class LocalResourceError(ValueError):
    """Report a local resource that is missing or outside the report boundary."""


def resolve_local_resource(base: Path, report_root: Path, resource: str) -> Path | None:
    """Resolve one local URL canonically and constrain it to the report root."""

    decoded_path = unquote(urlparse(resource.strip()).path)
    if not decoded_path:
        # Same-document fragments (for example SVG <use href="#icon">) do not load a file.
        return None
    try:
        allowed_root = report_root.resolve(strict=True)
        candidate = (base / decoded_path).resolve(strict=False)
        candidate.relative_to(allowed_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise LocalResourceError(
            f"local resource escapes report root: {resource}"
        ) from error
    if not candidate.is_file():
        raise LocalResourceError(f"missing local resource: {resource}")
    return candidate


def validate_resource(
    resource: str,
    *,
    base: Path,
    report_root: Path,
    failures: list[str],
) -> Path | None:
    """Validate a loading resource and return its canonical local file when present."""

    if is_external_http_resource(resource):
        failures.append(f"external resource dependency: {resource}")
        return None
    if not is_local_relative(resource):
        return None
    try:
        return resolve_local_resource(base, report_root, resource)
    except LocalResourceError as error:
        failures.append(str(error))
        return None


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

    for label, resources in (("CSS", parser.stylesheets), ("JS", parser.scripts)):
        if not resources:
            failures.append(f"missing local {label}")
        for resource in resources:
            if not is_local_relative(resource):
                failures.append(f"{label} is not local relative: {resource}")

    report_root = HTML_PATH.parent
    resolved_resources: dict[str, Path] = {}
    for resource in dict.fromkeys(parser.resource_urls):
        resolved = validate_resource(
            resource,
            base=HTML_PATH.parent,
            report_root=report_root,
            failures=failures,
        )
        if resolved is not None:
            resolved_resources[resource] = resolved
    for css in parser.inline_styles:
        for resource in css_urls(css):
            validate_resource(
                resource,
                base=HTML_PATH.parent,
                report_root=report_root,
                failures=failures,
            )
    for stylesheet in parser.stylesheets:
        if not is_local_relative(stylesheet):
            continue
        stylesheet_path = resolved_resources.get(stylesheet)
        if stylesheet_path is None:
            continue
        for resource in css_urls(stylesheet_path.read_text(encoding="utf-8")):
            validate_resource(
                resource,
                base=stylesheet_path.parent,
                report_root=report_root,
                failures=failures,
            )
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
