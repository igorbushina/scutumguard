import os

# ✅ Используем локальную папку проекта вместо /mnt/data
FORBIDDEN_DIR = "./forbidden_words"

# Создаём папку при необходимости
os.makedirs(FORBIDDEN_DIR, exist_ok=True)

def load_forbidden_words():
    words = set()

    if not os.path.exists(FORBIDDEN_DIR):
        print(f"⚠️ WARNING: Directory {FORBIDDEN_DIR} does not exist.")
        return words

    files = [f for f in os.listdir(FORBIDDEN_DIR) if f.endswith(".txt")]
    if not files:
        print(f"⚠️ WARNING: Directory {FORBIDDEN_DIR} is empty. Add .txt files with forbidden words.")

    for file in files:
        file_path = os.path.join(FORBIDDEN_DIR, file)
        try:
            with open(file_path, encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        words.add(word)
        except Exception as e:
            print(f"⚠️ WARNING: Could not read file {file_path}: {e}")
    return words

FORBIDDEN_WORDS = load_forbidden_words()

def check_text_for_violation(text: str):
    lowered = text.lower()
    for word in FORBIDDEN_WORDS:
        if word in lowered:
            return False, f"🚫 Detected forbidden word: '{word}'"
    return True, None
