# Research Presentation Implementation Plan

> **For agentic workers:** Implement the three approved tasks in this local checkout and verify each in the generated site. Keep progress here.

**Goal:** Feature recent demonstrations, explain projects more clearly, and make the twenty-video archive easier to browse.

**Architecture:** Keep the existing Hugo/Wowchemy site and stable bundles. Use shared project and video partials, the existing image pipeline, and a small progressively enhanced topic filter. Public-facing method overviews are editorial explanations, not new experimental claims.

**Tech Stack:** Hugo extended 0.115.4, Go templates, Markdown/YAML, Sass, browser-native JavaScript.

**Spec:** The first three recommendations in the October 10 conversation, approved by the owner with “Ok, do these three”.

## Global Constraints

- Work in the current locally refreshed repository so the existing preview contains the result.
- Preserve the logo, palette, hero statement, project/publication/video slugs, BibTeX, original images and PDFs.
- Separate the new October 2026 videos from what the linked manuscripts report; no new performance, clinical, deployment or general safety claims.
- Keep all twenty videos and their exact technical detail-page titles and source timestamps.
- No commit, push, publishing, Google Scholar request, dependency upgrade, or unrelated People/Resources/SEO/CI changes.
- Use build/link verification and browser behavior checks; no unit tests for editorial or style changes.

## Review Focus

- Filtering must show each matching video once, retain date order, and restore all twenty.
- A video with multiple topics must appear in each relevant filter.
- Keyboard activation, selected states, and result counts must remain understandable.
- All videos must remain browsable when JavaScript is unavailable.
- Desktop, tablet and phone layouts must avoid overflow; resource and citation links must remain intact.

### Task 1: Homepage demonstrations

**Files:** `data/lab.yaml`, `layouts/partials/lab/home.html`, shared demonstration styles.

- [x] Replace the three featured selections with perceptive footstep planning, dynamic-subgoal navigation, and model-informed safe learning.
- [x] Use source thumbnails, short titles, 2026 video dates, and method descriptions with supported experimental context.
- [x] Retain local video, publication and research links and add a route to the historical exoskeleton demonstrations.
- [x] Verify the three selections and destinations in generated HTML and the local browser.

### Task 2: Project stories

**Files:** seven `content/project/*/index.md` bundles, `layouts/project/single.html`, `layouts/partials/lab/project-header.html`, project grid styles.

- [x] Give each page a short heading, two-sentence introduction, and three-step method overview.
- [x] Use existing demonstrations as entry images where available; keep detailed original framework figures in an expandable section.
- [x] Refresh curated paper/video links, including the TCST 2026 status, and retain precise experimental settings.
- [x] Preserve the theme's related publication/news/talk lists and existing citation behavior.
- [x] Verify all seven old URLs, resource anchors, technical figures, and mobile presentation.

### Task 3: Video discovery

**Files:** `content/videos.md`, twenty video metadata files, `layouts/partials/blocks/lab-videos.html`, `assets/js/lab-videos.js`, gallery styles.

- [x] Add short `card_title` and `video_topics` metadata without changing detail-page titles or source dates.
- [x] Render twenty dated cards with Locomotion, Navigation, Control & Safety, and Exoskeletons buttons.
- [x] Keep controls hidden until JavaScript is ready; all cards are server-rendered and visible by default.
- [x] Filter with native buttons, `aria-pressed`, a live result count, and the HTML `hidden` attribute.
- [x] Verify all filters, a multiple-topic video, keyboard activation, reset, no-JavaScript output and responsive layouts.

## Final Verification

- [x] Build with pinned Hugo; run `scripts/check-site.py` and `git diff --check`.
- [x] Compare the baseline hashes: original assets, bibliography and unrelated content must remain unchanged.
- [x] Review the scoped change and save desktop/phone screenshots for inspection.
- [x] Leave the local preview open and report the concrete changes and checks.

## Execution Notes

The owner's instruction authorizes implementation of the presented design. This plan records that work without introducing another approval step. Local inspection is the delivery boundary; commits and publishing require a separate owner instruction.

## Verification Record — October 10, 2026

- Hugo extended 0.115.4 production build succeeded: 453 pages, 21 paginator pages, 215 non-page files and 296 processed images. Output: `/private/tmp/cyberbotics-research-refresh-20261010`.
- `python3 scripts/check-site.py /private/tmp/cyberbotics-research-refresh-20261010`: 376 HTML files checked, zero broken local references.
- All seven project resource anchors resolve. Four original method figures remain in expandable sections; detail-page citation modal opens with the expected bibliography.
- All twenty exact video detail-page headings and source dates retained. Server-rendered gallery contains all twenty visible cards; filter controls remain hidden until the script initializes.
- Desktop filter counts: Locomotion 11, Navigation 5, Control & Safety 10, Exoskeletons 2. Categories overlap. All videos restores twenty. Enter and Space activation checked; Navigation filter also checked at phone width.
- Phone viewport 390 × 844: gallery, homepage demonstrations and all seven project pages fit without horizontal overflow. Project images load and each page has three method steps. Tablet viewport 820 × 1000: two-column gallery and project introduction fit without overflow. Desktop viewport reset after testing.
- Fresh independent read-only code review found no material issues. Review covered content attribution, templates, resource anchors, bibliography retention, progressively enhanced filtering and scope preservation.
- Baseline hashes verified for all 435 original files. Changes are limited to the approved presentation content, templates, styles and supporting documentation; no original files missing.
- Desktop and phone screenshots saved under `materials/website/previews/` in the parent workspace, using the `2026-10-10-*` filenames. Homepage demonstrations left open as the local browser deliverable.
- Changes remain local and uncommitted.
