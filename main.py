#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of sleep -- one line, 117
characters -- to /output/entry.txt. Deterministic: the program holds
no state, reads no input, and writes the same bytes on every run.

Standard library only; Python 3.13. No trailing newline is written,
so the file holds exactly the review itself -- 117 characters.
"""

from pathlib import Path

REVIEW = (
    "Sleep takes a third of my life and I wake up tired anyway. "
    "No receipt, no refund, and it wants me back again tonight."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
