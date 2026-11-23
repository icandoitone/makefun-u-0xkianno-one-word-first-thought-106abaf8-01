#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind, with no topic, no explanation and no second draft.

The word is "vellichor": the strange wistfulness of used bookstores,
which are infused with the passage of time. It is surprising, vivid
and specific, and its soft sound rewards a second look.
"""

from pathlib import Path

WORD = "vellichor"

OUTPUT_PATH = Path("/output/entry.txt")


def check_word(word: str) -> str:
    """Make sure the word passes the gate: one word, 1-24 chars."""
    if not word or len(word) > 24:
        raise ValueError("word must be 1 to 24 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = check_word(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
