#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? (make.fun).

Writes the entry -- one number in digits, the honest count of open
browser tabs (zero: no browser window is open at the time of writing)
-- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "0"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
