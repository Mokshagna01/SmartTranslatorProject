from src.translation.english_to_global import EnglishToGlobalDocTranslator

translator = EnglishToGlobalDocTranslator()

print("\nLoading translation model...\n")

print("English → Global Document Translator")

input_file = input("Upload PDF/TXT/DOCX: ").strip()


languages = [
    "Spanish",
    "French",
    "German",
    "Russian",
    "Arabic",
    "Korean"
]

codes = [
    "spa_Latn",
    "fra_Latn",
    "deu_Latn",
    "rus_Cyrl",
    "arb_Arab",
    "kor_Hang"
]

for i, lang in enumerate(languages, 1):
    print(f"{i}. {lang}")

choice = int(input("Select language: "))

target = codes[choice - 1]

output_file = input("Output file name (example translated.docx): ")

translated = translator.translate_document(input_file, target)

translator.save_translated_document(translated, output_file)

print("\n✅ Translation Completed")
print("Saved to:", output_file)