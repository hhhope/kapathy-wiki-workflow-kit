import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from typing import Callable

from scripts import verify_rd_digital_employee_h5 as verifier


class RdDigitalEmployeeH5VerifierTest(unittest.TestCase):
    def _run_fixture(
        self,
        extra_markup: str,
        stylesheet_css: str = "body {}",
        *,
        script_src: str = "app.js",
        create_script: bool = True,
        prepare: Callable[[Path, Path], None] | None = None,
    ) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as directory:
            fixture_root = Path(directory)
            report_root = fixture_root / "report"
            report_root.mkdir()
            html_path = report_root / "profile.html"
            (html_path.parent / "assets").mkdir()
            (html_path.parent / "assets" / "infographic.svg").write_text(
                "<svg />", encoding="utf-8"
            )
            (html_path.parent / "styles.css").write_text(stylesheet_css, encoding="utf-8")
            if create_script:
                script_path = html_path.parent / "app.js"
                script_path.write_text("// fixture", encoding="utf-8")
            if prepare is not None:
                prepare(fixture_root, report_root)
            pages = "".join(
                f'<section data-content-page id="page-{number:02d}"></section>'
                for number in range(1, 7)
            )
            html_path.write_text(
                "<html><head>"
                '<link rel="stylesheet" href="styles.css">'
                "</head><body><main>"
                '<section data-chapter="one"></section>'
                '<section data-chapter="two"></section>'
                f"{pages}"
                "</main><nav></nav>"
                '<img src="assets/infographic.svg">'
                f'<script src="{script_src}"></script>'
                f"<p>{' '.join(verifier.REQUIRED_PHRASES)}</p>{extra_markup}"
                "</body></html>",
                encoding="utf-8",
            )
            previous_path = verifier.HTML_PATH
            verifier.HTML_PATH = html_path
            output = io.StringIO()
            try:
                with contextlib.redirect_stdout(output):
                    result = verifier.main()
            finally:
                verifier.HTML_PATH = previous_path
            return result, output.getvalue()

    def test_existing_url_encoded_script_with_query_and_fragment_is_accepted(self) -> None:
        def prepare(_fixture_root: Path, report_root: Path) -> None:
            (report_root / "assets" / "app bundle.js").write_text(
                "// fixture", encoding="utf-8"
            )

        result, output = self._run_fixture(
            "",
            script_src="assets/app%20bundle.js?v=1#module",
            create_script=False,
            prepare=prepare,
        )

        self.assertEqual(0, result, output)
        self.assertIn("PASS: rd-digital-employee-profile-v1-h5", output)

    def test_missing_local_script_is_rejected(self) -> None:
        result, output = self._run_fixture("", create_script=False)

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: missing local resource: app.js", output)

    def test_url_encoded_traversal_escape_is_rejected(self) -> None:
        def prepare(fixture_root: Path, _report_root: Path) -> None:
            (fixture_root / "outside.js").write_text("// outside", encoding="utf-8")

        result, output = self._run_fixture(
            "",
            script_src="..%2Foutside.js",
            create_script=False,
            prepare=prepare,
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: local resource escapes report root: ..%2Foutside.js", output)

    def test_symlink_escape_is_rejected_when_supported(self) -> None:
        def prepare(fixture_root: Path, report_root: Path) -> None:
            outside = fixture_root / "outside"
            outside.mkdir()
            (outside / "app.js").write_text("// outside", encoding="utf-8")
            linked = report_root / "linked"
            try:
                linked.symlink_to(outside, target_is_directory=True)
            except (NotImplementedError, OSError) as symlink_error:
                try:
                    import _winapi

                    _winapi.CreateJunction(str(outside), str(linked))
                except (ImportError, OSError) as junction_error:
                    self.skipTest(
                        "directory-link creation is unavailable: "
                        f"symlink={symlink_error}; junction={junction_error}"
                    )

        result, output = self._run_fixture(
            "",
            script_src="linked/app.js",
            create_script=False,
            prepare=prepare,
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: local resource escapes report root: linked/app.js", output)

    def test_missing_local_resource_referenced_from_css_is_rejected(self) -> None:
        result, output = self._run_fixture(
            "", 'body { background-image: url("assets/missing.png"); }'
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: missing local resource: assets/missing.png", output)

    def test_ordinary_link_does_not_count_as_a_resource_dependency(self) -> None:
        result, output = self._run_fixture(
            '<a href="https://example.com/reference">reference</a>'
        )

        self.assertEqual(0, result, output)
        self.assertIn("PASS: rd-digital-employee-profile-v1-h5", output)

    def test_protocol_relative_video_is_rejected_as_external_resource(self) -> None:
        result, output = self._run_fixture('<video src="//cdn.example/video.mp4"></video>')

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: external resource dependency: //cdn.example/video.mp4", output)

    def test_srcset_candidates_are_checked_individually(self) -> None:
        result, output = self._run_fixture(
            '<img srcset="assets/infographic.svg 1x, //cdn.example/image.png 2x">'
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: external resource dependency: //cdn.example/image.png", output)

    def test_video_poster_is_checked_as_a_resource(self) -> None:
        result, output = self._run_fixture(
            '<video poster="https://cdn.example/poster.png"></video>'
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: external resource dependency: https://cdn.example/poster.png", output)

    def test_inline_style_attribute_and_style_block_external_urls_are_rejected(self) -> None:
        result, output = self._run_fixture(
            '<div style="background:url(https://cdn.example/card.png)"></div>'
            '<style>@import url("//cdn.example/fonts.css");</style>'
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: external resource dependency: https://cdn.example/card.png", output)
        self.assertIn("FAIL: external resource dependency: //cdn.example/fonts.css", output)

    def test_local_stylesheet_import_and_url_external_resources_are_rejected(self) -> None:
        result, output = self._run_fixture(
            "",
            '@import "https://cdn.example/theme.css"; '
            'body { background-image: url(//cdn.example/background.png); }',
        )

        self.assertEqual(1, result, output)
        self.assertIn("FAIL: external resource dependency: https://cdn.example/theme.css", output)
        self.assertIn("FAIL: external resource dependency: //cdn.example/background.png", output)

    def test_data_urls_in_inline_styles_are_not_external_resources(self) -> None:
        result, output = self._run_fixture(
            '<div style="background:url(data:image/svg+xml,%3Csvg/%3E)"></div>'
        )

        self.assertEqual(0, result, output)
        self.assertIn("PASS: rd-digital-employee-profile-v1-h5", output)


if __name__ == "__main__":
    unittest.main()
