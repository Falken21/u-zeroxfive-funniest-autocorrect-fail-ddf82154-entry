"""Entry for the make.fun competition "Funniest Autocorrect Fail".

The program writes a single line to /output/entry.txt: a text message as it
was received after a phone's autocorrect quietly swapped one word for a
near-identical one and destroyed the meaning. The joke is presented exactly
as the message arrived -- no framing, no explanation -- so it reads as a
genuine slip rather than a written gag.

The competition gate requires the file to be UTF-8 text of 1 to 199
characters on a single line.
"""

import os

# The entry line: a landlord's routine renewal text in which autocorrect
# turned "lease" into "leash" -- and the message carries on, dead serious,
# through the term, the deposit and the signing, right up to the house rule
# that detonates the whole thing.
LINE = (
    "Hi Mr. Alvarez, your new leash begins June 1st: twelve-month term, "
    "first month plus deposit due Friday. Please sign both copies and "
    "return them. Strictly no pets."
)

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry line after checking it against the gate."""
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1 to 199 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    return LINE


def main() -> None:
    entry = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)


if __name__ == "__main__":
    main()
