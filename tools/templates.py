"""HTML templates/partials for hotel-lynx. Pure functions: (ctx) -> str.

ctx keys (built by tools/build.py):
  site  content/site.json (language-independent facts)
  t     content/<lang>.json (copy for one language)
  img   tools/images.manifest.json
  page  page key ("home", ...)
  url   helper: url(page_key, anchor=None) -> href valid for this language,
        falling back to a homepage anchor while a page is not built yet
  alt   {lang: href} of this page in every built language (hreflang + switch)
Copy strings are trusted HTML (may contain <br>, &nbsp;); attribute values go
through esc().
"""
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
}


def arrow(bearing):
    return ARROW.format(b=bearing) if bearing is not None else ""


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
        mv = m["mobile"][0]
        return (f'<picture><source media="(max-width: 47.99rem)" srcset="/assets/img/{mv["file"]} {mv["w"]}w" '
                f'sizes="100vw" width="{mv["w"]}" height="{mv["h"]}">{img}</picture>')
    return f"<picture>{img}</picture>"


def tel(site):
    return "tel:" + site["phone_e164"]


# --- document shell -----------------------------------------------------------

def head(ctx, title, description, path):
    site, t = ctx["site"], ctx["t"]
    canonical = site["base_url"] + path
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{site["base_url"]}{h}">' for l, h in ctx["alt"].items())
    if len(ctx["alt"]) > 1:
        alts += f'<link rel="alternate" hreflang="x-default" href="{site["base_url"]}{ctx["alt"]["en"]}">'
    og = site["base_url"] + "/assets/img/" + ctx["img"]["og-facade"]["file"]
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">{alts}
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
<meta name="twitter:card" content="summary_large_image">
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


def lang_switch(ctx):
    others = [(l, h) for l, h in ctx["alt"].items() if l != ctx["t"]["lang"]]
    if not others:
        return ""
    l, h = others[0]
    return f'<a class="lang" href="{h}" hreflang="{l}" lang="{l}">{ctx["t"]["ui"]["switch_label"]}</a>'


def header(ctx):
    site, t = ctx["site"], ctx["t"]
    links = "".join(
        f'<li><a href="{ctx["url"](n["page"], n["anchor"])}"><span class="n">{i:02d}</span>{n["label"]}</a></li>'
        for i, n in enumerate(t["nav"], 1))
    ask = ctx["url"]("ask", "ask")
    return f"""<a class="skip" href="#main">{t['ui']['skip']}</a>
<header class="hd" id="top">
  <div class="hd-in">
    {wordmark(ctx)}
    <nav class="hd-nav" aria-label="{esc(t['ui']['nav_label'])}">
      <ul>{links}</ul>
    </nav>
    <div class="hd-act">
      {lang_switch(ctx)}
      <a class="hd-tel" href="{tel(site)}" aria-label="{esc(t['ui']['call_reception'] + ': ' + site['phone_display'])}">{ICON['phone']}<span class="hd-tel-l"><span class="hd-c">{t['ui']['call']} </span>{t['ui']['h24']}</span><span class="hd-tel-n">{site['phone_display']}</span></a>
      <a class="btn btn-sig hd-ask" href="{ask}">{t['ui']['ask']}</a>
      <button class="hd-menu" type="button" aria-expanded="false" aria-controls="menu"><span class="hd-menu-l">{t['ui']['menu']}</span><span class="burger" aria-hidden="true"></span></button>
    </div>
  </div>
  <div class="menu" id="menu" hidden>
    <ul class="menu-list">{links}<li><a href="{ask}"><span class="n">{len(t['nav']) + 1:02d}</span>{t['ui']['ask']}</a></li></ul>
    <div class="menu-foot">
      <a class="btn btn-sig" href="{tel(site)}">{ICON['phone']}{t['ui']['call_reception']}</a>
      <a class="menu-mail" href="mailto:{site['email']}">{site['email']}</a>
      {lang_switch(ctx)}
    </div>
  </div>
</header>"""


def footer(ctx):
    site, t = ctx["site"], ctx["t"]
    f = t["footer"]
    a = site["address"]
    return f"""<footer class="ft" id="contact">
  <div class="ft-in">
    <div class="ft-brand">{wordmark(ctx, tag="span")}<p class="ft-class">{f['class']} · ★★</p></div>
    <address class="ft-addr">
      <p>{a['street']}<br>{a['district']}, {a['postcode']} {a['city']}<br><span class="mut">{f['address_note']}</span></p>
      <p><a class="lnk" href="{site['maps_url']}" rel="noopener" target="_blank">{f['map']}<span class="sr"> ({t['ui']['new_tab']})</span></a></p>
    </address>
    <div class="ft-contact">
      <p><a class="ft-tel" href="{tel(site)}">{site['phone_display']}</a><span class="mut mono"> · 24h</span></p>
      <p><a class="lnk" href="mailto:{site['email']}">{site['email']}</a></p>
      <p><a class="lnk" href="{site['booking_url']}" rel="noopener" target="_blank">Booking.com<span class="sr"> ({t['ui']['new_tab']})</span></a></p>
    </div>
    <p class="ft-times mono">{f['times']}</p>
    <p class="ft-copy mut">© {f['copy']}{(' — ' + lang_switch(ctx)) if lang_switch(ctx) else ''}</p>
  </div>
</footer>"""


def sticky(ctx):
    site, t = ctx["site"], ctx["t"]
    return f"""<div class="sticky" data-sticky>
  <a class="btn btn-ghost-d" href="{tel(site)}">{ICON['phone']}{t['sticky']['call']}</a>
  <a class="btn btn-sig" href="{ctx['url']('ask', 'ask')}">{t['sticky']['ask']}</a>
</div>"""


def jsonld_hotel(ctx):
    import json
    site, t = ctx["site"], ctx["t"]
    a, r = site["address"], site["rating"]["booking"]
    data = {
        "@context": "https://schema.org", "@type": "Hotel",
        "name": site["name"], "url": site["base_url"] + "/",
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
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in
                           ("Free Wi-Fi", "Free parking", "Air conditioning", "24-hour front desk", "Room service", "Rooftop terrace", "Non-smoking rooms")],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": r["score"], "bestRating": "10", "worstRating": "1", "reviewCount": r["count"]},
        "sameAs": [site["booking_url"]],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def document(ctx, title, description, path, main):
    return (head(ctx, title, description, path) + "\n<body>\n" + header(ctx) +
            f'\n<main id="main">\n{main}\n</main>\n' + footer(ctx) + "\n" + sticky(ctx) + "\n</body>\n</html>\n")


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
          <a class="btn btn-sig btn-lg" href="{ctx['url']('ask', 'ask')}">{t['ui']['ask']}{ICON['go']}</a>
          <a class="btn btn-ghost-d btn-lg" href="{tel(site)}">{ICON['phone']}{t['ui']['call_reception']}</a>
        </div>
        <a class="score" href="{ctx['url']('reviews', 'reviews')}">
          <span class="score-n">{r['score']}</span>
          <span class="score-t"><b>{h['rating_label']}</b><span>{h['rating_count']}</span></span>
          <span class="score-s"><b>{staff}</b><span>{h['staff_label']}</span></span>
        </a>
      </div>
    </div>
  </div>
</section>"""


def sec_basics(ctx):
    t = ctx["t"]
    b = t["basics"]
    yes = "".join(f'<li>{ICON["yes"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in b["yes"])
    no = "".join(f'<li>{ICON["no"]}<div><h3>{i["t"]}</h3><p>{i["d"]}</p></div></li>' for i in b["no"])
    return f"""<section class="basics sec" id="basics" aria-labelledby="basics-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{b['kicker']}</p>
      <h2 id="basics-h">{b['h2']}</h2>
      <p class="sec-intro">{b['intro']}</p>
    </header>
    <div class="board">
      <div class="board-col board-yes">
        <p class="board-tag mono"><span>{b['yes_label']}</span></p>
        <ul class="board-list">{yes}</ul>
      </div>
      <div class="board-col board-no">
        <p class="board-tag mono"><span>{b['no_label']}</span></p>
        <ul class="board-list">{no}</ul>
        <figure class="board-fig rv">
          {picture(ctx, 'reception', b['img_alt'], '(min-width: 64rem) 30vw, 100vw')}
          <figcaption>{b['img_cap']}</figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>"""


def sec_rooms(ctx):
    site, t = ctx["site"], ctx["t"]
    R = t["rooms"]
    L = R["labels"]
    rows = []
    for rm in site["rooms"]:
        c = R["items"][rm["key"]]
        rows.append(f"""<li class="room rv" id="room-{rm['key']}">
      <div class="room-key"><span class="room-no mono">{rm['no']}</span></div>
      <div class="room-txt">
        <h3>{c['name']}</h3>
        <p class="room-line">{c['line']}</p>
        <dl class="room-spec">
          <div><dt class="mono">{L['size']}</dt><dd>{rm['m2']}&nbsp;m²</dd></div>
          <div><dt class="mono">{L['sleeps']}</dt><dd>{R['guests'][str(rm['guests'])]}</dd></div>
          <div class="room-beds"><dt class="mono">{L['beds']}</dt><dd>{c['beds']}</dd></div>
        </dl>
        <a class="lnk room-ask" href="{ctx['url']('ask', 'ask')}" data-room="{rm['key']}">{L['ask']}{ICON['go']}</a>
      </div>
      <figure class="room-fig">
        {picture(ctx, rm['img'], c['alt'], '(min-width: 64rem) 34vw, 100vw')}
        <figcaption>{c['cap']}</figcaption>
      </figure>
    </li>""")
    notes = "".join(f"<li>{n}</li>" for n in R["notes"])
    return f"""<section class="rooms sec" id="rooms" aria-labelledby="rooms-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{R['kicker']}</p>
      <h2 id="rooms-h">{R['h2']}</h2>
      <p class="sec-intro">{R['intro']}</p>
    </header>
    <ol class="room-list">
    {''.join(rows)}
    </ol>
    <ul class="room-notes">{notes}</ul>
  </div>
</section>"""


def sec_agadir(ctx):
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
            f'<span class="stop-min mono">{w["min"]}<small>{A["min"]}</small></span>'
            f'<span class="stop-dot" aria-hidden="true"></span>'
            f'<span class="stop-lbl"><b>{p["name"]}</b>{note}<span class="stop-meta mono">{w["dist"]}{arrow(w.get("bearing"))}</span></span></li>')
    minor = [w for w in site["walk"] if w.get("list_only")]
    extra = '<span class="mono"> · </span>'.join(
        f'{P[w["key"]]["name"]} <span class="mono">{w["min"]}&nbsp;{A["min"]}, {w["dist"]}</span>' for w in minor)
    rides = "".join(
        f'<li class="ride"><span class="ride-min mono"><small>{A["ride_about"]}</small>{r["min"]}<small>{A["min"]}</small></span>'
        f'<span class="ride-lbl"><b>{P[r["key"]]["name"]}</b><span class="mono">{r["dist"]}{arrow(r.get("bearing"))}</span></span></li>'
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
    <div class="line" style="--span:{span}">
      <p class="line-axis mono" aria-hidden="true">{A['axis_label']}</p>
      <ol class="stops">
        <li class="stop stop-origin" style="--m:0;--gap:0"><span class="stop-min mono">0<small>{A['min']}</small></span><span class="stop-dot" aria-hidden="true"></span><span class="stop-lbl"><b>{A['origin']}</b><span class="stop-meta mono">{A['origin_sub']}</span></span></li>
        {''.join(stops)}
      </ol>
      <p class="line-extra">{extra}</p>
      <p class="line-note mono">{arrow(45)} {A['arrow_note']}</p>
    </div>
    <div class="rides">
      <h3>{A['ride_h']}</h3>
      <ul>{rides}</ul>
      <p class="mut">{A['ride_note']}</p>
    </div>
  </div>
</section>"""


def sec_arrive(ctx):
    site, t = ctx["site"], ctx["t"]
    A = t["arrive"]
    facts = "".join(f'<div><dt class="mono">{f["k"]}</dt><dd>{f["v"]}</dd></div>' for f in A["facts"])
    return f"""<section class="arrive" id="arrive" aria-labelledby="arrive-h">
  <div class="arrive-in">
    <figure class="arrive-fig rv">
      {picture(ctx, 'facade-night', A['img_alt'], '(min-width: 64rem) 55vw, 100vw')}
      <figcaption>{A['img_cap']}</figcaption>
    </figure>
    <div class="arrive-txt">
      <p class="kicker mono">{A['kicker']}</p>
      <h2 id="arrive-h">{A['h2']}</h2>
      <p>{A['p1']}</p>
      <p>{A['p2']}</p>
      <dl class="facts">{facts}</dl>
    </div>
  </div>
</section>"""


def sec_reviews(ctx):
    site, t = ctx["site"], ctx["t"]
    V, r = t["reviews"], site["rating"]["booking"]
    bars = "".join(
        f'<li style="--v:{v}"><span>{V["sub_labels"][k]}</span><b class="mono">{v}</b><i aria-hidden="true"></i></li>'
        for k, v in r["sub"])
    lq = V["lead_quote"]
    quotes = "".join(
        f'<figure class="q rv"><blockquote><p>“{q["q"]}”</p></blockquote><figcaption><b>{q["who"]}</b> · {q["src"]}</figcaption></figure>'
        for q in V["quotes"])
    return f"""<section class="reviews sec" id="reviews" aria-labelledby="reviews-h">
  <div class="wrap">
    <header class="sec-hd">
      <p class="kicker mono">{V['kicker']}</p>
      <h2 id="reviews-h">{V['h2']}</h2>
    </header>
    <div class="rv-grid">
      <div class="scorecard">
        <p class="sc-big"><span class="sc-n">{r['score']}</span><span class="sc-of mono">/10</span></p>
        <p class="sc-src"><b>{V['score_label']}</b>, {r['count_display']} {V['count_label']}</p>
        <ul class="bars">{bars}</ul>
        <p class="mut sc-g">{V['google']}</p>
      </div>
      <div class="quotes">
        <figure class="q q-lead"><blockquote><p>“{lq['q']}”</p></blockquote><figcaption><b>{lq['who']}</b> · {lq['src']}</figcaption></figure>
        {quotes}
      </div>
    </div>
  </div>
</section>"""


def sec_ask(ctx):
    import json
    site, t = ctx["site"], ctx["t"]
    K = t["ask"]
    F = K["f"]
    rooms = "".join(f'<option value="{rm["key"]}">{t["rooms"]["items"][rm["key"]]["name"]}</option>' for rm in site["rooms"])
    times = "".join(f"<option>{o}</option>" for o in F["time_opts"])
    i18n = {"err": K["err"], "mail": K["mail"], "done": K["done"], "email": site["email"], "lang": t["date_locale"],
            "room_any": F["room_any"],
            "rooms": {rm["key"]: t["rooms"]["items"][rm["key"]]["name"] for rm in site["rooms"]}}
    req = '<span class="req" aria-hidden="true">*</span>'
    opt = f'<span class="opt">({F["optional"]})</span>'
    return f"""<section class="ask sec" id="ask" aria-labelledby="ask-h">
  <div class="wrap ask-grid">
    <div class="ask-main">
      <header class="sec-hd">
        <p class="kicker mono">{K['kicker']}</p>
        <h2 id="ask-h">{K['h2']}</h2>
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
      <div class="done" id="ask-done" hidden tabindex="-1">
        <h3>{K['done']['h']}</h3>
        <p>{K['done']['p']}</p>
        <p class="done-act"><a class="btn btn-sig" id="ask-retry" href="mailto:{site['email']}">{ICON['mail']}{K['done']['retry']}</a>
        <button class="btn btn-ghost" type="button" id="ask-copy">{K['done']['copy']}</button></p>
        <p class="done-copied" id="ask-copied" hidden>{K['done']['copied']} <a class="lnk" href="mailto:{site['email']}">{site['email']}</a></p>
        <p>{K['done']['or_call']} <a class="lnk mono nowrap" href="{tel(site)}">{site['phone_display']}</a></p>
      </div>
      <script type="application/json" id="ask-i18n">{json.dumps(i18n, ensure_ascii=False)}</script>
    </div>
    <aside class="ask-side" aria-label="{esc(K['side']['h'])}">
      <h3>{K['side']['h']}</h3>
      <a class="side-tel" href="{tel(site)}"><span class="mono">{K['side']['call']}</span><b>{site['phone_display']}</b></a>
      <a class="side-row" href="mailto:{site['email']}"><span class="mono">{K['side']['email']}</span><b>{site['email']}</b></a>
      <a class="side-row" href="{site['booking_url']}" rel="noopener" target="_blank"><span class="mono">{K['side']['booking']}</span><b>{K['side']['booking_sub']} {ICON['out']}</b><span class="sr"> ({t['ui']['new_tab']})</span></a>
    </aside>
  </div>
</section>"""


def page_home(ctx):
    p = ctx["t"]["pages"]["home"]
    ctx["head_extra"] = jsonld_hotel(ctx)
    main = "\n".join(f(ctx) for f in (sec_hero, sec_basics, sec_rooms, sec_agadir, sec_arrive, sec_reviews, sec_ask))
    return document(ctx, p["title"], p["description"], ctx["alt"][ctx["t"]["lang"]], main)


def page_404(ctx):
    site, t = ctx["site"], ctx["t"]
    n = t["notfound"]
    main = f"""<section class="nf sec"><div class="wrap">
  <p class="kicker mono">404</p>
  <h1>{n['h1']}</h1>
  <p class="sec-intro">{n['p']}</p>
  <p class="hero-cta"><a class="btn btn-sig btn-lg" href="{ctx['url']('home')}">{n['home']}{ICON['go']}</a>
  <a class="btn btn-ghost btn-lg" href="{tel(site)}">{ICON['phone']}{site['phone_display']}</a></p>
</div></section>"""
    return document(ctx, n["title"], t["pages"]["home"]["description"], "/404.html", main)
