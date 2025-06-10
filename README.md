# SafeScutumBot

🛡️ Smart moderation service with keyword filtering, logging, and statistics.

## Features

- ❌ Forbidden word detection
- 📊 Category stats
- 📝 Logs of violations
- 🌐 Web admin interface at `/admin`
- 📥 CSV export

## Run locally

```bash
uvicorn main:app --reload --port 8000

Endpoints
    •    POST /check_ad — Проверка текста
    •    GET /admin — Статистика
    •    GET /admin/export — Экспорт в CSV
