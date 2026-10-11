# Lab template refinement

Approved scope: continue the proposed focused pass in this local checkout for inspection.

## Design and constraints

Keep Hugo 0.115.4, the pinned Wowchemy module, palette A, approved homepage copy, and the Cyber Suite feature. Preserve publication/project/profile URLs and all research, author, and BibTeX records. Use existing profile fields for People; omit unknown interests and do not infer alumni destinations. No commit, push, or publication.

## Implementation

- [x] Disable site-wide math and unused maps; retain per-page `math: true`. Disable the unused Netlify CMS import and identity integration without changing the theme or publishing workflow.
- [x] Replace the publication archive's Isotope enhancement with native combined search/year/type filtering, labeled controls, live count, reset, and an empty state. Keep all records visible in server-rendered HTML without JavaScript. Honor verified publication years and all assigned types.
- [x] Add a lab People block with a featured PI, student cards using existing interests, initials for missing portraits, accessible social links, group navigation, and compact alumni cards.
- [x] Add shared publication/news article headers, readable content widths, preserved abstract/resource/metadata/footer behavior, and contained featured images.
- [x] Build, run local-reference and feature checks, verify real browser interactions and desktop/mobile layouts, and obtain one fresh review of this pass.

## Verification

`scripts/check-page-features.py BUILD_DIR` checks optional asset loading, archive labels/no-JavaScript records, People/profile links, and article resources. Browser checks cover combined filters, author search, empty state/reset, keyboard interaction, citations, global search, and mobile navigation. Run the existing `scripts/check-site.py` and `git diff --check`; compare SHA-256 file snapshots to isolate this pass from existing edits.

## Execution notes

Use the current checkout as requested for local inspection; preserve its existing changes. Configuration and visual edits get build/render checks rather than implementation-mirroring unit tests. Browser behavior is checked with the actual site. Source scan found no active math expressions or interactive map blocks. Keep the theme's shared search, menu, citation, and gallery support.

## Results

- Hugo extended 0.115.4 production build: 452 Hugo pages; fresh output has 376 HTML files, with zero broken local references. All four page feature checks pass; whitespace check passes.
- Real browser: all 54 papers initially visible; combined 2024/conference/Paredes search gives two results; 2026/journal gives one; 2026/preprint gives two, including the paper with multiple types. Accent-insensitive author search, empty results, keyboard reset/focus, Cite modal/BibTeX, global search, and mobile navigation pass.
- Layouts inspected at desktop 1280 x 720, tablet 820 x 1000, and phone 390 x 844. People uses four student columns on desktop, two on tablet, one on phone. Article titles/resource controls remain readable. Preview screenshots are in the parent workspace's `materials/website/previews/` directory.
- Fresh independent review found no major issues or removed publication/news resource links. Its two minor findings were corrected and verified: saved numeric publication-type links initialize their filter, and Sean's existing GitLab destination receives the proper visible label, icon, and accessible name. `/publication/#2` now shows 11 journal papers; keyboard reset restores 54 and clears the fragment.
- Source author, publication, BibTeX, project, video, and news records were preserved. The existing local preview continues at `http://localhost:1313/`. No commit, push, or publication.
