# KoNote Chatbot API

## Railway Deployment

1. Create a new service in the Railway project
2. Set root directory to `/` and Dockerfile path to `chatbot/Dockerfile`
3. Add environment variables:
   - `OPENROUTER_API_KEY` — your OpenRouter API key
   - `WEBSITE_URL` — the website's public URL (for CORS)
   - `CHAT_MODEL` — OpenRouter model ID (default: `mistralai/mistral-large-latest`)
4. Set health check path to `/health`

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
