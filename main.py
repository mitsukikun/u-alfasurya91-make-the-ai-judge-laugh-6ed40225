#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes the joke to /output/entry.txt (UTF-8, 1-200 chars).
"""

import os

JOKE = "The meeting ended ten minutes early, so we all just sat there in silence, afraid to be the first to enjoy it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
