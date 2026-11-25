#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

TEXT = """Listen. The ritual is ready, the eclipse is Tuesday, the armies are — hold on. Sorry. I was up till four re-carving the runes because the last apprentice quit, and honestly, the dark lord business was simpler when I had staff. The prophecy says I rise. The prophecy never mentions the paperwork. So yes, kneel. But quickly, please. My knees hurt too, the throne is cold, the crown weighs a ton, the cape itches, and the minions have unionised. And if the hero comes before noon, tell him I'm indisposed. Eternal darkness can wait until after my nap."""

MAX_CHARS = 600

def main():
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
