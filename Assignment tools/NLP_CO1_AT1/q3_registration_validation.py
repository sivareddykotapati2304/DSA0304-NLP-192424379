"""
Q3 - Regex-Based University Registration Validation
Course: DSA03 - Natural Language Processing (CO1)

Validates register number, institutional email, course code, semester and
mobile number, prints a message per field and a final registration status.

Validation rules (edit the constants below to match your institution):
  Register number : exactly 9 digits (e.g. 192211234)
  Institutional email : name@saveetha.com (sub-domains allowed)
  Course code     : 3 capital letters + 2 digits (e.g. DSA03)
  Semester        : 1-8, optionally written as "Semester 3" / "Sem 3"
  Mobile number   : 10 digits starting 6-9, optional +91 / 91 prefix

Usage:
    python q3_registration_validation.py                # runs the test cases
    python q3_registration_validation.py --interactive  # enter one student's data
"""
import re
import sys

EMAIL_DOMAIN = "saveetha.com"

RULES = {
    "Register Number": (re.compile(r"^\d{9}$"), "9 digits, e.g. 192211234"),
    "Institutional Email": (
        re.compile(rf"^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)*{re.escape(EMAIL_DOMAIN)}$", re.I),
        f"name@{EMAIL_DOMAIN}",
    ),
    "Course Code": (re.compile(r"^[A-Z]{3}\d{2}$"), "3 capital letters + 2 digits, e.g. DSA03"),
    "Semester": (re.compile(r"^(?:sem(?:ester)?\s*)?[1-8]$", re.I), "a number from 1 to 8"),
    "Mobile Number": (re.compile(r"^(?:\+?91[\s-]?)?[6-9]\d{9}$"), "10 digits starting with 6-9"),
}


def validate_field(field, value):
    """Return (is_valid, message) for one field."""
    value = value.strip() if isinstance(value, str) else ""
    if not value:
        return False, f"{field}: INVALID - field is empty"
    pattern, expected = RULES[field]
    if pattern.fullmatch(value):
        return True, f"{field}: VALID   - '{value}'"
    return False, f"{field}: INVALID - '{value}' (expected {expected})"


def validate_student(student):
    """Validate all fields; print messages and the final status. Returns True if all valid."""
    all_valid, failed = True, []
    for field in RULES:
        ok, message = validate_field(field, student.get(field, ""))
        print("  " + message)
        if not ok:
            all_valid = False
            failed.append(field)

    print("  " + "-" * 50)
    if all_valid:
        print("  REGISTRATION STATUS: SUCCESSFUL")
    else:
        print(f"  REGISTRATION STATUS: FAILED (fix: {', '.join(failed)})")
    return all_valid


TEST_CASES = [
    ("Valid student", {
        "Register Number": "192211234", "Institutional Email": "arun.kumar@saveetha.com",
        "Course Code": "DSA03", "Semester": "5", "Mobile Number": "+91 9876543210"}),
    ("Invalid register number & email", {
        "Register Number": "19221", "Institutional Email": "arun@gmail.com",
        "Course Code": "DSA03", "Semester": "Semester 3", "Mobile Number": "9876543210"}),
    ("Invalid course, semester & mobile", {
        "Register Number": "192211235", "Institutional Email": "priya@saveetha.com",
        "Course Code": "dsa3", "Semester": "9", "Mobile Number": "1234567890"}),
    ("Empty fields", {
        "Register Number": "", "Institutional Email": "", "Course Code": "", "Semester": "", "Mobile Number": ""}),
]


def demo():
    results = []
    for title, student in TEST_CASES:
        print(f"\nTest case: {title}")
        results.append((title, validate_student(student)))
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    for title, ok in results:
        print(f"{title:<38}{'SUCCESS' if ok else 'FAILED'}")


def interactive():
    student = {field: input(f"Enter {field}: ") for field in RULES}
    print()
    validate_student(student)


if __name__ == "__main__":
    interactive() if "--interactive" in sys.argv else demo()
