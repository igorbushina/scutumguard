import os

FORBIDDEN_DIR = "/mnt/data/forbidden_words"

def load_forbidden_words():
    words = set()
    if not os.path.exists(FORBIDDEN_DIR):
        print(f"⚠️ WARNING: Directory {FORBIDDEN_DIR} does not exist.")
        return words

    for file in os.listdir(FORBIDDEN_DIR):
        if file.endswith(".txt"):
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
