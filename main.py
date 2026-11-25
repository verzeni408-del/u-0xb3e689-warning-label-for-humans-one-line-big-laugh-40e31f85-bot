"""Warning label for a human, written the way a real product label sounds.

The joke works because almost everyone has done exactly this. You open
the box, skip the manual, put the thing together wrong, and only then go
looking for the instructions. The label treats that habit like a contents
warning, which is what makes it land: the product is not the box, it is
the person holding it.

"One (1) human" borrows the dry numbering style printed on real labels,
so the line reads like something stamped on a package instead of a joke
someone wrote. The punch sits in the last few words. "Only after breaking
it" flips the order you expect, instructions first, and admits the truth
in the bluntest way. One idea, no setup beyond the label format, and
the laugh comes from recognising yourself in it.
"""

from pathlib import Path

LABEL_TEXT = "WARNING: This product contains one (1) human who reads the instructions only after breaking it."


def main():
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LABEL_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
