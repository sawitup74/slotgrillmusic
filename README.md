# slotgrillmusic.com
One-page Slot Grill Music player.
- songs/ holds the MP3s (slug + random suffix names); songs.json lists them with a default `listed` flag.
- Live listing state comes from the Apps Script URL in music-config.js; if it is empty or unreachable the page uses songs.json defaults.
- /admin/ manages listing (password checked by the Apps Script, never stored here).
- Streaming buttons: set url + enabled:true in config.json.
- Share links: each listed song has a page at /s/<song-id>/ with Open Graph tags that immediately redirects to /?song=<song-id>. That query loads the player, scrolls to the song, and starts it (or shows Tap to play if the browser blocks autoplay). Paste the /s/<song-id>/ URL in comments or posts so the preview can show the song name. Rebuild those pages with: python3 build-share-pages.py
- The public visit counter adds a display offset of 30,400 to the real Goatcounter total. The stored count is not changed.
