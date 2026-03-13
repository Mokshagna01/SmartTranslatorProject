# File: src/utils/document_loader.py

import os
from docx import Document
from PyPDF2 import PdfReader
from pathlib import Path

class DocumentLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extension = Path(file_path).suffix.lower()

    def read_document(self):
        paragraphs = []
        if self.extension == ".pdf":
            reader = PdfReader(self.file_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    paragraphs.extend([p.strip() for p in text.split("\n") if p.strip()])
        elif self.extension == ".docx":
            doc = Document(self.file_path)
            for para in doc.paragraphs:
                if para.text.strip():
                    paragraphs.append(para.text.strip())
        elif self.extension == ".txt":
            with open(self.file_path, "r", encoding="utf-8") as f:
                paragraphs = [line.strip() for line in f if line.strip()]
        else:
            raise ValueError(f"Unsupported file type: {self.extension}")
        return paragraphs

    def save_translated_text(self, paragraphs, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            for para in paragraphs:
                f.write(para + "\n\n")
        print(f"\n✅ Translated document saved at: {output_path}")