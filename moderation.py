FORBIDDEN_WORDS = [
    "гаш", "гашиш", "шишки", "дроп", "проститутка", "девочка на час",
    "пушку", "ствол", "оружие", "патроны", "услуги 18+", "работа с переездом",
    "убью", "насилие", "взрыв", "бомба", "ночь вместе", "доставка веселья",
    "массаж без белья"
]

def check_text_for_violation(text: str):
    lowered = text.lower()
    for word in FORBIDDEN_WORDS:
        if word in lowered:
            return False, f"Detected forbidden word: '{word}'"
    return True, None
