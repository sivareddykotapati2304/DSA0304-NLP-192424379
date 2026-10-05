import re

products = [
    "Apple iPhone 15", "Samsung Galaxy Phone", "Wireless Headphones",
    "Bluetooth Speaker", "Smart Watch", "Gaming Laptop", "Laptop Bag",
    "Laptop Stand", "Phone Case", "Phone Charger", "Mechanical Keyboard",
    "Wireless Mouse", "USB Cable", "Power Bank", "Headphone Stand",
    "Smartphone Gimbal", "Notebook", "Cable Organizer", "Webcam HD",
    "Earphones", "Tablet Cover", "Charger Cable",
]


def search(keyword, mode, ignore_case=True):
    kw = re.escape(keyword)
    patterns = {
        "exact": rf"\b{kw}\b",
        "prefix": rf"\b{kw}\w*",
        "suffix": rf"\w*{kw}\b",
        "partial": kw,
    }
    regex = re.compile(patterns[mode], re.I if ignore_case else 0)
    return [p for p in products if regex.search(p)]


tests = [
    ("laptop", "exact", True),
    ("phone", "prefix", True),
    ("phone", "suffix", True),
    ("phone", "partial", True),
    ("WIRELESS", "exact", True),
    ("WIRELESS", "exact", False),
    ("cable", "partial", True),
    ("xyz", "partial", True),
]

report = []
for keyword, mode, ignore_case in tests:
    results = search(keyword, mode, ignore_case)
    label = f"{mode} '{keyword}' ({'ignore case' if ignore_case else 'case sensitive'})"
    print(f"\n{label}")
    print("\n".join(f"  - {r}" for r in results) or "  No match")
    report.append((label, len(results)))

print("\nReport")
for label, count in report:
    print(f"{label:<40}{count}")
