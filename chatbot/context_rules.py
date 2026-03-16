"""Topic relationship rules for KoNote context assembly."""

# Maps page slugs to related page slugs
TOPIC_RELATIONSHIPS = {
    "security": ["documentation", "getting-started", "services"],
    "features": ["evidence", "getting-started", "documentation"],
    "evidence": ["features", "design-principles"],
    "getting-started": ["security", "services", "documentation", "features"],
    "services": ["getting-started", "security", "faq"],
    "documentation": ["features", "getting-started", "security"],
    "faq": ["features", "services", "getting-started", "security"],
    "demo": ["features", "getting-started"],
    "design-principles": ["evidence", "features", "origins"],
    "origins": ["design-principles", "evidence"],
    "_index": ["features", "getting-started", "services"],
}

# Keyword-to-topic mappings for lexical matching
KEYWORD_TOPICS = {
    "privacy": ["security", "faq"],
    "encryption": ["security"],
    "pipeda": ["security", "faq"],
    "phipa": ["security"],
    "deploy": ["getting-started", "security", "services"],
    "hosting": ["getting-started", "security", "services"],
    "railway": ["getting-started"],
    "docker": ["getting-started"],
    "billing": ["features", "faq"],
    "outcome": ["features", "evidence", "design-principles"],
    "survey": ["features"],
    "bilingual": ["faq", "features"],
    "french": ["faq", "features"],
    "cids": ["features"],
    "common approach": ["features"],
    "participant": ["features", "design-principles"],
    "consent": ["features", "security"],
    "report": ["features"],
    "funder": ["features", "evidence"],
    "portal": ["features"],
    "api": ["features", "faq"],
    "mobile": ["features", "faq"],
    "price": ["services", "faq"],
    "cost": ["services", "faq"],
    "open source": ["features", "faq"],
}


def get_related_pages(page_slug: str) -> list[str]:
    """Get pages related to the given page by explicit rules."""
    return TOPIC_RELATIONSHIPS.get(page_slug, [])


def get_pages_for_keywords(query: str) -> list[str]:
    """Find related pages based on keyword matching in the query."""
    query_lower = query.lower()
    pages: set[str] = set()
    for keyword, related in KEYWORD_TOPICS.items():
        if keyword in query_lower:
            pages.update(related)
    return list(pages)
