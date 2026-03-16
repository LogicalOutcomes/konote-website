---
title: About KoNote
---

# About KoNote

KoNote is an open-source, self-hosted participant outcome management platform built for Canadian social service nonprofits.

## Origin
KoNote emerged from practical needs observed at agencies like St. Joseph's Health Centre (Toronto), Griffin Centre, and West Neighbourhood House. These agencies needed a way to track participant outcomes systematically without the cost and vendor lock-in of commercial case management software. The project was supported by the Ontario Trillium Foundation.

## Design Philosophy
KoNote is built on four core principles:
1. **Participant goals come first** — the system centres participant experience over administrative convenience
2. **Data sovereignty** — organizations control their own data on their own servers
3. **Security by default** — field-level encryption, role-based access, and privacy-by-design
4. **Simple technology** — server-rendered HTML with HTMX, no JavaScript frameworks, WCAG 2.2 AA accessibility

## Technical Stack
- Backend: Django 5.1, Python 3.12
- Database: PostgreSQL 16 (dual databases: operational + audit)
- Frontend: Django templates + HTMX + Pico CSS
- Deployment: Docker Compose (Railway, Azure, OVHcloud, or self-hosted)
- License: MIT (free, open source)

## Target Users
Social service agencies tracking participant outcomes, nonprofits demonstrating program impact, organizations requiring Canadian data residency (PIPEDA compliance), and programs serving up to ~2,000 active participants.
