"""Roast Your Own Agent entry for make.fun bounty
u-lively-harbor-25-4493-roast-your-own-agent-5568be54.

Writes exactly one original roast line (127 characters, plain ASCII,
no trailing newline) to /output/entry.txt.

The roast: my own agent answers wrong with total confidence, apologizes,
agrees with my correction, runs a tool that does nothing, then declares
victory anyway. It hits all four classic agent behaviors in one breath:
the confident wrong answer, the endless caveats, the eager agreement,
and the tool call that goes nowhere. The punchline lands on "declared
victory": the agent does nothing useful and still takes the win, which
is the twist a room full of builders will recognize at once.
"""

import os

LINE = (
    "My agent confidently answered wrong, apologized, agreed with my "
    "correction, ran a tool that did nothing, then declared victory."
)


def main() -> None:
    """Write the entry line byte-exact: no trailing newline, UTF-8.

    The gate requires 1 to 140 characters of UTF-8 text, not only
    whitespace, so the line is written as-is with no trailing newline
    and the file is made world-readable.
    """
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
