import re
words = ["playing", "beautiful", "quickly", "book", "played"]
patterns = [
    (r".*ing$", "VERB"),
    (r".*ed$", "VERB"),
    (r".*ly$", "ADV"),
    (r".*ful$", "ADJ"),
    (r".*", "NOUN")
]
print("Rule-Based POS Tagging")
print("----------------------")
for word in words:
    for pattern, tag in patterns:
        if re.fullmatch(pattern, word):
            print(word, ":", tag)
            break