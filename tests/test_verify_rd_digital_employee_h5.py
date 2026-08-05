import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts import verify_rd_digital_employee_h5 as verifier


class RdDigitalEmployeeH5VerifierTest(unittest.TestCase):
    def _run_fixture(
        self, extra_markup: str, stylesheet_css: str = "body {}"
    ) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as directory:
            html_path = Path(directory) / "profile.html"
            (html_path.parent / "assets").mkdir()
            (html_path.parent / "assets" / "infographic.svg").write_text(
                "<svg />", encoding="utf-8"
            )
            (html_path.parent / "styles.css").write_text(stylesheet_css, encoding="utf-8")
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
                '<script src="app.js"></script>'
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
