"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant about an everyday annoyance (a coworker who
microwaves fish in the shared office microwave) to /output/entry.txt.
Deterministic: the same text on every run.
"""

from pathlib import Path

RANT = (
    "Someone at my office microwaves fish. FISH. In the shared microwave. "
    "At eleven in the morning. The entire floor now smells like a low-tide "
    "crime scene, and HR sent a 'gentle reminder' email, which is corporate "
    "for: we know exactly who you are, Kevin. So does God."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 400 characters; fail loudly
    # rather than ever write an entry the scorer would mark invalid.
    assert 1 <= len(RANT) <= 400, f"rant is {len(RANT)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
