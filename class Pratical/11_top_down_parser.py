GRAMMAR = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["Det", "Adj", "N"], ["Name"]],
    "VP": [["V", "NP"], ["V", "NP", "PP"], ["V"]],
    "PP": [["P", "NP"]],
    "Det": [["the"], ["a"]],
    "Adj": [["big"], ["small"]],
    "N": [["dog"], ["cat"], ["park"]],
    "Name": [["john"], ["mary"]],
    "V": [["chased"], ["saw"], ["slept"]],
    "P": [["in"], ["with"]],
}

SENTENCES = [
    "the dog chased a cat",
    "john saw the big dog in the park",
    "mary slept",
    "dog the chased cat",
    "the the dog chased cat",
]


def parse(symbol, tokens, pos):
    if symbol not in GRAMMAR:
        if pos < len(tokens) and tokens[pos] == symbol:
            yield pos + 1
        return
    for production in GRAMMAR[symbol]:
        yield from parse_sequence(production, tokens, pos)


def parse_sequence(symbols, tokens, pos):
    if not symbols:
        yield pos
        return
    for middle in parse(symbols[0], tokens, pos):
        yield from parse_sequence(symbols[1:], tokens, middle)


def accepts(sentence):
    tokens = sentence.lower().split()
    return any(end == len(tokens) for end in parse("S", tokens, 0))


def main():
    for sentence in SENTENCES:
        result = "Accepted" if accepts(sentence) else "Rejected"
        print(f"{sentence:<40}{result}")


if __name__ == "__main__":
    main()
