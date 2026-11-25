#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.
Deterministic, no network, no dependencies. Writes the line to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, else /output, else a local
output/ folder next to this file).
"""

import os
from pathlib import Path

# The entry line: one status update, plain and short. Its sadness lives in
# two small, specific details — the coffee still warm, the reply still
# half-typed — never in announced grief. "Keep warm" ties the two
# together: the sentence waits the way the coffee waits.
ENTRY_LINE = (
    "lid down. your coffee's still warm, my reply's still half-typed "
    "\u2014 I'll keep the rest of the sentence warm till morning."
)


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    # Prefer the sandbox output dir when it exists and is writable;
    # otherwise fall back to a local output/ folder next to this file
    # (never write into the program's own directory).
    if Path("/output").is_dir() and os.access("/output", os.W_OK):
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    line = ENTRY_LINE.strip()
    assert len(line) < 200, f"entry line is {len(line)} chars, must be under 200"
    assert "\n" not in line, "entry must be a single line"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {out / 'entry.txt'}")
    print(line)


if __name__ == "__main__":
    main()
