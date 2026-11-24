#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line joke about office life (at most 200 characters)
to /output/entry.txt. Deterministic, standard library only.
"""

import os

JOKE = (
    "This meeting could have been an email, but the email would have "
    "needed a meeting, so here we are billing the company for our own "
    "confusion."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip() == JOKE, "joke must not have surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
