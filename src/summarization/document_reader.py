# src/summarization/document_reader.py
import os
import docx
import pdfplumber

def read_document(file_path):
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