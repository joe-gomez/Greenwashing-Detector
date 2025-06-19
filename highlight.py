import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define phrases as simple keywords (can be extended later)
individualising_keywords = [
    "you should", "your responsibility", "individual choice", "personal duty",
    "you must", "on you", "each person", "it's up to you", "do your part"
]

def highlight_individualising_language(text):
    doc = nlp(text)
    highlighted_text = text

    for phrase in individualising_keywords:
        highlighted_text = re.sub(
            re.escape(phrase), 
            f'<span class="highlight">{phrase}</span>', 
            highlighted_text, 
            flags=re.IGNORECASE
        )

    return highlighted_text
