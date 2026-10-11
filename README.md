# Cyberbotics Lab website

The lab website uses Hugo and the pinned Wowchemy v5 module. Content lives in this repository; deployment uses `.github/workflows/hugo.yml`.

## Local preview

Use **Hugo extended 0.115.4**, matching the workflow. A newer system Hugo can fail with this theme's legacy template functions. Obtain the matching extended binary from the [official release](https://github.com/gohugoio/hugo/releases/tag/v0.115.4) and put it on your PATH, or invoke its absolute path.

```sh
hugo version
HUGO_MODULE_PROXY=https://proxy.golang.org hugo server --environment production --noHTTPCache --bind 127.0.0.1 --port 1313 --baseURL http://localhost:1313/ --disableFastRender
```

Open <http://localhost:1313/>. Go is needed for the first module download. Stop the server with Ctrl+C.

The production environment gives stylesheets content-based filenames, so a palette change cannot reuse a cached `wowchemy.css`. `--noHTTPCache` also prevents stale preview responses while editing. Live reload remains enabled.

## Validate a change

```sh
HUGO_MODULE_PROXY=https://proxy.golang.org hugo --gc --minify
python3 scripts/check-site.py public
python3 scripts/check-page-features.py public
git diff --check
```

The checks use Python's standard library. The link check covers generated local links, images, PDFs, citation-file references, and malformed Hugo URLs. The feature check covers optional script loading, publication labels and records without JavaScript, People links, and article resource controls. They do not check remote services or every accessibility criterion. Inspect the homepage and changed pages at desktop, tablet, and phone widths; test the mobile menu, search, combined publication filters, empty results/reset, and Cite dialog. Use a fresh output directory when checking removed pages or optional modules, since Hugo may leave old generated files in a reused directory.

## Content ownership and maintenance

- `data/lab.yaml` selects homepage demonstrations, research areas, and publications. `layouts/partials/lab/` renders those selections. `assets/scss/template.scss` owns the local visual style.
- `data/lab.yaml` also owns the shared Cyber Suite description, release status, platform overview, and capability cards. `/cyber-suite/` uses `layouts/lab-platform/single.html`; the homepage feature, Resources entry, and footer link lead there. Keep release availability aligned with the owner's instructions. The current copy announces an actively developed platform whose repository is not public yet; it promises no release date, license, access, hardware qualification, or performance result.
- Project bundles use `display_title` for concise visible headings, `overview` for the introduction, and `method_steps` for the three-step explanation. `hero_image_page` and `hero_video` connect a project to an existing demonstration. `method_figure: true` keeps the original featured framework figure in an expandable section. `resource_anchor` must match a heading ID on that page. The shared project template retains related papers, news, talks, and citations.
- Video detail pages retain exact source titles and dates. `card_title` supplies the gallery heading; `video_topics` uses `locomotion`, `navigation`, `control-safety`, or `exoskeletons` (multiple topics are allowed). The `lab-videos` block renders the full dated archive; its fingerprinted native script enhances it with topic buttons and a result count. All videos remain visible without JavaScript.
- Palette A uses brick red (`#A43B3B`), warm charcoal (`#302B29`), and ivory (`#FAF8F5`). `data/themes/lab_brick.toml` supplies the shared theme colors; the local Sass supplies supporting neutrals. `layouts/partials/functions/get_logo.html` wraps the original `assets/media/logo.png` in an SVG color filter after Hugo's normal resizing, preserving its artwork and transparency. Keep the source logo intact when adjusting the palette.
- Browser, Apple touch, and manifest icons use `assets/media/icon-brick.png` through the local `layouts/partials/functions/get_icon.html` override. Its editable color filter is `assets/media/icon-brick.svg`, which retains the original `assets/media/icon.png` artwork and transparency. After adjusting the filter, regenerate the PNG with `rsvg-convert assets/media/icon-brick.svg -o assets/media/icon-brick.png`; Hugo resizes it and gives each generated icon a content-based URL.
- Existing project and publication bundles keep their URLs. Add a new bundle only for a new paper or project. Preserve historical PDFs and images.
- `layouts/section/publication.html` groups the publication archive by verified year. Its fingerprinted `assets/js/lab-publications.js` enhances all server-rendered records with combined title/author/venue search, year/type filtering, a live count, and reset. Search folds accents, and records can match any assigned publication type. Saved numeric type links such as `/publication/#2` still select their type; reset clears that fragment. Controls stay hidden without JavaScript; all papers and resource links remain readable.
- `/people/` uses the `lab-people` block and shared person-card/link partials. Membership, role, interests, portrait, and social links come from existing author records. Empty groups are omitted. Missing portraits use initials, and alumni have compact cards. Do not infer missing interests or add current affiliations from old bios.
- Publication and news detail templates use `lab/article-header.html`, the established metadata/resource partials, and the theme's page footer. Featured images fit within the article rather than being cropped. Keep `date_precision` and `publication_year` semantics when adjusting these templates.
- Math rendering is per-page: set `math: true` when adding equations. Interactive maps are disabled until a page actually needs one. The unused Netlify CMS import and admin output are disabled; content is maintained in Git and deployment uses GitHub Pages. To restore CMS, enable its import/configuration and restore the admin page's `wowchemycms_config` output and build settings together. Keep search, citation, menu, and gallery dependencies available to their consumers.
- Use a project's problem, approach, demonstrated results and conditions, and resources to explain the research. State whether evidence comes from simulation, hardware, or human-participant experiments. Link the supporting paper; avoid unsupported clinical, deployment, safety, or performance claims.
- Confirm paper title, author order, venue, year, DOI, and BibTeX against primary records. `publication_year` can record a verified year when the source provides no exact publication date. The publication filter and metadata overrides honor this field. Keep the original deposit date when appropriate.
- Explicit `url_pdf` values point to the current manuscript. The local `page_links.html` override prioritizes this value while retaining archived PDFs at their existing URLs. Publications without `url_pdf` retain the theme's local-PDF behavior.
- Update `lastmod` only for an actual page edit. Date news by the event or source announcement, and identify author-reported acceptance when a final proceedings record is unavailable. If only the month or year is known, set `date_precision: month` or `year` and use the first day of that period in `date` as a sort key; the news templates display only the known precision. Do not use a DOI creation date as an acceptance or publication date.
- Verify role and membership changes directly before editing People. Describe recruiting pathways without inventing openings or funding. Link official admissions information instead of copying changing deadlines.
- Before replacing a pinned module or Hugo version, compare the local `page_links`, `page_metadata`, and publication-section overrides with the new theme and retest citations, metadata, and filters.

Refresh recent publications, news, people, and contact pathways each semester. Claim-specific sources for the October 2026 refresh are recorded in [docs/content-sources.md](docs/content-sources.md). Review and publishing are separate steps; a local build does not publish the website.
