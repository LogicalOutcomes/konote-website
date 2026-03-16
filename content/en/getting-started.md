---
title: "Getting Started"
description: "How to evaluate and deploy KoNote. Deployment options, requirements, and step-by-step guidance."
layout: "wide"
hero: true
hero_title: "Getting Started"
hero_tagline: "How to evaluate KoNote and decide if it's right for your organisation."
---

<section>
  <div class="container content-width">
    <h2>Is KoNote Right for You?</h2>
    <p>
      Before investing time in evaluation, make sure KoNote is a reasonable fit
      for your organisation. Answer these questions honestly:
    </p>

    <div class="card">
      <h3>Technical Capacity</h3>
      <p><strong>Do you have someone who can:</strong></p>
      <ul>
        <li>Deploy a Docker-based application to a cloud platform?</li>
        <li>Configure environment variables and manage secrets?</li>
        <li>Set up and maintain regular database backups?</li>
        <li>Apply software updates when new versions are released?</li>
        <li>Troubleshoot issues using documentation and logs?</li>
      </ul>
      <p>
        If yes to most of these, you have sufficient technical capacity.
        If no, you'll need an IT partner or our <a href="/en/services/">professional services</a>.
      </p>
    </div>

    <div class="card">
      <h3>Organisational Fit</h3>
      <p><strong>Does your organisation:</strong></p>
      <ul>
        <li>Track participant outcomes as a core function?</li>
        <li>Need to demonstrate program impact to funders?</li>
        <li>Serve fewer than ~2,000 active participants?</li>
        <li>Require control over where participant data is stored?</li>
        <li>Value open source software and avoiding vendor lock-in?</li>
      </ul>
      <p>
        If yes to most of these, KoNote is likely a good fit.
        If no, a commercial SaaS solution might serve you better.
      </p>
    </div>
  </div>
</section>

<section class="alt-bg">
  <div class="container content-width">
    <h2>Evaluation Path</h2>
    <p>
      We recommend this sequence for evaluating KoNote:
    </p>

    <div class="card">
      <h3>Step 1: Read the Documentation</h3>
      <p>
        Start with the <a href="/en/documentation/">documentation</a> to understand
        what KoNote does. The user guide will show you daily workflows; the technical
        documentation will help your IT team understand the architecture.
      </p>
      <p class="text-muted">Time: 1–2 hours</p>
    </div>

    <div class="card">
      <h3>Step 2: Try a Demo</h3>
      <p>
        <strong>Online demo (no setup needed):</strong>
        <a href="/en/demo/">Try the live registration form</a> to see how
        participants register for programs through KoNote. This runs on a real instance
        — no installation required.
      </p>
      <p>
        <strong>Local demo (requires Docker):</strong>
        If you want to explore the full staff interface, run a local demo
        with sample data:
      </p>
      <pre><code>docker-compose -f docker-compose.demo.yml up</code></pre>
      <p class="text-muted">Online demo: 2 minutes. Local demo: 30–45 minutes (including Docker setup).</p>
    </div>

    <div class="card">
      <h3>Step 3: Choose a Deployment Platform</h3>
      <p>
        If the demo looks promising, decide where you'll host KoNote.
        See the <a href="#deployment-options">deployment options</a> below.
      </p>
      <p class="text-muted">Time: Research and decision-making</p>
    </div>

    <div class="card">
      <h3>Step 4: Deploy and Configure</h3>
      <p>
        Follow the deployment guide for your chosen platform. Then configure
        your agency: set up programs, create user accounts, customise terminology.
      </p>
      <p class="text-muted">Time: 2–4 hours for deployment, plus configuration</p>
    </div>

    <div class="card">
      <h3>Step 5: Pilot with Real Users</h3>
      <p>
        Start with a small pilot group before rolling out organisation-wide.
        Gather feedback, refine your configuration, and build internal documentation.
      </p>
    </div>
  </div>
</section>

<section id="deployment-options">
  <div class="container">
    <h2>Deployment Options</h2>
    <p class="text-muted mb-8">
      KoNote runs anywhere Docker runs. Here are the most common options,
      with honest assessments of each.
    </p>

    <div class="card-grid">
      <div class="card">
        <h3>Railway</h3>
        <p><strong>Easiest deployment</strong></p>
        <p>
          One-click deployment from GitHub. Managed PostgreSQL databases.
          Automatic HTTPS. Good for organisations without dedicated IT staff.
        </p>
        <ul>
          <li><strong>Cost:</strong> ~$45–50 CAD/month</li>
          <li><strong>Difficulty:</strong> Low</li>
          <li><strong>Data location:</strong> US (Railway's infrastructure)</li>
        </ul>
        <p class="text-muted">
          Best for: Small-medium organisations wanting simplicity.
        </p>
      </div>

      <div class="card">
        <h3>Microsoft Azure</h3>
        <p><strong>Canadian data residency</strong></p>
        <p>
          Deploy to Azure Container Instances with Azure Database for PostgreSQL.
          Data can stay in Canadian regions. More complex setup.
        </p>
        <ul>
          <li><strong>Cost:</strong> Varies ($50–150 CAD/month typical)</li>
          <li><strong>Difficulty:</strong> Medium-High</li>
          <li><strong>Data location:</strong> Your choice (Canada Central available)</li>
        </ul>
        <p class="text-muted">
          Best for: Organisations requiring Canadian data residency.
        </p>
      </div>

      <div class="card">
        <h3>Elestio</h3>
        <p><strong>Managed Docker hosting</strong></p>
        <p>
          Docker Compose hosting with managed infrastructure.
          Middle ground between Railway's simplicity and full self-hosting.
        </p>
        <ul>
          <li><strong>Cost:</strong> Varies by plan</li>
          <li><strong>Difficulty:</strong> Medium</li>
          <li><strong>Data location:</strong> Multiple options</li>
        </ul>
        <p class="text-muted">
          Best for: Organisations comfortable with Docker but not infrastructure.
        </p>
      </div>

      <div class="card">
        <h3>OVHcloud (Beauharnois, QC)</h3>
        <p><strong>Canadian data residency</strong></p>
        <p>
          Deploy to OVHcloud's Beauharnois data centre in Quebec.
          Docker Compose with Caddy reverse proxy and automated self-healing.
        </p>
        <ul>
          <li><strong>Cost:</strong> Varies by VPS plan</li>
          <li><strong>Difficulty:</strong> Medium</li>
          <li><strong>Data location:</strong> Canada (Quebec)</li>
        </ul>
        <p class="text-muted">
          Best for: Organisations requiring Canadian data residency at lower cost than Azure.
        </p>
      </div>

      <div class="card">
        <h3>Self-Hosted</h3>
        <p><strong>Full control</strong></p>
        <p>
          Run Docker Compose on your own servers or VPS. Complete control
          over everything. Requires DevOps knowledge.
        </p>
        <ul>
          <li><strong>Cost:</strong> Infrastructure costs only</li>
          <li><strong>Difficulty:</strong> High</li>
          <li><strong>Data location:</strong> Your choice</li>
        </ul>
        <p class="text-muted">
          Best for: Organisations with dedicated IT staff and infrastructure.
        </p>
      </div>
    </div>

    <div class="notice notice-warning">
      <p class="notice-title">Data Residency Considerations</p>
      <p>
        If your organisation requires participant data to stay in Canada,
        Railway's US-based infrastructure may not be suitable.
        Consider OVHcloud Beauharnois, Azure (Canada Central region),
        or self-hosting in a Canadian data centre.
      </p>
    </div>
  </div>
</section>

<section class="alt-bg">
  <div class="container content-width">
    <h2>What You'll Need</h2>

    <div class="card">
      <h3>For the Demo (Local Testing)</h3>
      <ul>
        <li>Docker Desktop installed on your computer</li>
        <li>Command line/terminal access</li>
        <li>~2GB free disk space</li>
        <li>30–45 minutes</li>
      </ul>
    </div>

    <div class="card">
      <h3>For Production Deployment</h3>
      <ul>
        <li>A hosting platform account (Railway, Azure, etc.)</li>
        <li>A secure encryption key (you generate this)</li>
        <li>Azure AD tenant (if using SSO) or local authentication</li>
        <li>A backup strategy (you're responsible for this)</li>
        <li>Someone to manage ongoing operations</li>
      </ul>
    </div>

    <div class="disclaimer">
      <p class="disclaimer-title">Your Responsibilities</p>
      <p>
        Once deployed, you are responsible for:
      </p>
      <ul>
        <li><strong>Security:</strong> Keeping your encryption key safe, configuring HTTPS, managing user access</li>
        <li><strong>Backups:</strong> Regular database backups and testing restores</li>
        <li><strong>Updates:</strong> Applying new versions of KoNote when released</li>
        <li><strong>Training:</strong> Training your staff to use the system</li>
        <li><strong>Support:</strong> Troubleshooting issues (community support via GitHub)</li>
      </ul>
      <p>
        If this sounds like more than your team can handle,
        consider our <a href="/en/services/">professional services</a>.
      </p>
    </div>
  </div>
</section>

<section>
  <div class="container text-center">
    <h2>Ready to Proceed?</h2>
    <p class="text-muted mb-8">
      The full deployment guide has step-by-step instructions for each platform.
    </p>
    <div class="btn-group" style="justify-content: center;">
      <a href="/en/documentation/" class="btn btn-primary">View Documentation</a>
      <a href="/en/services/" class="btn btn-secondary">Get Professional Help</a>
    </div>
  </div>
</section>
