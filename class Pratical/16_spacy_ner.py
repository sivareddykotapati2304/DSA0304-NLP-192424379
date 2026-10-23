import spacy
from spacy.cli import download

TEXT = (
    "Apple was founded by Steve Jobs in California in 1976. "
    "In 2023, Satya Nadella announced that Microsoft would invest $2 billion in India. "
    "The meeting in London will start at 10 a.m. on Monday."
)


def load_model(name="en_core_web_sm"):
    try:
        return spacy.load(name)
    except OSError:
        download(name)
        return spacy.load(name)


def main():
    nlp = load_model()
    doc = nlp(TEXT)
    print(f"{'Entity':<20}{'Label':<10}Meaning")
    print("-" * 55)
    for ent in doc.ents:
        print(f"{ent.text:<20}{ent.label_:<10}{spacy.explain(ent.label_)}")


if __name__ == "__main__":
    main()
