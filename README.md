# TikTok Stickman-Serie

- `STIL-ANALYSE.md` – Analyse der Referenzvideos (Aufbau, Story-Formel, Visualisierung)
- `engine/` – Render-Engine (pycairo-Strichmännchen, Hintergründe, Lippensync, Kamera, Hook-Kasten)
- `episodes/` – Skripte der Folgen
- `output/` – fertige Videos (1080x1920, 30 fps)

Rendern:
```
pip install pycairo edge-tts numpy
python3 engine/render.py episodes/hausmeister_teil1.py            # komplett
python3 engine/render.py episodes/hausmeister_teil1.py --preview 10 # 10-s-Vorschau
```
