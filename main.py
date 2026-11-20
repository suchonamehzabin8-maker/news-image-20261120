#!/usr/bin/env python3
"""news-image-20261120 entry (Python 3.13, standard library only).

Copies the image held in this repository to /output/entry.png.
Deterministic: the same bytes are written on every run, no network,
no randomness, no clock use.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
