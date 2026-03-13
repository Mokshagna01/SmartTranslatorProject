from sacrebleu.metrics import BLEU, CHRF
from src.translation.translate import translate_paragraph

# Initialize metrics
bleu = BLEU(effective_order=True)
chrf = CHRF()

# ----------- TEST PARAGRAPH -----------
source_text = """
Artificial intelligence is changing the world rapidly.
In education, students can learn through personalized platforms.
Doctors use AI to detect diseases early and improve treatment.
Businesses automate tasks to improve efficiency and reduce costs.
Governments analyze data to provide better public services.
Technology also creates new job opportunities in emerging sectors.
However, ethical concerns such as privacy and bias must be addressed.
Researchers continue working on safer and more reliable systems.
In the future, AI will play an even bigger role in society.
Understanding this technology is important for every student.
"""

# ----------- HUMAN REFERENCES -----------
# (You or teacher should write these — sample references below)

ref_hi = """कृत्रिम बुद्धिमत्ता दुनिया को तेजी से बदल रही है।
शिक्षा में, छात्र व्यक्तिगत प्लेटफार्मों के माध्यम से सीख सकते हैं।
डॉक्टर बीमारियों का जल्दी पता लगाने और उपचार सुधारने के लिए एआई का उपयोग करते हैं।
व्यवसाय दक्षता बढ़ाने और लागत घटाने के लिए कार्यों को स्वचालित करते हैं।
सरकारें बेहतर सार्वजनिक सेवाएँ देने के लिए डेटा का विश्लेषण करती हैं।
प्रौद्योगिकी नए क्षेत्रों में रोजगार के अवसर भी पैदा करती है।
हालाँकि, गोपनीयता और पक्षपात जैसे नैतिक मुद्दों पर ध्यान देना आवश्यक है।
शोधकर्ता अधिक सुरक्षित और विश्वसनीय प्रणालियों पर काम कर रहे हैं।
भविष्य में एआई समाज में और बड़ी भूमिका निभाएगा।
इस तकनीक को समझना हर छात्र के लिए महत्वपूर्ण है।
"""

ref_te = """కృత్రిమ మేధస్సు ప్రపంచాన్ని వేగంగా మార్చుతోంది।
విద్యలో, విద్యార్థులు వ్యక్తిగతీకరించిన వేదికల ద్వారా నేర్చుకోవచ్చు।
డాక్టర్లు వ్యాధులను ముందుగానే గుర్తించడానికి AI ను ఉపయోగిస్తారు।
వ్యాపారాలు సామర్థ్యాన్ని పెంచి ఖర్చులను తగ్గించడానికి పనులను ఆటోమేట్ చేస్తాయి।
ప్రభుత్వాలు మెరుగైన ప్రజా సేవల కోసం డేటాను విశ్లేషిస్తాయి।
సాంకేతికత కొత్త ఉద్యోగ అవకాశాలను కూడా సృష్టిస్తుంది।
అయితే గోప్యత మరియు పక్షపాతం వంటి నైతిక సమస్యలను పరిష్కరించాలి।
పరిశోధకులు మరింత సురక్షితమైన వ్యవస్థలపై పని చేస్తున్నారు।
భవిష్యత్తులో AI సమాజంలో పెద్ద పాత్ర పోషిస్తుంది।
ఈ సాంకేతికతను అర్థం చేసుకోవడం ప్రతి విద్యార్థికి అవసరం।
"""

# ----------- MODEL TRANSLATION -----------
pred_hi = translate_paragraph(source_text, "eng_Latn", "hin_Deva")
pred_te = translate_paragraph(source_text, "eng_Latn", "tel_Telu")

# ----------- SCORING -----------
print("\n===== HINDI =====")
print(pred_hi[:500], "...\n")
print("BLEU:", bleu.corpus_score([pred_hi], [[ref_hi]]))
print("chrF:", chrf.corpus_score([pred_hi], [[ref_hi]]))

print("\n===== TELUGU =====")
print(pred_te[:500], "...\n")
print("BLEU:", bleu.corpus_score([pred_te], [[ref_te]]))
print("chrF:", chrf.corpus_score([pred_te], [[ref_te]]))