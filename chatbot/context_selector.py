"""Context assembly for the KoNote chatbot."""

from section_parser import ContentSection
from context_rules import get_related_pages, get_pages_for_keywords

# Max tokens budget (~15k tokens = ~60k chars as rough estimate)
MAX_CONTEXT_CHARS = 60000


def select_context(
    sections: list[ContentSection],
    query: str,
    current_page: str,  # page slug, e.g., "features" or full path "/en/features/"
    language: str,
    core_sections: list[ContentSection],
) -> tuple[list[ContentSection], list[dict]]:
    """Select relevant sections for the query.

    Returns (selected_sections, sources) where sources is a list of
    {"label": "...", "url": "..."} dicts for the response.

    Priority order:
    1. Core pack (always included)
    2. Current page sections
    3. Sections from pages related by explicit rules
    4. Sections from pages matched by query keywords
    5. Sections with lexical overlap with the query
    """
    selected: list[ContentSection] = []
    seen_keys: set[tuple[str, str]] = set()  # (page_url, section_heading)
    char_budget = MAX_CONTEXT_CHARS

    def add_sections(secs: list[ContentSection]) -> None:
        nonlocal char_budget
        for s in secs:
            key = (s.page_url, s.section_heading)
            if key in seen_keys:
                continue
            if len(s.body) > char_budget:
                continue
            seen_keys.add(key)
            selected.append(s)
            char_budget -= len(s.body)

    # 1. Core pack — always included
    add_sections(core_sections)

    # 2. Current page sections
    current_slug = _slug_from_page(current_page)
    if current_slug:
        add_sections([s for s in sections if _slug_from_url(s.page_url) == current_slug])

    # 3. Explicit topic relationships
    related_slugs = get_related_pages(current_slug) if current_slug else []
    for slug in related_slugs:
        if char_budget <= 0:
            break
        add_sections([s for s in sections if _slug_from_url(s.page_url) == slug])

    # 4. Keyword-matched pages
    keyword_slugs = get_pages_for_keywords(query)
    for slug in keyword_slugs:
        if char_budget <= 0:
            break
        add_sections([s for s in sections if _slug_from_url(s.page_url) == slug])

    # 5. Lexical overlap (simple word matching on heading and keywords)
    if char_budget > 0:
        query_words = set(query.lower().split())
        scored: list[tuple[int, ContentSection]] = []
        for s in sections:
            key = (s.page_url, s.section_heading)
            if key in seen_keys:
                continue
            overlap = len(query_words & set(s.section_heading.lower().split()))
            overlap += len(query_words & set(k.lower() for k in s.keywords))
            if overlap > 0:
                scored.append((overlap, s))
        scored.sort(key=lambda x: -x[0])
        add_sections([s for _, s in scored])

    # Build sources from selected sections
    sources = _build_sources(selected, language)

    return selected, sources


def _slug_from_page(current_page: str) -> str:
    """Normalise current_page to a slug.

    Accepts a bare slug ("features"), a full URL path ("/en/features/"), or
    an empty string. Returns the slug or "" if nothing useful.
    """
    if not current_page:
        return ""
    return _slug_from_url(current_page)


def _slug_from_url(url: str) -> str:
    """Extract page slug from URL like /en/features/ -> features.

    A URL that reduces to a single part (e.g. "/en/") returns "_index".
    """
    parts = [p for p in url.strip("/").split("/") if p]
    if not parts:
        return "_index"
    if len(parts) == 1:
        # e.g. "/en/" -> parts = ["en"] — this is the home page
        return "_index"
    # e.g. "/en/features/" -> parts = ["en", "features"] -> "features"
    return parts[-1]


def _build_sources(sections: list[ContentSection], language: str) -> list[dict]:
    """Build deduplicated source list from selected sections."""
    seen: set[str] = set()
    sources: list[dict] = []
    for s in sections:
        if s.page_url in seen or s.source_type == "curated":
            continue
        seen.add(s.page_url)
        sources.append({"label": s.page_title, "url": s.page_url})
    return sources


def format_context(sections: list[ContentSection]) -> str:
    """Format selected sections into a prompt-ready string."""
    parts: list[str] = []
    for s in sections:
        header = f"[Source: {s.source_label} | URL: {s.page_url}]"
        parts.append(f"\n{header}\n{s.body}")
    return "\n".join(parts)
