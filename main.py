"""Warning label for a human, one line, one big laugh.

Why this line lands: everyone knows the person who shrugs off a
mistake with a breezy "no worries" and then replays it in their head
for years. The joke opens with that familiar, instantly forgiving
phrase, so the reader relaxes -- then the tail of the sentence
undercuts it completely: "for the next eleven years". The absurdly
specific duration is the punchline. Eleven is too precise to be a
throwaway and too long to be harmless, so the casual shrug suddenly
reads as a decade-long grudge, carefully logged and never mentioned.

The "WARNING: This unit will..." frame sells it as a printed label
stuck on a product, not a person making a confession. That deadpan
instruction-manual voice makes the human flaw feel like a factory
defect, which is funnier than stating it outright. One sentence,
one recognition, one escalation -- and the laugh comes from the
reader realising they are the unit on the label.
"""

from pathlib import Path

ENTRY_TEXT = (
    "WARNING: This unit will say 'no worries' while worrying "
    "about it for the next eleven years."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
