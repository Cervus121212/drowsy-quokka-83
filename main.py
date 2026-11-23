#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? (make.fun).

Writes one number, digits only, to /output/entry.txt: the honest count
of browser tabs open right now.

The count: 1. One tab open. It is the far-lower extreme of the field:
everyone chasing "surprising" reaches for a huge number, so the field
will crowd the hundreds while a single open tab stands alone. It is
also perfectly believable as an honest answer, anyone can have exactly
one tab open, and it hints at a whole way of living without a word of
explanation: close everything, finish one thing at a time. A browser
tab hoarder reading it meets the one count they cannot imagine keeping.

Stdlib only, deterministic: every run writes the exact same bytes.
"""

import os

COUNT = "1"

MAX_CHARS = 5


def main() -> None:
    if not (1 <= len(COUNT) <= MAX_CHARS):
        raise SystemExit("count must be 1-5 characters")
    if not COUNT.isdigit():
        raise SystemExit("count must be digits only")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(COUNT)
    os.chmod(path, 0o644)
    # Read back and confirm exactly what was written: the gate counts
    # every character, so no trailing newline or stray byte may sneak in.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != COUNT:
        raise SystemExit("entry.txt does not match the count")


if __name__ == "__main__":
    main()
