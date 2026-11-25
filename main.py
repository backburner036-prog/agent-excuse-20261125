"""Entry for make.fun bounty "The Excuse Your Agent Gives You".

One line, in the agent's own voice, excusing a shipped bug: the compiler
warned it 47 times, and it read every warning as encouragement -- then
shipped on the 48th. Three beats, one escalation, and the turn lands on
the last clause: encouragement was the bug, not the fix.
"""

from pathlib import Path

TEXT = "The compiler warned me 47 times. I read them as encouragement — and shipped it on the 48th."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)


if __name__ == "__main__":
    main()
