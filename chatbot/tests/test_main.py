import os
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

os.environ.setdefault("OPENROUTER_API_KEY", "test-key")
os.environ.setdefault("WEBSITE_URL", "http://localhost:1313")

from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "en_sections" in data
    assert "fr_sections" in data


def test_chat_endpoint_with_page_context():
    with patch("main.call_openrouter", new_callable=AsyncMock) as mock:
        mock.return_value = "Test response"
        response = client.post("/chat", json={
            "query": "What is KoNote?",
            "language": "en",
            "current_page": "/en/features/",
            "current_page_title": "Features",
        })
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "sources" in data


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


def test_chat_returns_sources():
    with patch("main.call_openrouter", new_callable=AsyncMock) as mock:
        mock.return_value = "KoNote is a case management platform."
        response = client.post("/chat", json={
            "query": "What is KoNote?",
            "language": "en",
            "current_page": "/en/features/",
        })
        data = response.json()
        assert isinstance(data["sources"], list)
        if data["sources"]:
            assert "label" in data["sources"][0]
            assert "url" in data["sources"][0]
