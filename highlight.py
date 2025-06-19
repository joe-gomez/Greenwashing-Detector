import re

def highlight_individualising_language(text, phrases):
    pattern = r'(' + '|'.join(re.escape(p) for p in phrases) + r')'
    highlighted = re.sub(pattern, r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return highlighted
