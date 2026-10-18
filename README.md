# NPP Caprica 2072

A static, photo-led campaign website for the New Progressive Party, a fictional centre-left liberal party in opposition during 2068–2072.

Live site: https://manualalan.github.io/npp-caprica-2072/

The repository and website address use the 2072 campaign year. Current campaign content is for 2072. The original manifesto and Klinton Arkas speeches remain explicitly identified as 2068 archive material.

## Edit and preview

- Campaign copy and page templates: `scripts/build_site.py`
- Shared styling and browser interactions: `dist/styles.css`, `dist/app.js`
- Photography and source ledger: `dist/assets/2072/`
- Historical candidate page: `dist/klinton-arkas/`

Run `python3 scripts/build_site.py` after changing campaign copy or photo credits. Preview with `python3 -m http.server 3072 --directory dist`.

The generator uses only Python's standard library. The website requires no package installation or external fonts. Mobile navigation and programme disclosures use native HTML; JavaScript enhances deep links and sharing.

## Publication

Push to `main`. The existing GitHub Actions workflow publishes `dist/` to GitHub Pages. Confirm the deployment succeeds and check the live pages before reporting publication complete.

Do not relabel the archived 2068 PDF as a 2072 document or present proposed policies as achievements during the opposition term.
