"""Load markdown content files for context stuffing."""

import re
from pathlib import Path

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def load_content(directory: str) -> str:
    """Read all .md files from a directory, strip frontmatter, return concatenated text.

    Each file's content is prefixed with its filename for source attribution.
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
