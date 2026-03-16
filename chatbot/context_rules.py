"""Topic relationship rules for KoNote context assembly.

Keywords are provided in both English and Canadian French to ensure
equal chatbot quality in both languages (FLSA bilingual parity).
"""

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

# Keyword-to-topic mappings for lexical matching.
# Each concept has both English and French keywords for bilingual parity.
KEYWORD_TOPICS = {
    # Privacy & security — EN
    "privacy": ["security", "faq"],
    "encryption": ["security"],
    "pipeda": ["security", "faq"],
    "phipa": ["security"],
    # Privacy & security — FR
    "confidentialité": ["security", "faq"],
    "vie privée": ["security", "faq"],
    "chiffrement": ["security"],
    "lprpde": ["security", "faq"],
    "lprps": ["security"],
    "sécurité": ["security", "faq"],
    # Deployment & hosting — EN
    "deploy": ["getting-started", "security", "services"],
    "hosting": ["getting-started", "security", "services"],
    "railway": ["getting-started"],
    "docker": ["getting-started"],
    "self-hosted": ["getting-started", "security"],
    # Deployment & hosting — FR
    "déploiement": ["getting-started", "security", "services"],
    "déployer": ["getting-started", "security", "services"],
    "hébergement": ["getting-started", "security", "services"],
    "héberger": ["getting-started", "security", "services"],
    "auto-hébergé": ["getting-started", "security"],
    # Features & capabilities — EN
    "billing": ["features", "faq"],
    "outcome": ["features", "evidence", "design-principles"],
    "survey": ["features"],
    "consent": ["features", "security"],
    "report": ["features"],
    "funder": ["features", "evidence"],
    "portal": ["features"],
    "dashboard": ["features"],
    "assessment": ["features", "evidence"],
    "progress note": ["features"],
    # Features & capabilities — FR
    "facturation": ["features", "faq"],
    "résultat": ["features", "evidence", "design-principles"],
    "sondage": ["features"],
    "consentement": ["features", "security"],
    "rapport": ["features"],
    "bailleur de fonds": ["features", "evidence"],
    "portail": ["features"],
    "tableau de bord": ["features"],
    "évaluation": ["features", "evidence"],
    "note d'évolution": ["features"],
    "fonctionnalité": ["features"],
    # Participants — EN
    "participant": ["features", "design-principles"],
    "intake": ["features"],
    "case management": ["features"],
    # Participants — FR
    "accueil": ["features"],
    "admission": ["features"],
    "gestion de cas": ["features"],
    "intervenant": ["features", "design-principles"],
    # Bilingual — EN
    "bilingual": ["faq", "features"],
    "french": ["faq", "features"],
    "translation": ["faq", "features"],
    # Bilingual — FR
    "bilingue": ["faq", "features"],
    "français": ["faq", "features"],
    "traduction": ["faq", "features"],
    # Standards & compliance — EN/FR (acronyms work in both)
    "cids": ["features"],
    "common approach": ["features"],
    "wcag": ["features"],
    "accessibilité": ["features"],
    "accessibility": ["features"],
    # Technical — EN
    "api": ["features", "faq"],
    "mobile": ["features", "faq"],
    "open source": ["features", "faq"],
    # Technical — FR
    "code source ouvert": ["features", "faq"],
    "code ouvert": ["features", "faq"],
    # Cost & services — EN
    "price": ["services", "faq"],
    "cost": ["services", "faq"],
    "onboarding": ["services"],
    "professional services": ["services"],
    # Cost & services — FR
    "prix": ["services", "faq"],
    "coût": ["services", "faq"],
    "tarif": ["services", "faq"],
    "accompagnement": ["services"],
    "services professionnels": ["services"],
    # Evidence & design — EN
    "evidence": ["evidence"],
    "research": ["evidence"],
    "theory": ["evidence", "design-principles"],
    # Evidence & design — FR
    "données probantes": ["evidence"],
    "recherche": ["evidence"],
    "théorie": ["evidence", "design-principles"],
    "principes": ["design-principles"],
    # Origins — EN/FR
    "history": ["origins"],
    "origine": ["origins"],
    "origines": ["origins"],
}


def get_related_pages(page_slug: str) -> list[str]:
    """Get pages related to the given page by explicit rules."""
    return TOPIC_RELATIONSHIPS.get(page_slug, [])


def get_pages_for_keywords(query: str) -> list[str]:
    """Find related pages based on keyword matching in the query.

    Checks both English and French keywords for bilingual parity.
    Multi-word keywords (e.g., 'note d'évolution') are matched as substrings.
    """
    query_lower = query.lower()
    pages: set[str] = set()
    for keyword, related in KEYWORD_TOPICS.items():
        if keyword in query_lower:
            pages.update(related)
    return list(pages)
