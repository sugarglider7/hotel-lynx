#!/usr/bin/env python3
"""Declarative image pipeline for hotel-lynx (Pillow, strictly sequential).

    python3 tools/images.py            # build every entry in IMAGES (skips up-to-date outputs)
    python3 tools/images.py --force    # rebuild everything

Reads originals from research/raw/images/ (gitignored, on disk), writes
site/assets/img/<name>-<w>.webp plus tools/images.manifest.json, which
tools/build.py reads for width/height, srcset and the dominant colour that
sits behind every <img> while it loads.

Each entry:
  name   output stem
  src    original file in research/raw/images/
  crop   (left, top, right, bottom) as fractions of the original, or None
  widths output widths in px (largest first; never upscaled)
  q      WebP quality
  alt_crop optional {"suffix", "crop", "widths"} for an art-directed mobile crop
"""
import json, os, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "research", "raw", "images")
OUT = os.path.join(ROOT, "site", "assets", "img")
MANIFEST = os.path.join(ROOT, "tools", "images.manifest.json")
MAX_BYTES = 450 * 1024

IMAGES = [
    # Hero: the façade with the HOTEL LYNX fascia and blade sign (bk_01). The desktop crop is the
    # band from just above the blade sign (src y≈0.08) to just under the fascia sign, where the
    # black ground floor starts (y≈0.73) — neither sign is ever cut, and the photo hands over to
    # the black band right under the sign. The CSS shows this crop at its natural ratio.
    {"name": "facade", "src": "bk2048_01_418854421.jpg", "crop": (0.0, 0.065, 1.0, 0.745),
     "widths": [2000, 1200], "q": 74,
     "alt_crop": {"suffix": "m", "crop": (0.22, 0.04, 1.0, 1.0), "widths": [1200, 800]}},
    # Blue hour over the public car park opposite (bk_05).
    {"name": "facade-night", "src": "bk2048_05_418854455.jpg", "crop": (0.0, 0.0, 1.0, 1.0),
     "widths": [1400, 760], "q": 72},
    # Rooftop terrace, minaret of Mohammed V and the Oufella hill (bk_10).
    {"name": "terrace", "src": "bk2048_10_418854453.jpg", "crop": (0.0, 0.0, 1.0, 1.0),
     "widths": [1800, 900], "q": 72},
    # Rooms (the four on the homepage directory also get a 320 px thumb).
    {"name": "room-twin", "src": "bk2048_22_418854475.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600, 320], "q": 74},
    {"name": "room-double", "src": "bk2048_02_418854476.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600, 320], "q": 74},
    {"name": "room-double-b", "src": "bk2048_06_418854452.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600, 320], "q": 74},
    {"name": "room-triple", "src": "bk2048_21_418854470.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600, 320], "q": 74},
    # Reception + tiled stairs (bk_12).
    {"name": "reception", "src": "bk2048_12_418854477.jpg", "crop": (0.0, 0.1, 1.0, 1.0),
     "widths": [1000, 600], "q": 72},
    # Rooms page galleries (Booking's own room assignment, research/notes-rooms.md).
    {"name": "room-double-c", "src": "bk2048_19_418854446.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600], "q": 74},
    {"name": "room-triple-b", "src": "bk2048_25_418854451.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600], "q": 74},
    {"name": "room-triple-c", "src": "bk2048_18_418854439.jpg", "crop": (0.0, 0.08, 1.0, 1.0),
     "widths": [1000, 600], "q": 74},
    # Shower room with basin + WC (bk_03) — "in every room" figure.
    {"name": "shower-wc", "src": "bk2048_03_494137613.jpg", "crop": (0.0, 0.0, 1.0, 1.0),
     "widths": [1000, 600], "q": 72},
    # Tiled staircase, portrait (bk_14) — "stairs, no lift".
    {"name": "stairs", "src": "bk2048_14_418854478.jpg", "crop": (0.0, 0.12, 1.0, 0.88),
     "widths": [800, 480], "q": 72},
    # View through a balcony rail to the Kasbah hill (bk_09) — Your Agadir page head.
    {"name": "view", "src": "bk2048_09_418854413.jpg", "crop": (0.0, 0.05, 1.0, 1.0),
     "widths": [1400, 800], "q": 72},
]

OG = {"name": "og-facade", "src": "bk2048_01_418854421.jpg", "size": (1200, 630), "focus_y": 0.55}


def crop_frac(im, box):
    if not box:
        return im
    W, H = im.size
    return im.crop((round(box[0] * W), round(box[1] * H), round(box[2] * W), round(box[3] * H)))


def dominant(im):
    small = im.copy()
    small.thumbnail((64, 64))
    pal = small.quantize(4)
    count, idx = max(pal.getcolors())
    r, g, b = pal.getpalette()[idx * 3: idx * 3 + 3]
    return "#%02x%02x%02x" % (r, g, b)


def save_widths(im, stem, widths, q, force):
    out = []
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        fn = f"{stem}-{w}.webp"
        path = os.path.join(OUT, fn)
        if force or not os.path.exists(path):
            im.resize((w, h), Image.LANCZOS).save(path, "WEBP", quality=q, method=6)
        size = os.path.getsize(path)
        if size > MAX_BYTES:
            sys.exit(f"{fn} is {size // 1024} KB > 450 KB — lower q or width")
        out.append({"file": fn, "w": w, "h": h, "kb": round(size / 1024)})
    return out


def main():
    force = "--force" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    manifest = {}
    for spec in IMAGES:  # one image in memory at a time
        with Image.open(os.path.join(RAW, spec["src"])) as src:
            src.draft("RGB", (2400, 2400))
            im = ImageOps.exif_transpose(src).convert("RGB")
        base = crop_frac(im, spec["crop"])
        entry = {"src": spec["src"], "color": dominant(base),
                 "variants": save_widths(base, spec["name"], spec["widths"], spec["q"], force)}
        alt = spec.get("alt_crop")
        if alt:
            alt_im = crop_frac(im, alt["crop"])
            entry["mobile"] = save_widths(alt_im, f'{spec["name"]}-{alt["suffix"]}', alt["widths"], spec["q"], force)
        manifest[spec["name"]] = entry
        print(spec["name"], entry["color"], [(v["w"], v["kb"]) for v in entry["variants"] + entry.get("mobile", [])])
        del im, base

    # Open Graph card 1200x630 (JPEG for the widest crawler support).
    with Image.open(os.path.join(RAW, OG["src"])) as src:
        im = src.convert("RGB")
    tw, th = OG["size"]
    im = ImageOps.fit(im, (tw, th), Image.LANCZOS, centering=(0.5, OG["focus_y"]))
    og_path = os.path.join(OUT, OG["name"] + ".jpg")
    im.save(og_path, "JPEG", quality=80, optimize=True, progressive=True)
    manifest[OG["name"]] = {"file": OG["name"] + ".jpg", "w": tw, "h": th}
    print("og", round(os.path.getsize(og_path) / 1024), "KB")

    with open(MANIFEST, "w") as f:
        json.dump(manifest, f, indent=1)
    make_favicons()


def make_favicons():
    """PNG fallbacks of site/favicon.svg (black chamfered plate, white L, orange eye)."""
    from PIL import ImageDraw
    for size, fn in ((180, "apple-touch-icon.png"), (32, "favicon-32.png")):
        s = size * 4 / 64  # draw at 4x, downsample for clean edges
        im = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
        dr = ImageDraw.Draw(im)
        pts = lambda ps: [(x * s, y * s) for x, y in ps]
        # iOS rounds its own corners, so the touch icon is a full square
        plate = [(0, 0), (64, 0), (64, 64), (0, 64)] if size == 180 else [(0, 0), (50, 0), (64, 14), (64, 64), (0, 64)]
        dr.polygon(pts(plate), fill="#15110f")
        dr.polygon(pts([(16, 14), (25, 14), (25, 41), (44, 41), (44, 50), (16, 50)]), fill="#fffdfc")
        dr.polygon(pts([(35, 25), (44, 20), (53, 25), (44, 30)]), fill="#d4652f")
        im.resize((size, size), Image.LANCZOS).save(os.path.join(ROOT, "site", fn))
        print("favicon", fn)


if __name__ == "__main__":
    main()
