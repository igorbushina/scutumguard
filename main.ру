from fastapi import FastAPI, Request
from pydantic import BaseModel
from moderation import check_text_for_violation
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

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
        return {"status": "ok"}
    else:
        return {"status": "violation", "reason": reason}
