from src.translation.global_translate import translate_global
from sacrebleu.metrics import BLEU, CHRF

bleu = BLEU(effective_order=True)
chrf = CHRF()

# -------- TEST DATA --------
dataset = [
    {
        "en": "Artificial intelligence is transforming many industries around the world.",
        "es": "La inteligencia artificial está transformando muchas industrias en todo el mundo.",
        "fr": "L'intelligence artificielle transforme de nombreuses industries dans le monde.",
        "de": "Künstliche Intelligenz verändert viele Branchen weltweit.",
        "ru": "Искусственный интеллект преобразует многие отрасли по всему миру.",
        "ar": "يعمل الذكاء الاصطناعي على تحويل العديد من الصناعات حول العالم.",
        "ko": "인공지능은 전 세계 여러 산업을 변화시키고 있습니다."
    }
]

# -------- PREDICTION STORAGE --------

en_es_preds, en_es_refs = [], []
es_en_preds, es_en_refs = [], []

en_fr_preds, en_fr_refs = [], []
fr_en_preds, fr_en_refs = [], []

en_de_preds, en_de_refs = [], []
de_en_preds, de_en_refs = [], []

en_ru_preds, en_ru_refs = [], []
ru_en_preds, ru_en_refs = [], []

en_ar_preds, en_ar_refs = [], []
ar_en_preds, ar_en_refs = [], []

en_ko_preds, en_ko_refs = [], []
ko_en_preds, ko_en_refs = [], []

for item in dataset:

    # -------- ENGLISH → GLOBAL --------

    en_es_preds.append(translate_global(item["en"], "eng_Latn", "spa_Latn"))
    en_es_refs.append(item["es"])

    en_fr_preds.append(translate_global(item["en"], "eng_Latn", "fra_Latn"))
    en_fr_refs.append(item["fr"])

    en_de_preds.append(translate_global(item["en"], "eng_Latn", "deu_Latn"))
    en_de_refs.append(item["de"])

    en_ru_preds.append(translate_global(item["en"], "eng_Latn", "rus_Cyrl"))
    en_ru_refs.append(item["ru"])

    en_ar_preds.append(translate_global(item["en"], "eng_Latn", "arb_Arab"))
    en_ar_refs.append(item["ar"])

    en_ko_preds.append(translate_global(item["en"], "eng_Latn", "kor_Hang"))
    en_ko_refs.append(item["ko"])

    # -------- GLOBAL → ENGLISH --------

    es_en_preds.append(translate_global(item["es"], "spa_Latn", "eng_Latn"))
    es_en_refs.append(item["en"])

    fr_en_preds.append(translate_global(item["fr"], "fra_Latn", "eng_Latn"))
    fr_en_refs.append(item["en"])

    de_en_preds.append(translate_global(item["de"], "deu_Latn", "eng_Latn"))
    de_en_refs.append(item["en"])

    ru_en_preds.append(translate_global(item["ru"], "rus_Cyrl", "eng_Latn"))
    ru_en_refs.append(item["en"])

    ar_en_preds.append(translate_global(item["ar"], "arb_Arab", "eng_Latn"))
    ar_en_refs.append(item["en"])

    ko_en_preds.append(translate_global(item["ko"], "kor_Hang", "eng_Latn"))
    ko_en_refs.append(item["en"])


print("\n===== GLOBAL TRANSLATION SCORES =====")

# EN → GLOBAL

print("\nEnglish → Spanish BLEU:", bleu.corpus_score(en_es_preds, [en_es_refs]))
print("English → Spanish chrF:", chrf.corpus_score(en_es_preds, [en_es_refs]))

print("\nEnglish → French BLEU:", bleu.corpus_score(en_fr_preds, [en_fr_refs]))
print("English → French chrF:", chrf.corpus_score(en_fr_preds, [en_fr_refs]))

print("\nEnglish → German BLEU:", bleu.corpus_score(en_de_preds, [en_de_refs]))
print("English → German chrF:", chrf.corpus_score(en_de_preds, [en_de_refs]))

print("\nEnglish → Russian BLEU:", bleu.corpus_score(en_ru_preds, [en_ru_refs]))
print("English → Russian chrF:", chrf.corpus_score(en_ru_preds, [en_ru_refs]))

print("\nEnglish → Arabic BLEU:", bleu.corpus_score(en_ar_preds, [en_ar_refs]))
print("English → Arabic chrF:", chrf.corpus_score(en_ar_preds, [en_ar_refs]))

print("\nEnglish → Korean BLEU:", bleu.corpus_score(en_ko_preds, [en_ko_refs]))
print("English → Korean chrF:", chrf.corpus_score(en_ko_preds, [en_ko_refs]))

# GLOBAL → EN

print("\nSpanish → English BLEU:", bleu.corpus_score(es_en_preds, [es_en_refs]))
print("Spanish → English chrF:", chrf.corpus_score(es_en_preds, [es_en_refs]))

print("\nFrench → English BLEU:", bleu.corpus_score(fr_en_preds, [fr_en_refs]))
print("French → English chrF:", chrf.corpus_score(fr_en_preds, [fr_en_refs]))

print("\nGerman → English BLEU:", bleu.corpus_score(de_en_preds, [de_en_refs]))
print("German → English chrF:", chrf.corpus_score(de_en_preds, [de_en_refs]))

print("\nRussian → English BLEU:", bleu.corpus_score(ru_en_preds, [ru_en_refs]))
print("Russian → English chrF:", chrf.corpus_score(ru_en_preds, [ru_en_refs]))

print("\nArabic → English BLEU:", bleu.corpus_score(ar_en_preds, [ar_en_refs]))
print("Arabic → English chrF:", chrf.corpus_score(ar_en_preds, [ar_en_refs]))

print("\nKorean → English BLEU:", bleu.corpus_score(ko_en_preds, [ko_en_refs]))
print("Korean → English chrF:", chrf.corpus_score(ko_en_preds, [ko_en_refs]))