import os

FORBIDDEN_DIR = "mnt/data/forbidden_words"

def load_forbidden_words():
    words = set()
    for file in os.listdir(FORBIDDEN_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(FORBIDDEN_DIR, file), encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        words.add(word)
    return words

FORBIDDEN_WORDS = load_forbidden_words()

def check_text_for_violation(text: str):
    lowered = text.lower()
    for word in FORBIDDEN_WORDS:
        if word in lowered:
            return False, f"Detected forbidden word: '{word}'"
    return True, None
