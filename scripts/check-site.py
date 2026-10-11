#!/usr/bin/env python3
"""Check generated site links and assets without contacting external services."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        for name in ('href', 'src', 'data-filename'):
            if attributes.get(name):
                self.references.append(attributes[name])


def check_site(root):
    failures = []
    pages = sorted(root.rglob('*.html'))
    for page in pages:
        parser = Links()
        parser.feed(page.read_text(encoding='utf-8'))
        relative = page.relative_to(root).as_posix()
        for reference in parser.references:
            if 'ZgotmplZ' in reference:
                failures.append(f'{relative}: malformed URL {reference}')
                continue
            parsed = urlparse(reference)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = urlparse(urljoin('/' + relative, reference)).path
            target = root / unquote(resolved).lstrip('/')
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_file():
                failures.append(f'{relative}: missing destination {reference}')
    return pages, sorted(set(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='Hugo output directory')
    arguments = parser.parse_args()
    if not (arguments.directory / 'index.html').is_file():
        parser.error('directory must contain the generated index.html')
    pages, failures = check_site(arguments.directory)
    for failure in failures:
        print(failure)
    print(f'Checked {len(pages)} HTML pages; {len(failures)} broken local references.')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
