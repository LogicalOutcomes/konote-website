---
title: About KoNote
---

# About KoNote

KoNote is an open-source, self-hosted participant outcome management platform built for Canadian social service nonprofits.

## Origin
KoNote grew out of the work of Dr. David Gotlib, an adolescent psychiatrist at St. Joseph's Health Centre in Toronto. He launched KoNote in 2014 as a clinical documentation system. LogicalOutcomes later built a new version using Django, Python, PostgreSQL, and HTMX, with funding from the Ontario Trillium Foundation AI Lab. The evaluation framework comes from LogicalOutcomes' experience across hundreds of evaluations, including the OTF Outcome Measurement Platform, financial coaching work with West Neighbourhood House, and a four-year family violence services evaluation.

## Design Principles
KoNote is built on four structural principles:
1. **Collaborative Practice** — notes written together with participants, not about them. Every progress note has two sides: the participant's perspective and the worker's observations.
2. **Data Sovereignty** — data belongs to the people and communities it describes. Organisations control their own data. Cross-agency data combination is architecturally impossible.
3. **Security by Default** — field-level encryption, role-based access, dual-database audit trail, session timeouts. All protections are on by default and cannot be turned off.
4. **Nonprofit Sustainability** — minimal tech stack (46 Python packages), hosting for under $100 CAD per agency, designed for organisations without dedicated IT teams.

## Technical Stack
- Backend: Django 5.1, Python 3.12
- Database: PostgreSQL 16 (dual databases: operational + audit)
- Frontend: Django templates + HTMX + Pico CSS
- Deployment: Docker Compose (Railway, Azure, OVHcloud, or self-hosted)
- License: MIT (free, open source)

## Target Users
Social service agencies tracking participant outcomes, nonprofits demonstrating program impact, organisations requiring Canadian data residency (PIPEDA compliance), and programs serving up to ~2,000 active participants.

## How KoNote Compares
KoNote differs from commercial case management platforms (which charge per-user fees and host data on vendor servers, often in the US) and from general open source tools (which require significant technical capacity). KoNote is designed for a specific niche: Canadian nonprofits that need outcome tracking built on research, privacy built into the architecture, and costs a five-person agency can sustain. See the Compare page for a detailed comparison table.
