import os
from src.summarization.abstractive_summarizer import summarize_text, read_document

# ---------------- Chunking Function ----------------
def chunk_text(text, max_words=150):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

# ---------------- Main Function ----------------
def main():
    print("Upload a document or enter text manually:")
    choice = input("Enter 'file' for document or 'text' to type manually: ").strip().lower()

    if choice == "file":
        file_path = input("Enter full path of TXT/DOCX/PDF file: ").strip()
        if not os.path.exists(file_path):
            print("File does not exist!")
            return
        paragraphs = read_document(file_path)
        text = " ".join(paragraphs)
    elif choice == "text":
        print("Enter your text (finish with an empty line):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        text = " ".join(lines)
    else:
        print("Invalid choice!")
        return

    print("\nGenerating abstractive summary...\n")

    # ---------------- Split text into chunks ----------------
    chunks = chunk_text(text, max_words=150)
    chunk_summaries = []

    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx+1}/{len(chunks)}...")
        summary = summarize_text(chunk, max_length=200, min_length=100)
        chunk_summaries.append(summary)

    # ---------------- Final summary ----------------
    final_text = " ".join(chunk_summaries)
    print("\nGenerating final summary...\n")
    final_summary = summarize_text(final_text, max_length=300, min_length=150)

    print("===== Summary =====\n")
    print(final_summary)
    print("\n===== Summary Completed =====")

if __name__ == "__main__":
    main()