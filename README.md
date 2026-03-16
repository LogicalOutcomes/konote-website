# KoNote Website

Bilingual (EN/FR) marketing website for [KoNote](https://github.com/LogicalOutcomes/konote), an open source participant outcome management system for nonprofits.

Built with Hugo, served by Caddy, with Pagefind search and an AI chatbot.

## Structure

```
konote-website/
├── hugo.toml                  # Hugo config (bilingual)
├── content/
│   ├── en/                    # English pages (11 pages)
│   └── fr/                    # French pages (11 pages)
├── i18n/
│   ├── en.yaml                # English UI strings
│   └── fr.yaml                # French UI strings
├── layouts/                   # Hugo templates and partials
├── static/
│   ├── css/style.css          # Stylesheet
│   ├── js/search.js           # Pagefind search (bilingual)
│   ├── js/chatbot.js          # Chat widget
│   └── img/                   # Images
├── chatbot/                   # FastAPI chatbot API
│   ├── main.py                # API endpoint
│   ├── content_loader.py      # Knowledge base loader
│   ├── Dockerfile             # Chatbot container
│   └── knowledge/             # Curated knowledge base
├── Dockerfile                 # Website container (Hugo + Caddy)
├── Caddyfile                  # Caddy config with language detection
└── railway.toml               # Railway deployment config
```

## Local Development

```bash
# Install Hugo (https://gohugo.io/installation/)
hugo server
# Site available at http://localhost:1313/en/ and /fr/
```

## Deployment

Both services deploy on Railway:

1. **Website**: Uses root `Dockerfile` (Hugo build + Pagefind + Caddy)
2. **Chatbot API**: Uses `chatbot/Dockerfile` — see `chatbot/README.md`

## Licence

This website is released under the MIT Licence, same as KoNote itself.
