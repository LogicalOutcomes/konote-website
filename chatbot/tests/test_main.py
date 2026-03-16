import os
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

# Set env vars before importing app
os.environ.setdefault("OPENROUTER_API_KEY", "test-key")
os.environ.setdefault("WEBSITE_URL", "http://localhost:1313")

from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_endpoint_exists():
    with patch("main.call_openrouter", new_callable=AsyncMock) as mock:
        mock.return_value = "Test response"
        response = client.post("/chat", json={"query": "test", "language": "en"})
        assert response.status_code != 404
        assert response.status_code != 405


def test_chat_rejects_missing_query():
    response = client.post("/chat", json={"language": "en"})
    assert response.status_code == 422


def test_chat_rejects_long_query():
    response = client.post("/chat", json={
        "query": "x" * 501,
        "language": "en",
    })
    assert response.status_code == 422


def test_chat_defaults_to_english():
    with patch("main.call_openrouter", new_callable=AsyncMock) as mock:
        mock.return_value = "Test response"
        response = client.post("/chat", json={
            "query": "What is KoNote?",
            "language": "invalid",
        })
        assert response.status_code == 200
