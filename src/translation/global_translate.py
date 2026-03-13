"""
Global Translation Module
Handles both token-based context translation and paragraph translation
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# -------- MODEL LOAD --------
MODEL_NAME = "facebook/nllb-200-distilled-600M"

print("Loading NLLB translation model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# Load model safely
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    use_safetensors=True  # <-- safe and compatible
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

print("Model loaded successfully.\n")


# -------- CONTEXT TOKEN TRANSLATION --------
def translate_global(text, src_lang, tgt_lang):
    """
    Context token translation (used for ES, FR, DE, RU)
    """

    tokenizer.src_lang = src_lang

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
            max_length=512
        )

    translated = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return translated[0]


# -------- PARAGRAPH TRANSLATION --------
def translate_paragraph(text, src_lang, tgt_lang):
    """
    Sentence/paragraph translation
    Better for Arabic and Korean
    """

    tokenizer.src_lang = src_lang

    sentences = text.split(". ")

    translated_sentences = []

    for sentence in sentences:

        if sentence.strip() == "":
            continue

        inputs = tokenizer(
            sentence,
            return_tensors="pt",
            truncation=True,
            padding=True
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
                max_length=256
            )

        translated = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        translated_sentences.append(translated[0])

    return " ".join(translated_sentences)