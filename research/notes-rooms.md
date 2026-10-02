# Room inventory notes — Hôtel Lynx

_Source: Booking.com property page (S1), Apollo state `RoomData` / `RoomDetails` / `RoomTranslation` objects in `research/raw/_bk.html`, fetched 2026-10-02 (search dates 10–12 Nov 2026, all five types available). Raw dump of each object reviewed; nothing below is inferred unless marked._

## Inventory table

| # | Booking name | Room id | Beds (en-gb wording; en-us shows "twin"/"queen") | Max persons | Size | Bathroom | AC | TV | Wi-Fi | Other listed | Smoking | Access |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Single Room | 926402401 | 1 single bed | 1 | **15 m²** (161 ft²) | private: shower, toilet, towels, toilet paper | yes | flat-screen, satellite + cable | free Wi-Fi (property-wide, S1/S4) | wake-up service, alarm clock | non-smoking | upper floors by stairs only |
| 2 | Superior Single Room | 926402402 | 1 single bed **or** 1 large double bed ("Select your bed (if available)") | 1 | **16 m²** (172 ft²) | same | yes | same | same | same | non-smoking | same |
| 3 | Double Room (twin) | 926402403 | 2 single beds | 2 | **20 m²** (215 ft²) | same | yes | same | same | same | non-smoking | same |
| 4 | Double Room | 926402404 | 1 large double bed | 2 | **20 m²** (215 ft²) | same | yes | same | same | same | non-smoking | same |
| 5 | Triple Room | 926402405 | 1 single bed + 1 large double bed | 3 | **20 m²** (215 ft²) | same | yes | same | same | same | non-smoking | same |

- No children / cribs / extra beds on any type (`maxChildren: 0`, `allowChildren: false`) — see CONFLICT in SOURCE_OF_TRUTH.
- `bathroomCount: 0` in the RDS data is Booking's apartment-room field (not applicable to hotel rooms); the `private_bathroom` facility and `isPrivateBathroomInAllRooms: true` confirm en-suite bathrooms.
- `roomFloor: []` → floors not stated. Property `highFloorStartsAt: 3`.
- NOT listed for any room: desk, wardrobe, safe, minibar, fridge, kettle, hairdryer, balcony, view, soundproofing, toiletries, heating. Photos show wooden wardrobes, a small table + chairs, wall-mounted TV, split AC units and (some rooms) balcony doors → describe only what is visible in the specific photo, never as a guaranteed feature.
- Bathroom type from photos: walk-in shower with tiled tray, no cabin or curtain, wall basin with mirror, WC (bk_03/07/26/27). Reviews confirm "open shower" and water on the floor.
- Reviewers' room sizes: "big room", "spacious", "chambres grandes", "Room was huge" (Google) vs one "not quite enough room to open the wardrobes" (Double, Sept 2026).

## Photo → room-type mapping (Booking's own assignment in `RoomData.roomPhotos`)

| Photo (file) | Booking id | Shows | Assigned by Booking to |
|---|---|---|---|
| bk_22 | 418854475 | two single beds, TV, desk-table | Single (1), Double twin (3) |
| bk_02, bk_06, bk_19 | 418854476 / 418854452 / 418854446 | one large double bed, wardrobe, balcony door (bk_02 balcony visible) | Superior Single (2), Double (4) |
| bk_25, bk_23, bk_21, bk_24, bk_20, bk_18 | 418854451 / 462 / 470 / 469 / 467 / 439 | double + single bed (triple set-up), table and chairs, wardrobe, wall TV, AC | Triple (5) |
| bk_03, bk_07, bk_26, bk_27 | 494137613 / 632 / 618 / 630 | shower room (walk-in shower, basin, WC) | Single, Superior Single, Double twin (1–3); not attached to 4/5 by Booking but same design |
| bk_04, bk_17, bk_09, bk_05, bk_11, bk_13, bk_10 | balcony/terrace, view, façade, lobby, salon | attached to every room type as generic property shots |

**There is no photo of a single-bed Single Room.** The Single (1) is illustrated by Booking only with the twin room bk_22 + shared shots. If the site shows a Single, use bathroom/common shots or label the image honestly ("twin room") — ask the owner for a Single-room photo.

## Recommended public naming (site)
Single · Superior Single · Twin · Double · Triple — with "Twin" for Booking's "Double Room – 2 single beds" (clearer; Booking itself sells it as Double Room). Owner to confirm naming.
