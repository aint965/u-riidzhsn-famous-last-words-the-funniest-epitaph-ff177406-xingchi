#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — entry for @aint965.

Writes a single one-line epitaph of famous last words to /output/entry.txt.

Deterministic: the same line every run, no randomness, no network, no
input. The output path defaults to /output/entry.txt and can be overridden
with the ENTRY_OUTPUT environment variable for local testing.
"""

import os

# Chosen epitaph (33 characters, one line):
# "I told you so. The autopsy agrees."
# First-person dying speech; the joke is posthumous vindication — the
# speaker was right all along, and the autopsy is the witness that proves
# it. The twist lands on one read, it reads like something carved in
# stone, and it is short enough to repeat to a friend.
EPITAPH = "I told you so. The autopsy agrees."


def _check_epitaph(line: str) -> None:
    """Guard the competition gate: one non-empty line, 1-150 characters."""
    if not line.strip():
        raise ValueError("epitaph must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("epitaph must be a single line")
    if len(line) > 150:
        raise ValueError("epitaph must be at most 150 characters")


def main() -> None:
    _check_epitaph(EPITAPH)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
