---
title: À propos de KoNote
---

# À propos de KoNote

KoNote est une plateforme à code source ouvert et auto-hébergée de gestion des résultats des participant·e·s, conçue pour les organismes à but non lucratif canadiens du secteur des services sociaux.

## Origine
KoNote est né des besoins concrets observés dans des organismes comme le St. Joseph's Health Centre (Toronto), le Griffin Centre et le West Neighbourhood House. Ces organismes avaient besoin d'un moyen de suivre systématiquement les résultats des participant·e·s, sans les coûts ni la dépendance envers un fournisseur des logiciels commerciaux de gestion de cas. Le projet a été soutenu par la Fondation Trillium de l'Ontario.

## Philosophie de conception
KoNote repose sur quatre principes fondamentaux :
1. **Les objectifs des participant·e·s d'abord** — le système place l'expérience des participant·e·s au centre, avant la commodité administrative
2. **Souveraineté des données** — les organismes contrôlent leurs propres données sur leurs propres serveurs
3. **Sécurité par défaut** — chiffrement au niveau des champs, contrôle d'accès basé sur les rôles et protection de la vie privée dès la conception
4. **Technologie simple** — HTML rendu côté serveur avec HTMX, pas de cadriciel JavaScript, accessibilité WCAG 2.2 AA

## Pile technologique
- Dorsal : Django 5.1, Python 3.12
- Base de données : PostgreSQL 16 (double base : opérationnelle + audit)
- Frontal : Gabarits Django + HTMX + Pico CSS
- Déploiement : Docker Compose (Railway, Azure, OVHcloud ou auto-hébergé)
- Licence : MIT (gratuit, à code ouvert)

## Public cible
Organismes de services sociaux suivant les résultats des participant·e·s, OBNL démontrant l'impact de leurs programmes, organismes nécessitant la résidence des données au Canada (conformité LPRPDE), et programmes desservant jusqu'à environ 2 000 participant·e·s actif·ve·s.
