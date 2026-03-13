from datasets import load_dataset
from transformers import DistilBertTokenizerFast

print("Loading dataset...")
dataset = load_dataset("papluca/language-identification")

print("Loading tokenizer...")
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

# Convert labels to numbers
label_list = dataset["train"].unique("labels")
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for label, i in label2id.items()}

def preprocess(example):
    example["labels"] = label2id[example["labels"]]
    return example

dataset = dataset.map(preprocess)

def tokenize(example):
    return tokenizer(
        example["text"],
        padding="max_length",
        truncation=True,
        max_length=128
    )

dataset = dataset.map(tokenize, batched=True)

# Save processed dataset
print("Saving processed dataset...")
dataset.save_to_disk("data/processed/lang_detect")

print("Preprocessing complete!")