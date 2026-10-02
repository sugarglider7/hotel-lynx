# Neighbourhood notes — "Your Agadir from Lynx"

_Checked 2026-10-02. Raw data: `research/raw/_osrm.json`, `_osrm.py`, `_ovp_*.json` (gitignored)._

## 1. Where the hotel actually is (pin verification)

| Source | Coordinates | Verdict |
|---|---|---|
| Google Maps place "Hotel Lynx" (S4), plus code `CCF5+48 Agadir` | **30.4228588, -9.5917027** | **USE.** Sits ~15 m from OSM way 330793179 "Rue El Mahdi Ibn Toumert" (S11), near its south-east end (low house numbers → No. 9 fits). Mosquée Mohamed V is 110 m away, matching many reviews ("directly opposite biggest mosque in Agadir", "obok meczetu Mohammeda V"). Google's own "Sindibad Hotel 0.1 mi away" also fits. |
| Booking.com (S1) `b_map_center` | 30.427755, -9.598107 | **DO NOT USE.** 821 m from the Google pin and not on Rue Ibn Toumert. It coincides with the OSM node for the *district* "Cité Suisse / Swiss City" (30.42780, -9.59767) → Booking geocoded the district, not the building. Booking's "19-minute walk to Agadir Beach" and its "What's nearby" distances are computed from this wrong pin. |

Street-name spellings in use: Rue Al Mahdi Ibn Toumart (Google, Booking) · Rue El Mahdi Ibn Toumert (OSM) · Rue Mehdi Ben Toumert (Booking trader record) · rue Ibn Toumert (Telecontact). Same street.

Do NOT confuse with "Lynx" / "Lynx Optique" — an optician on Boulevard Mohammed Cheikh Saâdi (OSM node 5525171015, Instagram @lynxoptiqueagadir). Unrelated business.

## 2. Method
- Origin: Google pin 30.4228588, -9.5917027.
- Destinations: OpenStreetMap features via Overpass (snapshot 2026-10-02T04:25Z) and Nominatim; museum location from its published plus code.
- Routing: OSRM public servers `https://routing.openstreetmap.de/routed-foot/...` (walk) and `.../routed-car/...` (drive), `overview=false`, ≥1.2 s between requests. Walking speed implied ≈ 4.5 km/h. Drive times are free-flow (no traffic, no parking) — treat as minimums.
- Rounding for the site: walks → nearest minute, say "about"; drives → "about N min by taxi, traffic permitting".
- Open/closed status of shops and restaurants is NOT verified by this method (OSM presence only). Publish categories ("pharmacy 150 m", "three supermarkets within 550 m") rather than individual café names unless the owner confirms them.

## 3. Table (from the hotel door)

| Place | Category | Coordinates | Source | Walk (OSRM) | Drive (OSRM) |
|---|---|---|---|---|---|
| Mosquée Mohamed V | landmark | 30.42215, -9.59252 | OSM way 362486472 | 110 m / 1 min | 110 m / 1 min |
| Talborjt (district node) | landmark | 30.42373, -9.59057 | OSM node 3855001058 | 234 m / 3 min | 242 m / 1 min |
| Pharmacie Talberjt | pharmacy | 30.42387, -9.59270 | OSM | 146 m / 2 min | 146 m / 1 min |
| Pharmacie Du Soleil | pharmacy | 30.42136, -9.59276 | OSM | 311 m / 4 min | 325 m / 1 min |
| Marjane Market | supermarket | 30.42102, -9.59416 | OSM | 370 m / 5 min | 370 m / 1 min |
| Carrefour Market (Label'Vie) | supermarket | 30.42598, -9.59250 | OSM | 488 m / 6 min | 488 m / 1 min |
| Aswak Assalam | supermarket | 30.42632, -9.59243 | OSM | 524 m / 7 min | 549 m / 2 min |
| Al Barid Bank | bank | 30.42394, -9.59101 | OSM | 196 m / 3 min | 196 m / 1 min |
| Attijariwafa bank | bank | 30.42166, -9.59350 | OSM | 287 m / 4 min | 287 m / 1 min |
| Bank of Africa | bank | 30.42272, -9.59404 | OSM | 308 m / 4 min | 418 m / 1 min |
| Amana / Poste Talborjt | post | 30.42377, -9.59110 | OSM | 204 m / 3 min | 204 m / 1 min |
| Sweet Hamid | restaurant | 30.42319, -9.59229 | OSM | 70 m / 1 min | 70 m / 1 min |
| Etoile d'Agadir | restaurant | 30.42440, -9.59328 | OSM | 240 m / 3 min | 227 m / 1 min |
| Café Restaurant Ibtissam | restaurant | 30.42448, -9.59319 | OSM | 252 m / 3 min | 226 m / 1 min |
| Rôtisserie Marché | restaurant | 30.42442, -9.59348 | OSM | 243 m / 3 min | 243 m / 1 min |
| Yacout | restaurant | 30.42090, -9.59478 | OSM | 445 m / 6 min | 445 m / 1 min |
| Café Santiago | cafe | 30.42444, -9.59199 | OSM | 255 m / 3 min | 255 m / 1 min |
| Café Holanda | cafe | 30.42452, -9.59209 | OSM | 296 m / 4 min | 296 m / 1 min |
| Crèmerie du Sud | cafe | 30.42432, -9.59337 | OSM | 227 m / 3 min | 227 m / 1 min |
| Caramel | cafe | 30.42602, -9.59190 | OSM | 498 m / 7 min | 952 m / 2 min |
| Venezia Ice | ice cream | 30.42588, -9.59181 | OSM | 484 m / 6 min | 966 m / 2 min |
| Jardin Ibn Zaïdoun | park | 30.41918, -9.59275 | OSM | 540 m / 7 min | 710 m / 2 min |
| Jardin d'Olhão | park | 30.42468, -9.59707 | OSM way (centroid) | 717 m / 10 min | 687 m / 1 min |
| Musée Mémoire d'Agadir (in Jardin d'Olhão) | museum | 30.42479, -9.59842 | plus code CCF2+WJ8 (GetYourGuide, S13) | 838 m / 11 min | 831 m / 2 min |
| Musée du Patrimoine Amazigh | museum | 30.41604, -9.59713 | OSM way 709500538 | 1.1 km / 15 min | 1.1 km / 3 min |
| Marché Municipal (central market) | market | 30.42175, -9.60017 | OSM | 1.2 km / 16 min | 1.2 km / 3 min |
| Vallée des Oiseaux | park/zoo | 30.41963, -9.60213 | OSM way (centroid) | 1.5 km / 20 min | 2.7 km / 5 min |
| Agadir Corniche (nearest promenade point) | beach | 30.41783, -9.60383 | OSM relation 5393745, nearest node | 1.7 km / 23 min | 2.6 km / 4 min |
| Agadir Beach (nearest sand) | beach | 30.41686, -9.60555 | OSM way 386830407, nearest node | 1.9 km / 25 min | 2.6 km / 5 min |
| Téléphérique Agadir Oufella (lower station) | attraction | 30.42599, -9.60595 | OSM node 9863443589 | 1.7 km / 23 min | 1.7 km / 4 min |
| Marina d'Agadir (entrance, Avenue Mohammed V) | attraction | 30.42490, -9.61285 | OSM bus stop "Marina" | 2.6 km / 35 min | 2.6 km / 4 min |
| Kasbah Agadir Oufella | attraction | 30.42974, -9.62476 | OSM node | not a walk (13.5 km route, hill road) | 6.4 km / 12 min |
| Souk El Had | market | 30.41278, -9.57959 | OSM way (centroid) | 2.2 km / 30 min | 2.2 km / 4 min |
| CTM bus station (Gare routière) | transport | 30.41602, -9.56571 | OSM node "CTM bus station" | 3.1 km / 42 min | 3.2 km / 5 min |
| Supratours bus station | transport | 30.42032, -9.56044 | OSM node 909316179 (Av. Abderrahim Bouabid) | 3.6 km / 48 min | 3.7 km / 5 min |
| Agadir–Al Massira Airport (AGA) | transport | 30.32840, -9.40912 | OSM way 93357864 | not a walk | 23.6 km / 27 min |
| Taghazout (village centre, approx.) | day trip | 30.5446, -9.7089 | approximate point | not a walk | 23.8 km / 24 min |

Marina note: first attempt routed to a point inside the marina basin and OSRM-foot snapped to an unreachable pier (19 km nonsense) — replaced by the entrance on Avenue Mohammed V. A point inside the marina promenade (30.4232, -9.6155) gives 3.1 km / 41 min on foot.

## 4. What reviewers say about the area (Booking S2, Google S5) — supports tone, not numbers
- Restaurants, cafés, grills and "petits restaurants typiques" all around; local prices (many reviews, FR/EN/DE/PL).
- Breakfast spots nearby: "Frühstück ab 7.30 Uhr in der Nachbarschaft möglich" (Kirsten, Germany); "schuin tegenover de bakker met uitstekend ontbijt" (M, Netherlands); "une pâtisserie/boulangerie juste à côté" (Véronique, France); "en tournant juste au coin de la rue, vous vous trouverez au paradis des petits déjeuners" (Audrey, France).
- Square in front of the hotel ("Beautiful Square on front of the hotel. Street next to the hotel full of restaurants!" — Maria, Poland).
- Beach: guests quote 15–30 min on foot; OSRM gives 23 min to the promenade, 25 min to the sand. Use OSRM.
- Petit taxis easy to find ("petit taxi everywhere" — Nabilah, Singapore). OSM has no mapped taxi rank near the hotel (nearest mapped ranks are around Souk El Had, ~2 km) → do not name a rank; say "petits taxis pass constantly; reception can call one".
- Reception has organised airport taxis (Norbert, Austria; Gabrielė, Lithuania; Kirsten, Germany; Anastazja, Poland). Prices quoted in reviews (200–250 MAD) are NOT to be published.
- The cable car is walkable ("à proximité du téléphérique" — Franz, France).
- Noise side of the location: call to prayer from the mosque (early morning, Ramadan nights), street traffic/motorbikes, parking side of the building. Do not promise silence.

## 5. Items NOT verified / do not publish as fact
- Opening hours of any café/restaurant/shop (OSM hours exist for a few but are unverified).
- Cash machines: banks are mapped, ATMs are not individually confirmed → say "banks within 300 m".
- Musée Mémoire d'Agadir hours (Tue–Sun 9:30–12:30 / 14:30–18:30 per GetYourGuide/immersi-travel) and Téléphérique hours/prices → link out or "check times locally".
- "Airport Shuttle Bus (50 MAD)" stop in OSM (30.41992, -9.60251) — unverified, do not publish.
