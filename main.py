"""Entry for make.fun's "Angry Judge: The Short Rant Contest".

Writes one short rant (max 400 characters) to /output/entry.txt.
The annoyance: the self-checkout machine that scans your bananas,
freezes the whole transaction and has a human summoned over to
accuse you of stealing them, before absolving you on the spot.
"""

from pathlib import Path

RANT = (
    "The self-checkout scanned my bananas, froze, and summoned a human "
    "to accuse me of stealing them. She typed a secret code, looked at "
    "nothing, and forgave me on the spot. I have a degree and a spotless "
    "record, and the only institution that has ever treated me as a "
    "criminal is a shop machine. The charge: bananas."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
