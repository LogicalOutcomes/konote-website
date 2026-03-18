---
title: "Origins"
description: "The history of KoNote: how it grew from clinical work at St. Joseph's Health Centre, through LogicalOutcomes' evaluation experience, to its current form."
hero: true
hero_title: "Origins"
hero_tagline: "How KoNote came to be — the people, projects, and ideas behind it."
---

## Clinical Origins

KoNote grew out of the work of Dr. David Gotlib, an adolescent psychiatrist at St. Joseph's Health Centre in Toronto and former software developer. Around 2011, drawing on both backgrounds, he began prototyping a clinical documentation system at St. Joseph's. With the help of a programmer, he launched KoNote in 2014, and a prototype ran on a psychiatric inpatient unit there for three years.

Having worked with many electronic medical records (EMRs), Gotlib found none of them satisfactory — he described them as "glorified spreadsheets with a Windows front-end" and was actually faster with paper. The core problem was structural: traditional EMRs mirror the paper chart, with serial entries separated by discipline, and do little to help clinicians track the direction of a client's care over time. In mental health and social services, where narrative information matters and where, as Gotlib put it, "you really want to maintain a level of uncertainty," rigid data entry forms are a particularly poor fit.

Existing systems were also not collaborative — they didn't engage clients in their own care or reflect their voices and goals, because they were built for administrators rather than for the people actually filling out the notes.

KoNote's design draws on Dr. Lawrence Weed's problem-oriented medical record from the 1960s, integrating quantitative data (indicators and metrics) into the progress note itself rather than treating measurement as a separate task. The system generates graphs showing client progress across areas, and staff communicate within the software as they maintain a shared record. At St. Joseph's, staff described it as a system that "guides you to chart in a way that you treat people"; a nurse called it "the compass that aids us to map our care." At the Griffin Centre (now Lumenus Community Services), the most technophobic staff member liked it the most.

KoNote was used by a number of social service organizations, including the Griffin Centre. The original version, built on CoffeeScript and Node.js, is available as KoNote Classic on the [LogicalOutcomes GitHub account](https://github.com/LogicalOutcomes).

## How KoNote Came to LogicalOutcomes

LogicalOutcomes and Gotlib found that they shared values about what reporting systems should do — serve the people filling out the forms, not just the people reading the reports. Gotlib joined the LogicalOutcomes Board, and with his involvement and permission, LogicalOutcomes built a new version of KoNote. The new version uses a completely different tech stack (Django, Python, PostgreSQL, HTMX) but retains a very similar user interface, since KoNote Classic's UI components were the ones that had been tested extensively and used over several years by multiple programs. KoNote Classic remains open source on the LogicalOutcomes GitHub.

LogicalOutcomes had long known what it wanted to build, but the cost of custom software development had always been prohibitive. The arrival of AI-assisted development tools — specifically Anthropic's Claude — opened a route to building what had previously been out of reach. With funding from the Ontario Trillium Foundation AI Lab, LogicalOutcomes developed the new KoNote. It is MIT-licensed and currently pre-launch, being explored with three agencies.

## Evaluation Framework

The evaluation approach built into the new KoNote comes from Dr. Gillian Kerr, co-founder of LogicalOutcomes, and Sophie Llewelyn, Director of Evaluation, drawing on their experience with hundreds of evaluations over many years. Three initiatives were particularly formative.

### Ontario Trillium Foundation Outcome Measurement Platform

From 2020 to 2024, LogicalOutcomes provided the Ontario Trillium Foundation's (OTF) Outcome Measurement Platform, working closely with OTF's evaluation team and hundreds of OTF-funded organizations to design data collection tools, processes, and reports. The central challenge was building generic, reusable tools that would work across a wide range of community programs — from language training to settlement services to arts programming — so that each new evaluation didn't require starting from scratch. The standard data collection tools and templates now built into KoNote are a direct result: tested with hundreds of organizations, translated into over a dozen languages, and designed to compress evaluation timelines from months to weeks.

### Financial Counselling and Coaching at West Neighbourhood House

Starting in 2020, with an initial JPMorgan Chase grant, West Neighbourhood House and later Prosper Canada worked with LogicalOutcomes to develop a case management platform for financial empowerment services. The program served graduates from skilled trade apprenticeship programs, self-employed informal economy workers, patients from a local hospital system, and clients of employment and settlement programs.

LogicalOutcomes built the platform on Microsoft PowerApps, tracking not just financial outcomes but wellbeing over time at the individual participant level — stress, sense of belonging, social connectedness, and financial position — longitudinally over months and years through regular check-ins with integrated financial coaches. The wellbeing questions were chosen deliberately because they map onto validated indicators used in social determinants of health research.

This QOL (quality of life) platform's tools and data architecture are among the inputs to the new KoNote, alongside Gotlib's clinical documentation approach and the evaluation tools developed through the OTF and WAGE-funded projects.

### Services to Women Experiencing Family Violence

From 2019 to 2023, LogicalOutcomes conducted a four-year evaluation of services for newcomer and racialized women experiencing domestic or intimate partner violence in the Greater Toronto Area. The project was managed by COSTI Immigrant Services, funded by Women and Gender Equality Canada (WAGE), and involved five community-based agencies (Dinshaw, in preparation).

This project required extended stakeholder consultations across multiple agencies and communities. Data collection tools had to be translated and tested across multiple languages, then piloted with participants before deployment. The evaluation team developed visualizations and reports collaboratively with front-line staff and agency decision-makers. Working across five agencies with different practices and populations reinforced the need for a configurable system rather than a rigid template. The project also required addressing the particular challenges of collecting data in sensitive service contexts — participant safety, informed consent for potentially identifying information, and ensuring that evaluation processes did not create additional burden for women already navigating complex systems. The tools and methods developed through this work are among those now built into KoNote's standard data collection templates.

## What We Learned

These projects — and hundreds of others — shaped how LogicalOutcomes thinks evaluation should work in community services. Across them, we arrived at four conclusions: collect data only to improve services, not for its own sake; use participant feedback continuously to drive better practice; track a small number of process metrics rather than measuring everything; and delay outcome measurement until a client management system is in place. These conclusions, and the research behind them, are now built into KoNote's design — read more on our [Research Foundation](/en/evidence/) page. The [design principles](/en/design-principles/) behind the software reflect them as well.

## Data Standards and Metadata

Every funder, partner, and agency has its own framework, its own taxonomy for outcomes, its own logic model. KoNote does not commit to any single one. Instead, the platform's underlying metadata can be mapped to any of these frameworks — CIDS (Common Impact Data Standard), IRIS+, the SDGs, or whatever conceptual framework a funder requires. Report templates incorporate different taxonomies as part of each template's design, and the mapping is supported by AI, so that metrics and report templates can be developed with minimal human intervention. This is part of the same design philosophy as the rest of the platform: minimize the effort that goes into the reporting process and focus human time on the interactions that are meaningful.

KoNote's data model also borrows structural concepts from the HL7 FHIR data dictionary — specifically care plans, goals, encounters, and episodes of care — without implementing the full FHIR API. These concepts provide a tested structure for organizing longitudinal client data across programs and agencies.

This approach to metadata grew partly out of LogicalOutcomes' earlier work with [DHIS2](https://dhis2.org/), the open-source Health Management Information System used in over 100 countries. Beginning in 2015, LogicalOutcomes adapted DHIS2 for smaller non-profit monitoring and evaluation, developing open-source templates, training curricula, and a "Quick Start" methodology. That work included helping The Nature Conservancy adopt DHIS2 for conservation monitoring in Tanzania, one of the earlier documented uses of the platform outside the health sector. It built deep experience with configurable data collection and with using metadata frameworks to structure aggregate data for system-wide analysis.

---

## Read Next

- **[Research Foundation](/en/evidence/)** — the academic research and practice-derived conclusions behind KoNote's design
- **[Design Principles](/en/design-principles/)** — how these ideas became software architecture

---

*Sources: Canadian Healthcare Technology (November 2016); Kerr, G. & Llewelyn, S., LogicalOutcomes Evaluation Planning Handbook (2024, SSRN 4815131); KoNote GitHub repository.*
