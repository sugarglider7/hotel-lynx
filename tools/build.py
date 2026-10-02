#!/usr/bin/env python3
"""Render site/ for hotel-lynx from content/*.json + tools/templates.py (stdlib only).

    python3 tools/build.py

Content model
  content/site.json   language-independent facts (contact, rooms, ratings, walking times)
  content/en.json     English copy (root "/")
  content/fr.json     French copy (root "/fr/") — same keys as en.json; picked up
                      automatically when present (phase 3)
Pages are declared in PAGES. A page is "built" for a language when it is in
PAGES and its slug exists in that language's content file. Navigation to a page
that is not built yet falls back to the matching homepage anchor, so no link
ever points at a missing file.
Run tools/images.py first when image selections change (it writes the manifest).
"""
import hashlib, json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
SITE = os.path.join(ROOT, "site")
sys.path.insert(0, TOOLS)
import templates as T  # noqa: E402

LANGS = ["en", "fr"]          # order = hreflang order; en is x-default
PAGES = {"home": T.page_home}  # phase 3 adds: rooms, agadir, basics, reviews, ask


def load(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return json.load(f)


def write(rel, text):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


def asset_version():
    h = hashlib.sha1()
    for rel in ("assets/css/site.css", "assets/js/site.js"):
        p = os.path.join(SITE, rel)
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    return h.hexdigest()[:8]


def main():
    site = load("content/site.json")
    img = load("tools/images.manifest.json")
    content = {l: load(f"content/{l}.json") for l in LANGS if os.path.exists(os.path.join(ROOT, "content", f"{l}.json"))}

    def page_path(lang, key):
        t = content[lang]
        slug = t["pages"].get(key, {}).get("slug")
        if key not in PAGES or slug is None:
            return None
        return t["dir"] + (slug + "/" if slug else "")

    built = []
    v = asset_version()
    for lang, t in content.items():
        for key, render in PAGES.items():
            path = page_path(lang, key)
            if path is None:
                continue
            home = page_path(lang, "home")

            def url(target, anchor=None, _lang=lang, _key=key, _home=home):
                p = page_path(_lang, target)
                if p:
                    return p + (f"#{anchor}" if anchor and target == "home" else "")
                # not built yet → homepage section
                return (f"#{anchor}" if _key == "home" else f"{_home}#{anchor}") if anchor else _home

            alt = {l: page_path(l, key) for l in content if page_path(l, key)}
            ctx = {"site": site, "t": t, "img": img, "page": key, "url": url, "alt": alt, "v": v}
            write(path.lstrip("/") + "index.html", render(ctx))
            built.append(path)

    # 404 (English shell, root-absolute links only)
    t = content["en"]
    ctx = {"site": site, "t": t, "img": img, "page": "404", "alt": {"en": "/"}, "v": v,
           "url": lambda target, anchor=None: "/" + (f"#{anchor}" if anchor else "")}
    write("404.html", T.page_404(ctx))

    base = site["base_url"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{base}{p}</loc></url>\n" for p in built) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")
    # css/js are versioned by ?v=<hash>; fonts never change; images keep stable names → 1 week
    write("_headers", "/assets/css/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/js/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/img/*\n  Cache-Control: public, max-age=604800\n\n"
          "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")


if __name__ == "__main__":
    main()
