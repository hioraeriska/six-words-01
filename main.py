#!/usr/bin/env python3
"""Six Words, One Story entry: writes one complete six-word story."""
import os

STORY = "She sold everything. Kept the photograph."


def count_words(text):
    """Count the words in a story (split on whitespace)."""
    return len(text.split())


def validate_story(text):
    """Gate check: exactly six words, 1-60 chars, not only whitespace."""
    if count_words(text) != 6:
        raise ValueError(f"expected exactly 6 words, got {count_words(text)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"expected 1-60 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    return text


def main():
    story = validate_story(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(story)


if __name__ == "__main__":
    main()
