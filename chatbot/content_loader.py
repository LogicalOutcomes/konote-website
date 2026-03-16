"""Load and index content for the chatbot."""

import re
from pathlib import Path

from section_parser import ContentSection, parse_directory

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def load_content(directory: str) -> str:
    """Legacy: Read all .md files, strip frontmatter, return concatenated text.

    Each file's content is prefixed with its filename for source attribution.
    Kept for backward compatibility with existing tests.
    """
    content_dir = Path(directory)
    if not content_dir.exists():
        return ""

    parts = []
    for md_file in sorted(content_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        # Strip YAML frontmatter
        text = FRONTMATTER_PATTERN.sub("", text).strip()
        if text:
            parts.append(f"\n--- Source: {md_file.name} ---\n{text}")

    return "\n".join(parts)


def load_section_index(language: str) -> list[ContentSection]:
    """Load all content for a language into structured sections."""
    sections: list[ContentSection] = []
    sections.extend(parse_directory(f"knowledge/site/{language}/", language, "site"))
    sections.extend(parse_directory(f"knowledge/curated/{language}/", language, "curated"))
    return sections


def load_core_pack(language: str) -> list[ContentSection]:
    """Load the always-included core knowledge pack."""
    core_dir = f"knowledge/core/{language}/"
    return parse_directory(core_dir, language, "curated")
