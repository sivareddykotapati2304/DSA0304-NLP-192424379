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
    "dog the chased cat",
]


def add(column, state):
    if state not in column:
        column.append(state)


def earley(tokens):
    chart = [[] for _ in range(len(tokens) + 1)]
    add(chart[0], ("START", ("S",), 0, 0))
    for i, column in enumerate(chart):
        for lhs, rhs, dot, origin in column:
            if dot < len(rhs):
                symbol = rhs[dot]
                if symbol in GRAMMAR:
                    for production in GRAMMAR[symbol]:
                        add(column, (symbol, tuple(production), 0, i))
                elif i < len(tokens) and tokens[i] == symbol:
                    add(chart[i + 1], (lhs, rhs, dot + 1, origin))
            else:
                for p_lhs, p_rhs, p_dot, p_origin in chart[origin]:
                    if p_dot < len(p_rhs) and p_rhs[p_dot] == lhs:
                        add(column, (p_lhs, p_rhs, p_dot + 1, p_origin))
    return chart


def show(state):
    lhs, rhs, dot, origin = state
    symbols = list(rhs[:dot]) + ["."] + list(rhs[dot:])
    return f"{lhs} -> {' '.join(symbols)} [{origin}]"


def main():
    for sentence in SENTENCES:
        tokens = sentence.lower().split()
        chart = earley(tokens)
        accepted = ("START", ("S",), 1, 0) in chart[-1]
        print(f"\nSentence: {sentence}")
        print(f"Chart sizes: {[len(column) for column in chart]}")
        print("Completed S states:")
        for state in chart[-1]:
            if state[0] == "S" and state[2] == len(state[1]):
                print("  ", show(state))
        print("Result:", "Accepted" if accepted else "Rejected")


if __name__ == "__main__":
    main()
