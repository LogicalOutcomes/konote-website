FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy chatbot code
COPY chatbot/*.py /app/
COPY chatbot/knowledge/curated/ /app/knowledge/curated/
COPY chatbot/knowledge/core/ /app/knowledge/core/

# Copy website content for context stuffing
COPY content/en/ /app/knowledge/site/en/
COPY content/fr/ /app/knowledge/site/fr/

# Railway injects $PORT; default to 8000 for local dev
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
