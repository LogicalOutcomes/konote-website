import tempfile
from pathlib import Path

from content_loader import load_content


def test_load_content_reads_markdown_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page1.md").write_text(
            "---\ntitle: Test\n---\n\n# Hello\n\nSome content.", encoding="utf-8"
        )
        Path(tmpdir, "page2.md").write_text(
            "---\ntitle: Other\n---\n\n# World\n\nMore content.", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "# Hello" in result
        assert "Some content." in result
        assert "# World" in result
        assert "More content." in result


def test_load_content_strips_frontmatter():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page.md").write_text(
            "---\ntitle: Secret\ndescription: Hidden\n---\n\n# Visible", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "title: Secret" not in result
        assert "# Visible" in result


def test_load_content_includes_source_filename():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "features.md").write_text(
            "---\ntitle: Features\n---\n\n# Features page", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "features.md" in result


def test_load_content_handles_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = load_content(tmpdir)
        assert result == ""


def test_load_content_skips_non_markdown_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page.md").write_text("---\ntitle: A\n---\n\nContent", encoding="utf-8")
        Path(tmpdir, "image.png").write_bytes(b"\x89PNG")
        result = load_content(tmpdir)
        assert "Content" in result
        assert "PNG" not in result
