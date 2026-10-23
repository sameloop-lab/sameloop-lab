# Documentation build

Read `index.html` directly after extraction; no server, CDN, fetch request or
Node installation is needed to browse the supplied pages.

For regeneration, install Node.js 20+ and Python 3, then run from repository root:

```bash
npm ci
npm run build
npm run check
```

If Node reports `Cannot find package markdown-it`, run `npm ci` first.
Dependencies are pinned in package-lock.json. Node builds Markdown-it pages and
Graphviz SVGs via @viz-js/viz. The Python checker validates local links and
manifest references; a Node test checks filtering logic without a real browser.

Sources: ordinary Markdown, data/projects.json and assets/sources/*.dot.
Outputs: index.html, site/, assets/diagrammes/, docs/projects.md, docs/diagrams.md.
Do not put node_modules or build caches in the release archive.
