import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
