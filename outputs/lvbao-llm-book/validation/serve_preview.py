"""Serve the local course and resolve extensionless lesson URLs."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CoursePreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        translated = Path(super().translate_path(path))
        if not translated.exists() and not translated.suffix:
            html = translated.with_suffix(".html")
            if html.is_file():
                return str(html)
        return str(translated)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    handler = partial(CoursePreviewHandler, directory=str(root))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Course preview: http://localhost:{args.port}/", flush=True)
        server.serve_forever()
