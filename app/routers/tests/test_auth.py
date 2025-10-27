import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_register_and_token():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post(
            "/auth/register", json={"email": "t@test.com", "password": "pass123"}
        )
        assert r.status_code == 200
        r2 = await ac.post(
            "/auth/token", data={"username": "t@test.com", "password": "pass123"}
        )
        assert r2.status_code == 200
        assert "access_token" in r2.json()
