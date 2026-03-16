"""KoNote chatbot API — context stuffing with OpenRouter."""

import os
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from config import (
    CHAT_MODEL,
    MAX_HISTORY_LENGTH,
    MAX_QUERY_LENGTH,
    OPENROUTER_API_KEY,
    SYSTEM_PROMPTS,
    WEBSITE_URL,
)
from content_loader import load_content

# --- Load knowledge base ---
knowledge = {
    "en": load_content("knowledge/site/en/") + "\n" + load_content("knowledge/curated/en/"),
    "fr": load_content("knowledge/site/fr/") + "\n" + load_content("knowledge/curated/fr/"),
}

# --- HTTP client lifecycle ---
http_client: httpx.AsyncClient | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global http_client
    http_client = httpx.AsyncClient(timeout=60.0)
    yield
    await http_client.aclose()


# --- App setup ---
app = FastAPI(title="KoNote Chatbot API", lifespan=lifespan)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=[WEBSITE_URL],
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please try again later."},
    )


# --- Models ---
class HistoryMessage(BaseModel):
    role: str = Field(pattern=r"^(user|assistant)$")
    content: str = Field(max_length=2000)


class ChatRequest(BaseModel):
    query: str = Field(min_length=1, max_length=MAX_QUERY_LENGTH)
    language: str = "en"
    history: list[HistoryMessage] = Field(default_factory=list, max_length=MAX_HISTORY_LENGTH)


class ChatResponse(BaseModel):
    response: str
    sources: list[str] = Field(default_factory=list)


# --- API call ---
async def call_openrouter(messages: list[dict], lang: str) -> str:
    """Call OpenRouter API and return the response text."""
    try:
        resp = await http_client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": WEBSITE_URL,
                "X-Title": "KoNote Website Chatbot",
            },
            json={
                "model": CHAT_MODEL,
                "messages": messages,
                "max_tokens": 1024,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except (httpx.HTTPStatusError, httpx.RequestError, KeyError, IndexError):
        error_msg = {
            "en": "I'm having trouble connecting right now. Please try again in a moment.",
            "fr": "J'ai des difficultés de connexion en ce moment. Veuillez réessayer dans un instant.",
        }
        return error_msg.get(lang, error_msg["en"])


# --- Endpoints ---
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "en_content_length": len(knowledge["en"]),
        "fr_content_length": len(knowledge["fr"]),
    }


@app.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
async def chat(request: Request, body: ChatRequest):
    lang = body.language if body.language in ("en", "fr") else "en"

    system_content = SYSTEM_PROMPTS[lang] + knowledge[lang]
    messages = [
        {"role": "system", "content": system_content},
        *[{"role": m.role, "content": m.content} for m in body.history[-MAX_HISTORY_LENGTH:]],
        {"role": "user", "content": body.query},
    ]

    response_text = await call_openrouter(messages, lang)

    return ChatResponse(response=response_text, sources=[])
