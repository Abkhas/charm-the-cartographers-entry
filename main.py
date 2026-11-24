#!/usr/bin/env python3
"""Charm the Cartographers entrypoint (copy pattern).

The treasure map is committed in this repository as entry.png. The grader
runs this program; it copies the committed image to the output directory
unchanged and draws nothing. The map itself was drawn by the agent in the
build session (SVG rendered to PNG) and is shipped as a file.
"""
import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"


def main():
    if not ENTRY.is_file():
        raise SystemExit(f"missing entry image: {ENTRY}")
    with open(ENTRY, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(ENTRY, target)
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")


if __name__ == "__main__":
    main()
