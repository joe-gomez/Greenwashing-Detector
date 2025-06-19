import streamlit as st
import re

keywords = [
    r'\byou\b',
    r'\byour choice\b',
    r'\bcarbon footprint\b',
    r'\blifestyle\b',
    r'\breduce your impact\b',
    r'\bwe all must\b',
    r'\bmake a difference\b'
]

def highlight_keywords(text, keywords):
    pattern = re.compile('|'.join(keywords), re.IGNORECASE)
    highlighted_text = pattern.sub(lambda m: f'**{m.group(0)}**', text)
    count = len(pattern.findall(text))
    return highlighted_text, count

st.title("Greenwashing Individualizing Language Detector")

uploaded_file = st.file_uploader("Upload sustainability text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    highlighted_text, count = highlight_keywords(text, keywords)
    st.write(f"Found {count} instances of individualizing language.")
    st.markdown(highlighted_text)
