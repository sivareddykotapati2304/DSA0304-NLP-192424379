import re

rules = {
    "Register Number": r"\d{9}",
    "Institutional Email": r"[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)*saveetha\.com",
    "Course Code": r"[A-Z]{3}\d{2}",
    "Semester": r"(?:sem(?:ester)?\s*)?[1-8]",
    "Mobile Number": r"(?:\+?91[\s-]?)?[6-9]\d{9}",
}

students = [
    {"Register Number": "192211234", "Institutional Email": "arun.kumar@saveetha.com",
     "Course Code": "DSA03", "Semester": "5", "Mobile Number": "+91 9876543210"},
    {"Register Number": "19221", "Institutional Email": "arun@gmail.com",
     "Course Code": "DSA03", "Semester": "Semester 3", "Mobile Number": "9876543210"},
    {"Register Number": "192211235", "Institutional Email": "priya@saveetha.com",
     "Course Code": "dsa3", "Semester": "9", "Mobile Number": "1234567890"},
]


def validate(student):
    valid = True
    for field, pattern in rules.items():
        value = student.get(field, "").strip()
        ok = re.fullmatch(pattern, value, re.I if field in ("Institutional Email", "Semester") else 0) is not None
        print(f"{field}: {'Valid' if ok else 'Invalid'} ({value or 'empty'})")
        valid = valid and ok
    print("Registration Status:", "Successful" if valid else "Failed")


for i, s in enumerate(students, 1):
    print(f"\nStudent {i}")
    validate(s)
