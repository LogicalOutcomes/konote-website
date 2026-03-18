---
title: "Principes de conception"
description: "Les idées derrière la conception de KoNote : pratique collaborative, souveraineté des données, sécurité par défaut et viabilité des organismes à but non lucratif."
hero: true
hero_title: "Principes de conception"
hero_tagline: "Les idées derrière le logiciel."
---

## Notre nom

Le nom KoNote est bilingue par conception. «&nbsp;Note&nbsp;» est le même mot en anglais et en français — un enregistrement, une annotation, un élément de documentation qui a du poids dans les services sociaux. Le «&nbsp;Ko-&nbsp;» est un préfixe stylisé pour «&nbsp;co-&nbsp;» — collaboration, coopération, collectif — un préfixe qui fonctionne de manière identique dans les deux langues. Les francophones le lisent comme *co-note* : des notes collaboratives. Les anglophones perçoivent la même logique. Il y a aussi un écho discret du verbe français *connoter*, suggérant une profondeur et une signification qui vont au-delà de la simple tenue de registres — ce qui convient parfaitement à un travail où la documentation fait partie du service, et non de la paperasse à son sujet.

---

## Introduction

KoNote est fondé sur quatre principes qui façonnent chaque fonctionnalité, chaque paramètre par défaut et chaque décision quant à ce que le logiciel fait ou ne fait pas. Ces principes ne sont pas aspirationnels — ils sont structurels. L'architecture les applique, de sorte qu'ils tiennent même lorsque les personnes qui configurent le système n'y pensent pas.

---

## 1. Pratique collaborative — «&nbsp;Des notes rédigées ensemble, pas sur vous&nbsp;»

Le «&nbsp;Ko&nbsp;» dans KoNote signifie collaboratif. C'est la décision de conception la plus importante du système.

La plupart des logiciels de gestion de cas traitent la documentation comme quelque chose que le personnel fait seul à son bureau après une séance. KoNote la traite comme faisant partie du service lui-même. Chaque note d'évolution a deux côtés : la perspective du participant — ses propres mots, sa réflexion sur la séance, son évaluation de la relation de travail — et les observations de l'intervenant. Les deux sont structurels. Une note sans la voix du participant est incomplète par conception.

Cela importe parce que [la recherche est claire](/fr/donnees-probantes/) : les rétroactions régulières des participants améliorent les résultats jusqu'à 65 % pour les personnes à risque d'abandon. La relation de travail entre le participant et l'intervenant — mesurée du point de vue du participant, pas de l'intervenant — est le meilleur prédicteur du fait qu'un programme aide vraiment. KoNote fait de ces pratiques la voie de moindre résistance plutôt qu'un complément qui nécessite des efforts supplémentaires.

Le portail des participants étend cette philosophie au-delà de la séance. Les participants ne se contentent pas de lire ce que le personnel a écrit sur eux — ils agissent sur leurs propres informations. Ils fixent des objectifs dans leurs propres mots, tiennent un journal entre les séances, évaluent la relation de travail, suggèrent des modifications au programme et demandent des corrections à leurs dossiers. Chaque fonctionnalité du portail passe un test simple : est-ce que cela donne au participant quelque chose de significatif à faire ?

Les suggestions des participants ne sont pas recueillies et oubliées. Elles sont catégorisées en thèmes et présentées dans le tableau de bord de direction, de sorte que les tendances parviennent aux responsables en quelques jours plutôt que d'attendre un sondage annuel de satisfaction que personne ne lit jusqu'au prochain cycle de financement.

Tous les termes du système — descripteurs de progression, étiquettes du tableau de bord, ancrages relationnels — utilisent un cadrage axé sur les forces. La progression est décrite comme «&nbsp;Quelque chose bouge&nbsp;» et «&nbsp;Dans un bon espace&nbsp;», pas des étiquettes de déficit. Ce n'est pas cosmétique. Cela change la façon dont le personnel pense aux personnes qu'il sert et la façon dont les participants se sentent en lisant leurs propres dossiers.

> **Ce que cela signifie en pratique :**
>
> - Un participant consulte ses objectifs dans le portail avant une séance et signale quelque chose à discuter. L'intervenant voit le signalement et se prépare. La séance commence avec un contexte partagé plutôt qu'un démarrage à froid.
> - Une directrice de programme remarque une tendance de suggestions sur les horaires dans trois programmes. Elle ajuste les heures de présence libre et constate que les scores d'alliance s'améliorent le mois suivant.
> - Les organismes choisissent leur propre terminologie — client, participant, membre, ou un mot dans la langue de leur communauté — et le système entier s'adapte. Personne n'est forcé d'utiliser un langage clinique qui ne correspond pas à son travail.

---

## 2. Souveraineté des données — «&nbsp;Vos données vous appartiennent&nbsp;»

KoNote est conçu de sorte que les données appartiennent aux personnes et aux communautés qu'elles décrivent — pas à KoNote, pas à un fournisseur d'hébergement, et pas à un gouvernement disposant de pouvoirs de citation à comparaître qui supplantent le droit canadien.

**Les droits individuels sont intégrés, pas ajoutés après coup.** Les participants peuvent consulter leurs propres dossiers via le portail sans faire de demande d'accès formelle. Ils peuvent demander des corrections — avec des voies informelles et formelles — et le personnel doit répondre dans le délai réglementaire. Si les données d'un participant doivent être effacées, un processus à deux personnes (demande plus approbation) supprime tous les renseignements personnels identifiables tout en préservant les dossiers anonymisés pour les statistiques agrégées. Le consentement n'est pas une case à cocher unique lors de l'accueil. C'est un état continu que les participants peuvent changer à tout moment, chaque changement étant enregistré et appliqué par le système.

**La propriété communautaire est structurelle.** L'architecture de KoNote prend en charge la souveraineté des données autochtones (PCAP — Propriété, Contrôle, Accès et Possession) et la gouvernance des données des communautés noires (EGAP — Engagement, Gouvernance, Accès et Protection). Les données de chaque organisme vivent dans un schéma de base de données isolé. Les requêtes inter-organismes ne sont pas seulement déconseillées — elles sont architecturalement impossibles. Les communautés contrôlent quelles données sont collectées, qui les voit et si elles sont partagées. Lorsque les organismes choisissent de partager, ils publient volontairement des rapports agrégés dépersonnalisés. Aucun organisme n'est contraint de contribuer à un ensemble de données qu'il ne peut pas examiner, corriger ou retirer.

**KoNote ne combine délibérément pas les données individuelles entre les organismes.** Ce n'est pas une fonctionnalité manquante. La combinaison de données inter-organismes permet des schémas de surveillance qui suivent les individus dans chaque service auquel ils accèdent, construisant un profil qu'aucun organisme n'avait l'intention de créer. Quiconque contrôle un ensemble de données combinées dispose d'un pouvoir analytique sur toutes les communautés participantes, sans aucune responsabilité correspondante. KoNote refuse de construire cette infrastructure.

**La souveraineté numérique canadienne est importante.** Toutes les données des participants sont hébergées au Canada (Beauharnois, Québec). KoNote utilise des fournisseurs d'hébergement non soumis à la loi américaine CLOUD Act, qui permet aux tribunaux américains de contraindre la divulgation de données peu importe où elles sont stockées. Le traitement IA des données des participants se fait sur des serveurs auto-hébergés au Canada — les dossiers des participants ne quittent jamais l'infrastructure canadienne pour un traitement IA dans l'infonuage. Et parce que KoNote est à code ouvert avec des formats de données standard, tout organisme peut exporter toutes ses données et changer de fournisseur à tout moment. La portabilité des données est un droit, pas une fonctionnalité premium.

> **Ce que cela signifie en pratique :**
>
> - Un organisme communautaire autochtone configure ses propres champs démographiques, décide ce qui est collecté et contrôle qui peut le voir. Aucun organisme externe ne dicte quelles données d'identité doivent être recueillies.
> - Les rapports utilisent une suppression obligatoire des petits effectifs (les groupes de moins de cinq ne sont jamais affichés) pour éviter la réidentification dans les petites populations — et cette protection ne peut être désactivée par personne, y compris les bailleurs de fonds.
> - Lorsqu'un partenariat de financement prend fin, l'organisme exporte toutes ses données dans une archive autonome et les emporte. Il n'y a pas d'enfermement propriétaire ni de données retenues en otage.

---

## 3. Sécurité par défaut — «&nbsp;Sécurisé même sans équipe TI&nbsp;»

Les organismes à but non lucratif canadiens gèrent des informations très sensibles — notes sur la santé mentale, documentation sur la violence conjugale, dossiers de consommation de substances, statut d'immigration — mais la plupart n'ont pas de personnel dédié à la sécurité informatique. La sécurité de KoNote est donc architecturale, pas configurable. Chaque protection est activée par défaut, ne peut pas être désactivée via l'interface d'administration et échoue de manière fermée plutôt qu'ouverte.

Tous les renseignements personnels identifiables sont chiffrés avant d'atteindre la base de données. Ce n'est pas un paramètre qui peut être activé ou désactivé — c'est ainsi que le système fonctionne. En hébergement partagé, chaque organisme a sa propre clé de chiffrement, de sorte que la clé d'un organisme ne peut pas déchiffrer les données d'un autre. Si la clé de chiffrement est manquante ou mal configurée au démarrage, l'application refuse de démarrer. Un échec visible est toujours préférable à une exposition silencieuse.

Les permissions sont refusées par défaut. Quatre rôles de personnel (Réception, Intervenant direct, Gestionnaire de programme, Direction) sont régis par une matrice de permissions explicite vérifiée à trois niveaux indépendants. Une entrée manquante dans la matrice signifie aucun accès, pas un accès complet. Les blocages d'accès individuels — essentiels dans les contextes de violence conjugale où un membre du personnel ne doit jamais voir le dossier d'un participant spécifique — outrepassent toutes les permissions de rôle et ne peuvent pas expirer automatiquement.

La piste d'audit vit dans une base de données distincte à laquelle l'application ne peut qu'écrire, jamais modifier ni supprimer. Une application compromise ne peut pas altérer ses propres preuves. Les actions critiques pour la sécurité (suppression d'un indicateur de sécurité DV, effacement des données d'un participant, annulation d'une alerte) nécessitent deux personnes pour être complétées, protégeant contre l'erreur humaine et la coercition.

Les sessions expirent après 30 minutes parce que KoNote est utilisé sur des postes de travail partagés dans des refuges et des centres communautaires où un membre du personnel peut s'éloigner d'un écran déverrouillé. Les liens d'exportation expirent après 24 heures et peuvent être révoqués par un administrateur. Les exportations volumineuses déclenchent un délai de 10 minutes avec notification à l'administrateur.

Le test directeur pour chaque décision de sécurité : **«&nbsp;Si un organisme à but non lucratif l'exécute sans expertise TI, peut-il accidentellement le rendre non sécurisé ?&nbsp;»** Si la réponse est oui, la protection n'est pas suffisamment architecturale.

> **Ce que cela signifie en pratique :**
>
> - Un nouvel organisme déploie KoNote avec les paramètres par défaut. Sans rien changer, le chiffrement est actif, les permissions sont appliquées, les sessions expirent et le journal d'audit fonctionne. Il n'y a pas de liste de vérification de sécurité à oublier.
> - Un membre du personnel qui est l'ex-agresseur d'un participant est individuellement bloqué des dossiers de cette personne. Aucun rôle, aucune dérogation et aucune expiration automatique ne peuvent annuler cela — seul un gestionnaire de programme peut lever le blocage.
> - Une exportation de 200 dossiers de participants déclenche une retenue de 10 minutes et une notification à l'administrateur, donnant à l'organisme le temps d'intervenir si l'exportation n'était pas autorisée.

---

## 4. Viabilité des organismes à but non lucratif — «&nbsp;Conçu pour un organisme de 5 personnes, pas une entreprise&nbsp;»

KoNote existe parce que les organismes à but non lucratif qui font un travail communautaire essentiel ne devraient pas avoir besoin de budgets d'entreprise ni d'équipes TI dédiées pour suivre efficacement leurs résultats. Chaque choix architectural est fait avec un opérateur non technique et soucieux des coûts à l'esprit.

La pile technologique est délibérément minimale : HTML rendu côté serveur, pas de cadre JavaScript, pas de pipeline de compilation, pas de dossier node_modules. L'ensemble de la pile de production comprend 46 paquets Python. Comparez cela à une application Web moderne typique avec 500 dépendances ou plus, chacune étant une vulnérabilité de sécurité potentielle et un point de défaillance lors des mises à jour. KoNote n'a pas besoin de React parce que les organismes à but non lucratif n'ont pas besoin d'une application à page unique — ils ont besoin de formulaires qui fonctionnent.

Les coûts d'hébergement sont maintenus bas parce que KoNote utilise un hébergement VPS non géré plutôt que des services infonuagiques d'entreprise, et parce que l'automatisation de guérison automatique rend l'hébergement non géré sûr. Les conteneurs Docker redémarrent d'eux-mêmes. Si un serveur ne répond plus, une surveillance externe déclenche un redémarrage automatique. Un processus en arrière-plan gère les sauvegardes, la surveillance du disque et les rapports de santé. La charge opérationnelle est d'environ 1 à 5 heures par mois par organisme — révision des rapports, application des mises à jour — plutôt que les 10 à 15 heures que cela prendrait sans automatisation.

Les organismes peuvent déployer selon trois modèles selon leur capacité : autogéré (gérez votre propre serveur), service géré (un réseau ou un intermédiaire héberge plusieurs organismes) ou consortium (infrastructure partagée avec rapports agrégés volontaires). Chaque modèle réduit les coûts à mesure que d'autres organismes se joignent. Aucun modèle ne nécessite une équipe TI dédiée.

[L'évaluation n'est pas ajoutée après coup](/fr/fonctionnalites/) à la gestion de cas — c'est la structure sur laquelle tout le reste repose. Un cadre d'évaluation définit ce qui est mesuré et pourquoi. Les métriques ont une provenance complète : de quel instrument elles proviennent, ce que signifient les bandes de notation, quelles exigences des bailleurs de fonds elles satisfont. Les données collectées dans une note d'évolution aujourd'hui apparaissent dans l'analyse automatisée ce soir, dans le tableau de bord de demain et dans le rapport aux bailleurs de fonds du trimestre prochain — sans que personne ne les ressaisisse. Les organismes qui utilisent KoNote et s'alignent sur la Norme commune de données sur l'impact (CIDS) peuvent contribuer à l'apprentissage sectoriel : des données agrégées dépersonnalisées qui aident l'ensemble du secteur à but non lucratif à comprendre ce qui fonctionne, publiées volontairement et contrôlées par chaque communauté.

> **Ce que cela signifie en pratique :**
>
> - Un organisme d'emploi de cinq personnes déploie KoNote pour moins que le coût d'une seule licence logicielle d'un fournisseur commercial de gestion de cas. Lorsqu'il grandit pour servir trois programmes, le coût ne change pas.
> - Un bailleur de fonds demande un rapport trimestriel sur les résultats. La gestionnaire de programme le génère depuis le tableau de bord de rapport en quelques minutes parce que les données ont été collectées dans le cadre de la documentation normale, pas assemblées séparément pour la saison de rapport.
> - Le logiciel est à code ouvert sous la licence MIT. Si un organisme dépasse KoNote, il exporte ses données et passe à autre chose. S'il veut le modifier, il le peut. Il n'y a pas de frais de fournisseur, pas de tarification par utilisateur et pas de pénalités de sortie.
