# Chatbot Grounding Redesign Implementation Prompt

Use this prompt for the implementation session working on the bilingual Hugo site.

## Objective

Redesign the KoNote website chatbot grounding so it produces more accurate, better-sourced answers without changing the site's overall visual design or the Railway hosting model.

Keep these decisions fixed:

1. Keep Hugo for the website.
2. Keep Railway for hosting.
3. Keep two Railway services: website and chatbot API.
4. Do not introduce a vector database or a third service.
5. Do not redesign the website's visual style.
6. Do not broaden scope into a general UI refresh.

## Problem To Solve

The current chatbot implementation loads the entire language corpus into a single concatenated blob and sends that to the model for every request. That is simple, but it has three problems:

1. Weak structure for the model.
2. Poor source attribution.
3. Harder future refinement as content grows.

The goal is to replace raw full-corpus stuffing with structured context assembly while preserving cross-topic synthesis across related KoNote content.

## Required Outcome

Implement a structured grounding pipeline that:

1. Parses content into section-level records.
2. Always includes a small curated core pack.
3. Prioritizes the current page.
4. Adds related sections using simple deterministic rules and lexical matching.
5. Returns real source links based on selected sections.
6. Keeps English and French behavior aligned.

## Files To Inspect First

Read and understand these files before editing:

1. `chatbot/main.py`
2. `chatbot/content_loader.py`
3. `chatbot/tests/test_main.py`
4. `chatbot/tests/test_content_loader.py`
5. `static/js/chatbot.js`
6. `layouts/partials/chatbot-widget.html`
7. `content/en/**`
8. `content/fr/**`
9. `chatbot/knowledge/curated/en/**`
10. `chatbot/knowledge/curated/fr/**`

## Required Architecture

### 1. Section-aware content model

Replace the current concatenated text approach with a section-based model.

Each section record should include at minimum:

1. `language`
2. `source_type` (`site` or `curated`)
3. `page_title`
4. `page_url`
5. `section_heading`
6. `parent_heading`
7. `body`
8. `source_label`
9. `keywords`

It is acceptable to add more fields if useful.

### 2. Core pack

Create a small always-included knowledge pack per language. This should include compact, high-value grounding documents such as:

1. What KoNote is.
2. What KoNote is not.
3. Privacy and hosting responsibility basics.
4. Bilingual basics.
5. A compact conceptual map of major topics.

Use the existing curated knowledge area if practical.

### 3. Context assembly

For each chat request, assemble context from:

1. The core pack.
2. The current page.
3. Related sections selected by lexical matching.
4. Related sections selected by explicit topic relationship rules.

Do not send the full language corpus by default.

### 4. Source attribution

Return actual sources from the selected context records. Do not rely on model-generated citations. Sources should map to real pages or sections.

### 5. Frontend context

Update the chatbot frontend to send the current page context to the API, including:

1. current page path
2. current page title
3. language
4. optional current page section if easily available

### 6. No visual redesign

Limit UI changes to what is necessary for chatbot grounding improvements, such as:

1. rendering source links
2. showing a small “based on these pages” hint if useful
3. small wording updates in the chatbot panel

Do not change the broader website visual design.

## Suggested New Modules

Add modules if they improve clarity. A likely structure is:

1. `chatbot/section_parser.py`
2. `chatbot/context_selector.py`
3. `chatbot/context_rules.py`

You may choose different names if the structure is clear and tested.

## Implementation Tasks

### Task 1: Replace concatenated loading

Refactor `chatbot/content_loader.py` so it produces structured records instead of one merged string.

It must:

1. strip frontmatter
2. derive title and URL
3. split markdown by headings
4. preserve heading hierarchy where practical
5. support both site and curated content

### Task 2: Add section selection logic

Create context selection logic that:

1. always includes core documents
2. prioritizes the current page
3. expands to related sections by lexical overlap
4. expands to companion sections using explicit rules for KoNote cross-topic relationships

Example relationship ideas:

1. security -> documentation, getting-started, services
2. outcome measurement -> evidence, features, curated evaluation material
3. bilingual -> faq, documentation, curated bilingual material
4. hosting or deployment -> security, getting-started, services

### Task 3: Refactor the API

Update `chatbot/main.py` so the `/chat` endpoint:

1. accepts current page context
2. selects a targeted context set
3. builds the prompt from selected records
4. returns real sources
5. preserves rate limiting and existing basic protections

Keep the API simple. Do not add streaming unless it is already working cleanly and is required for this task.

### Task 4: Update the frontend

Update `static/js/chatbot.js` to send the new request fields and render returned sources.

Keep the frontend minimal and aligned with the current site.

### Task 5: Expand tests

Add or update tests covering:

1. section parsing
2. current-page prioritization
3. relationship-based context expansion
4. returned sources
5. EN and FR parity for the same question patterns
6. honest behavior when context does not contain the answer

### Task 6: Rebuild and verify

After implementation:

1. run the chatbot tests
2. rebuild the Hugo site
3. verify no site build errors
4. manually test representative English and French questions

## Acceptance Criteria

The work is complete when all of the following are true:

1. The website still builds successfully.
2. The website looks materially the same outside of small chatbot-related additions.
3. The chatbot no longer sends one giant raw corpus by default.
4. The chatbot uses structured selected context.
5. The chatbot returns real sources tied to selected sections or pages.
6. Existing chatbot protections still work.
7. Tests pass.
8. English and French both work.

## Manual Evaluation Set

Compare the redesigned chatbot against the current behavior using at least these questions in both English and French where appropriate:

1. How does KoNote handle privacy and hosting responsibility?
2. Is KoNote a SaaS product?
3. How do outcome tracking and evaluation planning fit together?
4. What parts of KoNote are bilingual?
5. What technical capacity does an agency need?
6. How do security, deployment, and services relate?

Judge the redesign on:

1. factual accuracy
2. completeness
3. ability to connect related issues
4. quality of source links
5. English and French consistency

## Decision Rule

Keep the redesign if it is at least as good as the current implementation on real KoNote questions and better at showing grounded sources.

If answers become too narrow, widen the selected context set before considering embeddings.

## Scope Guardrails

Do not:

1. redesign the website visual system
2. switch away from Railway
3. merge the two services into one
4. add a vector database
5. add a third service
6. broaden this task into general content editing unless required for chatbot grounding

## Deliverables

At the end, provide:

1. a short summary of the grounding redesign
2. the files changed
3. test results
4. build results
5. any remaining risks or follow-up recommendations