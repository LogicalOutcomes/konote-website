---
title: "Foire aux questions"
description: "Questions fréquentes sur KoNote : licences, soutien, limites et réponses honnêtes sur ce à quoi vous pouvez vous attendre."
layout: "wide"
hero: true
hero_title: "Foire aux questions"
hero_tagline: "Des réponses honnêtes aux questions courantes sur KoNote."
---

<section>
<div class="container content-width">

<h2>Licence et coûts</h2>

<div class="faq-item is-open">
<button class="faq-question" aria-expanded="true">
        KoNote est-il vraiment gratuit ?
</button>
<div class="faq-answer">
<p>
          Oui. KoNote est publié sous la licence MIT, ce qui signifie que vous pouvez l'utiliser,
          le modifier et le distribuer librement — y compris à des fins commerciales.
          Il n'y a pas de frais de licence, pas de tarification par utilisateur·rice, pas de niveaux premium.
</p>
<p>
          Vous aurez des frais d'hébergement (les serveurs qui exécutent KoNote), mais ceux-ci
          vont à votre fournisseur d'hébergement, pas à nous. Les frais d'hébergement typiques varient
          entre 45 et 150 $ CAD par mois selon la plateforme choisie.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Quel est le piège ?
</button>
<div class="faq-answer">
<p>
          Il n'y a pas de piège, mais il y a des compromis :
</p>
<ul>
<li>Vous êtes responsable du déploiement, de la sécurité et de la maintenance</li>
<li>Il n'y a pas de soutien du fournisseur — seulement une aide communautaire via GitHub</li>
<li>Vous avez besoin de capacité technique (ou d'un partenaire qui en dispose)</li>
</ul>
<p>
          Si vous souhaitez une solution entièrement gérée où quelqu'un d'autre s'occupe de tout,
          KoNote n'est pas cette solution. Si vous êtes à l'aise avec l'auto-hébergement et souhaitez
          un contrôle total sur vos données, KoNote vous convient bien.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Pouvons-nous modifier KoNote selon nos besoins ?
</button>
<div class="faq-answer">
<p>
          Oui. La licence MIT autorise explicitement la modification. Vous pouvez modifier
          le code, ajouter des fonctionnalités ou l'adapter selon vos besoins. Vous pouvez même
          redistribuer votre version modifiée.
</p>
<p>
          Si vous apportez des améliorations qui profiteraient à d'autres, nous accueillerions favorablement
          des contributions au projet principal — mais c'est optionnel.
</p>
</div>
</div>

<h2 class="mt-8">Soutien et mises à jour</h2>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Quel type de soutien est disponible ?
</button>
<div class="faq-answer">
<p>
<strong>Soutien communautaire :</strong> Vous pouvez poser des questions et signaler des problèmes
          sur <a href="https://github.com/LogicalOutcomes/konote/issues">GitHub</a>.
          Il n'y a pas de délais de réponse garantis — cela dépend de qui est disponible
          et si quelqu'un connaît la réponse.
</p>
<p>
<strong>Soutien professionnel :</strong> Si vous avez besoin d'une aide garantie,
          nous offrons des <a href="/fr/services/">services professionnels</a> incluant
          l'aide à la mise en œuvre et la formation.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Comment fonctionnent les mises à jour ?
</button>
<div class="faq-answer">
<p>
          Les nouvelles versions sont publiées sur GitHub. Vous êtes responsable de surveiller
          les nouvelles versions et d'appliquer les mises à jour à votre déploiement. Le guide de déploiement
          comprend des instructions pour la mise à jour.
</p>
<p>
          Les mises à jour ne sont pas automatiques — vous contrôlez quand les appliquer. Cela signifie
          que vous pouvez les tester avant de les appliquer, mais cela signifie aussi que vous devez
          maintenir activement votre installation à jour.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Que se passe-t-il si le projet est abandonné ?
</button>
<div class="faq-answer">
<p>
          La licence MIT signifie que le code vous appartient pour toujours. Si le développement actif
          s'arrête, vous pouvez :
</p>
<ul>
<li>Continuer à utiliser votre version actuelle indéfiniment</li>
<li>Créer une fourche du projet et le maintenir vous-même</li>
<li>Trouver quelqu'un d'autre pour maintenir une fourche</li>
</ul>
<p>
          Vous n'êtes pas lié à une relation avec un fournisseur qui pourrait disparaître.
</p>
</div>
</div>

<h2 class="mt-8">Questions techniques</h2>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Combien de participant·e·s KoNote peut-il gérer ?
</button>
<div class="faq-answer">
<p>
          KoNote a été testé avec jusqu'à environ 2 000 participant·e·s actif·ves.
</p>
<p>
          La principale limite est la recherche chiffrée : parce que les RPI sont chiffrés,
          la recherche de participant·e·s charge les participant·e·s accessibles en mémoire et filtre en Python.
          Cela fonctionne bien à plus petite échelle, mais peut ralentir avec des bases de participant·e·s plus importantes.
</p>
<p>
          Si vous avez beaucoup plus de participant·e·s, nous recommandons des tests de performance
          avant de vous engager avec KoNote.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Pouvons-nous migrer des données d'un autre système ?
</button>
<div class="faq-answer">
<p>
          Il n'y a pas d'outils de migration intégrés. La migration de données nécessite :
</p>
<ul>
<li>L'exportation des données de votre système actuel</li>
<li>La correspondance des champs avec le modèle de données de KoNote</li>
<li>La rédaction d'un script pour importer les données</li>
</ul>
<p>
          C'est techniquement possible, mais nécessite un travail de développement spécifique
          à votre système source. Si vous avez besoin d'aide à ce sujet, mentionnez-le lors de votre
          prise de contact au sujet des <a href="/fr/services/">services professionnels</a>.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        KoNote fonctionne-t-il hors connexion ?
</button>
<div class="faq-answer">
<p>
          L'interface Web de KoNote nécessite une connexion Internet pour une fonctionnalité complète.
          Un service worker fournit un mode hors connexion élégant —
          en cas de perte de connectivité, vous verrez un message convivial et l'application
          reprend automatiquement dès que vous êtes de nouveau en ligne.
</p>
<p>
          Pour le travail sur le terrain dans des endroits sans Internet, KoNote s'intègre avec
          ODK Central pour la collecte de données mobiles hors connexion. Le personnel collecte
          des données sur des appareils Android et les synchronise avec KoNote dès que la connectivité est
          disponible. Les niveaux de protection des RPI contrôlent quels identifiants sont envoyés aux
          appareils sur le terrain, et un protocole de perte d'appareil protège les données si un appareil
          est perdu ou volé.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Pouvons-nous intégrer KoNote avec d'autres systèmes ?
</button>
<div class="faq-answer">
<p>
          KoNote ne dispose pas d'une API publique, donc l'intégration directe n'est pas simple.
</p>
<p>
          Les options comprennent :
</p>
<ul>
<li>Exportation/importation CSV pour le transfert de données par lots</li>
<li>Développement personnalisé pour ajouter des points d'accès API (Django le rend possible)</li>
<li>Accès direct à la base de données (avec précaution et compréhension du schéma)</li>
</ul>
</div>
</div>

<h2 class="mt-8">Fonctionnalités</h2>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Comment fonctionnent les sondages ?
</button>
<div class="faq-answer">
<p>
          KoNote comprend un système de sondage complet pour collecter des rétroactions structurées.
          Les administrateur·rices créent des sondages avec six types de questions, une logique conditionnelle et
          une notation optionnelle par section. Les sondages peuvent être distribués de trois façons :
</p>
<ul>
<li><strong>Portail des participant·e·s :</strong> Les sondages assignés apparaissent dans le
            tableau de bord du·de la participant·e. Les réponses se sauvegardent automatiquement en cours de saisie.</li>
<li><strong>Liens publics partageables :</strong> N'importe qui peut compléter un sondage
            via une URL — aucune connexion requise. Utile pour les rétroactions communautaires ou
            la présélection avant l'admission.</li>
<li><strong>Saisie de données par le personnel :</strong> Le personnel saisit les réponses au nom
            d'un·e participant·e lors d'une séance.</li>
</ul>
<p>
          Les sondages peuvent être assignés manuellement ou automatiquement à l'aide de règles de déclenchement
          basées sur des événements, l'inscription à un programme, des intervalles de temps ou les
          caractéristiques du·de la participant·e. Vous pouvez importer des instruments existants (comme le PHQ-9 ou le SPDAT)
          depuis des fichiers CSV.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Qu'est-ce que le portail des participant·e·s ?
</button>
<div class="faq-answer">
<p>
          Le portail des participant·e·s est un site Web libre-service optionnel où
          les participant·e·s peuvent :
</p>
<ul>
<li>Consulter leurs plans de résultats et graphiques de progression</li>
<li>Remplir des sondages assignés</li>
<li>Rédiger des entrées de journal privées</li>
<li>Envoyer des messages à leur intervenant·e assigné·e</li>
<li>Demander des corrections à leurs dossiers</li>
<li>Accéder aux ressources partagées et aux documents du programme</li>
</ul>
<p>
          Le personnel invite les participant·e·s via un lien sécurisé avec un code verbal optionnel
          pour la vérification de l'identité. Les participant·e·s créent leurs propres identifiants
          et passent par un flux de consentement avant d'accéder au portail. Le portail
          prend en charge l'authentification multifacteur (application TOTP ou codes par courriel) et
          le personnel peut révoquer l'accès ou réinitialiser l'AMF à tout moment.
</p>
<p>
          Le portail est désactivé par défaut. Activez-le dans les paramètres des fonctionnalités
          lorsque votre organisme est prêt à l'offrir.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Comment fonctionne l'exportation de données ?
</button>
<div class="faq-answer">
<p>
          KoNote offre deux niveaux d'exportation de données :
</p>
<ul>
<li><strong>Exportation individuelle du·de la participant·e :</strong> Depuis le profil d'un·e participant·e,
            le personnel peut exporter ses données en format PDF, CSV ou JSON.
            Les téléchargements utilisent des liens sécurisés à durée limitée qui expirent après 24 heures.
            Les exportations volumineuses déclenchent une notification à l'administrateur·rice et un bref délai de supervision.</li>
<li><strong>Exportation de désaffectation à l'échelle de l'organisme :</strong> Une commande de gestion
            exporte toutes les données de l'organisme en format chiffré AES-256-GCM avec une phrase de passe Diceware.
            Ceci est conçu pour la désaffectation de l'organisme ou la migration de données —
            pas pour les rapports courants.</li>
</ul>
<p>
          Toutes les exportations sont entièrement auditées. Les administrateur·rices peuvent révoquer les liens de téléchargement et
          les permissions sont revérifiées au moment du téléchargement pour éviter les accès périmés.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Qu'est-ce que le mode démonstration ?
</button>
<div class="faq-answer">
<p>
          Le mode démonstration fournit des comptes de formation préconfigurés avec des données exemples réalistes
          pour que le personnel puisse explorer KoNote sans affecter les vrais dossiers de participant·e·s.
          Les principales mesures de protection comprennent :
</p>
<ul>
<li>Les dossiers de démonstration sont exclus de tous les rapports, exportations et tableaux de bord</li>
<li>Les comptes d'administrateur·rice de démonstration sont limités à la consultation des paramètres de l'organisme</li>
<li>Une bannière persistante de mode formation apparaît sur chaque page</li>
<li>Les boutons de connexion de démonstration sont visuellement séparés du vrai formulaire de connexion
            sous une étiquette «&nbsp;Comptes de formation&nbsp;»</li>
<li>Les événements de connexion de démonstration sont audités séparément de l'activité en production</li>
</ul>
<p>
          Les données de démonstration peuvent être régénérées à tout moment pour réinitialiser l'environnement de formation.
</p>
</div>
</div>

<h2 class="mt-8">Questions organisationnelles</h2>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Pourquoi KoNote n'est-il pas offert en mode SaaS ?
</button>
<div class="faq-answer">
<p>
          Les données des participant·e·s sont sensibles. De nombreux organismes à but non lucratif ont besoin d'un contrôle total sur
          l'emplacement de ces données — pour la conformité réglementaire, les exigences des bailleurs de fonds ou
          la politique organisationnelle.
</p>
<p>
          Un modèle auto-hébergé signifie :
</p>
<ul>
<li>Vous choisissez où les données sont stockées (serveurs canadiens si nécessaire)</li>
<li>Vous ne dépendez pas de la continuité des activités d'un fournisseur</li>
<li>Vous pouvez inspecter exactement ce que fait le logiciel</li>
<li>Aucun risque qu'un fournisseur augmente les prix ou modifie les conditions</li>
</ul>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        KoNote convient-il aux milieux cliniques ?
</button>
<div class="faq-answer">
<p>
          KoNote est conçu pour le suivi des résultats dans les services sociaux, pas pour la
          documentation clinique. Il lui manque :
</p>
<ul>
<li>Des outils d'évaluation clinique normalisés</li>
<li>Des fonctionnalités de planification du traitement</li>
<li>Le suivi des prescriptions ou des médicaments</li>
<li>Des fonctionnalités de conformité spécifiques aux soins de santé (HIPAA, etc.)</li>
</ul>
<p>
          Si vous avez besoin d'un DME/DSE clinique, KoNote n'est pas le bon outil.
          Si vous devez suivre les résultats des participant·e·s en parallèle avec le travail clinique,
          KoNote pourrait compléter (mais non remplacer) votre système clinique.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Plusieurs organisations peuvent-elles partager une même instance de KoNote ?
</button>
<div class="faq-answer">
<p>
          Oui. KoNote prend en charge l'hébergement multi-organismes, où plusieurs organisations
          partagent un seul serveur tout en maintenant une stricte séparation des données. Chaque
          organisme dispose de son propre espace de stockage de données et de sa propre clé de chiffrement,
          avec une configuration indépendante pour la terminologie, les fonctionnalités et les programmes.
</p>
<p>
          Ceci est conçu pour les organismes faîtiers, les consortiums ou les réseaux régionaux
          qui souhaitent réduire les coûts d'hébergement sans compromettre
          la confidentialité des données. Les données de chaque organisme restent entièrement isolées des
          autres organismes sur le même serveur. Les coûts typiques par organisme passent
          de 35&ndash;100&nbsp;$/mois (autonome) à 4&ndash;10&nbsp;$/mois (partagé).
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        Quelles langues KoNote prend-il en charge ?
</button>
<div class="faq-answer">
<p>
          KoNote offre une prise en charge bilingue complète en anglais et en français, selon les
          conventions de canada.ca. Les utilisateur·rices peuvent changer de langue d'un seul clic et tous
          les termes, étiquettes et textes du système s'affichent dans la langue choisie.
</p>
<p>
          Les organismes peuvent personnaliser toute la terminologie dans les deux langues pour correspondre
          à leur vocabulaire préféré. L'internationalisation complète vers d'autres langues au-delà
          de l'anglais et du français nécessiterait un travail de développement.
</p>
</div>
</div>

<div class="faq-item">
<button class="faq-question" aria-expanded="false">
        KoNote utilise-t-il l'IA ?
</button>
<div class="faq-answer">
<p>
          KoNote comprend des fonctionnalités optionnelles assistées par IA qui aident le personnel dans
          la rédaction d'objectifs, la documentation et l'analyse :
</p>
<ul>
<li>Rédaction d'objectifs assistée par IA — formulation d'objectifs en langage naturel avec validation fondée sur la recherche</li>
<li>Suggestions de métriques basées sur les descriptions des cibles de résultats</li>
<li>Amélioration de la formulation des objectifs</li>
<li>Aide à la structure des notes d'évolution</li>
<li>Thèmes de suggestions — regroupement des rétroactions qualitatives en tendances</li>
<li>Génération de récits pour les bailleurs de fonds à partir de données agrégées</li>
<li>Perspectives sur les résultats — résumés de programmes générés par l'IA</li>
</ul>
<p>
          Les fonctionnalités IA utilisent un commutateur à deux niveaux : mode outils uniquement (sans données sur les participant·e·s,
          activé par défaut) et mode analyse dépersonnalisée (données des participant·e·s avec
          identifiants supprimés, désactivé par défaut). Aucune information d'identification des participant·e·s
          n'est jamais envoyée au service d'IA. Les deux niveaux peuvent être entièrement désactivés
          si votre organisme préfère ne pas utiliser l'IA.
</p>
</div>
</div>

</div>
</section>

<section class="alt-bg">
<div class="container text-center">
<h2>Vous avez encore des questions ?</h2>
<p class="text-muted mb-8">
      Consultez la documentation ou contactez-nous sur GitHub.
</p>
<div class="btn-group" style="justify-content: center;">
<a href="/fr/documentation/" class="btn btn-primary">Documentation</a>
<a href="https://github.com/LogicalOutcomes/konote/issues" class="btn btn-secondary">Poser une question sur GitHub</a>
</div>
</div>
</section>

<script>
  document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
      const item = button.parentElement;
      const isOpen = item.classList.toggle('is-open');
      button.setAttribute('aria-expanded', isOpen);
    });
  });
</script>
