import re

RULES = {
    "Register Number": re.compile(r"\d{9}"),
    "Institutional Email": re.compile(r"[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)*saveetha\.com", re.I),
    "Course Code": re.compile(r"[A-Z]{3}\d{2}"),
    "Semester": re.compile(r"(?:sem(?:ester)?\s*)?[1-8]", re.I),
    "Mobile Number": re.compile(r"(?:\+?91[\s-]?)?[6-9]\d{9}"),
}

STUDENTS = [
    {"Register Number": "192211234", "Institutional Email": "arun.kumar@saveetha.com",
     "Course Code": "DSA03", "Semester": "5", "Mobile Number": "+91 9876543210"},
    {"Register Number": "19221", "Institutional Email": "arun@gmail.com",
     "Course Code": "DSA03", "Semester": "Semester 3", "Mobile Number": "9876543210"},
    {"Register Number": "192211235", "Institutional Email": "priya@saveetha.com",
     "Course Code": "dsa3", "Semester": "9", "Mobile Number": "1234567890"},
]


def is_valid(field, value):
    return RULES[field].fullmatch(value.strip()) is not None


def validate_student(student):
    all_valid = True
    for field in RULES:
        value = student.get(field, "")
        valid = is_valid(field, value)
        all_valid = all_valid and valid
        print(f"{field}: {'Valid' if valid else 'Invalid'} ({value.strip() or 'empty'})")
    print("Registration Status:", "Successful" if all_valid else "Failed")


def main():
    for number, student in enumerate(STUDENTS, 1):
        print(f"\nStudent {number}")
        validate_student(student)


if __name__ == "__main__":
    main()
