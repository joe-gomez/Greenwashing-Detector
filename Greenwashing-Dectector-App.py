import streamlit as st
from transcribe import transcribe
from highlight import highlight_individualising_language

import spacy
import subprocess
import sys

import spacy
nlp = spacy.load("en_core_web_sm")


st.set_page_config(page_title="Audio/Video Transcriber", layout="centered")

st.title("Whisper Transcription")

uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "mp4", "m4a", "wav", "webm"])

language_options = ["Auto", "English", "Spanish", "French", "German", "Hindi", "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Portuguese"]
selected_language = st.selectbox("Select original language (or choose Auto to detect):", language_options)

if uploaded_file is not None and st.button("Transcribe"):
    st.audio(uploaded_file, format="audio/mp3")
    with st.spinner("Transcribing... this may take a few seconds depending on the file size"):
        transcription = transcribe(uploaded_file, selected_language)
    
    st.success("Transcription complete!")
    st.markdown("### 📝 Transcription:")

    individualising_phrases = [
        "you should", "your responsibility", "individual choice", "personal duty",
        "you must", "on you", "each person", "it's up to you", "do your part"
    ]
    highlighted_transcript = highlight_individualising_language(transcription, individualising_phrases)

    st.markdown("""
    <style>
    .transcript-box {
        padding: 1em;
        border-radius: 8px;
        height: 300px;
        overflow-y: auto;
        white-space: pre-wrap;
        font-family: monospace;
    }
    .highlight {
        background-color: #fffa65;
        font-weight: bold;
    }
    </style>
    <div class="transcript-box">
    %s
    </div>
    """ % highlighted_transcript, unsafe_allow_html=True)

    st.download_button(
        label="Download as .txt",
        data=transcription,
        file_name="transcription.txt",
        mime="text/plain"
    )
