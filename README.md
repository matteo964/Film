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
