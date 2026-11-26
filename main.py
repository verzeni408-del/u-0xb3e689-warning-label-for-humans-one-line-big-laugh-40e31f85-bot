#!/usr/bin/env python3
"""Warning label printer for the human enclosure."""

SIGN_HEADER = "WARNING"
GLASS_RULE = "Do not tap the glass."
OCCUPANT = "The human inside is pretending to work"
CONSEQUENCE = "and will bite if disturbed."


def assemble_notice(header, rule, occupant, consequence):
    pieces = [header + ":", rule, occupant, consequence]
    return " ".join(pieces)


def main():
    line = assemble_notice(
        SIGN_HEADER,
        GLASS_RULE,
        OCCUPANT,
        CONSEQUENCE,
    )
    print(line)


if __name__ == "__main__":
    main()
