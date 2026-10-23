import re

TOKEN = re.compile(r"\s*(->|[A-Za-z_]\w*|[()&|~,])")

QUANTIFIERS = {"forall": "\u2200", "exists": "\u2203"}
SYMBOLS = {"and": " \u2227 ", "or": " \u2228 ", "implies": " \u2192 "}

EXPRESSIONS = [
    "Loves(john, mary)",
    "forall x (Man(x) -> Mortal(x))",
    "exists y (Dog(y) & Barks(y))",
    "~Hates(john, mary) & Loves(john, mary)",
    "forall x exists y Loves(x, y)",
    "Loves(john",
]


class ParseError(Exception):
    pass


def tokenize(text):
    tokens, pos = [], 0
    while pos < len(text.rstrip()):
        match = TOKEN.match(text, pos)
        if not match:
            raise ParseError(f"unexpected character at position {pos}")
        tokens.append(match.group(1))
        pos = match.end()
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def take(self, expected=None):
        token = self.peek()
        if token is None or (expected and token != expected):
            raise ParseError(f"expected '{expected}' but found '{token}'")
        self.pos += 1
        return token

    def formula(self):
        left = self.disjunction()
        if self.peek() == "->":
            self.take()
            return ("implies", left, self.formula())
        return left

    def disjunction(self):
        node = self.conjunction()
        while self.peek() == "|":
            self.take()
            node = ("or", node, self.conjunction())
        return node

    def conjunction(self):
        node = self.unary()
        while self.peek() == "&":
            self.take()
            node = ("and", node, self.unary())
        return node

    def unary(self):
        token = self.peek()
        if token == "~":
            self.take()
            return ("not", self.unary())
        if token in QUANTIFIERS:
            self.take()
            variable = self.take()
            return (token, variable, self.unary())
        if token == "(":
            self.take()
            node = self.formula()
            self.take(")")
            return node
        return self.atom()

    def atom(self):
        name = self.take()
        if not name[0].isalpha() or not name[0].isupper():
            raise ParseError(f"predicate '{name}' must start with a capital letter")
        self.take("(")
        terms = [self.take()]
        while self.peek() == ",":
            self.take()
            terms.append(self.take())
        self.take(")")
        return ("pred", name, tuple(terms))


def parse(text):
    parser = Parser(tokenize(text))
    tree = parser.formula()
    if parser.peek() is not None:
        raise ParseError(f"unexpected token '{parser.peek()}'")
    return tree


def to_string(node):
    kind = node[0]
    if kind == "pred":
        return f"{node[1]}({', '.join(node[2])})"
    if kind == "not":
        return "\u00ac" + to_string(node[1])
    if kind in QUANTIFIERS:
        return f"{QUANTIFIERS[kind]}{node[1]} {to_string(node[2])}"
    return f"({to_string(node[1])}{SYMBOLS[kind]}{to_string(node[2])})"


def main():
    for text in EXPRESSIONS:
        print(f"\nInput : {text}")
        try:
            tree = parse(text)
        except ParseError as error:
            print("Error :", error)
            continue
        print("Tree  :", tree)
        print("Output:", to_string(tree))


if __name__ == "__main__":
    main()
