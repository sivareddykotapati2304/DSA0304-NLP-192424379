import nltk

GRAMMAR = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'man' | 'dog' | 'telescope' | 'park'
V -> 'saw' | 'chased'
P -> 'with' | 'in'
""")

SENTENCES = [
    "the dog chased a man",
    "I saw the man with a telescope",
    "the man the saw dog",
]


def parse_sentence(sentence):
    parser = nltk.ChartParser(GRAMMAR)
    try:
        return list(parser.parse(sentence.split()))
    except ValueError as error:
        print("Error:", error)
        return []


def main():
    for sentence in SENTENCES:
        print(f"\nSentence: {sentence}")
        trees = parse_sentence(sentence)
        if not trees:
            print("No parse tree found")
            continue
        print(f"Number of parse trees: {len(trees)}")
        for number, tree in enumerate(trees, 1):
            print(f"\nTree {number}:")
            print(tree)
            tree.pretty_print()


if __name__ == "__main__":
    main()
