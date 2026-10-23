import nltk

GRAMMAR = nltk.CFG.fromstring("""
S -> NP_SG VP_SG | NP_PL VP_PL
NP_SG -> Det_SG N_SG
NP_PL -> Det_PL N_PL
NP -> NP_SG | NP_PL
VP_SG -> V_SG | V_SG NP
VP_PL -> V_PL | V_PL NP
Det_SG -> 'a' | 'the' | 'this'
Det_PL -> 'the' | 'these' | 'some'
N_SG -> 'dog' | 'cat' | 'student'
N_PL -> 'dogs' | 'cats' | 'students'
V_SG -> 'chases' | 'sees' | 'runs'
V_PL -> 'chase' | 'see' | 'run'
""")

NOUNS = {"dog": "singular", "cat": "singular", "student": "singular",
         "dogs": "plural", "cats": "plural", "students": "plural"}
VERBS = {"chases": "singular", "sees": "singular", "runs": "singular",
         "chase": "plural", "see": "plural", "run": "plural"}

SENTENCES = [
    "the dog chases a cat",
    "the dogs chase the cat",
    "these students run",
    "the dog chase a cat",
    "the dogs chases the cat",
    "this students runs",
]


def is_grammatical(tokens):
    parser = nltk.ChartParser(GRAMMAR)
    return any(True for _ in parser.parse(tokens))


def explain(tokens):
    nouns = [(w, NOUNS[w]) for w in tokens if w in NOUNS]
    verbs = [(w, VERBS[w]) for w in tokens if w in VERBS]
    if nouns and verbs and nouns[0][1] != verbs[0][1]:
        return f"subject '{nouns[0][0]}' is {nouns[0][1]} but verb '{verbs[0][0]}' is {verbs[0][1]}"
    return "sentence does not follow the grammar"


def main():
    for sentence in SENTENCES:
        tokens = sentence.split()
        if is_grammatical(tokens):
            print(f"{sentence:<28}Agreement OK")
        else:
            print(f"{sentence:<28}Agreement ERROR: {explain(tokens)}")


if __name__ == "__main__":
    main()
