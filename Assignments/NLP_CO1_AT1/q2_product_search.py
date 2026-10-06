import re

PRODUCTS = [
    "Apple iPhone 15", "Samsung Galaxy Phone", "Wireless Headphones",
    "Bluetooth Speaker", "Smart Watch", "Gaming Laptop", "Laptop Bag",
    "Laptop Stand", "Phone Case", "Phone Charger", "Mechanical Keyboard",
    "Wireless Mouse", "USB Cable", "Power Bank", "Headphone Stand",
    "Smartphone Gimbal", "Notebook", "Cable Organizer", "Webcam HD",
    "Earphones", "Tablet Cover", "Charger Cable",
]

SEARCHES = [
    ("laptop", "exact", True),
    ("phone", "prefix", True),
    ("phone", "suffix", True),
    ("phone", "partial", True),
    ("WIRELESS", "exact", True),
    ("WIRELESS", "exact", False),
    ("cable", "partial", True),
    ("xyz", "partial", True),
]


def build_pattern(keyword, mode):
    word = re.escape(keyword)
    return {
        "exact": rf"\b{word}\b",
        "prefix": rf"\b{word}\w*",
        "suffix": rf"\w*{word}\b",
        "partial": word,
    }[mode]


def search(keyword, mode, ignore_case):
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(build_pattern(keyword, mode), flags)
    return [product for product in PRODUCTS if regex.search(product)]


def main():
    report = []
    for keyword, mode, ignore_case in SEARCHES:
        results = search(keyword, mode, ignore_case)
        case = "ignore case" if ignore_case else "case sensitive"
        label = f"{mode} '{keyword}' ({case})"
        print(f"\n{label}")
        for product in results:
            print(f"  - {product}")
        if not results:
            print("  No match")
        report.append((label, len(results)))

    print("\nReport")
    for label, count in report:
        print(f"{label:<40}{count}")


if __name__ == "__main__":
    main()
