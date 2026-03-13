from sacrebleu.metrics import BLEU, CHRF
from src.translation.translate import translate_paragraph

bleu = BLEU(effective_order=True)
chrf = CHRF()

# -------- MULTIPLE PARAGRAPHS --------
dataset = [
    {
        "src": "Artificial intelligence improves education by enabling personalized learning.",
        "ref_hi": "कृत्रिम बुद्धिमत्ता व्यक्तिगत शिक्षा को संभव बनाकर शिक्षा में सुधार करती है।",
        "ref_te": "వ్యక్తిగతీకరించిన అభ్యాసాన్ని సాధ్యంచేసి కృత్రిమ మేధస్సు విద్యను మెరుగుపరుస్తుంది."
    },
    {
        "src": "Digital technology helps doctors treat patients more effectively.",
        "ref_hi": "डिजिटल तकनीक डॉक्टरों को मरीजों का अधिक प्रभावी उपचार करने में मदद करती है।",
        "ref_te": "డిజిటల్ సాంకేతికత వైద్యులకు రోగులను మరింత సమర్థవంతంగా చికిత్స చేయడంలో సహాయపడుతుంది."
    },
    {
        "src": "Governments use data analysis to improve public services.",
        "ref_hi": "सरकारें सार्वजनिक सेवाओं को बेहतर बनाने के लिए डेटा विश्लेषण का उपयोग करती हैं।",
        "ref_te": "ప్రభుత్వాలు ప్రజా సేవలను మెరుగుపరచడానికి డేటా విశ్లేషణను ఉపయోగిస్తాయి."
    }
]

hi_preds, hi_refs = [], []
te_preds, te_refs = [], []

for item in dataset:
    hi_preds.append(translate_paragraph(item["src"], "eng_Latn", "hin_Deva"))
    te_preds.append(translate_paragraph(item["src"], "eng_Latn", "tel_Telu"))

    hi_refs.append(item["ref_hi"])
    te_refs.append(item["ref_te"])

print("\n===== FINAL SCORES =====")
print("Hindi BLEU:", bleu.corpus_score(hi_preds, [hi_refs]))
print("Hindi chrF:", chrf.corpus_score(hi_preds, [hi_refs]))
print("Telugu BLEU:", bleu.corpus_score(te_preds, [te_refs]))
print("Telugu chrF:", chrf.corpus_score(te_preds, [te_refs]))