#!/usr/bin/env python3
"""Render site/ for hotel-lynx from content/*.json + tools/templates.py (stdlib only).

    python3 tools/build.py

Content model
  content/site.json   language-independent facts (contact, rooms, ratings, walking times)
  content/map.json    projection of the two OSM base maps (tools/mapdata.py)
  content/en.json     English copy (root "/")
  content/fr.json     French copy (root "/fr/") — same keys as en.json
Pages are declared in PAGES. A page is "built" for a language when it is in
PAGES and its slug exists in that language's content file. Navigation to a page
that is not built falls back to the matching homepage anchor, so no link ever
points at a missing file.
Run tools/images.py first when image selections change (it writes the manifest),
and tools/mapdata.py when the map data changes.
"""
import hashlib, json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
SITE = os.path.join(ROOT, "site")
sys.path.insert(0, TOOLS)
import templates as T  # noqa: E402

LANGS = ["en", "fr"]          # order = hreflang order; en is x-default
PAGES = {"home": T.page_home, "rooms": T.page_rooms, "agadir": T.page_agadir,
         "basics": T.page_basics, "ask": T.page_ask}


def load(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return json.load(f)


def fr_typo(v):
    """French typography on every copy string: narrow no-break space before : ; ! ? and » and after «
    (text only, never inside tags). The composed e-mail ("mail") keeps plain spaces for mail clients."""
    if isinstance(v, dict):
        return {k: (x if k == "mail" else fr_typo(x)) for k, x in v.items()}
    if isinstance(v, list):
        return [fr_typo(x) for x in v]
    if not isinstance(v, str):
        return v
    parts = re.split(r"(<[^>]+>)", v)
    for i in range(0, len(parts), 2):
        s = re.sub(r"[ \u00a0]([:;!?»])", "\u202f\\1", parts[i])
        parts[i] = re.sub(r"«[ \u00a0]", "«\u202f", s)
    return "".join(parts)


def write(rel, text):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


# style demo (site/assets/css/looks.css): the three OSM base maps re-tinted per demo palette, swapped in by looks.js.
# Base colour → palette colour; keep in step with html[data-look="…"] in looks.css (facade-l, night, white, ink).
MAPS = ("door", "city", "city-m")
LOOK_MAPS = {
    "green": {"#e6d9d9": "#e2e6d8", "#d9c9c9": "#d5d9ca", "#384770": "#2e4a52", "#fffdfc": "#fcfaf4", "#15110f": "#264a3a"},
    "blue": {"#e6d9d9": "#d6e0de", "#d9c9c9": "#c8d3d1", "#384770": "#2c4468", "#fffdfc": "#faf6ee", "#15110f": "#173a52"},
    "rose": {"#e6d9d9": "#f2e2d8", "#d9c9c9": "#e5d3c8", "#384770": "#5a4458", "#fffdfc": "#fffaf5", "#15110f": "#7c4c46"},
}


def map_variants():
    for which in MAPS:
        with open(os.path.join(SITE, "assets", "img", f"map-{which}.svg"), encoding="utf-8") as f:
            svg = f.read()
        for look, sub in LOOK_MAPS.items():
            write(f"assets/img/map-{which}-{look}.svg", re.sub(r"#[0-9a-f]{6}\b", lambda m: sub.get(m.group(0), m.group(0)), svg))


def asset_version():
    h = hashlib.sha1()
    rels = ["assets/css/site.css", "assets/js/site.js", "assets/css/looks.css", "assets/js/looks.js"]
    rels += [f"assets/img/map-{w}.svg" for w in MAPS] + [f"assets/img/map-{w}-{l}.svg" for w in MAPS for l in LOOK_MAPS]
    for rel in rels:
        p = os.path.join(SITE, rel)
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    return h.hexdigest()[:8]


def main():
    site = load("content/site.json")
    img = load("tools/images.manifest.json")
    mp = load("content/map.json")
    content = {l: load(f"content/{l}.json") for l in LANGS if os.path.exists(os.path.join(ROOT, "content", f"{l}.json"))}
    if "fr" in content:
        content["fr"] = fr_typo(content["fr"])

    def page_path(lang, key):
        t = content[lang]
        slug = t["pages"].get(key, {}).get("slug")
        if key not in PAGES or slug is None:
            return None
        return t["dir"] + (slug + "/" if slug else "")

    built = []
    map_variants()
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
                # not built → homepage section
                return (f"#{anchor}" if _key == "home" else f"{_home}#{anchor}") if anchor else _home

            alt = {l: page_path(l, key) for l in content if page_path(l, key)}
            ctx = {"site": site, "t": t, "img": img, "map": mp, "page": key, "url": url, "alt": alt, "v": v}
            write(path.lstrip("/") + "index.html", render(ctx))
            built.append(alt)

    # 404: English shell + a French line (one file serves every path)
    t = content["en"]
    ctx = {"site": site, "t": t, "img": img, "map": mp, "page": "404", "alt": {"en": "/404.html"}, "v": v,
           "fr": content.get("fr", t), "fr_home": page_path("fr", "home") if "fr" in content else "/",
           "url": lambda target, anchor=None: (page_path("en", target) or "/") + (f"#{anchor}" if anchor and target == "home" else "")}
    write("404.html", T.page_404(ctx))

    base = site["base_url"]
    urls = []
    for alt in built:
        if len(alt) > 1:
            links = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{base}{h}"/>' for l, h in alt.items())
            links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{base}{alt["en"]}"/>'
        else:
            links = ""
        for h in alt.values():
            if (base + h) not in [u[0] for u in urls]:
                urls.append((base + h, links))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "".join(f"  <url><loc>{u}</loc>{l}</url>\n" for u, l in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")
    # css/js/maps are versioned by ?v=<hash>; fonts never change; images keep stable names → 1 week
    write("_headers", "/assets/css/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/js/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/assets/img/*\n  Cache-Control: public, max-age=604800\n\n"
          "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
          "  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()\n")


if __name__ == "__main__":
    main()
