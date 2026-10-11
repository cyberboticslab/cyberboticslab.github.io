#!/usr/bin/env python3
"""Check the built site's progressive enhancements and optional asset loading."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.in_article_header = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'header' and attrs.get('class') == 'lab-article-header':
            self.in_article_header = True
        if self.in_article_header:
            attrs['_article_header'] = 'true'
        self.elements.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag == 'header':
            self.in_article_header = False

    def find(self, tag=None, **attrs):
        return [a for t, a in self.elements if (not tag or t == tag)
                and all(k in a and (v is None or a[k] == v) for k, v in attrs.items())]


BUILD = Path(sys.argv.pop(1)).resolve()


class SiteFeatures(unittest.TestCase):
    def page(self, relative):
        return Page(BUILD / relative / 'index.html')

    def test_shared_pages_load_only_used_features(self):
        for path in ('', 'people', 'publication', 'cyber-suite'):
            with self.subTest(page=path):
                page = self.page(path)
                scripts = ' '.join(a.get('src', '') for a in page.find('script')).lower()
                for unused in ('mathjax', 'leaflet', 'wowchemy-map', 'netlify-identity'):
                    self.assertNotIn(unused, scripts)
                self.assertIn('wowchemy-publication', scripts)  # Citation modal remains shared.
                self.assertNotIn('leaflet', ' '.join(a.get('href', '') for a in page.find('link')))

    def test_archive_has_labels_and_all_records_without_javascript(self):
        page = self.page('publication')
        labels = {a.get('for') for a in page.find('label')}
        self.assertTrue({'lab-paper-search', 'lab-paper-year', 'lab-paper-type'} <= labels)
        records = page.find(**{'data-publication': None})
        source_count = len(list((Path(__file__).resolve().parents[1] / 'content/publication').glob('*/index.md')))
        self.assertEqual(len(records), source_count)
        self.assertTrue(all('hidden' not in a for a in records))
        self.assertTrue(page.find(**{'data-publication-controls': None, 'hidden': None}))
        self.assertTrue(page.find(role='status', **{'aria-live': 'polite'}))
        self.assertTrue(page.find('button', **{'data-publication-reset': None, 'type': 'button'}))
        scripts = ' '.join(a.get('src', '') for a in page.find('script'))
        self.assertNotIn('isotope', scripts)
        self.assertNotIn('imagesloaded', scripts.lower())

    def test_people_preserves_known_groups_and_profile_links(self):
        page = self.page('people')
        for group in ('principal-investigator', 'graduate-students', 'alumni'):
            self.assertTrue(page.find(id=group), group)
        links = {a.get('href') for a in page.find('a')}
        for slug in ('suaib-al-mahmud', 'upama-pant', 'sunny-agrawal', 'victor-paredes'):
            self.assertIn('/author/' + slug + '/', links)
        self.assertTrue(page.find('a', href='mailto:almahmud.2@osu.edu', **{'aria-label': None}))
        self.assertTrue(page.find('a', href='https://gitlab.com/SeanStar13', **{'aria-label': 'GitLab for Sean Starrett'}))
        self.assertFalse(page.find('ul', **{'aria-hidden': 'true', 'class': 'lab-person-links'}))

    def test_publication_and_news_have_article_headers(self):
        publication = self.page('publication/xiang-2026-perceptive')
        news = self.page('post/26-07-upama-ms')
        for page in (publication, news):
            self.assertTrue(page.find('header', **{'class': 'lab-article-header'}))
            self.assertEqual(len(page.find('h1', _article_header='true')), 1)
        self.assertTrue(publication.find('a', **{'class': 'btn btn-outline-primary btn-page-header js-cite-modal'}))


if __name__ == '__main__':
    unittest.main()
