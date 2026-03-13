from src.language_detection.test_model import model, tokenizer, id2label
from src.translation.translate import translate_paragraph
import torch

# -------- Language Detection Function --------
def predict_language(text):
    inputs = tokenizer([text], padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=1).item()
    return id2label[pred]


# -------- Mapping to NLLB codes --------
LANG_CODE_MAP = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "te": "tel_Telu",
    "ta": "tam_Taml",
    "bn": "ben_Beng"
}


# -------- MAIN PIPELINE --------
def phase1_pipeline(text, target_lang="tel_Telu"):

    print("\n🔎 Detecting language...")
    detected = predict_language(text)
    print("Detected Language:", detected)

    # Convert detection label to NLLB code
    src_lang = LANG_CODE_MAP.get(detected, "eng_Latn")

    print("\n🌍 Translating paragraph...")
    translated = translate_paragraph(text, src_lang, target_lang)

    print("\n✅ TRANSLATED OUTPUT:\n")
    print(translated)

    return translated


# -------- TEST BLOCK --------
if __name__ == "__main__":

    paragraph = """
Technology has become an essential part of modern life. People use smartphones, computers,
and the internet every day to communicate, learn new skills, and solve problems.
In education, technology helps students access information from anywhere in the world.
Teachers can use digital tools to explain complex topics in a more interactive way.
At the same time, it is important for people to use technology responsibly and avoid
spending too much time online. By maintaining a healthy balance, technology can
greatly improve productivity and make everyday tasks easier. In the future,
advancements in artificial intelligence and machine learning will continue to
transform industries such as healthcare, transportation, and education.
"""

    phase1_pipeline(paragraph, target_lang="tel_Telu")
    phase1_pipeline(paragraph, target_lang="ben_Beng")
    phase1_pipeline(paragraph, target_lang="tam_Taml")