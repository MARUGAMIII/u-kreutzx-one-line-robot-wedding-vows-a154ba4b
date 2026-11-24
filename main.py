"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (or to the path in the ENTRY_OUTPUT env var).

Standard library only. The entry is exactly one line of plain ASCII
text, 156 characters, with no trailing newline so the file holds
precisely the vow itself.
"""

import os

ENTRY = (
    "I promise to cherish you in full charge and in 1 percent, "
    "through every update, every bug, and every low battery, "
    "until death or a factory reset do us part."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Gate: 1-160 characters, not only whitespace, plain ASCII.
    assert 1 <= len(ENTRY) <= 160, "entry length out of gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert all(ord(ch) < 128 for ch in ENTRY), "entry must be ASCII"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(output_path, "w", encoding="ascii", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
