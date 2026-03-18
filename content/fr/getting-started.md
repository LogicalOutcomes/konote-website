---
title: "Premiers pas"
description: "Comment évaluer et déployer KoNote. Options de déploiement, exigences et guide étape par étape."
layout: "wide"
hero: true
hero_title: "Premiers pas"
hero_tagline: "Comment évaluer KoNote et décider s'il convient à votre organisme."
---

<section>
<div class="container content-width">
<h2>KoNote vous convient-il&nbsp;?</h2>
<p>
      Avant d'investir du temps dans l'évaluation, assurez-vous que KoNote représente une option
      raisonnablement adaptée à votre organisme. Répondez à ces questions honnêtement :
</p>

<div class="card">
<h3>Capacité technique</h3>
<p><strong>Avez-vous quelqu'un qui peut&nbsp;:</strong></p>
<ul>
<li>Déployer une application basée sur Docker vers une plateforme infonuagique&nbsp;?</li>
<li>Configurer des variables d'environnement et gérer les secrets&nbsp;?</li>
<li>Mettre en place et maintenir des sauvegardes régulières de la base de données&nbsp;?</li>
<li>Appliquer les mises à jour du logiciel lors de la sortie de nouvelles versions&nbsp;?</li>
<li>Résoudre des problèmes à l'aide de la documentation et des journaux système&nbsp;?</li>
</ul>
<p>
        Si vous répondez oui à la plupart de ces questions, vous avez la capacité technique suffisante.
        Si non, vous aurez besoin d'un partenaire TI ou de nos <a href="/fr/services/">services professionnels</a>.
</p>
</div>

<div class="card">
<h3>Adéquation organisationnelle</h3>
<p><strong>Votre organisme&nbsp;:</strong></p>
<ul>
<li>Suit-il les résultats des participants comme fonction principale&nbsp;?</li>
<li>Doit-il démontrer l'impact des programmes aux bailleurs de fonds&nbsp;?</li>
<li>Sert-il moins d'environ 2&nbsp;000 participants actifs&nbsp;?</li>
<li>Nécessite-t-il un contrôle sur l'emplacement de stockage des données des participants&nbsp;?</li>
<li>Valorise-t-il le logiciel à code ouvert et l'évitement de la dépendance envers un fournisseur&nbsp;?</li>
</ul>
<p>
        Si vous répondez oui à la plupart de ces questions, KoNote est probablement bien adapté.
        Si non, une solution SaaS commerciale pourrait mieux vous convenir.
</p>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container content-width">
<h2>Parcours d'évaluation</h2>
<p>
      Nous recommandons cette séquence pour évaluer KoNote :
</p>

<div class="card">
<h3>Étape 1 : Lire la documentation</h3>
<p>
        Commencez par la <a href="/fr/documentation/">documentation</a> pour comprendre
        ce que fait KoNote. Le guide de l'utilisateur vous montrera les flux de travail quotidiens ; la
        documentation technique aidera votre équipe TI à comprendre l'architecture.
</p>
<p class="text-muted">Temps estimé : 1–2 heures</p>
</div>

<div class="card">
<h3>Étape 2 : Essayer une démonstration</h3>
<p>
<strong>Démonstration en ligne (aucune configuration requise) :</strong>
<a href="/fr/demo/">Essayez le formulaire d'inscription en direct</a> pour voir comment
        les participants s'inscrivent aux programmes dans KoNote. Cela fonctionne sur une vraie instance
        — aucune installation requise.
</p>
<p>
<strong>Démonstration locale (nécessite Docker) :</strong>
        Si vous souhaitez explorer l'interface complète du personnel, lancez une démonstration locale
        avec des données exemples :
</p>
<pre><code>docker-compose -f docker-compose.demo.yml up</code></pre>
<p class="text-muted">Démonstration en ligne : 2 minutes. Démonstration locale : 30–45 minutes (installation Docker comprise).</p>
</div>

<div class="card">
<h3>Étape 3 : Choisir une plateforme de déploiement</h3>
<p>
        Si la démonstration semble prometteuse, décidez où vous hébergerez KoNote.
        Consultez les <a href="#options-de-deploiement">options de déploiement</a> ci-dessous.
</p>
<p class="text-muted">Temps estimé : Recherche et prise de décision</p>
</div>

<div class="card">
<h3>Étape 4 : Déployer et configurer</h3>
<p>
        Suivez le guide de déploiement pour la plateforme choisie. Ensuite, configurez
        votre organisme : mettez en place des programmes, créez des comptes utilisateur, personnalisez la terminologie.
</p>
<p class="text-muted">Temps estimé : 2–4 heures pour le déploiement, plus la configuration</p>
</div>

<div class="card">
<h3>Étape 5 : Pilote avec de vrais utilisateurs</h3>
<p>
        Commencez avec un petit groupe pilote avant de déployer à l'échelle de l'organisme.
        Recueillez des rétroactions, affinez votre configuration et élaborez une documentation interne.
</p>
</div>
</div>
</section>

<section id="options-de-deploiement">
<div class="container">
<h2>Options de déploiement</h2>
<p class="text-muted mb-8">
      KoNote fonctionne partout où Docker fonctionne. Voici les options les plus courantes,
      avec une évaluation honnête de chacune.
</p>

<div class="card-grid">
<div class="card">
<h3>Railway</h3>
<p><strong>Déploiement le plus simple</strong></p>
<p>
          Déploiement en un clic depuis GitHub. Bases de données PostgreSQL gérées.
          HTTPS automatique. Bien adapté aux organismes sans personnel TI dédié.
</p>
<ul>
<li><strong>Coût :</strong> Environ 45–50&nbsp;$/mois (CAD)</li>
<li><strong>Difficulté :</strong> Faible</li>
<li><strong>Emplacement des données :</strong> États-Unis (infrastructure de Railway)</li>
</ul>
<p class="text-muted">
          Idéal pour : Les petites et moyennes organisations qui veulent la simplicité.
</p>
</div>

<div class="card">
<h3>Microsoft Azure</h3>
<p><strong>Résidence canadienne des données</strong></p>
<p>
          Déployez sur Azure Container Instances avec Azure Database for PostgreSQL.
          Les données peuvent rester dans des régions canadiennes. Configuration plus complexe.
</p>
<ul>
<li><strong>Coût :</strong> Variable (généralement 50–150&nbsp;$/mois CAD)</li>
<li><strong>Difficulté :</strong> Moyen à élevé</li>
<li><strong>Emplacement des données :</strong> Votre choix (Canada Centre disponible)</li>
</ul>
<p class="text-muted">
          Idéal pour : Les organisations nécessitant la résidence canadienne des données.
</p>
</div>

<div class="card">
<h3>Elestio</h3>
<p><strong>Hébergement Docker géré</strong></p>
<p>
          Hébergement Docker Compose avec infrastructure gérée.
          Juste milieu entre la simplicité de Railway et l'auto-hébergement complet.
</p>
<ul>
<li><strong>Coût :</strong> Variable selon le plan</li>
<li><strong>Difficulté :</strong> Moyen</li>
<li><strong>Emplacement des données :</strong> Plusieurs options</li>
</ul>
<p class="text-muted">
          Idéal pour : Les organisations à l'aise avec Docker mais pas avec l'infrastructure.
</p>
</div>

<div class="card">
<h3>OVHcloud (Beauharnois, QC)</h3>
<p><strong>Résidence canadienne des données</strong></p>
<p>
          Déployez dans le centre de données OVHcloud à Beauharnois, au Québec.
          Docker Compose avec proxy inverse Caddy et auto-guérison automatisée.
</p>
<ul>
<li><strong>Coût :</strong> Variable selon le plan VPS</li>
<li><strong>Difficulté :</strong> Moyen</li>
<li><strong>Emplacement des données :</strong> Canada (Québec)</li>
</ul>
<p class="text-muted">
          Idéal pour : Les organisations nécessitant la résidence canadienne des données à moindre coût qu'Azure.
</p>
</div>

<div class="card">
<h3>Auto-hébergé</h3>
<p><strong>Contrôle total</strong></p>
<p>
          Exécutez Docker Compose sur vos propres serveurs ou VPS. Contrôle complet
          sur tout. Nécessite des connaissances en DevOps.
</p>
<ul>
<li><strong>Coût :</strong> Coûts d'infrastructure uniquement</li>
<li><strong>Difficulté :</strong> Élevé</li>
<li><strong>Emplacement des données :</strong> Votre choix</li>
</ul>
<p class="text-muted">
          Idéal pour : Les organisations disposant de personnel TI dédié et d'une infrastructure propre.
</p>
</div>
</div>

<div class="notice notice-warning">
<p class="notice-title">Considérations sur la résidence des données</p>
<p>
        Si votre organisme exige que les données des participants restent au Canada,
        l'infrastructure américaine de Railway peut ne pas convenir.
        Envisagez OVHcloud Beauharnois, Azure (région Canada Centre)
        ou l'auto-hébergement dans un centre de données canadien.
</p>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container content-width">
<h2>Ce dont vous aurez besoin</h2>

<div class="card">
<h3>Pour la démonstration (test local)</h3>
<ul>
<li>Docker Desktop installé sur votre ordinateur</li>
<li>Accès à la ligne de commande ou au terminal</li>
<li>Environ 2&nbsp;Go d'espace disque libre</li>
<li>30–45 minutes</li>
</ul>
</div>

<div class="card">
<h3>Pour le déploiement en production</h3>
<ul>
<li>Un compte sur une plateforme d'hébergement (Railway, Azure, etc.)</li>
<li>Une clé de chiffrement sécurisée (que vous générez)</li>
<li>Un locataire Azure AD (si vous utilisez l'authentification unique) ou une authentification locale</li>
<li>Une stratégie de sauvegarde (vous en êtes responsable)</li>
<li>Quelqu'un pour gérer les opérations courantes</li>
</ul>
</div>

<div class="disclaimer">
<p class="disclaimer-title">Vos responsabilités</p>
<p>
        Une fois déployé, vous êtes responsable de :
</p>
<ul>
<li><strong>Sécurité :</strong> Protéger votre clé de chiffrement, configurer HTTPS, gérer l'accès des utilisateurs</li>
<li><strong>Sauvegardes :</strong> Sauvegardes régulières de la base de données et tests de restauration</li>
<li><strong>Mises à jour :</strong> Application des nouvelles versions de KoNote lors de leur sortie</li>
<li><strong>Formation :</strong> Former votre personnel à utiliser le système</li>
<li><strong>Soutien :</strong> Résolution des problèmes (soutien communautaire via GitHub)</li>
</ul>
<p>
        Si cela semble dépasser les capacités de votre équipe,
        envisagez nos <a href="/fr/services/">services professionnels</a>.
</p>
</div>
</div>
</section>

<section>
<div class="container text-center">
<h2>Prêt à continuer&nbsp;?</h2>
<p class="text-muted mb-8">
      Le guide de déploiement complet contient des instructions étape par étape pour chaque plateforme.
</p>
<div class="btn-group" style="justify-content: center;">
<a href="/fr/documentation/" class="btn btn-primary">Voir la documentation</a>
<a href="/fr/services/" class="btn btn-secondary">Obtenir de l'aide professionnelle</a>
</div>
</div>
</section>
