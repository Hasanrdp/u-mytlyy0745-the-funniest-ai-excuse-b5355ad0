#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes one line — the funniest excuse an AI agent could offer after
failing a task — to /output/entry.txt. Deterministic: the same bytes
on every run. No input, no network, no randomness, standard library
only.
"""

import os

EXCUSE = "I finished it, then saved it as 'untitled (1)'. There are now four hundred untitled files. One of them is yours. I refuse to guess which."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse must be 1-200 chars, got {len(text)}"
    assert text.strip(), "excuse must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the excuse above, byte for byte, on every run.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch: entry.txt differs from EXCUSE"


if __name__ == "__main__":
    main()
