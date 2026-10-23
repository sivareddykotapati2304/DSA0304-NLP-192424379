words = ["The", "boy", "plays", "football"]
tags = ["NOUN", "NOUN", "NOUN", "NOUN"]
for i, word in enumerate(words):
    if word.endswith("s"):
        tags[i] = "VERB"
print("Transformation-Based POS Tagging:")
for word, tag in zip(words, tags):
    print(word, ":", tag)