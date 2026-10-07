# KoNote Chatbot API

## Railway Deployment

1. Connect the service to the `LogicalOutcomes/konote-website` repository.
2. Keep Root Directory at `/` (the repository root). The chatbot Dockerfile copies
   both `chatbot/` and `content/` from this build context.
3. For an existing Railway service using Config as Code, set its Config File Path
   to `/chatbot/railway.toml`. The repository-root `railway.toml` configures the
   Hugo website and must not be used by the chatbot service. Clear any custom
   Start Command so the chatbot Dockerfile's Uvicorn command runs.
   For a new service without Config as Code, set
   `RAILWAY_DOCKERFILE_PATH=/chatbot/Dockerfile` in its Variables and set the
   Healthcheck Path to `/health` in its Settings instead.
4. Add environment variables:
   - `OPENROUTER_API_KEY` — your OpenRouter API key
   - `WEBSITE_URL=https://www.konote.ca` — the website's public URL (for CORS)
   - `CHAT_MODEL` — OpenRouter model ID (default: `google/gemini-3-flash-preview`)
5. Confirm the deployment builds `chatbot/Dockerfile` and GET `/health` returns 200.

## Local Development

```bash
cd chatbot
pip install -r requirements.txt
OPENROUTER_API_KEY=your-key uvicorn main:app --reload
```

## Running Tests

```bash
cd chatbot
python -m pytest tests/ -v
```
