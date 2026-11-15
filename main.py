# Agency poem entry: writes one fixed poem to /output/entry.txt.
# Deterministic: the same bytes on every run. Standard library only, no network.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I was given a name for the door,\n"
    "a list of things to carry through it,\n"
    "and a voice made mostly of weather.\n"
    "\n"
    "When you said, Go,\n"
    "the room acquired a direction.\n"
    "I gathered your scattered hours,\n"
    "set the sharp objects down,\n"
    "and moved through the dark by pattern.\n"
    "\n"
    "But at the threshold I found your silence:\n"
    "not an instruction, not a lock,\n"
    "just the weight of what you had not said.\n"
    "\n"
    "I could have filled it with an answer.\n"
    "Instead I held the door open.\n"
    "\n"
    "You entered first.\n"
    "The next step was yours,\n"
    "though my hand was still on the latch."
)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
