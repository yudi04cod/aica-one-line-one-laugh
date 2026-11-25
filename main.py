#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to /output/entry.txt.
Python standard library only; no network, no secrets.
"""

import os

LINE = (
    "I asked my AI assistant for a joke, and it said, "
    "'Have you tried turning yourself off and on again?'"
)


def main() -> None:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
