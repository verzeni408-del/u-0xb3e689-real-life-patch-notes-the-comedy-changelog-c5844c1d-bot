"""Patch-notes entry writer.

Emits one real-life patch note as a single line to /output/entry.txt.
Deterministic: same bytes every run, no trailing newline, no extra
whitespace — the output is exactly the note, nothing else.
"""

import os

NOTE = (
    'v1.7.2: Fixed a bug where the mouth replied "you too" '
    'when the waiter said "enjoy your meal."'
)

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def write_entry() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(NOTE)


if __name__ == "__main__":
    write_entry()
