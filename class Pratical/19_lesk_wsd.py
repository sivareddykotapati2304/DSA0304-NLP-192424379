import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet", quiet=True)

STOPWORDS = {
    "a", "an", "the", "to", "of", "in", "on", "at", "and", "or", "is", "was",
    "i", "he", "she", "it", "we", "you", "they", "for", "with", "that", "this",
    "by", "as", "from", "my", "his", "her", "went", "will",
}

CASES = [
    ("I went to the bank to deposit my money", "bank"),
    ("The fisherman sat on the bank of the river", "bank"),
    ("The bat sleeps in the cave and hunts insects at night with its wings", "bat"),
    ("He used the bat to hit the ball in a game", "bat"),
]

lemmatizer = WordNetLemmatizer()


def clean(text):
    words = [w.strip(".,!?").lower() for w in text.split()]
    return {lemmatizer.lemmatize(w) for w in words if w and w not in STOPWORDS}


def signature(synset):
    text = synset.definition() + " " + " ".join(synset.examples())
    return clean(text)


def lesk(sentence, word):
    context = clean(sentence) - {word}
    best_sense, best_score = None, -1
    for synset in wordnet.synsets(word, pos=wordnet.NOUN):
        score = len(context & signature(synset))
        if score > best_score:
            best_sense, best_score = synset, score
    return best_sense, best_score


def main():
    for sentence, word in CASES:
        sense, score = lesk(sentence, word)
        print(f"\nSentence : {sentence}")
        print(f"Word     : {word}")
        print(f"Sense    : {sense.name()} (overlap = {score})")
        print(f"Meaning  : {sense.definition()}")


if __name__ == "__main__":
    main()
