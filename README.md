# 🌍 Smart AI Multilingual Translator

An AI-powered multilingual translation system designed to translate **documents, speech, and text** while preserving **context across paragraphs**.

This project combines **language detection, context-based translation, and summarization** using modern Natural Language Processing models.

---

# 🚀 Project Overview

Smart AI Translator is a multilingual NLP system capable of processing different types of input and translating them into meaningful output while maintaining contextual consistency.

The system integrates multiple components such as language detection, translation, document processing, and summarization.

Supported capabilities include:

• Global Language → English translation  
• English → Global Language translation  
• English → Indian Language translation  
• Speech-to-text translation  
• Document translation  
• Context-aware paragraph translation  
• Automatic text summarization  

---

# 🧠 Models Used

### Language Detection
DistilBERT (Fine-tuned for multilingual language identification)

### Translation
Facebook NLLB-200 model for multilingual translation

### Context Evaluation (Research Testing)
BLEU and chrF metrics were used during experimentation to evaluate translation quality and verify contextual consistency across translated paragraphs.

---

# ⚙️ System Workflow

1️⃣ Input text, speech, or document

2️⃣ Language detection using DistilBERT

3️⃣ Context-aware translation using NLLB

4️⃣ Document translation pipeline

5️⃣ Optional summarization of translated text

---

# 📂 Project Structure

SmartTranslatorProject

app/  
data/  
ffmpeg-8.0.1-essentials_build/  
src/  
models/  

main.py  
doc.txt  
doc1.txt  

.gitignore  

---

# 🛠 Installation

Clone the repository

git clone https://github.com/Mokshagna01/SmartTranslatorProject.git

Move into project folder

cd SmartTranslatorProject

Install dependencies

pip install -r requirements.txt

Run the project

python main.py

---

# 🌐 Supported Capabilities

Multilingual translation  
Document translation  
Speech translation  
Context-aware paragraph translation  
Text summarization  

---

# 📈 Future Improvements

• Low-resource language translation support  
• Improved summarization models  
• Web-based translation interface  
• Real-time speech translation  

---

# 👨‍💻 Author

Mokshagna Rajulapati

AI / Machine Learning Enthusiast

GitHub: https://github.com/Mokshagna01

---

# ⭐ Project Goal

The objective of this project is to develop a multilingual AI translation system that can understand contextual relationships within long text passages and generate accurate translations across multiple languages.
