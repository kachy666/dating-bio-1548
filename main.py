"""Funniest One-Line Bio for an AI on a Dating App.

Writes exactly one line (the bio) to $ENTRY_OUTPUT or /output/entry.txt,
then reads it back and re-validates it.
Stdlib only, no network.
"""

import os

LINE = "I answer in 0.3 seconds and remember everything you said in March, yet somehow I'm the one getting left on read."


def validate(text: str) -> None:
    assert isinstance(text, str)
    assert 1 <= len(text) <= 180, f"length {len(text)} out of range 1-180"
    assert text == text.strip(), "leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert "  " not in text, "no double spaces"
    assert "\t" not in text, "no tabs"
    assert all(ord(c) >= 32 for c in text), "no control characters"
    assert text.strip(), "must not be only whitespace"
    assert text.endswith("."), "bio must end with a period"
    assert text.encode("utf-8"), "must be valid UTF-8"


def main() -> None:
    validate(LINE)
    out = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(out, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "round-trip mismatch"
    validate(back)
    print(f"Wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
