import re

NAME_LABEL = re.compile(r"^\s*name\s*[:\-]\s*([A-Za-z][A-Za-z .'-]+?)\s*$", re.I | re.M)
NAME_FIRST_LINE = re.compile(r"^\s*([A-Z][a-z]+(?:\s+[A-Z][a-z.]*){1,3})\s*$", re.M)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
MOBILE = re.compile(r"(?<!\d)(?:\+?91[\s-]?|0)?([6-9]\d{4}[\s-]?\d{5})(?!\d)")
EXPERIENCE = [
    re.compile(r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)(?:\s+of)?\s+(?:work\s+)?(?:experience|exp)\b", re.I),
    re.compile(r"experience\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)", re.I),
]
SKILLS = {
    "Python": re.compile(r"\bpython\b", re.I),
    "Java": re.compile(r"\bjava\b", re.I),
    "SQL": re.compile(r"\bsql\b", re.I),
    "Machine Learning": re.compile(r"\bmachine[\s-]+learning\b", re.I),
    "NLP": re.compile(r"\bnlp\b|\bnatural\s+language\s+processing\b", re.I),
}

RESUMES = [
    """Name: Arjun Kumar
Email: arjun.kumar@gmail.com | arjun.k@work.co.in
Mobile: +91 98765 43210
Skills: Python, SQL, Machine Learning, NLP
Summary: Data scientist with 4 years of experience in text analytics.""",
    """Priya Sharma
priya_sharma92@outlook.com
Phone: 9123456780
Technical Skills: Java, SQL, JavaScript
Experience: 5 years in backend development.""",
    """Name: Rahul Menon
Contact: rahul.menon@example.org, +91-90000-11111
Skills: Python, Natural Language Processing
Fresher with 1 year of experience in internships.""",
    """Name: Divya Lakshmi
Email: divya.lakshmi@mail.com
Mobile: 8765432109
Skills: Python, Java, Machine Learning
Total 2.5 years of experience in AI projects.""",
]


def extract_name(text):
    match = NAME_LABEL.search(text) or NAME_FIRST_LINE.search(text)
    return match.group(1).strip() if match else "Not found"


def extract_emails(text):
    return list(dict.fromkeys(EMAIL.findall(text)))


def extract_mobiles(text):
    return list(dict.fromkeys(re.sub(r"[\s-]", "", n) for n in MOBILE.findall(text)))


def extract_skills(text):
    return [skill for skill, pattern in SKILLS.items() if pattern.search(text)]


def extract_experience(text):
    for pattern in EXPERIENCE:
        match = pattern.search(text)
        if match:
            return float(match.group(1))
    return 0.0


def build_profile(text):
    return {
        "name": extract_name(text),
        "emails": extract_emails(text),
        "mobiles": extract_mobiles(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
    }


def is_eligible(profile):
    return profile["experience"] >= 2 and "Python" in profile["skills"]


def print_profile(number, profile):
    print(f"\nCandidate {number}")
    print(f"Name       : {profile['name']}")
    print(f"Email      : {', '.join(profile['emails']) or 'Not found'}")
    print(f"Mobile     : {', '.join(profile['mobiles']) or 'Not found'}")
    print(f"Skills     : {', '.join(profile['skills']) or 'None'}")
    print(f"Experience : {profile['experience']:g} year(s)")


def main():
    profiles = [build_profile(text) for text in RESUMES]
    for number, profile in enumerate(profiles, 1):
        print_profile(number, profile)

    print("\nEligible Candidates (2+ years and Python)")
    for profile in filter(is_eligible, profiles):
        print(f"- {profile['name']} | {profile['experience']:g} years | {', '.join(profile['skills'])}")


if __name__ == "__main__":
    main()
