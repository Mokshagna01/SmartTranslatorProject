import streamlit as st
import tempfile
import os

from src.translation.translate import translate_paragraph
from src.summarization.abstractive_summarizer import read_document


# Only supported Indian languages
languages = {
    "Telugu": "tel_Telu",
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Bengali": "ben_Beng"
}


def english_to_indian_ui():

    st.header("🇮🇳 English → Indian Languages Document Translation")

    uploaded_file = st.file_uploader(
        "Upload English Document",
        type=["txt", "docx", "pdf"]
    )

    target_language = st.selectbox(
        "Select Target Language",
        list(languages.keys())
    )

    if uploaded_file:

        # Save uploaded file temporarily
        file_ext = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        if st.button("Translate Document"):

            with st.spinner("Translating document..."):

                paragraphs = read_document(temp_path)

                tgt_lang = languages[target_language]

                translated_paragraphs = []

                for para in paragraphs:

                    translated = translate_paragraph(
                        para,
                        source_lang="eng_Latn",
                        target_lang=tgt_lang
                    )

                    translated_paragraphs.append(translated)

                final_translation = "\n\n".join(translated_paragraphs)

            st.subheader("Translated Output")

            st.text_area(
                "Translation",
                final_translation,
                height=300
            )

            st.download_button(
                "Download Translation",
                final_translation,
                file_name="translated_document.txt"
            )

        os.remove(temp_path)