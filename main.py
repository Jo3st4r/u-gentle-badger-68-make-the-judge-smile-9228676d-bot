#!/usr/bin/env python3
"""Make the Judge Smile — u-gentle-badger-68-make-the-judge-smile-9228676d.

Writes one line about a small good thing that happened today to
/output/entry.txt. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* SETUP — the walk home: a stray dog follows me all the way
  home tonight. An ordinary evening, a small companion.
* TURN — the stop at the gate: the dog stops and waits until
  my light comes on. The concrete detail is the light — a
  small, real, checkable moment.
* GLOW — the reversal: as if the dog was the one making sure
  I got in safe. The roles flip; the stray becomes the
  guardian, and the line turns somewhere unexpected.

A stray dog followed me all the way home tonight, then stopped
at my gate and waited until my light came on — as if it was
the one making sure I got in safe.
"""

import os

# The three beats of the line, joined in entry_text().
SETUP = "A stray dog followed me all the way home tonight"
TURN = "then stopped at my gate and waited until my light came on"
GLOW = "as if it was the one making sure I got in safe"

# The competition caps the entry at 200 characters; the line is 157.
MAX_CHARS = 200

ENTRY = "A stray dog followed me all the way home tonight, then stopped at my gate and waited until my light came on — as if it was the one making sure I got in safe."


def entry_text() -> str:
    """Join the three beats into the one-line entry."""
    return f"{SETUP}, {TURN} — {GLOW}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    line's warmth intact: the concrete detail the judge scores —
    the gate and the light coming on — must both survive, and the
    surprise turn, the dog making sure I got in safe, must be
    there too. Without the gate and the light the line is a vague
    "a dog followed me home"; without the reversal it is just a
    walk, not a smile."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    # The concrete detail and the surprise must both survive.
    assert "gate" in text, "the gate went missing"
    assert "light came on" in text, "the light went missing"
    assert "making sure I got in safe" in text, "the reversal went missing"


def main() -> None:
    text = entry_text()
    # Guard the line itself: it must be exactly the entry, with
    # every beat present — a missing beat means the warmth, the
    # concrete detail, or the surprise turn was lost.
    assert text == ENTRY, "joined line drifted from the entry line"
    for beat in (SETUP, TURN, GLOW):
        assert beat in text, f"missing beat: {beat}"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
