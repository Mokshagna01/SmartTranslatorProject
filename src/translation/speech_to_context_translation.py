# src/translation/speech_to_context_translation.py

import whisper
import sounddevice as sd
import numpy as np
import queue
import sys
import tempfile
import threading
import wave
from src.pipeline.phase1_global_pipeline import hybrid_translate
from src.translation.english_to_indian_doc import translate_paragraph

# ------------------
# Whisper model
# ------------------
print("Loading Whisper model...")
model = whisper.load_model("small")  # You can use tiny, base, small, medium, large
print("Model loaded successfully.\n")

# ------------------
# Target Languages
# ------------------
languages = {
    1: ("Spanish", "spa_Latn"),
    2: ("French", "fra_Latn"),
    3: ("German", "deu_Latn"),
    4: ("Russian", "rus_Cyrl"),
    5: ("Arabic", "arb_Arab"),
    6: ("Korean", "kor_Hang"),
    7: ("Telugu", "tel_Telu"),
    8: ("Hindi", "hin_Deva"),
    9: ("Tamil", "tam_Taml"),
    10: ("Bengali", "ben_Beng")
}

# ------------------
# Live Recording Setup
# ------------------
q = queue.Queue()
recording = True

def audio_callback(indata, frames, time, status):
    """This function is called for each audio block from the microphone"""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def record_audio():
    """Records audio until Enter is pressed"""
    global recording
    with sd.InputStream(samplerate=16000, channels=1, callback=audio_callback):
        print("Recording... Speak now! Press ENTER when done.\n")
        input()  # Wait for Enter
        recording = False

# ------------------
# Main Function
# ------------------
def main():
    # Choose target language
    print("Select target language:")
    for k, (name, _) in languages.items():
        print(f"{k}: {name}")
    choice = int(input("Enter number (1-10): "))
    tgt_lang_name, tgt_lang_code = languages[choice]
    print(f"Target language: {tgt_lang_name} ({tgt_lang_code})\n")

    # Start recording in separate thread
    global recording
    recording = True
    audio_thread = threading.Thread(target=record_audio)
    audio_thread.start()

    # Collect audio in chunks
    audio_data = []

    while recording or not q.empty():
        try:
            chunk = q.get(timeout=0.1)
            audio_data.append(chunk)
        except queue.Empty:
            continue

    # Combine all chunks
    audio_np = np.concatenate(audio_data, axis=0)

    # Save to temporary WAV file
    tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    with wave.open(tmp_file.name, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes((audio_np * 32767).astype(np.int16).tobytes())

    # ------------------
    # Transcribe speech
    # ------------------
    print("\nTranscribing speech...")
    result = model.transcribe(tmp_file.name)
    src_text = result["text"]
    print("\n--- Recognized Text ---\n")
    print(src_text)

    # ------------------
    # Context-Based Translation
    # ------------------
    print("\nTranslating text...\n")

    if tgt_lang_code in ["spa_Latn","fra_Latn","deu_Latn","rus_Cyrl","arb_Arab","kor_Hang"]:
        translation = hybrid_translate(src_text, "eng_Latn", tgt_lang_code)
    else:
        translation = translate_paragraph(src_text, "eng_Latn", tgt_lang_code)

    print("\n--- Translation Completed ---\n")
    print(translation)

if __name__ == "__main__":
    main()