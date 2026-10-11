# Recent Publication Synchronization Plan

**Goal:** Reconcile the twelve papers in the owner's `ref.bib` export with the local website, focusing on 2024 onward.

**Architecture:** Match normalized titles to existing publication bundles and retain every existing URL and archived asset. Copy each supplied BibTeX entry exactly into its bundle; synchronize page metadata and add a bundle only for a missing paper.

**Tech stack:** Hugo extended 0.115.4, Wowchemy, Markdown/YAML, BibTeX.

**Spec:** The owner's October 10, 2026 request and `/Users/hereid.1/Downloads/ref.bib`.

## Constraints and review focus

- Use the supplied export without querying Google Scholar.
- Preserve unrelated changes, established slugs, PDFs, videos, project links, and older publications.
- Keep separately sourced resource links and publication-status notes on the pages; citation files reproduce the export without added fields.
- Use `publication_year` for sorting/filtering when the final year differs from the original deposit date. Do not invent publication days.
- Preserve author order and correct names against the supplied records, including the accented name in the ALIP paper.
- Do not commit, push, or publish. This is local content maintenance; no new software behavior or unit tests are needed.

## Task 1: Reconcile citations and publication pages

- [x] Compare all twelve records and save the source checksum and key-to-slug mapping.
- [x] Update matching citation/page metadata; add the missing Peng 2025 navigation preprint and promote the existing terrain-aware paper to its 2026 journal record.
- [x] Record source provenance and deliberate retention of previously verified page links/status.
- [x] Verify one page per supplied title, exact citation contents, author order, year/type filters, stable URLs, and unchanged archived assets.
- [x] Run the pinned production build, local link check, and whitespace check; inspect the publications list and Cite dialog in the local preview.

Execution is authorized by the owner's request to update the local publications. The work proceeds in this checkout for inspection.
