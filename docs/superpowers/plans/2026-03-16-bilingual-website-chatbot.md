# Bilingual KoNote Website + Chatbot Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the KoNote marketing website from 9 hand-coded English HTML pages to a Hugo bilingual (EN/FR) site with Pagefind language-filtered search and an "Ask KoNote" chatbot, deployed on Railway.

**Architecture:** Hugo generates `/en/` and `/fr/` page trees from markdown content with shared templates. Pagefind builds separate search indexes per language. A FastAPI chatbot API uses context stuffing (not RAG) to answer questions via OpenRouter. Caddy serves the static site with browser language detection. Both services deploy on Railway.

**Tech Stack:** Hugo (static site generator), Caddy (static server), Pagefind (search), FastAPI + Python (chatbot API), OpenRouter (LLM gateway), Railway (hosting), vanilla JS (frontend)

**Spec:** `docs/superpowers/specs/2026-03-16-bilingual-website-chatbot-design.md`

**Translation standards:** See spec Section 6 and `c:\Users\gilli\GitHub\konote\tasks\design-rationale\bilingual-requirements.md` (KoNote app bilingual DRR). Key rules: formal "vous," Canadian French terminology (see spec Section 6.3), guillemets « » with non-breaking spaces, same-PR translation rule.

**Prompt for all translation tasks:** When translating website content to Canadian French, produce natural-reading prose (not mechanical translation). Use formal "vous," OQLF terminology, guillemets « », space before `:` `;` `?` `!`. Follow the terminology table in spec Section 6.3. Maintain the same structure and sections as English but adapt phrasing for natural French flow.

**Important — Same-PR rule:** Chunks 2 (English content) and 3 (French translation) MUST be in the same PR/branch. Do not merge English content without French translations. All chunks in this plan are on a single feature branch (`feat/bilingual-website-chatbot`) and merged together as one PR.

**Large page handling:** `features.html` (32KB, 70+ cards) and `evidence.html` (21KB) are very large pages. When converting these, work section by section: hero, then each card group, then technical specs. When translating, work in the same section-by-section pattern. Verify each section renders before proceeding to the next.

---

## Chunk 1: Hugo Foundation

### Task 1: Initialize Hugo Project

**Files:**
- Create: `hugo.toml`
- Create: `.gitignore` (update existing)
- Preserve: `css/style.css`, `js/search.js`, `img/`, favicon files

**Context:** The repo currently has HTML files at the root. Hugo expects content in `content/`, layouts in `layouts/`, and static assets in `static/`. We need to restructure without losing the existing files (they're our source material for content extraction).

- [ ] **Step 1: Install Hugo and verify it works**

Run: `hugo version`
Expected: Hugo version output (v0.139+ recommended). If not installed, install via `choco install hugo-extended` or download from gohugo.io.

- [ ] **Step 2: Create `hugo.toml` config**

```toml
baseURL = "https://konote.ca/"
languageCode = "en"
title = "KoNote"
defaultContentLanguage = "en"
defaultContentLanguageInSubdir = true
# robots.txt is served from static/robots.txt (not Hugo-generated)

[languages]
  [languages.en]
    languageName = "English"
    weight = 1
    title = "KoNote — Participant-Centred Case Management"
    [languages.en.params]
      description = "Track participant progress, measure outcomes, and demonstrate impact with KoNote."

  [languages.fr]
    languageName = "Français"
    weight = 2
    title = "KoNote — Gestion de cas centrée sur les participants"
    [languages.fr.params]
      description = "Suivez les progrès des participants, mesurez les résultats et démontrez l'impact avec KoNote."

[params]
  chatbotApiUrl = ""

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

- [ ] **Step 3: Create directory structure**

```bash
mkdir -p content/en content/fr i18n layouts/_default layouts/partials static/css static/js static/img
```

- [ ] **Step 4: Move static assets to Hugo's `static/` directory**

```bash
cp css/style.css static/css/style.css
cp js/search.js static/js/search.js
cp img/* static/img/
cp favicon* static/
cp robots.txt static/robots.txt
```

Do NOT delete the original HTML files yet — they are the source material for content extraction in later tasks.

- [ ] **Step 5: Update `.gitignore` and create `.dockerignore`**

Add to `.gitignore`:
```
public/
resources/_gen/
.hugo_build.lock
```

Create `.dockerignore`:
```
.git/
.github/
.gitignore
.worktrees/
public/
content-drafts/
node_modules/
*.md
!README.md
```

- [ ] **Step 6: Commit**

```bash
git add hugo.toml .gitignore static/ content/ i18n/ layouts/
git commit -m "feat: initialize Hugo project with bilingual config"
```

---

### Task 2: Create Base Template (`baseof.html`)

**Files:**
- Create: `layouts/_default/baseof.html`

**Context:** This is the root template that all pages inherit. It sets `<html lang="">`, includes the head partial, header, main content block, and footer. Study the current HTML files (e.g., `index.html` lines 1-20 and bottom 30 lines) for the existing structure to replicate.

- [ ] **Step 1: Read current HTML structure**

Read `index.html` to understand the current `<head>`, `<body>`, header, footer, and script patterns. All 9 HTML files share the same structure.

- [ ] **Step 2: Create `layouts/_default/baseof.html`**

```html
<!DOCTYPE html>
<html lang="{{ .Language.Lang }}">
<head>
  {{- partial "head.html" . -}}
</head>
<body>
  <a href="#main" class="skip-link">{{ i18n "skip_to_content" }}</a>

  {{- partial "header.html" . -}}

  <main id="main">
    {{- block "main" . }}{{- end }}
  </main>

  {{- partial "footer.html" . -}}

  {{- partial "search-dialog.html" . -}}
  {{- partial "chatbot-widget.html" . -}}

  <script src="/js/search.js" defer></script>
  <script src="/js/chatbot.js" defer></script>
</body>
</html>
```

- [ ] **Step 3: Commit**

```bash
git add layouts/_default/baseof.html
git commit -m "feat: add base Hugo template with bilingual lang attribute"
```

---

### Task 3: Create Head, Header, Footer, and Nav Partials

**Files:**
- Create: `layouts/partials/head.html`
- Create: `layouts/partials/header.html`
- Create: `layouts/partials/nav.html`
- Create: `layouts/partials/footer.html`
- Create: `layouts/partials/lang-switcher.html`

**Context:** Extract these from the current HTML files. Every page has the same head, header, nav, and footer. The language switcher is new — follows the KoNote app's `_lang_toggle.html` pattern (see spec Section 3.3).

- [ ] **Step 1: Read the current `index.html` header/footer/nav HTML**

Read the `<head>`, `<header>`, `<nav>`, and `<footer>` sections from `index.html`. These are duplicated across all 9 files.

- [ ] **Step 2: Create `layouts/partials/head.html`**

Port the current `<head>` content. Replace hardcoded text with Hugo variables and i18n calls:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="{{ .Description | default .Site.Params.description }}">
<title>{{ .Title }} | {{ .Site.Title }}</title>
<link rel="icon" href="/favicon.ico">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="stylesheet" href="/css/style.css">
{{ $pagefindCSS := printf "/%s/_pagefind/pagefind-ui.css" .Language.Lang }}
<link rel="stylesheet" href="{{ $pagefindCSS }}">
```

- [ ] **Step 3: Create `layouts/partials/lang-switcher.html`**

```html
{{ range .Translations }}
  <a href="{{ .Permalink }}" class="lang-link" lang="{{ .Language.Lang }}"
     aria-label="{{ if eq .Language.Lang "fr" }}Voir cette page en français{{ else }}View this page in English{{ end }}">
    {{- .Language.LanguageName -}}
  </a>
{{ end }}
```

- [ ] **Step 4: Create `layouts/partials/nav.html`**

Port the current nav structure, replacing hardcoded text with `{{ i18n "nav_features" }}` etc. Nav links must use Hugo's language-aware URL function:

```html
{{ $currentPath := .RelPermalink }}
{{ $lang := .Language.Lang }}
<nav class="main-nav" aria-label="{{ i18n "nav_label" | default "Main navigation" }}">
  <ul>
    {{ $pages := slice "features" "evidence" "getting-started" "documentation" "security" "services" "faq" "demo" }}
    {{ $keys := slice "nav_features" "nav_evidence" "nav_getting_started" "nav_documentation" "nav_security" "nav_services" "nav_faq" "nav_demo" }}
    {{ range $i, $slug := $pages }}
      {{ $key := index $keys $i }}
      {{ $href := printf "%s/" $slug | relLangURL }}
      {{ $isCurrent := eq $currentPath (printf "/%s/%s/" $lang $slug) }}
      <li><a href="{{ $href }}"{{ if $isCurrent }} aria-current="page"{{ end }}>{{ i18n $key }}</a></li>
    {{ end }}
  </ul>
</nav>
```

Note: This uses Hugo's `range` to avoid repetition and ensures `aria-current="page"` is applied to ALL nav items, not just a subset.

- [ ] **Step 5: Create `layouts/partials/header.html`**

Combine nav + lang-switcher + search button + mobile toggle into the header, matching the current HTML structure:

```html
<header class="site-header">
  <div class="container header-container">
    <a href="{{ "/" | relLangURL }}" class="site-logo" aria-label="{{ .Site.Title }} — {{ i18n "nav_home" }}">
      <img src="/img/konote-mark.png" alt="" width="24" height="22">
      <span>KoNote</span>
    </a>

    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">
      Menu
    </button>

    {{ partial "nav.html" . }}

    <div class="header-actions">
      {{ partial "lang-switcher.html" . }}
      <button class="search-trigger" aria-label="{{ i18n "search_button" }}">
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 20 20"><path d="M8 3a5 5 0 104.36 7.45l4.1 4.1a1 1 0 01-1.42 1.42l-4.1-4.1A5 5 0 018 3zm0 2a3 3 0 100 6 3 3 0 000-6z" fill="currentColor"/></svg>
      </button>
    </div>
  </div>
</header>

<script>
  document.querySelector('.nav-toggle')?.addEventListener('click', function() {
    const nav = document.querySelector('.main-nav');
    const isOpen = nav.classList.toggle('is-open');
    this.setAttribute('aria-expanded', isOpen);
  });
</script>
```

- [ ] **Step 6: Create `layouts/partials/footer.html`**

Port the current footer, replacing hardcoded text with i18n calls:

```html
<footer class="site-footer">
  <div class="container">
    <p>&copy; {{ now.Year }} {{ i18n "footer_copyright" }} <a href="https://www.gnu.org/licenses/agpl-3.0.en.html">{{ i18n "footer_license" }}</a>.</p>
  </div>
</footer>
```

- [ ] **Step 7: Commit**

```bash
git add layouts/partials/
git commit -m "feat: add Hugo partials (head, header, nav, footer, lang-switcher)"
```

---

### Task 4: Create i18n String Files and Page Templates

**Files:**
- Create: `i18n/en.yaml`
- Create: `i18n/fr.yaml`
- Create: `layouts/_default/single.html`
- Create: `layouts/index.html`
- Create: `layouts/_default/list.html`

**Context:** i18n files contain all UI strings (nav labels, footer, search, chatbot). The single.html template renders individual pages. The index.html template renders the homepage. Copy the exact YAML from spec Section 3.5.

- [ ] **Step 1: Create `i18n/en.yaml`**

Copy the complete English i18n YAML from spec Section 3.5 (lines 257-295). All 23 string entries.

- [ ] **Step 2: Create `i18n/fr.yaml`**

Copy the complete French i18n YAML from spec Section 3.5 (lines 297-335). All 23 string entries with proper accents.

- [ ] **Step 3: Create `layouts/_default/single.html`**

```html
{{ define "main" }}
<article class="page-content">
  {{ if .Params.hero }}
  {{ partial "hero.html" . }}
  {{ end }}

  <div class="container content-width">
    {{ .Content }}
  </div>
</article>
{{ end }}
```

- [ ] **Step 4: Create `layouts/index.html` (homepage)**

The homepage has a unique layout (hero + feature cards + design philosophy + target audience). Read the current `index.html` to understand its sections, then create a Hugo template that renders the homepage content within the baseof.html structure.

```html
{{ define "main" }}
{{ partial "hero.html" . }}

<div class="container">
  {{ .Content }}
</div>
{{ end }}
```

- [ ] **Step 5: Create `layouts/partials/hero.html`**

Port the hero section from the current HTML. Use frontmatter params for the title, tagline, and CTA buttons:

```html
<section class="hero">
  <div class="container">
    <h1>{{ .Params.hero_title | default .Title }}</h1>
    {{ with .Params.hero_tagline }}<p class="hero-tagline">{{ . }}</p>{{ end }}
    {{ with .Params.hero_cta }}
    <div class="hero-actions">
      {{ range . }}
      <a href="{{ .url | relLangURL }}" class="btn {{ .class | default "btn-primary" }}">{{ .text }}</a>
      {{ end }}
    </div>
    {{ end }}
  </div>
</section>
```

- [ ] **Step 6: Create `layouts/_default/list.html`**

Simple list template (used for section index pages if needed):

```html
{{ define "main" }}
<div class="container content-width">
  <h1>{{ .Title }}</h1>
  {{ .Content }}
</div>
{{ end }}
```

- [ ] **Step 7: Verify Hugo builds with empty content**

Create a minimal `content/en/_index.md`:
```markdown
---
title: "KoNote"
hero_title: "Participant-centred case management"
hero_tagline: "Track progress. Measure outcomes. Demonstrate impact."
---
```

Run: `hugo server`
Expected: Site builds and serves at localhost:1313. The `/en/` page should render with header, footer, and hero section. Styling will be partially applied (CSS is ported but content is minimal).

- [ ] **Step 8: Commit**

```bash
git add i18n/ layouts/ content/en/_index.md
git commit -m "feat: add i18n strings, page templates, and verify Hugo build"
```

---

## Chunk 2: English Content Migration

### Task 5: Convert Homepage and First 3 Pages to English Markdown

**Files:**
- Create: `content/en/_index.md` (homepage — update from Task 4 minimal version)
- Create: `content/en/features.md`
- Create: `content/en/evidence.md`
- Create: `content/en/getting-started.md`

**Context:** Extract content from the existing HTML files into markdown. The HTML files are at the repo root (`index.html`, `features.html`, `evidence.html`, `getting-started.html`). Strip HTML tags, preserve headings hierarchy, convert tables and card grids to markdown. Some HTML may be needed for complex layouts (cards, grids) — Hugo allows raw HTML in markdown with `unsafe = true`.

**Important:** Some pages (features.html at 32KB, evidence.html at 21KB) have complex card-based layouts that don't convert cleanly to plain markdown. For these, use Hugo shortcodes or raw HTML within the markdown file. The goal is to preserve the visual structure while making the content editable.

- [ ] **Step 1: Read `index.html` and extract content to `content/en/_index.md`**

Read the full `index.html`. Extract:
- Hero section content → frontmatter (`hero_title`, `hero_tagline`, `hero_cta`)
- "What KoNote Does" highlights → markdown with raw HTML for card grid
- Design philosophy section → markdown
- "Is KoNote Right For You?" section → markdown
- CTA section → markdown

Write as a markdown file with Hugo frontmatter. Preserve the existing page structure and all text exactly.

- [ ] **Step 2: Read `features.html` and extract to `content/en/features.md`**

This is the largest page (32KB, 70+ feature cards). Read the full file. Extract:
- Hero section → frontmatter
- "What KoNote Does" cards (35 cards) → preserve as raw HTML within markdown (card grid layout requires HTML)
- "What KoNote Doesn't Do" cards → raw HTML
- Technical specifications table → markdown table
- Scaling notes → markdown

- [ ] **Step 3: Read `evidence.html` and extract to `content/en/evidence.md`**

Read the full file. Extract all research sections, evidence tables, and citations into markdown.

- [ ] **Step 4: Read `getting-started.html` and extract to `content/en/getting-started.md`**

Read the full file. Extract evaluation path, deployment options, requirements checklist.

- [ ] **Step 5: Verify these 4 pages build correctly**

Run: `hugo server`
Navigate to `/en/`, `/en/features/`, `/en/evidence/`, `/en/getting-started/`
Expected: Pages render with correct content, navigation works, CSS applies.

- [ ] **Step 6: Commit**

```bash
git add content/en/
git commit -m "feat: convert homepage, features, evidence, getting-started to Hugo markdown"
```

---

### Task 6: Convert Remaining 5 Existing Pages to English Markdown

**Files:**
- Create: `content/en/documentation.md`
- Create: `content/en/security.md`
- Create: `content/en/services.md`
- Create: `content/en/faq.md`
- Create: `content/en/demo.md`

**Context:** Same approach as Task 5. Read each HTML file, extract content to markdown.

- [ ] **Step 1: Read and convert `documentation.html` → `content/en/documentation.md`**

Card-based link hub to GitHub docs (User Guide, Admin, Deployment, Developer, Compliance, API).

- [ ] **Step 2: Read and convert `security.html` → `content/en/security.md`**

Security features, shared responsibility model, encryption details, compliance info.

- [ ] **Step 3: Read and convert `services.html` → `content/en/services.md`**

Professional onboarding services, pricing model.

- [ ] **Step 4: Read and convert `faq.html` → `content/en/faq.md`**

FAQ accordion. The accordion functionality requires raw HTML with the existing CSS classes (`.faq-item`, `.faq-question`, `.faq-answer`, `.is-open`). Include the accordion JavaScript inline or as a Hugo partial.

- [ ] **Step 5: Read and convert `demo.html` → `content/en/demo.md`**

Demo page with embedded iframe. The iframe embed needs raw HTML in markdown.

- [ ] **Step 6: Verify all 9 pages build and render correctly**

Run: `hugo server`
Visit each of the 9 pages at `/en/*`. Verify content, navigation, styling.

- [ ] **Step 7: Commit**

```bash
git add content/en/
git commit -m "feat: convert documentation, security, services, faq, demo to Hugo markdown"
```

---

### Task 7: Add New Pages from Content Drafts

**Files:**
- Create: `content/en/design-principles.md`
- Create: `content/en/origins.md`
- Modify: `layouts/partials/nav.html` (add links to new pages)
- Modify: `i18n/en.yaml` (add nav strings for new pages)
- Modify: `i18n/fr.yaml` (add nav strings for new pages)

**Context:** Two draft files exist at `content-drafts/design-principles.md` and `content-drafts/origins-draft.md`. Convert these to Hugo content pages.

- [ ] **Step 1: Read `content-drafts/design-principles.md` and create `content/en/design-principles.md`**

Add Hugo frontmatter (title, description, layout). Keep the content as-is — it's already well-structured markdown.

- [ ] **Step 2: Read `content-drafts/origins-draft.md` and create `content/en/origins.md`**

Add Hugo frontmatter. The draft has a title "The Origins of KoNote" — use this.

- [ ] **Step 3: Add navigation links for new pages**

Update `layouts/partials/nav.html` to include Design Principles and Origins links. Add corresponding i18n strings to both `i18n/en.yaml` and `i18n/fr.yaml`:

```yaml
# Add to en.yaml
- id: nav_design_principles
  translation: "Design Principles"
- id: nav_origins
  translation: "Origins"

# Add to fr.yaml
- id: nav_design_principles
  translation: "Principes de conception"
- id: nav_origins
  translation: "Origines"
```

- [ ] **Step 4: Create 404 layout and content pages**

Create `layouts/404.html` (Hugo requires this specific filename for 404 handling):

```html
{{ define "main" }}
<div class="container content-width">
  <h1>{{ .Title }}</h1>
  {{ .Content }}
  <p><a href="{{ "/" | relLangURL }}">{{ if eq .Language.Lang "fr" }}Retourner à la page d'accueil{{ else }}Return to the homepage{{ end }}</a></p>
</div>
{{ end }}
```

Create `content/en/404.md`:

```markdown
---
title: "Page Not Found"
---

The page you're looking for doesn't exist or has been moved.
```

- [ ] **Step 5: Verify new pages render**

Run: `hugo server`
Visit `/en/design-principles/`, `/en/origins/`, navigate via updated nav.

- [ ] **Step 6: Commit**

```bash
git add content/en/ layouts/partials/nav.html i18n/
git commit -m "feat: add design principles, origins, and 404 pages"
```

---

### Task 8: Create Search Dialog Partial (Placeholder)

**Files:**
- Create: `layouts/partials/search-dialog.html`
- Create: `layouts/partials/chatbot-widget.html` (placeholder)

**Context:** Port the search dialog from the current HTML. The chatbot widget is a placeholder for now — it will be built in Chunk 6.

- [ ] **Step 1: Read current search dialog from any existing HTML file**

The search dialog is a `<dialog>` element at the bottom of every page.

- [ ] **Step 2: Create `layouts/partials/search-dialog.html`**

Port the dialog, using Hugo's language variable for the Pagefind bundle path:

```html
<dialog id="search-dialog" class="search-dialog">
  <div class="search-dialog-content">
    <button class="search-close" aria-label="Close search">&times;</button>
    <div id="search"></div>
  </div>
</dialog>

{{ $pagefindJS := printf "/%s/_pagefind/pagefind-ui.js" .Language.Lang }}
<script src="{{ $pagefindJS }}" defer></script>
```

- [ ] **Step 3: Create placeholder `layouts/partials/chatbot-widget.html`**

```html
<!-- Chatbot widget will be added in Chunk 6 -->
```

- [ ] **Step 4: Verify the full English site builds cleanly**

Run: `hugo --minify`
Expected: Build succeeds with 0 errors. All 11 English pages generated in `public/en/`.

Run: `ls public/en/`
Expected: Directories for each page (features/, evidence/, etc.)

- [ ] **Step 5: Commit**

```bash
git add layouts/partials/
git commit -m "feat: add search dialog and chatbot widget placeholder"
```

---

## Chunk 3: French Translation

### Task 9: Translate Homepage and First 3 Pages to French

**Files:**
- Create: `content/fr/_index.md`
- Create: `content/fr/features.md`
- Create: `content/fr/evidence.md`
- Create: `content/fr/getting-started.md`

**Context:** For each English page, create the French equivalent. The French file MUST have the same filename as its English counterpart (Hugo matches translations by filename). The French `title` in frontmatter is where the French page name goes.

**Translation prompt for all content tasks:** Translate this page into natural Canadian French following the standards in spec Section 6: formal "vous," OQLF terminology, guillemets « » with non-breaking spaces, space before `:` `;` `?` `!`. Use the terminology table in spec Section 6.3. This should read as original French prose, not a translation.

- [ ] **Step 1: Read `content/en/_index.md` and create `content/fr/_index.md`**

Translate frontmatter (title, description, hero content, CTAs) and body content. The hero tagline and CTA button text must be natural French.

- [ ] **Step 2: Read `content/en/features.md` and create `content/fr/features.md`**

This is the largest page. Translate all 70+ feature card titles and descriptions, the "What KoNote Doesn't Do" cards, technical specifications table, and scaling notes. Pay particular attention to social services terminology.

- [ ] **Step 3: Read `content/en/evidence.md` and create `content/fr/evidence.md`**

Translate research section headings, evidence descriptions, and citation context. Academic terms should follow Canadian French convention.

- [ ] **Step 4: Read `content/en/getting-started.md` and create `content/fr/getting-started.md`**

Translate evaluation path, deployment options (keep technical terms like "Railway," "Azure," "Docker" untranslated), requirements checklist.

- [ ] **Step 5: Verify French pages build and language switcher works**

Run: `hugo server`
Visit `/fr/`, `/fr/features/`, `/fr/evidence/`, `/fr/getting-started/`.
Click the language switcher — verify it links to the correct English equivalent.
Verify `<html lang="fr">` is set on French pages.

- [ ] **Step 6: Commit**

```bash
git add content/fr/
git commit -m "feat: translate homepage, features, evidence, getting-started to French"
```

---

### Task 10: Translate Remaining 7 Pages to French

**Files:**
- Create: `content/fr/documentation.md`
- Create: `content/fr/security.md`
- Create: `content/fr/services.md`
- Create: `content/fr/faq.md`
- Create: `content/fr/demo.md`
- Create: `content/fr/design-principles.md`
- Create: `content/fr/origins.md`
- Create: `content/fr/404.md`

- [ ] **Step 1: Translate `documentation.md`**

Card labels and descriptions for docs links.

- [ ] **Step 2: Translate `security.md`**

Security features, shared responsibility, encryption details. Pay attention to privacy/legal terminology (PIPEDA → LPRPDE in French).

- [ ] **Step 3: Translate `services.md`**

Onboarding services description.

- [ ] **Step 4: Translate `faq.md`**

All FAQ questions and answers. Keep accordion HTML structure identical — only translate the text content.

- [ ] **Step 5: Translate `demo.md`**

Demo page description. The iframe embed stays the same.

- [ ] **Step 6: Translate `design-principles.md`**

Design philosophy, data sovereignty, security by default sections.

- [ ] **Step 7: Translate `origins.md`**

History of KoNote. Institutional names (St. Joseph's, Griffin Centre, OTF) stay in English. Contextual descriptions translated naturally.

- [ ] **Step 8: Create `content/fr/404.md`**

```markdown
---
title: "Page introuvable"
---

La page que vous recherchez n'existe pas ou a été déplacée.
```

(The "Return to homepage" link is in the 404 layout template, not the content file.)

- [ ] **Step 9: Verify all 11 French pages build and switcher works end-to-end**

Run: `hugo server`
Visit each of the 11 French pages. Verify:
- Content is in French
- Language switcher goes to correct English page
- `<html lang="fr">` on all French pages
- Navigation labels are in French (from i18n/fr.yaml)

- [ ] **Step 10: Commit**

```bash
git add content/fr/
git commit -m "feat: translate all remaining pages to French"
```

---

## Chunk 4: Pagefind Bilingual Search

### Task 11: Update Search JS for Per-Language Indexes

**Files:**
- Modify: `static/js/search.js`

**Context:** The current search.js initializes Pagefind with default paths. For the bilingual site, each language has its own index at `/{lang}/_pagefind/`. The search JS must detect the current language and point to the correct index.

- [ ] **Step 1: Read the current `static/js/search.js`**

Understand the current initialization pattern (dialog open/close, keyboard shortcut, Pagefind init).

- [ ] **Step 2: Rewrite `static/js/search.js` with bilingual support**

```javascript
(function () {
  "use strict";

  const currentLang = document.documentElement.lang || "en";
  const bundlePath = "/" + currentLang + "/_pagefind/";

  const frTranslations = {
    placeholder: "Rechercher sur le site\u2026",
    zero_results: "Aucun résultat pour [SEARCH_TERM]",
    many_results: "[COUNT] résultats pour [SEARCH_TERM]",
    one_result: "[COUNT] résultat pour [SEARCH_TERM]",
    search_label: "Rechercher sur ce site",
    filters_label: "Filtres",
    load_more: "Charger plus de résultats",
  };

  const searchEl = document.getElementById("search");
  if (!searchEl) return;

  new PagefindUI({
    element: "#search",
    bundlePath: bundlePath,
    showSubResults: true,
    showImages: false,
    translations: currentLang === "fr" ? frTranslations : {},
  });

  // Search dialog open/close
  const dialog = document.getElementById("search-dialog");
  const trigger = document.querySelector(".search-trigger");
  const closeBtn = document.querySelector(".search-close");

  if (trigger && dialog) {
    trigger.addEventListener("click", () => {
      dialog.showModal();
      dialog.querySelector(".pagefind-ui__search-input")?.focus();
    });
  }

  if (closeBtn && dialog) {
    closeBtn.addEventListener("click", () => dialog.close());
  }

  if (dialog) {
    dialog.addEventListener("click", (e) => {
      if (e.target === dialog) dialog.close();
    });
  }

  // Keyboard shortcut: Ctrl+K / Cmd+K
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault();
      if (dialog) {
        dialog.showModal();
        dialog.querySelector(".pagefind-ui__search-input")?.focus();
      }
    }
  });
})();
```

- [ ] **Step 3: Verify search builds with per-language indexes**

Run:
```bash
hugo --minify
npx pagefind@latest --site public/en/ --output-subdir _pagefind/
npx pagefind@latest --site public/fr/ --output-subdir _pagefind/
```

Expected: Two separate `_pagefind/` directories created — one in `public/en/`, one in `public/fr/`.

Run: `hugo server`
(Note: For local dev, Pagefind indexes aren't served by `hugo server`. You'll need to build + serve with a separate static server to test search fully. The full test happens during deployment.)

- [ ] **Step 4: Commit**

```bash
git add static/js/search.js
git commit -m "feat: update search.js for per-language Pagefind indexes"
```

---

## Chunk 5: Chatbot Backend

### Task 12: Create Content Loader Module

**Files:**
- Create: `chatbot/content_loader.py`
- Create: `chatbot/tests/test_content_loader.py`
- Create: `chatbot/requirements.txt`
- Create: `chatbot/tests/__init__.py`
- Create: `chatbot/__init__.py`

**Context:** The content loader reads all markdown files from a directory, strips frontmatter, and concatenates them into a single string for context stuffing. It's the simplest part of the chatbot — read files, join text.

- [ ] **Step 1: Create `chatbot/requirements.txt`**

```
fastapi==0.115.*
uvicorn[standard]==0.34.*
httpx==0.28.*
slowapi==0.1.*
pydantic==2.*
pytest==8.*
pytest-asyncio==0.24.*
```

- [ ] **Step 2: Install dependencies**

```bash
cd chatbot && pip install -r requirements.txt && cd ..
```

- [ ] **Step 3: Write failing test for content loader**

Create `chatbot/tests/__init__.py` (empty) and `chatbot/tests/test_content_loader.py`:

```python
import os
import tempfile
from pathlib import Path

from content_loader import load_content


def test_load_content_reads_markdown_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page1.md").write_text(
            "---\ntitle: Test\n---\n\n# Hello\n\nSome content.", encoding="utf-8"
        )
        Path(tmpdir, "page2.md").write_text(
            "---\ntitle: Other\n---\n\n# World\n\nMore content.", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "# Hello" in result
        assert "Some content." in result
        assert "# World" in result
        assert "More content." in result


def test_load_content_strips_frontmatter():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page.md").write_text(
            "---\ntitle: Secret\ndescription: Hidden\n---\n\n# Visible", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "title: Secret" not in result
        assert "# Visible" in result


def test_load_content_includes_source_filename():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "features.md").write_text(
            "---\ntitle: Features\n---\n\n# Features page", encoding="utf-8"
        )
        result = load_content(tmpdir)
        assert "features.md" in result


def test_load_content_handles_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = load_content(tmpdir)
        assert result == ""


def test_load_content_skips_non_markdown_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "page.md").write_text("---\ntitle: A\n---\n\nContent", encoding="utf-8")
        Path(tmpdir, "image.png").write_bytes(b"\x89PNG")
        result = load_content(tmpdir)
        assert "Content" in result
        assert "PNG" not in result
```

- [ ] **Step 4: Run tests to verify they fail**

```bash
cd chatbot && python -m pytest tests/test_content_loader.py -v && cd ..
```

Expected: FAIL — `ModuleNotFoundError: No module named 'content_loader'`

- [ ] **Step 5: Implement content loader**

Create `chatbot/content_loader.py`:

```python
"""Load markdown content files for context stuffing."""

import re
from pathlib import Path

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def load_content(directory: str) -> str:
    """Read all .md files from a directory, strip frontmatter, return concatenated text.

    Each file's content is prefixed with its filename for source attribution.
    """
    content_dir = Path(directory)
    if not content_dir.exists():
        return ""

    parts = []
    for md_file in sorted(content_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        # Strip YAML frontmatter
        text = FRONTMATTER_PATTERN.sub("", text).strip()
        if text:
            parts.append(f"\n--- Source: {md_file.name} ---\n{text}")

    return "\n".join(parts)
```

- [ ] **Step 6: Run tests to verify they pass**

```bash
cd chatbot && python -m pytest tests/test_content_loader.py -v && cd ..
```

Expected: All 5 tests PASS.

- [ ] **Step 7: Commit**

```bash
git add chatbot/
git commit -m "feat: add chatbot content loader with tests"
```

---

### Task 13: Create FastAPI Chat Endpoint

**Files:**
- Create: `chatbot/main.py`
- Create: `chatbot/config.py`
- Create: `chatbot/tests/test_main.py`

**Context:** The FastAPI app has one endpoint: `POST /chat`. It takes a query, language, and optional history. It loads the pre-loaded content for the requested language, prepends it as context to the system prompt, calls OpenRouter, and streams the response back.

- [ ] **Step 1: Write failing tests for the chat endpoint**

Create `chatbot/tests/test_main.py`:

```python
import os
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

# Set env vars before importing app
os.environ.setdefault("OPENROUTER_API_KEY", "test-key")
os.environ.setdefault("WEBSITE_URL", "http://localhost:1313")

from main import app


client = TestClient(app)


def test_chat_endpoint_exists():
    response = client.post("/chat", json={"query": "test", "language": "en"})
    # Should not be 404 or 405
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
        # Should fall back to English
        call_args = mock.call_args
        assert "en" in str(call_args) or response.status_code == 200


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd chatbot && python -m pytest tests/test_main.py -v && cd ..
```

Expected: FAIL — `ModuleNotFoundError: No module named 'main'`

- [ ] **Step 3: Create `chatbot/config.py`**

```python
"""Chatbot configuration."""

import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
WEBSITE_URL = os.environ.get("WEBSITE_URL", "https://konote.ca")
CHAT_MODEL = os.environ.get("CHAT_MODEL", "mistralai/mistral-large-latest")
MAX_QUERY_LENGTH = 500
MAX_HISTORY_LENGTH = 6
DAILY_QUERY_LIMIT = 500

SYSTEM_PROMPTS = {
    "en": """You are KoNote's website assistant. You help visitors understand KoNote, a \
participant-centred case management and evaluation platform for Canadian nonprofits.

Rules:
- Respond ONLY in English
- Draw ONLY from the provided context documents. Do not fabricate information.
- If the context doesn't contain an answer, say so honestly
- Be concise and direct. Use bullet points for lists.
- When relevant, mention which section of the website has more detail
- Do not discuss pricing beyond what's in the provided context
- Do not make promises about features that aren't described in the context
- At the end of your response, cite which source documents you drew from

The following documents contain everything you know about KoNote:
""",
    "fr": """Vous êtes l'assistant du site Web de KoNote. Vous aidez les visiteurs à \
comprendre KoNote, une plateforme de gestion de cas et d'évaluation centrée \
sur les participants pour les organismes à but non lucratif canadiens.

Règles :
- Répondez UNIQUEMENT en français canadien
- Utilisez le vouvoiement (« vous »)
- Utilisez les conventions typographiques françaises : guillemets « », espace avant : ; ? !
- Utilisez la terminologie canadienne : « courriel », « connexion », « téléverser »
- Tirez UNIQUEMENT des documents de contexte fournis. Ne fabriquez pas d'informations.
- Si le contexte ne contient pas de réponse, dites-le honnêtement
- Soyez concis et direct
- À la fin de votre réponse, citez les documents sources que vous avez utilisés

Les documents suivants contiennent tout ce que vous savez sur KoNote :
""",
}
```

- [ ] **Step 4: Create `chatbot/main.py`**

```python
"""KoNote chatbot API — context stuffing with OpenRouter."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import httpx

from config import (
    OPENROUTER_API_KEY,
    WEBSITE_URL,
    CHAT_MODEL,
    MAX_QUERY_LENGTH,
    MAX_HISTORY_LENGTH,
    SYSTEM_PROMPTS,
)
from content_loader import load_content

# --- App setup ---

app = FastAPI(title="KoNote Chatbot API")
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


# --- Load knowledge base at startup ---

knowledge = {
    "en": load_content("knowledge/site/en/") + "\n" + load_content("knowledge/curated/en/"),
    "fr": load_content("knowledge/site/fr/") + "\n" + load_content("knowledge/curated/fr/"),
}


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

from contextlib import asynccontextmanager

# Reuse a single httpx client for connection pooling
http_client: httpx.AsyncClient | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global http_client
    http_client = httpx.AsyncClient(timeout=60.0)
    yield
    await http_client.aclose()

# Update the FastAPI app initialization above to: app = FastAPI(title="KoNote Chatbot API", lifespan=lifespan)

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
    except (httpx.HTTPStatusError, httpx.RequestError, KeyError) as e:
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
```

- [ ] **Step 5: Run tests**

```bash
cd chatbot && python -m pytest tests/ -v && cd ..
```

Expected: All tests pass (some may need adjustment based on the actual implementation — fix any failures).

- [ ] **Step 6: Commit**

```bash
git add chatbot/
git commit -m "feat: add FastAPI chatbot with rate limiting and bilingual system prompts"
```

---

### Task 14: Chatbot Dockerfile and Knowledge Base Setup

**Files:**
- Create: `chatbot/Dockerfile`
- Create: `chatbot/knowledge/curated/en/.gitkeep`
- Create: `chatbot/knowledge/curated/fr/.gitkeep`

**Context:** The Dockerfile uses the repo root as build context. It copies both the chatbot code and the Hugo content directories into the container. Curated knowledge base documents (evaluation handbook, etc.) go in `chatbot/knowledge/curated/`.

- [ ] **Step 1: Create `chatbot/Dockerfile`**

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy chatbot code
COPY chatbot/*.py /app/
COPY chatbot/knowledge/curated/ /app/knowledge/curated/

# Copy website content for context stuffing
COPY content/en/ /app/knowledge/site/en/
COPY content/fr/ /app/knowledge/site/fr/

# Railway injects $PORT; default to 8000 for local dev
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

- [ ] **Step 2: Create placeholder curated knowledge directories**

```bash
mkdir -p chatbot/knowledge/curated/en chatbot/knowledge/curated/fr
touch chatbot/knowledge/curated/en/.gitkeep chatbot/knowledge/curated/fr/.gitkeep
```

- [ ] **Step 3: Add curated knowledge documents**

For each curated document, BOTH English and French versions must be added together (same-PR rule).

Start with smaller documents first. The evaluation handbook (61KB) is deferred to a follow-up PR because it requires significant translation effort. For launch, the chatbot knowledge base includes:
- Website content (automatically copied from `content/en/` and `content/fr/`)
- Any shorter curated documents (bilingual requirements summary, design principles context)

Create a `chatbot/knowledge/curated/en/about-konote.md` and `chatbot/knowledge/curated/fr/about-konote.md` with a concise overview of KoNote drawn from the origins draft and design principles draft. This gives the chatbot background context beyond the website pages themselves.

- [ ] **Step 4: Verify Dockerfile builds locally (optional — requires Docker)**

```bash
docker build -f chatbot/Dockerfile -t konote-chatbot .
docker run -p 8000:8000 -e OPENROUTER_API_KEY=test konote-chatbot
curl http://localhost:8000/health
```

Expected: Health endpoint returns OK with content lengths > 0.

- [ ] **Step 5: Commit**

```bash
git add chatbot/
git commit -m "feat: add chatbot Dockerfile and curated knowledge base"
```

---

## Chunk 6: Chatbot Frontend Widget

### Task 15: Build the Chatbot Widget (Vanilla JS)

**Files:**
- Create: `static/js/chatbot.js`
- Modify: `layouts/partials/chatbot-widget.html` (replace placeholder)
- Modify: `static/css/style.css` (add chatbot CSS)

**Context:** A lightweight "Ask KoNote" button in the bottom-right corner that opens a chat panel. No frameworks — vanilla JS. Must be accessible (keyboard navigation, ARIA labels, screen reader announcements). Must detect the current language and pass it to the API.

- [ ] **Step 1: Create `static/js/chatbot.js`**

```javascript
(function () {
  "use strict";

  const lang = document.documentElement.lang || "en";
  const apiUrl = document.body.dataset.chatbotApi;
  if (!apiUrl) return;

  const widget = document.getElementById("chatbot-widget");
  const panel = document.getElementById("chatbot-panel");
  const toggleBtn = document.getElementById("chatbot-toggle");
  const closeBtn = document.getElementById("chatbot-close");
  const form = document.getElementById("chatbot-form");
  const input = document.getElementById("chatbot-input");
  const messages = document.getElementById("chatbot-messages");
  const disclaimer = document.getElementById("chatbot-disclaimer");

  if (!widget || !panel || !toggleBtn || !form || !input || !messages) return;

  let history = [];
  let isOpen = false;

  function toggle() {
    isOpen = !isOpen;
    panel.hidden = !isOpen;
    toggleBtn.setAttribute("aria-expanded", isOpen);
    if (isOpen) {
      input.focus();
      if (messages.children.length === 0 && disclaimer) {
        disclaimer.hidden = false;
      }
    }
  }

  function addMessage(role, text) {
    const div = document.createElement("div");
    div.className = "chatbot-msg chatbot-msg--" + role;
    div.textContent = text;
    if (role === "assistant") {
      div.setAttribute("aria-live", "polite");
    }
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function setLoading(on) {
    const existing = messages.querySelector(".chatbot-msg--loading");
    if (on && !existing) {
      const div = document.createElement("div");
      div.className = "chatbot-msg chatbot-msg--loading";
      div.setAttribute("aria-live", "polite");
      div.textContent = lang === "fr" ? "Réflexion en cours\u2026" : "Thinking\u2026";
      messages.appendChild(div);
      messages.scrollTop = messages.scrollHeight;
    } else if (!on && existing) {
      existing.remove();
    }
  }

  async function sendMessage(query) {
    addMessage("user", query);
    setLoading(true);

    try {
      const resp = await fetch(apiUrl + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, language: lang, history }),
      });

      if (resp.status === 429) {
        setLoading(false);
        addMessage("assistant", lang === "fr"
          ? "Trop de demandes. Veuillez réessayer dans un moment."
          : "Too many requests. Please try again in a moment.");
        return;
      }

      if (!resp.ok) throw new Error("API error: " + resp.status);

      const data = await resp.json();
      setLoading(false);
      addMessage("assistant", data.response);

      history.push({ role: "user", content: query });
      history.push({ role: "assistant", content: data.response });
      // Keep last 6 messages
      if (history.length > 6) history = history.slice(-6);
    } catch (err) {
      setLoading(false);
      addMessage("assistant", lang === "fr"
        ? "Désolé, je n'ai pas pu traiter votre question. Veuillez réessayer."
        : "Sorry, I couldn't process your question. Please try again.");
    }
  }

  toggleBtn.addEventListener("click", toggle);
  if (closeBtn) closeBtn.addEventListener("click", toggle);

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const query = input.value.trim();
    if (!query) return;
    input.value = "";
    sendMessage(query);
  });

  // Close on Escape
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && isOpen) toggle();
  });
})();
```

- [ ] **Step 2: Update `layouts/partials/chatbot-widget.html`**

Replace the placeholder with the full widget HTML:

```html
{{ $chatbotApiUrl := .Site.Params.chatbotApiUrl }}
{{ if $chatbotApiUrl }}
<div id="chatbot-widget" data-chatbot-api="{{ $chatbotApiUrl }}">
  <button id="chatbot-toggle" class="chatbot-toggle-btn" aria-expanded="false" aria-controls="chatbot-panel">
    <span class="chatbot-toggle-label">{{ i18n "ask_konote" }}</span>
    <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
  </button>

  <div id="chatbot-panel" class="chatbot-panel" hidden>
    <div class="chatbot-header">
      <h2 class="chatbot-title">{{ i18n "ask_konote" }}</h2>
      <button id="chatbot-close" class="chatbot-close" aria-label="Close">&times;</button>
    </div>
    <div id="chatbot-messages" class="chatbot-messages" role="log" aria-live="polite"></div>
    <p id="chatbot-disclaimer" class="chatbot-disclaimer" hidden>{{ i18n "chatbot_disclaimer" }}</p>
    <form id="chatbot-form" class="chatbot-form">
      <label for="chatbot-input" class="visually-hidden">{{ i18n "chatbot_placeholder" }}</label>
      <input id="chatbot-input" type="text" class="chatbot-input" placeholder="{{ i18n "chatbot_placeholder" }}" maxlength="500" autocomplete="off">
      <button type="submit" class="chatbot-send btn btn-primary">
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 20 20" fill="currentColor"><path d="M2.94 17.06a1 1 0 01-.3-1.02L4.38 10 2.64 3.96a1 1 0 011.32-1.22l14 6a1 1 0 010 1.82l-14 6a1 1 0 01-1.02-.5z"/></svg>
      </button>
    </form>
  </div>
</div>
{{ end }}
```

Note: The `data-chatbot-api` attribute on the body should be moved to the widget container. Update `chatbot.js` to read from `widget.closest('[data-chatbot-api]').dataset.chatbotApi` or from the widget's parent.

Actually, simpler: put it on `<body>` in `baseof.html`:

Add to `layouts/_default/baseof.html` on the `<body>` tag:
```html
<body data-chatbot-api="{{ .Site.Params.chatbotApiUrl }}">
```

- [ ] **Step 3: Add chatbot CSS to `static/css/style.css`**

Append chatbot styles to the end of the existing CSS file. Style the floating button, slide-up panel, message bubbles, input form. Use the existing CSS custom properties (colours, spacing, fonts) for consistency.

Key CSS requirements:
- `.chatbot-toggle-btn` — fixed bottom-right, z-index above content
- `.chatbot-panel` — fixed bottom-right, above toggle button, max-width 400px, max-height 500px
- `.chatbot-msg--user` — right-aligned, primary colour background
- `.chatbot-msg--assistant` — left-aligned, light background
- `.chatbot-msg--loading` — pulsing animation
- `.chatbot-form` — flex row (input + send button)
- Responsive: full-width on mobile (<768px)
- Print: hide chatbot entirely

- [ ] **Step 4: Verify chatbot widget renders**

Run: `hugo server`
Expected: "Ask KoNote" button visible in bottom-right corner. Clicking opens the chat panel. Panel shows input field and disclaimer. (Chat won't work yet — no API running locally.)

- [ ] **Step 5: Commit**

```bash
git add static/js/chatbot.js static/css/style.css layouts/partials/chatbot-widget.html layouts/_default/baseof.html
git commit -m "feat: add chatbot frontend widget with bilingual support"
```

---

## Chunk 7: Deployment Configuration

### Task 16: Create Website Dockerfile and Caddyfile

**Files:**
- Create: `Dockerfile` (root — website service)
- Create: `Caddyfile`

**Context:** Railway deploys Docker containers. The website needs a multi-stage build: Hugo builds the site, Pagefind indexes per language, Caddy serves static files. The Caddyfile handles root URL language detection and custom 404 pages.

- [ ] **Step 1: Create `Dockerfile` at repo root**

```dockerfile
# Stage 1: Build with Hugo + Pagefind
FROM hugomods/hugo:go-git-0.141.0 AS builder
RUN apk add --no-cache nodejs npm
WORKDIR /src
COPY . .
RUN hugo --minify
RUN npx pagefind@latest --site public/en/ --output-subdir _pagefind/
RUN npx pagefind@latest --site public/fr/ --output-subdir _pagefind/

# Stage 2: Serve with Caddy
FROM caddy:2-alpine
COPY --from=builder /src/public /srv
COPY Caddyfile /etc/caddy/Caddyfile
EXPOSE 8080
```

Note: The Hugo image tag should match the version installed locally. Check `hugo version` and adjust.

- [ ] **Step 2: Create `Caddyfile`**

```
:{$PORT:8080} {
    root * /srv

    # Root URL: detect browser language preference
    @root path /
    handle @root {
        @french header_regexp Accept-Language (?i)fr
        redir @french /fr/ temporary
        redir * /en/ temporary
    }

    # Custom 404 pages per language subtree
    handle /en/* {
        root * /srv
        try_files {path} {path}/index.html /en/404.html
        file_server
    }

    handle /fr/* {
        root * /srv
        try_files {path} {path}/index.html /fr/404.html
        file_server
    }

    # Fallback for any other path
    handle {
        redir * /en/ temporary
    }

    encode gzip
}
```

- [ ] **Step 3: Verify Docker build locally (requires Docker)**

```bash
docker build -t konote-website .
docker run -p 8080:8080 konote-website
curl -I http://localhost:8080/
curl -I http://localhost:8080/en/features/
curl -I -H "Accept-Language: fr" http://localhost:8080/
```

Expected:
- `/` → redirects to `/en/` (or `/fr/` with French Accept-Language)
- `/en/features/` → 200 OK with HTML content
- French header → redirects to `/fr/`

- [ ] **Step 4: Commit**

```bash
git add Dockerfile Caddyfile
git commit -m "feat: add website Dockerfile (Hugo+Caddy) and Caddyfile with language detection"
```

---

### Task 17: Railway Configuration

**Files:**
- Create: `railway.toml` (or configure via Railway dashboard)

**Context:** Railway needs to know how to build and deploy both services. The website service uses the root Dockerfile. The chatbot service uses `chatbot/Dockerfile` with the repo root as build context.

- [ ] **Step 1: Create `railway.toml` for the website service**

```toml
[build]
builder = "dockerfile"
dockerfilePath = "Dockerfile"

[deploy]
healthcheckPath = "/en/"
healthcheckTimeout = 30
restartPolicyType = "on_failure"
```

- [ ] **Step 2: Document chatbot Railway setup**

The chatbot service is configured separately in the Railway dashboard:
- **Root directory:** `/` (repo root)
- **Dockerfile path:** `chatbot/Dockerfile`
- **Environment variables:** `OPENROUTER_API_KEY`, `WEBSITE_URL`, `CHAT_MODEL`
- **Health check:** `/health`

Create a brief `chatbot/README.md`:

```markdown
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
```

- [ ] **Step 3: Update `hugo.toml` with chatbot API URL placeholder**

Once the chatbot is deployed on Railway, update `hugo.toml`:
```toml
[params]
  chatbotApiUrl = "https://your-chatbot-service.up.railway.app"
```

Leave blank for now — set after Railway deployment.

- [ ] **Step 4: Commit**

```bash
git add railway.toml chatbot/README.md
git commit -m "feat: add Railway deployment configuration"
```

---

### Task 18: Clean Up Old HTML Files and Finalize

**Files:**
- Delete: `index.html`, `features.html`, `evidence.html`, `getting-started.html`, `documentation.html`, `security.html`, `services.html`, `faq.html`, `demo.html`
- Delete: `css/` directory (moved to `static/css/`)
- Delete: `js/` directory (moved to `static/js/`)
- Delete: `img/` directory (moved to `static/img/`)
- Delete: Root favicon files (moved to `static/`)
- Modify: `README.md` (update with new project structure)

**Context:** Now that all content is migrated to Hugo markdown and templates, the old HTML files and root-level asset directories are no longer needed. This is the final cleanup task.

**IMPORTANT:** Verify the Hugo build produces all pages correctly BEFORE deleting the source HTML files.

- [ ] **Step 1: Verify complete Hugo build**

```bash
hugo --minify
```

Expected: 0 errors, 22+ pages generated (11 EN + 11 FR + 404 pages).

Check output:
```bash
ls public/en/
ls public/fr/
```

Both should contain: features/, evidence/, getting-started/, documentation/, security/, services/, faq/, demo/, design-principles/, origins/, 404.html, index.html

- [ ] **Step 2: Remove old HTML files and root asset directories**

```bash
git rm index.html features.html evidence.html getting-started.html documentation.html security.html services.html faq.html demo.html
git rm -r css/ js/ img/
git rm -r images/ 2>/dev/null || true
git rm favicon.ico favicon.svg favicon-16.png favicon-32.png
git rm robots.txt
```

Keep `content-drafts/` — these are reference material.

- [ ] **Step 3: Update README.md**

Update the README to reflect the new Hugo-based project structure, bilingual support, and deployment instructions.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: remove old HTML files, complete migration to Hugo"
```

---

## Chunk 8: End-to-End Verification

### Task 19: Local End-to-End Test

- [ ] **Step 1: Build and verify the complete site**

```bash
hugo --minify
npx pagefind@latest --site public/en/ --output-subdir _pagefind/
npx pagefind@latest --site public/fr/ --output-subdir _pagefind/
```

- [ ] **Step 2: Serve locally and test all pages**

Use a static file server to test the full build (including Pagefind):

```bash
npx serve public/ -l 8080
```

Test checklist:
- [ ] `http://localhost:8080/en/` — English homepage renders
- [ ] `http://localhost:8080/fr/` — French homepage renders
- [ ] Language switcher on every page links to correct translation
- [ ] All 11 EN pages render with correct content
- [ ] All 11 FR pages render with correct content
- [ ] `<html lang="en">` on EN pages, `<html lang="fr">` on FR pages
- [ ] Navigation labels are in the correct language
- [ ] Search dialog opens (Ctrl+K), returns results in current language
- [ ] FAQ accordion works on both EN and FR
- [ ] Skip-to-content link works
- [ ] Mobile nav toggle works
- [ ] 404 pages render for invalid URLs

- [ ] **Step 3: Test chatbot API locally**

```bash
cd chatbot
OPENROUTER_API_KEY=your-key python -m uvicorn main:app --reload --port 8000
```

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is KoNote?", "language": "en"}'
```

Expected: JSON response with a relevant answer about KoNote.

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "Qu'\''est-ce que KoNote?", "language": "fr"}'
```

Expected: JSON response in Canadian French.

- [ ] **Step 4: Commit any fixes**

If any issues were found during testing, fix them and commit.

---

### Task 20: Deploy to Railway

- [ ] **Step 1: Push branch and create PR**

```bash
git push -u origin feat/bilingual-website-chatbot
```

Create a PR to `main` with a summary of all changes.

- [ ] **Step 2: Deploy website service on Railway**

1. Connect the GitHub repo to Railway
2. Railway auto-detects the root `Dockerfile`
3. Set the public domain
4. Verify the site loads at the assigned URL

- [ ] **Step 3: Deploy chatbot service on Railway**

1. Create a second service in the same Railway project
2. Set Dockerfile path to `chatbot/Dockerfile`
3. Set build context to repo root
4. Add environment variables:
   - `OPENROUTER_API_KEY`
   - `WEBSITE_URL` (the website's Railway URL)
   - `CHAT_MODEL` (e.g., `mistralai/mistral-large-latest`)
5. Verify `/health` endpoint returns OK

- [ ] **Step 4: Connect chatbot to website**

Update `hugo.toml` with the chatbot service URL:
```toml
[params]
  chatbotApiUrl = "https://your-chatbot-service.up.railway.app"
```

Commit and push — Railway auto-deploys.

- [ ] **Step 5: End-to-end verification on production**

- [ ] Visit `/` — redirects to `/en/` (or `/fr/` with French browser)
- [ ] All 11 EN pages load
- [ ] All 11 FR pages load
- [ ] Language switcher works
- [ ] Search returns language-appropriate results
- [ ] Chatbot answers questions in English
- [ ] Chatbot answers questions in French
- [ ] Rate limiting works (send 11 requests in a minute — 11th should be rejected)
- [ ] `robots.txt` serves correctly (`Disallow: /`)

- [ ] **Step 6: Final commit and merge**

```bash
git commit -m "feat: connect chatbot API URL for production deployment"
```

Merge the PR. Clean up the feature branch.

---

## Implementation Prompt

The following prompt should be used when starting the implementation session:

---

**Implementation Prompt for Claude Code:**

You are implementing the bilingual KoNote website migration. Follow the plan at `docs/superpowers/plans/2026-03-16-bilingual-website-chatbot.md` step by step.

**Key references:**
- Design spec: `docs/superpowers/specs/2026-03-16-bilingual-website-chatbot-design.md`
- KoNote bilingual requirements: `c:\Users\gilli\GitHub\konote\tasks\design-rationale\bilingual-requirements.md`
- Current HTML files (source material): root directory (`index.html`, `features.html`, etc.)

**Translation rules (non-negotiable):**
- Every English page MUST have a French equivalent in the same commit
- French content must be natural Canadian French, not mechanical translation
- Use formal "vous," OQLF terminology, guillemets « » with non-breaking spaces
- Follow the terminology table in spec Section 6.3
- Space before `:` `;` `?` `!`

**Content extraction rules:**
- When converting HTML to markdown, preserve ALL text exactly — do not summarize or omit
- Maintain heading hierarchy (h1, h2, h3, etc.)
- For complex HTML layouts (card grids, accordions), use raw HTML within markdown
- Preserve all links, including external URLs

**Quality checks before each commit:**
- `hugo --minify` builds with 0 errors
- All pages render in both languages
- Language switcher links to the correct page

**Work through the plan chunk by chunk. After completing each chunk, verify all pages build correctly before moving to the next chunk.**

---
