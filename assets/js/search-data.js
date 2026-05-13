// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "in reverse chronological order. * denotes equal contribution.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "current as of May 2026.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-τ-bench-released-a-benchmark-for-evaluating-conversational-agents-in-a-dual-control-environment-where-both-the-agent-and-the-user-can-take-actions-on-the-world",
          title: 'τ²-Bench released — a benchmark for evaluating conversational agents in a dual-control environment,...',
          description: "",
          section: "News",},{id: "news-organizing-and-judging-the-sierra-τ-bench-custom-track-of-the-agentx-agentbeats-competition-berkeley-rdi-fall-2025-spring-2026",
          title: 'Organizing and judging the Sierra τ²-Bench Custom Track of the AgentX–AgentBeats Competition (Berkeley...',
          description: "",
          section: "News",},{id: "news-τ-bench-released-extending-τ-bench-with-a-knowledge-retrieval-domain-τ-knowledge-full-duplex-voice-evaluation-τ-voice-and-community-contributed-task-fixes-live-leaderboard-at-taubench-com",
          title: 'τ³-Bench released — extending τ-Bench with a knowledge-retrieval domain (τ-Knowledge), full-duplex voice evaluation...',
          description: "",
          section: "News",},{id: "news-μ-bench-released-an-open-multilingual-transcription-benchmark-covering-5-locales-5-asr-providers-and-4-270-human-annotated-utterances-from-real-customer-calls",
          title: 'μ-Bench released — an open multilingual transcription benchmark covering 5 locales, 5 ASR...',
          description: "",
          section: "News",},{id: "news-τ-voice-first-benchmark-to-measure-full-duplex-voice-agents-on-realistic-grounded-customer-service-tasks-voice-agents-have-closed-most-of-the-gap-to-non-reasoning-text-models-in-8-months",
          title: 'τ-Voice — first benchmark to measure full-duplex voice agents on realistic, grounded customer-service...',
          description: "",
          section: "News",},{id: "news-three-τ-bench-family-papers-accepted-to-icml-2026-including-τ-bench-as-a-spotlight-τ-bench-dual-control-evaluation-τ-knowledge-knowledge-retrieval-and-τ-voice-full-duplex-voice-agents-see-you-in-july",
          title: 'Three τ-Bench family papers accepted to ICML 2026 — including τ²-Bench as a...',
          description: "",
          section: "News",},{id: "news-new-blog-post-τ-knowledge-benchmarking-agents-on-realistic-knowledge-frontier-has-moved-from-25-5-37-4-pass-1-since-the-march-release-with-63-pp-of-headroom-still-left-includes-a-behavioral-analysis-of-what-separates-the-strong-agents-from-the-rest",
          title: 'New blog post — τ-Knowledge: benchmarking agents on realistic knowledge. Frontier has moved...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%76%69%63%74%6F%72.%62%61%72%72%65%73@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/victorbarres", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=RpPIx5AAAAAJ", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/victor-barres", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/VBarres86633", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
