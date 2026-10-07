import os

import nltk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize

for resource in ("wordnet", "averaged_perceptron_tagger_eng"):
    nltk.download(resource, quiet=True)

TEXT = "The children were running quickly and the unhappy dogs studied better strategies."

PREFIXES = ("un", "re", "dis", "pre", "mis", "non", "over")
DOUBLING_ENDINGS = ("ing", "ed", "er", "est")

FEATURES = {
    "NN": "singular noun",
    "NNS": "plural noun",
    "VB": "base verb",
    "VBD": "past tense",
    "VBG": "present participle",
    "VBN": "past participle",
    "VBP": "present tense",
    "VBZ": "3rd person singular",
    "JJ": "adjective",
    "JJR": "comparative adjective",
    "JJS": "superlative adjective",
    "RB": "adverb",
}

WORDNET_POS = {"J": wordnet.ADJ, "V": wordnet.VERB, "N": wordnet.NOUN, "R": wordnet.ADV}

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def to_wordnet_pos(tag):
    return WORDNET_POS.get(tag[0], wordnet.NOUN)


def find_prefix(word):
    for prefix in PREFIXES:
        rest = word[len(prefix):]
        if word.startswith(prefix) and len(rest) >= 4 and wordnet.synsets(rest):
            return prefix
    return "-"


def find_suffix(word, lemma):
    shared = os.path.commonprefix([word, lemma])
    if not shared:
        return "irregular" if word != lemma else "-"
    suffix = word[len(shared):]
    if suffix and suffix[0] == shared[-1] and suffix[1:] in DOUBLING_ENDINGS:
        suffix = suffix[1:]
    return suffix or "-"


def analyse(word, tag):
    lowered = word.lower()
    lemma = lemmatizer.lemmatize(lowered, to_wordnet_pos(tag))
    return {
        "word": word,
        "tag": tag,
        "lemma": lemma,
        "stem": stemmer.stem(lowered),
        "prefix": find_prefix(lowered),
        "suffix": find_suffix(lowered, lemma),
        "feature": FEATURES.get(tag, "other"),
    }


def print_table(rows):
    header = f"{'Word':<12}{'POS':<6}{'Lemma':<12}{'Stem':<11}{'Prefix':<8}{'Suffix':<11}Feature"
    print(header)
    print("-" * len(header) + "-" * 20)
    for r in rows:
        print(f"{r['word']:<12}{r['tag']:<6}{r['lemma']:<12}{r['stem']:<11}{r['prefix']:<8}{r['suffix']:<11}{r['feature']}")


def main():
    tokens = [t for t in wordpunct_tokenize(TEXT) if t.isalpha()]
    print("Text:", TEXT, "\n")
    rows = [analyse(word, tag) for word, tag in pos_tag(tokens)]
    print_table(rows)


if __name__ == "__main__":
    main()
