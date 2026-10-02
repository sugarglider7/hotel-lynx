# BUILD STATUS — hotel-lynx

_Last updated: 2026-10-02 07:20 UTC by BuildLynx (phase 3: EN + FR built, QA rounds next)_

## Recovered state (resume of crashed run "agadir-batch2")
- Prior run left ONLY raw material (no repo, no status files, no code, no deployment):
  raw page dumps + downloaded images, now in `research/raw/` (gitignored; on disk at /home/agent/agadir-pilot/sites/hotel-lynx/research/raw/). Original copy still at /tmp/sites2/hotel-lynx/.
- Confirmed on 2026-10-02: no GitHub repo, no Cloudflare Pages project, no live hotel-lynx.peashoot.io before this run.

## Orchestrator review (phase 2 → phase 3, binding)
- Homepage proof approved: "Signposted" concept, Overpass/Overpass Mono, façade + black band, transit-line "Your Agadir from Lynx". Keep it.
- Fix: "free parking by the door" overstates — use "free public parking right by the hotel" (hero + anywhere else).
- Fix: the "Or hop in a petit taxi" grid includes Al Massira airport — petit taxis don't serve the airport (grand taxi / arranged taxi). Retitle to something like "By taxi" and keep times "by road, traffic permitting"; airport line = "about 30 min by taxi — we can book one".
- Phase 3 must add the dedicated pages from the page map (rooms, your Agadir, practical/getting here, ask for a room, reviews if planned) + full FR mirror; keep homepage sections as summaries linking to them, not duplicates.
- No WhatsApp anywhere until the owner gives a mobile number (decision stands).
- Live: https://hotel-lynx.peashoot.io/ (Cloudflare Pages project hotel-lynx, output dir site/, auto-deploys on push to main).

## Research
- **Phase 1 research DONE (2026-10-02).**
- SOURCE_OF_TRUTH.md — done: 15 sources, contact block, facts tagged, ratings, people, 12 quotes, 12 owner questions.
- CONTENT_INVENTORY.md — done: per page/section ✅/🟡/⛔ lines with tags.
- ASSET_INVENTORY.md — done: 27 unique Booking photos (2048 px originals downloaded as `research/raw/images/bk2048_*`), 27 `hr_*` = affiliate duplicates (DO-NOT-USE), Best 12 + gaps.
- research/notes-rooms.md (room table + photo↔room mapping), notes-reviews.md (themes, staff names), notes-neighbourhood.md (pin verification + OSRM table).
- Key facts: 5 room types (Single 15 m² · Superior Single 16 m² · Twin 20 m² · Double 20 m² · Triple 20 m²); **no breakfast** (verified); free public parking; 24 h desk; no lift; Booking 8.4/1,009 (Staff 9.2, Clean 8.9, Value 8.8, Location 8.9, Wi-Fi 9.5); Google 4.1/241.

## Design
- **Phase 2 DONE.** BRAND_NOTES.md: concept "Signposted" (the hotel's own sign system: façade photo → black fascia hero, fingerposts with real bearings, the Lynx Line walking-minute transit map, key-tag room directory, yes/no board), palette sampled from bk_01/05/12/14, Overpass + Overpass Mono (self-hosted, registered in FONTS.md), page map EN/FR, section plans, conversion spec + EN/FR mail templates, must-not list.
- Tooling: `tools/images.py` (Pillow, sequential, declarative list → `site/assets/img/*.webp` + `tools/images.manifest.json` + og image + favicons), `tools/build.py` (stdlib; `content/site.json` facts + `content/<lang>.json` copy + `tools/templates.py` partials/pages → `site/`; also 404, sitemap, robots, _headers). Rebuild: `python3 tools/images.py && python3 tools/build.py`. **Edit content/templates, never site/*.html by hand.**
- `site/assets/css/site.css` (26 KB, tokens + components), `site/assets/js/site.js` (8 KB: menu, sticky bar, reveal, mailto composer), favicon.svg/32/180.
- Phase 3 adding a page: add renderer to `PAGES` in build.py + `slug` under `pages.<key>` in each content file; nav/hreflang/lang switch update automatically (unbuilt pages fall back to homepage anchors). FR: create `content/fr.json` (same keys, `dir: "/fr/"`, `date_locale: "fr-FR"`).

## Pages implemented
- Phase 3 (EN, 06:45): `/rooms/`, `/your-agadir/` (two self-drawn OSM maps: `tools/mapdata.py` → `site/assets/img/map-{door,city}.svg` + `content/map.json`; HTML markers placed from `content/site.json` → `near`), `/practical/`, `/ask/` (full form + robust success panel). Homepage sections now summaries linking to these pages; homepage ask = dates mini-form (GET → /ask/ prefill).
- `/` EN homepage (final quality): hero/fascia · The deal (yes/no) · Rooms 01–05 · Your Agadir from Lynx (Lynx Line + taxi branch) · Getting in · Reviews · Ask for a room (form → composed email) · footer. JSON-LD Hotel with aggregateRating 8.4/1,009.
- `/404.html` (EN shell).

## Pages remaining
- EN: `/rooms/`, `/your-agadir/`, `/practical/`, `/ask/` (until built, nav links go to homepage anchors).
- FR: `/fr/`, `/fr/chambres/`, `/fr/votre-agadir/`, `/fr/infos-pratiques/`, `/fr/demande/` (+ bilingual 404 line, language switch appears automatically once fr.json exists).

## Factual uncertainties
- **Map pin**: Booking's coordinates are the "Swiss City" district centroid (821 m off). Use Google pin 30.4228588, -9.5917027 (verified against OSM street + mosque).
- **WhatsApp**: no number exists publicly; phone is a landline (05 28 84 78 86). Conversion must be tel/mailto/Booking unless owner provides a mobile.
- **Email**: agadir.hlynx@gmail.com (Booking trader record, use) vs agadirhotellynx@gmail.com (old directory).
- **Children**: Booking says "children not allowed", but 46 "family" reviews exist → omit; ask owner.
- **Payment**: Booking says cash only → confirm before publishing.
- **Stars**: 2★ (Booking, Google, Priceline) vs "3*" (Telecontact) → use 2★.
- **Room count** 41 only from affiliate template → don't publish.
- **Staff names** Rachid / Ahmed (~15 independent reviews each), Hicham (2): roles inconsistent → no titles; owner consent needed.
- No photo of the Single room; no neighbourhood/street photos; no official socials or website.
- Noise (mosque call to prayer, street) and dated furniture are recurring criticisms → never "quiet", "modern", "renovated".

## QA status
- Phase 2: check_site OK (2 pages; contacts = tel:+212528847886, mailto:agadir.hlynx@gmail.com only; 0 WARN). Screenshots `/home/agent/agadir-pilot/qa/hotel-lynx/p2/` (round1–3, 390 + 1440, fold + full, menu, form errors/done, 404).
- Verified in one browser tab: no horizontal overflow at 360/390/430; menu aria-expanded/Esc/focus/close-on-link; room "Ask for this room" preselects the form; validation messages; composed mailto decoded correctly (no undefined/NaN); 0 console errors (only the expected headless mailto abort); cold mobile first load 169 KB (html 40, css 26, js 8, fonts 61, hero 34 KB), LCP = hero webp, CLS 0.
- Full QA_CHECKLIST pass still to do in phase 4.

## Deployment URL
- target: https://hotel-lynx.peashoot.io/ (Cloudflare Pages project "hotel-lynx", output dir `site/`, no build command) — not yet created

## Outstanding problems
- Owner permission for the Booking gallery photos (SOT Q11) and naming staff (not used yet — no staff names on the site).
- Local preview has no custom 404 (python http.server); Cloudflare Pages serves `site/404.html`.

## Log
- 07:20 FR mirror: content/fr.json (all 5 pages, natural French, FR quotes from Booking where they exist, EN quotes kept in English with lang=en), decimal commas, FR mail template; header de-crowded (2-letter lang switch, phone number ≥88rem); no overflow 360–1440 on all 11 pages; check_site OK (11 pages).
- 06:45 phase 3: orchestrator fixes applied ("free public parking right by the hotel", taxi grid → "By taxi", airport "about 30 min by taxi — we can book one"); EN rooms/your-agadir/practical/ask built; images +6 (bk_19/25/18/03/14/09); Overpass roads/coast/near streets fetched to research/raw for the maps; check_site OK.
- 05:08 recovery: workspace created from prior raw research; brief + standard written.
- 05:20 research: Booking page + Apollo state parsed (rooms, sizes, beds, policies, trader contact); 377 Booking reviews captured via one browser tab; Google 4.1/241 + 30 reviews; tab closed.
- 05:28 research: pin verified (Google vs Booking), OSRM foot/car table for 37 places; hr_ images identified as pixcdn affiliate copies of Booking photos.
- 05:35 research: SOURCE_OF_TRUTH, CONTENT_INVENTORY, ASSET_INVENTORY, notes-* written; committed + pushed.
- 05:40 design: read contract/brief/SOT/assets; looked at sheets + full bk2048 images; palette sampled with Pillow; Overpass/Overpass Mono fetched (4 woff2) and registered in FONTS.md.
- 05:55 build: images.py, build.py, templates.py, content/site.json + en.json, site.css, site.js, favicons; check_site OK.
- 05:57 round 1 (390 + 1440): strong fascia hero; problems — full-page shots missed lazy images (scroll helper didn't await), desktop hero photo too tall (h1 pushed below fold), ghost buttons' chamfer clipped the border, mobile header "CALL 24H" wrapped, "Mohammed / V" orphan, Overpass "·" eats the following space, desktop rooms too tall/sparse, line axis label overlapped stop labels, terrace crop lost the minaret, 4-up facts wrapped. Fixed all: hero photo 44vh, ghost buttons unchamfered, nbsp, mono separators, compact room rows (3:2, 3-col specs), desktop 2-col section headers, terrace object-position, 2×2 facts.
- 06:03 round 2: mobile header overflowed (Menu cut off) → ≤26rem shows "☎ 24h" + burger only; line extra/axis overlap → axis label moved top-left, notes hidden on desktop, line widened; success panel phone wrapped; email dates were US style → en-GB date locale; success copy no longer promises a reply. Functional checks passed (menu, preselect, validation, mailto).
- 06:08 round 3 (final): 390/1440 fold + full clean; 404 checked; tab closed; preview stopped.
