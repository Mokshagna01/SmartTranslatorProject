import streamlit as st
import whisper
import tempfile
import os

from streamlit_mic_recorder import mic_recorder

from src.pipeline.phase1_global_pipeline import hybrid_translate
from src.translation.translate import translate_paragraph


# Load whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("small")


model = load_model()


languages = {
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Korean": "kor_Hang",
    "Telugu": "tel_Telu",
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Bengali": "ben_Beng"
}


def speech_translation_ui():

    st.header("🎤 Speech Translation")

    target_lang = st.selectbox(
        "Select Target Language",
        list(languages.keys())
    )

    lang_code = languages[target_lang]

    st.subheader("Option 1: Upload Audio")

    audio_file = st.file_uploader(
        "Upload audio",
        type=["wav", "mp3"]
    )

    st.subheader("Option 2: Record Live Speech")

    audio = mic_recorder(
        start_prompt="🎙 Start Recording",
        stop_prompt="⏹ Stop Recording",
        key="recorder"
    )

    audio_bytes = None

    if audio_file:
        audio_bytes = audio_file.read()

    elif audio:
        audio_bytes = audio["bytes"]

    if audio_bytes:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            temp_audio = tmp.name

        st.audio(audio_bytes)

        if st.button("Transcribe & Translate"):

            with st.spinner("Transcribing speech..."):
                result = model.transcribe(temp_audio)
                src_text = result["text"]

            st.subheader("Recognized Text")
            st.write(src_text)

            with st.spinner("Translating..."):

                if lang_code in [
                    "spa_Latn","fra_Latn","deu_Latn",
                    "rus_Cyrl","arb_Arab","kor_Hang"
                ]:

                    translation = hybrid_translate(
                        src_text,
                        "eng_Latn",
                        lang_code
                    )

                else:

                    translation = translate_paragraph(
                        src_text,
                        "eng_Latn",
                        lang_code
                    )

            st.subheader("Translation")
            st.write(translation)

            st.download_button(
                "Download Translation",
                translation,
                file_name="speech_translation.txt"
            )

        os.remove(temp_audio)