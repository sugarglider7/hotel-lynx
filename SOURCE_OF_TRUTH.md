# SOURCE OF TRUTH — Hôtel Lynx, Agadir

_Research phase 1, compiled 2026-10-02. Tags: `[VERIFIED: S#]` use freely · `[PROBABLE: S#]` soften · `[CONFLICT: S#,S#]` · `[STALE]` never as current · `[UNVERIFIED]` do not publish._
_Detailed working notes: `research/notes-reviews.md`, `research/notes-neighbourhood.md`, `research/notes-rooms.md`._

## (a) Sources

| S# | URL | type | date checked | notes |
|---|---|---|---|---|
| S1 | https://www.booking.com/hotel/ma/lynx.html (hotel id 9264024) | listing | 2026-10-02 | Property page (raw `_bk.html` + re-opened live in 1 browser tab). Rooms, sizes, beds, facilities, policies, ratings, 27 photos. Booking search dates Nov 10–12 2026 show 5 room types bookable. |
| S2 | Booking.com ReviewList (GraphQL, loaded from S1 "Read all reviews") | review | 2026-10-02 | 377 unique reviews: newest 327 (2025-08-03→2026-09-27) + 50 lowest. Raw `_bk_reviews*.json`. |
| S3 | S1 → `legalInfo.traderInfo` (trader details the business declared to Booking) | official (business-declared) | 2026-10-02 | Trade name HOTEL LYNX, reg. no. 9195-01, address "N 9 RUE MEHDI BEN TOUMERT NOUVEAU TALBORJT AGADIR 80000", email agadir.hlynx@gmail.com, phone +212528847886. |
| S4 | https://www.google.com/maps/place/Hotel+Lynx/@30.4228588,-9.5917027,17z (CID 0x16ddb0725a480466) | listing | 2026-10-02 | Name "Hotel Lynx", 2-star hotel, 4.1★ / 241 reviews, phone, address, plus code CCF5+48, no website ("Add website"), unclaimed-looking ("Claim this business" shown). |
| S5 | S4 → Reviews tab ("Most relevant", 30 read) | review | 2026-10-02 | Includes 2 Tripadvisor reviews syndicated by Google. Raw `_g_reviews.json`. |
| S6 | https://www.telecontact.ma/annonceur/hotel-lynx/3120133/agadir.php | other (Moroccan yellow pages) | 2026-10-02 | "9 rue Ibn Toumert, Talborjt"; Tel 1 05 28 84 78 86, Tel 2 05 28 84 78 87, Fax 05 28 84 78 63; SARL created 2003, RC 9195 Agadir, capital 1,000,000; labels it "Hôtel 3*". |
| S7 | https://www.marocannuaire.org/Annuaire/Details_infos.php?e=HOTEL+LYNX&activite=Hotel&ville=AGADIR&p=&id=3434 | other (directory, undated) | 2026-10-02 | +212 528 847 886 / 887; email agadirhotellynx@gmail.com; services "climatisation, cafétéria, TV satellite, room service, téléphone, douche-WC, terrasse panoramique". Likely old. |
| S8 | https://www.tripadvisor.com/Hotel_Review-g293731-d26100627-Reviews-Hotel_Lynx-Agadir_Souss_Massa.html | review | 2026-10-02 | Page blocked (captcha) by fetch and browser; figures only from search-engine snippet: 5.0, 2 reviews, #70 of 112. |
| S9 | https://www.priceline.com/hotel-deals/en-us/P5000481199/H285223703/hotel-lynx.ssp (raw `_pl.html`) | listing | 2026-10-02 | 2-star; aggregateRating 8.6/10 from 238 reviews; uses Booking photos. |
| S10 | Affiliate mirrors: lynx.hotelagadir.net, lynx.hotelagadir.org, lynx.agadirhotelsonline.com, lynx.hotels-agadir.com, lynx.agadir-hotels.net, lynxagadir.ma-hotels.net, lynx.agadirhotels.org, hotelpascher.org/lynx | other | 2026-10-02 (raw from 04:44) | Same template network; "41 rooms"; re-host Booking photos on pixcdn.co. Not independent. |
| S11 | OpenStreetMap via Overpass API / Nominatim | other | 2026-10-02 (OSM base 04:25Z) | Street geometry (Rue El Mahdi Ibn Toumert, way 330793179), POIs, beach/corniche geometry. |
| S12 | OSRM `routing.openstreetmap.de` routed-foot / routed-car | other | 2026-10-02 | All distances/times in `research/notes-neighbourhood.md`. |
| S13 | https://www.getyourguide.com/fr-fr/explorer/agadir-ttd1413/best-museums-in-agadir/ ; https://immersi-travel.com/le-jardin-dolhao-agadir/ | other | 2026-10-02 | Musée Mémoire d'Agadir in Jardin d'Olhão, plus code CCF2+WJ8, hours Tue–Sun 9:30–12:30/14:30–18:30. |
| S14 | https://www.kayak.com/Agadir-Hotels-Hotel-Lynx.9739428.ksp ; planetofhotels | listing | 2026-10-02 | Captcha — unusable. |
| S15 | web search: Facebook / Instagram / official site | social | 2026-10-02 | **No official website, Facebook or Instagram found.** "Lynx Optique" (@lynxoptiqueagadir) is an unrelated optician. |

## (b) Contact block

| Field | Value | Source / tag |
|---|---|---|
| Name (as displayed) | **Hôtel Lynx** (Booking) · **Hotel Lynx** (Google, façade sign "HOTEL ⟨HL monogram⟩ LYNX") · "HOTEL LYNX" (trade register) | [VERIFIED: S1,S3,S4] + façade photo bk_01 |
| Google listing title variant | "Hôtel Lynx Agadir Talborjt" (search query match) | [PROBABLE: S4] |
| Legal | SARL, created 2003, RC 9195 Agadir (Booking reg. no. 9195-01) | [VERIFIED: S3,S6] — not for the site except legal footer if owner wants |
| Address | **9 Rue Al Mahdi Ibn Toumart, Talborjt, 80000 Agadir, Morocco** | [VERIFIED: S1,S3,S4,S6] (spellings vary: Ibn Toumert / Mehdi Ben Toumert) |
| District | Talborjt (Booking also files it under "Swiss City") | [VERIFIED: S1,S4,S11] |
| Coordinates | **30.4228588, -9.5917027** (Google pin; plus code CCF5+48 Agadir) | [VERIFIED: S4,S11] — Booking's 30.427755,-9.598107 is the "Cité Suisse" district centroid → **wrong, never use** [CONFLICT: S1,S4 → S4 wins] |
| Phone 1 | **+212 5 28 84 78 86** (05 28 84 78 86) | [VERIFIED: S3,S4,S6,S7] — landline |
| Phone 2 | +212 5 28 84 78 87 | [PROBABLE: S6,S7] directories only |
| Fax | 05 28 84 78 63 | [STALE] don't publish |
| WhatsApp | **none found** | [UNVERIFIED] — no wa.me link until owner gives a number |
| Email | **agadir.hlynx@gmail.com** (declared to Booking as trader contact) | [VERIFIED: S3] |
| Email (alt) | agadirhotellynx@gmail.com | [CONFLICT: S3,S7] — directory only; ask owner which is monitored |
| Website | none (Google shows "Add website") | [VERIFIED: S4] |
| Socials | none found | [VERIFIED: S15] (absence) |
| Booking.com URL | https://www.booking.com/hotel/ma/lynx.html | [VERIFIED: S1] |
| Reception | 24-hour front desk | [VERIFIED: S1] (one Aug-2026 review reports a refused night arrival → ask owner) |
| Check-in | from 12:00 to 22:00 | [VERIFIED: S1] (24h desk + reviews of late-night check-ins → "arriving later? tell us") |
| Check-out | until 12:00 | [VERIFIED: S1] |
| Star rating | **2 stars** | [VERIFIED: S1,S4,S9]; Telecontact says 3* [CONFLICT: S1,S6 → use 2★ or omit] |

## (c) Facts by topic

### Property & facilities
- Hotel (Booking accommodation type HOTEL), 2-star. [VERIFIED: S1,S4]
- Air-conditioned rooms; AC also heats ("Die Klimaanlage spendet Wärme an kalten Tagen"; "silent AC (worked perfectly on heat)"). AC [VERIFIED: S1]; heating mode [PROBABLE: S2]
- Private bathroom in **all** rooms (`isPrivateBathroomInAllRooms: true`), with shower, toilet, towels, toilet paper. [VERIFIED: S1]
- Flat-screen TV with satellite and cable channels in every room type. [VERIFIED: S1]; English channels incl. football [PROBABLE: S5]
- Free Wi-Fi: Booking guest Wi-Fi score 9.5; Booking description "Guests enjoy free WiFi"; Google amenity "Free Wi-Fi". [VERIFIED: S1,S4] (2 recent complaints of slow/no Wi-Fi → don't promise speed)
- **Free parking**: Booking facility "Parking", chargeMode FREE, type PUBLIC, not off-site; highlights "Free parking", "Parking on site". Google "Free parking". Reviews: parking in front and behind the building, large public car park by the hotel, easy to park. → "Free public parking right by the hotel" [VERIFIED: S1,S4,S2]. Not a private/guarded/reserved car park [UNVERIFIED]. One nearby lot in OSM is tagged fee "3DH" (way 135585218) → don't say "all parking around is free".
- Covered parking for a motorbike — one review [PROBABLE: S2] → "ask us".
- 24-hour front desk. [VERIFIED: S1]
- Room service. [VERIFIED: S1] (what it consists of is unknown — no food service evidenced; one guest: "Ahmed for the tea") → list as "room service" without menu claims.
- Terrace (Booking) = rooftop terrace with city view (photos bk_10/bk_04/bk_08; reviews "Taras na dachu z widokiem na miasto", "le rooftop"). [VERIFIED: S1 + photos]; one review "Rooftop moins bien aménagé" → don't oversell.
- Balconies: Booking photos show room balconies with wrought-iron rails; "la plupart des chambres en ont une" (Quentin, FR). Not listed as a room facility on Booking. [PROBABLE: S2] → "many rooms have a balcony — ask".
- Lobby with lounge + zellige-tiled Moroccan salon (photos bk_11/12/13). [VERIFIED: photos S1]
- **No lift — upper floors by stairs only.** [VERIFIED: S1 "Upper floors accessible by stairs only"; S2 multiple]
- **No pool, no gym.** Google amenities list Pool = no, Fitness = no [VERIFIED: S4]; "No swimming pool" (S2).
- No fridge, no kettle in rooms (reviews). [PROBABLE: S2] → don't list.
- Wheelchair accessible: **no** (`isWheelChairAccessible: false`). [VERIFIED: S1]
- Smoking: all 5 room types non-smoking (`isSmoking: false`); no designated smoking area. [VERIFIED: S1]
- Wake-up service / alarm clock. [VERIFIED: S1]
- Luggage help: staff carry luggage up (Google, Booking AI summary "luggage assistance"). [PROBABLE: S2,S5]. Luggage storage as a service [UNVERIFIED].
- Laundry: "they also provide laundry service if needed" (Diletta, Italy); "laundry related … without additional cost" (Google). [PROBABLE: S2,S5] → "ask at reception".
- Airport taxi arranged by reception (4 reviews 2026). [PROBABLE: S2] → "we can book you a taxi"; **no airport shuttle** of the hotel's own [UNVERIFIED]; prices never.
- Tickets printed for guests (Gabrielė). [PROBABLE: S2] — minor, optional.
- Daily room cleaning. [PROBABLE: S2] (Ingo, Quentin, Audrey, Chevenon) → "rooms cleaned daily" is consistent and safe-ish; confirm with owner.
- Number of rooms: 41. [PROBABLE: S10] (affiliate template only) → ask owner; don't publish yet.
- Year: business (SARL) created 2003 [VERIFIED: S6]; returning guest's "first visit was 19 years ago" (≈2006) consistent. Hotel opening year itself [UNVERIFIED].
- Cafeteria/café on site: [STALE: S7] — reviews say "No breakfast cafe". Never claim.

### Breakfast — VERDICT: **NOT OFFERED** [VERIFIED: S1,S2]
Evidence: (1) Booking: every rate for all 5 room types says "No meal is included in this room rate"; property `meals: []`, `mealPlans: []`, `breakfastType: 0`, current breakfast review score = 0 reviews (an older legacy field shows 7.5 from 5 reviews → breakfast existed long ago [STALE]). (2) Reviews 2025–2026 explicitly: "No breakfast cafe although loads of nice cafes nearby" (Colin, UK, Aug 2026); "Il n y avait de petit déjeuner" (David, Morocco, Jul 2026); "No breakfast facilities" (Martin, UK, Mar 2026); "No hay desayuno pero hay mucho café acerca del hotel" (Dec 2025); "il ne sert pas le petit déjeuner" (Audrey, Oct 2025); "Manque de petit déjeuner" (Lahsen, Dec 2025). (3) Neighbourhood breakfast: bakery opposite/next door, breakfast places from 7:30 nearby (Kirsten DE, M NL, Véronique FR, Audrey FR). → Site: turn it into a feature ("Breakfast is round the corner"), never imply in-house breakfast.

### Rooms — see table in `research/notes-rooms.md`; summary
| Booking room type (room id) | Beds (Booking en-gb terms) | Max guests | Size | Notes |
|---|---|---|---|---|
| Single Room (926402401) | 1 single bed | 1 | 15 m² | [VERIFIED: S1] |
| Superior Single Room (926402402) | 1 single bed **or** 1 large double bed (choose if available) | 1 | 16 m² | [VERIFIED: S1] |
| Double Room — twin (926402403) | 2 single beds | 2 | 20 m² | [VERIFIED: S1] Booking names this "Double Room" too |
| Double Room (926402404) | 1 large double bed | 2 | 20 m² | [VERIFIED: S1] |
| Triple Room (926402405) | 1 single bed + 1 large double bed | 3 | 20 m² | [VERIFIED: S1] |
All five: AC, private bathroom with shower + toilet, towels, flat-screen TV (satellite + cable), wake-up service/alarm clock, non-smoking, upper floors stairs-only, no cribs/extra beds. [VERIFIED: S1]
Not listed by Booking for any room → do not claim: desk, wardrobe, safe, minibar, fridge, kettle, hairdryer, balcony, view, soundproofing, toiletries. Photos show wooden wardrobes, small tables/chairs and balconies in some rooms [PROBABLE: photos] (one review: "not quite enough room to open the wardrobes").
US-English Booking pages render "single bed" as "twin bed" and "large double bed" as "queen bed" — same data.

### Policies
- Children: **"Children not allowed"** (`allowChildren: false`), no cribs, no extra beds. [VERIFIED: S1] **but** Booking review filter shows 46 "Families" reviews and 11 family stays in the last 13 months; one family recommends it "aux familles" [CONFLICT: S1,S2] → **omit from site; ask owner**.
- "No age requirement for check-in." [VERIFIED: S1]
- Pets not allowed. [VERIFIED: S1]
- Payment: Booking house rules "Accepted payment methods: Cash" (card list = "Cash only"). [VERIFIED: S1] One guest: payment at the day's exchange rate (Lars, DE) [PROBABLE: S2]. → "Payment at the hotel in cash (dirhams)" — confirm with owner (do they take cards now? euros?).
- Booking terms (Nov 2026 search): free cancellation until 1 day before arrival, no prepayment, pay at property; prices exclude 20 % VAT and €1 city tax pp/night. [VERIFIED: S1 — for Booking rates only; not a direct-booking policy] → don't publish as hotel policy.
- Prices seen (Booking, 2 nights Nov 10–12 2026): Single €33/night, Superior Single €33, Double twin €38, Double €39, Triple €50 (+VAT/tax). [STALE by nature] → never show; "Ask for today's price".

### Languages
- Booking "Languages spoken": French only. [VERIFIED: S1]
- English spoken at reception (Nuala UK: "They also spoke both English & French"; Google: "The guy at the reception spoke English"). [PROBABLE: S2,S5]
- Arabic/Tamazight/Spanish: [UNVERIFIED] (very likely Arabic, but do not list without owner).

### Location (details + times in notes-neighbourhood.md)
- Talborjt, Agadir's post-1960 town centre; opposite/next to Mosquée Mohamed V (110 m walk). [VERIFIED: S4,S11,S12; S2 reviews]
- Agadir beach promenade (Corniche) ≈1.7 km / ~23 min walk; nearest sand ≈1.9 km / ~25 min. [VERIFIED: S11,S12] (Booking's "19-minute walk" uses the wrong pin [CONFLICT: S1,S12 → S12])
- Jardin d'Olhão ≈720 m / 10 min; Musée Mémoire d'Agadir ≈840 m / 11 min; Vallée des Oiseaux ≈1.5 km / 20 min; Téléphérique (Agadir Oufella cable car) lower station ≈1.7 km / 23 min; Marina entrance ≈2.6 km / 35 min (4 min drive); Souk El Had ≈2.2 km / 30 min (4 min drive); Kasbah Agadir Oufella 6.4 km / ~12 min drive; CTM bus station 3.2 km / ~5 min drive; Supratours 3.7 km / ~5 min drive; Al Massira airport 23.6 km / ~27 min drive (free-flow). [VERIFIED: S11,S12]
- Pharmacy 150 m; supermarkets 370–520 m (Marjane Market, Carrefour Market, Aswak Assalam); banks 200–310 m; post office 200 m; restaurants/cafés from 70 m. [VERIFIED: S11,S12] — individual businesses' current trading [UNVERIFIED].

## (d) Ratings

| Platform | Score | Count | Subscores | Tag |
|---|---|---|---|---|
| **Booking.com** | **8.4 / 10 "Very Good"** | **1,009** reviews | Staff **9.2** · Facilities 8.2 · Cleanliness **8.9** · Comfort 8.6 · Value for money **8.8** · Location **8.9** · Free Wi-Fi **9.5** · (bed comfort 8.5 from 446) · couples rate location 8.8 | [VERIFIED: S1,S2] |
| Google | **4.1 / 5** | **241** reviews | — | [VERIFIED: S4] |
| Priceline | 8.6 / 10 | 238 | — | [VERIFIED: S9] (likely Booking-syndicated) |
| Tripadvisor | 5.0 / 5 | 2 | all 5.0; #70 of 112 hotels in Agadir | [PROBABLE: S8] snippet only — too few to show |
| Expedia / Hotels.com | not found | — | — | — |
Brief's figures (8.5 overall) are slightly off: current overall is **8.4**. Use "8.4 on Booking.com · 1,000+ reviews" and "9.2 for staff".

## (e) People

| Name | Independent reviews (approx.) | Short snippets (exact) | Established | NOT established |
|---|---|---|---|---|
| **Rachid** (also "Rashid") | ~15: Booking 12 (Aug 2025–Apr 2026 mostly) + Google 3 | "Rachid at the reception ws rezlly helpful and nice" — Kaoutar, Morocco (Booking) · "Un remerciement particulier à Rachid à la réception, toujours souriant et très gentil." — Khaoula, Morocco (Booking) | Works at the reception/front desk; consistently named for warmth and help. | Any title (one guest says "le directeur de l'hôtel" — single source), surname, owner status. |
| **Ahmed** (also "Ahmad") | ~16: Booking 13 + Google 3 | "A special thank you to Ahmed for the tea 🍵." — Marnia, United Kingdom (Booking) · "Special props to Ahmad the receptionist." — Ron Weasly (Google) | Works at the reception; named for help, answering questions, late check-out. | Title ("directeur de la réception"/"gérant" each from 1 guest — inconsistent), owner status. |
| **Hicham** | 2 (Booking) | "Rachid, Hicham and Ahmed are great. Always with a smile and offering to assist." — Chafik, United States · "The 3 receptionists - Rachid, Hicham & Ahmed" — Nuala, United Kingdom | Front-desk team member (2 independent). | Enough frequency for a feature — mention only alongside the others, or ask owner. |
| Haseem | 1 (Google) | "Haseem will take care of you." — Paul Gibson | — | Do not use. |
| Housekeeping team (unnamed women) | many | "les femmes de ménage sont elles aussi adorable" — Joël, France | Housekeeping praised. | No names. |
| Owner | 1 review title: "The property owner was a kind and supportive gentl…" — Hashim, UK | — | Owner's name/identity unknown. |
Rule for the site: "Rachid and Ahmed at the front desk" phrased as guest experience is OK; no job titles, no bios. Ask owner before naming anyone.

## (f) Quotable reviews (≤12, exact text, attribution as the platform shows it: first name, country, platform)
1. "Friendly, Central, Clean and Simple Hotel" (review title) — **Ingo, Germany — Booking.com** (Jan 2026) — *theme: brand thesis*
2. "Simple Hotel and very good value for money. Very friendly staff and always very helpful. Daily cleaning exceptional." — **Ingo, Germany — Booking.com** (Jan 2026) — *value, cleaning*
3. "So clean. I had a fantastic stay. The hotels can be a gamble in Morocco, and this one was excellent." — **Kätlin, Estonia — Booking.com** (Mar 2026) — *cleanliness*
4. "Always great to visit the hotel, Rachid, Hicham and Ahmed are great. Always with a smile and offering to assist." — **Chafik, United States — Booking.com** (Apr 2026) — *staff, returning*
5. "Convenient location. Great staff. We are returning guests. First visit was 19 years ago." — **Joanna, United Kingdom — Booking.com** (Dec 2025) — *loyalty*
6. "Smooth and easy check in, all nice staff no matter which time of the day, clean room and room service, clean linen and towels , hot shower and good water pressure." — **Lars, Germany — Booking.com** (Nov 2025) — *practical basics*
7. "On both side of the hotel there are free parking places and few supermarkets." — **Arman, France — Booking.com** (Jul 2025, featured) — *parking*
8. "Near great restaurants and public transportation." — **Grant, United States — Booking.com** (Mar 2026) — *location*
9. "My room has balcony which i can see the kasbah at night which lit up nicely." — **Nabilah, Singapore — Booking.com** (Jan 2026) — *view*
10. "Lovely little hotel , very clean on inside , staff every morning working hard , wifi was good too" — **Mohammed, United Kingdom — Booking.com** (Nov 2025) — *Wi-Fi, housekeeping*
11. "Mais en tournant juste au coin de la rue, vous vous trouverez au paradis des petits déjeuners" — **Audrey, France — Booking.com** (Oct 2025) — *breakfast nearby (FR page)*
12. "Hôtel bien placé, propre et très adapté pour un séjour court avec un très bon rapport qualité prix. […] Très facile de se garer." — **Thomas, France — Booking.com** (Nov 2025) — *FR: value, parking* (if "[…]" elision is unwanted, use first sentence only)
Spare (Google, display as name + "Google"): "Friendly staff that carries your luggage up." — Jesse van Duijne, Google (4/5) · "Tv in room which does actually show English channels including football." — Scott Anderson, Google.
Spelling/punctuation kept exactly as written. Dates are for internal reference only — never on the site.

## (g) Open questions for the owner
1. Which contact should the site use: phone 05 28 84 78 86 (and/or …87)? Is there a **WhatsApp** number (mobile)? Which email is read: agadir.hlynx@gmail.com or agadirhotellynx@gmail.com?
2. **Children**: Booking says "children not allowed" — true, or a Booking setting to fix? From what age?
3. **Payment**: cash only? Dirhams only, or euros too? Cards at the desk?
4. Exact **number of rooms** (affiliates say 41) and floors; which rooms have balconies / views to the Kasbah hill; are there ground-floor rooms (no lift)?
5. Is **Hicham** happy to be named? Are Rachid and Ahmed happy to be named on the site?
6. Room service: what does it include (tea? drinks? none)?
7. Rooftop terrace: open to all guests, any hours?
8. Laundry, luggage storage, airport-taxi booking: offered as standard? (reviews say yes)
9. Late arrivals after 22:00: what should guests do (call ahead)?
10. Star classification: 2★ (Booking/Google) vs "3*" (Telecontact) — confirm official classification.
11. Any photos newer than the Booking set (date unknown; no EXIF — [INFERENCE] Booking photo IDs suggest two upload batches, the bathrooms later)? Permission to use the Booking gallery images (they appear to be the hotel's own professional shoot).
12. Hotel founding/opening year and a sentence of history (business registered 2003)?
