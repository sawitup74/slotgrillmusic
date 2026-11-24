#!/usr/bin/env python3
"""Generate static /s/<song-id>/index.html pages for link-preview tags."""
from __future__ import annotations

import json
import shutil
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SONGS = json.loads((ROOT / "songs.json").read_text(encoding="utf-8"))
OUT = ROOT / "s"
ORIGIN = "https://slotgrillmusic.com"


def page(song: dict) -> str:
    title = song["title"]
    sid = song["id"]
    play = f"{ORIGIN}/?song={sid}"
    rel = f"/?song={sid}"
    share = f"{ORIGIN}/s/{sid}/"
    og_title = f"{title} · Slot Grill Music"
    desc = f'Listen to "{title}" by Slot Grill Music. Play it here, then browse the rest of the songs.'
    et, ed, eo, er = escape(og_title), escape(desc), escape(play), escape(rel)
    es = escape(share)
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(og_title)}</title>
<meta name="description" content="{ed}">
<meta property="og:type" content="music.song">
<meta property="og:site_name" content="Slot Grill Music">
<meta property="og:title" content="{et}">
<meta property="og:description" content="{ed}">
<meta property="og:url" content="{es}">
<meta property="og:image" content="{ORIGIN}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{et}">
<meta name="twitter:description" content="{ed}">
<meta name="twitter:image" content="{ORIGIN}/og.jpg">
<link rel="canonical" href="{eo}">
<link rel="icon" href="../../favicon.ico" sizes="any">
<meta http-equiv="refresh" content="0;url={er}">
<script>location.replace({rel!r});</script>
</head>
<body style="margin:0;font:16px/1.5 system-ui,sans-serif;background:#0b0705;color:#fff4ea;padding:40px 20px;text-align:center">
<p>Opening <a href="{er}" style="color:#ffd23f">{escape(title)}</a> on Slot Grill Music…</p>
</body></html>
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    written = 0
    skipped = 0
    for song in SONGS.get("songs", []):
        if song.get("listed") is False:
            skipped += 1
            continue
        dest = OUT / song["id"]
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text(page(song), encoding="utf-8")
        written += 1
    print(f"wrote {written} share pages, skipped {skipped} unlisted")


if __name__ == "__main__":
    main()
