from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
import json
import os
import io
import csv

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
    html += '''
        <a href="/admin/export">📥 Export Category Stats</a><br>
        <a href="/admin/logs">🔎 View Violation Logs</a>
    '''
    return html


@router.get("/admin/export")
def export_stats_csv():
    try:
        with open("stats.json", "r") as f:
            stats = json.load(f)

        csv_content = "category,count\n" + "\n".join([f"{k},{v}" for k, v in stats.items()])
        os.makedirs("logs", exist_ok=True)
        with open("logs/stats.csv", "w", encoding="utf-8") as f:
            f.write(csv_content)

        return FileResponse("logs/stats.csv", media_type="text/csv", filename="stats.csv")
    except Exception as e:
        return {"error": str(e)}


@router.get("/admin/logs", response_class=HTMLResponse)
def view_violations():
    try:
        with open("logs/violations.log", encoding="utf-8") as f:
            entries = [json.loads(line) for line in f.readlines()]
    except FileNotFoundError:
        entries = []

    table_rows = ""
    for entry in reversed(entries[-100:]):  # последние 100 записей
        table_rows += f"""
        <tr>
            <td>{entry.get("timestamp", "")}</td>
            <td>{entry.get("category", "-")}</td>
            <td>{entry.get("city", "-")}</td>
            <td>{entry.get("text", "")}</td>
            <td>{entry.get("user_id", "-")}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>Violation Log</title>
        <style>
            table {{ border-collapse: collapse; width: 100%; font-family: sans-serif }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left }}
            th {{ background-color: #f0f0f0 }}
        </style>
    </head>
    <body>
        <h2>🚨 Последние блокировки (100)</h2>
        <table>
            <tr>
                <th>Время</th>
                <th>Категория</th>
                <th>Город</th>
                <th>Текст</th>
                <th>User ID</th>
            </tr>
            {table_rows}
        </table>
        <br>
        <a href="/admin/export-violations">📥 Export All Logs (CSV)</a>
    </body>
    </html>
    """


@router.get("/admin/export-violations")
def export_logs_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["timestamp", "category", "city", "text", "user_id"])

    try:
        with open("logs/violations.log", encoding="utf-8") as f:
            for line in f:
                row = json.loads(line)
                writer.writerow([
                    row.get("timestamp", ""),
                    row.get("category", ""),
                    row.get("city", ""),
                    row.get("text", ""),
                    row.get("user_id", ""),
                ])
    except FileNotFoundError:
        pass

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=violations.csv"
    })
