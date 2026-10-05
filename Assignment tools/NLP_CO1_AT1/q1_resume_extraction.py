"""
Q1 - Regex-Based Resume Information Extraction
Course: DSA03 - Natural Language Processing (CO1)

Extracts name, email, mobile number, technical skills and years of experience
from plain-text resumes, builds a structured profile summary and lists the
candidates who meet the eligibility criteria (>= 2 years experience + Python).

Usage:
    python q1_resume_extraction.py              # runs on built-in sample resumes
    python q1_resume_extraction.py resumes_dir  # runs on every .txt file in a folder
"""
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- patterns --
NAME_LABEL = re.compile(r"^\s*name\s*[:\-]\s*([A-Za-z][A-Za-z .'-]+?)\s*$", re.I | re.M)
NAME_FIRST_LINE = re.compile(r"^\s*([A-Z][a-z]+(?:\s+[A-Z][a-z.]*){1,3})\s*$", re.M)

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")

# Indian mobile numbers: optional +91 / 91 / 0 prefix, starts with 6-9, 10 digits
MOBILE = re.compile(r"(?<!\d)(?:\+?91[\s-]?|0)?([6-9]\d{4}[\s-]?\d{5})(?!\d)")

SKILLS = {
    "Python": re.compile(r"\bpython\b", re.I),
    "Java": re.compile(r"\bjava\b", re.I),  # \b stops it matching JavaScript
    "SQL": re.compile(r"\bsql\b", re.I),
    "Machine Learning": re.compile(r"\bmachine[\s-]+learning\b", re.I),
    "NLP": re.compile(r"\bnlp\b|\bnatural\s+language\s+processing\b", re.I),
}

# "3 years of experience", "2+ yrs experience", "Experience: 4.5 years"
EXP_PATTERNS = [
    re.compile(r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)(?:\s+of)?\s+(?:work\s+)?(?:experience|exp)\b", re.I),
    re.compile(r"experience\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)", re.I),
]

MIN_EXPERIENCE = 2.0
REQUIRED_SKILL = "Python"


# --------------------------------------------------------------- extractors --
def extract_name(text):
    m = NAME_LABEL.search(text) or NAME_FIRST_LINE.search(text)
    return m.group(1).strip() if m else "Not found"


def extract_emails(text):
    return list(dict.fromkeys(EMAIL.findall(text)))  # unique, order preserved


def extract_mobiles(text):
    numbers = []
    for digits in MOBILE.findall(text):
        clean = re.sub(r"[\s-]", "", digits)
        if clean not in numbers:
            numbers.append(clean)
    return numbers


def extract_skills(text):
    return [skill for skill, pat in SKILLS.items() if pat.search(text)]


def extract_experience(text):
    for pat in EXP_PATTERNS:
        m = pat.search(text)
        if m:
            return float(m.group(1))
    return 0.0


# ------------------------------------------------------------------ profile --
def build_profile(text):
    return {
        "name": extract_name(text),
        "emails": extract_emails(text),
        "mobiles": extract_mobiles(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
    }


def is_eligible(profile):
    return profile["experience"] >= MIN_EXPERIENCE and REQUIRED_SKILL in profile["skills"]


def print_profile(profile, index):
    print(f"\nCandidate {index}")
    print("-" * 40)
    print(f"Name       : {profile['name']}")
    print(f"Email      : {', '.join(profile['emails']) or 'Not found'}")
    print(f"Mobile     : {', '.join(profile['mobiles']) or 'Not found'}")
    print(f"Skills     : {', '.join(profile['skills']) or 'None detected'}")
    print(f"Experience : {profile['experience']:g} year(s)")
    print(f"Eligible   : {'YES' if is_eligible(profile) else 'NO'}")


# ------------------------------------------------------------- sample data --
SAMPLE_RESUMES = {
    "resume_1": """Name: Arjun Kumar
Email: arjun.kumar@gmail.com | arjun.k@work.co.in
Mobile: +91 98765 43210
Skills: Python, SQL, Machine Learning, NLP
Summary: Data scientist with 4 years of experience in text analytics.""",

    "resume_2": """Priya Sharma
priya_sharma92@outlook.com
Phone: 9123456780
Technical Skills: Java, SQL, JavaScript
Experience: 5 years in backend development.""",

    "resume_3": """Name: Rahul Menon
Contact: rahul.menon@example.org, +91-90000-11111
Skills: Python, Natural Language Processing
Fresher with 1 year of experience in internships.""",

    "resume_4": """Name: Divya Lakshmi
Email: divya.lakshmi@mail.com
Mobile: 8765432109
Skills: Python, Java, Machine Learning
Total 2.5 years of experience in AI projects.""",
}


def load_resumes(argv):
    if len(argv) > 1:
        folder = Path(argv[1])
        if not folder.is_dir():
            sys.exit(f"Error: '{folder}' is not a directory.")
        resumes = {}
        for f in sorted(folder.glob("*.txt")):
            try:
                resumes[f.stem] = f.read_text(encoding="utf-8")
            except OSError as err:
                print(f"Warning: could not read {f.name}: {err}")
        return resumes
    return SAMPLE_RESUMES


def main():
    resumes = load_resumes(sys.argv)
    if not resumes:
        sys.exit("No resumes found.")

    profiles = []
    for i, (_, text) in enumerate(resumes.items(), start=1):
        profile = build_profile(text)
        profiles.append(profile)
        print_profile(profile, i)

    print("\n" + "=" * 60)
    print(f"ELIGIBLE CANDIDATES (>= {MIN_EXPERIENCE:g} yrs experience and {REQUIRED_SKILL})")
    print("=" * 60)
    eligible = [p for p in profiles if is_eligible(p)]
    if eligible:
        for p in eligible:
            print(f"- {p['name']:<18} {p['experience']:g} yrs | {', '.join(p['skills'])}")
    else:
        print("No candidate satisfies the criteria.")
    print(f"\nTotal resumes: {len(profiles)} | Shortlisted: {len(eligible)}")


if __name__ == "__main__":
    main()
