from datasets import load_from_disk
from transformers import (
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
    DistilBertTokenizerFast
)
import numpy as np
import evaluate

print("Loading processed dataset...")
dataset = load_from_disk("data/processed/lang_detect")

print("Loading tokenizer...")
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

print("Loading model...")
num_labels = len(set(dataset["train"]["labels"]))
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

accuracy = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return accuracy.compute(predictions=preds, references=labels)

training_args = TrainingArguments(
    output_dir="models/language_detection",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
    eval_strategy="epoch",   # <-- NEW NAME
    save_strategy="epoch",
    logging_dir="logs",
    load_best_model_at_end=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
print("Starting training...")
trainer.train()

print("Saving model...")
trainer.save_model("models/language_detection/final_model")
tokenizer.save_pretrained("models/language_detection/final_model")

print("Training complete!")