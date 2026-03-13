"""
Phase 1 Global → English Translation (Paragraph Level)
Context-based translation evaluation using long paragraphs
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sacrebleu.metrics import BLEU, CHRF

# ------------------------------
# Load Model
# ------------------------------
print("Loading NLLB global translation model...")

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    use_safetensors=True
)
print("Model loaded successfully!")

# ------------------------------
# Language Codes
# ------------------------------
LANG_CODES = {
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Korean": "kor_Hang"
}

# ------------------------------
# Translation Function
# ------------------------------
def translate_to_english(paragraph, source_lang):
    # Set source language
    tokenizer.src_lang = source_lang

    # Encode the paragraph
    inputs = tokenizer(paragraph, return_tensors="pt", truncation=True)

    # Generate translation
    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("eng_Latn"),
        max_length=512
    )

    # Decode translation
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

# ------------------------------
# Paragraph Dataset
# ------------------------------
dataset = {

    "Spanish": [(
        """La inteligencia artificial está transformando muchas industrias en todo el mundo.
        Las empresas utilizan el aprendizaje automático para mejorar la toma de decisiones
        y aumentar la eficiencia. En educación, la tecnología ayuda a los estudiantes
        a aprender de manera más efectiva mediante plataformas digitales.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )],

    "French": [(
        """L'intelligence artificielle transforme de nombreuses industries dans le monde.
        Les entreprises utilisent l'apprentissage automatique pour améliorer la prise de décision
        et accroître l'efficacité. Dans le domaine de l'éducation, la technologie aide les étudiants
        à apprendre plus efficacement grâce aux plateformes numériques.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )],

    "German": [(
        """Künstliche Intelligenz verändert viele Branchen auf der ganzen Welt.
        Unternehmen nutzen maschinelles Lernen, um Entscheidungen zu verbessern
        und die Effizienz zu steigern. In der Bildung hilft Technologie den
        Studierenden, effektiver über digitale Plattformen zu lernen.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )],

    "Russian": [(
        """Искусственный интеллект меняет многие отрасли по всему миру.
        Компании используют машинное обучение для улучшения принятия решений
        и повышения эффективности. В образовании технологии помогают студентам
        учиться более эффективно с помощью цифровых платформ.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )],

    "Arabic": [(
        """يغير الذكاء الاصطناعي العديد من الصناعات حول العالم.
        تستخدم الشركات التعلم الآلي لتحسين عملية اتخاذ القرار
        وزيادة الكفاءة. في مجال التعليم تساعد التكنولوجيا الطلاب
        على التعلم بشكل أكثر فعالية من خلال المنصات الرقمية.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )],

    "Korean": [(
        """인공지능은 전 세계의 많은 산업을 변화시키고 있습니다.
        기업들은 의사결정을 개선하고 효율성을 높이기 위해
        머신러닝을 활용하고 있습니다. 교육 분야에서는
        기술이 학생들이 디지털 플랫폼을 통해 더 효과적으로
        학습할 수 있도록 돕고 있습니다.""",

        """Artificial intelligence is transforming many industries around the world.
        Companies use machine learning to improve decision making and increase efficiency.
        In education, technology helps students learn more effectively through digital platforms."""
    )]

}

# ------------------------------
# Metrics
# ------------------------------
bleu = BLEU(effective_order=True)
chrf = CHRF()

results = {}

print("\n===== GLOBAL → ENGLISH PARAGRAPH TRANSLATION =====\n")

# ------------------------------
# Translation Loop
# ------------------------------
for lang, samples in dataset.items():

    src_lang = LANG_CODES[lang]

    predictions = []
    references = []

    for src_text, ref_text in samples:

        translation = translate_to_english(src_text, src_lang)

        print(f"\n--- {lang} Paragraph ---")
        print("\nSOURCE:")
        print(src_text)

        print("\nTRANSLATED:")
        print(translation)

        predictions.append(translation)
        references.append(ref_text)

    bleu_score = bleu.corpus_score(predictions, [references])
    chrf_score = chrf.corpus_score(predictions, [references])

    results[lang] = (bleu_score, chrf_score)

# ------------------------------
# Final Scores
# ------------------------------
print("\n\n===== GLOBAL → ENGLISH TRANSLATION SCORES =====\n")

for lang, scores in results.items():

    bleu_score, chrf_score = scores

    print(f"{lang} → English BLEU: {bleu_score}")
    print(f"{lang} → English chrF: {chrf_score}\n")