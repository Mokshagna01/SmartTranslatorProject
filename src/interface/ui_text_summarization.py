import streamlit as st
import tempfile
import os

from src.summarization.abstractive_summarizer import summarize_text, read_document


# -------- Chunk Function (same as run_summarizer.py) --------
def chunk_text(text, max_words=150):

    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


def text_summarization_ui():

    st.header("🧠 AI Text Summarization")

    option = st.radio(
        "Select Input Type",
        ["Upload Document", "Enter Text"]
    )

    # ---------------- DOCUMENT ----------------
    if option == "Upload Document":

        uploaded_file = st.file_uploader(
            "Upload TXT / DOCX / PDF",
            type=["txt", "docx", "pdf"]
        )

        if uploaded_file:

            file_ext = os.path.splitext(uploaded_file.name)[1]

            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            if st.button("Generate Summary"):

                with st.spinner("Generating summary..."):

                    paragraphs = read_document(temp_path)

                    text = " ".join(paragraphs)

                    # -------- chunking --------
                    chunks = chunk_text(text, max_words=150)

                    chunk_summaries = []

                    for chunk in chunks:
                        summary = summarize_text(
                            chunk,
                            max_length=200,
                            min_length=100
                        )
                        chunk_summaries.append(summary)

                    # -------- final summary --------
                    final_text = " ".join(chunk_summaries)

                    final_summary = summarize_text(
                        final_text,
                        max_length=300,
                        min_length=150
                    )

                st.subheader("Final Summary")

                st.text_area(
                    "Summary",
                    final_summary,
                    height=300
                )

                st.download_button(
                    "Download Summary",
                    final_summary,
                    file_name="summary.txt"
                )

            os.remove(temp_path)

    # ---------------- DIRECT TEXT ----------------
    else:

        text_input = st.text_area(
            "Enter Text",
            height=250
        )

        if st.button("Generate Summary"):

            if text_input.strip():

                with st.spinner("Generating summary..."):

                    chunks = chunk_text(text_input, max_words=150)

                    chunk_summaries = []

                    for chunk in chunks:
                        summary = summarize_text(
                            chunk,
                            max_length=200,
                            min_length=100
                        )
                        chunk_summaries.append(summary)

                    final_text = " ".join(chunk_summaries)

                    final_summary = summarize_text(
                        final_text,
                        max_length=300,
                        min_length=150
                    )

                st.subheader("Final Summary")

                st.text_area(
                    "Summary",
                    final_summary,
                    height=300
                )