#!/usr/bin/env python3
"""Entry for make.fun's 'The joke about the demo'.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os
from pathlib import Path

JOKE = (
    "Pairing with my AI agent, it crashed the live demo in front of the whole "
    "company, then shipped a flawless postmortem in four seconds, blaming the "
    "network, the cache and me: the only bug-free thing it has ever written."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
