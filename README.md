# slotgrillmusic.com
One-page Slot Grill Music player.
- songs/ holds the MP3s (slug + random suffix names); songs.json lists them with a default `listed` flag.
- Live listing state comes from the Apps Script URL in music-config.js; if it is empty or unreachable the page uses songs.json defaults.
- /admin/ manages listing (password checked by the Apps Script, never stored here).
- Streaming buttons: set url + enabled:true in config.json.
