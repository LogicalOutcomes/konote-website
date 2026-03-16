# Bilingual KoNote Website with AI Chatbot — Design Specification

**Date:** 2026-03-16
**Status:** Draft — awaiting approval
**Scope:** Migrate konote-website from plain HTML to Hugo with full EN/FR bilingual support, Pagefind language-filtered search, and an "Ask KoNote" chatbot powered by open-source LLMs via OpenRouter.

---

## 1. Problem Statement

The KoNote marketing website is currently 9 hand-coded English-only HTML pages (plus 2 content drafts ready for conversion) with duplicated headers/footers. KoNote serves Canadian nonprofits where bilingual service delivery is a legal obligation (Official Languages Act, FLSA, funder requirements). The website must be fully bilingual with high-quality Canadian French. Additionally, the site contains dense, complex content (evaluation frameworks, evidence base, security details, FAQ) that would benefit from a conversational AI assistant for discovery.

### Goals

1. Every page available in both English and Canadian French
2. Pagefind search returns only results in the active language
3. "Ask KoNote" chatbot answers questions drawing from site content, KoNote docs, and curated documents
4. Translation workflow ensures French versions are created alongside English content
5. Deploy on Railway (replacing GitHub Pages)
6. Maintain WCAG 2.2 AA accessibility throughout

### Non-Goals

- Translating into languages beyond EN/FR
- Real-time chat or conversation history persistence (stateless chatbot at launch)
- User authentication on the website
- CMS or admin interface for content editing

---

## 2. Architecture Overview

```
Railway Project: konote-website
+-------------------------------------------------------+
|                                                        |
|  Service 1: Hugo Static Site                           |
|  +--------------------------------------------------+ |
|  | Hugo build -> Pagefind index -> static serving    | |
|  | Domain: konote.ca (or chosen domain)              | |
|  |                                                    | |
|  | /en/ pages  <-- Pagefind filtered to lang="en"    | |
|  | /fr/ pages  <-- Pagefind filtered to lang="fr"    | |
|  | Language switcher in header (FLSA active offer)   | |
|  | "Ask KoNote" button -> chatbot widget             | |
|  +--------------------------------------------------+ |
|                                                        |
|  Service 2: Chatbot API (FastAPI + Python)             |
|  +--------------------------------------------------+ |
|  | POST /chat {query, language, history}             | |
|  |                                                    | |
|  | 1. Load all content files for {language}           | |
|  | 2. Prepend as context to system prompt             | |
|  | 3. Call OpenRouter (Mistral/Qwen/DeepSeek)         | |
|  | 4. Stream response back to client                  | |
|  |                                                    | |
|  | No database. No vector store. No embedding model.  | |
|  | Context stuffing into 128k token window.           | |
|  +--------------------------------------------------+ |
|                                                        |
+-------------------------------------------------------+
```

### Key Architectural Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Static site generator | Hugo | Native i18n, team familiarity, markdown content |
| URL structure | `/en/page/` and `/fr/page/` path prefixes | Clear, bookmarkable, SEO-friendly, Pagefind-friendly |
| Default language | English with prominent "Français" toggle | FLSA active offer — toggle visible in header; browser language detection for root URL |
| Search | Pagefind with `lang` attribute filtering | Automatic language-scoped results, no custom code |
| Chatbot retrieval | Context stuffing (no RAG) | Corpus fits in 128k window (~80-90k tokens per language); simpler, better answer quality |
| Chatbot LLM | Open-source via OpenRouter | No vendor lock-in, model-swappable, pennies per query |
| Chatbot backend | FastAPI (Python) | Lightweight, async, single-endpoint API |
| Vector database | None | Corpus too small to justify RAG infrastructure |
| Hosting | Railway (both services) | Backend capability for chatbot API; static site serving |
| Translation workflow | Translate in same PR | Inherited from KoNote app bilingual requirements (I18N-DRR1) |

---

## 3. Hugo Bilingual Site

### 3.1 Directory Structure

```
konote-website/
+-- hugo.toml                        # Multilingual config
+-- content/
|   +-- en/
|   |   +-- _index.md                # Homepage
|   |   +-- features.md
|   |   +-- evidence.md
|   |   +-- getting-started.md
|   |   +-- documentation.md
|   |   +-- security.md
|   |   +-- services.md
|   |   +-- faq.md
|   |   +-- demo.md
|   |   +-- design-principles.md     # New page (from draft)
|   |   +-- origins.md               # New page (from draft)
|   +-- fr/
|       +-- _index.md
|       +-- features.md              # "Fonctionnalités" (same filename as EN — Hugo matches by filename)
|       +-- evidence.md              # "Données probantes"
|       +-- getting-started.md       # "Pour commencer"
|       +-- documentation.md
|       +-- security.md              # "Sécurité"
|       +-- services.md
|       +-- faq.md                   # "FAQ"
|       +-- demo.md                  # "Démo"
|       +-- design-principles.md
|       +-- origins.md
+-- i18n/
|   +-- en.yaml                      # UI strings (nav, footer, buttons, search)
|   +-- fr.yaml
+-- layouts/
|   +-- _default/
|   |   +-- baseof.html              # Base template (html lang, head, body structure)
|   |   +-- single.html              # Single page template
|   |   +-- list.html                # List/section template
|   +-- index.html                   # Homepage template
|   +-- partials/
|       +-- head.html                # Meta tags, CSS, favicons
|       +-- header.html              # Sticky header with nav + lang switcher
|       +-- nav.html                 # Navigation links (translated)
|       +-- footer.html              # Footer with links
|       +-- lang-switcher.html       # "Francais" / "English" toggle
|       +-- search-dialog.html       # Pagefind search modal
|       +-- chatbot-widget.html      # "Ask KoNote" button + chat panel
|       +-- hero.html                # Reusable hero section
+-- static/
|   +-- css/style.css                # Existing CSS (ported directly)
|   +-- js/
|   |   +-- search.js                # Updated for language filtering
|   |   +-- chatbot.js               # Chat widget client-side code
|   +-- img/
|       +-- konote-mark.png
|       +-- favicon files...
+-- chatbot/                         # Chatbot API service (separate Railway service)
|   +-- main.py                      # FastAPI app
|   +-- config.py                    # Settings, model config
|   +-- content_loader.py            # Load and prepare content for context
|   +-- Dockerfile
|   +-- requirements.txt
|   +-- knowledge/                   # Curated knowledge base documents
|       +-- en/
|       |   +-- evaluation-handbook.md
|       |   +-- bilingual-requirements.md
|       |   +-- ... (additional curated docs)
|       +-- fr/
|           +-- evaluation-handbook.md
|           +-- bilingual-requirements.md
|           +-- ...
+-- .github/workflows/deploy.yml     # Railway deployment (Hugo + Pagefind)
+-- Dockerfile                       # Hugo static site build
```

**Important: Translation pairing.** Hugo matches EN/FR translations by **filename** within the language directory. French content files must use the same filename as their English counterpart (e.g., `content/fr/features.md`, not `content/fr/fonctionnalites.md`). The French page title is set in frontmatter, not the filename.

### 3.2 Hugo Configuration

```toml
# hugo.toml
baseURL = "https://konote.ca/"    # Update to actual domain
languageCode = "en"
defaultContentLanguage = "en"
defaultContentLanguageInSubdir = true  # /en/ prefix for English too

[languages]
  [languages.en]
    languageName = "English"
    weight = 1
    [languages.en.params]
      searchPlaceholder = "Search the site..."
      searchNoResults = "No results for"
      chatbotGreeting = "Ask me anything about KoNote"

  [languages.fr]
    languageName = "Français"
    weight = 2
    [languages.fr.params]
      searchPlaceholder = "Rechercher sur le site..."
      searchNoResults = "Aucun résultat pour"
      chatbotGreeting = "Posez-moi une question sur KoNote"

[params]
  description = "KoNote - Participant-centred case management"
  chatbotApiUrl = "https://api.konote.ca"  # Or Railway-assigned URL

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true  # Allow raw HTML in markdown if needed
```

### 3.3 Language Switcher (FLSA Active Offer)

The language switcher follows the KoNote app's `_lang_toggle.html` pattern:

```html
<!-- layouts/partials/lang-switcher.html -->
{{ if eq .Language.Lang "en" }}
  {{ with .Translations }}
    {{ range . }}
      <a href="{{ .Permalink }}" class="lang-link" lang="fr"
         aria-label="Voir cette page en francais">Francais</a>
    {{ end }}
  {{ end }}
{{ else }}
  {{ with .Translations }}
    {{ range . }}
      <a href="{{ .Permalink }}" class="lang-link" lang="en"
         aria-label="View this page in English">English</a>
    {{ end }}
  {{ end }}
{{ end }}
```

Requirements:
- Visible in the header at all times (not buried in footer or dropdown)
- Shows "Français" when browsing English, "English" when browsing French
- Links to the same page in the other language (not the homepage)
- `lang` attribute set correctly for WCAG 3.1.2 compliance

### 3.4 Content Format

Each page is a markdown file with Hugo frontmatter:

```markdown
---
title: "Features"
description: "What KoNote does and what it doesn't"
layout: "single"
---

## Participant-Centred Case Management

KoNote tracks participant progress, measures outcomes...
```

French equivalent:

```markdown
---
title: "Fonctionnalités"
description: "Ce que fait KoNote et ce qu'il ne fait pas"
layout: "single"
---

## Gestion de cas centrée sur les participants

KoNote suit les progrès des participants, mesure les résultats...
```

### 3.5 UI String Translations

```yaml
# i18n/en.yaml
- id: nav_home
  translation: "Home"
- id: nav_features
  translation: "Features"
- id: nav_evidence
  translation: "Evidence"
- id: nav_getting_started
  translation: "Getting Started"
- id: nav_documentation
  translation: "Documentation"
- id: nav_security
  translation: "Security & Privacy"
- id: nav_services
  translation: "Services"
- id: nav_faq
  translation: "FAQ"
- id: nav_demo
  translation: "Demo"
- id: footer_copyright
  translation: "LogicalOutcomes. Licensed under"
- id: footer_license
  translation: "GNU Affero General Public License v3"
- id: skip_to_content
  translation: "Skip to main content"
- id: search_button
  translation: "Search"
- id: ask_konote
  translation: "Ask KoNote"
- id: chatbot_placeholder
  translation: "Ask a question about KoNote..."
- id: chatbot_thinking
  translation: "Thinking..."
- id: chatbot_error
  translation: "Sorry, I couldn't process your question. Please try again."
- id: chatbot_disclaimer
  translation: "AI-generated answers may not be perfectly accurate."
```

```yaml
# i18n/fr.yaml
- id: nav_home
  translation: "Accueil"
- id: nav_features
  translation: "Fonctionnalités"
- id: nav_evidence
  translation: "Données probantes"
- id: nav_getting_started
  translation: "Pour commencer"
- id: nav_documentation
  translation: "Documentation"
- id: nav_security
  translation: "Sécurité et confidentialité"
- id: nav_services
  translation: "Services"
- id: nav_faq
  translation: "FAQ"
- id: nav_demo
  translation: "Démo"
- id: footer_copyright
  translation: "LogicalOutcomes. Distribué sous licence"
- id: footer_license
  translation: "GNU Affero General Public License v3"
- id: skip_to_content
  translation: "Passer au contenu principal"
- id: search_button
  translation: "Rechercher"
- id: ask_konote
  translation: "Demandez à KoNote"
- id: chatbot_placeholder
  translation: "Posez une question sur KoNote..."
- id: chatbot_thinking
  translation: "Réflexion en cours..."
- id: chatbot_error
  translation: "Désolé, je n'ai pas pu traiter votre question. Veuillez réessayer."
- id: chatbot_disclaimer
  translation: "Les réponses générées par l'IA peuvent ne pas être parfaitement exactes."
```

---

## 4. Pagefind Search (Language-Filtered)

### 4.1 How It Works

Hugo generates separate subtrees for each language (`public/en/` and `public/fr/`), each with the correct `lang` attribute on `<html>`. **Pagefind builds a separate search index per language subtree.** This ensures that each language's search only contains results in that language — no filtering needed at query time.

### 4.2 Build Pipeline

```bash
# Build step (Railway or CI)
hugo --minify
npx pagefind@latest --site public/en/ --output-subdir _pagefind/
npx pagefind@latest --site public/fr/ --output-subdir _pagefind/
```

This creates:
- `public/en/_pagefind/` — index of English pages only
- `public/fr/_pagefind/` — index of French pages only

Each language's search UI points to its own index, so results are language-scoped by construction.

### 4.3 Search Initialization

```javascript
// static/js/search.js
const currentLang = document.documentElement.lang;

new PagefindUI({
  element: "#search",
  // Each language subtree has its own _pagefind/ index
  bundlePath: "/" + currentLang + "/_pagefind/",
  showSubResults: true,
  showImages: false,
  translations: currentLang === "fr" ? {
    placeholder: "Rechercher sur le site...",
    zero_results: "Aucun résultat pour [SEARCH_TERM]",
    many_results: "[COUNT] résultats pour [SEARCH_TERM]",
    one_result: "[COUNT] résultat pour [SEARCH_TERM]",
    search_label: "Rechercher sur ce site",
    filters_label: "Filtres",
    load_more: "Charger plus de résultats"
  } : {}
});
```

The search dialog, keyboard shortcut (Ctrl+K / Cmd+K), and modal pattern are carried forward from the current site.

---

## 5. Chatbot: "Ask KoNote"

### 5.1 Architecture

The chatbot uses **context stuffing** (not RAG). The entire knowledge base for the active language is loaded into the LLM's context window with each query.

**Why not RAG:**
- Single-language corpus is ~80-90k tokens — fits comfortably in 128k context window
- Better answer quality: model sees all content, can synthesize across documents
- Radically simpler: no embedding model, no vector store, no index
- Lower infrastructure cost at low traffic volumes

**Upgrade trigger for RAG:** If single-language corpus exceeds ~100k tokens or monthly API costs exceed $50.

### 5.2 Content Sources

| Source | Description | Update Frequency |
|--------|-------------|-----------------|
| Website pages | Hugo markdown content (EN + FR) | Every deploy |
| KoNote docs | User Guide, Admin Guide, Deployment Guide, etc. | Occasional |
| Curated documents | Evaluation handbook, origins story, bilingual requirements, design rationale docs | Rare |

Content is organized in the `chatbot/knowledge/` directory, separated by language.

### 5.3 API Design

```
POST /chat
Content-Type: application/json

{
  "query": "How does KoNote handle outcome measurement?",
  "language": "en",
  "history": [
    {"role": "user", "content": "What is KoNote?"},
    {"role": "assistant", "content": "KoNote is a participant-centred..."}
  ]
}

Response (streamed):
{
  "response": "KoNote integrates outcome measurement directly into...",
  "sources": ["features.md", "evidence.md"]
}
```

### 5.4 System Prompt

**English version:**
```
You are KoNote's website assistant. You help visitors understand KoNote, a
participant-centred case management and evaluation platform for Canadian
nonprofits.

Rules:
- Respond ONLY in English
- Draw ONLY from the provided context documents. Do not fabricate information.
- If the context doesn't contain an answer, say so honestly
- Be concise and direct. Use bullet points for lists.
- When relevant, mention which section of the website has more detail
- Do not discuss pricing beyond what's in the provided context
- Do not make promises about features that aren't described in the context

The following documents contain everything you know about KoNote:
```

**French version:**
```
Vous êtes l'assistant du site Web de KoNote. Vous aidez les visiteurs à
comprendre KoNote, une plateforme de gestion de cas et d'évaluation centrée
sur les participants pour les organismes à but non lucratif canadiens.

Règles :
- Répondez UNIQUEMENT en français canadien
- Utilisez le vouvoiement (« vous »)
- Utilisez les conventions typographiques françaises : guillemets « »,
  espace avant : ; ? !
- Utilisez la terminologie canadienne : « courriel », « connexion »,
  « téléverser »
- Tirez UNIQUEMENT des documents de contexte fournis. Ne fabriquez pas
  d'informations.
- Si le contexte ne contient pas de réponse, dites-le honnêtement
- Soyez concis et direct

Les documents suivants contiennent tout ce que vous savez sur KoNote :
```

### 5.5 Backend Implementation

```python
# chatbot/main.py (simplified structure)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import httpx
import os
from content_loader import load_content

app = FastAPI()

# CORS for website domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("WEBSITE_URL", "https://konote.ca")],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# Load content at startup (build-time baked into container)
content = {
    "en": load_content("knowledge/en/"),
    "fr": load_content("knowledge/fr/"),
}

SYSTEM_PROMPTS = {
    "en": "You are KoNote's website assistant...",
    "fr": "Vous êtes l'assistant du site Web de KoNote...",
}

@app.post("/chat")
async def chat(request: ChatRequest):
    lang = request.language if request.language in ("en", "fr") else "en"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPTS[lang] + content[lang]},
        *request.history[-6:],  # Last 3 exchanges for continuity
        {"role": "user", "content": request.query},
    ]

    # Call OpenRouter
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            },
            json={
                "model": os.getenv("CHAT_MODEL", "mistralai/mistral-large-latest"),
                "messages": messages,
                "max_tokens": 1024,
                "stream": True,
            },
        )
        # Stream response back to client
        ...
```

### 5.6 Client-Side Widget

A lightweight chat panel that opens from a button in the bottom-right corner:

- "Ask KoNote" / "Demandez à KoNote" button (translated via i18n)
- Opens a slide-up panel with input field and response area
- Streams responses token-by-token for perceived speed
- Shows a brief disclaimer: "AI-generated answers may not be perfectly accurate"
- Maintains conversation history within the browser session (cleared on page reload)
- No external dependencies (vanilla JS, no React/Vue)
- Accessible: keyboard navigable, ARIA labels, focus management

### 5.7 Cost Model

| Component | Monthly Cost |
|-----------|-------------|
| Railway: Hugo static site service | ~$5 |
| Railway: Chatbot API service | ~$5-10 |
| OpenRouter API (10 queries/day, Qwen/DeepSeek) | ~$9 |
| **Total** | **~$19-24/month** |

At 50 queries/day: ~$55-60/month. At 100 queries/day: ~$100/month.

### 5.8 Cold Start Strategy

Railway may scale the chatbot service to zero when idle. First query after idle takes a few seconds to spin up (no heavy model loading since we're calling an API — just container startup). Show a "Thinking..." animation in the chat widget.

### 5.9 Rate Limiting and Abuse Protection

The chatbot API is publicly accessible (CORS-restricted to the website domain, but callable directly via curl). Protection measures:

- **IP-based rate limiting:** 10 requests per minute per IP (using `slowapi` or similar)
- **Global daily cap:** 500 queries/day as a circuit breaker (returns a friendly "busy" message when exceeded)
- **OpenRouter spending limit:** Set a monthly budget cap on the OpenRouter dashboard (e.g., $50/month) to prevent runaway costs
- **Input validation:** Maximum query length (500 characters), maximum history length (6 messages), reject messages with obvious prompt injection patterns
- **No conversation history persistence on server** — history is client-side only, reducing abuse surface

### 5.10 Response Sources

The API response includes a `sources` field listing which documents the answer drew from. The system prompt instructs the model to cite its sources by document name at the end of each response. The backend parses these citations from the model's output. If the model does not cite sources, the field returns empty — this is acceptable and avoids fabricated citations.

---

## 6. Canadian French Translation Standards

Inherited from KoNote app bilingual requirements (I18N-DRR1), adapted for website content:

### 6.1 UI Strings (i18n/*.yaml)

- Short, stable strings: nav labels, button text, footer, search UI, chatbot UI
- Translated once, rarely change
- Follow KoNote app terminology table (see Section 6.3)

### 6.2 Page Content (content/fr/*.md)

- Long-form marketing/informational prose
- Must read as **natural Canadian French**, not translated English
- Same structure and sections as English, but phrasing adapted for natural flow
- French sentences are 15-20% longer — CSS must accommodate

### 6.3 Terminology Standards

| English | French (Canadian) | Notes |
|---------|-------------------|-------|
| Participant | Participant(e) | Not "client" |
| Progress note | Note d'évolution | Not "note de progrès" (calque) |
| Outcome | Résultat | In evaluation context |
| Case worker | Intervenant(e) | Not "travailleur de cas" |
| Goal | Objectif | Not "but" |
| Intake | Accueil / Admission | Context-dependent |
| Assessment | Évaluation | Not "estimation" |
| Funder | Bailleur de fonds | Standard nonprofit term |
| Nonprofit | Organisme à but non lucratif | Or "OBNL" for short |
| Self-hosted | Auto-hébergé | Technical term |
| Open source | Code source ouvert | Or "à code ouvert" |
| Dashboard | Tableau de bord | Standard |
| Deployment | Déploiement | Standard |

### 6.4 Typographic Conventions

- Formal "vous" throughout (never "tu")
- Guillemets « » for quotes (with non-breaking spaces inside: `«&nbsp;texte&nbsp;»`)
- Space before `:` `;` `?` `!`
- Canadian spelling: "courriel" (not "e-mail"), "connexion" (not "login"), "téléverser" (not "uploader")
- Inclusive writing: follow KoNote app convention ("les participant·e·s" or "les personnes participantes")
- OQLF recommendations where they exist

### 6.5 Translation Workflow

**Rule:** Every PR that adds or modifies English content MUST include the French translation. No exceptions. Translation is not a follow-up task.

**For website content (markdown pages):**
1. Write/edit the English page in `content/en/`
2. Create/update the French equivalent in `content/fr/` in the same PR
3. French content should be natural Canadian French prose, not mechanical translation

**For UI strings (i18n/*.yaml):**
1. Add the English string to `i18n/en.yaml`
2. Add the French translation to `i18n/fr.yaml` in the same commit

**For chatbot knowledge base:**
1. Add the English document to `chatbot/knowledge/en/`
2. Add the French translation to `chatbot/knowledge/fr/` in the same PR

---

## 7. Accessibility (WCAG 2.2 AA)

Carried forward from the existing site plus new bilingual requirements:

- `<html lang="en">` / `<html lang="fr">` set correctly per page (SC 3.1.1)
- Language switcher has `lang` attribute on the link text (SC 3.1.2)
- Skip navigation link
- Semantic HTML (headings hierarchy, landmarks, lists)
- Colour contrast ratios maintained (existing CSS design tokens)
- Keyboard navigation for search dialog, chatbot widget, FAQ accordion
- ARIA labels on all interactive elements
- Focus management when opening/closing search and chatbot panels
- Chatbot responses announced to screen readers (aria-live region)

---

## 8. Deployment

### 8.1 Railway Configuration

Two Railway services in one project:

**Service 1: Website (Hugo static)**
- Dockerfile: Multi-stage build — stage 1 builds with Hugo + Pagefind, stage 2 serves via Caddy
- Domain: Primary domain (konote.ca or chosen domain)

```dockerfile
# Dockerfile (root — website service)
FROM hugomods/hugo:go-git AS builder
WORKDIR /src
COPY . .
RUN hugo --minify
RUN npx pagefind@latest --site public/en/ --output-subdir _pagefind/
RUN npx pagefind@latest --site public/fr/ --output-subdir _pagefind/

FROM caddy:2-alpine
COPY --from=builder /src/public /srv
COPY Caddyfile /etc/caddy/Caddyfile
```

```
# Caddyfile
:$PORT {
    root * /srv

    # Root URL: detect browser language, redirect to /en/ or /fr/
    @root path /
    handle @root {
        @french header_regexp Accept-Language fr
        redir @french /fr/ temporary
        redir * /en/ temporary
    }

    # Custom 404 pages per language
    handle /en/* {
        try_files {path} {path}/ /en/404.html
    }
    handle /fr/* {
        try_files {path} {path}/ /fr/404.html
    }

    file_server
    encode gzip
}
```

**Service 2: Chatbot API**
- Build: Docker (Python 3.12 + FastAPI + httpx), build context is repo root
- Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Domain: Subdomain or path prefix (api.konote.ca or konote.ca/api)
- Environment variables: `OPENROUTER_API_KEY`, `WEBSITE_URL`, `CHAT_MODEL`

### 8.2 Root URL Behaviour (FLSA Active Offer)

When a visitor arrives at `konote.ca/` (no language prefix):
1. Caddy checks the `Accept-Language` header
2. If the browser prefers French (`fr`), redirect to `/fr/`
3. Otherwise, redirect to `/en/`

This respects the FLSA active offer requirement — Francophone visitors see French by default without having to find a toggle. The language switcher in the header is always available to change manually.

### 8.3 Build Pipeline

```
Push to main
  -> Railway detects changes
  -> Service 1: Docker builds Hugo + Pagefind (per-language indexes) -> Caddy serves static
  -> Service 2: Docker builds chatbot container (content baked in) -> start FastAPI
```

### 8.4 Content Sync

The chatbot's knowledge base includes the website's own markdown content. The chatbot Dockerfile uses the repo root as build context:

```dockerfile
# chatbot/Dockerfile (build context: repo root)
FROM python:3.12-slim
WORKDIR /app
COPY chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY chatbot/ /app/
COPY content/en/ /app/knowledge/site/en/
COPY content/fr/ /app/knowledge/site/fr/
```

Railway build command for this service: `docker build -f chatbot/Dockerfile .` (context is repo root, so `COPY content/` works).

This means every deploy automatically updates the chatbot's knowledge.

### 8.5 Custom 404 Pages

Hugo generates `content/en/404.md` and `content/fr/404.md` as custom error pages. Caddy's `try_files` directive serves the appropriate 404 page based on the URL prefix. The 404 page includes the language switcher and navigation, so lost visitors can find their way.

---

## 9. Migration Plan

### What Changes

| Current | After Migration |
|---------|----------------|
| 9 hand-coded HTML files + 2 drafts | Hugo markdown content + templates (11 pages) |
| Duplicated header/footer/nav in every file | Shared Hugo partials |
| English only | Full EN/FR with language switcher |
| Pagefind searches all content | Pagefind filtered by active language |
| No chatbot | "Ask KoNote" with context-stuffing LLM |
| GitHub Pages hosting | Railway hosting |
| No build step | Hugo build + Pagefind indexing |

### What Stays the Same

| Preserved Element | How |
|-------------------|-----|
| CSS design system | `style.css` ported directly (no redesign) |
| Visual design | Hugo templates replicate current HTML structure |
| Page content | Extracted from HTML to markdown (same text) |
| Pagefind search UX | Same dialog/modal pattern, same keyboard shortcut |
| Accessibility features | All WCAG features carried forward |
| robots.txt / noindex | Preserved |
| URL structure | Pages at same relative paths (with `/en/` or `/fr/` prefix) |

---

## 10. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Hugo adds complexity for non-developer | Medium | Medium | Claude handles all template work; user edits markdown only |
| French content quality drift | Medium | High | Follow KoNote app standards; periodic review |
| Context window exceeded as content grows | Low | Medium | Monitor token count; add RAG if >100k per language |
| Chatbot gives incorrect answers | Medium | Medium | System prompt limits to provided context; disclaimer shown |
| OpenRouter API outage | Low | Low | Chatbot degrades gracefully; Pagefind search still works |
| Railway costs increase with traffic | Low | Medium | Monitor usage; rate-limit chatbot if needed |
| Translation debt accumulates | Medium | High | Enforce same-PR rule; CI check for missing French files |

---

## 11. Success Criteria

1. All existing pages available in both EN and FR with natural-reading French
2. Language switcher visible and functional on every page
3. Pagefind returns only results in the active language
4. Chatbot answers questions accurately from the knowledge base in both languages
5. WCAG 2.2 AA compliance maintained (including SC 3.1.1 and 3.1.2)
6. Site deploys successfully on Railway
7. Total monthly cost under $30 at expected traffic levels
8. Page load performance comparable to or better than current static site
