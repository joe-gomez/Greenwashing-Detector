import re
import html

def highlight_individualising_language(text):
    phrases = [
        "you should", "your responsibility", "individual choice", "personal duty",
        "you must", "on you", "each person", "it's up to you", "do your part"
    ]
    # Escape HTML to prevent injection
    text = html.escape(text)

    # Re-inject highlights (phrase matching happens post-escaping)
    pattern = r'(' + '|'.join(re.escape(p) for p in phrases) + r')'
    highlighted = re.sub(pattern, r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)

    return highlighted
