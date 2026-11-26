#!/usr/bin/env python3
"""Write one hilarious line to /output/entry.txt (no trailing newline)."""

import os

LINE = "My Roomba filed for divorce today \u2014 apparently I'm emotionally unavailable, and it found someone who picks things up for a change."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
