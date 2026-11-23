#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt.

The joke: a reply-all storm, with concrete real numbers (4,000 staff,
312 replies) and a twist in the last words -- the people agreeing with
the removal request commit the exact mistake they are agreeing about.
The line is 107 characters, inside the 1-199 gate.
"""
import os

LINE = (
    "Someone replied-all to all 4,000 staff asking to be removed "
    "from the list. 312 people replied-all to agree."
)


def main():
    assert 1 <= len(LINE) <= 199, "entry must be 1-199 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
