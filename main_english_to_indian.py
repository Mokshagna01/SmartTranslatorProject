from src.translation.english_to_indian_doc import EnglishToIndianDocTranslator


translator = EnglishToIndianDocTranslator()

print("\n=== English → Indian Languages Document Translator ===\n")

input_file = input("Upload document (PDF/TXT/DOCX): ")

print("\nSelect Target Language\n")

print("1: Telugu (tel_Telu)")
print("2: Hindi (hin_Deva)")
print("3: Tamil (tam_Taml)")
print("4: Bengali (ben_Beng)")

choice = input("\nChoose language (1-4): ")

lang_map = {
    "1": "tel_Telu",
    "2": "hin_Deva",
    "3": "tam_Taml",
    "4": "ben_Beng"
}

target_lang = lang_map.get(choice)

if target_lang is None:
    print("Invalid choice")
    exit()

output_file = input("\nEnter output file name (TXT or DOCX): ")

translated_blocks = translator.translate_document(
    input_file,
    target_lang
)

translator.save_document(translated_blocks, output_file)

print("\n✅ Translation Completed")
print("Saved to:", output_file)