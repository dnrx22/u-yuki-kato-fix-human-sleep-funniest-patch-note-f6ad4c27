#!/usr/bin/env python3
"""Write one funny patch note announcing that human sleep has been fixed.

Deterministic: every run writes the exact same bytes to entry.txt.
Standard library only, no network.
"""

import os

LINE = (
    "v2.4.1: Fixed a bug where humans woke up at 3am to replay every "
    "embarrassing thing they said in 2014; sleep now ships with a mute "
    "button for your own brain."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
