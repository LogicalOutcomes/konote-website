---
title: "Try It"
description: "Try KoNote's self-service registration and survey forms. See how participants register and how staff collect feedback — all in a live demo."
layout: "wide"
hero: true
hero_title: "Try It"
hero_tagline: "These are live forms connected to a real KoNote instance. Try the registration form, fill out a survey, then log in to see how staff manage everything."
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

<h2>How It Works</h2>
<div class="workflow-steps">
<div class="workflow-step">
<h3>Register</h3>
<p>Fill out the form below. Use any name you like &mdash; this is a demo environment.</p>
</div>
<div class="workflow-step">
<h3>Log In</h3>
<p>Open the <a href="https://demo.konote.ca/" target="_blank" rel="noopener">KoNote demo app</a> and sign in as a demo user (credentials below).</p>
</div>
<div class="workflow-step">
<h3>Find Your Registration</h3>
<p>Go to the Supported Employment program. Your registration appears as a new participant.</p>
</div>
<div class="workflow-step">
<h3>Explore</h3>
<p>Add an outcome plan, write progress notes, record metrics, and see charts update in real time.</p>
</div>
</div>

<h2>Step 1: Register a Participant</h2>
<div class="section-header">
<p>
        This demo shows a simplified version. KoNote includes over 50 configurable
        fields across 9 field groups &mdash; contact details, emergency contacts, demographics,
        accessibility, referral info, consent forms, and more. Your agency chooses which
        fields and groups to include, and can add custom ones in minutes. No developer needed.
</p>
</div>

<div class="demo-frame-container">
<div class="demo-frame-header">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
<circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
<path d="M8 5v3M8 10h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</svg>
        Live demo &mdash; submissions go to a test environment, not real data
</div>
<iframe
        src="https://demo.konote.ca/register/demo/?embed=1"
        title="KoNote Registration Form Demo"
        loading="lazy"
        scrolling="no"
        allow="forms">
</iframe>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container">
<h2>Step 2: Log In and Find Them</h2>
<p>
      After submitting the form, your registration is automatically approved and the
      participant appears in the <strong>Supported Employment</strong> program.
</p>

<div class="card-grid">
<div class="card">
<h3>Demo Login</h3>
<p>
          Open the <a href="https://demo.konote.ca/" target="_blank" rel="noopener"><strong>KoNote demo app</strong></a>
          and sign in:
</p>
<ul>
<li><strong>Username:</strong> <code>demo-worker-1</code></li>
<li><strong>Password:</strong> <code>demo1234</code></li>
</ul>
<p class="text-muted" style="font-size: var(--font-size-sm); margin-top: var(--space-3);">
          This logs you in as Casey Worker, a program manager for Supported Employment.
</p>
</div>
<div class="card">
<h3>Find the Participant</h3>
<p>Once logged in:</p>
<ol>
<li>Type the name you registered in the <strong>search bar</strong></li>
<li>Click their name to open their file</li>
<li>They are enrolled in <strong>Supported Employment</strong></li>
</ol>
</div>
</div>
</div>
</section>

<section>
<div class="container">
<h2>Step 3: Try the Full Workflow</h2>
<p>Now that you have a participant, try these features:</p>

<div class="card-grid">
<div class="card">
<h3>Add an Outcome Plan</h3>
<p>Go to the <strong>Plan</strong> tab. Apply a plan template to set up goals and targets the participant will work towards.</p>
</div>
<div class="card">
<h3>Write a Progress Note</h3>
<p>Go to the <strong>Notes</strong> tab and click <strong>+ Progress Note</strong>. Select targets, add metrics, and capture a participant reflection.</p>
</div>
<div class="card">
<h3>See Progress Charts</h3>
<p>After recording a few notes with metrics, check the <strong>Analysis</strong> tab to see progress visualized over time.</p>
</div>
</div>

<div class="notice notice-info">
<p class="notice-title">This is a shared demo</p>
<p>
        Other visitors may also be trying the demo, so you might see participants you did not create.
        The demo resets periodically. Use any name you like &mdash; no real data is collected.
</p>
</div>
</div>
</section>

<section class="alt-bg">
<div class="container">
<h2>Try a Survey</h2>
<p>
      KoNote includes a full survey engine for intake forms, satisfaction questionnaires,
      and standardized assessments. Staff create surveys in the admin panel, then share
      them with participants in three ways: a public link (no login needed), the
      participant portal, or staff-assisted data entry.
</p>
<p>
      The form below is a live shareable link &mdash; the same kind you would send to
      participants or post on your website. Fill it out to see how it works, then log in
      as the demo user to view the results.
</p>

<div class="workflow-steps" style="counter-reset: step;">
<div class="workflow-step">
<h3>Fill Out the Survey</h3>
<p>Complete the form below. Your answers go to the demo environment &mdash; no real data is collected.</p>
</div>
<div class="workflow-step">
<h3>Log In as Staff</h3>
<p>Open the <a href="https://demo.konote.ca/" target="_blank" rel="noopener">KoNote demo app</a> and sign in with the demo credentials above.</p>
</div>
<div class="workflow-step">
<h3>View Results</h3>
<p>Go to <strong>Surveys</strong> in the main menu. Open the survey to see all responses, including yours.</p>
</div>
</div>

<div class="demo-frame-container">
<div class="demo-frame-header">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
<circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
<path d="M8 5v3M8 10h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</svg>
        Live survey &mdash; submissions go to a test environment, not real data
</div>
<iframe
        src="https://demo.konote.ca/s/demo-program-feedback/?embed=1"
        title="KoNote Survey Demo"
        loading="lazy"
        scrolling="no"
        allow="forms">
</iframe>
</div>

<div class="notice notice-info" style="margin-top: var(--space-8);">
<p class="notice-title">What staff see</p>
<p>
        After you submit, log in as <code>demo-worker-1</code> and go to
<strong>Surveys</strong>. You can view individual responses, see
        response counts, and export results to CSV. Staff can also assign
        surveys to specific participants and track completion.
</p>
</div>
</div>
</section>

<section>
<div class="container text-center">
<p class="text-muted mb-8">
      Registration and surveys are just two of many features in KoNote.
      See the <a href="/en/features/">features overview</a> or
      read the <a href="/en/getting-started/">getting started guide</a>
      to learn more.
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
