from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse
import json
import os

router = APIRouter()

@router.get("/admin", response_class=HTMLResponse)
def admin_panel():
    try:
        with open("stats.json", "r") as f:
            stats = json.load(f)
    except Exception:
        stats = {}

    html = "<h1>📊 Scutum Admin Panel</h1><ul>"
    for category, count in stats.items():
        html += f"<li><strong>{category}</strong>: {count}</li>"
    html += "</ul>"
    html += '<a href="/admin/export">📥 Export CSV</a>'
    return html

@router.get("/admin/export")
def export_csv():
    try:
        with open("stats.json", "r") as f:
            stats = json.load(f)
        csv_content = "category,count\n" + "\n".join([f"{k},{v}" for k, v in stats.items()])
        with open("logs/stats.csv", "w") as f:
            f.write(csv_content)
        return FileResponse("logs/stats.csv", media_type="text/csv", filename="stats.csv")
    except Exception as e:
        return {"error": str(e)}# Интерфейс /admin и экспорт логов
