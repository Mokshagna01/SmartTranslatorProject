import streamlit as st
import tempfile
import os

from src.translation.english_to_global import EnglishToGlobalDocTranslator


translator = EnglishToGlobalDocTranslator()

# Only the languages you support
languages = {
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Korean": "kor_Hang"
}


def english_to_global_ui():

    st.header("🌍 English → Global Document Translation")

    uploaded_file = st.file_uploader(
        "Upload English Document",
        type=["pdf", "docx", "txt"]
    )

    target_language = st.selectbox(
        "Select Target Language",
        list(languages.keys())
    )

    if uploaded_file:

        # keep original extension
        file_ext = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            input_path = tmp.name

        if st.button("Translate Document"):

            with st.spinner("Translating document..."):

                tgt_lang_code = languages[target_language]

                translated_paragraphs = translator.translate_document(
                    input_path,
                    tgt_lang_code
                )

                translated_text = "\n\n".join(translated_paragraphs)

            st.subheader("Translated Output")

            st.text_area(
                "Translation",
                translated_text,
                height=300
            )

            st.download_button(
                "Download Translation",
                translated_text,
                file_name="translated_document.txt"
            )

        os.remove(input_path)