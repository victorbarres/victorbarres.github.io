---
layout: page
permalink: /cv/
title: cv
description: current as of May 2026.
nav: true
nav_order: 4
---

<!--
  _pages/cv.md — the canonical source for the CV PDF is cv-src/barres_cv.tex.
  Build with `bin/build_cv.sh`, which compiles the LaTeX and publishes the PDF to
  assets/pdf/barres_cv.pdf.

  The short HTML summary below the download button is hand-curated to give the
  page indexable, screen-reader-friendly content (PDF embeds aren't crawled).
  Keep it in sync with cv-src/barres_cv.tex when roles change.

  If you'd rather have the al-folio cv.liquid layout rendering from _data/cv.yml,
  create _data/cv.yml in the rendercv schema, flip the layout back to `cv`, and
  add `cv_pdf: /assets/pdf/barres_cv.pdf` to the front matter. (The PDF download
  icon will appear in the page header.)
-->

<p>
  <a href="/assets/pdf/barres_cv.pdf" class="btn btn-outline-primary" target="_blank" rel="noopener">
    Download PDF →
  </a>
</p>

<section class="cv-summary" aria-label="CV summary" markdown="1">

### experience

- **Sierra** — *AI Researcher* · Sep 2024 – Present · San Francisco, CA. Lead the
  τ-Bench family of agent benchmarks (research direction, codebase, public
  leaderboard at [taubench.com](https://taubench.com), and a sequence of
  extensions: τ²-Bench, τ-Knowledge, τ-Voice, τ³-Bench — three papers accepted
  to ICML 2026). Kickstarted Sierra's internal agent evaluation system and the
  user-simulation-driven stress testing used to harden agents pre-release.
- **Elemental Cognition** — *Senior Researcher (NLP)* · Jun 2023 – Jul 2024 ·
  Remote. Core algorithms for EC's hybrid AI architecture integrating LLMs
  with formal reasoning. Led the multi-round-RAG + causal-modeling work
  published as *From Generating Answers to Building Explanations* at NAACL
  2025 (Industry).
- **Uniphore.ai** — *Principal NLP Scientist & NLP Research Lead* (previously
  Senior NLP Scientist) · Dec 2019 – Jun 2023 · Palo Alto, CA. Built and led
  Uniphore's NLP Lab (7+ scientists); set short-, mid-, and long-term
  research strategy for understanding human–human spoken conversation in the
  contact-center domain.
- **Astound.ai** — *AI Scientist (NLP)* · Sep 2017 – Dec 2019 · Menlo Park, CA.
  Core member of the team that built Astound's domain-expert conversational
  agent for IT / HR / Finance enterprise self-service from the ground up.

### education

- **University of Southern California** — *PhD, Computational Cognitive
  Neuroscience* · 2010 – 2017. Dissertation: *Schema Architecture for
  Language–Vision Interactions*. Advisor: Michael A. Arbib.
- **École Normale Supérieure**, Paris — *MS, Cognitive Science* · 2008 – 2010.
- **École Polytechnique**, Palaiseau — *MS, Physics* · 2003 – 2006.
- **Lycée Louis-le-Grand**, Paris — Classes Préparatoires, Mathematics &
  Physics · 2001 – 2003.

### languages

English (fluent) · French (native) · Spanish (conversational).

The PDF below is the canonical, formatted version — see it for full
publication and selected-works lists.

</section>

<div class="cv-embed">
  <embed
    src="/assets/pdf/barres_cv.pdf"
    type="application/pdf"
    width="100%"
    height="900px"
    aria-label="Victor Barres — CV (PDF). The HTML summary above mirrors the same content."
  />
</div>
