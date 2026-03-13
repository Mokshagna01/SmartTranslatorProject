from datasets import load_dataset

print("Downloading language detection dataset from Hugging Face...")

dataset = load_dataset("papluca/language-identification")

print(dataset)
print("Download complete!")