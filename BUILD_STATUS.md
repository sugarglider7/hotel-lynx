# BUILD STATUS — hotel-lynx

_Last updated: 2026-10-02 05:35 UTC by ResearchLynx (phase 1 research)_

## Recovered state (resume of crashed run "agadir-batch2")
- Prior run left ONLY raw material (no repo, no status files, no code, no deployment):
  raw page dumps + downloaded images, now in `research/raw/` (gitignored; on disk at /home/agent/agadir-pilot/sites/hotel-lynx/research/raw/). Original copy still at /tmp/sites2/hotel-lynx/.
- Confirmed on 2026-10-02: no GitHub repo, no Cloudflare Pages project, no live hotel-lynx.peashoot.io before this run.

## Research
- **Phase 1 research DONE (2026-10-02).**
- SOURCE_OF_TRUTH.md — done: 15 sources, contact block, facts tagged, ratings, people, 12 quotes, 12 owner questions.
- CONTENT_INVENTORY.md — done: per page/section ✅/🟡/⛔ lines with tags.
- ASSET_INVENTORY.md — done: 27 unique Booking photos (2048 px originals downloaded as `research/raw/images/bk2048_*`), 27 `hr_*` = affiliate duplicates (DO-NOT-USE), Best 12 + gaps.
- research/notes-rooms.md (room table + photo↔room mapping), notes-reviews.md (themes, staff names), notes-neighbourhood.md (pin verification + OSRM table).
- Key facts: 5 room types (Single 15 m² · Superior Single 16 m² · Twin 20 m² · Double 20 m² · Triple 20 m²); **no breakfast** (verified); free public parking; 24 h desk; no lift; Booking 8.4/1,009 (Staff 9.2, Clean 8.9, Value 8.8, Location 8.9, Wi-Fi 9.5); Google 4.1/241.

## Design
- BRAND_NOTES.md — not started

## Pages implemented
- none

## Pages remaining
- all

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
- not started (see QA_CHECKLIST.md)

## Deployment URL
- target: https://hotel-lynx.peashoot.io/ (Cloudflare Pages project "hotel-lynx", output dir `site/`, no build command) — not yet created

## Outstanding problems
- none recorded

## Log
- 05:08 recovery: workspace created from prior raw research; brief + standard written.
- 05:20 research: Booking page + Apollo state parsed (rooms, sizes, beds, policies, trader contact); 377 Booking reviews captured via one browser tab; Google 4.1/241 + 30 reviews; tab closed.
- 05:28 research: pin verified (Google vs Booking), OSRM foot/car table for 37 places; hr_ images identified as pixcdn affiliate copies of Booking photos.
- 05:35 research: SOURCE_OF_TRUTH, CONTENT_INVENTORY, ASSET_INVENTORY, notes-* written; committed + pushed.
