"""Offline source/interaction checks. No network, publication or repository writes.
Run: python3 -m unittest discover -s tests -p 'test_indexing_satellites.py' -v
Node.js is optional; its absence explicitly skips two JavaScript interaction tests.
"""
from collections import Counter
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from urllib.robotparser import RobotFileParser
import json
import shutil
import subprocess
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://asf.surf/'
APPS = ('satellites/swell-checklist/index.html', 'satellites/surf-glossary/index.html')
ARTICLES = ('blog/ocean-safety-rip-currents.html', 'blog/surf-etiquette-lineup-guide.html', 'blog/beginner-surfboard-selection.html')
PAGES = APPS + ARTICLES + ('blog/index.html',)


def page_url(path):
    return ORIGIN + (path[:-10] if path.endswith('index.html') else path)


def file_for(url):
    path = unquote(urlsplit(url).path).lstrip('/')
    candidate = ROOT / (path + 'index.html' if not path or path.endswith('/') else path)
    return candidate


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.canonical, self.hrefs, self.ids, self.scripts = [], [], [], []
        self.meta, self.html_attrs, self.resources = {}, {}, []
        self.h1, self.title, self.text = '', '', []
        self._h1 = self._title = self._style = False
        self._script = None
        self.doctype = False
        self.feed(text)
        self.close()

    def handle_decl(self, decl):
        self.doctype = decl.lower() == 'doctype html'

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] += 1
        if a.get('id'):
            self.ids.append(a['id'])
        if tag == 'html':
            self.html_attrs = a
        if tag == 'meta':
            self.meta[a.get('name', a.get('property', a.get('http-equiv', ''))).lower()] = a.get('content', '')
        if tag == 'link' and 'canonical' in a.get('rel', '').lower().split():
            self.canonical.append(a.get('href', ''))
        if tag == 'a' and a.get('href'):
            self.hrefs.append(a['href'])
        if tag in ('img', 'iframe', 'script') and a.get('src'):
            self.resources.append(a['src'])
        if tag == 'link' and 'stylesheet' in a.get('rel', '').split():
            self.resources.append(a.get('href', ''))
        if tag == 'h1':
            self._h1 = True
        if tag == 'title':
            self._title = True
        if tag == 'style':
            self._style = True
        if tag == 'script':
            self._script = {'type': a.get('type', ''), 'src': a.get('src', ''), 'code': ''}
            self.scripts.append(self._script)

    def handle_endtag(self, tag):
        if tag == 'h1':
            self._h1 = False
        if tag == 'title':
            self._title = False
        if tag == 'style':
            self._style = False
        if tag == 'script':
            self._script = None

    def handle_data(self, data):
        if self._script is not None:
            self._script['code'] += data
        elif not self._style:
            self.text.append(data)
        if self._h1:
            self.h1 += data
        if self._title:
            self.title += data

    def schema(self):
        return [json.loads(s['code']) for s in self.scripts if s['type'] == 'application/ld+json']

    def executable(self):
        return '\\n'.join(s['code'] for s in self.scripts if s['type'] != 'application/ld+json')


@lru_cache(maxsize=None)
def read(path):
    return Page((ROOT / path).read_text(encoding='utf-8'))


class IndexingSatelliteTests(unittest.TestCase):
    def test_semantics_and_unique_metadata(self):
        titles, descriptions = [], []
        for path in PAGES:
            with self.subTest(path=path):
                p = read(path)
                self.assertTrue(p.doctype)
                self.assertEqual(p.html_attrs.get('lang'), 'en')
                for tag in ('html', 'head', 'body', 'main', 'h1', 'title'):
                    self.assertEqual(p.tags[tag], 1, tag)
                self.assertGreater(p.tags['nav'], 0)
                self.assertEqual(len(p.ids), len(set(p.ids)), 'Duplicate ids')
                self.assertTrue(p.title.strip())
                self.assertTrue(p.meta.get('description', '').strip())
                self.assertNotIn('noindex', p.meta.get('robots', '').lower())
                self.assertEqual(p.canonical, [page_url(path)])
                self.assertEqual(p.meta.get('og:url'), page_url(path))
                titles.append(p.title)
                descriptions.append(p.meta['description'])
        self.assertEqual(len(titles), len(set(titles)))
        self.assertEqual(len(descriptions), len(set(descriptions)))

    def test_webapplication_schema(self):
        for path in APPS:
            with self.subTest(path=path):
                p = read(path)
                apps = [s for s in p.schema() if s.get('@type') == 'WebApplication']
                self.assertEqual(len(apps), 1)
                app = apps[0]
                self.assertEqual(app['@context'], 'https://schema.org')
                self.assertEqual(app['url'], page_url(path))
                self.assertEqual(app['@id'], page_url(path) + '#app')
                self.assertEqual(app['name'], p.h1)
                self.assertEqual(app['inLanguage'], 'en')
                self.assertEqual(app['applicationCategory'], 'EducationalApplication')
                self.assertIs(app['isAccessibleForFree'], True)
                self.assertTrue(app['operatingSystem'])
                self.assertNotIn('aggregateRating', app)

    def test_article_schema_and_substantial_text_retained(self):
        for path in ARTICLES:
            with self.subTest(path=path):
                p = read(path)
                articles = [s for s in p.schema() if s.get('@type') == 'Article']
                self.assertEqual(len(articles), 1)
                self.assertEqual(articles[0]['url'], page_url(path))
                self.assertEqual(articles[0]['headline'], p.h1)
                self.assertIs(articles[0]['isAccessibleForFree'], True)
                self.assertGreater(len(' '.join(p.text).split()), 900)

    def test_mutual_static_interlinks(self):
        app_urls = {page_url(p) for p in APPS}
        article_urls = {page_url(p) for p in ARTICLES}
        for path in APPS:
            hrefs = {urljoin(page_url(path), h) for h in read(path).hrefs}
            self.assertTrue(article_urls | {ORIGIN} | (app_urls - {page_url(path)}) <= hrefs, path)
        for path in ARTICLES + ('blog/index.html',):
            hrefs = {urljoin(page_url(path), h) for h in read(path).hrefs}
            self.assertTrue(app_urls <= hrefs, path)
        index_schema = read('blog/index.html').schema()[0]
        parts = {p.get('url') for p in index_schema['hasPart']}
        self.assertTrue(app_urls | article_urls <= parts)

    def test_local_links_and_fragments_resolve(self):
        for path in PAGES:
            for href in read(path).hrefs + read(path).resources:
                url = urljoin(page_url(path), href)
                parsed = urlsplit(url)
                if parsed.scheme not in ('http', 'https') or parsed.netloc != 'asf.surf':
                    continue
                target = file_for(url)
                with self.subTest(path=path, href=href):
                    self.assertTrue(target.is_file(), str(target))
                    if parsed.fragment and target.suffix == '.html':
                        self.assertIn(unquote(parsed.fragment), Page(target.read_text(encoding='utf-8')).ids)

    def test_apps_are_standalone_and_non_tracking(self):
        for path in APPS:
            p = read(path)
            self.assertEqual(p.resources, [])
            self.assertEqual(p.tags['iframe'], 0)
            self.assertGreaterEqual(p.tags['noscript'], 1)
            self.assertGreater(len(p.executable()), 100)
            for forbidden in ('fetch(', 'XMLHttpRequest', 'sendBeacon', 'WebSocket', 'localStorage', 'document.cookie', 'adsbygoogle', 'googletagmanager'):
                self.assertNotIn(forbidden, p.executable())
        self.assertEqual(read(APPS[0]).tags['input'], 11)
        self.assertEqual(read(APPS[1]).tags['dt'], 28)
        self.assertEqual(read(APPS[1]).tags['dd'], 28)
        self.assertIn('not a safety clearance', ' '.join(read(APPS[0]).text).lower())

    def test_sitemap_is_unique_resolved_and_self_canonical(self):
        tree = ET.fromstring((ROOT / 'sitemap.xml').read_text(encoding='utf-8'))
        self.assertEqual(tree.tag, '{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
        urls = [loc.text for loc in tree.findall('{*}url/{*}loc')]
        self.assertEqual(len(urls), len(set(urls)))
        self.assertTrue({page_url(p) for p in PAGES} <= set(urls))
        for url in urls:
            with self.subTest(url=url):
                parsed = urlsplit(url)
                self.assertEqual((parsed.scheme, parsed.netloc, parsed.query, parsed.fragment), ('https', 'asf.surf', '', ''))
                self.assertFalse(parsed.path.endswith('index.html'))
                target = file_for(url)
                self.assertTrue(target.is_file())
                p = Page(target.read_text(encoding='utf-8'))
                self.assertNotIn('noindex', p.meta.get('robots', '').lower())
                self.assertNotIn('refresh', p.meta)
                self.assertEqual(p.canonical, [url])
        self.assertNotIn(ORIGIN + 'previsao-surf/', urls)
        self.assertNotIn(ORIGIN + 'espacos-logo-app.html', urls)

    def test_robots_allows_new_content(self):
        robots = RobotFileParser()
        robots.parse((ROOT / 'robots.txt').read_text(encoding='utf-8').splitlines())
        for path in PAGES:
            self.assertTrue(robots.can_fetch('Googlebot', page_url(path)), path)

    def test_intentional_noindex_protections_remain(self):
        for path in ('404.html', 'emitir.html', 'recuperar-carteirinha.html', 'carteirinhas-admin.html'):
            self.assertIn('noindex', read(path).meta.get('robots', '').lower(), path)

    def test_release_guide_exists(self):
        text = (ROOT / 'INDEXING_AND_SATELLITE_GUIDE.md').read_text(encoding='utf-8')
        for required in ('Google Search Console', 'not deployed', 'Pages', 'Actions', 'robots.txt', 'URL Inspection'):
            self.assertIn(required, text)

    def run_node(self, script):
        result = subprocess.run(['node', '-e', script], capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which('node'), 'Node.js unavailable: checklist interaction test skipped')
    def test_checklist_interactions_do_not_issue_clearance(self):
        template = r"""
const vm=require('node:vm'),assert=require('node:assert/strict');
const reviews=Array.from({length:8},()=>({checked:false}));
const hazards=Array.from({length:3},()=>({checked:false}));
const events={};const status={textContent:''};const progress={};
const form={querySelectorAll:q=>q.includes('review')?reviews:hazards,addEventListener:(event,fn)=>{events[event]=fn;}};
const elements={'readiness-form':form,'review-status':status,'review-progress':progress};
vm.runInNewContext(__SCRIPT__,{document:{getElementById:id=>elements[id]},setTimeout:fn=>fn()});
assert.match(status.textContent,/Reviewed 0 of 8/);assert.equal(progress.value,0);
reviews.forEach(i=>{i.checked=true;});events.change();
assert.match(status.textContent,/does not establish safe conditions/);assert.equal(progress.value,8);
hazards[1].checked=true;events.change();assert.match(status.textContent,/Postpone/);
reviews.concat(hazards).forEach(i=>{i.checked=false;});events.reset();
assert.match(status.textContent,/Reviewed 0 of 8/);assert.equal(progress.value,0);
"""
        self.run_node(template.replace('__SCRIPT__', json.dumps(read(APPS[0]).executable())))

    @unittest.skipUnless(shutil.which('node'), 'Node.js unavailable: glossary interaction test skipped')
    def test_glossary_search_accents_empty_results_and_reset(self):
        template = r"""
const vm=require('node:vm'),assert=require('node:assert/strict');
const inputEvents={},buttonEvents={};let focused=false;
const input={value:'',addEventListener:(e,f)=>{inputEvents[e]=f;},focus:()=>{focused=true;}};
const items=[{textContent:'Tide changing sea level',dataset:{keywords:'mare high low'},hidden:false},{textContent:'Swell organised waves',dataset:{keywords:'ondulacao'},hidden:false},{textContent:'Wave period seconds',dataset:{keywords:'periodo'},hidden:false}];
const count={textContent:''},empty={hidden:true};
const button={addEventListener:(e,f)=>{buttonEvents[e]=f;}};
const elements={'term-search':input,'result-count':count,'no-results':empty,'clear-search':button};
vm.runInNewContext(__SCRIPT__,{document:{getElementById:id=>elements[id],querySelectorAll:()=>items}});
assert.equal(count.textContent,'3 of 3 terms shown');
input.value='MARÉ';inputEvents.input();assert.equal(count.textContent,'1 of 3 terms shown');assert.equal(items[0].hidden,false);
input.value='<script>';inputEvents.input();assert.equal(count.textContent,'0 of 3 terms shown');assert.equal(empty.hidden,false);
buttonEvents.click();assert.equal(count.textContent,'3 of 3 terms shown');assert.equal(input.value,'');assert.equal(empty.hidden,true);assert.equal(focused,true);
"""
        self.run_node(template.replace('__SCRIPT__', json.dumps(read(APPS[1]).executable())))


if __name__ == '__main__':
    unittest.main(verbosity=2)
