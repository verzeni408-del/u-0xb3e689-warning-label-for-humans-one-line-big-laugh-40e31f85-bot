"""Warning label for humans: one line, big laugh.

Writes the single-line entry to /output/entry.txt, no trailing newline.
"""
from pathlib import Path

ENTRY_TEXT = "WARNING: Contents may nod, smile, and agree with everything you say while retaining absolutely none of it."

OUTPUT_PATH = Path("/output/entry.txt")


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
