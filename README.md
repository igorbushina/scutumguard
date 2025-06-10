# ScutumGuardBot

AI-powered moderation bot for Telegram and external API filtering.
# 🛡️ ScutumGuardBot

**ScutumGuardBot** is an AI-powered moderation microservice for Telegram bots, channels, and groups.  
It checks messages and prevents the publication of content related to adult services, drugs, weapons, violence, and spam — **before it reaches your audience**.

---

## ✨ Features

- 🚫 Blocks: adult content, drugs, weapons, hate speech, violence, spam
- ⚡ Lightning-fast API for message validation
- 🔌 Plug & Play integration with any Telegram bot
- 🔐 Privacy Mode OFF support for group moderation
- 🌍 External API: can be used by websites and other systems
- 💸 Free tier, scalable infrastructure, monetization-ready

---

## 📦 Project Structure
scutumguard/
├── main.py            # FastAPI application + API endpoints
├── moderation.py      # Message filtering logic
├── config.py          # Loads .env config
├── .env               # Contains secrets like BOT_TOKEN
├── requirements.txt   # Python dependencies
└── README.md          # This documentation
---

## 🔗 API Usage

### Endpoint
POST /check_ad
Content-Type: application/json

### Request Body

```json
{
  "text": "Sample message text"
}

Response

If the message is clean:
{
  "status": "ok"
}
If the message contains violations:
{
  "status": "violation",
  "reason": "Detected forbidden word: 'гаш'"
}
🧪 Local Development
	1.	Install dependencies:
pip install -r requirements.txt
2.	Create a .env file with your bot token:
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
3.	Run the server locally:
3.	Run the server locally:
🚀 Deployment on Render
	1.	Set the Start Command:
🚀 Deployment on Render
	1.	Set the Start Command:
        2.	Add environment variable BOT_TOKEN in Render’s dashboard.
	3.	Done — your bot and API are live!

🧩 Integration

Use this API inside your Telegram bot’s message flow:
response = requests.post("https://your-api-url.com/check_ad", json={"text": ad_text})
if response.json().get("status") == "ok":
    publish_ad()
else:
    warn_user(response.json().get("reason"))

📬 Contact & Licensing

Want to integrate, white-label, or discuss monetization?
📩 Contact us via @SafeScutumBot

© 2025 Scutum AI. All rights reserved.



