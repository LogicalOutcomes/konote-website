---
title: "Sécurité et confidentialité"
description: "Comment KoNote protège les données des participant·e·s : chiffrement, contrôle d'accès, journal d'audit, conformité LPRPS/LPRPDE et résidence canadienne des données."
layout: "wide"
hero: true
hero_title: "Sécurité et confidentialité"
hero_tagline: "Comment KoNote protège les données des participant·e·s — et ce dont vous êtes responsable."
---

<section>
  <div class="container content-width">
    <div class="disclaimer">
      <p class="disclaimer-title">Modèle de responsabilité partagée</p>
      <p>
        KoNote fournit des fonctionnalités de sécurité, mais la sécurité est une responsabilité partagée.
        Le logiciel ne peut protéger les données que si vous le configurez et l'exploitez correctement.
        Cette page explique à la fois ce que KoNote fait et ce que vous devez faire.
      </p>
    </div>
  </div>
</section>

<section class="alt-bg">
  <div class="container">
    <h2>Ce que KoNote fait</h2>

    <div class="card-grid">
      <div class="card">
        <h3>Chiffrement au niveau des champs</h3>
        <p>
          Tous les renseignements personnels identifiables (RPI) sont chiffrés avant
          d'être stockés dans la base de données.
        </p>
        <ul>
          <li><strong>Algorithme :</strong> Fernet (AES-128-CBC + HMAC-SHA256) pour les RPI au repos</li>
          <li><strong>Champs chiffrés :</strong> Noms des participant·e·s, dates de naissance, courriels, numéros de téléphone, contenu des notes d'évolution, champs personnalisés sensibles, soumissions d'inscription</li>
          <li><strong>Stockage de la clé :</strong> Votre clé de chiffrement, stockée comme variable d'environnement (Azure Key Vault recommandé en production)</li>
          <li><strong>Rotation des clés :</strong> Commande intégrée de rotation des clés de chiffrement</li>
          <li><strong>Clés par organisme :</strong> Dans les déploiements multi-organismes, chaque organisme possède sa propre clé de chiffrement — la clé d'un organisme ne peut pas déchiffrer les données d'un autre</li>
        </ul>
        <p class="text-muted">
          Même si quelqu'un accède à la base de données, les champs chiffrés
          sont illisibles sans la clé de chiffrement. En hébergement partagé,
          la clé d'un organisme ne peut pas déchiffrer les données d'un autre organisme.
        </p>
      </div>

      <div class="card">
        <h3>Architecture à deux bases de données</h3>
        <p>
          KoNote utilise deux bases de données PostgreSQL distinctes.
        </p>
        <ul>
          <li><strong>Base de données opérationnelle :</strong> Dossiers des participant·e·s, notes, plans (opérations CRUD normales)</li>
          <li><strong>Base de données d'audit :</strong> Journal immuable de tous les accès et modifications de données (insertion uniquement)</li>
        </ul>
        <p class="text-muted">
          La base de données d'audit ne peut être ni modifiée ni supprimée par l'application,
          ce qui fournit un enregistrement inviolable.
        </p>
      </div>

      <div class="card">
        <h3>Contrôle d'accès basé sur les rôles</h3>
        <p>
          Cinq rôles avec des permissions différentes, appliquées au niveau de l'intergiciel.
        </p>
        <ul>
          <li><strong>Administrateur·rice :</strong> Configuration du système (aucun accès direct aux données des participant·e·s)</li>
          <li><strong>Gestionnaire de programme :</strong> Accès complet aux participant·e·s et au personnel de ses programmes</li>
          <li><strong>Intervenant·e direct·e :</strong> Accès aux participant·e·s des programmes qui lui sont assignés</li>
          <li><strong>Réception :</strong> Accès limité à certains champs seulement</li>
          <li><strong>Direction :</strong> Accès au tableau de bord et aux rapports</li>
        </ul>
        <p class="text-muted">
          Le personnel ne peut voir que les participant·e·s inscrit·e·s dans les programmes qui lui sont assignés.
          Les administrateur·rices sont délibérément bloqué·e·s des données des participant·e·s.
        </p>
      </div>

      <div class="card">
        <h3>Journal d'audit complet</h3>
        <p>
          Chaque action significative est consignée avec son contexte complet.
        </p>
        <ul>
          <li><strong>Modifications de données :</strong> Création, mise à jour, suppression avec les valeurs avant/après</li>
          <li><strong>Accès aux données :</strong> Qui a consulté quel dossier de participant·e et quand</li>
          <li><strong>Authentification :</strong> Connexion, déconnexion, tentatives de connexion échouées</li>
          <li><strong>Métadonnées :</strong> Horodatage, identifiant de l'utilisateur·rice, adresse IP</li>
        </ul>
        <p class="text-muted">
          Les journaux sont consultables depuis l'interface d'administration et peuvent être exportés.
        </p>
      </div>

      <div class="card">
        <h3>Authentification sécurisée</h3>
        <p>
          Deux options d'authentification, toutes deux utilisant des pratiques de sécurité modernes.
        </p>
        <ul>
          <li><strong>SSO Azure AD :</strong> Intégration avec Microsoft 365 de votre organisme</li>
          <li><strong>Authentification locale :</strong> Mots de passe hachés avec Argon2 (lauréat du concours Password Hashing Competition)</li>
        </ul>
        <p class="text-muted">
          Les jetons de session sont stockés dans la base de données avec des délais d'expiration configurables.
        </p>
      </div>

      <div class="card">
        <h3>Exportations de données sécurisées</h3>
        <p>
          Contrôles de défense en profondeur sur les exportations de données pour prévenir l'extraction non autorisée.
        </p>
        <ul>
          <li><strong>SecureExportLink :</strong> Liens de téléchargement à durée limitée avec expiration de 24 heures et déduplication par nonce</li>
          <li><strong>Exportations importantes :</strong> Les exportations volumineuses (100+ participant·e·s) ou contenant des notes déclenchent une notification à l'administrateur·rice et un délai de 10 minutes</li>
          <li><strong>Supervision administrative :</strong> Les administrateur·rices peuvent révoquer les liens d'exportation avant leur expiration</li>
          <li><strong>Suivi des téléchargements :</strong> Chaque téléchargement est consigné (qui, quand, combien de fois)</li>
          <li><strong>Revalidation :</strong> Les permissions d'accès aux RPI sont revérifiées au moment du téléchargement</li>
          <li><strong>Exportation à l'échelle de l'organisme :</strong> Exportation chiffrée AES-256-GCM pour la désaffectation complète de l'organisme, avec découverte automatique des modèles et génération de phrase de passe Diceware</li>
        </ul>
      </div>

      <div class="card">
        <h3>Résidence canadienne des données</h3>
        <p>
          Pour les organismes qui exigent que leurs données restent au Canada, KoNote prend en charge
          le déploiement sur une infrastructure canadienne.
        </p>
        <ul>
          <li><strong>OVHcloud Beauharnois :</strong> Centre de données canadien dédié au Québec</li>
          <li><strong>Azure Canada Central :</strong> Région infonuagique canadienne de Microsoft</li>
          <li><strong>Auto-hébergé :</strong> Déploiement sur n'importe quel serveur canadien que vous contrôlez</li>
          <li><strong>Clés de chiffrement :</strong> Stockées dans Azure Key Vault ou votre infrastructure sécurisée</li>
        </ul>
        <p class="text-muted">
          Les données des participant·e·s, les sauvegardes et les clés de chiffrement restent toutes à l'intérieur des frontières canadiennes.
        </p>
      </div>

      <div class="card">
        <h3>En-têtes de sécurité HTTP</h3>
        <p>
          En-têtes de sécurité HTTP configurés par défaut.
        </p>
        <ul>
          <li>Politique de sécurité du contenu (CSP)</li>
          <li>HTTP Strict Transport Security (HSTS)</li>
          <li>X-Frame-Options (protection contre le détournement de clic)</li>
          <li>X-Content-Type-Options</li>
          <li>Protection CSRF sur tous les formulaires</li>
        </ul>
      </div>

      <div class="card">
        <h3>Consentement inter-programmes conforme à la LPRPS</h3>
        <p>
          Applique les exigences de la LPRPS de l'Ontario concernant le partage de notes cliniques
          entre les programmes d'un même organisme.
        </p>
        <ul>
          <li><strong>Conception fermée par défaut :</strong> Les notes inter-programmes sont masquées par défaut</li>
          <li><strong>Accès conditionnel au consentement :</strong> Les notes cliniques ne sont visibles entre les programmes que lorsque le·la participant·e ou l'organisme a explicitement autorisé le partage</li>
          <li><strong>Application sur les listes et les détails :</strong> Les filtres de consentement s'appliquent à la fois sur les listes de notes (ensembles de requêtes) et sur les vues de notes individuelles</li>
          <li><strong>Vues exemptées :</strong> Les totaux agrégés, les rapports dépersonnalisés et les vues de plans ne sont pas affectés</li>
        </ul>
      </div>

      <div class="card">
        <h3>Limitation du débit et protection contre les attaques par force brute</h3>
        <p>
          Protections contre les attaques automatisées sur les points d'accès d'authentification.
        </p>
        <ul>
          <li><strong>Verrouillage de compte :</strong> Le portail des participant·e·s verrouille les comptes après plusieurs tentatives de connexion infructueuses</li>
          <li><strong>Sécurité des sessions :</strong> Jetons de session stockés dans la base de données avec des délais d'expiration configurables</li>
          <li><strong>Témoins sécurisés :</strong> Les témoins de session et CSRF sont marqués comme sécurisés en production</li>
          <li><strong>Vérifications au démarrage :</strong> La validation au démarrage assure que les clés de chiffrement, l'intergiciel de sécurité et les indicateurs de témoins sont correctement configurés</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Ce que vous devez faire</h2>
    <p class="text-muted mb-8">
      Les fonctionnalités de sécurité de KoNote ne fonctionnent que si vous remplissez vos responsabilités.
      Celles-ci ne sont pas facultatives.
    </p>

    <div class="card-grid">
      <div class="card">
        <h3>Protéger votre clé de chiffrement</h3>
        <p>
          <strong>Si vous perdez la clé de chiffrement, vous perdez définitivement l'accès à toutes les données chiffrées.</strong>
        </p>
        <ul>
          <li>Conservez la clé en lieu sûr (gestionnaire de mots de passe, coffre sécurisé)</li>
          <li>Conservez des sauvegardes hors ligne dans des endroits sûrs</li>
          <li>Ne jamais soumettre la clé dans un système de contrôle de version</li>
          <li>Limitez la connaissance de la clé au personnel essentiel</li>
        </ul>
        <div class="notice notice-warning mb-0">
          <p>Il n'y a pas de « mot de passe oublié » pour les clés de chiffrement. Clé perdue = données perdues.</p>
        </div>
      </div>

      <div class="card">
        <h3>Configurer HTTPS</h3>
        <p>
          Tous les déploiements en production doivent utiliser HTTPS. Sans cela, les données
          (y compris les identifiants de connexion) peuvent être interceptées.
        </p>
        <ul>
          <li>Railway et Elestio fournissent HTTPS automatiquement</li>
          <li>Azure nécessite une configuration</li>
          <li>L'auto-hébergement nécessite un proxy inverse (Caddy, nginx) avec des certificats</li>
        </ul>
        <div class="notice notice-warning mb-0">
          <p>N'exécutez jamais KoNote en HTTP simple en production.</p>
        </div>
      </div>

      <div class="card">
        <h3>Maintenir des sauvegardes régulières</h3>
        <p>
          Vous êtes responsable de la sauvegarde des deux bases de données et de la vérification
          que les sauvegardes peuvent être restaurées.
        </p>
        <ul>
          <li>Sauvegardes automatisées quotidiennes (au minimum)</li>
          <li>Conservez les sauvegardes dans un emplacement distinct de la base de données principale</li>
          <li>Testez les restaurations régulièrement (au moins chaque trimestre)</li>
          <li>Gardez les sauvegardes chiffrées et à accès contrôlé</li>
        </ul>
        <div class="notice notice-warning mb-0">
          <p>Si vous n'avez pas de sauvegardes et que quelque chose tourne mal, les données sont perdues.</p>
        </div>
      </div>

      <div class="card">
        <h3>Contrôler l'accès des utilisateur·rices</h3>
        <p>
          KoNote fournit les outils ; vous devez les utiliser correctement.
        </p>
        <ul>
          <li>Ne créez des comptes que pour les personnes qui en ont besoin</li>
          <li>Attribuez le rôle minimal nécessaire à chaque poste</li>
          <li>Supprimez les comptes rapidement lorsque le personnel quitte l'organisme</li>
          <li>Révisez régulièrement les accès des utilisateur·rices</li>
        </ul>
      </div>

      <div class="card">
        <h3>Maintenir le logiciel à jour</h3>
        <p>
          Des vulnérabilités de sécurité sont découvertes au fil du temps. Les mises à jour y remédient.
        </p>
        <ul>
          <li>Surveillez le dépôt GitHub pour les nouvelles versions</li>
          <li>Appliquez les mises à jour rapidement, en particulier les correctifs de sécurité</li>
          <li>Testez les mises à jour dans un environnement de préproduction si possible</li>
        </ul>
      </div>

      <div class="card">
        <h3>Former votre personnel</h3>
        <p>
          La sécurité technique n'est qu'une partie de l'équation.
        </p>
        <ul>
          <li>Formez le personnel sur l'utilisation acceptable et la gestion des données</li>
          <li>Établissez des politiques de partage de l'information</li>
          <li>Créez des procédures pour les incidents de sécurité</li>
          <li>Documentez les pratiques de confidentialité de votre organisme</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt-bg">
  <div class="container content-width">
    <h2>Fonctionnalités de conformité</h2>

    <div class="card">
      <h3>Conformité à la LPRPS et à la LPRPDE</h3>
      <p>
        KoNote comprend des fonctionnalités pour soutenir la conformité à la Loi sur la protection des renseignements personnels et les documents électroniques (LPRPDE) du Canada
        et à la Loi sur la protection des renseignements personnels sur la santé (LPRPS) de l'Ontario.
      </p>
      <ul>
        <li>Chiffrement des renseignements personnels (Fernet AES au repos)</li>
        <li>Clés de chiffrement par organisme dans les déploiements multi-organismes</li>
        <li>Contrôles d'accès et journal d'audit</li>
        <li>Enregistrement du consentement avec suivi immuable des retraits</li>
        <li>Application du consentement inter-programmes — notes cliniques partagées uniquement avec la permission du·de la participant·e ou de l'organisme</li>
        <li>Configuration de la rétention des données</li>
        <li>Flux de travail d'effacement des données en plusieurs étapes avec chaîne d'approbation</li>
        <li>Modèle de politique de confidentialité</li>
        <li>Option de résidence canadienne des données (OVHcloud Beauharnois, QC)</li>
        <li>Protection des données de collecte sur le terrain hors connexion — niveaux RPI et protocoles en cas de perte d'appareil</li>
      </ul>
      <p class="text-muted">
        <strong>Note :</strong> L'utilisation de KoNote ne vous rend pas automatiquement conforme à la LPRPS ou à la LPRPDE.
        La conformité dépend de la façon dont vous configurez et exploitez le système,
        de vos politiques et des pratiques de votre personnel.
      </p>
    </div>

    <div class="card">
      <h3>Conformité au RGPD</h3>
      <p>
        Pour les organismes qui servent des participant·e·s européen·nes, KoNote comprend :
      </p>
      <ul>
        <li>Suivi du consentement (champ consent_given_at)</li>
        <li>Périodes de rétention des données</li>
        <li>Flux de travail d'approbation d'effacement par plusieurs gestionnaires de programme</li>
        <li>Exécution automatique de l'effacement lorsque toutes les approbations sont reçues</li>
        <li>Piste d'audit du traitement des données conservée après l'effacement</li>
      </ul>
      <p class="text-muted">
        <strong>Note :</strong> La conformité au RGPD nécessite davantage que des fonctionnalités logicielles.
        Consultez un·e professionnel·le de la confidentialité pour votre situation spécifique.
      </p>
    </div>

    <div class="card">
      <h3>Accessibilité (WCAG 2.2 AA)</h3>
      <p>
        KoNote est conçu avec l'accessibilité comme exigence fondamentale, et non comme une réflexion après coup :
      </p>
      <ul>
        <li>Structure HTML sémantique avec hiérarchie des titres appropriée</li>
        <li>Navigation complète au clavier avec les modèles WAI-ARIA roving tabindex</li>
        <li>Conformité au contraste des couleurs WCAG 2.2 AA</li>
        <li>Tailles de zones tactiles respectant le minimum WCAG 2.5.8 (24 px)</li>
        <li>Compatible avec les lecteurs d'écran — rôles WAI-ARIA pour les menus, onglets et éléments interactifs</li>
        <li>Liens d'évitement sur chaque page</li>
        <li>Tests d'accessibilité automatisés avec axe-core intégrés dans le pipeline CI</li>
        <li>Le service worker fournit un mode hors connexion élégant</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container content-width">
    <h2>Limites de sécurité</h2>
    <p>
      Pour être honnête sur ce que KoNote ne peut pas faire :
    </p>

    <div class="card">
      <h3>Pas de recherche chiffrée</h3>
      <p>
        Les champs chiffrés ne peuvent pas être recherchés par des requêtes SQL. La recherche de participant·e·s
        charge les participant·e·s accessibles en mémoire et filtre en Python.
        Cela fonctionne bien jusqu'à environ 2 000 participant·e·s, mais peut ralentir à plus grande échelle.
      </p>
    </div>

    <div class="card">
      <h3>AMF du personnel via SSO uniquement</h3>
      <p>
        L'authentification locale du personnel n'inclut pas l'authentification multifacteur (AMF). Si vous avez besoin de l'AMF pour le personnel, utilisez Azure AD SSO,
        qui prend en charge les politiques AMF de votre organisme. Le portail des participant·e·s dispose
        d'une AMF intégrée (application d'authentification TOTP ou codes de vérification par courriel).
      </p>
    </div>

    <div class="card">
      <h3>Pas de détection automatique des intrusions</h3>
      <p>
        KoNote consigne les accès mais ne génère pas automatiquement d'alertes sur les comportements suspects.
        Vous devez réviser les journaux d'audit périodiquement ou intégrer des outils
        de surveillance externes.
      </p>
    </div>
  </div>
</section>

<section class="alt-bg">
  <div class="container text-center">
    <h2>Des questions sur la sécurité ?</h2>
    <p class="text-muted mb-8">
      La documentation technique contient plus de détails sur la mise en œuvre de la sécurité.
      Pour les questions propres à votre organisme, envisagez une consultation professionnelle.
    </p>
    <div class="btn-group" style="justify-content: center;">
      <a href="/fr/documentation/" class="btn btn-primary">Documentation technique</a>
      <a href="/fr/services/" class="btn btn-secondary">Services professionnels</a>
    </div>
  </div>
</section>
