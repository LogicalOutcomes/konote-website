import asyncio
import os
from unittest.mock import AsyncMock, patch

import httpx
from fastapi.testclient import TestClient

os.environ.setdefault("OPENROUTER_API_KEY", "test-key")
os.environ.setdefault("WEBSITE_URL", "http://localhost:1313")

from main import app, call_openrouter, extract_followups

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["provider_configured"] is True
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


def test_extract_followups_from_inline_and_separate_lines():
    answer, followups = extract_followups(
        "KoNote est auto-hébergé.\n\n"
        "[followup: Comment commencer ?] [followup: Est-ce bilingue ?]\n"
        "[followup: Où sont les données ?]"
    )
    assert answer == "KoNote est auto-hébergé."
    assert followups == [
        "Comment commencer ?", "Est-ce bilingue ?", "Où sont les données ?",
    ]


def test_chat_reports_provider_failure_without_sources():
    with patch("main.call_openrouter", new_callable=AsyncMock) as mock:
        mock.return_value = None
        response = client.post("/chat", json={
            "query": "Qu'est-ce que KoNote ?",
            "language": "fr",
        })
    assert response.status_code == 503
    assert "difficultés de connexion" in response.json()["response"]
    assert response.json()["sources"] == []
    assert response.json()["followups"] == []


def test_missing_api_key_is_logged_without_query(caplog):
    query = "Private synthetic test question"
    with patch("main.OPENROUTER_API_KEY", ""):
        result = asyncio.run(call_openrouter(
            [{"role": "user", "content": query}], "en",
        ))
    assert result is None
    assert "not configured" in caplog.text
    assert query not in caplog.text


def test_upstream_http_failures_log_status_without_secrets(caplog):
    query = "Private synthetic test question"
    request = httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions")
    for status in (401, 402, 429, 500):
        upstream = httpx.Response(status, request=request, text="upstream secret body")
        with patch("main.http_client") as mock_client:
            mock_client.post = AsyncMock(return_value=upstream)
            result = asyncio.run(call_openrouter(
                [{"role": "user", "content": query}], "en",
            ))
        assert result is None
        assert f"upstream_status={status}" in caplog.text
    assert query not in caplog.text
    assert "test-key" not in caplog.text
    assert "upstream secret body" not in caplog.text


def test_transport_failure_is_logged_without_query(caplog):
    query = "Private synthetic test question"
    with patch("main.http_client") as mock_client:
        mock_client.post = AsyncMock(side_effect=httpx.ConnectError("connection failed"))
        result = asyncio.run(call_openrouter(
            [{"role": "user", "content": query}], "en",
        ))
    assert result is None
    assert "transport_error=ConnectError" in caplog.text
    assert query not in caplog.text


def test_malformed_provider_response_is_logged(caplog):
    request = httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions")
    upstream = httpx.Response(200, request=request, json={"choices": []})
    with patch("main.http_client") as mock_client:
        mock_client.post = AsyncMock(return_value=upstream)
        result = asyncio.run(call_openrouter(
            [{"role": "user", "content": "What is KoNote?"}], "en",
        ))
    assert result is None
    assert "malformed_response" in caplog.text
