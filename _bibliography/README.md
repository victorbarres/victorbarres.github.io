# Bibliography notes (not rendered)

This folder is excluded from the site build (al-folio renders only `papers.bib` via jekyll-scholar). This README is just for the maintainer.

## Layout

Entries are grouped by **year** on the publications page (descending). The grouping/sort config lives in `_config.yml` under `scholar:` (`group_by: year`, `group_order: descending`).

Each entry carries a `keywords` field (`ai-agents` or `cogsci`) for future use, but the page itself is currently a single year-ordered list rather than category-grouped.

## What's currently included

### Conversational AI / Agents (keywords: ai-agents)
- τ-Knowledge (Shi, Zytek, Razavi, Narasimhan, Barres) — arXiv 2603.04370, 2026
- **τ-Voice** (Barres*, Ray*, Dhandhania*, Narasimhan) — arXiv 2603.13686, 2026 — *selected* — equal contribution
- **τ²-Bench** (Barres*, Dong*, Ray, Si, Narasimhan) — arXiv 2506.07982, 2025 — *selected* — equal contribution
- **From Generating Answers to Building Explanations** (Barres, McFate, Kalyanpur, Saravanakumar, Moon, Seifu, Bautista-Castillo) — NAACL Industry 2025 — *selected*
- **LLM-ARC** (Kalyanpur, Saravanakumar, Barres, Chu-Carroll, Melville, Ferrucci) — arXiv 2406.17663, 2024 — *selected*
- Multi-step Inference over Unstructured Data (Kalyanpur et al.) — arXiv 2406.17987, 2024
- Controllable Discovery of Intents (Rawat, Sankararaman, Barres) — IJCNLP 2023
- Real-time Caller Intent Detection (Rawat, Barres) — arXiv 2208.06802, 2022

### Cognitive Science / Neurolinguistics (keywords: cogsci)
- Can We Already Conceive of a Computational Construction Grammar… (Arbib, Chang, Dominey, Barres, Spranger) — AAAI Spring Symposium 2017
- **Template Construction Grammar: A Schema-Theoretic Computational CG** (Barres) — AAAI Spring Symposium 2017 — *selected*
- Hearing (rivaling) lips and seeing voices (Vidal, Barres) — Frontiers in Human Neuroscience 2014
- Language is handy but is it embodied? (Arbib, Gasser, Barres) — Neuropsychologia 2014
- **Template Construction Grammar: From Visual Scene Description…** (Barres, Lee) — Neuroinformatics 2014 — *selected*
- **Synthetic event-related potentials** (Barres, Simons, Arbib) — Neural Networks 2013 — *selected*
- Hearing lips and (not) seeing voices (Vidal, Barres) — Perception 2012 (conference abstract)
- How Auditory Information Influences Volitional Control… (Vidal, Barres) — i-Perception 2011 (conference abstract)

## Open items

- **τ-Bench (Yao et al. 2024)** is not listed because Victor isn't an author. It's referenced in the homepage `current work` block as the originating work that he now leads the codebase / leaderboard / extensions for.
- **Patents** (e.g. US Patent App. 17/491,511 "Method and apparatus for redacting sensitive information from audio"; 17/491,527 "active learning based call categorization"; 19/093,239 "Causal reasoning system") aren't listed here. Move to a separate Patents section if/when wanted.
- **Author name spelling**: site uses "Victor Barres" (ASCII) consistently. Scholar profile uses "Victor Barrès".

## Selected papers (homepage)

Papers marked `selected = {true}` appear on the homepage selected-papers panel. Currently 6:
- τ-Knowledge (2026)
- τ-Voice (2026) — equal contribution
- τ²-Bench (2025) — equal contribution
- From Generating Answers to Building Explanations (NAACL 2025)
- LLM-ARC (2024)
- Template Construction Grammar: A Schema-Theoretic Computational CG (AAAI-SS 2017)

The homepage panel renders all `selected = {true}` entries via `_includes/selected_papers.liquid`; a "See all publications →" link below it points to `/publications/`. Aim for ≤ 6 selected to keep the panel scannable; adjust `selected` flags in `papers.bib` to taste.
