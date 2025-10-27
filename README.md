# 🔐 Auth API — FastAPI Authentication & User Management Service

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend%20Framework-009688)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/tests-passed-success)
![Status](https://img.shields.io/badge/status-active-success)

> Auth API — продакшен-ориентированное решение для аутентификации и управления пользователями на базе FastAPI.  
> Проект реализует современные подходы к архитектуре, безопасности и структуре Python-приложений, накопленные за год коммерческой разработки backend-сервисов.

---

## 🧭 Краткое описание

API предоставляет готовую инфраструктуру для регистрации, авторизации и управления пользователями через JWT.  
Архитектура построена по принципам чистой архитектуры (Clean Architecture) и разделения ответственности: модели, схемы, маршруты и бизнес-логика оформлены отдельно для масштабируемости и тестируемости.

---

## 🚀 Основные возможности

- 🔑 Регистрация и аутентификация пользователей (JWT)
- 🧩 Ролевая модель доступа (User / Admin)
- 🛡️ Хэширование паролей (PassLib)
- 🧾 Валидация данных через Pydantic
- 🗃️ Поддержка SQLite / PostgreSQL (через SQLAlchemy)
- 🧠 Асинхронная работа на FastAPI
- 🧪 Покрытие тестами с pytest
- 📄 Swagger UI и ReDoc автодокументация
- ⚙️ Готовность к контейнеризации (Docker-ready)

---

## 🧠 Технологический стек

| Компонент | Используется для |
|------------|------------------|
| FastAPI | высокопроизводительный backend |
| SQLAlchemy | ORM для работы с БД |
| Pydantic | строгая валидация входных данных |
| Uvicorn | ASGI сервер |
| PassLib / bcrypt | безопасное хэширование паролей |
| Pytest | тестирование API |
| Docker / dotenv | контейнеризация и конфигурация окружения |

---

## ⚙️ Установка и запуск проекта

### 1️⃣ Клонируй репозиторий
```bash
git clone https://github.com/khruslan2805-sys/auth-api.git
cd auth-api

