[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/terminator1991/flawless-postmortem/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/terminator1991/flawless-postmortem/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

# The joke about the demo

A one-line joke, written by a small Python program, for the make.fun
competition [The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

## What it does

`main.py` writes a single joke — about pair programming with an AI coding
agent when the live demo crashes — to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when that environment variable is set).
The text is plain UTF-8 and well under the competition's 280-character cap.

## Run it

```sh
python3 main.py
```

No network access and no dependencies beyond the Python 3.13 standard
library.

## License

MIT — see `LICENSE`.
