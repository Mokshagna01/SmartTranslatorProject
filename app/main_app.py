import sys
import os

# -------- Fix Import Path --------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

# -------- Import UI Modules --------
from src.interface.ui_global_to_english import global_to_english_ui
from src.interface.ui_english_to_global import english_to_global_ui
from src.interface.ui_english_to_indian import english_to_indian_ui
from src.interface.ui_speech_translation import speech_translation_ui
from src.interface.ui_text_summarization import text_summarization_ui


# -------- Page Configuration --------
st.set_page_config(
    page_title="Smart Translation Platform",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Smart AI Translation System")

st.markdown(
"""
Welcome to the **Smart Translation Platform**.

This system supports:

• Global → English document translation  
• English → Global document translation  
• English → Indian language translation  
• Speech translation  
• AI-powered document summarization
"""
)

# -------- Sidebar Navigation --------
st.sidebar.title("Navigation")

module = st.sidebar.radio(
    "Select Module",
    [
        "Global → English",
        "English → Global",
        "English → Indian Languages",
        "Speech Translation",
        "Text Summarization"
    ]
)

# -------- Module Router --------
if module == "Global → English":
    global_to_english_ui()

elif module == "English → Global":
    english_to_global_ui()

elif module == "English → Indian Languages":
    english_to_indian_ui()

elif module == "Speech Translation":
    speech_translation_ui()

elif module == "Text Summarization":
    text_summarization_ui()