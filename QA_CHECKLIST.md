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
| Reception 24 h | [VERIFIED: S1] | verified; paired with "tell us your arrival time" (one refused night arrival in S2) |
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
| Yes board: cleanliness 8.9, Wi-Fi 9.5, free parking (public), 24 h, AC every room, own shower room, satellite/cable TV, rooftop terrace facing the Kasbah hill | [VERIFIED: S1,S4 + photo bk_10] | verified |
| No board: no breakfast (cafés 3 min), no lift ("ask at the desk for a hand"), no pool/gym, no smoking rooms | [VERIFIED: S1,S2,S4]; luggage help [PROBABLE: S2,S5] | verified / help softened to "ask" |
| Room directory: 5 types, m², guests | [VERIFIED: S1] | verified; Single shown as a "15 m² · 1 single bed" plate (no photo exists) |
| Lynx Line: 16 walking stops with OSRM minutes/metres | [VERIFIED: S11,S12] | verified, "measured on foot from our front door" |
| "Talborjt … rebuilt after the 1960 earthquake" | context S11/S13 | plain context |
| "By taxi": promenade ~4, CTM ~5, Kasbah ~12, airport ~30 min; "petits taxis pass all day in town; for the airport, we can book you a taxi" | [VERIFIED: S12] times; taxi booking [PROBABLE: S2] | "about", "by road, traffic permitting"; orchestrator fix applied (retitled, airport line) |
| Getting in: free public parking, airport ~24 km, "ask us about booking you a taxi" | [VERIFIED: S1,S12]; [PROBABLE: S2] | softened ("ask us") |
| Reviews: Booking 8.4/1,009 + 7 subscores; Google 4.1/241 | [VERIFIED: S1,S4] | verified |
| Quotes EN: Ingo (title), Joanna, Kätlin, Lars | SOT §f 1,5,3,6 | exact text |
| Quotes FR: Alexandre (title), Chaimae, Linda; Joanna kept in English (`lang="en"`) | S2 raw `_bk_reviews_flat.json`, exact text | exact text, attribution name + country + Booking.com |
| Mini form → /ask/ ("nothing is booked or charged") | design | honest |

### Rooms `/rooms/` · `/fr/chambres/`
| Claim | Tag | Phrasing |
|---|---|---|
| In every room: AC, own shower room (walk-in shower, basin, toilet), towels, flat-screen TV satellite+cable, free Wi-Fi 9.5, wake-up call, non-smoking, stairs | [VERIFIED: S1] | verified |
| "No bathtubs" | photos bk_03/07/26/27 (S1) | verified from photos |
| "Towels and fresh linen — ready when you arrive" | towels [VERIFIED: S1] | plain |
| Single 15 m², 1 single bed, 1 guest; "We don't have a photo of the Single yet" + shower photo captioned "the shower room layout the Single shares with the Superior Single and Twin — not the bedroom" | [VERIFIED: S1]; Booking photo mapping (notes-rooms) | honest caption approach kept |
| Superior Single 16 m², single bed or large double "when one is free" | [VERIFIED: S1] ("if available") | verified |
| Twin 20 m², 2 single beds; "on Booking.com listed as a Double Room with two single beds" | [VERIFIED: S1] | verified |
| Double 20 m², large double; "Some of our Doubles open onto a small balcony — we can't promise one" | beds [VERIFIED: S1]; balcony [PROBABLE: S2 + photo bk_02] | softened |
| Triple 20 m², large double + single; "We don't add extra beds" | [VERIFIED: S1] (no extra beds) | verified |
| Photo captions only describe what is visible (balcony, round table, dressing table) | photos S1 | verified |
| What we don't do: breakfast, lift, pool/gym, extra beds, smoking rooms | [VERIFIED: S1,S2,S4] | verified |
| Balcony block: "Many of our rooms have a small balcony; some look towards the Kasbah hill. We can't promise one" + Nabilah quote | [PROBABLE: S2] + photos; quote SOT §f 9 | softened; quote exact (kept in English on FR page) |
| "Ask for today's price" (no prices) | prices [STALE] | no figures |
| JSON-LD HotelRoom ×5 (floorSize, occupancy, bed) | [VERIFIED: S1] | verified, no aggregateRating on this page |

### Your Agadir `/your-agadir/` · `/fr/votre-agadir/`
All minutes/distances = OSRM from the verified pin (`research/notes-neighbourhood.md` §3) [VERIFIED: S11,S12]; bearings computed from OSM coordinates at build time; named places exist in OSM (trading/opening hours not claimed).
| Claim | Tag | Phrasing |
|---|---|---|
| "Every walking time … measured on foot from our front door, along the streets — not as the crow flies" | S12 method | verified |
| Eat: restaurants from 70 m / 1 min; cafés 3–4 min / 230–300 m; "We don't serve breakfast. Talborjt does" | [VERIFIED: S11,S12; S1,S2] | categories only, no café names |
| Breakfast quote EN Colin ("No breakfast cafe although loads of nice cafes nearby"), FR Audrey | S2 raw, exact text | exact |
| Errands: pharmacy 2 min/150 m (second 4 min/310 m); banks 3–4 min/200–310 m (Al Barid, Attijariwafa, Bank of Africa); post office 3 min/200 m (Amana / Poste Talborjt); supermarkets 5–7 min/370–520 m (Marjane Market, Carrefour Market, Aswak Assalam) | [VERIFIED: S11,S12] | verified; "banks", never "ATMs/cash" |
| Sights: mosque 1, Jardin Ibn Zaïdoun 7, Jardin d'Olhão 10, Musée Mémoire 11 ("the city and the 1960 earthquake"), Amazigh Heritage Museum 15, central market 16, Vallée des Oiseaux 20 ("on the way to the beach"), cable car lower station 23 (~4 by taxi), Souk El Had 30 (~4), Marina entrance 35 (~4) | [VERIFIED: S11,S12,S13] | verified; "opening times change, check locally" (no hours) |
| Kasbah hilltop: not a walk, ~12 min by taxi or the cable car | [VERIFIED: S12] | "about" |
| Beach: promenade 23 min / 1.7 km (~4 taxi), sand 25 min / 1.9 km (~5 taxi) | [VERIFIED: S11,S12] (Booking's 19 min = wrong pin, not used) | verified |
| Transport: petits taxis "flag one down, or ask reception to call one"; CTM ~5 min / 3.2 km; Supratours ~5 min / 3.7 km "check your ticket for the departure point"; airport ~30 min / 24 km, "petits taxis don't serve the airport — we can book you a taxi" | [PROBABLE: S2]; [VERIFIED: S12]; Supratours [PROBABLE]; orchestrator airport wording | softened / "about" |
| Two maps drawn from OSM (roads, coast, beach, parks, Rue Ibn Toumert), rings "distance as the crow flies", unnamed dots for eat/errands | S11 (ODbL) | credit "Map data © OpenStreetMap contributors" on page |
| "Open in Google Maps" + per-place "Route ↗" (Google directions from the pin) | pin [VERIFIED: S4] | — |

### Practical `/practical/` · `/fr/infos-pratiques/`
| Claim | Tag | Phrasing |
|---|---|---|
| Times, reception 24 h, parking free | [VERIFIED: S1,S4] | verified |
| By car: public spaces right by the hotel, "public, so we can't reserve one" | [VERIFIED: S1,S4] (type PUBLIC) | verified + honest limit |
| From the airport: ~24 km, ~30 min by taxi, "we can book you a taxi" | [VERIFIED: S12]; [PROBABLE: S2] | softened |
| By bus: CTM and Supratours ~5 min by petit taxi | [VERIFIED: S12]; Supratours [PROBABLE] | "about" |
| From the beach: 23 min on foot, ~4 by taxi | [VERIFIED: S12] | verified |
| House rules: check-in/out, "ask at the desk if you need a little longer", non-smoking, no pets, no lift, not wheelchair accessible | [VERIFIED: S1]; late check-out [PROBABLE: S2] | late check-out softened to "ask" |
| FAQ: no breakfast; free public parking; no lift + "ask for a hand"; arrival after 22:00 → tell us your time; airport taxi on request; Wi-Fi free 9.5; "Is it quiet?" → mosque across the square, lively streets; no pool/gym; laundry "ask at reception"; price → ask / Booking.com | [VERIFIED: S1,S2,S4]; laundry/taxi [PROBABLE: S2,S5] | honest; never "quiet"; laundry reduced to "ask at reception" |
| FAQPage JSON-LD mirrors the visible FAQ | — | — |

### Ask `/ask/` · `/fr/demande/` (+ homepage mini form)
| Claim | Tag | Phrasing |
|---|---|---|
| "This form doesn't book or charge anything: it writes a clear email to our reception" | design | honest |
| "Reception replies with what's free and today's price" | email [VERIFIED: S3] | hotel voice |
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
- On phones the city map is wider than the screen and scrolls sideways inside its frame (starts centred on the hotel).
