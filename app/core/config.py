import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")


settings = Settings()
