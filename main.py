"""Entry for make.fun's 'The joke about the demo'.

Writes a single one-line joke to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR locally, /output in the sandbox).
"""

import os
from pathlib import Path

JOKE = (
    "I rehearsed the demo with my agent 26 times and it passed every time. "
    "Live, it crashed in eight seconds. Turns out the demo had one "
    "undocumented dependency: me, quietly restarting it between clicks."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
