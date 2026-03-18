---
title: "Design Principles"
description: "The ideas behind KoNote's software design: collaborative practice, data sovereignty, security by default, and nonprofit sustainability."
hero: true
hero_title: "Design Principles"
hero_tagline: "The ideas behind the software."
---

## Our Name

The name KoNote is bilingual by design. "Note" is the same word in English and French — a record, an annotation, a piece of documentation that carries weight in social services. The "Ko-" is a stylized prefix for "co-" — collaboration, cooperation, collectif — a prefix that works identically in both languages. French speakers parse it as *co-note*: collaborative notes. English speakers read the same logic. There is also a quiet echo of the French verb *connoter* (to connote), suggesting depth and significance beyond surface-level record-keeping — fitting for work where documentation is part of the service, not just paperwork about it.

---

## Introduction

KoNote is built on four principles that shape every feature, every default, and every decision about what the software does and does not do. These are not aspirational — they are structural. The architecture enforces them, so they hold even when the people configuring the system are not thinking about them.

---

## 1. Collaborative Practice — "Notes written together, not about you"

The "Ko" in KoNote means collaborative. It is the single most important design decision in the system.

Most case management software treats documentation as something staff do alone at their desk after a session. KoNote treats it as part of the service itself. Every progress note has two sides: the participant's perspective — their own words, their reflection on the session, their rating of the working relationship — and the worker's observations. Both are structural. A note without the participant's voice is incomplete by design.

This matters because [the research is clear](/en/evidence/): routine feedback from participants improves outcomes by as much as 65% for people at risk of dropping out. The working relationship between participant and worker — measured from the participant's perspective, not the worker's — is the strongest predictor of whether a program actually helps. KoNote makes these practices the path of least resistance rather than an add-on that requires extra effort.

The participant portal extends this philosophy beyond the session. Participants do not just read what staff wrote about them — they act on their own information. They set goals in their own words, journal between sessions, rate the working relationship, suggest changes to the program, and request corrections to their records. Every feature in the portal passes a simple test: does this give the participant something meaningful to do?

Participant suggestions are not collected and forgotten. They are categorized into themes and surfaced on the executive dashboard, so patterns reach leadership in days rather than waiting for an annual satisfaction survey that nobody reads until the next funding cycle.

All system language — progress descriptors, dashboard labels, relationship anchors — uses strengths-based framing. Progress is described as "Something's shifting" and "In a good place," not deficit labels. This is not cosmetic. It changes how staff think about the people they serve and how participants feel when they read their own records.

> **What this means in practice:**
>
> - A participant reviews their goals in the portal before a session and flags something to discuss. The worker sees the flag and prepares. The session starts with shared context instead of a cold open.
> - A program director notices a pattern of suggestions about scheduling across three programs. She adjusts drop-in hours and sees alliance ratings improve the following month.
> - Agencies choose their own terminology — client, participant, member, or a word in their community's language — and the entire system adapts. No one is forced into clinical language that does not fit their work.

---

## 2. Data Sovereignty — "Your data belongs to you"

KoNote is designed so that data belongs to the people and communities it describes — not to KoNote, not to a hosting provider, and not to any government with subpoena powers that override Canadian law.

**Individual rights are built in, not bolted on.** Participants can see their own records through the portal without making a formal access request. They can request corrections — with both informal and formal pathways — and staff must respond within the regulatory timeline. If a participant's data needs to be erased, a two-person process (request plus approval) strips all personally identifiable information while preserving anonymized records for aggregate statistics. Consent is not a one-time checkbox at intake. It is an ongoing state that participants can change at any time, with every change recorded and enforced by the system.

**Community ownership is structural.** KoNote's architecture supports Indigenous data sovereignty (OCAP — Ownership, Control, Access, and Possession) and Black data governance (EGAP — Engagement, Governance, Access, and Protection). Each agency's data lives in an isolated database schema. Cross-agency queries are architecturally impossible. Communities control what data is collected, who sees it, and whether any of it is shared. When agencies do choose to share, they publish de-identified aggregate reports voluntarily. No agency is forced to contribute to a dataset it cannot review, correct, or withdraw from.

**KoNote deliberately does not combine individual-level data across agencies.** This is not a missing feature. Cross-agency data combination enables surveillance patterns that track individuals across every service they access, building a profile that no single agency intended to create. Whoever controls a combined dataset has analytical power over all participating communities with none of the accountability. KoNote refuses to build that infrastructure.

**Canadian digital sovereignty matters.** All participant data is hosted in Canada (Beauharnois, Quebec). KoNote uses hosting providers not subject to the US CLOUD Act, which allows US courts to compel disclosure of data regardless of where it is stored. AI processing of participant data happens on self-hosted servers in Canada — participant records never leave Canadian infrastructure for cloud AI processing. And because KoNote is open source with standard data formats, any agency can export all their data and move to a different provider at any time. Data portability is a right, not a premium feature.

> **What this means in practice:**
>
> - An Indigenous community agency configures its own demographic fields, decides what gets collected, and controls who can see it. No external body dictates what identity data must be gathered.
> - Reports use mandatory small-cell suppression (groups of fewer than five are never shown) to prevent re-identification in small populations — and this protection cannot be turned off by anyone, including funders.
> - When a funding partnership ends, the agency exports all their data in a self-contained archive and takes it with them. There is no vendor lock-in and no data held hostage.

---

## 3. Security by Default — "Secure even without an IT team"

Canadian nonprofits handle deeply sensitive information — mental health notes, domestic violence documentation, substance use records, immigration status — but most do not have dedicated IT security staff. KoNote's security is therefore architectural, not configurable. Every protection is on by default, cannot be turned off through the admin interface, and fails closed rather than open.

All personally identifiable information is encrypted before it reaches the database. This is not a setting that can be toggled — it is how the system works. In shared hosting, each agency has its own encryption key, so one agency's key cannot decrypt another's data. If the encryption key is missing or misconfigured on startup, the application refuses to start. A loud failure is always better than a silent exposure.

Permissions default to deny. Four staff roles (Front Desk, Direct Service, Program Manager, Executive) are governed by an explicit permission matrix checked at three independent layers. A missing entry in the matrix means no access, not full access. Individual access blocks — essential for domestic violence scenarios where a staff member must never see a specific participant's records — override all role permissions and cannot expire automatically.

The audit trail lives in a separate database that the application can only write to, never modify or delete. A compromised application cannot alter its own evidence. Safety-critical actions (removing a DV safety flag, erasing a participant's data, cancelling an alert) require two people to complete, protecting against both human error and coercion.

Sessions time out after 30 minutes because KoNote is used on shared workstations in shelters and community centres where a staff member may walk away from an unlocked screen. Export links expire after 24 hours and can be revoked by an administrator. Large exports trigger a 10-minute delay with admin notification.

The guiding test for every security decision: **"If a nonprofit runs this with zero IT expertise, can they accidentally make it insecure?"** If the answer is yes, the protection is not architectural enough.

> **What this means in practice:**
>
> - A new agency deploys KoNote with default settings. Without changing anything, encryption is active, permissions are enforced, sessions time out, and audit logging is running. There is no security setup checklist to forget.
> - A staff member who is a participant's former abuser is individually blocked from that participant's records. No role, no override, and no automatic expiry can reverse this — only a Program Manager can clear the block.
> - An export of 200 participant records triggers a 10-minute hold and an admin notification, giving the agency time to intervene if the export was not authorized.

---

## 4. Nonprofit Sustainability — "Built for a 5-person agency, not an enterprise"

KoNote exists because nonprofits doing critical community work should not need enterprise budgets or dedicated IT teams to track outcomes effectively. Every architectural choice is made with a cost-conscious, non-technical operator in mind.

The tech stack is deliberately minimal: server-rendered HTML, no JavaScript frameworks, no build pipeline, no node_modules folder. The entire production stack is 46 Python packages. Compare that to a typical modern web application with 500 or more dependencies, each one a potential security vulnerability and a point of failure during upgrades. KoNote does not need React because nonprofits do not need a single-page application — they need forms that work.

Hosting costs are kept low because KoNote uses unmanaged VPS hosting rather than enterprise cloud services, and because the self-healing automation makes unmanaged hosting safe. Docker containers restart themselves. If a server goes unresponsive, external monitoring triggers an automatic reboot. A background process handles backups, disk monitoring, and health reports. The operational burden is roughly 1–5 hours per month per agency — reviewing reports, applying updates — rather than the 10–15 hours it would take without automation.

Agencies can deploy in three models depending on their capacity: self-managed (run your own server), managed service (a network or intermediary hosts multiple agencies), or consortium (shared infrastructure with voluntary aggregate reporting). Each model reduces cost as more agencies join. No model requires a dedicated IT team.

[Evaluation is not bolted on](/en/features/) after the case management is built — it is the structure that everything else rests on. An evaluation framework defines what gets measured and why. Metrics carry full provenance: what instrument they come from, what scoring bands mean, which funder requirements they satisfy. Data collected in a progress note today appears in tonight's automated analysis, tomorrow's dashboard, and next quarter's funder report — without anyone re-entering it. Agencies that use KoNote and align to the Common Impact Data Standard (CIDS) can contribute to sector-wide learning: de-identified aggregate data that helps the entire nonprofit sector understand what works, published voluntarily and controlled by each community.

> **What this means in practice:**
>
> - A five-person employment agency deploys KoNote for less than the cost of a single software licence from a commercial case management vendor. When they grow to serve three programs, the cost does not change.
> - A funder asks for a quarterly outcome report. The program manager generates it from the reporting dashboard in minutes because the data was collected as part of normal documentation, not assembled separately for reporting season.
> - The software is open source under the MIT licence. If an agency outgrows KoNote, they export their data and move on. If they want to modify it, they can. There are no vendor fees, no per-user pricing, and no exit penalties.
