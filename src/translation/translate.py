from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re

MODEL_NAME = "facebook/nllb-200-distilled-600M"

print("Loading translation model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    use_safetensors=True
)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)


# ---------- Helper: split paragraph into smart chunks ----------
def split_into_chunks(text, max_words=120):
    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if len(current) >= max_words:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks


# ---------- Context-based translation ----------
def translate_paragraph(text, source_lang="eng_Latn", target_lang="hin_Deva"):
    tokenizer.src_lang = source_lang

    chunks = split_into_chunks(text)

    translated_chunks = []

    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True).to(device)

        tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang),
            max_length=300
        )

        translated = tokenizer.batch_decode(tokens, skip_special_tokens=True)[0]
        translated_chunks.append(translated)

    return " ".join(translated_chunks)
