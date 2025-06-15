import json
import os
from datetime import datetime

LOG_FILE = "logs/violations.log"
STATS_FILE = "stats.json"

# Убедимся, что директория для логов существует
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_violation(text, user_id=None, category=None, city=None):
    """
    Логирует нарушение в файл LOG_FILE
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "text": text,
        "user_id": user_id,
        "category": category,
        "city": city
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def log_stats(category):
    """
    Увеличивает счётчик для указанной категории в STATS_FILE
    """
    if not category:
        return

    try:
        # Загружаем текущие данные
        stats = {}
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                stats = json.load(f)

        # Обновляем счётчик
        stats[category] = stats.get(category, 0) + 1

        # Сохраняем обновлённую статистику
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"Error logging stats: {e}")
