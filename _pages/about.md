---
layout: about
title: about
permalink: /
subtitle: Research Scientist at <a href='https://www.mercor.com'>Mercor</a>.

profile:
  align: right
  image: victor_barres.jpg
  image_circular: false # crops the image to make it circular
  alt: Victor Barres, Research Scientist at Mercor. # screen-reader / SEO alt text; defaults to image filename if omitted
  more_info: # TODO: add address / office / contact lines here if desired

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false # blog disabled — flip to true if you start posting
  scrollable: true
  limit: 3
---

I build and study **conversational AI agents** — systems that have to get
real work done while sustaining long, coherent interactions with the people
they work with. Doing both at once is where most of what's hard about
deploying them lives.

I'm a founding member of the APEX research team at
[Mercor](https://www.mercor.com/blog/why-mercor-is-building-a-research-team/),
where I'm taking that beyond the single conversation: agents inside real
organizations, working with people, and transforming the work itself — and
how we measure that well enough to understand it, and help shape it. Before
that, I led the τ-Bench family of agent benchmarks at
[Sierra](https://sierra.ai) (live leaderboard at
[taubench.com](https://taubench.com)).

My background is in computational cognitive science and cognitive
linguistics, and I've spent years building real-world conversational
systems across several startups.
[More on how I think about the work →](/research/)

## the τ-Bench family

At Sierra I led the [**τ-Bench family**](https://taubench.com) of agent
benchmarks (originally introduced there in 2024) — code, repo, public
leaderboard, and a sequence of extensions, a line I still contribute to:

- **[τ²-Bench](https://sierra.ai/blog/benchmarking-agents-in-collaborative-real-world-scenarios)** — extends τ-Bench to a _dual-control_ setting where both the agent and the user can act on the world.
- **[τ-Knowledge](https://sierra.ai/blog/tau-knowledge)** — knowledge-retrieval domain.
- **[τ-Voice](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)** — first benchmark to measure full-duplex voice agents on realistic, grounded customer-service tasks.
- **[τ³-Bench](https://sierra.ai/blog/bench-advancing-agent-benchmarking-to-knowledge-and-voice)** — combines τ-Knowledge and τ-Voice with community-contributed task fixes and code improvements.
- **[τ-Multilingual](https://arxiv.org/abs/2609.35820)** — extends voice-agent evaluation across languages.
- **[Hyper-τ-Bench](https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents)** — flips τ-Bench around: the agent has to _build_ the agent, from scattered requirements and a client who holds the rest, and we grade what it ships.

**User simulation** runs through all of it — to build and evaluate agents
that talk with people, you need simulated people you can trust. I'm
co-organizing the NeurIPS 2026 workshop on
[**Grounded User Simulation for Model Evaluation and Training**](https://usersim-workshop.github.io/)
(Paris, December 12).
