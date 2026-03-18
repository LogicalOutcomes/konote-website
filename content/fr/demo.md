---
title: "Essayez-le"
description: "Essayez les formulaires d'inscription et de sondage en libre-service de KoNote. Voyez comment les participants s'inscrivent et comment le personnel recueille les rétroactions — dans une démonstration en direct."
layout: "wide"
hero: true
hero_title: "Essayez-le"
hero_tagline: "Ce sont des formulaires en direct connectés à une vraie instance de KoNote. Essayez le formulaire d'inscription, remplissez un sondage, puis connectez-vous pour voir comment le personnel gère tout."
---

<style>
  .workflow-steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--space-6);
    margin: var(--space-8) 0;
    counter-reset: step;
  }

  .workflow-step {
    text-align: center;
    padding: var(--space-6) var(--space-4);
    position: relative;
  }

  .workflow-step::before {
    counter-increment: step;
    content: counter(step);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.5rem;
    height: 2.5rem;
    background: var(--color-primary);
    color: white;
    font-weight: 700;
    font-size: var(--font-size-lg);
    border-radius: 50%;
    margin-bottom: var(--space-4);
  }

  .workflow-step h3 {
    font-size: var(--font-size-base);
    margin-bottom: var(--space-2);
  }

  .workflow-step p {
    color: var(--color-text-muted);
    font-size: var(--font-size-sm);
    margin-bottom: 0;
  }

  .demo-frame-container {
    max-width: 720px;
    margin: 0 auto;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    background: var(--color-bg);
    box-shadow: var(--shadow-md);
  }

  .demo-frame-header {
    background: var(--color-bg-alt);
    border-bottom: 1px solid var(--color-border);
    padding: var(--space-3) var(--space-4);
    font-size: var(--font-size-sm);
    color: var(--color-text-muted);
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }

  .demo-frame-header svg {
    flex-shrink: 0;
  }

  .demo-frame-container iframe {
    display: block;
    width: 100%;
    min-height: 820px;
    border: none;
    overflow: hidden;
    transition: height 0.15s ease;
  }
</style>

<section>
<div class="container">

<h2>Comment ça fonctionne</h2>
<div class="workflow-steps">
<div class="workflow-step">
<h3>S'inscrire</h3>
<p>Remplissez le formulaire ci-dessous. Utilisez le nom que vous souhaitez &mdash; c'est un environnement de démonstration.</p>
</div>
<div class="workflow-step">
<h3>Se connecter</h3>
<p>Ouvrez l'<a href="https://demo.konote.ca/" target="_blank" rel="noopener">application de démonstration KoNote</a> et connectez-vous en tant qu'utilisateur de démonstration (identifiants ci-dessous).</p>
</div>
<div class="workflow-step">
<h3>Trouver votre inscription</h3>
<p>Allez dans le programme Emploi avec soutien. Votre inscription apparaît comme un nouveau participant.</p>
</div>
<div class="workflow-step">
<h3>Explorer</h3>
<p>Ajoutez un plan de résultats, rédigez des notes d'évolution, enregistrez des métriques et voyez les graphiques se mettre à jour en temps réel.</p>
</div>
</div>

<h2>Étape 1 : Inscrire un participant</h2>
<div class="section-header">
<p>
        Cette démonstration présente une version simplifiée. KoNote comprend plus de 50 champs configurables
        répartis en 9 groupes de champs &mdash; coordonnées, contacts d'urgence, données démographiques,
        accessibilité, informations sur la référence, formulaires de consentement, et plus encore. Votre organisme choisit quels
        champs et groupes inclure, et peut en ajouter de personnalisés en quelques minutes. Aucun développeur requis.
</p>
</div>

<div class="demo-frame-container">
<div class="demo-frame-header">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
<circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
<path d="M8 5v3M8 10h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</svg>
        Démonstration en direct &mdash; les soumissions vont dans un environnement de test, pas des données réelles
</div>
<iframe
        src="https://demo.konote.ca/register/demo/?embed=1"
        title="Démonstration du formulaire d'inscription KoNote"
        loading="lazy"
        scrolling="no"
        allow="forms">
</iframe>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container">
<h2>Étape 2 : Se connecter et trouver la personne</h2>
<p>
      Après la soumission du formulaire, votre inscription est automatiquement approuvée et le
      participant apparaît dans le programme <strong>Emploi avec soutien</strong>.
</p>

<div class="card-grid">
<div class="card">
<h3>Connexion de démonstration</h3>
<p>
          Ouvrez l'<a href="https://demo.konote.ca/" target="_blank" rel="noopener"><strong>application de démonstration KoNote</strong></a>
          et connectez-vous :
</p>
<ul>
<li><strong>Nom d'utilisateur :</strong> <code>demo-worker-1</code></li>
<li><strong>Mot de passe :</strong> <code>demo1234</code></li>
</ul>
<p class="text-muted" style="font-size: var(--font-size-sm); margin-top: var(--space-3);">
          Ceci vous connecte en tant que Casey Worker, gestionnaire de programme pour Emploi avec soutien.
</p>
</div>
<div class="card">
<h3>Trouver le participant</h3>
<p>Une fois connecté :</p>
<ol>
<li>Tapez le nom que vous avez inscrit dans la <strong>barre de recherche</strong></li>
<li>Cliquez sur son nom pour ouvrir son dossier</li>
<li>La personne est inscrite dans le programme <strong>Emploi avec soutien</strong></li>
</ol>
</div>
</div>
</div>
</section>

<section>
<div class="container">
<h2>Étape 3 : Essayer le flux de travail complet</h2>
<p>Maintenant que vous avez un participant, essayez ces fonctionnalités :</p>

<div class="card-grid">
<div class="card">
<h3>Ajouter un plan de résultats</h3>
<p>Allez dans l'onglet <strong>Plan</strong>. Appliquez un modèle de plan pour établir des objectifs et des cibles sur lesquels la personne participante travaillera.</p>
</div>
<div class="card">
<h3>Rédiger une note d'évolution</h3>
<p>Allez dans l'onglet <strong>Notes</strong> et cliquez sur <strong>+ Note d'évolution</strong>. Sélectionnez des cibles, ajoutez des métriques et saisissez une réflexion du participant.</p>
</div>
<div class="card">
<h3>Voir les graphiques de progression</h3>
<p>Après avoir enregistré quelques notes avec des métriques, consultez l'onglet <strong>Analyse</strong> pour voir la progression visualisée dans le temps.</p>
</div>
</div>

<div class="notice notice-info">
<p class="notice-title">C'est une démonstration partagée</p>
<p>
        D'autres visiteurs peuvent également essayer la démonstration, vous pourriez donc voir des participants que vous n'avez pas créés.
        La démonstration se réinitialise périodiquement. Utilisez le nom que vous souhaitez &mdash; aucune vraie donnée n'est collectée.
</p>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container">
<h2>Essayer un sondage</h2>
<p>
      KoNote comprend un moteur de sondage complet pour les formulaires d'accueil, les questionnaires de satisfaction
      et les évaluations normalisées. Le personnel crée des sondages dans le panneau d'administration, puis les partage
      avec les participants de trois façons : un lien public (aucune connexion requise), le
      portail des participants ou la saisie de données assistée par le personnel.
</p>
<p>
      Le formulaire ci-dessous est un lien partageable en direct &mdash; le même type que vous enverriez aux
      participants ou publieriez sur votre site Web. Remplissez-le pour voir comment ça fonctionne, puis connectez-vous
      en tant qu'utilisateur de démonstration pour voir les résultats.
</p>

<div class="workflow-steps" style="counter-reset: step;">
<div class="workflow-step">
<h3>Remplir le sondage</h3>
<p>Complétez le formulaire ci-dessous. Vos réponses vont dans l'environnement de démonstration &mdash; aucune vraie donnée n'est collectée.</p>
</div>
<div class="workflow-step">
<h3>Se connecter en tant que personnel</h3>
<p>Ouvrez l'<a href="https://demo.konote.ca/" target="_blank" rel="noopener">application de démonstration KoNote</a> et connectez-vous avec les identifiants de démonstration ci-dessus.</p>
</div>
<div class="workflow-step">
<h3>Voir les résultats</h3>
<p>Allez dans <strong>Sondages</strong> dans le menu principal. Ouvrez le sondage pour voir toutes les réponses, y compris les vôtres.</p>
</div>
</div>

<div class="demo-frame-container">
<div class="demo-frame-header">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
<circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
<path d="M8 5v3M8 10h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</svg>
        Sondage en direct &mdash; les soumissions vont dans un environnement de test, pas des données réelles
</div>
<iframe
        src="https://demo.konote.ca/s/demo-program-feedback/?embed=1"
        title="Démonstration de sondage KoNote"
        loading="lazy"
        scrolling="no"
        allow="forms">
</iframe>
</div>

<div class="notice notice-info" style="margin-top: var(--space-8);">
<p class="notice-title">Ce que voit le personnel</p>
<p>
        Après votre soumission, connectez-vous en tant que <code>demo-worker-1</code> et allez dans
<strong>Sondages</strong>. Vous pouvez consulter les réponses individuelles, voir
        le nombre de réponses et exporter les résultats en CSV. Le personnel peut également assigner
        des sondages à des participants spécifiques et suivre leur complétion.
</p>
</div>
</div>
</section>

<section>
<div class="container text-center">
<p class="text-muted mb-8">
      L'inscription et les sondages ne sont que deux des nombreuses fonctionnalités de KoNote.
      Consultez l'<a href="/fr/fonctionnalites/">aperçu des fonctionnalités</a> ou
      lisez le <a href="/fr/premiers-pas/">guide de démarrage</a>
      pour en savoir plus.
</p>
</div>
</section>

<script>
  window.addEventListener('message', function(event) {
    if (event.data && event.data.type === 'konote-embed-resize') {
      var iframes = document.querySelectorAll('.demo-frame-container iframe');
      iframes.forEach(function(iframe) {
        if (iframe.contentWindow === event.source) {
          iframe.style.height = event.data.height + 'px';
        }
      });
    }
  });
</script>
