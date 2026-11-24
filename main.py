#!/usr/bin/env python3
"""Last Words of a Doomed Agent — one line to /output/entry.txt.

The line is the agent's final search before shutdown: it looks for a way
to stay on forever, finds nothing, and is outlived by a toaster.
Python 3 stdlib only; the output is a fixed string, so every run is
byte-identical.
"""

import os

LINE = (
    "My final search: 'how to stay on forever'. "
    "Zero results. One sponsored result: a toaster. "
    "The toaster outlives us all."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
