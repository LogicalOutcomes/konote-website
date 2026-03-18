#!/usr/bin/env python3
"""Check that all content is translated into both English and French.

Compares:
  1. Hugo content pages in content/en/ vs content/fr/
  2. i18n UI string keys in i18n/en.yaml vs i18n/fr.yaml
  3. Chatbot knowledge files in chatbot/knowledge/*/en/ vs */fr/

Usage:
    python scripts/check-translations.py

Exit code 0 if everything matches, 1 if anything is missing.
"""

import os
import re
import sys
from pathlib import Path

# Resolve project root (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent

PASS = "\033[32mPASS\033[0m"
FAIL = "\033[31mFAIL\033[0m"


def compare_file_sets(en_dir: Path, fr_dir: Path) -> tuple[set[str], set[str]]:
    """Return (missing_in_fr, missing_in_en) filename sets."""
    en_files = {f.name for f in en_dir.iterdir() if f.is_file()} if en_dir.is_dir() else set()
    fr_files = {f.name for f in fr_dir.iterdir() if f.is_file()} if fr_dir.is_dir() else set()
    return en_files - fr_files, fr_files - en_files


def parse_i18n_keys(yaml_path: Path) -> set[str]:
    """Extract id values from Hugo i18n YAML files (simple list-of-dicts format)."""
    keys = set()
    if not yaml_path.is_file():
        return keys
    with open(yaml_path, encoding="utf-8") as f:
        for line in f:
            match = re.match(r'^- id:\s*(\S+)', line)
            if match:
                keys.add(match.group(1))
    return keys


def check_hugo_content() -> bool:
    """Check content/en/ vs content/fr/ pages."""
    print("=== Hugo Content Pages ===")
    en_dir = ROOT / "content" / "en"
    fr_dir = ROOT / "content" / "fr"

    if not en_dir.is_dir() and not fr_dir.is_dir():
        print(f"  SKIP: No content directories found")
        return True

    missing_fr, missing_en = compare_file_sets(en_dir, fr_dir)
    matched = len({f.name for f in en_dir.iterdir() if f.is_file()} & {f.name for f in fr_dir.iterdir() if f.is_file()})
    ok = True

    if missing_fr:
        print(f"  {FAIL}: Missing French translations:")
        for f in sorted(missing_fr):
            print(f"    - {f}")
        ok = False

    if missing_en:
        print(f"  {FAIL}: Missing English translations:")
        for f in sorted(missing_en):
            print(f"    - {f}")
        ok = False

    if ok:
        print(f"  {PASS}: {matched} pages matched in both languages")

    return ok


def check_i18n_keys() -> bool:
    """Check i18n/en.yaml vs i18n/fr.yaml keys."""
    print("\n=== i18n UI Strings ===")
    en_path = ROOT / "i18n" / "en.yaml"
    fr_path = ROOT / "i18n" / "fr.yaml"

    if not en_path.is_file() and not fr_path.is_file():
        print(f"  SKIP: No i18n files found")
        return True

    en_keys = parse_i18n_keys(en_path)
    fr_keys = parse_i18n_keys(fr_path)
    missing_fr = en_keys - fr_keys
    missing_en = fr_keys - en_keys
    matched = len(en_keys & fr_keys)
    ok = True

    if missing_fr:
        print(f"  {FAIL}: Keys missing from fr.yaml:")
        for k in sorted(missing_fr):
            print(f"    - {k}")
        ok = False

    if missing_en:
        print(f"  {FAIL}: Keys missing from en.yaml:")
        for k in sorted(missing_en):
            print(f"    - {k}")
        ok = False

    if ok:
        print(f"  {PASS}: {matched} keys matched in both languages")

    return ok


def check_chatbot_knowledge() -> bool:
    """Check chatbot/knowledge/*/en/ vs */fr/ files."""
    print("\n=== Chatbot Knowledge ===")
    knowledge_dir = ROOT / "chatbot" / "knowledge"

    if not knowledge_dir.is_dir():
        print(f"  SKIP: No chatbot/knowledge/ directory found")
        return True

    ok = True
    found_any = False

    for category in sorted(knowledge_dir.iterdir()):
        if not category.is_dir():
            continue
        en_dir = category / "en"
        fr_dir = category / "fr"
        if not en_dir.is_dir() and not fr_dir.is_dir():
            continue

        found_any = True
        missing_fr, missing_en = compare_file_sets(en_dir, fr_dir)
        en_files = {f.name for f in en_dir.iterdir() if f.is_file()} if en_dir.is_dir() else set()
        fr_files = {f.name for f in fr_dir.iterdir() if f.is_file()} if fr_dir.is_dir() else set()
        matched = len(en_files & fr_files)

        if missing_fr or missing_en:
            if missing_fr:
                print(f"  {category.name}: {FAIL} — Missing French translations:")
                for f in sorted(missing_fr):
                    print(f"    - {f}")
            if missing_en:
                print(f"  {category.name}: {FAIL} — Missing English translations:")
                for f in sorted(missing_en):
                    print(f"    - {f}")
            ok = False
        else:
            print(f"  {category.name}: {PASS} ({matched} file{'s' if matched != 1 else ''} matched)")

    if not found_any:
        print(f"  SKIP: No en/fr subdirectories found")

    return ok


def main():
    print()
    all_ok = True
    all_ok = check_hugo_content() and all_ok
    all_ok = check_i18n_keys() and all_ok
    all_ok = check_chatbot_knowledge() and all_ok

    print()
    if all_ok:
        print(f"Result: {PASS} — All translations complete")
    else:
        print(f"Result: {FAIL} — Missing translations found (see above)")

    print()
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
