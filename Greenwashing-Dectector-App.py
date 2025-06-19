import streamlit as st
from transcribe import transcribe
from highlight import highlight_individualising_language

st.set_page_config(page_title="Transcript Highlighter", layout="centered")
st.title("Transcribe or Highlight Existing Transcript")

# --- MODE SELECTION ---
mode = st.radio("Choose a mode:", ["Transcribe Audio/Video", "Highlight Existing .txt"])

# --- MODE 1: TRANSCRIBE AUDIO/VIDEO ---
if mode == "Transcribe Audio/Video":
    uploaded_file = st.file_uploader("Upload audio/video file", type=["mp3", "mp4", "m4a", "wav", "webm"])
    language_options = ["Auto", "English", "Spanish", "French", "German", "Hindi", "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Portuguese"]
    selected_language = st.selectbox("Language (or Auto):", language_options)

    if uploaded_file and st.button("Transcribe"):
        st.audio(uploaded_file, format="audio/mp3")
        with st.spinner("Transcribing..."):
            transcription = transcribe(uploaded_file, selected_language)
        
        st.success("Done!")
        st.text_area("Transcription", transcription, height=300)
        st.download_button(
            label="Download .txt",
            data=transcription,
            file_name="transcription.txt",
            mime="text/plain"
        )

# --- MODE 2: HIGHLIGHT FROM TXT FILE ---
elif mode == "Highlight Existing .txt":
    txt_file = st.file_uploader("Upload a .txt transcript", type=["txt"])
    
    if txt_file is not None:
        raw_text = txt_file.read().decode("utf-8")
        
        individualising_phrases = [
            "you should", "your responsibility", "individual choice", "personal duty",
            "you must", "on you", "each person", "it's up to you", "do your part"
        ]

        highlighted = highlight_individualising_language(raw_text, individualising_phrases)

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
        """ % highlighted, unsafe_allow_html=True)
