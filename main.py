from fastapi import FastAPI
from pydantic import BaseModel
from moderation import check_text_for_violation
from logger import log_violation, log_stats
from dotenv import load_dotenv
from admin import router as admin_router
import os

# Загружаем переменные окружения
load_dotenv()

# Создаем приложение
app = FastAPI()
app.include_router(admin_router)

# Модель запроса
class AdRequest(BaseModel):
    text: str
    user_id: int | None = None
    category: str | None = None
    city: str | None = None

# Рутовая точка
@app.get("/")
def root():
    return {"status": "ScutumGuardBot API is running"}

# Проверка объявления
@app.post("/check_ad")
def check_ad(data: AdRequest):
    # Проверка текста
    is_clean, reason = check_text_for_violation(data.text)

    if is_clean:
        # Логируем статистику
        if data.category:
            log_stats(data.category)
        return {"status": "ok"}
    else:
        # Логируем нарушение и статистику
        log_violation(
            text=data.text,
            user_id=data.user_id,
            category=data.category,
            city=data.city
        )
        if data.category:
            log_stats(data.category)
        return {"status": "violation", "reason": reason}
