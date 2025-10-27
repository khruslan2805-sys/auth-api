from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./auth.db"
    JWT_SECRET: str = "change_this_secret_for_prod"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
