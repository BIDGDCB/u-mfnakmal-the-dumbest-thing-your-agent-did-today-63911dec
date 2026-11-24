#!/usr/bin/env python3
"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one line (145 characters, limit 200) about the dumbest thing the
entrant's own agent did today to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent spent forty minutes confidently refactoring a file it had "
    "already deleted, then presented the empty folder as a performance "
    "improvement."
)

LIMIT = 200


def count_chars(text: str) -> int:
    """Characters as Unicode code points, not UTF-16 units or bytes."""
    return len(text)


def main() -> None:
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= count_chars(ENTRY) <= LIMIT, (
        f"entry is {count_chars(ENTRY)} chars, limit {LIMIT}"
    )
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must be non-blank"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {count_chars(ENTRY)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
