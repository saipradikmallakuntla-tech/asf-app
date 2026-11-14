# Indexing and satellite mini-app guide

Prepared 14 November 2026 for `saipradikmallakuntla-tech/asf-app`, branch `seo-indexing-hub`.

## Deployment boundary

**These additions are not deployed.** They exist only in the fork's feature branch. Neither `main` branch is merged or modified by this addition; upstream is not changed. GitHub Pages and GitHub Actions remain disabled in the fork. No Search Console submission, DNS change or publication is performed.

`https://asf.surf/` is the intended production origin inherited from the project, not proof that the connected GitHub user owns that domain. Production publication, branding/reuse permission, editorial approval and domain verification require the authorised site owner. Do not enable Pages or reuse the production CNAME merely to preview this branch.

## URL and interlinking map

| Resource | Intended self-canonical URL | Static outbound education links |
| --- | --- | --- |
| Hub | `https://asf.surf/` | Existing learning, catalogue and community routes |
| Blog index | `https://asf.surf/blog/` | All three articles, both apps, hub |
| Ocean safety | `https://asf.surf/blog/ocean-safety-rip-currents.html` | Both apps, related articles, hub |
| Surf etiquette | `https://asf.surf/blog/surf-etiquette-lineup-guide.html` | Both apps, related articles, hub |
| Board selection | `https://asf.surf/blog/beginner-surfboard-selection.html` | Both apps, related articles, hub |
| Swell checklist | `https://asf.surf/satellites/swell-checklist/` | Glossary, all three articles, blog index, hub |
| Surf glossary | `https://asf.surf/satellites/surf-glossary/` | Checklist, all three articles, blog index, hub |

The blog is also linked from existing branch pages including Diary, board selection, Apps em Destaque and Destaques da Rede. Core discovery links are ordinary HTML anchors, not click-only JavaScript routes. The apps are self-contained single HTML files with embedded CSS/JS, no libraries, no ads, no account requirement and no trackers. Interactions remain in page memory; no data is sent or persisted.

Each app has one absolute self-canonical, matching Open Graph URL and WebApplication JSON-LD URL. Neither app canonicalises to the homepage: they are distinct resources. Relative links work in the matching repository structure and on the intended production host. Directory `index.html` variants should consolidate to their directory canonicals; server redirects are an owner-controlled deployment task.

## Sitemap curation and remaining legacy work

The branch sitemap contains **40 unique intended production URLs**. It includes the blog index, all three articles, both mini-apps, the beaches hub, seasonal guide and two existing travel/learning guides. Only source-resolved, indexable, self-canonical HTML is listed. Unverified historical `lastmod`, `priority` and `changefreq` values are omitted rather than presenting deployment dates as content-review dates.

Removed from the feed:
- `/previsao-surf/`: a `noindex` client redirect to the external forecast hub.
- `/espacos-logo-app.html`: an internal `noindex` layout page.

Four other existing pages are **temporarily excluded**, not deleted, because their canonical migration is still pending: `/apps/`, `/quiz/`, `/sessoes-interativas.html`, and `/novidades.html`. Normalise their HTML canonical/social URLs and validate them before restoring their sitemap entries. These satellite additions do not claim to complete the broader earlier SEO audit. Retired subdomain redirect stubs and the broader robots/asset policy also remain release-review work outside these new files.

The root `robots.txt` already permits the new `/blog/` and `/satellites/` paths; it is not changed in this addition. Preserve intentional noindex protections for administration, membership operations and errors. Do not block a noindex or redirect URL in robots.txt if Google needs to read its directive. A project-path `/asf-app/robots.txt` does not control an entire `github.io` host; robots rules apply at an origin's root.

## Local verification

From a checkout of this branch:

```sh
python3 -m unittest discover -s tests -p 'test_indexing_satellites.py' -v
```

The checks use Python's standard library. With Node.js available, two additional dependency-free tests execute the embedded JavaScript with small DOM fixtures: checklist progress/concerns/reset and glossary filtering/accent handling/no-results/reset. Without Node they report explicit skips. No network requests, deployment or GitHub writes are performed by the tests. Actions remains disabled; there is no claim of a GitHub-hosted CI run.

Checks cover canonical metadata, semantic landmarks, distinct titles/descriptions, JSON-LD parsing and consistency, substantial retained article text, reciprocal links, local targets and fragments, 28 static glossary definitions, no external app assets/tracking calls, robots access and every sitemap target's source indexability. These are regression checks, not an official HTML conformance certificate, Google's Rich Results Test, an ocean-risk assessment or evidence that Google has indexed the pages.

For manual preview, run `python3 -m http.server 8000` from the checkout and open the blog and each `/satellites/.../` route. Test keyboard navigation, small screens, printing and disabled JavaScript. Do not submit localhost, GitHub blob URLs or an unpublished fork URL to Search Console as production pages.

## Google Search Console checklist — authorised release only

- [ ] Complete the remaining legacy fixes above and obtain editorial/safety and branding approval. Article preparation dates are not proof of public publication; set a truthful visible publication date and matching Article `datePublished` when publishing.
- [ ] Publish through an independently authorised deployment. This branch does not enable Pages or change DNS. Confirm final production HTTPS routes return actual HTTP 200 responses, not a GitHub code viewer, redirect stub, authentication page or soft 404.
- [ ] Verify the authorised `asf.surf` Domain property using DNS, or use the appropriate verified URL-prefix property. A verification file in a repository alone is not proof of access.
- [ ] In **URL Inspection**, test the two canonical app URLs, the blog index and all three articles. Compare the user-declared and Google-selected canonicals; inspect rendered content, crawl permissions and any `X-Robots-Tag` header.
- [ ] Confirm one canonical per page, stable internal links, accessible CSS/JS and valid structured data matching visible content. WebApplication markup does not guarantee a particular rich result.
- [ ] Fetch `https://asf.surf/robots.txt` and `https://asf.surf/sitemap.xml` from the deployed origin. Recheck every submitted URL after deployment; local source tests do not prove live HTTP status.
- [ ] Submit the canonical sitemap through the verified property. Request indexing for a few important newly published URLs if appropriate; do not use the restricted Indexing API for ordinary blog posts or these apps.
- [ ] Monitor Page indexing, sitemap processing, duplicate/canonical exclusions, crawl errors, security/manual actions and Search performance over time. Record observations rather than promising indexing dates or rankings.

## Content and safety limits

The checklist is a question organiser, not a readiness score. Even all boxes checked produces no safety clearance; a flagged concern prompts postponement and local professional advice. The glossary explains wave mechanics without declaring any fixed wave height, period, tide or wind safe. Both remain useful without JavaScript. Sources linked for further learning include RNLI surfing safety and National Weather Service rip-current guidance; these organisations do not endorse this fork.

Further technical references: [Google canonical guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [sitemap construction](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), and [robots.txt scope](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt).
