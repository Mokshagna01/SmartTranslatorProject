from src.translation.global_translate import translate_global, translate_paragraph
from sacrebleu.metrics import BLEU, CHRF

bleu = BLEU(effective_order=True)
chrf = CHRF()

# -------- LANGUAGE ROUTER --------
def hybrid_translate(text, src_lang, tgt_lang):
    # Arabic and Korean → paragraph translation
    if tgt_lang in ["arb_Arab", "kor_Hang"]:
        return translate_paragraph(text, src_lang, tgt_lang)
    # Other languages → context token translation
    else:
        return translate_global(text, src_lang, tgt_lang)


# ---------------- TEST / EVALUATION BLOCK ----------------
# This will run ONLY when the pipeline file itself is executed
# It will NOT run when imported by your translator

if __name__ == "__main__":

    print("\n===== GLOBAL LANGUAGE CONTEXT TRANSLATION TEST =====\n")

    dataset = [
        {
            "src": """Artificial intelligence is transforming many industries across the world.
Organizations are using machine learning systems to analyze massive amounts of data.
These technologies help companies make faster and more accurate decisions.
In education, AI-powered platforms personalize learning experiences for students.
Teachers can identify knowledge gaps and provide targeted support.
However, experts emphasize that ethical guidelines and responsible AI usage are essential.
As technology continues to evolve, collaboration between humans and intelligent systems will become even more important.""",

            "ref_es": """La inteligencia artificial está transformando muchas industrias en todo el mundo.
Las organizaciones están utilizando sistemas de aprendizaje automático para analizar grandes cantidades de datos.
Estas tecnologías ayudan a las empresas a tomar decisiones más rápidas y precisas.
En la educación, las plataformas impulsadas por IA personalizan las experiencias de aprendizaje para los estudiantes.
Los profesores pueden identificar lagunas de conocimiento y brindar apoyo específico.
Sin embargo, los expertos enfatizan que las directrices éticas y el uso responsable de la IA son esenciales.
A medida que la tecnología continúa evolucionando, la colaboración entre humanos y sistemas inteligentes será aún más importante.""",

            "ref_fr": """L'intelligence artificielle transforme de nombreuses industries à travers le monde.
Les organisations utilisent des systèmes d'apprentissage automatique pour analyser d'énormes quantités de données.
Ces technologies aident les entreprises à prendre des décisions plus rapides et plus précises.
Dans l'éducation, les plateformes alimentées par l'IA personnalisent l'expérience d'apprentissage des étudiants.
Les enseignants peuvent identifier les lacunes et fournir un soutien ciblé.
Cependant, les experts soulignent que des directives éthiques et une utilisation responsable de l'IA sont essentielles.
À mesure que la technologie évolue, la collaboration entre les humains et les systèmes intelligents deviendra encore plus importante.""",

            "ref_de": """Künstliche Intelligenz verändert viele Branchen weltweit.
Organisationen nutzen maschinelle Lernsysteme, um große Datenmengen zu analysieren.
Diese Technologien helfen Unternehmen, schnellere und genauere Entscheidungen zu treffen.
Im Bildungsbereich personalisieren KI-gestützte Plattformen das Lernen für Studierende.
Lehrkräfte können Wissenslücken erkennen und gezielte Unterstützung geben.
Experten betonen jedoch, dass ethische Richtlinien und eine verantwortungsvolle Nutzung von KI entscheidend sind.
Mit der Weiterentwicklung der Technologie wird die Zusammenarbeit zwischen Menschen und intelligenten Systemen noch wichtiger.""",

            "ref_ru": """Искусственный интеллект преобразует многие отрасли по всему миру.
Организации используют системы машинного обучения для анализа огромных объемов данных.
Эти технологии помогают компаниям принимать более быстрые и точные решения.
В образовании платформы на основе ИИ персонализируют процесс обучения для студентов.
Учителя могут выявлять пробелы в знаниях и оказывать целевую поддержку.
Однако эксперты подчеркивают, что этические нормы и ответственное использование ИИ крайне важны.
По мере развития технологий сотрудничество между людьми и интеллектуальными системами станет еще более важным.""",

            "ref_ar": """يعمل الذكاء الاصطناعي على تحويل العديد من الصناعات حول العالم.
تستخدم المؤسسات أنظمة التعلم الآلي لتحليل كميات هائلة من البيانات.
تساعد هذه التقنيات الشركات على اتخاذ قرارات أسرع وأكثر دقة.
في التعليم، تقوم المنصات المدعومة بالذكاء الاصطناعي بتخصيص تجربة التعلم للطلاب.
يمكن للمعلمين تحديد فجوات المعرفة وتقديم دعم موجه.
ومع ذلك، يؤكد الخبراء أن الإرشادات الأخلاقية والاستخدام المسؤول للذكاء الاصطناعي أمران أساسيان.
ومع تطور التكنولوجيا، سيصبح التعاون بين البشر والأنظمة الذكية أكثر أهمية.""",

            "ref_ko": """인공지능은 전 세계 여러 산업을 변화시키고 있습니다.
조직들은 대규모 데이터를 분석하기 위해 머신러닝 시스템을 사용하고 있습니다.
이러한 기술은 기업이 더 빠르고 정확한 의사결정을 내리는 데 도움을 줍니다.
교육 분야에서는 AI 기반 플랫폼이 학생들의 학습 경험을 개인화합니다.
교사는 지식의 격차를 파악하고 맞춤형 지원을 제공할 수 있습니다.
그러나 전문가들은 윤리적 지침과 책임 있는 AI 사용이 중요하다고 강조합니다.
기술이 발전함에 따라 인간과 지능형 시스템 간의 협력이 더욱 중요해질 것입니다."""
        }
    ]

    languages = ["es", "fr", "de", "ru", "ar", "ko"]
    preds = {lang: [] for lang in languages}
    refs = {lang: [] for lang in languages}

    for item in dataset:

        src_text = item["src"]

        print("\n--- Translating paragraph ---\n")

        for lang_code, tgt_lang in zip(
            languages,
            ["spa_Latn","fra_Latn","deu_Latn","rus_Cyrl","arb_Arab","kor_Hang"]
        ):

            translation = hybrid_translate(src_text,"eng_Latn",tgt_lang)

            preds[lang_code].append(translation)
            refs[lang_code].append(item[f"ref_{lang_code}"])

            print(f"\n--- {lang_code.upper()} Translation ---\n")
            print(translation)

    print("\n===== GLOBAL LANGUAGE SCORES =====\n")

    for lang_code in languages:
        print(f"{lang_code.upper()} BLEU:", bleu.corpus_score(preds[lang_code],[refs[lang_code]]))
        print(f"{lang_code.upper()} chrF:", chrf.corpus_score(preds[lang_code],[refs[lang_code]]))