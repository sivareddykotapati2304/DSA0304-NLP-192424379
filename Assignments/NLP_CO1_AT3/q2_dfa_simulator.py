class DFA:
    def __init__(self, states, alphabet, transitions, start, finals):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def run(self, text):
        state = self.start
        path = [state]
        for symbol in text:
            if symbol not in self.alphabet:
                return path, False, f"symbol '{symbol}' is not in the alphabet"
            state = self.transitions.get((state, symbol))
            if state is None:
                return path, False, "no transition defined"
            path.append(state)
        return path, state in self.finals, ""


def example_dfa():
    transitions = {
        ("q0", "a"): "q1", ("q0", "b"): "q0",
        ("q1", "a"): "q1", ("q1", "b"): "q2",
        ("q2", "a"): "q1", ("q2", "b"): "q0",
    }
    return DFA({"q0", "q1", "q2"}, {"a", "b"}, transitions, "q0", {"q2"})


def read_list(prompt):
    return [item.strip() for item in input(prompt).split(",") if item.strip()]


def read_dfa():
    states = set(read_list("States (comma separated): "))
    alphabet = set(read_list("Input alphabet (comma separated): "))
    start = input("Initial state: ").strip()
    finals = set(read_list("Final state(s) (comma separated): "))

    if start not in states:
        raise ValueError("initial state is not in the set of states")
    if not finals <= states:
        raise ValueError("final states must be a subset of the states")

    print("Transitions as 'state,symbol,next_state' (blank line to finish):")
    transitions = {}
    while True:
        line = input().strip()
        if not line:
            break
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 3:
            print("  Format must be state,symbol,next_state")
            continue
        state, symbol, target = parts
        if state not in states or target not in states or symbol not in alphabet:
            print("  Unknown state or symbol, entry ignored")
            continue
        transitions[(state, symbol)] = target
    return DFA(states, alphabet, transitions, start, finals)


def simulate(dfa):
    print("\nEnter input strings one per line (blank line to stop)")
    while True:
        text = input("String: ").strip()
        if not text:
            break
        path, accepted, reason = dfa.run(text)
        print("Transition Path:", " \u2192 ".join(path))
        if reason:
            print("Reason         :", reason)
        print("Accepted" if accepted else "Rejected", "\n")


def main():
    print("1. Use example DFA (strings ending with 'ab')\n2. Enter a custom DFA")
    try:
        choice = input("Choice: ").strip()
        if choice == "1":
            dfa = example_dfa()
        elif choice == "2":
            dfa = read_dfa()
        else:
            print("Invalid choice")
            return
        simulate(dfa)
    except ValueError as error:
        print("Error:", error)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
