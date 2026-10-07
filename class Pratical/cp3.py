def fsa(string):
    state = "q0"

    for ch in string:
        if state == "q0" and ch == "a":
            state = "q1"
            print(True)

        elif state == "q1" and ch == "a":
            state = "q2"
            print(True)

        elif state == "q2" and ch == "b":
            state = "q3"
            print(True)

        else:
            print(False)
            break


string = "aab"
fsa(string)
