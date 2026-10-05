"""
Q2 - Regex-Based Product Search System
Course: DSA03 - Natural Language Processing (CO1)

Supports exact, prefix, suffix, partial and case-insensitive keyword search
over a product catalogue, prints the matching products and a summary report.

Usage:
    python q2_product_search.py                # runs the demo searches
    python q2_product_search.py --interactive  # choose search type and keyword
"""
import re
import sys

PRODUCTS = [
    "Apple iPhone 15", "Samsung Galaxy Phone", "Wireless Headphones",
    "Bluetooth Speaker", "Smart Watch", "Gaming Laptop", "Laptop Bag",
    "Laptop Stand", "Phone Case", "Phone Charger", "Mechanical Keyboard",
    "Wireless Mouse", "USB Cable", "Power Bank", "Headphone Stand",
    "Smartphone Gimbal", "Notebook", "Cable Organizer", "Webcam HD",
    "Earphones", "Tablet Cover", "Charger Cable",
]


def build_pattern(keyword, mode):
    """Return the regex string for the requested search mode."""
    kw = re.escape(keyword)
    patterns = {
        "exact": rf"\b{kw}\b",        # whole word
        "prefix": rf"\b{kw}\w*",      # word starts with keyword
        "suffix": rf"\w*{kw}\b",      # word ends with keyword
        "partial": kw,                # keyword anywhere
    }
    if mode not in patterns:
        raise ValueError(f"Unknown search mode: {mode}")
    return patterns[mode]


def search(products, keyword, mode="partial", ignore_case=True):
    """Return the list of products matching keyword in the given mode."""
    if not keyword or not keyword.strip():
        raise ValueError("Keyword must not be empty.")
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(build_pattern(keyword.strip(), mode), flags)
    return [p for p in products if regex.search(p)]


def run_and_record(report, products, keyword, mode, ignore_case=True):
    results = search(products, keyword, mode, ignore_case)
    label = f"{mode.capitalize()} | '{keyword}' | {'Case-insensitive' if ignore_case else 'Case-sensitive'}"
    print(f"\nSearch -> {label}")
    if results:
        for r in results:
            print(f"  - {r}")
    else:
        print("  (no matching products)")
    report.append((label, len(results)))


def print_report(report):
    print("\n" + "=" * 62)
    print("SEARCH REPORT")
    print("=" * 62)
    print(f"{'No.':<5}{'Search':<48}{'Matches':>7}")
    print("-" * 62)
    for i, (label, count) in enumerate(report, start=1):
        print(f"{i:<5}{label:<48}{count:>7}")
    print("-" * 62)
    print(f"Total matches across all searches: {sum(c for _, c in report)}")


def demo():
    report = []
    run_and_record(report, PRODUCTS, "laptop", "exact")
    run_and_record(report, PRODUCTS, "phone", "prefix")
    run_and_record(report, PRODUCTS, "phone", "suffix")
    run_and_record(report, PRODUCTS, "phone", "partial")
    run_and_record(report, PRODUCTS, "WIRELESS", "exact", ignore_case=True)
    run_and_record(report, PRODUCTS, "WIRELESS", "exact", ignore_case=False)
    run_and_record(report, PRODUCTS, "cable", "partial")
    run_and_record(report, PRODUCTS, "xyz", "partial")
    print_report(report)


def interactive():
    report = []
    while True:
        keyword = input("\nEnter keyword (blank to finish): ").strip()
        if not keyword:
            break
        mode = input("Mode [exact/prefix/suffix/partial]: ").strip().lower() or "partial"
        case = input("Ignore case? [Y/n]: ").strip().lower() != "n"
        try:
            run_and_record(report, PRODUCTS, keyword, mode, case)
        except ValueError as err:
            print(f"Error: {err}")
    if report:
        print_report(report)


if __name__ == "__main__":
    interactive() if "--interactive" in sys.argv else demo()
