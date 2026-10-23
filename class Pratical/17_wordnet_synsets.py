import nltk
from nltk.corpus import wordnet

nltk.download("wordnet", quiet=True)

WORD = "bank"


def show_synsets(word, limit=4):
    synsets = wordnet.synsets(word)
    print(f"'{word}' has {len(synsets)} synsets\n")
    for synset in synsets[:limit]:
        print(f"Synset     : {synset.name()}")
        print(f"Category   : {synset.pos()}")
        print(f"Meaning    : {synset.definition()}")
        print(f"Example    : {synset.examples()[:1]}")
        print(f"Synonyms   : {synset.lemma_names()}")
        print(f"Hypernyms  : {[h.name() for h in synset.hypernyms()]}")
        print(f"Hyponyms   : {[h.name() for h in synset.hyponyms()][:3]}\n")


def show_antonyms(word):
    antonyms = {a.name() for s in wordnet.synsets(word) for l in s.lemmas() for a in l.antonyms()}
    print(f"Antonyms of '{word}':", sorted(antonyms))


def show_similarity(first, second):
    a, b = wordnet.synsets(first)[0], wordnet.synsets(second)[0]
    print(f"Similarity of '{first}' and '{second}': {a.path_similarity(b):.2f}")


def main():
    show_synsets(WORD)
    show_antonyms("good")
    show_similarity("dog", "cat")
    show_similarity("dog", "car")


if __name__ == "__main__":
    main()
