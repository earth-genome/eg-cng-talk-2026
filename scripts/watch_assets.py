#!/usr/bin/env python3
"""Touch index.qmd when theme/assets change (Quarto often ignores SCSS-only saves)."""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.qmd"
PATHS = [
    ROOT / "custom.scss",
    ROOT / "animations.html",
    ROOT / "preview-reload.html",
]
IMAGE_DIR = ROOT / "images"


def _mtime(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0.0


def _snapshot() -> dict[str, float]:
    out: dict[str, float] = {str(p): _mtime(p) for p in PATHS if p.exists()}
    if IMAGE_DIR.is_dir():
        for p in IMAGE_DIR.rglob("*"):
            if p.is_file():
                out[str(p)] = _mtime(p)
    return out


def main() -> int:
    if not INDEX.is_file():
        print("watch_assets: index.qmd not found", file=sys.stderr)
        return 1

    prev = _snapshot()
    print("Asset watcher: custom.scss, animations.html, images/ → touch index.qmd", flush=True)

    while True:
        time.sleep(1.0)
        cur = _snapshot()
        if cur != prev:
            os.utime(INDEX, None)
            prev = cur

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
