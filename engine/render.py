"""Rendert eine Episode (Skript-Modul) zu einem MP4.

Aufruf: python3 engine/render.py episodes/<datei>.py [--preview SEK] [--start SEK]
"""
import asyncio
import hashlib
import importlib.util
import math
import os
import random
import ssl
import subprocess
import sys

import cairo
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import backgrounds as bgm  # noqa: E402
render = sys.modules[__name__]
from stickman import POSES, draw_figure, rrect  # noqa: E402

W, H, FPS, SR = 1080, 1920, 30, 24000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "build", "tts")
os.makedirs(CACHE, exist_ok=True)


# ------------------------------------------------------------------ TTS
async def _tts(text, voice, rate, pitch, path):
    import edge_tts
    import edge_tts.communicate as c
    ca = os.environ.get("CCR_CA", "/root/.ccr/ca-bundle.crt")
    if os.path.exists(ca):
        c._SSL_CTX = ssl.create_default_context(cafile=ca)
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(path)


def tts(text, voice, rate="+0%", pitch="+0Hz"):
    key = hashlib.md5(f"{voice}|{rate}|{pitch}|{text}".encode()).hexdigest()
    mp3 = os.path.join(CACHE, key + ".mp3")
    if not os.path.exists(mp3) or os.path.getsize(mp3) == 0:
        for attempt in range(4):
            try:
                asyncio.run(_tts(text, voice, rate, pitch, mp3))
                break
            except Exception as ex:  # Netzwerk-Wackler
                print("TTS retry", attempt, ex)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.float32).copy()
    # Stille an den Rändern kürzen
    idx = np.where(np.abs(a) > 0.01)[0]
    if len(idx):
        a = a[max(0, idx[0] - int(0.03 * SR)): idx[-1] + int(0.08 * SR)]
    return a


# ------------------------------------------------------------------ ElevenLabs
EMO_TAG = {"angry": "[angry]", "smug": "[sarcastically]", "shocked": "[shocked]", "worried": "[nervously]",
           "happy": "[cheerfully]", "annoyed": "[annoyed]", "sad": "[sadly]", "confused": "[confused]",
           "calm": "[calmly]"}
_WHISPER = None


_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen " \
        "seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def _num_words(n):
    if n < 20:
        return _ONES[n]
    if n < 100:
        return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        return _ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + _num_words(n % 100))
    if n < 1000000:
        return _num_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + _num_words(n % 1000))
    return str(n)


def _norm_words(t):
    import re
    t = re.sub(r"\[[^\]]*\]", " ", t.lower())
    t = re.sub(r"(?<=\d),(?=\d)", "", t)
    t = re.sub(r"\d+", lambda m: " " + _num_words(int(m.group())) + " ", t)
    t = t.replace("-", " ")
    words = re.findall(r"[a-z']+", t)
    return [w for w in words if w not in ("ha", "haha", "hahaha", "and", "a", "uh", "um")]


def _check(a, text):
    """Spracherkennung: Ähnlichkeit 0..1 zwischen gesprochenem und Soll-Text."""
    global _WHISPER
    import difflib
    from faster_whisper import WhisperModel
    if _WHISPER is None:
        _WHISPER = WhisperModel("small", device="cpu", compute_type="int8")
    y = np.interp(np.arange(0, len(a), SR / 16000), np.arange(len(a)), a).astype(np.float32)
    heard = " ".join(seg.text for seg in _WHISPER.transcribe(y, language="en")[0])
    return difflib.SequenceMatcher(None, _norm_words(heard), _norm_words(text)).ratio(), heard


def _decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def eleven(text, voice_id, model="eleven_v3", stability=0.5, seed=1):
    import json
    import urllib.request
    key = hashlib.md5(f"el|{voice_id}|{model}|{stability}|{seed}|{text}".encode()).hexdigest()
    mp3 = os.path.join(CACHE, "el_" + key + ".mp3")
    if not os.path.exists(mp3) or os.path.getsize(mp3) == 0:
        body = {"text": text, "model_id": model, "seed": seed,
                "voice_settings": {"stability": stability, "similarity_boost": 0.8}}
        if model != "eleven_v3":
            body["voice_settings"].update(style=0.45, use_speaker_boost=True)
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128",
            data=json.dumps(body).encode(),
            headers={"xi-api-key": os.environ.get("ELEVENLABS_API_KEY", "proxy-injected"),
                     "Content-Type": "application/json"})
        for attempt in range(4):
            try:
                data = urllib.request.urlopen(req, timeout=180).read()
                open(mp3, "wb").write(data)
                break
            except urllib.error.HTTPError as ex:
                msg = ex.read()[:300]
                print("ElevenLabs Fehler", ex.code, msg)
                if ex.code in (401, 402, 403, 422):
                    raise SystemExit(f"ElevenLabs: {ex.code} {msg}")
            except Exception as ex:
                print("ElevenLabs retry", attempt, ex)
    return _decode(mp3)


def trim_norm(a):
    idx = np.where(np.abs(a) > 0.012)[0]
    if len(idx):
        a = a[max(0, idx[0] - int(0.03 * SR)): idx[-1] + int(0.08 * SR)]
    rms = np.sqrt(np.mean(a ** 2)) + 1e-9
    a = a * (0.09 / rms)
    pk = np.max(np.abs(a))
    if pk > 0.95:
        a = a * (0.95 / pk)
    return a


def voice_line(c, text, emotion):
    """Erzeugt eine Sprachzeile; ElevenLabs (mit Emotions-Tag + Prüfung) oder Edge-TTS."""
    if "el_voice" not in c:
        return tts(text, c["voice"], c.get("rate", "+0%"), c.get("pitch", "+0Hz"))
    tagged = text if text.lstrip().startswith("[") else (EMO_TAG.get(emotion, "") + " " + text).strip()
    best = None
    for seed in (1, 2):
        a = trim_norm(eleven(tagged, c["el_voice"], c.get("el_model", "eleven_v3"), c.get("stability", 0.5), seed))
        score, heard = _check(a, text)
        if best is None or score > best[0]:
            best = (score, a, heard)
        has_num = any(w in _norm_words(text) for w in ("one", "two", "three", "four", "five", "six", "seven", "eight",
                                                         "nine", "ten", "forty", "ninety", "hundred", "thousand"))
        if score >= (0.5 if has_num else 0.75) or os.environ.get("EL_OFFLINE"):
            break
        print(f"  Prüfung {score:.2f} (seed {seed}): '{heard.strip()}' statt '{text}'")
    return best[1]


def phone_fx(a):
    """Telefon-Klang: Bandpass 300–3400 Hz, leichte Sättigung."""
    f = np.fft.rfft(a)
    fr = np.fft.rfftfreq(len(a), 1 / SR)
    f[(fr < 320) | (fr > 3400)] = 0
    b = np.fft.irfft(f, len(a)).astype(np.float32)
    b = np.tanh(b * 2.2) / 2.2
    return trim_norm(b) * 0.9


def envelope(a):
    hop = SR // FPS
    n = int(math.ceil(len(a) / hop))
    env = np.array([np.sqrt(np.mean(a[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n)])
    ref = np.percentile(env, 90) + 1e-6
    m = np.clip((env / ref - 0.18) * 1.35, 0, 1)
    # leichtes Glätten, dann in Cartoon-Stufen quantisieren
    m = np.convolve(m, [0.25, 0.5, 0.25], mode="same")
    return np.round(m * 3) / 3


# ------------------------------------------------------------------ SFX
def sfx(name):
    t = np.arange(int(SR * 2.0)) / SR
    rng = np.random.default_rng(1)
    if name == "hiss":
        n = rng.standard_normal(len(t)).astype(np.float32)
        n = np.convolve(n, np.ones(6) / 6, mode="same")
        return (n * 0.12 * np.minimum(1, t * 4) * np.exp(-t * 1.2)).astype(np.float32)
    if name == "clunk":
        s = np.sin(2 * np.pi * 70 * t) * np.exp(-t * 9) + 0.4 * rng.standard_normal(len(t)) * np.exp(-t * 30)
        return (s * 0.5).astype(np.float32)
    if name == "alarm":
        out = np.zeros(int(SR * 2.4), np.float32)
        for k in range(4):
            st = int(k * 0.55 * SR)
            tt = np.arange(int(0.5 * SR)) / SR
            b = (np.sin(2 * np.pi * 988 * tt) + 0.5 * np.sin(2 * np.pi * 1976 * tt)) * np.exp(-tt * 7) * 0.18
            out[st:st + len(b)] += b.astype(np.float32)
        return out
    if name == "ding":
        b = (np.sin(2 * np.pi * 1318 * t) + 0.4 * np.sin(2 * np.pi * 2636 * t)) * np.exp(-t * 4) * 0.15
        return b.astype(np.float32)
    if name == "whoosh":
        n = rng.standard_normal(int(SR * 0.5)).astype(np.float32)
        n = np.convolve(n, np.ones(20) / 20, mode="same")
        tt = np.arange(len(n)) / SR
        return (n * np.sin(np.pi * tt / 0.5) * 0.25).astype(np.float32)
    return np.zeros(1, np.float32)


# ------------------------------------------------------------------ Timeline
def build(ep):
    events = []
    t = 0.4
    shot = None
    emo = {}
    for item in ep.SCRIPT:
        emo.update(item.get("e", {}))
        if item.get("shot"):
            shot = item["shot"]
        if "beat" in item:
            events.append(dict(kind="beat", shot=shot, start=t, end=t + item["beat"], item=item))
            t += item["beat"]
            continue
        if "t" not in item:
            continue
        c = ep.CHARS[item["s"]]
        a = voice_line(c, item.get("say", item["t"]), item.get("tone", emo.get(item["s"], "neutral")))
        if item.get("fx") == "phone":
            a = phone_fx(a)
        dur = len(a) / SR
        events.append(dict(kind="line", shot=shot, start=t, end=t + dur, audio=a, env=envelope(a), item=item))
        t += dur + item.get("gap", ep.GAP)
    total = t + 0.6
    audio = np.zeros(int(total * SR) + SR, np.float32)
    for ev in events:
        if ev["kind"] == "line":
            s = int(ev["start"] * SR)
            audio[s:s + len(ev["audio"])] += ev["audio"]
        for name, off in ev["item"].get("sfx", []):
            s = int((ev["start"] + off) * SR)
            fx = sfx(name)
            audio[s:s + len(fx)] += fx[:max(0, len(audio) - s)]
    audio = np.clip(audio, -1, 1)
    return events, total, audio


# ------------------------------------------------------------------ Zeichnen
def draw_hook(cr, lines):
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(45)
    fe = cr.font_extents()
    lh = fe[2] + 8
    y0 = 250
    exts = [cr.text_extents(s) for s in lines]
    pad_x, pad_y = 22, 8
    for i, (s, e) in enumerate(zip(lines, exts)):
        w = e.x_advance + 2 * pad_x
        x = (W - w) / 2
        y = y0 + i * lh
        rrect(cr, x, y - pad_y, w, lh + 2 * pad_y - 4, 16)
        cr.set_source_rgb(1, 1, 1)
        cr.fill()
    for i, (s, e) in enumerate(zip(lines, exts)):
        x = (W - e.x_advance) / 2
        y = y0 + i * lh + fe[0] + 2
        cr.move_to(x, y)
        cr.set_source_rgb(0.05, 0.05, 0.05)
        cr.show_text(s)


def draw_caption(cr, text, frac):
    """TikTok-Untertitel: Wortgruppen à ~3 Wörter, zeitlich nach Zeichenanteil verteilt."""
    words = text.split()
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 3 or w[-1] in ".?!,":
            chunks.append(" ".join(cur)); cur = []
    if cur:
        chunks.append(" ".join(cur))
    total = sum(len(c) + 2 for c in chunks)
    acc, idx = 0, len(chunks) - 1
    for i, c in enumerate(chunks):
        acc += len(c) + 2
        if frac <= acc / total:
            idx = i
            break
    s = chunks[idx].upper()
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    size = 84
    cr.set_font_size(size)
    e = cr.text_extents(s)
    while e.x_advance > W - 120 and size > 40:
        size -= 4
        cr.set_font_size(size)
        e = cr.text_extents(s)
    x, y = (W - e.x_advance) / 2, 1450
    cr.move_to(x, y)
    cr.text_path(s)
    cr.set_source_rgb(0.05, 0.05, 0.05)
    cr.set_line_width(14)
    cr.set_line_join(cairo.LINE_JOIN_ROUND)
    cr.stroke_preserve()
    cr.set_source_rgb(1, 0.85, 0.2) if any(ch.isdigit() for ch in s) else cr.set_source_rgb(1, 1, 1)
    cr.fill()
    cr.new_path()


def draw_caption_hl(cr, text, frac):
    """Untertitel wie in der Referenz: 3er-Gruppen, aktuelles Wort rot hinterlegt (Bebas Neue)."""
    words = text.replace("...", "").split()
    if not words:
        return
    lens = [len(w) + 1 for w in words]
    tot = sum(lens)
    acc, wi = 0, len(words) - 1
    for i, l in enumerate(lens):
        acc += l
        if frac <= acc / tot:
            wi = i
            break
    start = (wi // 3) * 3
    chunk = [w.upper().strip(",.?!") for w in words[start:start + 3]]
    cr.select_font_face("Bebas Neue", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    size = 74
    cr.set_font_size(size)
    space = cr.text_extents(" ").x_advance + 6
    widths = [cr.text_extents(w).x_advance for w in chunk]
    total = sum(widths) + space * (len(chunk) - 1)
    x = (W - total) / 2
    y = 1360
    for i, w in enumerate(chunk):
        if start + i == wi:
            rrect(cr, x - 10, y - size * 0.82, widths[i] + 20, size * 0.98, 10)
            cr.set_source_rgb(0.86, 0.12, 0.26)
            cr.fill()
        cr.move_to(x, y)
        cr.text_path(w)
        cr.set_source_rgb(0.04, 0.04, 0.05)
        cr.set_line_width(10)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        cr.stroke_preserve()
        cr.set_source_rgb(1, 1, 1)
        cr.fill()
        x += widths[i] + space


class CharState:
    def __init__(self, cid):
        self.cid = cid
        self.emotion = "neutral"
        self.pose = "idle"
        self.hands = dict(POSES["idle"])
        self.prop = None
        self.look = None
        rnd = random.Random(hash(cid) % 1000)
        self.blink_off = rnd.uniform(0, 4)
        self.blink_per = rnd.uniform(3.2, 4.6)


def camera(cr, mode, focus, sp):
    if mode == "wide" or focus is None:
        return
    z = {"med": 1.2, "close": 1.55, "xclose": 1.9}[mode]
    fx, fy = focus
    ox = 540 - z * fx
    oy = 1050 - z * fy
    ox = min(0, max(W - z * W, ox))
    oy = min(0, max(H - z * H, oy))
    cr.translate(ox, oy)
    cr.scale(z, z)


def render(ep, out, preview=None, start=0.0):
    events, total, audio = build(ep)
    end = total if preview is None else min(total, start + preview)
    wav = out.replace(".mp4", ".wav")
    s0, s1 = int(start * SR), int(end * SR)
    seg = (audio[s0:s1] * 32767).astype("<i2")
    import wave
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(seg.tobytes())

    bg_cache = {}
    states = {cid: CharState(cid) for cid in ep.CHARS}
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    proc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS),
         "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out],
        stdin=subprocess.PIPE)

    nframes = int((end - start) * FPS)
    ev_i = 0
    applied = set()
    for f in range(nframes):
        t = start + f / FPS
        while ev_i + 1 < len(events) and events[ev_i + 1]["start"] <= t:
            ev_i += 1
        # alle Events bis jetzt anwenden (Emotion/Pose bleibt bestehen)
        for k in range(ev_i + 1):
            if k in applied:
                continue
            applied.add(k)
            it = events[k]["item"]
            for cid, emo in it.get("e", {}).items():
                states[cid].emotion = emo
            for cid, p in it.get("p", {}).items():
                states[cid].pose = p
            for cid, pr in it.get("prop", {}).items():
                states[cid].prop = pr
            for cid, lk in it.get("look", {}).items():
                states[cid].look = lk
        ev = events[ev_i]
        it = ev["item"]
        shot = ep.SHOTS[ev["shot"]]
        lt = t - ev["start"]
        speaker = it.get("s") if ev["kind"] == "line" and t <= ev["end"] else None

        cr = cairo.Context(surf)
        cr.save()
        # Kamera
        mode = it.get("cam", "wide")
        focus = None
        if mode != "wide":
            tgt = it.get("focus", it.get("s"))
            for layer in shot["layers"]:
                if layer[0] == "char" and layer[1] == tgt:
                    _, _, x, y, sc, fc = layer[:6]
                    focus = (x, y - 700 * sc)
        if ev["kind"] == "beat" and it.get("zoom"):
            z0, z1 = it["zoom"]
            z = z0 + (z1 - z0) * min(1, lt / (ev["end"] - ev["start"]))
            cr.translate(540 * (1 - z), 1150 * (1 - z))
            cr.scale(z, z)
        else:
            camera(cr, mode, focus, None)
        if it.get("punch") and lt < 0.25:
            pz = 1 + 0.06 * (1 - lt / 0.25)
            cr.translate(540 * (1 - pz), 1000 * (1 - pz))
            cr.scale(pz, pz)

        key = shot["bg"]
        if key not in bg_cache:
            bg_cache[key] = ep.BG[key]()
        cr.set_source_surface(bg_cache[key], 0, 0)
        cr.paint()
        if ev["shot"] != getattr(render, "_last_shot", None):
            render._last_shot = ev["shot"]
            render._shot_start = ev["start"]
        bgm.CLOCK["lt"] = t - render._shot_start
        bgm.CLOCK["t"] = t
        bgm.CLOCK["speaker"] = speaker
        _fi = int(lt * FPS)
        bgm.CLOCK["mouth"] = float(ev["env"][_fi]) if speaker and "env" in ev and 0 <= _fi < len(ev["env"]) else 0.0
        bgm.CLOCK["line_t"] = lt
        for fn in shot.get("overlays", []):
            fn(cr, t)

        for layer in shot["layers"]:
            if layer[0] == "fn":
                layer[1](cr)
                continue
            _, cid, x, y, sc, fc = layer[:6]
            opts = layer[6] if len(layer) > 6 else {}
            stt = states[cid]
            pose = stt.pose
            if isinstance(pose, list):
                pose = pose[int(lt / it.get("rate", 1.1)) % len(pose)] if (speaker == cid or it.get("always")) else pose[0]
            tgt = POSES[pose]
            for side in ("L", "R"):
                hx, hy = stt.hands[side][:2]
                tx, ty = tgt[side][:2]
                mode = tgt[side][2] if len(tgt[side]) > 2 else "low"
                stt.hands[side] = (hx + (tx - hx) * 0.35, hy + (ty - hy) * 0.35, mode)
            mo = 0.0
            if speaker == cid:
                fi = int(lt * FPS)
                if 0 <= fi < len(ev["env"]):
                    mo = float(ev["env"][fi])
            ph = (t + stt.blink_off) % stt.blink_per
            blink = 1.0 if ph < 0.11 else 0.0
            lookv = {None: (1.0, 0.05), "down": (0.4, 0.8), "away": (-1.0, 0.0), "up": (0.6, -0.8),
                     "front": (0.0, 0.1)}[stt.look]
            st = dict(hands=stt.hands, emotion=stt.emotion, mouth_open=mo, blink=blink, look=lookv,
                      prop=stt.prop)
            draw_figure(cr, opts.get("look", ep.CHARS[cid]["look"]), x, y, sc, fc, st, t,
                        hide_legs=opts.get("hide_legs", False), shiver=opts.get("shiver", 0.0),
                        sit=opts.get("sit", False))
        for fn in shot.get("front", []):
            fn(cr, t)
        cr.restore()

        if getattr(ep, "CAPTIONS", False) and ev["kind"] == "line" and t <= ev["end"]:
            frac = (t - ev["start"]) / max(0.01, ev["end"] - ev["start"])
            if getattr(ep, "CAPTION_STYLE", "") == "highlight":
                draw_caption_hl(cr, it["t"], frac)
            else:
                draw_caption(cr, it["t"], frac)

        if ep.HOOK and (ep.HOOK_UNTIL is None or t < ep.HOOK_UNTIL):
            draw_hook(cr, ep.HOOK)

        surf.flush()
        proc.stdin.write(bytes(surf.get_data()))
        if f % 300 == 0:
            print(f"frame {f}/{nframes}", flush=True)
    proc.stdin.close()
    proc.wait()
    os.remove(wav)
    print("fertig:", out, f"{end - start:.1f}s")


if __name__ == "__main__":
    path = sys.argv[1]
    preview = None
    start = 0.0
    if "--preview" in sys.argv:
        preview = float(sys.argv[sys.argv.index("--preview") + 1])
    if "--start" in sys.argv:
        start = float(sys.argv[sys.argv.index("--start") + 1])
    sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
    spec = importlib.util.spec_from_file_location("ep", path)
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    os.makedirs(os.path.join(ROOT, "output"), exist_ok=True)
    name = os.path.splitext(os.path.basename(path))[0]
    parent = os.path.basename(os.path.dirname(os.path.abspath(path)))
    if parent != "episodes":
        name = parent + "_" + name
    out = os.path.join(ROOT, "output", name + ("_preview" if preview else "") + ".mp4")
    render(ep, out, preview, start)
