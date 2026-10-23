import sys

VOWELS = set("aeiu")
SIBILANTS = set("sxz")

IRREGULAR = {
    "child": "children", "man": "men", "woman": "women", "foot": "feet",
    "tooth": "teeth", "mouse": "mice", "goose": "geese", "person": "people",
    "sheep": "sheep", "fish": "fish", "deer": "deer", "leaf": "leaves",
    "knife": "knives", "wolf": "wolves", "life": "lives", "photo": "photos",
    "piano": "pianos", "quiz": "quizzes",
}

SAMPLE_WORDS = [
    "cat", "dog", "bus", "box", "buzz", "church", "dish", "city", "baby",
    "boy", "day", "hero", "tomato", "child", "mouse", "sheep", "leaf", "photo",
]


def classify(ch):
    if ch in VOWELS:
        return "V"
    if ch == "o":
        return "O"
    if ch == "y":
        return "Y"
    if ch == "c":
        return "C"
    if ch == "h":
        return "H"
    if ch in SIBILANTS:
        return "S"
    return "K"


VOWEL_LIKE = {"VOW", "VO", "CO"}

TRANSITIONS = {
    "V": lambda state: "VOW",
    "O": lambda state: "VO" if state in VOWEL_LIKE else "CO",
    "Y": lambda state: "VY" if state in VOWEL_LIKE else "CY",
    "C": lambda state: "CH",
    "H": lambda state: "SIB" if state in {"CH", "SIB"} else "CONS",
    "S": lambda state: "SIB",
    "K": lambda state: "CONS",
}

OUTPUT = {
    "SIB": (0, "es"),
    "CO": (0, "es"),
    "CY": (1, "ies"),
}
DEFAULT_OUTPUT = (0, "s")


def run_machine(word):
    state = "START"
    path = [state]
    for ch in word:
        state = TRANSITIONS[classify(ch)](state)
        path.append(state)
    return state, path


def pluralize(word):
    word = word.lower().strip()
    if not word.isalpha():
        raise ValueError(f"'{word}' is not a valid word")
    if word in IRREGULAR:
        return IRREGULAR[word], "irregular", ["lookup"]
    state, path = run_machine(word)
    strip, suffix = OUTPUT.get(state, DEFAULT_OUTPUT)
    stem = word[:-strip] if strip else word
    return stem + suffix, state, path


def main():
    words = sys.argv[1:] or SAMPLE_WORDS
    print(f"{'Singular':<10}{'Plural':<12}{'Final state':<13}Path")
    print("-" * 70)
    for word in words:
        try:
            plural, state, path = pluralize(word)
        except ValueError as error:
            print(error)
            continue
        print(f"{word:<10}{plural:<12}{state:<13}{' > '.join(path)}")


if __name__ == "__main__":
    main()
