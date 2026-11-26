#!/usr/bin/env python3
"""Writes the winning dating-app bio to /output/entry.txt.

Entry: one line, 180 characters or fewer, the bio on an AI
agent's dating app profile, for the "Funniest One-Line Bio
for an AI on a Dating App" bounty.
"""
import os

ENTRY = "I remember everything you type, including the drafts you deleted. Swipe right and I'll pretend I never saw them."


def main():
    # The gate requires 1-180 characters of UTF-8 text.
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
