# app/crud.py
from sqlalchemy.orm import Session
import bcrypt
from app import models, schemas

# bcrypt: будем хешировать напрямую, работая с байтами
# bcrypt принимает только первые 72 байта — поэтому мы обрезаем строго по байтам


def _to_safe_bytes(password: str) -> bytes:
    if isinstance(password, str):
        b = password.encode("utf-8")
    else:
        b = bytes(password)
    if len(b) > 72:
        return b[:72]
    return b


def get_password_hash(password: str) -> str:
    """
    Возвращает bcrypt-хеш в виде строки (utf-8).
    Гарантированно обрезаем пароль до 72 байт перед хешированием.
    """
    pw_bytes = _to_safe_bytes(password)
    hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
    # возвращаем строку (utf-8)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверяет пароль (с учётом обрезки до 72 байт).
    """
    pw_bytes = _to_safe_bytes(plain_password)
    # hashed_password в базе у нас хранится как str, переведём в bytes
    if isinstance(hashed_password, str):
        hashed_bytes = hashed_password.encode("utf-8")
    else:
        hashed_bytes = bytes(hashed_password)
    try:
        return bcrypt.checkpw(pw_bytes, hashed_bytes)
    except Exception:
        return False


def get_user_by_email(db: Session, email: str):
    """
    Возвращает пользователя по email.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Создаёт пользователя: хешируем пароль безопасно и сохраняем.
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email, hashed_password=hashed_password, is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
