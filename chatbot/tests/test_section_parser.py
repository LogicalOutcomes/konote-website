import tempfile
from pathlib import Path

from section_parser import parse_file, parse_directory, ContentSection


def test_parse_file_extracts_sections():
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "features.md")
        md.write_text(
            "---\ntitle: Features\n---\n\n## Participant Records\n\nTrack participants.\n\n### Custom Fields\n\nDefine fields.\n\n## Outcome Plans\n\nDefine outcomes.",
            encoding="utf-8",
        )
        sections = parse_file(str(md), "en", "site")
        assert len(sections) >= 3
        titles = [s.section_heading for s in sections]
        assert "Participant Records" in titles
        assert "Custom Fields" in titles
        assert "Outcome Plans" in titles


def test_parse_file_sets_metadata():
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "security.md")
        md.write_text(
            "---\ntitle: Security & Privacy\n---\n\n## Encryption\n\nAll data is encrypted.",
            encoding="utf-8",
        )
        sections = parse_file(str(md), "en", "site")
        s = sections[0]
        assert s.language == "en"
        assert s.source_type == "site"
        assert s.page_title == "Security & Privacy"
        assert s.page_url == "/en/security/"
        assert s.section_heading == "Encryption"


def test_parse_file_homepage():
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "_index.md")
        md.write_text(
            "---\ntitle: KoNote\n---\n\n## What is KoNote?\n\nA case management tool.",
            encoding="utf-8",
        )
        sections = parse_file(str(md), "en", "site")
        assert sections[0].page_url == "/en/"


def test_parse_directory_loads_all_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "a.md").write_text("---\ntitle: A\n---\n\n## S1\n\nContent A.", encoding="utf-8")
        Path(tmpdir, "b.md").write_text("---\ntitle: B\n---\n\n## S2\n\nContent B.", encoding="utf-8")
        sections = parse_directory(tmpdir, "fr", "site")
        assert len(sections) >= 2
        urls = {s.page_url for s in sections}
        assert "/fr/a/" in urls
        assert "/fr/b/" in urls


def test_parse_file_strips_frontmatter():
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "test.md")
        md.write_text("---\ntitle: Secret Title\ndescription: Hidden\n---\n\n## Visible\n\nContent here.", encoding="utf-8")
        sections = parse_file(str(md), "en", "curated")
        for s in sections:
            assert "description: Hidden" not in s.body


def test_parse_file_generates_keywords():
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "features.md")
        md.write_text("---\ntitle: Features\n---\n\n## Participant Records\n\nEncrypted storage for participants.", encoding="utf-8")
        sections = parse_file(str(md), "en", "site")
        assert len(sections[0].keywords) > 0


def test_parse_file_no_headings_creates_single_section():
    """Files with no headings produce one section with the page title as heading."""
    with tempfile.TemporaryDirectory() as tmpdir:
        md = Path(tmpdir, "simple.md")
        md.write_text(
            "---\ntitle: Simple Page\n---\n\nJust some plain text without any headings.",
            encoding="utf-8",
        )
        sections = parse_file(str(md), "en", "site")
        assert len(sections) == 1
        assert sections[0].section_heading == "Simple Page"
        assert "Just some plain text" in sections[0].body


def test_parse_directory_missing_dir_returns_empty():
    sections = parse_directory("/nonexistent/path/", "en", "site")
    assert sections == []
