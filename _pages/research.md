---
layout: page
title: research
permalink: /research/
description: how I think about the work, and the threads that run through it.
nav: true
nav_order: 2
---

<figure class="hero-banner" role="presentation" aria-hidden="true">
  <img
    class="hero-banner__light"
    src="{{ '/assets/img/phrenology_banner.jpg' | relative_url }}"
    alt=""
    loading="eager"
    decoding="async"
    width="1600"
    height="625"
  >
  <img
    class="hero-banner__dark"
    src="{{ '/assets/img/phrenology_banner_dark.png' | relative_url }}"
    alt=""
    loading="eager"
    decoding="async"
    width="1600"
    height="625"
  >
</figure>

I'm a researcher at [Sierra](https://sierra.ai), where I build and study
**conversational AI agents** and the benchmarks that tell us when they
actually work — the τ-Bench family (live leaderboard at
[taubench.com](https://taubench.com)). My focus is on agents that must
execute complex tool-using tasks while sustaining long, coherent
conversational interactions — the two things real-world deployments
demand at once, and the source of most of what's hard about deploying
language models in customer-facing settings.

I came up through **computational cognitive science**, studying how humans
use language as part of the continuous action–perception cycles that ground
them in their environment. That work is rooted in **cognitive linguistics**
— the view of language as an *activity*, embodied and situated, rather than
a disembodied symbol system — and that lens still shapes how I think about
agents today. Since then I've spent years building conversational systems
deployed in the real world across several startups. My research view is
shaped by that practice: the minutiae of everyday interaction — the
ecological details of real systems in real deployments — are where the
whole-system challenges actually surface. You don't see them from the top
down; you see them from the inside.

A tension I keep coming back to, and another thread I've worked on
throughout, is **the place of structure in language and cognition**.
Humans don't just associate — they reason over concepts, need guarantees,
organize knowledge. Cognitive science taught me to take that seriously,
and it's part of why **neuro-symbolic systems** have run through my work
for years: how do we let language models do what they do well while still
honoring the kinds of structured, accountable reasoning that real
understanding seems to require? I don't have a clean answer. The latest
iteration of this thread is
[*From Generating Answers to Building Explanations*](https://aclanthology.org/2025.naacl-industry.42/),
from my time at Elemental Cognition.

A third thing cognitive science taught me, and one I think the field of AI
underweights: cognitive systems are **systems of systems**, organized for
**maintenance and resilience** as much as for performance. An intelligent
system isn't a clever algorithm — it's something that exists through time,
adapts to its environment, and keeps learning from it. I've found, perhaps
surprisingly, that modern MLOps is one of the clearest illustrations of
this: what *learns*, in any production setting, isn't a model on its own;
it's the whole pipeline of data, evaluation, deployment, monitoring, and
iteration around it. And in fact it doesn't stop at the pipeline — the
real "learning system" is the whole organization around it: the people
gathering requirements, the QA teams catching regressions, support and
ops closing the loop with users. Maintenance is the substrate of
intelligence, not an afterthought, and it is irreducibly sociotechnical.

The throughline is *verum factum*: **we know what we make**. Theories of
language, cognition, and intelligence are most trustworthy when you can
build them, run them, maintain them, and watch them fail in informative
ways. Benchmarks are the same idea pointed at agents — a discipline for
being honest about what these systems can and can't do.

<!-- TODO (optional): closing line on what you're interested in collaborating on, or how to reach you. -->
