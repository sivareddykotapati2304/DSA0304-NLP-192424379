import random
words = ["I", "play", "cricket"]
probabilities = {
    "I": [("PRON", 0.9), ("NOUN", 0.1)],
    "play": [("VERB", 0.8), ("NOUN", 0.2)],
    "cricket": [("NOUN", 0.9), ("VERB", 0.1)]
}
for word in words:
    tags, probs = zip(*probabilities[word])
    tag = random.choices(tags, weights=probs)[0]
    print(word, ":", tag)