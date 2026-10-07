from collections import defaultdict

from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

WORDS = [
    "running", "runs", "ran", "easily", "fairly", "studies", "studying",
    "studied", "connect", "connected", "connection", "connecting",
    "generalization", "generous", "happiness", "caring", "universal", "university",
]

SENTENCE = "The students were studying connected systems and running experiments quickly."

stemmer = PorterStemmer(PorterStemmer.ORIGINAL_ALGORITHM)


def stem_words(words):
    return [(word, stemmer.stem(word)) for word in words]


def group_by_stem(pairs):
    groups = defaultdict(list)
    for word, stem in pairs:
        groups[stem].append(word)
    return groups


def print_pairs(pairs):
    print(f"{'Word':<18}Stem")
    print("-" * 30)
    for word, stem in pairs:
        print(f"{word:<18}{stem}")


def print_groups(groups):
    print(f"{'Stem':<12}Words")
    print("-" * 50)
    for stem, words in groups.items():
        print(f"{stem:<12}{', '.join(words)}")


def main():
    pairs = stem_words(WORDS)
    print("Stemming a word list\n")
    print_pairs(pairs)

    print("\nWords grouped by stem\n")
    print_groups(group_by_stem(pairs))

    tokens = [t for t in wordpunct_tokenize(SENTENCE.lower()) if t.isalpha()]
    print("\nStemming a sentence\n")
    print("Original:", SENTENCE)
    print("Stemmed :", " ".join(stemmer.stem(t) for t in tokens))


if __name__ == "__main__":
    main()
