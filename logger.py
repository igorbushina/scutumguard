import json
import os
from datetime import datetime

LOG_FILE = "logs/violations.log"
STATS_FILE = "stats.json"
os.makedirs("logs", exist_ok=True)

def log_violation(text, user_id=None, category=None, city=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "text": text,
        "user_id": user_id,
        "category": category,
        "city": city
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def log_stats(category):
    if not category:
        return
    try:
        if not os.path.exists(STATS_FILE):
            with open(STATS_FILE, "w") as f:
                json.dump({}, f)
        with open(STATS_FILE, "r") as f:
            stats = json.load(f)
        stats[category] = stats.get(category, 0) + 1
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error logging stats: {e}")# Запись нарушений и подсчёт статистики
