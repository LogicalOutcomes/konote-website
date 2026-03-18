---
title: À propos de KoNote
---

# À propos de KoNote

KoNote est une plateforme à code source ouvert et auto-hébergée de gestion des résultats des participant·e·s, conçue pour les organismes à but non lucratif canadiens du secteur des services sociaux.

## Origine
KoNote est né du travail du Dr David Gotlib, psychiatre pour adolescent·e·s au St. Joseph's Health Centre de Toronto. Il a lancé KoNote en 2014 comme système de documentation clinique. LogicalOutcomes a ensuite construit une nouvelle version utilisant Django, Python, PostgreSQL et HTMX, avec un financement du Laboratoire IA de la Fondation Trillium de l'Ontario. Le cadre d'évaluation provient de l'expérience de LogicalOutcomes dans des centaines d'évaluations, notamment la Plateforme de mesure des résultats de la FTO, le travail d'accompagnement financier avec West Neighbourhood House et une évaluation sur quatre ans des services aux femmes vivant de la violence familiale.

## Principes de conception
KoNote repose sur quatre principes structurels :
1. **Pratique collaborative** — les notes sont rédigées avec les participant·e·s, non à leur sujet. Chaque note d'évolution comporte deux volets : la perspective du·de la participant·e et les observations de l'intervenant·e.
2. **Souveraineté des données** — les données appartiennent aux personnes et aux communautés qu'elles décrivent. Les organismes contrôlent leurs propres données. La combinaison de données entre organismes est architecturalement impossible.
3. **Sécurité par défaut** — chiffrement au niveau des champs, accès basé sur les rôles, journal d'audit sur double base de données, délais d'expiration de session. Toutes les protections sont activées par défaut et ne peuvent pas être désactivées.
4. **Durabilité pour les OBNL** — pile technologique minimale (46 paquets Python), hébergement pour moins de 100 $ CAD par organisme, conçu pour les organismes sans équipe TI dédiée.

## Pile technologique
- Dorsal : Django 5.1, Python 3.12
- Base de données : PostgreSQL 16 (double base : opérationnelle + audit)
- Frontal : Gabarits Django + HTMX + Pico CSS
- Déploiement : Docker Compose (Railway, Azure, OVHcloud ou auto-hébergé)
- Licence : MIT (gratuit, à code ouvert)

## Public cible
Organismes de services sociaux suivant les résultats des participant·e·s, OBNL démontrant l'impact de leurs programmes, organismes nécessitant la résidence des données au Canada (conformité LPRPDE), et programmes desservant jusqu'à environ 2 000 participant·e·s actif·ve·s.

## Comment KoNote se compare
KoNote se distingue des plateformes commerciales de gestion de cas (qui facturent par utilisateur·rice et hébergent les données sur des serveurs de fournisseurs, souvent aux États-Unis) et des outils à code ouvert génériques (qui nécessitent une capacité technique importante). KoNote est conçu pour un créneau spécifique : les OBNL canadiens qui ont besoin d'un suivi des résultats fondé sur la recherche, d'une confidentialité intégrée dans l'architecture et de coûts qu'un organisme de cinq personnes peut assumer. Voir la page Comparer pour un tableau de comparaison détaillé.
