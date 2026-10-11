# YouTube Video Content Update Plan

**Goal:** Update the existing video gallery from the Cyberbotics Lab channel identified by the owner's supplied video link, after completing publication synchronization.

**Architecture:** Match channel uploads to existing bundles by YouTube video ID. Preserve existing gallery URLs and historical videos, add missing channel uploads with their original thumbnails and verified upload timestamps, and connect matching paper/video records.

**Tech stack:** Hugo extended 0.115.4, Wowchemy portfolio block, Markdown/YAML, existing YouTube shortcode.

**Spec:** The owner's October 10, 2026 request; https://www.youtube.com/watch?v=V_tpiH_t2Hc; channel `UCqZ799nQtfhGVshr4IaOjEA` (`@cyberboticslab3194`).

## Constraints and review focus

- Reuse the current gallery and video-page structure; this is content maintenance.
- Match video IDs, rather than titles alone, to avoid duplicate pages for the same clip. Different uploads of a study may have separate video pages.
- Use exact channel/feed/watch metadata for titles, source URLs and upload timestamps; do not infer hardware results or unspecified paper associations.
- Preserve existing URLs, archived images and videos outside this channel.
- Use the channel's own original thumbnails; do not download video files.
- Link papers only where the source title/record establishes the match. Remove the ALIP page's unrelated whole-body task-space control clip.
- Do not query Google Scholar, commit, push or publish.

## Task 1: Refresh channel videos and related links

- [x] Archive the channel catalog and compare its eighteen upload IDs with the six existing video bundles.
- [x] Add fourteen missing uploads, retain the four existing channel pages and two historical pages, and synchronize upload dates/source links.
- [x] Add related-paper links and recent paper video links; correct the navigation paper's channel video and remove the unrelated ALIP embed.
- [x] Record provenance and verify unique IDs, expected gallery membership, timestamps, thumbnail resources and preserved URLs/assets.
- [x] Run the pinned production build, local link/whitespace checks, and inspect the gallery and a latest embedded video at desktop and phone widths.

The owner's request authorizes local implementation in this checkout for inspection.
