---
title: "Origines"
description: "L'histoire de KoNote : comment il a évolué à partir du travail clinique au St. Joseph's Health Centre, à travers l'expérience en évaluation de LogicalOutcomes, jusqu'à sa forme actuelle."
hero: true
hero_title: "Origines"
hero_tagline: "Comment KoNote a vu le jour — les personnes, les projets et les idées qui l'ont inspiré."
---

## Origines cliniques

KoNote est né du travail du Dr David Gotlib, psychiatre pour adolescent·e·s au St. Joseph's Health Centre de Toronto et ancien développeur de logiciels. Vers 2011, s'appuyant sur ces deux formations, il a commencé à développer un prototype de système de documentation clinique au St. Joseph's. Avec l'aide d'un programmeur, il a lancé KoNote en 2014, et un prototype a fonctionné dans une unité psychiatrique de soins aux patient·e·s hospitalisé·e·s pendant trois ans.

Ayant travaillé avec de nombreux dossiers médicaux électroniques (DME), Gotlib n'en trouvait aucun satisfaisant — il les décrivait comme des «&nbsp;chiffriers glorifiés avec une interface Windows&nbsp;» et était en réalité plus rapide avec le papier. Le problème fondamental était structurel : les DME traditionnels reproduisent le dossier papier, avec des entrées en série séparées par discipline, et font peu pour aider les clinicien·nes à suivre l'évolution des soins d'un·e client·e dans le temps. En santé mentale et dans les services sociaux, où l'information narrative importe et où, comme le disait Gotlib, «&nbsp;on veut vraiment maintenir un niveau d'incertitude&nbsp;», les formulaires de saisie de données rigides s'adaptent particulièrement mal.

Les systèmes existants n'étaient pas non plus collaboratifs — ils n'engageaient pas les client·e·s dans leurs propres soins ni ne reflétaient leurs voix et leurs objectifs, parce qu'ils avaient été conçus pour les administrateur·rices plutôt que pour les personnes qui remplissaient réellement les notes.

La conception de KoNote s'inspire du dossier médical orienté par problèmes du Dr Lawrence Weed des années 1960, intégrant des données quantitatives (indicateurs et métriques) dans la note d'évolution elle-même plutôt que de traiter la mesure comme une tâche séparée. Le système génère des graphiques montrant la progression des client·e·s dans différents domaines, et le personnel communique à l'intérieur du logiciel tout en tenant un dossier commun. Au St. Joseph's, le personnel décrivait KoNote comme un système qui «&nbsp;vous guide vers une façon de documenter qui vous aide à traiter les gens&nbsp;» ; une infirmière l'a appelé «&nbsp;la boussole qui nous aide à tracer notre parcours de soins&nbsp;». Au Griffin Centre (maintenant Lumenus Community Services), c'est le membre du personnel le plus réfractaire à la technologie qui l'aimait le plus.

KoNote a été utilisé par plusieurs organisations de services sociaux, notamment le Griffin Centre. La version originale, développée sur CoffeeScript et Node.js, est disponible sous le nom de KoNote Classic sur le [compte GitHub de LogicalOutcomes](https://github.com/LogicalOutcomes).

## Comment KoNote est venu à LogicalOutcomes

LogicalOutcomes et Gotlib ont constaté qu'ils partageaient les mêmes valeurs quant à ce que les systèmes de rapport devraient faire — servir les personnes qui remplissent les formulaires, pas seulement celles qui lisent les rapports. Gotlib a rejoint le conseil d'administration de LogicalOutcomes, et avec sa participation et sa permission, LogicalOutcomes a développé une nouvelle version de KoNote. La nouvelle version utilise une pile technologique complètement différente (Django, Python, PostgreSQL, HTMX) mais conserve une interface utilisateur très similaire, puisque les composants d'interface de KoNote Classic étaient ceux qui avaient été testés de manière approfondie et utilisés pendant plusieurs années par de nombreux programmes. KoNote Classic reste à code ouvert sur le GitHub de LogicalOutcomes.

LogicalOutcomes savait depuis longtemps ce qu'il voulait créer, mais le coût du développement de logiciels personnalisés avait toujours été prohibitif. L'avènement des outils de développement assistés par IA — spécifiquement Claude d'Anthropic — a ouvert une voie vers la construction de ce qui était auparavant hors de portée. Avec un financement du Laboratoire IA de la Fondation Trillium de l'Ontario, LogicalOutcomes a développé le nouveau KoNote. Il est sous licence MIT et est actuellement en phase de pré-lancement, exploré avec trois organismes.

## Cadre d'évaluation

L'approche d'évaluation intégrée dans le nouveau KoNote provient de Dr Gillian Kerr, cofondatrice de LogicalOutcomes, et de Sophie Llewelyn, directrice de l'évaluation, qui s'appuient sur leur expérience de centaines d'évaluations au fil des années. Trois initiatives ont été particulièrement formatrices.

### Plateforme de mesure des résultats de la Fondation Trillium de l'Ontario

De 2020 à 2024, LogicalOutcomes a fourni la Plateforme de mesure des résultats de la Fondation Trillium de l'Ontario (FTO), travaillant en étroite collaboration avec l'équipe d'évaluation de la FTO et des centaines d'organisations financées par la FTO pour concevoir des outils de collecte de données, des processus et des rapports. Le défi central consistait à créer des outils génériques et réutilisables qui fonctionneraient pour un large éventail de programmes communautaires — de la formation linguistique aux services d'établissement en passant par la programmation artistique — afin que chaque nouvelle évaluation ne nécessite pas de repartir de zéro. Les outils et modèles de collecte de données standard maintenant intégrés à KoNote en sont le résultat direct : testés avec des centaines d'organisations, traduits en plus d'une douzaine de langues et conçus pour comprimer les délais d'évaluation de plusieurs mois à quelques semaines.

### Counseling et accompagnement financier à West Neighbourhood House

À partir de 2020, avec une subvention initiale de JPMorgan Chase, West Neighbourhood House et plus tard Prosper Canada ont travaillé avec LogicalOutcomes pour développer une plateforme de gestion de cas pour les services d'autonomisation financière. Le programme servait des diplômé·e·s de programmes d'apprentissage des métiers spécialisés, des travailleur·euses autonomes de l'économie informelle, des patient·e·s d'un réseau hospitalier local et des client·e·s de programmes d'emploi et d'établissement.

LogicalOutcomes a développé la plateforme sur Microsoft PowerApps, suivant non seulement les résultats financiers mais aussi le bien-être dans le temps au niveau individuel des participant·e·s — stress, sentiment d'appartenance, connectivité sociale et situation financière — de façon longitudinale sur des mois et des années grâce à des bilans réguliers avec des coachs financiers intégrés. Les questions sur le bien-être ont été choisies délibérément parce qu'elles correspondent à des indicateurs validés utilisés dans la recherche sur les déterminants sociaux de la santé.

Les outils et l'architecture de données de cette plateforme de qualité de vie (QdV) font partie des éléments qui ont inspiré le nouveau KoNote, aux côtés de l'approche de documentation clinique de Gotlib et des outils d'évaluation développés dans le cadre des projets financés par la FTO et FEGSC.

### Services aux femmes vivant de la violence familiale

De 2019 à 2023, LogicalOutcomes a mené une évaluation sur quatre ans des services destinés aux femmes nouvellement arrivées et racialisées vivant de la violence conjugale ou des partenaires intimes dans la région du Grand Toronto. Le projet était géré par COSTI Immigrant Services, financé par Femmes et Égalité des genres Canada (FEGSC), et impliquait cinq organismes communautaires (Dinshaw, en préparation).

Ce projet a nécessité de longues consultations avec les parties prenantes dans plusieurs organismes et communautés. Les outils de collecte de données devaient être traduits et testés dans plusieurs langues, puis mis à l'essai auprès des participant·e·s avant le déploiement. L'équipe d'évaluation a élaboré des visualisations et des rapports en collaboration avec le personnel de première ligne et les décideur·euses des organismes. Le travail dans cinq organismes ayant des pratiques et des populations différentes a renforcé la nécessité d'un système configurable plutôt que d'un gabarit rigide. Le projet exigeait également de relever les défis particuliers de la collecte de données dans des contextes de services sensibles — sécurité des participant·e·s, consentement éclairé pour les informations potentiellement identifiantes et veiller à ce que les processus d'évaluation n'imposent pas un fardeau supplémentaire aux femmes naviguant déjà dans des systèmes complexes. Les outils et méthodes développés dans ce cadre font partie de ceux qui sont maintenant intégrés dans les modèles de collecte de données standard de KoNote.

## Ce que nous avons appris

Ces projets — et des centaines d'autres — ont façonné la vision de LogicalOutcomes sur la façon dont l'évaluation devrait fonctionner dans les services communautaires. Nous en sommes arrivés à quatre conclusions : ne collecter des données que pour améliorer les services, et non pour leur propre fin ; utiliser les rétroactions des participant·e·s en continu pour améliorer les pratiques ; suivre un petit nombre de métriques de processus plutôt que de tout mesurer ; et retarder la mesure des résultats jusqu'à ce qu'un système de gestion de cas soit en place. Ces conclusions, et les données probantes qui les soutiennent, sont maintenant intégrées dans la conception de KoNote — consultez notre page [Fondements de la recherche](/fr/donnees-probantes/) pour en savoir plus. Les [principes de conception](/fr/principes-de-conception/) du logiciel les reflètent également.

## Normes de données et métadonnées

Chaque bailleur de fonds, partenaire et organisme a son propre cadre, sa propre taxonomie des résultats, son propre modèle logique. KoNote ne s'engage pas envers un seul d'entre eux. Au lieu de cela, les métadonnées sous-jacentes de la plateforme peuvent être cartographiées vers n'importe lequel de ces cadres — CIDS (Norme commune de données sur l'impact), IRIS+, les ODD, ou tout cadre conceptuel qu'un bailleur de fonds exige. Les modèles de rapport intègrent différentes taxonomies dans la conception de chaque modèle, et la cartographie est soutenue par l'IA, de sorte que les métriques et les modèles de rapport peuvent être développés avec une intervention humaine minimale. Cela fait partie du même principe de conception que le reste de la plateforme : minimiser les efforts consacrés au processus de rapport et concentrer le temps humain sur les interactions qui ont du sens.

Le modèle de données de KoNote emprunte également des concepts structurels au dictionnaire de données HL7 FHIR — spécifiquement les plans de soins, les objectifs, les rencontres et les épisodes de soins — sans pour autant mettre en œuvre l'API FHIR complète. Ces concepts fournissent une structure éprouvée pour organiser les données longitudinales des client·e·s dans les programmes et les organismes.

Cette approche des métadonnées est issue en partie du travail antérieur de LogicalOutcomes avec [DHIS2](https://dhis2.org/), le Système d'information pour la gestion de la santé à code ouvert utilisé dans plus de 100 pays. À partir de 2015, LogicalOutcomes a adapté DHIS2 pour la surveillance et l'évaluation de plus petits organismes à but non lucratif, développant des gabarits à code ouvert, des programmes de formation et une méthodologie de «&nbsp;démarrage rapide&nbsp;». Ce travail comprenait l'aide à l'adoption de DHIS2 par The Nature Conservancy pour le suivi de la conservation en Tanzanie, l'une des premières utilisations documentées de la plateforme en dehors du secteur de la santé. Ce travail a permis d'acquérir une profonde expérience en matière de collecte de données configurable et d'utilisation de cadres de métadonnées pour structurer les données agrégées en vue d'une analyse à l'échelle du système.

---

## Lire la suite

- **[Fondements de la recherche](/fr/donnees-probantes/)** — les données probantes et les conclusions pratiques derrière la conception de KoNote
- **[Principes de conception](/fr/principes-de-conception/)** — comment ces idées sont devenues une architecture logicielle

---

*Sources : Canadian Healthcare Technology (novembre 2016) ; Kerr, G. et Llewelyn, S., LogicalOutcomes Evaluation Planning Handbook (2024, SSRN 4815131) ; Dépôt GitHub de KoNote.*
