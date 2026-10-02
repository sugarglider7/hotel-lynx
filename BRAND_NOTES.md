# BRAND NOTES — Hôtel Lynx (phase 2, 2026-10-02)

Fact tags refer to `SOURCE_OF_TRUTH.md` (S# = its Sources table). Copy lives in `content/en.json` (FR: `content/fr.json`, same keys).

## 1. Positioning

- **What it sells emotionally:** relief. A clean, straightforward room in the real centre of Agadir, a desk that is always staffed, Wi-Fi and parking that just work, a sensible price — so the city is the experience, not the hotel. "Your base in Agadir."
- **Who the customer is:** independent travellers and couples on a budget, Moroccan and European road-trippers with a car, people on short city stays or transit (airport/bus), returning guests (one first came 19 years ago, S2). They compare on Booking.com, read the scores, and hate surprises.
- **Primary conversion:** an availability request that composes a clear email to agadir.hlynx@gmail.com [VERIFIED: S3], plus an always-visible "Call reception (24h)" `tel:+212528847886` [VERIFIED: S3,S4,S6]. Secondary: Booking.com listing [VERIFIED: S1]. **No WhatsApp anywhere** (no verified number).
- **Visual thesis:** the hotel's own façade is the brand book — a dusty-pink block, a black ground floor, a black sign plate with white capitals. The site is that building turned into a wayfinding system: crisp black plates, one hot signal colour, mono numerals, transit-map clarity. Anti-resort confidence: honest about what it is, proud of what it does well.

## 2. The one creative concept — "Signposted"

The website is the hotel's own sign system, and the city is the destination.
1. **The fascia hero.** The façade photo (pink upper floors) runs straight into a black band — the building's real black ground floor becomes the hero's text panel. Their sign "HOTEL LYNX" stays visible in the photo; our wordmark repeats it as a black plate.
2. **Fingerposts** on the hero photo (desktop): "Mohammed V Mosque 1 min ↙ · Cafés for breakfast 3 min · Beach promenade 23 min ↙" — arrows rotated to the real compass bearing from the verified pin.
3. **The Lynx Line** (signature, "Your Agadir from Lynx"): a transit-map strip in walking minutes, 0 → 35, stations as rings, names at 45° (desktop) / a vertical line with proportional gaps (mobile). Every time is OSRM-measured from the door [VERIFIED: S11,S12]; every arrow is the real bearing. A "petit taxi" branch adds the by-road times.
4. **Key-tag rooms:** rooms are a numbered directory (01–05), each with a black key-fob numeral, not a card grid.
5. **The yes/no board:** "What we do. What we don't." — a white YES plate and a black NO plate, turning "no breakfast / no lift / no pool" into confidence.
- **Lynx, subtly:** one shape only — the chamfered top-right corner on every plate/button (a sharp ear-tuft cut), and a flattened orange diamond "eye" between HOTEL and LYNX in the wordmark/favicon. No cats.

## 3. Typography

Self-hosted Overpass + Overpass Mono (registered in `/home/agent/agadir-pilot/FONTS.md`). Overpass is the open-source descendant of Highway Gothic, the road-sign face: wayfinding DNA, honest, crisp, normal width (not Line Up's condensed/expanded surf-mag display, not Hala's editorial voice). Mono = room-key numerals, minutes, labels (only Lynx uses a label face in this batch).

| role | family / weight | 390 px | 1440 px |
|---|---|---|---|
| h1 | Overpass 800, lh .94, -0.022em | 46 px | 96 px (clamp 2.875→6rem) |
| h2 | Overpass 800, lh .98 | 38 px | 68 px (clamp 2.375→4.25rem) |
| room name / big quote | Overpass 800 | 26 / 32 px | 36 / 56 px |
| h3 | Overpass 700 | 19 px | 19–20 px |
| intro | Overpass 400 | 18 px | 21 px |
| body | Overpass 400, lh 1.55 | 17 px | 17 px |
| labels / kickers | Overpass Mono 600 caps, +0.08em | 12–13 px | 12–13 px |
| numerals (minutes, keys) | Overpass Mono 500–600, tabular | 22–28 px | 17–28 px |
| scorecard figure | Overpass 800 | 80 px | 128 px |
| wordmark | Overpass 700 caps, +0.24em, in black plate | 13 px | 15 px |

Hosting: woff2 from the Google Fonts CSS2 API (modern UA), latin + latin-ext per family = 4 files on disk; `unicode-range` means EN/FR pages download only the 2 latin files (61 KB; latin covers é è à ç œ). Preload of Overpass latin. Self-hosting = no third-party request, no layout shift beyond swap. Note: Overpass's middle dot "·" collapses the following space — use mono for "·" separators or other punctuation.

## 4. Palette (sampled with Pillow from the hotel's own photos)

| token | hex | source |
|---|---|---|
| `--ink` | #15110F | black sign panel + black ground floor, bk2048_01 (#110a07 / #26201f) |
| `--white` | #FFFDFC | the sign's white capitals |
| `--facade` | #C8B2B4 | façade wall, bk2048_01 upper right (#c8b2b4) |
| `--facade-l` | #E6D9D9 | façade tint (Agadir section ground) |
| `--paper` | #F5EFEE | façade pink lifted to paper (page ground) |
| `--sig` | #D4652F | backlit reception desk glow, bk2048_12 (#c65927, lifted for 5:1 contrast with ink text) — CTAs, station dots, scores |
| `--night` | #384770 | blue-hour sky over the hotel, bk2048_05 (#3a476e) — "Getting in" band |
| `--tile` | #1C274D | zellige stair risers, bk2048_14 — reserve |
Text on `--sig` is always ink (5.1:1); white is never set on orange.

## 5. Grid, spacing, imagery, motion

- **Grid:** max 84rem, side padding clamp(20→40 px); section rhythm clamp(64→128 px). Desktop splits 7/5 (hero fascia, yes/no board, arrive), 5/7 (reviews), 8/4 (form/side). Section headers on desktop: h2 left, intro right, kicker above.
- **Section grounds alternate:** ink (hero fascia) → paper (deal) → white (rooms) → façade tint (Agadir) → night blue (getting in) → paper (reviews) → white (ask) → ink (footer).
- **Image treatment:** real Booking-gallery photos only (property's own pro shoot; owner OK pending, SOT Q11). Straight, untinted, square-cornered, cropped hard (4:3 / 3:2) with a mono caption that says plainly what the photo shows ("This Double has a balcony", "Shower room — the Single, Superior Single and Twin share this layout"). No filters, no duotone, no beach/resort stock. Dominant colour behind every image; WebP q72–74; hero mobile crop 800 w (34 KB).
- **Motion:** minimal and functional. Rows/figures fade-up 0.6 s once (IntersectionObserver); the Lynx Line draws once in signal orange along the route (1.6 s). Nothing loops. `prefers-reduced-motion` = no motion; content visible without JS.

## 6. Navigation, CTAs, sticky action, forms

- **Desktop nav:** sticky paper bar — wordmark plate · "Talborjt · Agadir" · numbered links (01 Rooms, 02 Your Agadir, 03 The deal, 04 Reviews) · "Call 24h +212 5 28 84 78 86" · orange "Ask for a room".
- **Mobile nav:** wordmark · outlined "☎ 24h" call button · black burger. Menu = full-screen black **directory board** (numbered rows 01–05, big type), call button + email at the foot. aria-expanded, Esc closes and returns focus, closes on link tap.
- **CTAs:** primary = orange chamfered plate with ink text + arrow ("Ask for a room"); secondary = outlined (no chamfer) "Call reception (24h)". One primary per view.
- **Sticky mobile bar** (< 64rem): black bar with "Call 24h" + "Ask for a room"; appears after the hero, hides whenever the form section or the footer is on screen (never covers submit or footer).
- **Forms:** 2 px ink borders, square corners, 52 px fields, ≥17 px text (no iOS zoom), mono caps labels, orange focus ring, inline errors in #B3341A with aria-invalid/aria-describedby, custom square checkboxes.

## 7. Page map (EN root + FR mirror)

| key | EN | FR | status |
|---|---|---|---|
| home | `/` | `/fr/` | EN built (phase 2) |
| rooms | `/rooms/` | `/fr/chambres/` | phase 3 |
| agadir | `/your-agadir/` | `/fr/votre-agadir/` | phase 3 |
| basics | `/practical/` | `/fr/infos-pratiques/` | phase 3 |
| ask | `/ask/` | `/fr/demande/` | phase 3 |
| 404 | `/404.html` | (same file, bilingual line in phase 3) | built |
Reviews stay a homepage section (nav "Reviews" → `/#reviews`). `tools/build.py` falls back to the homepage anchor for any page not yet built, so links never dangle; when a page is added to `PAGES` + its `slug` to `content/<lang>.json`, nav and hreflang/switch update automatically.

### Homepage (built) — section order
1. **Hero / fascia** — façade bk2048_01 (mobile crop `facade-m-800`); "Your base in Agadir."; lead (clean rooms, 24 h reception, free Wi-Fi, free parking, opposite Mohammed V Mosque) [VERIFIED: S1,S4,S11]; CTAs; score plate 8.4 Booking · 1,009 reviews · 9.2 staff [VERIFIED: S1]; fingerposts mosque 1 / cafés 3 / promenade 23 min [VERIFIED: S12].
2. **The deal (yes/no board)** — YES: cleanliness 8.9, Wi-Fi 9.5, free public parking, 24 h reception, AC, private shower room, satellite TV, rooftop terrace [VERIFIED: S1,S4]. NO: breakfast (cafés 3 min) [VERIFIED: S1,S2; S12], lift ("ask at the desk for a hand" — soft) [VERIFIED: S1; PROBABLE: S2], pool/gym [VERIFIED: S4], smoking rooms [VERIFIED: S1]. Image: reception bk2048_12.
3. **Rooms** — 01 Single 15 m² · 02 Superior Single 16 m² · 03 Twin 20 m² · 04 Double 20 m² · 05 Triple 20 m², beds/guests [VERIFIED: S1]; images bk2048_26 (shower room, honestly captioned for Single), bk2048_06, bk2048_22, bk2048_02, bk2048_21; notes "many rooms have a small balcony — ask" [PROBABLE: S2], "ask for today's price" (prices STALE).
4. **Your Agadir from Lynx** — terrace bk2048_10; the Lynx Line (16 walking stops) + taxi branch (promenade 4, CTM 5, Kasbah 12, airport ~30 min) [VERIFIED: S11,S12]; "Talborjt … rebuilt after the 1960 earthquake" (S11/S13 context).
5. **Getting in** — bk2048_05 blue hour over the car park; check-in 12–22, check-out 12, reception 24 h, free public parking [VERIFIED: S1,S4]; "ask us about booking you a taxi" [PROBABLE: S2].
6. **Reviews** — Booking 8.4/1,009 + all seven subscores, Google 4.1/241 [VERIFIED: S1,S4]; quotes Ingo (title), Joanna, Kätlin, Lars (SOT §f, exact text).
7. **Ask for a room** — form + "Rather talk?" plate (tel, email, Booking.com).
Footer: address, "Opposite the Mohammed V Mosque", Google Maps link on the verified pin, phone, email, Booking.com, check-in/out, two-star.

### Phase 3 pages — planned sections
- **/rooms/**: intro + shared equipment line [S1]; five full room entries (key tag, specs, all Booking photos per type from notes-rooms mapping, bathroom set bk_03/07/26/27); "What's not in the room" honesty list (no fridge/kettle claims; stairs only) [S1,S2]; balcony note [PROBABLE]; CTA per room → /ask/?room=key.
- **/your-agadir/**: the Lynx Line full-width + grouped lists (Within 5 min / 10–16 / 20–35 / by taxi) with bearings; "Breakfast round the corner" block (cafés/crèmeries by category, Audrey quote on FR) [S2,S12]; transport (CTM/Supratours ~5 min by taxi, airport ~30 min) [S12; Supratours PROBABLE]; views bk_09/bk_10; link out for attraction hours (never state hours).
- **/practical/**: the full yes/no board; getting here (car/airport/bus); house rules: check-in/out, pets not allowed, non-smoking, no lift [S1]; FAQ (breakfast, parking, lift, pool, late arrival). Omit children & payment until owner confirms (SOT Q2/Q3).
- **/ask/**: the same form as the homepage, room preselect from `?room=`, side plate, what happens next.

## 8. Conversion flow (verified channels only)

**Fields:** arrival* (date, ≥ today) · departure* (date, > arrival; auto-set to arrival+1) · guests* (1–12) · room (No preference / Single / Superior Single / Twin / Double / Triple) · arriving around (Not sure yet / before 14:00 / 14–18 / 18–22 / after 22:00) · balcony if possible ☐ · parking needed ☐ · name* · email* (pattern) · phone/WhatsApp (optional; the guest's own number) · message (optional).
**Validation:** client-side, inline per field, focus first invalid; messages in page language.
**On submit:** compose and open `mailto:agadir.hlynx@gmail.com?subject=…&body=…`; replace form by success panel: "Your email is ready" + "Didn't open? Try again" (same mailto) + "Copy the message" (clipboard, textarea fallback) + "Or call reception, 24h: +212 5 28 84 78 86".
**EN template**
```
Subject: Room request: {12 Oct} – {15 Oct}, {2} guest(s), {Double}
Hello Hôtel Lynx,

I'd like to ask about a room:

Arrival: {Mon 12 Oct 2026}
Departure: {Thu 15 Oct 2026} ({3} night(s))
Guests: {2}
Room: {Double}
Balcony if possible: {yes/no}
Parking needed: {yes/no}
Arriving around: {18:00–22:00}

Name: {…}
Email: {…}
Phone / WhatsApp: {…}            (only if given)

Message:                          (only if given)
{…}

Could you tell me what's available and today's price? Thank you.

Best regards,
{Name}
```
**FR template** (phase 3, `content/fr.json` → `ask.mail`)
```
Objet : Demande de chambre : {12 oct.} – {15 oct.}, {2} personne(s), {Double}
Bonjour Hôtel Lynx,

Je souhaiterais réserver une chambre :

Arrivée : {lun. 12 oct. 2026}
Départ : {jeu. 15 oct. 2026} ({3} nuit(s))
Personnes : {2}
Chambre : {Double}
Balcon si possible : {oui/non}
Parking nécessaire : {oui/non}
Arrivée prévue vers : {18:00–22:00}

Nom : {…}
E-mail : {…}
Téléphone / WhatsApp : {…}

Message :
{…}

Pourriez-vous m'indiquer vos disponibilités et le tarif du jour ? Merci.

Bien cordialement,
{Nom}
```
**Fallbacks:** tel 24 h always visible (header, hero, sticky bar, side plate, footer, success panel); Booking.com secondary; if the owner gives a WhatsApp mobile, add wa.me as a second submit target (same composed text) — not before.

## 9. Must NOT look like

- Hala Tours (joyful colour-burst, photographic editorial travel guide, mood discovery) — Lynx is graphic, two colours + one signal, plates not collages.
- Line Up Surf House (surf-publication editorial, Anybody expanded display + Newsreader serif, horizon/line-up geometry) — Lynx has no serif, no expanded/condensed display, its line is a transit route with stations, not a horizon.
- hyle-surfhouse.peashoot.io (warm, host-centred surf house), agadir-trip / agadir-camel-horse (tour sellers) — no host portraits, no activity cards, no sunset-camel imagery.
- Fake luxury: no gold, no black-and-gold, no script fonts, no "boutique", no spa/pool imagery, no "oasis".
- Generic Morocco beige / riad template: no arches as frames, no zellige wallpaper as background pattern, no lantern icons.
- SaaS/template: no glassmorphism, gradients, rounded-card grids, icon-grid "amenities", stock imagery, cartoon cats.
