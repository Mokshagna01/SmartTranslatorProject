import streamlit as st
import tempfile
import os

from src.translation.global_to_english_doc import GlobalToEnglishDocTranslator

translator = GlobalToEnglishDocTranslator()

# Only supported global languages
languages = {
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Korean": "kor_Hang"
}


def global_to_english_ui():

    st.header("🌍 Global → English Document Translation")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx", "txt"]
    )

    source_language = st.selectbox(
        "Select Source Language",
        list(languages.keys())
    )

    if uploaded_file:

        file_ext = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            input_path = tmp.name

        if st.button("Translate to English"):

            with st.spinner("Translating document..."):

                src_lang = languages[source_language]

                translated = translator.translate_document(
                    input_path,
                    src_lang
                )

                output_text = "\n\n".join(translated)

            st.text_area("English Translation", output_text, height=300)

            st.download_button(
                "Download Translation",
                output_text,
                file_name="english_translation.txt"
            )

        os.remove(input_path)