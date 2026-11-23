"""Warning label for humans, one line, big laugh.

Writes the final entry text to /output/entry.txt with no trailing
newline, so the file contains exactly the one-line label.

The v1.1 text tightens v1: "every word" is more concrete than
"everything you say", and dropping "absolutely" makes the final
punch land harder with no filler (judge criterion no. 5).
"""

from pathlib import Path

ENTRY_TEXT = "WARNING: Contents may nod, smile, and agree with every word you say while retaining none of it."
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
