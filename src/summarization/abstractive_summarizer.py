import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import docx
import pdfplumber
import os

# ---------------- GPU/CPU ----------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------- Load Model ----------------
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.to(device)
print("Model loaded successfully!\n")

# ---------------- Document Reader ----------------
def read_document(file_path):
    """
    Reads TXT, DOCX, or PDF files and returns a list of paragraphs.
    """
    ext = os.path.splitext(file_path)[1].lower()
    paragraphs = []

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            paragraphs = [line.strip() for line in f if line.strip()]

    elif ext == ".docx":
        doc = docx.Document(file_path)
        paragraphs = [para.text.strip() for para in doc.paragraphs if para.text.strip()]

    elif ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    paragraphs.extend([line.strip() for line in text.split("\n") if line.strip()])
    else:
        raise ValueError("Unsupported file format! Use TXT, DOCX, or PDF.")

    return paragraphs

# ---------------- Summarize Function ----------------
def summarize_text(text, max_length=150, min_length=50):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    ).to(device)

    summary_ids = model.generate(
        **inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary