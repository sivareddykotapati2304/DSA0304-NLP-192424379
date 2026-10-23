import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
text = "The boy plays cricket"
words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)
print("Words and POS Tags:")
for word, tag in tags:
    print(word, ":", tag)