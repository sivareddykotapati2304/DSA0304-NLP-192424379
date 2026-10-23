import math
import re
from collections import Counter

DOCUMENTS = [
    "Natural language processing helps computers understand human language",
    "Machine learning models learn patterns from data",
    "Search engines rank documents using term frequency and inverse document frequency",
    "Deep learning improves natural language processing and machine translation",
    "Football is a popular sport played by millions of people",
]

QUERIES = [
    "natural language processing",
    "document ranking with term frequency",
    "football sport",
]

STOPWORDS = {"a", "an", "the", "is", "of", "and", "by", "from", "using", "with", "helps"}


def tokenize(text):
    return [w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOPWORDS]


def inverse_document_frequency(documents):
    total = len(documents)
    counts = Counter(word for doc in documents for word in set(doc))
    return {word: math.log10(total / count) for word, count in counts.items()}


def tfidf_vector(tokens, idf):
    counts = Counter(tokens)
    return {w: (counts[w] / len(tokens)) * idf[w] for w in counts if w in idf}


def cosine(a, b):
    dot = sum(a[w] * b.get(w, 0) for w in a)
    norm = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return dot / norm if norm else 0.0


def rank(query, documents, idf, vectors):
    query_vector = tfidf_vector(tokenize(query), idf)
    scores = [(cosine(query_vector, vector), index) for index, vector in enumerate(vectors)]
    return sorted(scores, reverse=True)


def main():
    tokenized = [tokenize(doc) for doc in DOCUMENTS]
    idf = inverse_document_frequency(tokenized)
    vectors = [tfidf_vector(tokens, idf) for tokens in tokenized]

    for query in QUERIES:
        print(f"\nQuery: {query}")
        for score, index in rank(query, DOCUMENTS, idf, vectors):
            print(f"  Doc {index + 1}  score = {score:.4f}  {DOCUMENTS[index][:60]}")


if __name__ == "__main__":
    main()
