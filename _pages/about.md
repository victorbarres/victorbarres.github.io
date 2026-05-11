---
layout: about
title: about
permalink: /
subtitle: AI Researcher at <a href='https://sierra.ai'>Sierra</a>.

profile:
  align: right
  image: victor_barres.jpg
  image_circular: false # crops the image to make it circular
  alt: Victor Barres, AI Researcher at Sierra. # screen-reader / SEO alt text; defaults to image filename if omitted
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

I'm a researcher at [Sierra](https://sierra.ai), where I build and study
**conversational AI agents** and the benchmarks that tell us when they
actually work — the τ-Bench family (live leaderboard at
[taubench.com](https://taubench.com)). My focus is on agents that must
execute complex tool-using tasks while sustaining long, coherent
conversational interactions — the two things real-world deployments
demand at once.

My background is in computational cognitive science and cognitive
linguistics, and I've spent years building real-world conversational
systems across several startups.
[More on how I think about the work →](/research/)

## current work

I lead the current work on the [**τ-Bench family**](https://taubench.com) of
agent benchmarks (originally introduced at Sierra in 2024) — code, repo,
public leaderboard, and a sequence of extensions:

- **[τ²-Bench](https://sierra.ai/blog/benchmarking-agents-in-collaborative-real-world-scenarios)** — extends τ-Bench to a *dual-control* setting where both the agent and the user can act on the world.
- **[τ-Knowledge](https://sierra.ai/blog/bench-advancing-agent-benchmarking-to-knowledge-and-voice)** — knowledge-retrieval domain.
- **[τ-Voice](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)** — first benchmark to measure full-duplex voice agents on realistic, grounded customer-service tasks.
- **[τ³-Bench](https://sierra.ai/blog/bench-advancing-agent-benchmarking-to-knowledge-and-voice)** — combines τ-Knowledge and τ-Voice with community-contributed task fixes and code improvements.
