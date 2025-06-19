import os
import sys

# Install packages if not already installed (runs once per session)
try:
    import whisper
except ImportError:
    os.system(f"{sys.executable} -m pip install --quiet openai-whisper")

# Install ffmpeg (Linux, for Windows/macOS you need to install separately)
if not os.path.exists("/usr/bin/ffmpeg") and not os.path.exists("/usr/local/bin/ffmpeg"):
    os.system("apt-get update -qq && apt-get install -y -qq ffmpeg")

import streamlit as st
import whisper
import tempfile

st.title("Greenwashing Ad Analyzer")

uploaded_file = st.file_uploader("Upload a video (mp4, mov) or text transcript (.txt)", 
                                 type=["mp4", "mov", "txt"])

if uploaded_file:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    st.write(file_details)

    if uploaded_file.type.startswith("text"):
        # Handle text file
        text = uploaded_file.read().decode("utf-8")
        st.text_area("Transcript Text", text, height=300)

    elif uploaded_file.type in ["video/mp4", "video/quicktime"]:
        # Handle video file
        st.video(uploaded_file)

        # Save uploaded video to a temp file so whisper can read it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(uploaded_file.read())
            temp_video_path = temp_video.name

        # Load Whisper model (you can choose tiny/base/large depending on performance)
        model = whisper.load_model("base")
        st.info("Transcribing video — this may take a moment...")

        # Transcribe
        result = model.transcribe(temp_video_path)
        transcript = result["text"]

        st.subheader("Transcript:")
        st.text_area("", transcript, height=300)
