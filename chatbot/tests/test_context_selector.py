from section_parser import ContentSection
from context_selector import select_context, format_context, _slug_from_url


def _make_section(page_slug, heading, body="Test content.", lang="en"):
    return ContentSection(
        language=lang,
        source_type="site",
        page_title=page_slug.title(),
        page_url=f"/{lang}/{page_slug}/",
        section_heading=heading,
        parent_heading="",
        body=body,
        source_label=f"{page_slug.title()} — {heading}",
        keywords=[w.lower() for w in heading.split()],
    )


def test_current_page_prioritized():
    sections = [
        _make_section("features", "Records"),
        _make_section("security", "Encryption"),
    ]
    core = [_make_section("core", "Overview", "Core info.")]
    selected, sources = select_context(sections, "tell me about encryption", "/en/security/", "en", core)
    headings = [s.section_heading for s in selected]
    assert "Overview" in headings  # core always included
    assert "Encryption" in headings  # current page included


def test_core_always_included():
    sections = [_make_section("features", "Records")]
    core = [_make_section("core", "What KoNote Is", "Core overview.")]
    selected, _ = select_context(sections, "anything", "", "en", core)
    assert any(s.section_heading == "What KoNote Is" for s in selected)


def test_keyword_matching():
    sections = [
        _make_section("security", "Encryption"),
        _make_section("features", "Billing Note"),
        _make_section("faq", "Privacy Questions"),
    ]
    core = []
    selected, _ = select_context(sections, "how does encryption work?", "", "en", core)
    headings = [s.section_heading for s in selected]
    assert "Encryption" in headings


def test_sources_deduplicated():
    sections = [
        _make_section("features", "Section A"),
        _make_section("features", "Section B"),
    ]
    _, sources = select_context(sections, "test", "/en/features/", "en", [])
    urls = [s["url"] for s in sources]
    assert urls.count("/en/features/") == 1


def test_format_context():
    sections = [_make_section("features", "Records", "Track participants.")]
    text = format_context(sections)
    assert "Records" in text
    assert "Track participants." in text
    assert "/en/features/" in text


def test_slug_from_url():
    assert _slug_from_url("/en/features/") == "features"
    assert _slug_from_url("/fr/getting-started/") == "getting-started"
    assert _slug_from_url("/en/") == "_index"


def test_french_sections():
    sections = [_make_section("features", "Dossiers", lang="fr")]
    core = [_make_section("core", "Aperçu", "Info de base.", lang="fr")]
    selected, sources = select_context(sections, "dossiers", "/fr/features/", "fr", core)
    assert any(s.section_heading == "Dossiers" for s in selected)


def test_no_duplicate_sections():
    """The same section should not appear twice in selected output."""
    sections = [_make_section("features", "Records")]
    core = []
    selected, _ = select_context(sections, "records features", "/en/features/", "en", core)
    keys = [(s.page_url, s.section_heading) for s in selected]
    assert len(keys) == len(set(keys))


def test_empty_current_page():
    """Empty current_page should not crash and core should still be included."""
    sections = [_make_section("features", "Records")]
    core = [_make_section("core", "Overview", "Core info.")]
    selected, _ = select_context(sections, "what is konote", "", "en", core)
    assert any(s.section_heading == "Overview" for s in selected)
