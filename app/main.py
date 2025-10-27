from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, users

# создаём таблицы при старте (для простоты)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth API")
app.include_router(auth.router)
app.include_router(users.router)
