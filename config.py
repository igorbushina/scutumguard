import os
from dotenv import load_dotenv

load_dotenv()

SCUTUM_SECRET = os.getenv("SCUTUM_SECRET", "default_secret")# Загрузка .env и переменных окружения
