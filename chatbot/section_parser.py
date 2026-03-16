"""Section-aware markdown content parser for the KoNote chatbot."""

import re
from dataclasses import dataclass, field
from pathlib import Path

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_PATTERN = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)

# Stop words to exclude from keyword generation
_STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "by", "do", "for",
    "from", "has", "have", "how", "in", "is", "it", "its", "of", "on", "or",
    "that", "the", "this", "to", "was", "what", "when", "where", "who",
    "will", "with", "your", "our", "can", "not", "but", "we", "you", "us",
    "les", "des", "une", "est", "que", "qui", "sur", "par", "dans", "pour",
    "avec", "son", "ses", "leur", "leurs",
}


@dataclass
class ContentSection:
    language: str
    source_type: str  # "site" or "curated"
    page_title: str
    page_url: str  # e.g., "/en/features/"
    section_heading: str
    parent_heading: str  # empty if top-level
    body: str
    source_label: str  # e.g., "Features — Participant Records"
    keywords: list[str] = field(default_factory=list)


def _extract_frontmatter_title(text: str) -> tuple[str, str]:
    """Extract title from YAML frontmatter. Returns (title, remaining_text)."""
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return "", text

    frontmatter = match.group(1)
    remaining = text[match.end():]

    title = ""
    for line in frontmatter.splitlines():
        if line.startswith("title:"):
            title = line[len("title:"):].strip().strip('"').strip("'")
            break

    return title, remaining


def _derive_page_url(filepath: str, language: str) -> str:
    """Derive page URL from filename and language.

    Examples:
        features.md + en -> /en/features/
        _index.md + en -> /en/
        getting-started.md + fr -> /fr/getting-started/
    """
    stem = Path(filepath).stem
    if stem == "_index":
        return f"/{language}/"
    return f"/{language}/{stem}/"


def _generate_keywords(heading: str, body_snippet: str) -> list[str]:
    """Generate keywords from heading text and first few significant words of body."""
    words = re.findall(r"[a-zA-ZÀ-ÿ]+", heading.lower() + " " + body_snippet.lower())
    keywords = [w for w in words if len(w) > 3 and w not in _STOP_WORDS]
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique.append(kw)
    return unique[:20]  # cap at 20 keywords


def parse_file(filepath: str, language: str, source_type: str) -> list[ContentSection]:
    """Parse a single .md file into ContentSection records.

    Splits on ## and ### headings. If the file has no headings, creates a
    single section using the page title as the heading.
    """
    path = Path(filepath)
    raw = path.read_text(encoding="utf-8")

    page_title, body_text = _extract_frontmatter_title(raw)
    page_url = _derive_page_url(filepath, language)

    if not page_title:
        # Fall back to stem-based title
        stem = path.stem.replace("-", " ").replace("_", " ").title()
        page_title = stem if stem != "Index" else "Home"

    sections: list[ContentSection] = []
    heading_matches = list(HEADING_PATTERN.finditer(body_text))

    if not heading_matches:
        # No headings — single section with page title as heading
        content = body_text.strip()
        if content:
            keywords = _generate_keywords(page_title, content[:300])
            sections.append(ContentSection(
                language=language,
                source_type=source_type,
                page_title=page_title,
                page_url=page_url,
                section_heading=page_title,
                parent_heading="",
                body=content,
                source_label=page_title,
                keywords=keywords,
            ))
        return sections

    # Build sections from heading spans
    current_h2 = ""

    for i, match in enumerate(heading_matches):
        level = len(match.group(1))  # 2 or 3
        heading_text = match.group(2).strip()

        # Body is from end of this heading line to start of next heading (or EOF)
        start = match.end()
        end = heading_matches[i + 1].start() if i + 1 < len(heading_matches) else len(body_text)
        section_body = body_text[start:end].strip()

        if level == 2:
            current_h2 = heading_text
            parent = ""
        else:
            parent = current_h2

        # Build source label
        if parent:
            source_label = f"{page_title} — {parent} — {heading_text}"
        else:
            source_label = f"{page_title} — {heading_text}"

        # Include body snippet for keyword generation
        body_snippet = section_body[:300]
        keywords = _generate_keywords(heading_text, body_snippet)

        # Only add if there's substantive content
        if section_body or heading_text:
            sections.append(ContentSection(
                language=language,
                source_type=source_type,
                page_title=page_title,
                page_url=page_url,
                section_heading=heading_text,
                parent_heading=parent,
                body=section_body,
                source_label=source_label,
                keywords=keywords,
            ))

    return sections


def parse_directory(directory: str, language: str, source_type: str) -> list[ContentSection]:
    """Parse all .md files in directory into ContentSection records."""
    content_dir = Path(directory)
    if not content_dir.exists():
        return []

    sections: list[ContentSection] = []
    for md_file in sorted(content_dir.glob("*.md")):
        sections.extend(parse_file(str(md_file), language, source_type))

    return sections
