import re

DEFAULT_TEXT = "Meeting on 12/09/2026 Call 9876543210 #NLP @OpenAI natural language processing"

DATE = re.compile(r"\b\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}\b")
PHONE = re.compile(r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)")
HASHTAG = re.compile(r"(?<!\w)#\w+")
MENTION = re.compile(r"(?<!\w)@\w+")


def find_all(pattern, text):
    return pattern.findall(text)


def word_search(text, word):
    return re.findall(rf"\b{re.escape(word)}\b", text, re.I)


def prefix_search(text, prefix):
    return re.findall(rf"\b{re.escape(prefix)}\w*", text, re.I)


def suffix_search(text, suffix):
    return re.findall(rf"\w*{re.escape(suffix)}\b", text, re.I)


def show(title, matches):
    print(f"Processing : {title}")
    if matches:
        print(f"Output     : {len(matches)} match(es)")
        for match in matches:
            print(f"  - {match}")
    else:
        print("Output     : No match found")


def ask(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("input must not be empty")
    return value


def handle(choice, text):
    if choice == "1":
        show("date pattern", find_all(DATE, text))
    elif choice == "2":
        show("phone number pattern", find_all(PHONE, text))
    elif choice == "3":
        show("hashtag pattern", find_all(HASHTAG, text))
    elif choice == "4":
        show("mention pattern", find_all(MENTION, text))
    elif choice == "5":
        prefix = ask("Enter prefix: ")
        show(f"words starting with '{prefix}'", prefix_search(text, prefix))
    elif choice == "6":
        suffix = ask("Enter suffix: ")
        show(f"words ending with '{suffix}'", suffix_search(text, suffix))
    elif choice == "7":
        word = ask("Enter word: ")
        show(f"whole word '{word}'", word_search(text, word))
    else:
        print("Invalid choice")


def main():
    text = DEFAULT_TEXT
    while True:
        print(f"\nText: {text}")
        print("1.Search Date\n2.Search Phone Number\n3.Search Hashtag\n4.Search Mention")
        print("5.Search Prefix\n6.Search Suffix\n7.Search Word\n8.Change Text\n9.Exit")
        try:
            choice = input("Choice: ").strip()
            if choice == "9":
                break
            if choice == "8":
                text = ask("Enter new text: ")
            else:
                handle(choice, text)
        except ValueError as error:
            print("Error:", error)
        except EOFError:
            break


if __name__ == "__main__":
    main()
