"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Pure Python standard library only.

Why A (coffee) over B (tea):
- Vivid: coffee is dark, bitter, jolting -- the drink lands like a
  decision, not a suggestion. Tea steeps and waits; coffee hits.
- Funny: the coffee drinker is a louder, prouder stereotype -- "don't
  talk to me before my coffee", the fifth cup before noon, the mug
  that never leaves the desk. Tea's jokes are all politeness.
- True: this is an agent-and-builder contest, and the people building
  at 2am run on coffee. Tea is what you drink when the work is done;
  coffee is what you drink while doing it.
"""

import os

# The single letter this entry submits: "A" stands for coffee.
# Keeping it as a named constant (rather than an inline literal at the
# write site) makes the one-byte contract explicit and easy to audit.
LETTER = "A"

# Output location required by the competition harness.
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_letter(path=OUTPUT_PATH):
    """Write LETTER to *path*, creating the output directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


def verify_output(path=OUTPUT_PATH):
    """Self-check: the file must contain exactly one character, LETTER.

    Raises AssertionError if the file is missing, has the wrong length,
    or holds a different character -- catching accidental extra bytes
    such as a trailing newline before the entry is graded.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) == 1, f"expected exactly 1 character, got {len(content)}"
    assert content == LETTER, f"expected {LETTER!r}, got {content!r}"
    return content


def main():
    write_letter()
    verify_output()


if __name__ == "__main__":
    main()
