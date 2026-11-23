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

LETTER = "A"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
