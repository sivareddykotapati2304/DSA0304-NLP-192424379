import nltk

GRAMMAR = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
PP -> P NP [1.0]
VP -> V NP [0.7] | VP PP [0.3]
NP -> Det N [0.5] | NP PP [0.2] | 'John' [0.3]
Det -> 'the' [0.6] | 'a' [0.4]
N -> 'man' [0.4] | 'dog' [0.3] | 'telescope' [0.3]
V -> 'saw' [1.0]
P -> 'with' [1.0]
""")

SENTENCES = [
    "John saw the man with a telescope",
    "John saw a dog",
]


def main():
    parser = nltk.ViterbiParser(GRAMMAR)
    for sentence in SENTENCES:
        print(f"\nSentence: {sentence}")
        for tree in parser.parse(sentence.split()):
            print(f"Most probable parse (probability = {tree.prob():.6f}):")
            tree.pretty_print()


if __name__ == "__main__":
    main()
