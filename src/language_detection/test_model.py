from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from datasets import load_dataset
import torch

print("Loading language detection model...")

model = DistilBertForSequenceClassification.from_pretrained(
    "models/language_detection/final_model"
)
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "models/language_detection/final_model"
)

# Load labels from dataset (same order as training)
dataset = load_dataset("papluca/language-identification")
labels = dataset["train"].unique("labels")
id2label = {i: label for i, label in enumerate(labels)}

model.eval()

# ✅ THIS is the function pipeline needs
def predict_language(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=1).item()
    return id2label[pred]


# Optional test block (safe to keep)
if __name__ == "__main__":
    sample = "यह एक हिंदी वाक्य है।"
    print("Detected language:", predict_language(sample))