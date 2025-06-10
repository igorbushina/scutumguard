from fastapi import FastAPI, Request
from pydantic import BaseModel
from moderation import check_text_for_violation
from logger import log_violation, log_stats
from dotenv import load_dotenv
from admin import router as admin_router
import os

load_dotenv()
app = FastAPI()
app.include_router(admin_router)

class AdRequest(BaseModel):
    text: str
    user_id: int = None
    category: str = None
    city: str = None

@app.get("/")
def root():
    return {"status": "ScutumGuardBot API is running"}

@app.post("/check_ad")
def check_ad(data: AdRequest):
    is_clean, reason = check_text_for_violation(data.text)
    if is_clean:
        log_stats(data.category)
        return {"status": "ok"}
    else:
        log_violation(data.text, data.user_id, data.category, data.city)
        log_stats(data.category)
        return {"status": "violation", "reason": reason}# Entry point: запускает FastAPI и импортирует endpoints
