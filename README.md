# personal-site

Source for [victorbarres.github.io](https://victorbarres.github.io) (TBD — not yet deployed).

Built on [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academic personal pages.

## Local dev

```bash
bundle exec jekyll serve --livereload
```

Runs at `http://127.0.0.1:4000/`. Live-reloads on most file edits; `_config.yml` changes need a server restart, or `touch _pages/about.md` to trigger a watcher rebuild.

## Layout

- `_pages/about.md` — landing page (`/`); short bio, current work, news, selected publications.
- `_pages/research.md` — long-form research statement (`/research/`).
- `_pages/publications.md` — `/publications/`, year-grouped list driven by `_bibliography/papers.bib`.
- `_pages/service.md` — currently `nav: false`; re-enable once it has 3+ entries.
- `_pages/cv.md` — `/cv/`, embeds the PDF compiled from `cv-src/barres_cv.tex` (see CV workflow below).
- `_news/` — homepage news bullets. Filenames are numbered most-recent-first
  (`announcement_1.md` = newest), so the filename order mirrors the on-page
  order. When adding a new item, rename the existing files up (shift _1 → _2,
  _2 → _3, …) and drop the new entry into `announcement_1.md`.
- `_bibliography/papers.bib` — all publications. Mark papers with `selected = {true}` to surface them on the homepage. See `_bibliography/README.md` for the curation conventions.
- `_data/socials.yml` — socials shown in the page footer.
- `_config.yml` — site-wide identity and Jekyll plugin config.

## CV / resume

The CV PDF lives at `assets/pdf/barres_cv.pdf` and is the canonical hosted version.
Source: `cv-src/barres_cv.tex` (plain LaTeX, no external class).

To update:

```bash
# Edit cv-src/barres_cv.tex, then:
bin/build_cv.sh
```

Requires MacTeX (xelatex + latexmk). The script rebuilds the PDF and copies it into
`assets/pdf/`. Commit both `cv-src/barres_cv.tex` and the rebuilt
`assets/pdf/barres_cv.pdf`.

## Conventions

- Author name: **Victor Barres** (ASCII) everywhere on the site, even though Google Scholar uses "Victor Barrès".
- τ symbols: clean Unicode (`τ`, `τ²`, `τ³`), not LaTeX `$\tau$`.
- Equal contribution: append `*` to the author name in the bibtex `author` field, and add `annotation = {* Equal contribution.}`.

## Deploy (later)

Not yet pushed to GitHub. When ready:

1. Create a `victorbarres.github.io` repo (or wire a custom domain).
2. Audit `.github/workflows/` — al-folio ships ~17 workflows, most of which are theme-maintenance noise. Keep `deploy.yml` and probably `update-citations.yml`; drop the rest.
3. Run `bin/deploy` (al-folio's deploy script — pushes the built `_site` to a `gh-pages` branch).

## TODOs

Search for `TODO` in the repo for outstanding placeholders. Notable ones:

- `_pages/about.md` — `more_info:` block is empty (optional contact line under the profile picture).
- `_config.yml` — `middle_name` is blank; intentional for now.

The CV page (`/cv/`) embeds the LaTeX-rendered PDF directly and includes a
hand-curated HTML summary above it (for SEO indexability). If you ever want
to switch to the al-folio `layout: cv` for HTML rendering, create a
`_data/cv.yml` in the rendercv schema (see al-folio docs) and change
`_pages/cv.md`'s `layout:` accordingly.
