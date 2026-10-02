"""HTML templates/partials for hotel-lynx. Pure functions: (ctx) -> str.

ctx keys (built by tools/build.py):
  site  content/site.json (language-independent facts)
  t     content/<lang>.json (copy for one language)
  img   tools/images.manifest.json
  map   content/map.json (projection of the two OSM base maps)
  page  page key ("home", "rooms", ...)
  url   helper: url(page_key, anchor=None) -> href valid for this language,
        falling back to a homepage anchor while a page is not built yet
  alt   {lang: href} of this page in every built language (hreflang + switch)
Copy strings are trusted HTML (may contain <br>, &nbsp;, <a>); attribute values go
through esc().
"""
import json
import math
import re
from html import escape


def esc(s):
    return escape(str(s), quote=True)


# --- small building blocks -------------------------------------------------

ARROW = ('<svg class="arw" viewBox="0 0 16 16" aria-hidden="true" style="--b:{b}deg">'
         '<path d="M8 1.5 13 7H9.4v7.5H6.6V7H3z"/></svg>')
ICON = {
    "phone": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 2.8 9.4 6c.5.6.5 1.4 0 2l-1.6 1.7a12.6 12.6 0 0 0 6.5 6.5l1.7-1.6c.6-.5 1.4-.5 2 0l3.2 2.8c.6.6.7 1.5.1 2.1l-1.6 1.9c-.7.8-1.8 1.1-2.8.8A19.5 19.5 0 0 1 1.8 7.1c-.3-1 0-2.1.8-2.8L4.5 2.7c.6-.6 1.5-.5 2.1.1z"/></svg>',
    "go": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.5 20.7 12l-7.5 7.5-1.9-1.9 4.2-4.2H3.3v-2.8h12.2l-4.2-4.2z"/></svg>',
    "out": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 4h12v12h-2.8V8.8L5.9 20.1 3.9 18.1 15.2 6.8H8z"/></svg>',
    "yes": '<svg class="mk" viewBox="0 0 24 24" aria-hidden="true"><path d="m9.5 15.6 9.4-9.4 2 2-11.4 11.4L3.1 13.2l2-2z"/></svg>',
    "no": '<svg class="mk" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 9.9 6.4-6.4 2.1 2.1-6.4 6.4 6.4 6.4-2.1 2.1-6.4-6.4-6.4 6.4-2.1-2.1 6.4-6.4-6.4-6.4 2.1-2.1z"/></svg>',
    "mail": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5h20v14H2zm2.6 2.4v.3l7.4 5 7.4-5v-.3zm14.8 2.9-7.4 5-7.4-5v6.3h14.8z"/></svg>',
    "copy": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 2h13v15h-3v-2.6h.4V4.6H10.6V5H8zM3 7h13v15H3zm2.6 2.6v9.8h7.8V9.6z"/></svg>',
    "pin": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1.5a8 8 0 0 1 8 8c0 5.6-8 13-8 13s-8-7.4-8-13a8 8 0 0 1 8-8zm0 4.7a3.3 3.3 0 1 0 0 6.6 3.3 3.3 0 0 0 0-6.6z"/></svg>',
}


def arrow(bearing):
    return ARROW.format(b=bearing) if bearing is not None else ""


def bearing(site, ll):
    """Initial great-circle bearing (degrees) from the hotel pin to ll=[lat, lng]."""
    la1, lo1 = math.radians(site["geo"]["lat"]), math.radians(site["geo"]["lng"])
    la2, lo2 = math.radians(ll[0]), math.radians(ll[1])
    y = math.sin(lo2 - lo1) * math.cos(la2)
    x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(lo2 - lo1)
    return round((math.degrees(math.atan2(y, x)) + 360) % 360)


def picture(ctx, name, alt, sizes, cls="", eager=False):
    """<picture>/<img> from the image manifest: srcset, intrinsic size, dominant colour."""
    m = ctx["img"][name]
    vs = sorted(m["variants"], key=lambda v: v["w"])
    big = vs[-1]
    fallback = vs[0] if len(vs) == 1 else vs[-2] if len(vs) > 2 else vs[0]
    srcset = ", ".join(f'/assets/img/{v["file"]} {v["w"]}w' for v in vs)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    img = (f'<img class="{esc(cls)}" src="/assets/img/{fallback["file"]}" srcset="{srcset}" sizes="{esc(sizes)}" '
           f'width="{big["w"]}" height="{big["h"]}" alt="{esc(alt)}" {load} style="background:{m["color"]}">')
    if "mobile" in m:
        mvs = sorted(m["mobile"], key=lambda v: v["w"])
        mset = ", ".join(f'/assets/img/{v["file"]} {v["w"]}w' for v in mvs)
        return (f'<picture><source media="(max-width: 47.99rem)" srcset="{mset}" '
                f'sizes="100vw" width="{mvs[-1]["w"]}" height="{mvs[-1]["h"]}">{img}</picture>')
    return f"<picture>{img}</picture>"


def dec(ctx, s):
    """A decimal score in the page language (8.4 → 8,4 in French)."""
    return str(s).replace(".", ctx["t"]["decimal"])


def dist(ctx, s):
    """A distance in the page language: decimal comma in French, no-break space before the unit."""
    s = re.sub(r"(\d)\.(\d)", r"\1" + ctx["t"]["decimal"] + r"\2", str(s))
    return re.sub(r" (k?m)\b", "\u00a0\\1", s)


def m2(n):
    """Floor area; the unit is set in the text face so the superscript doesn't float in a mono cell."""
    return f'{n}&nbsp;<span class="u">m²</span>'


def eo(html):
    """Keep Cloudflare's e-mail obfuscation off an address: otherwise it rewrites text and
    mailto: links into /cdn-cgi/l/email-protection that only work once its script has run."""
    return f"<!--email_off-->{html}<!--/email_off-->"


def tel(site):
    return "tel:" + site["phone_e164"]


def ask_href(ctx, room=None, balcony=False):
    q = "&".join(([f"room={room}"] if room else []) + (["balcony=1"] if balcony else []))
    return ctx["url"]("ask", "ask") + (f"?{q}" if q else "")


def ext(ctx, href, label, cls="lnk"):
    return (f'<a class="{cls}" href="{esc(href)}" rel="noopener" target="_blank">{label}'
            f'<span class="sr"> ({ctx["t"]["ui"]["new_tab"]})</span></a>')


# --- document shell -----------------------------------------------------------

def head(ctx, title, description, path):
    site, t = ctx["site"], ctx["t"]
    canonical = site["base_url"] + path
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{site["base_url"]}{h}">' for l, h in ctx["alt"].items())
    if len(ctx["alt"]) > 1:
        alts += f'<link rel="alternate" hreflang="x-default" href="{site["base_url"]}{ctx["alt"]["en"]}">'
    # the 404 is served at any path: no canonical, no alternates, not indexed
    links = '<meta name="robots" content="noindex">' if ctx.get("noindex") else f'<link rel="canonical" href="{canonical}">{alts}'
    og = site["base_url"] + "/assets/img/" + ctx["img"]["og-facade"]["file"]
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{links}
<meta name="theme-color" content="#15110f">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hôtel Lynx">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(t['hero']['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/overpass-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={ctx['v']}">
<script>document.documentElement.classList.add('js')</script>
<script src="/assets/js/site.js?v={ctx['v']}" defer></script>
{ctx.get('head_extra', '')}
</head>"""


def wordmark(ctx, tag="a"):
    t = ctx["t"]
    inner = ('<span class="wm-plate"><span class="wm-a">Hotel</span><span class="wm-eye" aria-hidden="true"></span>'
             f'<span class="wm-b">Lynx</span></span><span class="wm-sub">{t["ui"]["wordmark_sub"]}</span>')
    if tag == "a":
        return f'<a class="wm" href="{ctx["url"]("home")}" aria-label="{esc(t["ui"]["home_label"])}">{inner}</a>'
    return f'<span class="wm">{inner}</span>'


def lang_switch(ctx, short=False):
    """Link to this page in the other language; the header shows the 2-letter code."""
    others = [(l, h) for l, h in ctx["alt"].items() if l != ctx["t"]["lang"]]
    if not others:
        return ""
    l, h = others[0]
    label = ctx["t"]["ui"]["switch_label"]
    if short:
        return f'<a class="lang lang-hd" href="{h}" hreflang="{l}" lang="{l}" aria-label="{esc(label)}">{l.upper()}</a>'
    return f'<a class="lang" href="{h}" hreflang="{l}" lang="{l}">{label}</a>'


def nav_links(ctx):
    out = []
    for i, n in enumerate(ctx["t"]["nav"], 1):
        cur = ' aria-current="page"' if n["page"] == ctx["page"] else ""
        out.append(f'<li><a href="{ctx["url"](n["page"], n["anchor"])}"{cur}><span class="n">{i:02d}</span>{n["label"]}</a></li>')
    return "".join(out)


def header(ctx):
    site, t = ctx["site"], ctx["t"]
    links = nav_links(ctx)
    ask = ask_href(ctx)
    cur = ' aria-current="page"' if ctx["page"] == "ask" else ""
    return f"""<a class="skip" href="#main">{t['ui']['skip']}</a>
<header class="hd" id="top">
  <div class="hd-in">
    {wordmark(ctx)}
    <nav class="hd-nav" aria-label="{esc(t['ui']['nav_label'])}">
      <ul>{links}</ul>
    </nav>
    <div class="hd-act">
      {lang_switch(ctx, short=True)}
      <a class="hd-tel" href="{tel(site)}" aria-label="{esc(t['ui']['call_reception'] + t['ui']['colon'] + site['phone_display'])}">{ICON['phone']}<span class="hd-tel-l"><span class="hd-c">{t['ui']['call']} </span>{t['ui']['h24']}</span><span class="hd-tel-n">{site['phone_display']}</span></a>
      <a class="btn btn-sig hd-ask" href="{ask}"{cur}>{t['ui']['ask']}</a>
      <button class="hd-menu" type="button" aria-expanded="false" aria-controls="menu"><span class="hd-menu-l">{t['ui']['menu']}</span><span class="burger" aria-hidden="true"></span></button>
    </div>
  </div>
  <div class="menu" id="menu" hidden>
    <ul class="menu-list">{links}<li><a href="{ask}"{cur}><span class="n">{len(t['nav']) + 1:02d}</span>{t['ui']['ask']}</a></li></ul>
    <div class="menu-foot">
      <a class="btn btn-sig" href="{tel(site)}">{ICON['phone']}{t['ui']['call_reception']}</a>
      {eo(f'<a class="menu-mail" href="mailto:{site["email"]}">{site["email"]}</a>')}
      {lang_switch(ctx)}
    </div>
  </div>
</header>"""


def footer(ctx):
    site, t = ctx["site"], ctx["t"]
    f = t["footer"]
    a = site["address"]
    pages = "".join(f'<li><a href="{ctx["url"](n["page"], n["anchor"])}">{n["label"]}</a></li>' for n in t["nav"])
    pages += f'<li><a href="{ask_href(ctx)}">{t["ui"]["ask"]}</a></li>'
    return f"""<footer class="ft" id="contact">
  <div class="ft-in">
    <div class="ft-brand">{wordmark(ctx, tag="span")}<p class="ft-class">{f['class']} · ★★</p></div>
    <address class="ft-addr">
      <p>{a['street']}<br>{a['district']}, {a['postcode']} {a['city']}<br><span class="mut">{f['address_note']}</span></p>
      <p>{ext(ctx, site['maps_url'], f['map'])}</p>
    </address>
    <div class="ft-contact">
      <p><a class="ft-tel" href="{tel(site)}">{site['phone_display']}</a><span class="mut mono"> · 24h</span></p>
      <p>{eo(f'<a class="lnk" href="mailto:{site["email"]}">{site["email"]}</a>')}</p>
      <p>{ext(ctx, site['booking_url'], 'Booking.com')}</p>
    </div>
    <nav class="ft-nav" aria-label="{esc(f['nav_label'])}"><ul>{pages}</ul></nav>
    <p class="ft-times mono">{f['times']}</p>
    <p class="ft-copy mut">© {f['copy']}{(' — ' + lang_switch(ctx)) if lang_switch(ctx) else ''}</p>
  </div>
</footer>"""


def sticky(ctx):
    site, t = ctx["site"], ctx["t"]
    return f"""<div class="sticky" data-sticky>
  <a class="btn btn-ghost-d" href="{tel(site)}">{ICON['phone']}{t['sticky']['call']}</a>
  <a class="btn btn-sig" href="{ask_href(ctx)}">{t['sticky']['ask']}</a>
</div>"""


def ld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def hotel_data(ctx):
    site, t = ctx["site"], ctx["t"]
    a = site["address"]
    data = {
        "@context": "https://schema.org", "@type": "Hotel", "@id": site["base_url"] + "/#hotel",
        "name": site["name"], "url": site["base_url"] + ctx["url"]("home"),
        "image": site["base_url"] + "/assets/img/" + ctx["img"]["og-facade"]["file"],
        "description": t["pages"]["home"]["description"],
        "telephone": site["phone_e164"], "email": site["email"],
        "address": {"@type": "PostalAddress", "streetAddress": a["street"], "addressLocality": a["city"],
                    "addressRegion": "Souss-Massa", "postalCode": a["postcode"], "addressCountry": a["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": site["geo"]["lat"], "longitude": site["geo"]["lng"]},
        "hasMap": site["maps_url"],
        "starRating": {"@type": "Rating", "ratingValue": site["stars"]},
        "checkinTime": site["checkin"], "checkoutTime": site["checkout"],
        "petsAllowed": False,
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in t["ld"]["hotel"]],
        "sameAs": [site["booking_url"]],
    }
    return data


def crumbs(ctx):
    site, t = ctx["site"], ctx["t"]
    home = t["pages"]["home"]["crumb"]
    p = t["pages"][ctx["page"]]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": home, "item": site["base_url"] + ctx["url"]("home")},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": site["base_url"] + ctx["url"](ctx["page"])}]}


def document(ctx, main, jsonld=()):
    p = ctx["t"]["pages"][ctx["page"]] if ctx["page"] in ctx["t"]["pages"] else None
    title, desc = (p["title"], p["description"]) if p else (ctx["title"], ctx["description"])
    ctx["head_extra"] = "".join(ld(d) for d in jsonld)
    path = ctx["alt"][ctx["t"]["lang"]]
    return (head(ctx, title, desc, path) + "\n<body>\n" + header(ctx) +
            f'\n<main id="main">\n{main}\n</main>\n' + footer(ctx) + "\n" + sticky(ctx) + "\n</body>\n</html>\n")


def page_head(ctx, side="", cls=""):
    """Interior page header: a black fascia plate with a sign-board breadcrumb."""
    t = ctx["t"]
    P = t[ctx["page"] + "_page"]["head"]
    n = next((i for i, x in enumerate(t["nav"], 1) if x["page"] == ctx["page"]), len(t["nav"]) + 1)
    return f"""<section class="ph {cls}" aria-labelledby="h1">
  <div class="ph-in">
    <div class="ph-copy">
      <p class="ph-sign mono"><a href="{ctx['url']('home')}">Hôtel Lynx</a><span aria-hidden="true">/</span><span><span class="n">{n:02d}</span> {t['pages'][ctx['page']]['crumb']}</span></p>
      <h1 id="h1">{P['h1']}</h1>
      <p class="lead">{P['lead']}</p>
    </div>
    {side}
  </div>
</section>"""


def cta_band(ctx, key):
    site, t = ctx["site"], ctx["t"]
    c = t["cta"][key]
    return f"""<section class="band" aria-labelledby="band-{key}">
  <div class="band-in">
    <h2 id="band-{key}">{c['h']}</h2>
    <p>{c['p']}</p>
    <div class="band-act">
      <a class="btn btn-sig btn-lg" href="{ask_href(ctx)}">{t['ui']['ask']}{ICON['go']}</a>
      <a class="btn btn-ghost-d btn-lg" href="{tel(site)}">{ICON['phone']}{t['ui']['call_reception']}</a>
    </div>
  </div>
</section>"""


def more_link(href, label):
    return f'<p class="more"><a class="more-a" href="{href}">{label}{ICON["go"]}</a></p>'


# --- homepage sections --------------------------------------------------------

def sec_hero(ctx):
    site, t = ctx["site"], ctx["t"]
    h, r = t["hero"], site["rating"]["booking"]
    walk = {w["key"]: w for w in site["walk"]}
    posts = "".join(
        f'<li class="post"><span class="post-l">{p["label"]}</span>'
        f'<span class="post-m mono">{walk[p["key"]]["min"]}&nbsp;{t["agadir"]["min"]}{arrow(walk[p["key"]].get("bearing"))}</span></li>'
        for p in h["posts"])
    staff = dict(r["sub"])["staff"]
    return f"""<section class="hero" aria-labelledby="h1">
  <div class="hero-photo">
    {picture(ctx, 'facade', h['alt'], '100vw', eager=True)}
    <ul class="posts" aria-label="{esc(t['agadir']['axis_label'])}">{posts}</ul>
  </div>
  <div class="fascia">
    <div class="fascia-in">
      <div class="hero-copy">
        <p class="kicker mono">{h['kicker']}</p>
        <h1 id="h1">{h['h1']}</h1>
        <p class="lead">{h['lead']}</p>
      </div>
      <div class="hero-side">
        <div class="hero-cta">
          <a class="btn btn-sig btn-lg" href="{ask_href(ctx)}">{t['ui']['ask']}{ICON['go']}</a>
          <a class="btn btn-ghost-d btn-lg" href="{tel(site)}">{ICON['phone']}{t['ui']['call_reception']}</a>
        </div>
        <a class="score" href="#reviews">
          <span class="score-n">{dec(ctx, r['score'])}</span>
          <span class="score-t"><b>{h['rating_label']}</b><span>{h['rating_count']}</span></span>
          <span class="score-s"><b>{dec(ctx, staff)}</b><span>{h['staff_label']}</span></span>
        </a>
      </div>
    </div>
  </div>
</section>"""


def board(ctx, b, fig=True):
    yes = "".join(f'<li>{ICON["yes"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in b["yes"])
    no = "".join(f'<li>{ICON["no"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in b["no"])
    figure = f"""<figure class="board-fig rv">
          {picture(ctx, 'reception', b['img_alt'], '(min-width: 64rem) 30vw, 100vw')}
          <figcaption>{b['img_cap']}</figcaption>
        </figure>""" if fig else ""
    return f"""<div class="board">
      <div class="board-col board-yes">
        <p class="board-tag mono"><span>{b['yes_label']}</span></p>
        <ul class="board-list">{yes}</ul>
      </div>
      <div class="board-col board-no">
        <p class="board-tag mono"><span>{b['no_label']}</span></p>
        <ul class="board-list">{no}</ul>
        {figure}
      </div>
    </div>"""


def sec_basics(ctx):
    t = ctx["t"]
    b = t["basics"]
    return f"""<section class="basics sec" id="basics" aria-labelledby="basics-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{b['kicker']}</p>
      <h2 id="basics-h">{b['h2']}</h2>
      <p class="sec-intro">{b['intro']}</p>
    </header>
    {board(ctx, b)}
    {more_link(ctx['url']('basics'), b['more'])}
  </div>
</section>"""


def key_plate(rm, c, cls="dir-plate"):
    """The black key-tag plate that stands in for a room photo we don't have (the Single)."""
    return (f'<span class="{cls}" aria-hidden="true"><b class="mono">{m2(rm["m2"])}</b>'
            f'<span>{c["beds"]}</span></span>')


def room_tile_img(ctx, rm, c, sizes):
    """Photo for a room tile; the Single has none, so it gets a plain sign plate instead."""
    if not rm["img"]:
        return key_plate(rm, c)
    return picture(ctx, rm["img"], c["alt"], sizes)


def sec_rooms(ctx):
    """Homepage summary: the room directory, each row leading to the full entry on /rooms/."""
    site, t = ctx["site"], ctx["t"]
    R = t["rooms"]
    rooms_url = ctx["url"]("rooms", "rooms")
    base = rooms_url if "#" not in rooms_url else rooms_url.split("#")[0]
    rows = []
    for rm in site["rooms"]:
        c = R["items"][rm["key"]]
        rows.append(f"""<li class="dir-item rv">
      <a class="dir-row" href="{base}#room-{rm['key']}">
        <span class="dir-img">{room_tile_img(ctx, rm, c, '(min-width: 64rem) 18vw, 30vw')}</span>
        <span class="dir-txt">
          <span class="dir-no mono">{rm['no']}</span>
          <span class="dir-name">{c['name']}</span>
          <span class="dir-spec mono">{m2(rm['m2'])} · {R['guests'][str(rm['guests'])]}</span>
        </span>
        <span class="dir-go" aria-hidden="true">{ICON['go']}</span>
      </a>
    </li>""")
    return f"""<section class="rooms sec" id="rooms" aria-labelledby="rooms-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{R['kicker']}</p>
      <h2 id="rooms-h">{R['h2']}</h2>
      <p class="sec-intro">{R['intro']}</p>
    </header>
    <ol class="dir">
    {''.join(rows)}
    </ol>
    {more_link(base, R['more'])}
  </div>
</section>"""


def lynx_line(ctx):
    site, t = ctx["site"], ctx["t"]
    A = t["agadir"]
    P = A["places"]
    span = max(w["min"] for w in site["walk"])
    stops, prev = [], 0
    for w in site["walk"]:
        p = P[w["key"]]
        gap = min(w["min"] - prev, 6)
        prev = w["min"]
        cls = "stop" + (" stop-minor" if w.get("list_only") else "") + (" stop-end" if w.get("end") else "") + (" stop-star" if w.get("star") else "")
        note = f'<span class="stop-note">{p["note"]}</span>' if p.get("note") else ""
        stops.append(
            f'<li class="{cls}" style="--m:{w["min"]};--gap:{gap}">'
            f'<span class="stop-min mono">{w.get("min_label", w["min"])}<small>{A["min"]}</small></span>'
            f'<span class="stop-dot" aria-hidden="true"></span>'
            f'<span class="stop-lbl"><b>{p["name"]}</b>{note}<span class="stop-meta mono">{dist(ctx, w["dist"])}{arrow(w.get("bearing"))}</span></span></li>')
    minor = [w for w in site["walk"] if w.get("list_only")]
    extra = '<span class="mono"> · </span>'.join(
        f'{P[w["key"]]["name"]} <span class="mono">{w.get("min_label", w["min"])}&nbsp;{A["min"]}, {dist(ctx, w["dist"])}</span>' for w in minor)
    return f"""<div class="line" style="--span:{span}">
      <p class="line-axis mono" aria-hidden="true">{A['axis_label']}</p>
      <ol class="stops">
        <li class="stop stop-origin" style="--m:0;--gap:0"><span class="stop-min mono">0<small>{A['min']}</small></span><span class="stop-dot" aria-hidden="true"></span><span class="stop-lbl"><b>{A['origin']}</b><span class="stop-meta mono">{A['origin_sub']}</span></span></li>
        {''.join(stops)}
      </ol>
      <p class="line-extra">{extra}</p>
      <p class="line-note mono">{arrow(45)} {A['arrow_note']}</p>
    </div>"""


def sec_agadir(ctx):
    site, t = ctx["site"], ctx["t"]
    A = t["agadir"]
    P = A["places"]
    rides = "".join(
        f'<li class="ride"><span class="ride-min mono"><small>{A["ride_about"]}</small>{r["min"]}<small>{A["min"]}</small></span>'
        f'<span class="ride-lbl"><b>{P[r["key"]]["name"]}</b><span class="mono">{dist(ctx, r["dist"])}{arrow(r.get("bearing"))}</span></span></li>'
        for r in site["ride"])
    return f"""<section class="agadir" id="agadir" aria-labelledby="agadir-h">
  <figure class="agadir-fig">
    {picture(ctx, 'terrace', A['img_alt'], '100vw')}
    <figcaption>{A['img_cap']}</figcaption>
  </figure>
  <div class="wrap sec">
    <header class="sec-hd">
      <p class="kicker mono">{A['kicker']}</p>
      <h2 id="agadir-h">{A['h2']}</h2>
      <p class="sec-intro">{A['intro']}</p>
    </header>
    {lynx_line(ctx)}
    <div class="rides">
      <h3>{A['ride_h']}</h3>
      <ul>{rides}</ul>
      <p class="mut">{A['ride_note']}</p>
    </div>
    {more_link(ctx['url']('agadir'), A['more'])}
  </div>
</section>"""


def sec_arrive(ctx, h="h2", more=True, eager=False, brief=False):
    """Getting in. brief=True (the practical page) keeps the photo, heading and the four times;
    the parking/airport sentences live in that page's "Finding us" instead."""
    t = ctx["t"]
    A = t["arrive"]
    facts = "".join(f'<div><dt class="mono">{f["k"]}</dt><dd>{f["v"]}</dd></div>' for f in A["facts"])
    link = more_link(ctx['url']('basics'), A['more']) if more else ""
    paras = "" if brief else f"<p>{A['p1']}</p>\n      <p>{A['p2']}</p>"
    return f"""<section class="arrive" id="arrive" aria-labelledby="arrive-h">
  <div class="arrive-in">
    <figure class="arrive-fig rv">
      {picture(ctx, 'facade-night', A['img_alt'], '(min-width: 64rem) 55vw, 100vw', eager=eager)}
      <figcaption>{A['img_cap']}</figcaption>
    </figure>
    <div class="arrive-txt">
      <p class="kicker mono">{A['kicker']}</p>
      <{h} id="arrive-h">{A['h2']}</{h}>
      {paras}
      <dl class="facts">{facts}</dl>
      {link}
    </div>
  </div>
</section>"""


def quote(ctx, q, cls="q"):
    lang = f' lang="{q["lang"]}"' if q.get("lang") else ""
    o, c = ("«\u202f", "\u202f»") if ctx["t"]["lang"] == "fr" else ("“", "”")
    return (f'<figure class="{cls}"><blockquote{lang}><p>{o}{q["q"]}{c}</p></blockquote>'
            f'<figcaption><b>{q["who"]}</b> · {q["src"]}</figcaption></figure>')


def sec_reviews(ctx):
    site, t = ctx["site"], ctx["t"]
    V, r = t["reviews"], site["rating"]["booking"]
    bars = "".join(
        f'<li style="--v:{v}"><span>{V["sub_labels"][k]}</span><b class="mono">{dec(ctx, v)}</b><i aria-hidden="true"></i></li>'
        for k, v in r["sub"])
    quotes = "".join(quote(ctx, q, "q rv") for q in V["quotes"])
    return f"""<section class="reviews sec" id="reviews" aria-labelledby="reviews-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{V['kicker']}</p>
      <h2 id="reviews-h">{V['h2']}</h2>
    </header>
    <div class="rv-grid">
      <div class="scorecard">
        <p class="sc-big"><span class="sc-n">{dec(ctx, r['score'])}</span><span class="sc-of mono">/10</span></p>
        <p class="sc-src"><b>{V['score_label']}</b>, {V['count']}</p>
        <ul class="bars">{bars}</ul>
        <p class="mut sc-g">{V['google']}</p>
      </div>
      <div class="quotes">
        {quote(ctx, V['lead_quote'], 'q q-lead')}
        {quotes}
      </div>
    </div>
  </div>
</section>"""


def side_plate(ctx):
    site, t = ctx["site"], ctx["t"]
    S = t["ask"]["side"]
    return f"""<aside class="ask-side" aria-label="{esc(S['h'])}">
      <h3>{S['h']}</h3>
      <a class="side-tel" href="{tel(site)}"><span class="mono">{S['call']}</span><b>{site['phone_display']}</b></a>
      {eo(f'<a class="side-row" href="mailto:{site["email"]}"><span class="mono">{S["email"]}</span><b>{site["email"]}</b></a>')}
      <a class="side-row" href="{site['booking_url']}" rel="noopener" target="_blank"><span class="mono">{S['booking']}</span><b>{S['booking_sub']} {ICON['out']}</b><span class="sr"> ({t['ui']['new_tab']})</span></a>
    </aside>"""


def sec_ask_mini(ctx):
    """Homepage summary of the inquiry: dates + guests, handed to /ask/ by a plain GET (works without JS)."""
    site, t = ctx["site"], ctx["t"]
    K, F, M = t["ask"], t["ask"]["f"], t["ask"]["mini"]
    return f"""<section class="ask sec" id="ask" aria-labelledby="ask-h">
  <div class="wrap ask-grid">
    <div class="ask-main">
      <header class="sec-hd">
        <p class="kicker mono">{K['kicker']}</p>
        <h2 id="ask-h">{K['h2']}</h2>
        <p class="sec-intro">{M['intro']}</p>
      </header>
      <form class="form mini" id="ask-mini" action="{ctx['url']('ask')}" method="get">
        <div class="fg fg-3">
          <div class="fld"><label for="m-arr">{F['arrival']}</label><input id="m-arr" name="arrival" type="date"></div>
          <div class="fld"><label for="m-dep">{F['departure']}</label><input id="m-dep" name="departure" type="date"></div>
          <div class="fld"><label for="m-gst">{F['guests']}</label><input id="m-gst" name="guests" type="number" inputmode="numeric" min="1" max="12" value="2"></div>
        </div>
        <button class="btn btn-sig btn-lg" type="submit">{M['submit']}{ICON['go']}</button>
        <p class="fine">{M['fine']}</p>
      </form>
    </div>
    {side_plate(ctx)}
  </div>
</section>"""


def sec_ask(ctx):
    """The full availability request (the /ask/ page): validation → composed email + robust fallbacks."""
    site, t = ctx["site"], ctx["t"]
    K = t["ask"]
    F = K["f"]
    D = K["done"]
    rooms = "".join(f'<option value="{rm["key"]}">{t["rooms"]["items"][rm["key"]]["name"]}</option>' for rm in site["rooms"])
    times = "".join(f"<option>{o}</option>" for o in F["time_opts"])
    i18n = {"err": K["err"], "mail": K["mail"], "email": site["email"], "lang": t["date_locale"],
            "room_any": F["room_any"],
            "rooms": {rm["key"]: t["rooms"]["items"][rm["key"]]["name"] for rm in site["rooms"]}}
    req = '<span class="req" aria-hidden="true">*</span>'
    opt = f'<span class="opt">({F["optional"]})</span>'
    steps = "".join(f'<li><span class="mono">{i:02d}</span><p>{s}</p></li>' for i, s in enumerate(K["steps"], 1))
    return f"""<section class="ask sec ask-page" id="ask" aria-labelledby="h1">
  <div class="wrap ask-grid">
    <div class="ask-main">
      <header class="sec-hd">
        <p class="ph-sign mono"><a href="{ctx['url']('home')}">Hôtel Lynx</a><span aria-hidden="true">/</span><span><span class="n">{len(t['nav']) + 1:02d}</span> {t['pages']['ask']['crumb']}</span></p>
        <h1 id="h1">{K['h2']}</h1>
        <p class="sec-intro">{K['intro']}</p>
      </header>
      <form class="form" id="ask-form" novalidate>
        <div class="fg fg-2">
          <div class="fld"><label for="f-arr">{F['arrival']}{req}</label><input id="f-arr" name="arrival" type="date" required></div>
          <div class="fld"><label for="f-dep">{F['departure']}{req}</label><input id="f-dep" name="departure" type="date" required></div>
        </div>
        <div class="fg fg-2">
          <div class="fld"><label for="f-gst">{F['guests']}{req}</label><input id="f-gst" name="guests" type="number" inputmode="numeric" min="1" max="12" value="2" required></div>
          <div class="fld"><label for="f-room">{F['room']}</label><select id="f-room" name="room"><option value="">{F['room_any']}</option>{rooms}</select></div>
        </div>
        <div class="fld"><label for="f-time">{F['time']}</label><select id="f-time" name="time">{times}</select></div>
        <div class="checks">
          <label class="chk"><input type="checkbox" name="balcony"><span>{F['balcony']}</span></label>
          <label class="chk"><input type="checkbox" name="parking"><span>{F['parking']}</span></label>
        </div>
        <div class="fld"><label for="f-name">{F['name']}{req}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
        <div class="fg fg-2">
          <div class="fld"><label for="f-mail">{F['email']}{req}</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
          <div class="fld"><label for="f-tel">{F['phone']} {opt}</label><input id="f-tel" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <div class="fld"><label for="f-msg">{F['message']} {opt}</label><textarea id="f-msg" name="message" rows="3" placeholder="{esc(F['message_ph'])}"></textarea></div>
        <button class="btn btn-sig btn-lg btn-wide" type="submit">{ICON['mail']}{F['submit']}</button>
        <p class="fine">{F['fine']}</p>
      </form>
      <div class="done" id="ask-done" hidden tabindex="-1" aria-labelledby="done-h">
        <h2 id="done-h">{D['h']}</h2>
        <p>{D['p']}</p>
        <p class="done-act">{eo(f'<a class="btn btn-sig" id="ask-retry" href="mailto:{site["email"]}">{ICON["mail"]}{D["retry"]}</a>')}</p>
        <div class="done-box">
          <p class="done-k mono">{D['no_app']}</p>
          <dl class="done-to">
            <div><dt class="mono">{D['to']}</dt><dd>{eo(f'<span id="done-email">{site["email"]}</span>')} <button class="btn-mini" type="button" data-copy="email">{ICON['copy']}{D['copy_email']}</button></dd></div>
            <div><dt class="mono">{D['subject']}</dt><dd><span id="done-subject"></span> <button class="btn-mini" type="button" data-copy="subject">{ICON['copy']}{D['copy_email']}</button></dd></div>
          </dl>
          <pre class="done-msg" id="done-body" tabindex="0" aria-label="{esc(D['msg_label'])}"></pre>
          <p class="done-act"><button class="btn btn-ghost" type="button" data-copy="all">{ICON['copy']}{D['copy']}</button>
          <span class="done-copied" id="ask-copied" role="status"></span></p>
        </div>
        <p class="done-call">{D['or_call']} <a class="lnk mono nowrap" href="{tel(site)}">{site['phone_display']}</a></p>
        <p><button class="lnk btn-reset" type="button" id="ask-edit">{D['edit']}</button></p>
      </div>
      <script type="application/json" id="ask-i18n">{json.dumps(dict(i18n, copied=D['copied'], copied_email=D['copied_email'], copied_subject=D['copied_subject'], copy_fail=D['copy_fail']), ensure_ascii=False)}</script>
    </div>
    <div class="ask-aside">
      {side_plate(ctx)}
      <div class="steps">
        <h2 class="steps-h">{K['steps_h']}</h2>
        <ol>{steps}</ol>
      </div>
    </div>
  </div>
</section>"""


def page_home(ctx):
    main = "\n".join(f(ctx) for f in (sec_hero, sec_basics, sec_rooms, sec_agadir, sec_arrive, sec_reviews, sec_ask_mini))
    return document(ctx, main, [hotel_data(ctx)])


# --- rooms page ----------------------------------------------------------------

def page_rooms(ctx):
    site, t = ctx["site"], ctx["t"]
    R, RP = t["rooms"], t["rooms_page"]
    keys = "".join(
        f'<li><a href="#room-{rm["key"]}"><span class="mono">{rm["no"]}</span>{R["items"][rm["key"]]["name"]}</a></li>'
        for rm in site["rooms"])
    side = f'<nav class="ph-keys" aria-label="{esc(RP["head"]["keys_label"])}"><ol>{keys}</ol></nav>'

    every = "".join(f'<li>{ICON["yes"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in RP["every"]["items"])
    E = RP["every"]
    every_sec = f"""<section class="every sec" aria-labelledby="every-h">
  <div class="wrap every-grid">
    <div>
      <p class="kicker mono">{E['kicker']}</p>
      <h2 id="every-h">{E['h2']}</h2>
      <ul class="board-list every-list">{every}</ul>
    </div>
    <figure class="every-fig rv">
      {picture(ctx, 'shower-wc', E['img_alt'], '(min-width: 64rem) 40vw, 100vw')}
      <figcaption>{E['img_cap']}</figcaption>
    </figure>
  </div>
</section>"""

    L = R["labels"]
    entries = []
    for rm in site["rooms"]:
        c = R["items"][rm["key"]]
        cp = RP["items"][rm["key"]]
        gal = cp["photos"]
        figs = []
        for i, ph in enumerate(gal):
            sizes = "(min-width: 64rem) 56vw, 100vw" if i == 0 else "(min-width: 64rem) 27vw, 50vw"
            figs.append(f'<figure class="rg-{"main" if i == 0 else "sub"}">{picture(ctx, ph["img"], ph["alt"], sizes)}'
                        f'<figcaption>{ph["cap"]}</figcaption></figure>')
        if not gal:
            # no photo of this room: a key-tag plate the size of a room photo, not a borrowed bathroom shot
            figs.append(f'<figure class="rg-main"><div class="room-plate"><b aria-hidden="true">{m2(rm["m2"])}</b>'
                        f'<span aria-hidden="true">{c["beds"]}</span><p class="room-plate-note mono">{cp["nophoto"]}</p></div></figure>')
        entries.append(f"""<article class="rm" id="room-{rm['key']}" aria-labelledby="rm-{rm['key']}">
    <div class="rm-hd">
      <span class="room-no mono" aria-hidden="true">{rm['no']}</span>
      <div>
        <h2 id="rm-{rm['key']}">{c['name']}</h2>
        <p class="rm-line">{c['line']}</p>
      </div>
    </div>
    <div class="rm-body">
      <div class="rm-gal rg-{len(figs)}">{''.join(figs)}</div>
      <div class="rm-txt">
        <dl class="room-spec">
          <div><dt class="mono">{L['size']}</dt><dd>{m2(rm['m2'])}</dd></div>
          <div><dt class="mono">{L['sleeps']}</dt><dd>{R['guests'][str(rm['guests'])]}</dd></div>
          <div class="room-beds"><dt class="mono">{L['beds']}</dt><dd>{c['beds']}</dd></div>
        </dl>
        <p>{cp['p']}</p>
        <p class="rm-also mono">{RP['also']}</p>
        <a class="btn btn-sig" href="{ask_href(ctx, rm['key'])}">{L['ask']}{ICON['go']}</a>
      </div>
    </div>
  </article>""")

    N = RP["nots"]
    nots = "".join(f'<li>{ICON["no"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in N["items"])
    B = RP["balcony"]
    nots_sec = f"""<section class="nots sec" id="not" aria-labelledby="not-h">
  <div class="wrap nots-grid">
    <div class="board-col board-no nots-board">
      <p class="board-tag mono"><span>{N['tag']}</span></p>
      <h2 id="not-h">{N['h2']}</h2>
      <ul class="board-list">{nots}</ul>
    </div>
    <figure class="nots-fig rv">
      {picture(ctx, 'stairs', N['img_alt'], '(min-width: 64rem) 28vw, 60vw')}
      <figcaption>{N['img_cap']}</figcaption>
    </figure>
    <div class="balc">
      <p class="kicker mono">{B['kicker']}</p>
      <h2>{B['h2']}</h2>
      <p>{B['p']}</p>
      {quote(ctx, B['quote'])}
      <a class="btn btn-ghost" href="{ask_href(ctx, balcony=True)}">{B['cta']}{ICON['go']}</a>
    </div>
  </div>
</section>"""

    rooms_data = dict(hotel_data(ctx), containsPlace=[
        {"@type": "HotelRoom", "name": R["items"][rm["key"]]["name"],
         "url": site["base_url"] + ctx["url"]("rooms") + f"#room-{rm['key']}",
         "floorSize": {"@type": "QuantitativeValue", "value": rm["m2"], "unitCode": "MTK"},
         "occupancy": {"@type": "QuantitativeValue", "maxValue": rm["guests"]},
         "bed": R["items"][rm["key"]]["beds"],
         "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in t["ld"]["room"]],
         "smokingAllowed": False} for rm in site["rooms"]])
    main = "\n".join([page_head(ctx, side, "ph-rooms"), every_sec,
                      f'<section class="rms" aria-label="{esc(RP["list_label"])}"><div class="wrap">{"".join(entries)}</div></section>',
                      nots_sec, cta_band(ctx, "price")])
    return document(ctx, main, [rooms_data, crumbs(ctx)])


# --- your Agadir page ----------------------------------------------------------

def map_pos(m, ll):
    x = (ll[1] - m["lng0"]) * m["c"] * m["k"]
    y = (m["lat1"] - ll[0]) * m["k"]
    return x, y


def pct(v, total):
    return f"{v / total * 100:.2f}%"


RING_FS = {"door": 18, "city": 17, "city-m": 21}   # ring label size in map units (matches site.css)


def ring_label(m, px, py, r, lbl, fs, avoid, auto):
    """Place a ring label just outside the ring. Fixed maps keep the south-east quarter (the emptiest
    round the hotel); auto maps try other bearings until the label is inside the frame and clear of
    every marker. Returns (x, y) or None (label dropped rather than drawn over a marker)."""
    R = r * m["m"]
    w, h = len(lbl) * fs * .62, fs
    for a in ((135, 160, 110, 200, 225, 250, 90, 60, 300, 330) if auto else (135,)):
        x = px + R * math.sin(math.radians(a)) + 4
        y = py - R * math.cos(math.radians(a)) + 14
        if not auto:
            return x, y
        if x < 4 or x + w > m["w"] - 4 or y - h < 4 or y > m["h"] - 4:
            continue
        cx, cy = min(max(px, x), x + w), min(max(py, y - h), y)
        if math.hypot(cx - px, cy - py) < 28:
            continue
        if all(math.hypot(min(max(ax, x), x + w) - ax, min(max(ay, y - h), y) - ay) > 26 for ax, ay in avoid):
            return x, y
    return None


def map_box(ctx, which, marks, dots, rings, edges, cls="", auto_rings=False):
    """One drawn map: OSM base SVG + rings + HTML markers placed in % so they stay legible.
    Returns (html, marks that fall outside this frame)."""
    m = ctx["map"][which]
    W, H = m["w"], m["h"]
    site = ctx["site"]
    px, py = map_pos(m, [site["geo"]["lat"], site["geo"]["lng"]])
    pad = 14 if auto_rings else 0     # a marker cut by the frame edge counts as off the map
    inside = lambda x, y: pad <= x <= W - pad and pad <= y <= H - pad
    shown, off = [], []
    for mk in marks:
        x, y = map_pos(m, mk["ll"])
        (shown if inside(x, y) else off).append((mk, x, y))
    avoid = [(x, y) for _, x, y in shown]
    fs = RING_FS[which]
    ring_svg = ""
    for r, lbl in rings:
        ring_svg += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * m["m"]:.1f}"/>'
        pos = ring_label(m, px, py, r, lbl, fs, avoid, auto_rings)
        if pos:
            ring_svg += f'<text x="{pos[0]:.1f}" y="{pos[1]:.1f}">{lbl}</text>'
    items = []
    for d in dots:
        x, y = map_pos(m, d["ll"])
        if 0 <= x <= W and 0 <= y <= H:
            items.append(f'<li class="mp-dot mp-{d["kind"]}" style="left:{pct(x, W)};top:{pct(y, H)}" aria-hidden="true"></li>')
    for mk, x, y in shown:
        items.append(f'<li class="mp-n mp-{mk["kind"]}" style="left:{pct(x, W)};top:{pct(y, H)}"><span class="mono">{mk["n"]}</span><span class="sr">{mk["name"]}</span></li>')
    for e in edges:
        x, y = map_pos(m, e["ll"])
        side = "l" if x < 0 else "r"
        yy = min(max(y, H * .1), H * .9)
        items.append(f'<li class="mp-edge mp-edge-{side}" style="top:{pct(yy, H)}"><span>{arrow(e["b"])}<b>{e["name"]}</b> <span class="mono">{e["meta"]}</span></span></li>')
    items.append(f'<li class="mp-pin" style="left:{pct(px, W)};top:{pct(py, H)}"><span>Lynx</span></li>')
    html = f"""<div class="map-box {cls}" style="aspect-ratio:{W}/{H}">
          <img src="/assets/img/map-{which}.svg?v={ctx['v']}" width="{W}" height="{H}" alt="" loading="lazy" decoding="async">
          <svg class="map-rings" viewBox="0 0 {W} {H}" aria-hidden="true">{ring_svg}</svg>
          <ol class="map-pts">{''.join(items)}</ol>
        </div>"""
    return html, [mk for mk, _, _ in off]


def map_figure(ctx, which, marks, dots, rings, edges, title, legend, mobile=None, off_label=""):
    """A map with its title and key. mobile = key of a phone-framed version of the same map (shown
    below 48rem instead of the wide one, so nothing needs sideways scrolling); whatever falls outside
    the phone frame — marks and the edge arrows — is listed under it."""
    box, _ = map_box(ctx, which, marks, dots, rings, edges, "map-box-d" if mobile else "")
    off = ""
    if mobile:
        mbox, out = map_box(ctx, mobile, marks, dots, rings, [], "map-box-m", auto_rings=True)
        box += "\n        " + mbox
        rows = [f'<li>{arrow(mk["b"])}<b><span class="lg lg-n">{mk["n"]}</span>{mk["name"]}</b> <span class="mono">{mk["meta"]}</span></li>' for mk in out]
        rows += [f'<li>{arrow(e["b"])}<b>{e["name"]}</b> <span class="mono">{e["meta"]}</span></li>' for e in edges]
        off = f'<div class="map-off"><p class="mono">{off_label}</p><ul>{"".join(rows)}</ul></div>' if rows else ""
    return f"""<figure class="map map-{which}">
      <figcaption class="map-t"><h3>{title}</h3></figcaption>
      <div class="map-frame">
        {box}
      </div>
      {off}
      <p class="map-leg">{legend}</p>
    </figure>"""


def page_agadir(ctx):
    site, t = ctx["site"], ctx["t"]
    A, AP = t["agadir"], t["agadir_page"]
    P, G = AP["places"], AP["groups"]
    L = AP["labels"]
    route = lambda ll, mode: ("https://www.google.com/maps/dir/?api=1&origin="
                              f"{site['geo']['lat']},{site['geo']['lng']}&destination={ll[0]},{ll[1]}&travelmode={mode}")

    # numbering: everything with a single location that is drawn on a map
    n, num = 0, {}
    for g in site["near"]:
        for it in g["items"]:
            if it.get("ll") and not it.get("edge"):
                n += 1
                num[it["key"]] = n

    side = f"""<figure class="ph-fig">
      {picture(ctx, 'view', AP['head']['img_alt'], '(min-width: 64rem) 40vw, 100vw', eager=True)}
      <figcaption>{AP['head']['img_cap']}</figcaption>
    </figure>"""
    chips = "".join(f'<li><a href="#{g["group"]}"><span class="mono">{i:02d}</span>{G[g["group"]]["h2"]}</a></li>'
                    for i, g in enumerate(site["near"], 1))

    # maps
    door_marks = [{"ll": it["ll"], "n": num[it["key"]], "name": P[it["key"]]["name"], "kind": g["group"]}
                  for g in site["near"] for it in g["items"] if it["key"] == "mosque"]
    dots = [{"ll": d, "kind": g["group"]} for g in site["near"] for it in g["items"] for d in it.get("dots", [])]
    city_marks = [{"ll": it["ll"], "n": num[it["key"]], "name": P[it["key"]]["name"], "kind": g["group"],
                   "b": bearing(site, it["ll"]), "meta": f'{it["walk"]}&nbsp;{L["min_walk"]}'}
                  for g in site["near"] for it in g["items"] if it["key"] in num and it["key"] != "mosque"]
    edges = []
    for g in site["near"]:
        for it in g["items"]:
            if it.get("edge"):
                edges.append({"ll": it["ll"], "b": bearing(site, it["ll"]), "name": P[it["key"]]["short"],
                              "meta": f'{L["about"]} {it["taxi"]}&nbsp;{A["min"]} {L["by_taxi"]}'})
    M = AP["maps"]
    maps = f"""<section class="maps sec" id="map" aria-labelledby="map-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{M['kicker']}</p>
      <h2 id="map-h">{M['h2']}</h2>
      <p class="sec-intro">{M['intro']}</p>
    </header>
    <div class="maps-grid">
      {map_figure(ctx, 'door', door_marks, dots, [(100, '100 m'), (250, '250 m'), (500, '500 m')], [], M['door_t'], M['door_leg'])}
      {map_figure(ctx, 'city', city_marks, [], [(500, '500 m'), (1000, '1 km'), (2000, '2 km')], edges, M['city_t'], M['city_leg'], mobile='city-m', off_label=M['off'])}
    </div>
    <p class="maps-foot">{ext(ctx, site['maps_url'], ICON['pin'] + M['gmaps'], 'btn btn-ghost')}<span class="mut">{M['credit']}</span></p>
  </div>
</section>"""

    groups = []
    for gi, g in enumerate(site["near"], 1):
        gc = G[g["group"]]
        rows = []
        for it in g["items"]:
            p = P[it["key"]]
            if it.get("walk"):
                big = f'{it["walk"]}<small>{L["min_walk"]}</small>'
            elif it.get("taxi"):
                big = f'<em>~</em>{it["taxi"]}<small>{L["min_taxi"]}</small>'
            else:
                big = f'<small class="rt-word">{L["anytime"]}</small>'
            meta = []
            if it.get("dist"):
                d = (L["from"] + " " if it.get("from") else "") + dist(ctx, it["dist"])
                meta.append(d + (arrow(bearing(site, it["ll"])) if it.get("ll") else ""))
            if it.get("taxi") and it.get("walk"):
                meta.append(f'{L["about"]} {it["taxi"]}&nbsp;{A["min"]} {L["by_taxi"]}')
            if it.get("ll"):
                mode = "walking" if it.get("walk") else "driving"
                meta.append(ext(ctx, route(it["ll"], mode), L["route"], "rt-route"))
            badge = f'<span class="rt-n mono" aria-hidden="true">{num[it["key"]]}</span>' if it["key"] in num else ""
            note = f'<p>{p["note"]}</p>' if p.get("note") else ""
            rows.append(f"""<li class="rt{' rt-taxi' if not it.get('walk') else ''}">
          <span class="rt-min mono">{big}</span><span class="rt-dot" aria-hidden="true"></span>
          <div class="rt-txt"><h3>{badge}{p['name']}</h3>{note}<p class="rt-meta mono">{'<span aria-hidden="true"> · </span>'.join(meta)}</p></div>
        </li>""")
        extra = quote(ctx, gc["quote"], "q rt-q") if gc.get("quote") else ""
        groups.append(f"""<section class="grp grp-{g['group']}" id="{g['group']}" aria-labelledby="g-{g['group']}">
      <header class="grp-hd">
        <p class="grp-tag mono">{gi:02d}</p>
        <h2 id="g-{g['group']}">{gc['h2']}</h2>
        <p>{gc['intro']}</p>
      </header>
      <ol class="route">{''.join(rows)}</ol>
      {extra}
    </section>""")

    main = "\n".join([
        page_head(ctx, side, "ph-agadir"),
        f'<nav class="chips" aria-label="{esc(AP["chips_label"])}"><div class="wrap"><ol>{chips}</ol></div></nav>',
        maps,
        f'<div class="grps"><div class="wrap grps-grid">{"".join(groups)}</div></div>',
        cta_band(ctx, "agadir")])
    return document(ctx, main, [crumbs(ctx)])


# --- practical page -------------------------------------------------------------

def page_basics(ctx):
    site, t = ctx["site"], ctx["t"]
    BP = t["basics_page"]
    a = site["address"]
    W = BP["ways"]
    ways = "".join(f'<li class="way"><h3><span class="mono">{w["k"]}</span>{w["t"]}</h3><p>{w["d"]}</p></li>' for w in W["items"])
    getting = f"""<section class="ways sec" id="getting-here" aria-labelledby="ways-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{W['kicker']}</p>
      <h2 id="ways-h">{W['h2']}</h2>
      <p class="sec-intro">{W['intro']}</p>
    </header>
    <div class="ways-grid">
      <div class="addr-plate">
        <p class="mono addr-k">{W['addr_k']}</p>
        <p class="addr">{a['street']}<br>{a['district']}, {a['postcode']} {a['city']}</p>
        <p class="addr-note">{t['footer']['address_note']}</p>
        {ext(ctx, site['maps_url'], ICON['pin'] + t['footer']['map'], 'btn btn-sig')}
      </div>
      <ol class="way-list">{ways}</ol>
    </div>
  </div>
</section>"""
    R = BP["rules"]
    rules = "".join(f'<li>{ICON["no" if r.get("no") else "yes"]}<div><h3>{r["t"]}</h3><p>{r["d"]}</p></div></li>' for r in R["items"])
    F = BP["faq"]
    faq = "".join(f'<details class="qa"><summary><h3>{q["q"]}</h3></summary><div class="qa-a"><p>{q["a"]}</p></div></details>' for q in F["items"])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": strip_tags(q["a"])}} for q in F["items"]]}
    rest = f"""<section class="rules sec" id="rules" aria-labelledby="rules-h">
  <div class="wrap rules-grid">
    <div>
      <p class="kicker mono">{R['kicker']}</p>
      <h2 id="rules-h">{R['h2']}</h2>
      <ul class="board-list rules-list">{rules}</ul>
    </div>
    <div class="faq" id="faq">
      <p class="kicker mono">{F['kicker']}</p>
      <h2>{F['h2']}</h2>
      {faq}
    </div>
  </div>
</section>"""
    call = (f'<a class="ph-call" href="{tel(site)}"><span class="mono">{t["ask"]["side"]["call"]}</span>'
            f'<b class="mono">{site["phone_display"]}</b></a>')
    main = "\n".join([page_head(ctx, call, "ph-basics"), sec_arrive(ctx, more=False, eager=True, brief=True), getting, rest, cta_band(ctx, "basics")])
    return document(ctx, main, [faq_ld, crumbs(ctx)])


def strip_tags(s):
    """Plain text for JSON-LD: a trailing " — <a>see where</a>" pointer means nothing without its link."""
    s = re.sub(r"\s*—\s*<a\b[^>]*>.*?</a>", "", s)
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ")


# --- ask page -------------------------------------------------------------------

def page_ask(ctx):
    return document(ctx, sec_ask(ctx), [crumbs(ctx)])


# --- 404 --------------------------------------------------------------------------

def page_404(ctx):
    site, t = ctx["site"], ctx["t"]
    n, fr = t["notfound"], ctx["fr"]["notfound"]
    main = f"""<section class="nf sec"><div class="wrap">
  <p class="kicker mono">404</p>
  <h1>{n['h1']}</h1>
  <p class="sec-intro">{n['p']}</p>
  <p class="nf-fr" lang="fr"><b>{fr['h1']}</b> {fr['p']} <a class="lnk" href="{ctx['fr_home']}">{fr['home']}</a></p>
  <p class="hero-cta"><a class="btn btn-sig btn-lg" href="{ctx['url']('home')}">{n['home']}{ICON['go']}</a>
  <a class="btn btn-ghost btn-lg" href="{tel(site)}">{ICON['phone']}{site['phone_display']}</a></p>
</div></section>"""
    ctx["title"], ctx["description"], ctx["noindex"] = n["title"], n["description"], True
    return document(ctx, main)
