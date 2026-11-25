#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Pure standard library, no network, deterministic:
the same bytes on every run.
"""

import os
import stat

# The rant (375 characters, under the 400 cap). A self-checkout machine
# accuses the shopper of stealing the very bag it just sold them.
RANT = (
    "The self-checkout just accused me of stealing my own groceries. "
    "'Unexpected item in the bagging area.' The item was the bag. "
    "I scanned it, I bagged it, I paid for it, and now a robot with "
    "the voice of a disappointed librarian is announcing to a queue "
    "of strangers that I am a criminal. I have never felt so judged "
    "by a machine that cannot count to three without a supervisor."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = RANT.encode("utf-8")
    assert 1 <= len(RANT) <= 400, "rant must be 1-400 characters"
    assert RANT.strip(), "rant must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644) and the folder 0755.
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
