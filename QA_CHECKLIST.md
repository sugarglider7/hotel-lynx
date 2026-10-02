# QA_CHECKLIST — hotel-lynx (phase 3, 2026-10-02)

Tags refer to `SOURCE_OF_TRUTH.md` (S# = Sources table). "Verified" = stated plainly; "softened" = phrased as ask/try/can't promise. EN wording shown; FR (`content/fr.json`) carries the same claims in French.

## 1. Claims, page by page

### Every page (header, footer, sticky bar, JSON-LD)
| Claim | Tag | Phrasing |
|---|---|---|
| Name "Hôtel Lynx", wordmark HOTEL ◆ LYNX | [VERIFIED: S1,S3,S4] | verified |
| Two-star hotel, ★★ | [VERIFIED: S1,S4,S9] (S6 "3*" conflict → 2★) | verified |
| 9 Rue Al Mahdi Ibn Toumart, Talborjt, 80000 Agadir | [VERIFIED: S1,S3,S4,S6] | verified |
| "Opposite the Mohammed V Mosque" | [VERIFIED: S4,S11,S12; S2] (110 m) | verified |
| Phone +212 5 28 84 78 86, tel:+212528847886 | [VERIFIED: S3,S4,S6] | verified (only phone on site; …87 omitted) |
| Reception 24 h | [VERIFIED: S1] | verified; check-in ends 22:00 → "arriving after 22:00? call reception before you travel" (no promise; one refused night arrival in S2) |
| Email agadir.hlynx@gmail.com | [VERIFIED: S3] | verified (alt address omitted, CONFLICT S3,S7) |
| Booking.com link | [VERIFIED: S1] | secondary CTA |
| Google Maps link on 30.4228588, -9.5917027 | [VERIFIED: S4,S11] | verified (Booking pin never used) |
| Check-in 12:00–22:00, check-out by 12:00 | [VERIFIED: S1] | verified |
| JSON-LD Hotel: address, geo, phone, email, 2★, check-in/out, petsAllowed false, amenities (Wi-Fi, free public parking, AC, 24h desk, room service, rooftop terrace, non-smoking), aggregateRating 8.4/10 × 1009 (home only) | [VERIFIED: S1,S3,S4] | verified; no priceRange |
| No WhatsApp link anywhere ("Phone / WhatsApp" is the guest's own optional field) | [UNVERIFIED] number | omitted per orchestrator |

### Home `/` · `/fr/`
| Claim | Tag | Phrasing |
|---|---|---|
| "Clean rooms, a reception that never closes, free Wi-Fi and free public parking right by the hotel" | [VERIFIED: S1,S4] | verified; orchestrator fix applied (was "by the door") |
| 8.4 on Booking.com · 1,009 reviews · 9.2 for staff | [VERIFIED: S1] | verified, no dates |
| Fingerposts: mosque 1 min, cafés 3 min, beach promenade 23 min (+ bearings) | [VERIFIED: S11,S12] | verified (OSRM foot) |
| Yes board: cleanliness 8.9, Wi-Fi 9.5, free parking (public), 24 h, room service ("ask at the desk", no menu), AC every room, own shower room, satellite/cable TV, rooftop terrace facing the Kasbah hill | [VERIFIED: S1,S4 + photo bk_10] | verified |
| No board: no breakfast (cafés 3 min), no lift ("upper floors by the stairs only"; "ask at the desk for a hand"), no pool/gym, no smoking rooms | [VERIFIED: S1,S2,S4]; luggage help [PROBABLE: S2,S5] | verified / help softened to "ask" |
| Room directory: "Five kinds of room", 5 types, m², guests | [VERIFIED: S1] | verified; Single shown as a "15 m² · 1 single bed" plate (no photo exists) |
| Lynx Line: 16 walking stops with OSRM minutes/metres (cafés and banks "3–4 min", as on Your Agadir) | [VERIFIED: S11,S12] | verified, "walking times follow the streets from our front door" |
| "Talborjt … rebuilt after the 1960 earthquake" | context S11/S13 | plain context |
| "By taxi": promenade ~4, CTM ~5, Kasbah ~12, airport ~30 min; "petits taxis pass all day in town; for the airport, ask reception about booking you a taxi" | [VERIFIED: S12] times; taxi booking [PROBABLE: S2] | "about", "by road, traffic permitting"; booking softened (A5) |
| Getting in: "Late flight? Call ahead." · free public parking, airport ~24 km, "ask us about booking you a taxi" | [VERIFIED: S1,S12]; [PROBABLE: S2] | softened ("ask us"); no late-arrival promise (A3) |
| Reviews: Booking 8.4/1,009 + 7 subscores; Google 4.1/241 | [VERIFIED: S1,S4] | verified |
| Quotes EN: Ingo (title), Joanna, Kätlin, Lars | SOT §f 1,5,3,6 | exact text |
| Quotes FR: Alexandre (title), Chaimae, Linda; Joanna kept in English (`lang="en"`) | S2 raw `_bk_reviews_flat.json`, exact text | exact text, attribution name + country + Booking.com |
| Mini form → /ask/ ("nothing is booked or charged") | design | honest |

### Rooms `/rooms/` · `/fr/chambres/`
| Claim | Tag | Phrasing |
|---|---|---|
| In every room: AC, own shower room (shower, basin, toilet), towels, flat-screen TV satellite+cable, free Wi-Fi 9.5, wake-up call ("ask at reception"), non-smoking, room service ("ask at the desk") | [VERIFIED: S1] | verified |
| "No bathtubs" | photos bk_03/07/26/27 (S1) | verified from photos |
| "Towels and fresh linen — ready when you arrive" | towels [VERIFIED: S1] | plain |
| Single 15 m², 1 single bed, 1 guest; key-tag plate "15 m² · 1 single bed · We don't have a photo of the Single yet" (no borrowed bathroom photo) | [VERIFIED: S1] | honest plate (B7/A21) |
| Superior Single 16 m², single bed or large double "when one is free" | [VERIFIED: S1] ("if available") | verified |
| Twin 20 m², 2 single beds; "on Booking.com listed as a Double Room with two single beds" | [VERIFIED: S1] | verified |
| Double 20 m², large double; "Some of our Doubles open onto a small balcony — we can't promise one" | beds [VERIFIED: S1]; balcony [PROBABLE: S2 + photo bk_02] | softened |
| Triple 20 m², large double + single; "We don't add extra beds" | [VERIFIED: S1] (no extra beds) | verified |
| Photo captions only describe what is visible (balcony, round table, dressing table) | photos S1 | verified |
| What we don't do: breakfast, lift, pool/gym, extra beds, smoking rooms | [VERIFIED: S1,S2,S4] | verified |
| Balcony block: "Many of our rooms have a small balcony; some look towards the Kasbah hill. We can't promise one" + Nabilah quote; button → `/ask/?balcony=1` (box ticked) | [PROBABLE: S2] + photos; quote SOT §f 9 | softened; quote exact (kept in English on FR page) |
| "Ask for today's price" (no prices) | prices [STALE] | no figures |
| JSON-LD HotelRoom ×5 (floorSize, occupancy, bed) | [VERIFIED: S1] | verified, no aggregateRating on this page |

### Your Agadir `/your-agadir/` · `/fr/votre-agadir/`
All minutes/distances = OSRM from the verified pin (`research/notes-neighbourhood.md` §3) [VERIFIED: S11,S12]; bearings computed from OSM coordinates at build time; named places exist in OSM (trading/opening hours not claimed).
| Claim | Tag | Phrasing |
|---|---|---|
| "Walking times … follow the streets from our front door, at an easy pace — not as the crow flies" | S12 method (OSRM foot estimate) | no "measured on foot" claim (A8) |
| Eat: restaurants from 70 m / 1 min; cafés 3–4 min / 230–300 m; "We don't serve breakfast. Talborjt does" | [VERIFIED: S11,S12; S1,S2] | categories only, no café names |
| Breakfast quote EN Colin ("No breakfast cafe although loads of nice cafes nearby"), FR Audrey | S2 raw, exact text | exact |
| Errands: pharmacy 2 min/150 m (second 4 min/310 m); banks 3–4 min/200–310 m (Al Barid, Attijariwafa, Bank of Africa); post office 3 min/200 m (Amana / Poste Talborjt); supermarkets 5–7 min/370–520 m (Marjane Market, Carrefour Market, Aswak Assalam) | [VERIFIED: S11,S12] | verified; "banks", never "ATMs/cash" |
| Sights: mosque 1, Jardin Ibn Zaïdoun 7, Jardin d'Olhão 10, Musée Mémoire 11 ("the city and the 1960 earthquake"), Amazigh Heritage Museum 15, central market 16, Vallée des Oiseaux 20 ("on the way to the beach"), cable car lower station 23 (~4 by taxi), Souk El Had 30 (~4), Marina entrance 35 (~4) | [VERIFIED: S11,S12,S13] | verified; "opening times change, check locally" (no hours) |
| Kasbah hilltop: not a walk, ~12 min by taxi or the cable car | [VERIFIED: S12] | "about" |
| Beach: promenade 23 min / 1.7 km (~4 taxi), sand 25 min / 1.9 km (~5 taxi) | [VERIFIED: S11,S12] (Booking's 19 min = wrong pin, not used) | verified |
| Transport: petits taxis "all day", "flag one down, or ask at reception"; CTM ~5 min / 3.2 km; Supratours ~5 min / 3.7 km "check your ticket for the departure point"; airport ~30 min / 24 km, "petits taxis don't serve the airport — ask reception about booking you a taxi" | [PROBABLE: S2]; [VERIFIED: S12]; Supratours [PROBABLE] | softened / "about" |
| Three maps drawn from OSM (around the door; Talborjt to the sea, wide ≥48rem and phone-framed <48rem with an "Off this map" list for Souk El Had/Kasbah/CTM/Supratours/airport), rings "distance as the crow flies", unnamed dots for eat/errands | S11 (ODbL) | credit "Map data © OpenStreetMap contributors" on page |
| "Open in Google Maps" + per-place "Route ↗" (Google directions from the pin) | pin [VERIFIED: S4] | — |

### Practical `/practical/` · `/fr/infos-pratiques/`
| Claim | Tag | Phrasing |
|---|---|---|
| Times, reception 24 h, parking free | [VERIFIED: S1,S4] | verified |
| By car: public spaces right by the hotel, "public, so we can't reserve one" | [VERIFIED: S1,S4] (type PUBLIC) | verified + honest limit |
| From the airport: ~24 km, ~30 min by taxi, "ask us about booking one when you write" | [VERIFIED: S12]; [PROBABLE: S2] | softened |
| By bus: CTM and Supratours ~5 min by petit taxi | [VERIFIED: S12]; Supratours [PROBABLE] | "about" |
| From the beach: 23 min on foot, ~4 by taxi | [VERIFIED: S12] | verified |
| House rules: check-in/out, "arriving after 22:00? call reception before you set off", "ask at the desk if you need a little longer", non-smoking, no pets, no lift, not wheelchair accessible | [VERIFIED: S1]; late check-out [PROBABLE: S2] | late check-out softened to "ask"; no late-arrival promise |
| FAQ: no breakfast; free public parking; no lift + "ask for a lower floor when you write"; after 22:00 → "call reception before you travel and check with us first"; airport taxi "reception will try to arrange one"; Wi-Fi free 9.5; "Is it quiet?" → mosque across the square, lively streets; no pool/gym; laundry "ask at reception"; price → ask or call / Booking.com | [VERIFIED: S1,S2,S4]; laundry/taxi [PROBABLE: S2,S5] | honest; never "quiet"; no promise of a reply |
| FAQPage JSON-LD mirrors the visible FAQ | — | — |

### Ask `/ask/` · `/fr/demande/` (+ homepage mini form)
| Claim | Tag | Phrasing |
|---|---|---|
| "This form doesn't book or charge anything: it writes a clear email to our reception" | design | honest |
| "Ask what's free and today's price" · "Need an answer today? Call reception — it's staffed 24 hours" (no promised e-mail reply until the owner confirms which inbox is read) | email [VERIFIED: S3]; inbox monitoring = owner Q1 | softened (A6) |
| Side plate: call 24 h, email, Booking.com 8.4 from 1,009 reviews | [VERIFIED: S1,S3,S4] | verified |

### Omitted on purpose (owner questions)
Children policy (CONFLICT S1,S2) · payment terms/cash (S1, unconfirmed) · room count 41 (S10 affiliates only) · staff names (Rachid/Ahmed/Hicham — none on site; FR quote picked without names) · second phone …87 · WhatsApp · room service content · cancellation terms · prices · café/restaurant names and hours · ATMs · "quiet", "modern", "renovated".

### Owner-embarrassment self-test (done)
Removed/softened during QA: "No room upgrades to upsell" (unfounded) → removed; "guests rarely have to look far" for parking → replaced by "public, so we can't reserve one"; errands intro "cash" (ATMs unverified) → "banks"; FR mail line "réserver une chambre" (implied booking) → "Je cherche une chambre". Every remaining number traces to S1/S4/S11/S12.

## 2. Functional checklist (STANDARD §10) — preview http://127.0.0.1:8702, one tab
| Check | Result |
|---|---|
| `check_site.py` | **OK (11 pages)**, 0 WARN; contact targets = `tel:+212528847886`, `mailto:agadir.hlynx@gmail.com` only |
| One h1 per page, unique title/description, canonical on https://hotel-lynx.peashoot.io/…, hreflang en/fr/x-default, sitemap with xhtml:link alternates | ✅ (all 10 pages + 404 checked) |
| Horizontal overflow at 360/390/430/768/1024/1280/1440, all 11 pages | ✅ none (the city map scrolls inside its own frame on phones, by design) |
| Mobile menu: aria-expanded true/false, focus to first link, Esc closes + focus back to button, closes on link tap, hidden ≥64rem | ✅ EN + FR |
| Language switch keeps the current page (header 2-letter link ≥64rem, menu + footer full name) | ✅ e.g. /rooms/ ↔ /fr/chambres/ |
| Form validation: empty submit → 4 inline errors (aria-invalid/aria-describedby), focus on first invalid; past date / departure ≤ arrival / guests 1–12 / email pattern | ✅ |
| Prefill: `/ask/?room=double&arrival=…&departure=…&guests=…` (room links, homepage mini GET form) | ✅ |
| Composed email EN: subject "Room request: 10 Nov – 11 Nov, 3 guest(s), Triple"; body decoded with accents (Élodie), `&`, em dash, line breaks intact; no undefined/NaN/empty labels | ✅ |
| Composed email FR: "Demande de chambre : 24 déc. – 25 déc., 2 personne(s), Double", French spacing before colons, fr-FR dates | ✅ |
| Success panel: "Open my email app again" (same mailto), To + Subject + full message shown on screen (works with no mail app), copy address, copy message (clipboard API → execCommand fallback → "select by hand" message), phone 24 h, "Change my details" back to the form | ✅ clipboard verified ("Room request: … Hello Hôtel Lynx, …") |
| Sticky bar: appears after the page head, hidden while the form, a CTA band or the footer is on screen; never covers submit | ✅ |
| Console errors / failed requests | ✅ 0 / 0 on 8 templates (only the expected headless mailto navigation) |
| Inputs ≥17 px (no iOS zoom), tap targets ≥44 px, reduced motion respected | ✅ |
| Images: all via `tools/images.py` (WebP, srcset/sizes, width/height, dominant colour), largest file 105 KB, hero mobile 34 KB | ✅ |
| `_headers`: immutable cache for css/js/fonts, 1 week for images, nosniff, referrer policy, X-Frame-Options SAMEORIGIN, Permissions-Policy (camera/mic/geo/payment off) — no CSP that could block tel:/mailto:/map links | ✅ |
| 404: self-contained, EN + FR line, links home (EN + FR) and phone | ✅ live: /no-such-page/ → 404 with the custom page |
| Cloudflare e-mail obfuscation (zone feature) would rewrite mailto: links → each address wrapped in `<!--email_off-->` | ✅ live: 0 `email-protection` rewrites, 4 intact mailto links on /ask/ |
| Live site (after deploy 5b9ccfc): home, /your-agadir/, /fr/, 404 at 390 — 200, canonical correct, no broken assets, no failed requests | ✅ screenshots `live-*` |

## 3. Performance (390×844, cache disabled, local server = **uncompressed**; Cloudflare adds brotli/gzip to HTML/CSS/JS)
| Template | KB before scroll | Requests | LCP element | LCP (local) | CLS |
|---|---|---|---|---|---|
| Home `/` | 183 (html 36) | 6 | hero `facade-m-800.webp` (34 KB, fetchpriority high) | 0.40 s | 0 |
| Rooms | 150 (html 29) | 6 | h1 text | 0.39 s | 0 |
| Your Agadir | 209 (html 33) | 8 | `view-800.webp` (18 KB, eager) | 0.34 s | 0 |
| Practical | 155 (html 18) | 6 | lead paragraph (the blue-hour photo below it, 23 KB, is now eager — it was LCP at 0.96 s while lazy) | 0.28 s | 0 |
| Ask | 129 (html 15) | 5 | intro paragraph | 0.23 s | 0 |
| FR home | 185 | 6 | hero webp | 0.38 s | 0 |
| FR Your Agadir | 210 | 8 | `view-800.webp` | 0.28 s | 0 |
| 404 | 122 | 5 | FR paragraph | 0.19 s | 0 |
**Live (Cloudflare, brotli) home at 390: 118 KB / 8 requests before scroll** (html 8, css 11, js 4, fonts 61, hero 34; 2 zone analytics beacons). CSS 43 KB raw (≤60), JS 10 KB raw (≤30), fonts 61 KB (2 latin woff2, preloaded Overpass). Map base SVGs 27 + 17 KB, lazy.

## 4. Screenshots — `/home/agent/agadir-pilot/qa/hotel-lynx/p3/`
Round 1 (390 + 1440 full pages): `r1-home-*`, `r1-rooms-*`, `r1-agadir-*`, `r1-practical-390`, `r1-ask-390-full/-errors/-filled/-done`, `r1-fr-home-*`, `r1-fr-ask-390-done`.
Fixed after round 1: map ring labels clashing with the pin, sand colour, swipe hint hidden on desktop, wide map centred on the hotel on phones, Double gallery layout, stairs crop, 3-field mini form overflow, success panel e-mail wrapping, header overflow once FR existed (lang code, phone number from 88rem), FR sticky labels, FR balcony heading overflow at 1024, 404 buttons, practical head call plate, practical LCP eager.
Round 2: `r2-home-390/1440`, `r2-rooms-1440`, `r2-agadir-1440`, `r2-practical-1440`, `r2-ask-1440`, `r2-fr-ask-1440`, `r2-fr-rooms-390`, `r2-fr-agadir-390`, `r2-fr-practical-390`, `r2-404-390/1440`, `r2-menu-en-390`, `r2-menu-fr-390`.
Round 3 (folds after last fixes): `r3-home-390-fold`, `r3-fr-home-390-fold`, `r3-practical-390-fold`, `r3-practical-1440-fold`.
Live: `live-home-390`, `live-agadir-390`, `live-fr-home-390`, `live-404-390`, `live-fr-ask-done-390`.

## 5. Known weaknesses
- No Single-room photo (honest caption + plate instead) — owner photo needed.
- Head photo on Your Agadir (bk_09) is soft by design (blurred balcony rail in front).
- ~~On phones the city map is wider than the screen and scrolls sideways~~ → fixed in phase 4 (B1): phone-framed map, no sideways scroll.


## Audit A — facts & copy

_Auditor: AuditFactsLynx · 2026-10-02 · scope: all 11 HTML files in `site/` (EN + FR + 404), `content/{en,fr,site}.json`, `tools/build.py`/`templates.py` output; checked against SOURCE_OF_TRUTH.md, research/notes-*.md and the raw review dump `research/raw/_bk_reviews_flat.json`. Spot-checked live (curl): A1, A2, A3, A4 strings are on https://hotel-lynx.peashoot.io/ now. Viewport: copy findings apply to all viewports._
_Format: ID · severity · page · what is wrong (evidence) · why it matters · concrete fix. Content keys refer to `content/<lang>.json`._

**Checked and correct (no action):** breakfast is "we don't serve it" everywhere (EN/FR, yes/no board, rooms, FAQ, Your Agadir) · parking is always "free public parking right by the hotel / they're public, we can't reserve one" — never private/guarded · 24 h reception vs check-in 12:00–22:00 / check-out 12:00 consistent on every page, footer and JSON-LD · "no lift" + "not wheelchair accessible" correct · room facts (15/16/20/20/20 m², beds, 1/1/2/2/3 guests, no extra beds, non-smoking) match S1 on every page and in HotelRoom JSON-LD · all 17 walking and 7 taxi times/distances match `notes-neighbourhood.md` §3 (only rounding inconsistencies, A12) · Booking 8.4 / 1,009 and all seven subscores (9.5/9.2/8.9/8.9/8.8/8.6/8.2) + Google 4.1/241 identical across EN/FR/JSON-LD · all 12 quotes found verbatim in the raw Booking dump (Ingo, Joanna, Kätlin, Lars, Nabilah, Colin, Audrey, Alexandre, Chaimae, Linda) with correct first name + country + platform · no staff names anywhere · no children or payment claims · no banned words (EN/FR) · one h1 per page, titles unique, canonical + hreflang pairs correct on all 10 content pages · inquiry form has every field the brief asks for.

### P1 — must fix before Fadwa shows it

**A1 · P1 · `/` (#rooms h2), `/rooms/` (h1), `/fr/` (h2), `/fr/chambres/` (h1)** — "Five rooms. No surprises." / "Five rooms. One standard." / "Cinq chambres. Aucune surprise." / "Cinq chambres. Un seul niveau." (keys `rooms.h2`, `rooms_page.head.h1`). Read cold, this says the hotel has **five rooms**; it has five room *types* (the meta description even says "Five room types"; affiliates list ~41 rooms). The FR h1 is worse: "Un seul niveau" means "a single floor/level" — on the page that then says there is no lift and everything is up the stairs. · **Why:** the owner's first reaction will be "we have far more than five rooms"; FR reads as nonsense. · **Fix:** EN `rooms.h2` "Five room types.<br>Shown as they are." · `rooms_page.head.h1` "Five room types.<br>One standard." · FR `rooms.h2` "Cinq types de chambre.<br>Montrées telles quelles." · `rooms_page.head.h1` "Cinq types de chambre.<br>Une même exigence."

**A2 · P1 · `/` (#rooms intro), `/rooms/` ("What every room has" → "Up the stairs"), `/fr/` and `/fr/chambres/` (same)** — "All non-smoking, all up the stairs." / "Toutes non-fumeurs, toutes par l'escalier." (`rooms.intro`) and a "What every room has" item "Up the stairs — There's no lift" / "Par l'escalier" (`rooms_page.every.items[7]`). Evidence against: Colin, United Kingdom, Booking (Aug 2026, 10/10): "Staff were able to cancel booking of 3 bedded upstairs room … and get ground room" (`_bk_reviews_flat.json`; also notes-reviews.md "Colin UK swapped to a ground-floor room"). Booking only states "Upper floors accessible by stairs only"; SOT owner question 4 (ground-floor rooms?) is still open. · **Why:** an untrue universal claim that turns away exactly the guests who can't manage stairs — the people a ground-floor room would serve. · **Fix:** `rooms.intro` → "…and free Wi-Fi. All non-smoking. No lift: the upper floors are by the stairs." FR "…et le Wi-Fi gratuit. Toutes non-fumeurs. Pas d'ascenseur : on monte aux étages par l'escalier." Replace every-item 7 with t "No lift" / d "Upper floors by the stairs. Stairs hard for you? Say so when you write." (FR "Pas d'ascenseur" / "On monte aux étages par l'escalier. Les marches vous posent problème ? Dites-le en écrivant.").

**A3 · P1 · `/` (#arrive), `/practical/`, `/fr/`, `/fr/infos-pratiques/`** — late arrival is promised although check-in ends at 22:00: h2 "Late flight? Hire car? Fine." / "Vol tardif ? Voiture de location ? Aucun souci." (`arrive.h2`); house rule "Arriving later? Tell us your time and we'll expect you." / "…et nous vous attendrons." (`basics_page.rules.items[0].d`); FAQ "Can I arrive after 22:00?" answered with an implied yes ("Reception is staffed 24 hours. Tell us your arrival time…", `basics_page.faq.items[3].a`). SOT: check-in 12:00–22:00 [VERIFIED: S1]; an Aug-2026 review reports a refused night arrival; owner question 9 ("late arrivals after 22:00: what should guests do?") unanswered. · **Why:** a policy the hotel has not given; a guest turned away at 01:00 will quote this page. · **Fix:** h2 "Late flight? Hire car? Call ahead." / "Vol tardif ? Voiture de location ? Appelez-nous avant." · rule "Arriving after 22:00? Call reception before you set off to arrange it." / "Arrivée après 22 h ? Appelez la réception avant de partir pour l'organiser." · FAQ answer "Check-in is until 22:00. If you'll be later, call reception (24 h) before you travel so we can arrange it." Same pattern in `arrive.p1` ("Landing later? Call reception before you fly." instead of "Tell us your arrival time when you write").

**A4 · P1 · `/fr/` (Le deal, intro)** — "Nous sommes un **hôtel de ville** deux étoiles, et ça nous va très bien. Voici tout le contrat avant de réserver — pas de **petites lignes** ensuite." (`basics.intro`, FR). "Hôtel de ville" = town hall/city hall in French; "petites lignes" is a literal calque of "small print" (French: "petits caractères"). · **Why:** the first FR paragraph after the hero reads "We are a two-star town hall" — instantly marks the FR as machine-translated in front of a French-speaking owner. · **Fix:** "Un hôtel deux étoiles en plein centre, et fier de l'être. Voici l'essentiel avant de réserver — pour éviter les mauvaises surprises." (also resolves A7 in FR).

### P2 — should fix

**A5 · P2 · `/` (By taxi note), `/your-agadir/` (Airport), `/practical/` (From the airport + FAQ), FR mirrors** — airport taxi booking stated as a firm service: "for the airport, we can book you a taxi" (`agadir.ride_note`), "Petits taxis don't serve the airport — we can book you a taxi." (`agadir_page.places.airport.note`), "tell us your flight and we can book you a taxi" (`basics_page.ways.items[1].d`), FAQ "Can you book an airport taxi? **Yes** — ask us when you write." (`basics_page.faq.items[4].a`). SOT: [PROBABLE: S2] (4 reviews) → "soften"; owner Q8 open. The home "Getting in" block already has the right register ("ask us about booking you a taxi"). · **Why:** unconfirmed service promised in four places. · **Fix:** "for the airport, ask reception to book you a taxi." · FAQ "Ask us when you write and reception will try to arrange one. The ride is about 30 minutes; petits taxis don't go to the airport." FR: "pour l'aéroport, demandez à la réception de vous réserver un taxi." / "Demandez-le en écrivant : la réception essaiera de vous en trouver un."

**A6 · P2 · `/ask/`, `/fr/demande/`, `/rooms/` (price band), `/practical/` FAQ "How much"** — reply promises built on an unconfirmed inbox: "it goes straight to our reception" / "le message part directement à notre réception" (`ask.done.p`), "Reception replies with what's free and today's price." (`ask.steps[3]`), "we'll reply with what's free and today's price" (ask intro + meta description, rooms price band, FAQ). SOT contact block: which address is read (agadir.hlynx@ vs agadirhotellynx@) is owner question 1; Booking sample shows 0 partner replies to reviews. · **Why:** if that Gmail is not checked at the desk, every lead from the primary CTA silently dies and the site has promised an answer. · **Fix:** (1) put "Which email do you read every day?" at the top of Fadwa's owner questions before this goes live; (2) until confirmed, soften: `ask.done.p` "If your email app opened, just press send. In a hurry? Call reception, 24 hours." · `ask.steps[3]` "We answer with what's free and today's price — for a same-day answer, call." FR likewise.

**A7 · P2 · `/` (The deal intro)** — "Here's the whole deal before you book — no small print later." (`basics.intro`). The board deliberately omits two house rules Booking states (cash-only payment, "children not allowed" — both held back pending owner, SOT Q2/Q3) and the top complaint (noise). · **Why:** claiming completeness while omitting the payment rule is the kind of line a guest arriving with only a card throws back. · **Fix:** "We're a two-star city hotel and happy with it. Here's the short version before you book." (FR: see A4.)

**A8 · P2 · `/your-agadir/` (lead), `/` (Your Agadir intro), meta description of `/your-agadir/`, FR mirrors** — "Every walking time on this page was **measured on foot** from our front door" / "Every time below is measured on foot" / "chaque temps a été mesuré à pied" (`agadir_page.head.lead`, `agadir.intro`, `pages.agadir.description`). The times are OSRM routing estimates at ~4.5 km/h (notes-neighbourhood §2), nobody walked them. · **Why:** an untrue method claim, and method talk at all is research voice (STANDARD §3). · **Fix:** "Walking times follow the streets from our front door, at an easy pace — not as the crow flies." FR "Les temps de marche suivent les rues depuis notre porte, à pas tranquille — pas à vol d'oiseau." Meta: "…every time counted from the door of Hôtel Lynx." / "…temps comptés depuis la porte de l'Hôtel Lynx."

**A9 · P2 · `/fr/`, `/fr/votre-agadir/`** — English decimal points in French distances: "1.1 km", "1.2 km", "1.5 km", "1.7 km", "1.9 km", "2.2 km", "2.6 km", "3.2 km", "3.7 km", "6.4 km" (Lynx Line, taxi grid, all lists), while the same pages correctly write "8,4", "9,5", "1 009". Source: language-independent `dist` strings in `content/site.json` (`walk`, `ride`, `near`). · **Why:** visible on the most-praised FR page; inconsistent within one screen. · **Fix:** localise `dist` at render time in `tools/build.py`/`templates.py` for `fr` (`re.sub(r'(\d)\.(\d)', r'\1,\2', dist)`), giving "1,1 km" (ideally with U+202F before "km").

### P3 — polish

**A10 · P3 · `/rooms/`, `/fr/chambres/` ("What every room has")** — "Walk-in shower, basin, toilet. No bathtubs." / "Douche à l'italienne…" and "A wall unit in every room." / "Un climatiseur mural dans chaque chambre." Booking lists only shower + toilet + towels and AC; "walk-in" and "wall unit" come from 4 bathroom photos Booking attaches to 3 of the 5 types (notes-rooms). The open shower is also a recurring complaint (water on the floor). · **Fix:** "Shower, basin, toilet and towels. No bathtubs." / "Douche, lavabo, toilettes et serviettes. Pas de baignoire." · AC: "In every room." / "Dans chaque chambre."

**A11 · P3 · `/rooms/`, `/fr/chambres/`** — "Wake-up call — Ask at reception the night before." / "Demandez à la réception la veille au soir." (`rooms_page.every.items[5].d`): an invented procedure; S1 only lists wake-up service. · **Fix:** "Ask at reception." / "Demandez à la réception."

**A12 · P3 · `/` vs `/your-agadir/` vs `/rooms/` (EN + FR)** — the same places get different minutes: home Lynx Line "Banks & post office 3 min, 200–310 m" and "Cafés & crèmeries 3 min" vs Your Agadir "Banks 3–4 min" and "Cafés 3–4 min"; home No-board "the first cafés are three minutes from the door" vs rooms/FAQ "3–4 minutes". OSRM: Bank of Africa 308 m / 4 min, Café Holanda 296 m / 4 min. · **Fix:** the ranges are right; on the home line label them "from 3 min" (`site.json walk` cafes/banks) and keep "three minutes" only where it says "the first cafés".

**A13 · P3 · `/your-agadir/`, `/fr/votre-agadir/` (Getting around)** — petits taxis labelled "Any time" / "À toute heure" (`agadir_page.labels.anytime`) while the copy above says "pass all day in town"; 24 h availability is not evidenced. · **Fix:** "All day" / "Toute la journée".

**A14 · P3 · `/` (Your Agadir h2), `/fr/`** — "Everything is a walk away." / "Tout se fait à pied." directly above a "By taxi" block (Kasbah, CTM, airport). · **Fix:** "Most of it is a walk away." / "Presque tout se fait à pied."

**A15 · P3 · copy tone (EN + FR)** — the copy is mostly sharp and in voice; the few template-sounding lines: "No surprises." / "Aucune surprise." (generic, and risky next to noise/dated-decor reviews — handled in A1's rewrite); "Feet in the sand" / "Les pieds dans le sable" (Lynx Line beach note, `agadir.places.beach.note`) — beach-brochure cliché off-brand for "Signposted". · **Fix:** "Nearest sand" / "Le sable le plus proche" (already used on Your Agadir — reuse it).

**A16 · P3 · `/` (yes/no board) — brief compliance** — the brief's baseline lists room service; SOT has it [VERIFIED: S1] ("list as 'room service' without menu claims") and JSON-LD declares it, but no visible page mentions it (only inside Lars's quote). Everything else the brief asks for (hero, base, rooms, amenities, why guests return, neighbourhood, distances, reviews, parking/Wi-Fi/reception, inquiry with all listed fields, Booking secondary) is present. · **Fix:** add a YES item "Room service — Ask at the desk." / "Service en chambre — Demandez à la réception." (no menu, no hours).

**A17 · P3 · FR wording (`/fr/`, `/fr/chambres/`, `/fr/infos-pratiques/`)** — literal or stiff French: "Ce que chaque chambre a." → "Dans chaque chambre." · "Le deal" (kicker) → "Franchement" or "En clair" · "Quelqu'un au comptoir, jour et nuit." / "Le comptoir est tenu jour et nuit." / "la réception est tenue 24h/24" → "Quelqu'un à l'accueil, jour et nuit." / "La réception est ouverte jour et nuit." · "Les étages se font uniquement par l'escalier" → "On monte aux étages uniquement par l'escalier" · "Chaque temps à pied de cette page a été mesuré" (see A8). vous is used consistently (OK).

**A18 · P3 · FR typography (`/fr/`, `/fr/chambres/`, `/fr/votre-agadir/`, all FR pages)** — FR quotes use English curly quotes “…” (4 on `/fr/`, 1 on `/fr/votre-agadir/`), while `/fr/chambres/` uses « Chambre Double » with plain spaces; before ":" ";" and inside « » the spaces are ordinary U+0020 (wrap risk: "Depuis notre toit : le…", "Indiquez vos dates : nous…"), whereas "?" correctly uses U+00A0; aria-label "Appeler la réception (24h/24): +212…" has no space before the colon. · **Fix:** in the FR render, use « » with U+202F inside for quotes (EN-language quotes may keep lang="en" but still take « »), U+202F before : ; and inside « », and "(24h/24) : " in the aria-label.

**A19 · P3 · JSON-LD (`/`, `/rooms/`, `/practical/`, FR mirrors)** — (a) FR pages' Hotel/HotelRoom `amenityFeature` names are English ("Free Wi-Fi", "Private bathroom with shower", "24-hour front desk"); (b) FAQPage answers end with a dangling link text: "…Talborjt is full of them — see where." / "— voir où." (link stripped); (c) `aggregateRating` 8.4/1,009 is Booking's figure: verified (allowed by STANDARD §9), but Google ignores third-party ratings in self-serving LocalBusiness markup — keep only if the orchestrator accepts that. · **Fix:** localise FR amenity names; end the breakfast answer at "…Talborjt is full of them." in JSON-LD; decide on (c).

**A20 · P3 · `/404.html`** — reuses the homepage meta description ("Clean rooms, a 24-hour reception…"), declares `canonical` and `hreflang="en"` to `/404.html`, and has no `noindex`. · **Fix:** own description ("Wrong door — this page doesn't exist. Back to Hôtel Lynx, Talborjt."), drop canonical/hreflang, add `<meta name="robots" content="noindex">`.

**A21 · P3 · `/rooms/#room-single`, `/fr/chambres/`** — caption "This is the shower room layout the Single shares with the Superior Single and Twin — not the bedroom." states a layout fact that only comes from Booking's photo assignment (notes-rooms). · **Fix:** "A Lynx shower room, like the Single's — not the bedroom." / "Une salle d'eau du Lynx, comme celle de la Single — pas la chambre."

## Audit B — visual, mobile, conversion, links, performance, live

_Auditor: AuditVisualLynx · 2026-10-02 · live https://hotel-lynx.peashoot.io/ (deploy 5b9ccfc), one tab, 360×740 / 390×844 / 430×932 / 1440×900, all 10 sitemap pages + 404, EN + FR. Screenshots: `/home/agent/agadir-pilot/qa/hotel-lynx/p4/` (below: `p4/<file>`). Format: ID · severity · page (+ viewport) · what is wrong (evidence) · why it matters · fix. No P0 found._

**Checked and passing (no action):** `documentElement.scrollWidth` = viewport on all 11 pages at 360/390/430/1440 (only the city map scrolls inside its own frame) · 10/10 sitemap URLs 200, 75 internal href/src 200, `/no-such-page/` and `/fr/nope/` → 404 status with the custom bilingual page · external: Google Maps search + 16 "Route" directions links 200, Booking.com 202 (bot challenge; fine in browsers), every `target=_blank` has `noopener` · language switch lands on the counterpart on every page type (`/rooms/`↔`/fr/chambres/`, `/your-agadir/`↔`/fr/votre-agadir/`, `/practical/`↔`/fr/infos-pratiques/`, `/ask/`↔`/fr/demande/`), hreflang en/fr/x-default + canonical correct · 0 console errors, 0 failed requests on 8 templates (404 logs only its own 404) · 18 `tel:+212528847886` links, only contact targets are that tel + `mailto:agadir.hlynx@gmail.com` · WhatsApp/Facebook/Telegram/Twitter crawlers get 200 + og:image 1200×630 (94 KB) · menu: `aria-expanded` true/false, focus to first link, Esc closes and returns focus to the button, closes on link tap (`/#reviews`), body scroll locked · sticky bar sampled every 300 px on 6 templates: never over a submit button or the footer, hidden on `/ask/` · chips on Your Agadir: headings land 140 px below the sticky chip bar · inputs 17 px, 52 px tall, correct types (`date`, `number`+`inputmode=numeric`, `email`, `tel`, `autocomplete` name/email/tel); checkbox labels 44 px · validation EN/FR: empty → 5 inline errors with `aria-invalid`/`aria-describedby`, focus on first; past date / departure ≤ arrival / 0 or 13 guests / `abc@`, `a@b` all caught; arrival change pushes departure to arrival+1 · prefill: homepage mini form → `/ask/?arrival=…&departure=…&guests=3` filled; `/ask/?room=triple` preselects · copy buttons write to the clipboard (message → "Copied. Paste it into a new email to agadir.hlynx@gmail.com.", address → `agadir.hlynx@gmail.com`) · reduced motion respected, content visible without JS (`.js .rv` gating).

**Composed e-mail, decoded from the live success-panel href (correct; accents, `&`, `%`, `#`, em dash and line breaks all intact):**
```
EN  To: agadir.hlynx@gmail.com · Subject: Room request: 12 Nov – 15 Nov, 2 guest(s), Double
Hello Hôtel Lynx, / I’d like to ask about a room: / Arrival: Thu, 12 Nov 2026 / Departure: Sun, 15 Nov 2026 (3 night(s)) /
Guests: 2 / Room: Double / Balcony if possible: yes / Parking needed: yes / Arriving around: After 22:00 /
Name: Élodie Brás-Nuñez / Email: elodie.bras@example.fr / Phone / WhatsApp: +33 6 12 34 56 78 /
Message: We land at 23:40 — is a late check-in OK? ↵ Also: room on a low floor & quiet side if possible (50% chance we bring a bike #2). /
Could you tell me what’s available and today’s price? Thank you. / Best regards, Élodie Brás-Nuñez        (href 985 chars)
FR  Objet : Demande de chambre : 24 déc. – 27 déc., 3 personne(s), Triple
Bonjour Hôtel Lynx, / Je cherche une chambre : / Arrivée : jeu. 24 déc. 2026 / Départ : dim. 27 déc. 2026 (3 nuit(s)) / Personnes : 3 /
Chambre : Triple / Balcon si possible : non / Parking nécessaire : oui / Arrivée prévue vers : 18 h – 22 h /
Nom : Hélène Lefèvre-Aït Ouaziz / E-mail : helene.lefevre@exemple.fr / Téléphone / WhatsApp : 06 12 34 56 78 /
Message : Nous arrivons en voiture vers 19 h ; est-ce qu'il y a de la place… ↵ Merci & à bientôt « Lynx » ! /
Pourriez-vous m’indiquer vos disponibilités et le tarif du jour ? Merci. / Bien cordialement, Hélène Lefèvre-Aït Ouaziz   (href 1,142 chars)
```

**Performance, live at 390 (Cloudflare brotli, cache disabled; host DPR 1.25, VM unthrottled — times are relative):**
| Template | before scroll | after full scroll | LCP element | LCP | CLS |
|---|---|---|---|---|---|
| `/` · `/fr/` | 130 KB / 9 req | 289 KB / 16 | hero `facade-m-800.webp` (34 KB, `fetchpriority=high`, not lazy) | 388 ms | 0 |
| `/rooms/` | 101 KB / 8 | 213 KB / 15 | h1 text | 312 ms | 0 |
| `/your-agadir/` · FR | 129 KB / 10 | 129 KB / 10 (map SVGs 11 + 6 KB load up front) | `view-800.webp` (18 KB) | 268 ms | 0 |
| `/practical/` | 116 KB / 8 | 116 KB / 8 | lead paragraph | 328 ms | 0 |
| `/ask/` | 92 KB / 8 | 92 KB / 8 | intro paragraph | 404 ms | 0 |
| 404 | 90 KB / 7 | — | — | — | — |
Fonts: 2 files (Overpass latin 39 KB, Overpass Mono latin 22 KB), no latin-ext fetched. CSS 11.5 KB, JS 4.2 KB transferred; Cloudflare beacon 10 KB is the only third party. Headers as served (`curl -I`): HTML `max-age=0, must-revalidate`; `/assets/css|js|fonts/*` `max-age=31536000, immutable`; `/assets/img/*` `max-age=604800`; favicon/robots Cloudflare default 4 h; nosniff / referrer / X-Frame-Options / Permissions-Policy on HTML. All within STANDARD §7.

### P1 — must fix

**B1 · P1 · `/your-agadir/`, `/fr/votre-agadir/` — "Talborjt to the sea · 3 km" map, 360–430** — The known weakness, judged: on phones the map opens with **no sea in it**. The 640 px map sits in a 345 px frame and JS centres it on the Lynx pin (`scrollLeft` 218, `site.js` line 53), so what you see is a street grid, Lynx and pins 2/3/4/5/6/7. The sea, the beach pins 11–12, the marina (10) and the cable car (8) — the whole point of a map called "Talborjt to the sea" — are off-frame to the left; the taxi tags on the right are cut mid-word ("Supratours about 5 mi", "CTM buses about 5 mi", "Airport about 30 mi"), and the Kasbah tag on the left shows only "…y taxi". The only hint is the small grey legend text "Swipe the map sideways." *under* the map. Evidence: `p4/agadir-390-map-city-initial.png` (first view), `p4/agadir-390-map-city-left.png` (sea after swiping), `p4/agadir-390-map-city-right.png`. · **Why:** this is the page the brief calls "the coolest part of the site", and Fadwa shows it from her phone; the first view looks like a blank street plan, and the owner won't swipe. Sideways scrolling inside a frame is fine as an *extra*; it can't be the only way to see the sea. · **Fix (pick one):** (a) a proper mobile version (recommended): have `tools/mapdata.py` output a portrait base `map-city-m.svg` cropped around Lynx and pins 2–12, about 345×420, used below 48rem through `<picture>`/CSS, with no horizontal scroll. Move the four taxi edge tags out of the map into a one-line row under it on phones; they repeat "Getting around" anyway. (b) A smaller fix: start the scroll at the midpoint between the Lynx pin and pin 11 instead of the Lynx pin (scrollLeft ≈ 150 at 390: Lynx at x≈390 and beach pins at x≈188–213 then both show). Add an in-frame affordance (fade on the scrollable edge plus a small "← swipe →" plate inside the frame) and move the taxi tags below the map so they are never cut.

### P2 — should fix

**B2 · P2 · `/`, `/fr/` room directory (#rooms), every viewport** — The four room thumbnails don't fill their 4:3 boxes: a black band runs under every photo, 16 px at 360–430 (box 116×87, img 116×71) and 32 px at 1440 (box 238×178, img 238×146). Evidence: `p4/home-390-rooms-list-zoom.png`, `p4/home-1440-full.png`. Cause: `.dir-img img{height:100%}` resolves against `<picture>`, which has `display:block` and auto height. · **Why:** it looks like broken image loading in the second section a viewer sees. · **Fix:** `.dir-img picture{height:100%}`. No other image box on the site has this problem; all were scanned.

**B3 · P2 · `/your-agadir/` + FR, both map legends, 390 and 1440** — Legend swatches split from their labels. Each swatch and each text is a separate flex item in `.map-leg`, so lines wrap between them: at 390 the "■" sits at the end of the "Restaurants & cafés" line and the "◌" at the end of the "Pharmacies…" line, so each symbol appears to belong to the wrong label. At 1440 the "◌" ends one line and "Distance as the crow flies" starts the next. Evidence: `p4/agadir-390-map-door.png`, `p4/agadir-1440-groups.png`. · **Why:** a map key that pairs symbols with the wrong labels misleads, and it looks sloppy on the signature page. · **Fix (templates.py):** wrap each pair in `<span class="leg-i"><span class="lg …"></span>Label</span>` and add `.leg-i{display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap}`.

**B4 · P2 · `/rooms/` "Balcony? Ask for one." + `/fr/chambres/`** — The "Ask for a room with a balcony" / "Demander une chambre avec balcon" button links to `/ask/?room=double` / `/fr/demande/?room=double`. The balcony checkbox is not ticked, and `/ask/?balcony=1` is ignored. Meanwhile the copy says "tick the box when you write" and "Many of our rooms have a small balcony", so not only Doubles. · **Why:** the button promises a balcony request, then hands the guest a form that silently asks for a Double with no balcony. · **Fix:** read `balcony=1` in the `site.js` prefill and tick `input[name=balcony]`. Point both buttons to `/ask/?balcony=1` (no room preselected).

**B5 · P2 · all pages, phones (360–430)** — The language switch is hard to use on a phone. The mobile header has no FR/EN link, so the only switches are a 16 px-tall "FRANÇAIS"/"ENGLISH" text link at the very bottom of the full-screen menu and the same small link in the footer (70×16 px). Evidence: `p4/menu-rooms-390.png`. · **Why:** Fadwa will switch to French in front of a French-speaking owner. A 16 px target at the bottom of a black screen is the hardest tap on the site. · **Fix:** in the menu, make the language a full 44 px row, or an "EN | FR" plate next to the "Call reception" button. Optionally, from 390 px show the 2-letter code (already used at ≥64rem) in the mobile header between "24H" and the burger, after checking it fits.

**B6 · P2 · `/your-agadir/` + FR, 1440** — The need-groups grid leaves holes. "Sights & walks" (1,594 px tall) spans two rows, and the grid shares its height across both auto rows. So "Eat & breakfast" and "Everyday errands" sit in 779 px cells: Eat's content ends at y≈2348, yet "The beach"/"Getting around" start at y 2649. That leaves about 300 px of blank paper under Eat and a similar gap under Errands, while Sights runs on alone in the third column. Evidence: `p4/agadir-1440-full.png`. · **Why:** on the "coolest part" page, the desktop view reads as unfinished. · **Fix:** `.grps-grid{grid-template-rows:min-content 1fr}` above 64rem. Row 1 then hugs Eat/Errands, Beach/Transport follow directly, and the spare height falls at the bottom of column 1–2. Alternatively, give Sights its own full-width row with a 2-column list.

**B7 · P2 · `/rooms/` + FR, all viewports (most visible at 1440)** — The first room imagery on the Rooms page is two bathroom photos in a row: the "What every room has" shower photo (`shower-wc`), then the Single entry with a large shower-room photo (`shower`, ≈960 px wide at 1440, the largest image on screen) under the "We don't have a photo of the Single yet" plate. Evidence: `p4/rooms-1440-full.png`, `p4/rooms-390-full.png`. · **Why:** an art director would ask why a hotel's rooms page opens on two toilets. The honest no-photo note is right, but the photo still dominates. · **Fix:** for the Single, use the black key-tag plate already used on the homepage ("15 m² · 1 single bed"), sized like the other room images. Show the shower photo once at most, small. Caption wording is covered in A21.

**B8 · P2 · `/`, `/fr/` hero, phones** — The mobile `<source>` offers only `facade-m-800.webp 800w`. On a 390 px phone at 3× DPR the browser needs about 1,170 px, so the hero (and the HOTEL LYNX sign in it) is upscaled 1.46×. · **Why:** it is the first pixel the owner sees on Fadwa's phone, and the sign lettering goes soft. · **Fix:** add `facade-m-1200.webp 1200w` (expect about 60–70 KB, still well under the 200 KB LCP budget) to the mobile `srcset` in `tools/images.py` and the template.

_(FR decimal points "2.6 km", "1.7 km"… on `/fr/` and `/fr/votre-agadir/` were also seen live; already filed as A9.)_

### P3 — polish

**B9 · P3 · all pages, 390** — Several tap targets are under 44 px (measured): footer phone 244×27, footer e-mail / Google Maps / Booking.com 22 px tall, header wordmark (home link) 139×28, breadcrumb "Hôtel Lynx" 20 px, Your Agadir "Route ↗" links 67×34 (×16 per page), success panel "Copy" (address) 36 px. · **Why:** STANDARD §6 asks for ≥44 px; the footer phone is a primary action on phones. · **Fix:** `min-height:44px; display:inline-flex; align-items:center` on footer contact links, Route links and `.copy` buttons (or padding-block to reach 44).

**B10 · P3 · `/`, `/rooms/` room metadata + key-tag plates, EN/FR, all viewports** — "m²" in Overpass Mono renders as "15 m ²": the superscript gets its own monospace cell and looks detached, like a stray mark. Evidence: `p4/home-390-rooms-list-zoom.png`. · **Fix:** set the unit in Overpass, e.g. `<span class="u">m²</span>` with `.u{font-family:var(--sans)}`, or pull the ² back with `margin-left:-.35em`.

**B11 · P3 · `/`, `/fr/` hero kicker, 360 and 390** — "— TWO-STAR HOTEL · TALBORJT, / AGADIR" wraps with "AGADIR" alone on line 2, the rule aligned to line 1 only. FR does the same ("HÔTEL DEUX ÉTOILES · TALBORJT, / AGADIR"). Evidence: `p4/home-360-fold.png`, `p4/fr-home-390-fold.png`. · **Fix:** a non-breaking space in "Talborjt, Agadir" plus `text-wrap:balance`, or drop "Agadir" from the kicker below 26rem (the h1 already says it).

**B12 · P3 · `/`, `/fr/` hero, 1440** — The desktop crop cuts the hotel's own vertical blade sign down to "NX" at the top right and loses the top floor. The og:image (`og-facade.jpg`) shows the stronger full-façade framing. Evidence: `p4/home-1440-fold.png`. · **Fix:** adjust `object-position` (e.g. `center 30%`), or make a 1440 crop that keeps the blade sign in frame.

**B13 · P3 · `/ask/`, `/fr/demande/` success panel, phones** — The on-screen message is a 320 px inner scroll box holding 738 px of text, so name, e-mail, phone and message sit inside a nested scroll on a phone. There is no copy button for the subject: "Copy the message" puts the subject as the first line of the body, so a guest pasting into a new mail ends up with an empty subject field. Evidence: `p4/ask-390-done-full.png`. · **Fix:** no `max-height` on `.done-msg` below 48rem, or a "Show the whole message" toggle. Add a "Copy" button next to SUBJECT, like the one for TO.

**B14 · P3 · `/ask/` + FR mailto** — Body line breaks are encoded as bare `%0A`. RFC 6068 specifies `%0D%0A`. Gmail and iOS/Android mail handle `%0A`; some desktop clients (classic Outlook) can run lines together. · **Fix:** join lines with `\r\n` before `encodeURIComponent`.

**B15 · P3 · all pages, mobile menu** — The full-screen menu doesn't trap focus. After "Français", Tab moves to the page behind the overlay (breadcrumb "Hôtel Lynx", then the room jump list on `/rooms/`). · **Fix:** set `inert` on `main` and `footer` while the menu is open, or loop focus between the menu button and the last menu link.

**B16 · P3 · `/practical/` + FR** — The page repeats the homepage "Getting in" block word for word (night photo, "Late flight? Hire car? Fine.", both paragraphs, 4 tiles). "Finding us → By car / From the airport" then repeats the parking and airport sentences a third time. Evidence: `p4/practical-390-full.png`. · **Fix:** on `/practical/`, keep the 4 tiles and one photo as the opening block and drop the duplicated paragraphs. The details live in "Finding us".

**B17 · P3 · `/`, `/fr/` room thumbnails, phones** — `sizes="(min-width: 64rem) 18vw, 40vw"`, but the thumbs render at 116 px (≈30vw), and the smallest candidate is 600w: 2.6× the rendered width at 2× DPR (4× at 1×). · **Fix:** add a 320w variant in `tools/images.py` and set `sizes="(min-width: 64rem) 18vw, 30vw"`.

**Screenshots (`p4/`):** full pages at 390 for all 11 (`<page>-390-full.png`, `fr-*`), FR rooms/practical/ask at 360 (`*-360-full.png`), 1440 full for home/rooms/agadir/practical/ask/FR agadir, home folds at 360/390/430/1440 EN+FR (`*-fold.png`), maps (`agadir-390-map-*.png`, `agadir-1440-groups.png`), Lynx Line desktop (`home-1440-line-crop.png`), form errors / done EN+FR (`ask-390-errors.png`, `ask-390-done-*.png`, `fr-ask-390-done-fold.png`), menu (`menu-rooms-390.png`), room-list zoom (`home-390-rooms-list-zoom.png`).

## Fix log

_Phase 4 fix pass · FixLynx · 2026-10-02. All changes made in `content/*.json`, `tools/{build,templates,mapdata,images}.py`, `site/assets/{css,js}` and rebuilt (`images.py && mapdata.py && build.py`); `check_site` OK (11 pages). Screenshots: `/home/agent/agadir-pilot/qa/hotel-lynx/p4-fix/`. Overflow sweep 320/360/390/430/480/600/768/1024/1440 × 11 pages: `scrollWidth` = viewport everywhere (only the Your Agadir chip row scrolls inside itself, by design)._

| ID | Status | Fix · how verified |
|---|---|---|
| A1 | fixed | "Five kinds of room.<br>Shown as they are." / "…One standard."; FR "Cinq types de chambre.<br>Telles qu’elles sont." / "…Les mêmes bases." ("Un seul niveau" gone); "more" link + list label say room types · `home-390-full`, `rooms-1440-full`, `fr-rooms-390-single` |
| A2 | fixed | No universal "all up the stairs": "No lift: the upper floors are by the stairs." + "Stairs hard for you? Ask for a lower floor when you write." (rooms "What we don't do", FAQ, FR mirrors). The "Up the stairs" tick item in "What every room has" replaced by Room service (a "No lift" item under a ✓ icon would read as a feature; the lift stays in the No list) · built HTML grep + `home-390-full` |
| A3 | fixed | "Late flight? Hire car? Fine." → "Late flight?<br>Call ahead." / "Vol tardif ?<br>Appelez-nous avant."; p1, house rule and FAQ now say check-in ends 22:00, call reception before you travel, desk staffed 24 h — no "we'll expect you" · `home-390-full` (arrive), `practical-390-full` |
| A4 | fixed | FR intro "Un hôtel deux étoiles en plein centre-ville, et ça nous va très bien. Voici l’essentiel avant de réserver."; FR pass for calques (see A17) · `fr-home-360-basics` |
| A5 | fixed | Airport taxi everywhere = "ask reception about booking you a taxi" / FAQ "reception will try to arrange one" (no "Yes", no "we can book") · built HTML grep |
| A6 | fixed | No reply promised: ask intro/meta "ask what’s free and today’s price … Need an answer today? Call"; step 4 = call 24 h; done panel "just press send. In a hurry? Call reception, 24 hours a day." (no "straight to reception"); price band/FAQ "ask or call". Inbox question is SOT §g Q1 · decoded composed e-mails below |
| A7 | fixed | "Here’s the short version before you book." (no "whole deal / no small print") · `home-390-full` |
| A8 | fixed | "Walking times … follow the streets from our front door, at an easy pace — not as the crow flies" (EN/FR lead, home intro, meta) · built HTML grep |
| A9 | fixed | `dist()` in templates.py localises every distance: FR "1,1 km" … "6,4 km" with no-break space before the unit (EN keeps "1.1 km") · grep of `/fr/` + `/fr/votre-agadir/`: 0 dotted decimals |
| A10 | fixed | "In every room." / "Shower, basin and toilet. No bathtubs." (+ FR); caption no longer says "walk-in" · `rooms-1440-full` |
| A11 | fixed | Wake-up call "Ask at reception." / "Demandez à la réception." |
| A12 | fixed | Lynx Line cafés and banks show "3–4 min" (`min_label` in site.json), matching Your Agadir; "first cafés … three minutes" kept · `home-390-full` |
| A13 | fixed | "All day" / "Toute la journée" · `agadir-1440-full` |
| A14 | fixed | "Most of it is a walk away." / "Presque tout se fait à pied." |
| A15 | fixed | "No surprises" removed (A1); beach note "Nearest sand" / "Le sable le plus proche" |
| A16 | fixed | YES board item "Room service — Ask at the desk." (+ FR), also in "What every room has"; no menu/hours · `home-390-full` |
| A17 | fixed | "Le deal" → "En clair"; "Ce que chaque chambre a" → "Dans chaque chambre."; comptoir → "à l’accueil" / "La réception est ouverte jour et nuit"; "On monte aux étages … par l’escalier"; "Votre salle d’eau" → "Une salle d’eau privée"; "regardent vers" → "sont tournées vers"; taxis "circulent"; meta "Ce que vous trouverez dans chaque chambre" |
| A18 | fixed | build.py `fr_typo()` puts U+202F before : ; ! ? » and after « in all FR copy (text only, never in tags; the composed e-mail keeps plain spaces); FR quotes render «&#8239;…&#8239;» (EN quotes on FR pages too); aria-label "(24h/24)&#8239;: +212…" via `ui.colon` · `/fr/`: 0 “ ”, 31 U+202F |
| A19 | fixed (a, b) · kept (c) | (a) FR Hotel/HotelRoom `amenityFeature` names from `content/fr.json → ld`; (b) FAQ JSON-LD drops the trailing "— see where" link text ("…Talborjt is full of them."); (c) `aggregateRating` 8.4/1,009 **kept**: STANDARD §9 allows it with verified numbers and it is the exact Booking figure — orchestrator may drop it if Google's self-serving-review policy matters more |
| A20 | fixed | 404: own description, `<meta name="robots" content="noindex">`, no canonical/hreflang · grep `site/404.html` |
| A21 | fixed (by removal) | The Single no longer shows a borrowed bathroom photo at all (B7), so no layout claim remains |
| B1 | fixed | `tools/mapdata.py` draws `map-city-m.svg` (600×588, Lynx ↔ sand ↔ marina, sea on screen) shown below 48rem; wide map from 48rem; everything outside the phone frame (9 Souk El Had, Kasbah, CTM, Supratours, airport) listed under it as "Off this map" with bearing arrows + times; ring labels auto-placed clear of markers; no sideways scroll so the swipe hint and the JS centring are removed · `agadir-360-map-city`, `agadir-390-map-city`: frame scrollWidth = clientWidth (316/345) |
| B2 | fixed | `.dir-img picture{height:100%}` — thumbs fill their 4:3 boxes · `home-390-full` |
| B3 | fixed | Legend pairs wrapped in `.leg-i` (inline-flex), swatch always beside its own label · `agadir-390-map-door`, `agadir-1440-full` |
| B4 | fixed | Balcony buttons → `/ask/?balcony=1` / `/fr/demande/?balcony=1`; site.js ticks the box · in-tab: balcony checked, room "No preference", e-mail "Balcony if possible: yes" |
| B5 | fixed | 44×44 "FR"/"EN" plate in the header at every width (header re-fitted: ≤30rem burger-only + "☎ 24h"; ≤22.5rem icon-only phone; wordmark sub-line only 52–64rem); menu language = full-width 48 px row · header fit 320–1440, `menu-rooms-390`, `home-390-fold` |
| B6 | fixed | `.grps-grid{grid-template-rows:min-content 1fr}` ≥64rem — Beach/Getting around follow straight under Eat/Errands · `agadir-1440-full` |
| B7 | fixed | Single = black key-tag plate the size of a room photo ("15 m² · 1 single bed · We don’t have a photo of the Single yet"); the shower photo appears once (What every room has); unused `shower-*.webp` removed · `rooms-1440-full`, `fr-rooms-390-single` |
| B8 | fixed | `facade-m-1200.webp` (56 KB) added to the mobile `srcset` (800 + 1200) · images.py output |
| B9 | fixed | ≥44 px: footer phone/e-mail/Maps/Booking/lang, Route ↗ links, breadcrumb, header wordmark, `.btn-mini` copy buttons, menu e-mail |
| B10 | fixed | `m2()` sets "m²" in Overpass (`.u`) inside mono text · `home-390-full`, `fr-rooms-390-single` |
| B11 | fixed | No-break spaces "· Talborjt, Agadir" + `text-wrap:balance`: one line at 390, "…ÉTOILES / TALBORJT, AGADIR" at 360 FR · `home-390-fold`, `fr-home-360-fold` |
| B12 | fixed | Desktop hero `object-position:50% 47%`: blade sign reads "LYNX" with the fascia sign in frame · `home-1440-fold` |
| B13 | fixed | `.done-msg` no inner scroll below 48rem; "Copy" button for the subject; "Copy the message" copies the body only · in-tab clipboard: "Objet copié." → subject text; body copy starts "Bonjour Hôtel Lynx," · `ask-390-done-fr` |
| B14 | fixed | mailto body joined with CRLF (`%0D%0A`, no bare `%0A`) · decoded href below |
| B15 | fixed | Menu open → `main`, footer and sticky bar `inert`; Tab cycles menu → header only, never the page behind; Esc restores · in-tab Tab sequence |
| B16 | fixed | `/practical/` keeps photo, heading and the four time tiles; the parking/airport paragraphs live only in "Finding us" · `practical-390-full` |
| B17 | fixed | 320 w variants for the four directory thumbs (7 KB each), `sizes` 30vw on phones |

**Composed e-mails after the fix (decoded from the success-panel href, `/ask/?balcony=1` and `/fr/demande/?balcony=1`):** EN subject "Room request: 12 Nov – 15 Nov, 2 guest(s), No preference", body lines CRLF-joined: "Hello Hôtel Lynx, / I’d like to ask about a room: / Arrival: Thu, 12 Nov 2026 / Departure: Sun, 15 Nov 2026 (3 night(s)) / Guests: 2 / Room: No preference / Balcony if possible: yes / Parking needed: no / Arriving around: Not sure yet / Name: Élodie Brás-Nuñez / Email: elodie.bras@example.fr / Message: / Late — 23:40 & a low floor? / Thanks / Could you tell me what’s available and today’s price? Thank you. / Best regards, Élodie Brás-Nuñez". FR subject "Demande de chambre : 12 nov. – 15 nov., 2 personne(s), Pas de préférence", "Balcon si possible : oui", accents/&/em dash intact, no undefined/NaN. `window.open` stubbed; no tabs opened (the form only navigates to `mailto:`).
