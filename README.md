# From Uploads to Impact: Improving Discovery with a CNG Default

**Brad Andrick · Earth Genome**

CNG Forum lightning talk — **Thu Oct 8, 2026**, **3:19–3:26 PM MDT**, **Ballroom 1**.

Built from the [CNG Quarto/Reveal.js template](https://github.com/cloudnativegeo/lightning-talk-quarto-TEMPLATE). Slides auto-advance every 15 seconds during rehearsal (turn off with `?autoSlide=0` while editing).

**Published deck:** [https://earth-genome.github.io/eg-cng-talk-2026/](https://earth-genome.github.io/eg-cng-talk-2026/)

## Session abstract

In cloud-native geospatial we often focus on large-scale, even global datasets. In practice, discovery for many practitioners starts with data they already own—often at a more local scope. This talk covers **user-uploaded reference layers**, why **PMTiles** was our team’s default, and how cloud-native standards let us ship a simple, high-value feature instead of a heavier traditional upload architecture.

## Edit slides

- Main content: `index.qmd`
- Push to `main` → GitHub Actions renders and updates GitHub Pages

## Local preview

Use Quarto’s **preview server** (it watches `index.qmd`, `custom.scss`, `animations.html`, and `images/`, then reloads the browser). Opening `docs/index.html` directly will **not** hot refresh.

```bash
uv sync
./scripts/preview.sh
```

`preview.sh` runs a small Python watcher so edits to **`custom.scss`** (and images) trigger a re-render.

Open **http://127.0.0.1:4200/** in **Chrome or Safari** and leave that tab open. Do not open `docs/index.html` directly.

After each save you should see **`pandoc`** in the terminal, then the browser reloads within ~1–2 seconds.

While writing, use `?autoSlide=0`, e.g. `http://127.0.0.1:4200/?autoSlide=0#/slide-01`.
