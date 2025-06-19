import streamlit as st
from transcribe import transcribe
from highlight import highlight_individualising_language

st.set_page_config(page_title="Audio/Video Transcriber", layout="centered")
st.title("📝 Whisper Transcription & Highlighting")

uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "mp4", "m4a", "wav", "webm"])

language_options = ["Auto", "English", "Spanish", "French", "German", "Hindi", "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Portuguese"]
selected_language = st.selectbox("Select original language (or choose Auto to detect):", language_options)

if uploaded_file is not None and st.button("Transcribe"):
    st.audio(uploaded_file, format="audio/mp3")

    with st.spinner("Transcribing... this may take a few seconds depending on the file size"):
        transcription = transcribe(uploaded_file, selected_language)

    st.success("Transcription complete!")

    # === 1. Raw transcript
    st.markdown("### 🔤 Raw Transcription")
    st.text_area("Original Transcript", transcription, height=300)

    # === 2. Highlighted version
    st.markdown("### 🌟 Highlighted Language (Individualising Phrases)")

    highlighted = highlight_individualising_language(transcription)

    st.markdown("""
    <style>
    .transcript-box {
        padding: 1em;
        border-radius: 8px;
        height: 300px;
        overflow-y: auto;
        white-space: pre-wrap;
        font-family: monospace;
        background-color: #f9f9f9;
    }
    .highlight {
        background-color: #fffa65;
        font-weight: bold;
    }
    </style>
    <div class="transcript-box">%s</div>
    """ % highlighted, unsafe_allow_html=True)

    # Optional: download raw transcription
    st.download_button(
        label="Download as .txt",
        data=transcription,
        file_name="transcription.txt",
        mime="text/plain"
    )
