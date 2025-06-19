import re

def highlight_individualising_language(text):
    individualising_phrases = [
        "you should", "your responsibility", "individual choice", "personal duty",
        "you must", "on you", "each person", "it's up to you", "do your part"
    ]
    pattern = r'(' + '|'.join(re.escape(p) for p in individualising_phrases) + r')'
    highlighted = re.sub(pattern, r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return highlighted
