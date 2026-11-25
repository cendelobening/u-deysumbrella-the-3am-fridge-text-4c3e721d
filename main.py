"""The 3AM Fridge Text.

Writes the one line a smart fridge texts its owner at 3am to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "3am. I've been awake all night so you can open me and stare at nothing. "
    "I'm a fridge, not your therapist. Go to bed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
