"""
Phase 1 Global Translation Test
Tests translation from English to global languages
"""

from src.translation.global_translate import translate_global

# Test sentences
test_sentences = [
    "Artificial intelligence is transforming the world.",
    "Education is the key to success.",
    "Technology helps people communicate better."
]

# Target languages
languages = {
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Korean": "kor_Hang"
}

print("\n===== GLOBAL TRANSLATION TEST =====\n")

for sentence in test_sentences:

    print("English:", sentence)
    print()

    for lang_name, lang_code in languages.items():

        translated = translate_global(
            sentence,
            src_lang="eng_Latn",
            tgt_lang=lang_code
        )

        print(f"{lang_name}: {translated}")

    print("\n-----------------------------------\n")