# TikTok Stickman-Serie

- `STIL-ANALYSE.md` – Analyse der Referenzvideos (Aufbau, Story-Formel, Visualisierung)
- `engine/` – Render-Engine (pycairo-Strichmännchen, Hintergründe, Lippensync, Kamera, Hook-Kasten)
- `episodes/` – Skripte der Folgen
- `output/` – fertige Videos (1080x1920, 30 fps)

Rendern:
```
pip install pycairo edge-tts numpy
python3 engine/render.py episodes/owner/part1.py   # -> output/owner_part1.mp4
python3 engine/render.py episodes/owner/part2.py --preview 10  # 10-s-Vorschau
```
- `archive/` – erste deutsche Testversion (Hausmeister)

## Stimmen
Mit `el_voice` in `CHARS` werden die Stimmen über ElevenLabs (Modell `eleven_v3`) erzeugt.
Jede Zeile bekommt automatisch einen Emotions-Tag passend zur Emotion der Figur (z. B. `[sarcastically]`),
mit `say=` lässt sich der gesprochene Text inkl. eigener Tags/Betonung überschreiben.
Jede Zeile wird per Spracherkennung geprüft und bei Abweichungen mit anderem Seed neu erzeugt.
Der API-Schlüssel wird in dieser Cloud-Umgebung automatisch eingesetzt; lokal `ELEVENLABS_API_KEY` setzen.
Ohne `el_voice` wird Edge-TTS (kostenlos) verwendet.
