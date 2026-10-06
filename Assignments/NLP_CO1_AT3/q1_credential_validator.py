import re

EMAIL_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(?:com|org|edu|net|in)")
PASSWORD_PATTERN = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}")
MOBILE_PATTERN = re.compile(r"[6-9]\d{9}")

TEST_CASES = [
    ("john.doe_12@gmail.com", "Strong@123", "9876543210"),
    ("1john@gmail.com", "password", "5876543210"),
    ("alice@mail2.com", "Alice#2026", "98765"),
    ("bob@university.edu", "bob@12345", "6123456789"),
    ("carol@site.xyz", "Carol$9999", "98765432101"),
    ("dave_x@domain.in", "Dave!2024", "8000000000"),
]


def validate_email(email):
    return EMAIL_PATTERN.fullmatch(email) is not None


def validate_password(password):
    return PASSWORD_PATTERN.fullmatch(password) is not None


def validate_mobile(mobile):
    return MOBILE_PATTERN.fullmatch(mobile) is not None


def check_credentials(email, password, mobile):
    print(f"Input      : {email} | {password} | {mobile}")
    print("Processing : matching against email, password and mobile patterns")
    print("Output     :", "Valid Email" if validate_email(email) else "Invalid Email")
    print("            ", "Strong Password" if validate_password(password) else "Weak Password")
    print("            ", "Valid Mobile Number" if validate_mobile(mobile) else "Invalid Mobile Number")


def run_test_cases():
    for number, (email, password, mobile) in enumerate(TEST_CASES, 1):
        print(f"\nTest Case {number}")
        check_credentials(email, password, mobile)


def read_credentials():
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()
    mobile = input("Enter mobile number: ").strip()
    print()
    check_credentials(email, password, mobile)


def main():
    actions = {"1": run_test_cases, "2": read_credentials}
    while True:
        print("\n1. Run test cases\n2. Enter credentials\n3. Exit")
        try:
            choice = input("Choice: ").strip()
        except EOFError:
            break
        if choice == "3":
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice")
            continue
        try:
            action()
        except EOFError:
            break


if __name__ == "__main__":
    main()
