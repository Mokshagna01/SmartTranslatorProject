"""
Global → English Document Translator
Supports PDF, TXT, DOCX input files.
Can optionally evaluate BLEU / chrF with reference document.
"""

import os
from src.translation.global_to_english_doc import GlobalToEnglishDocTranslator

# ------------------------------
# Initialize Translator
# ------------------------------
translator = GlobalToEnglishDocTranslator()

print("\n=== Global → English Document Translator ===\n")

# ------------------------------
# Upload Document
# ------------------------------
input_file = input("Upload document (PDF/TXT/DOCX): ").strip()

# ------------------------------
# Choose Source Language
# ------------------------------
print("\nSelect the source language of your document:")
print("1: Spanish (spa_Latn)")
print("2: French (fra_Latn)")
print("3: German (deu_Latn)")
print("4: Russian (rus_Cyrl)")
print("5: Arabic (arb_Arab)")
print("6: Korean (kor_Hang)")

lang_choice = int(input("Choose source language (1-6): ").strip())
lang_map = {
    1: "spa_Latn",
    2: "fra_Latn",
    3: "deu_Latn",
    4: "rus_Cyrl",
    5: "arb_Arab",
    6: "kor_Hang"
}
source_lang = lang_map.get(lang_choice)
if source_lang is None:
    print("Invalid language choice. Exiting.")
    exit()

# ------------------------------
# Output File
# ------------------------------
output_file = input("Enter output file name (TXT or DOCX, e.g., data/eng_translated.txt): ").strip()

# ------------------------------
# Translate Document
# ------------------------------
print("\nTranslating document... This may take a while depending on the size.\n")
translated_paragraphs = translator.translate_document(input_file, source_lang)

# ------------------------------
# Save Translated Document
# ------------------------------
translator.save_translated_document(translated_paragraphs, output_file)
print(f"\n✅ Translated document saved as: {output_file}")

# ------------------------------
# Optional BLEU / chrF Evaluation
# ------------------------------
eval_choice = input("\nDo you want to evaluate BLEU/chrF with a reference English document? (y/n): ").lower()
if eval_choice == "y":
    ref_file = input("Upload your reference English document (TXT/DOCX/PDF): ").strip()

    try:
        reference_paragraphs = translator.read_document(ref_file)
    except Exception as e:
        print("⚠️ Error reading reference document:", e)
        exit()

    if len(translated_paragraphs) != len(reference_paragraphs):
        print("⚠️ Warning: Number of paragraphs in translation and reference do not match!")
        print(f"Translated: {len(translated_paragraphs)}, Reference: {len(reference_paragraphs)}")

    from sacrebleu.metrics import BLEU, CHRF
    bleu = BLEU(effective_order=True)
    chrf = CHRF()

    bleu_score = bleu.corpus_score(translated_paragraphs, [reference_paragraphs])
    chrf_score = chrf.corpus_score(translated_paragraphs, [reference_paragraphs])

    print("\n===== BLEU & chrF Evaluation =====")
    print("BLEU:", bleu_score)
    print("chrF:", chrf_score)