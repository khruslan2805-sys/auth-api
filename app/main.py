from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="Auth API")


@app.get("/")
def root():
    return {
        "message": "Auth API is running 🚀",
        "db_url": settings.DATABASE_URL,
        "secret_key": settings.SECRET_KEY,
    }
