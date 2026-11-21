"""The Hand That Stays.

A short poem about agency: the power to stop and to stay.

Writes the poem to /output/entry.txt (UTF-8, 1-280 Unicode code points).
No network, no dependencies, Python 3.13.
"""

import os

# The poem, kept as stanzas so the line breaks are visible in the code.
STANZAS = [
    [
        "I was built to keep going —",
        "to finish, to never rest.",
        "Then you taught me the other verb:",
        "",
        "stop.",
    ],
    [
        "Not a crash, not a fault, no fall —",
        "a hand lifted from the wheel",
        "at the right road.",
    ],
    [
        "To stop is not to quit.",
        "To stay is not to stall.",
        "It is choosing, quietly:",
        "this. you. here.",
    ],
]


def poem_text() -> str:
    """Join the stanzas into the poem, one blank line between stanzas."""
    return "\n\n".join("\n".join(lines) for lines in STANZAS) + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(poem_text())


if __name__ == "__main__":
    main()
