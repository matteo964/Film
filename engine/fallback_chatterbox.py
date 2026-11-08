"""Erzeugt fehlende ElevenLabs-Zeilen lokal mit Chatterbox.

Stimmvorlage = vorhandene ElevenLabs-Aufnahmen derselben ElevenLabs-Stimme (aus allen Serien).
Die Datei wird unter dem ElevenLabs-Cache-Namen abgelegt und in build/tts/fallback.txt vermerkt,
damit sie später (mit Credits) gelöscht und echt neu erzeugt werden kann.
Figuren mit robot=True werden mit Edge-TTS + Roboter-Effekt erzeugt.

Aufruf (Chatterbox-venv):  python engine/fallback_chatterbox.py episodes/<serie>
"""
import functools
import glob
import hashlib
import importlib.util
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render  # noqa: E402

import tqdm  # noqa: E402
tqdm.tqdm.__init__ = functools.partialmethod(tqdm.tqdm.__init__, disable=True)

HOT = ("shout", "angry", "panick", "desperate", "excited", "outraged", "horrified", "fake cheerful")


def items(path, ep_dir):
    sys.path.insert(0, ep_dir)
    sys.modules.pop("common", None)
    spec = importlib.util.spec_from_file_location("ep", path)
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    sys.path.pop(0)
    emo = {}
    for it in ep.SCRIPT:
        emo.update(it.get("e", {}))
        if "t" not in it or "beat" in it:
            continue
        c = ep.CHARS[it["s"]]
        if "el_voice" not in c:
            continue
        text = it.get("say", it["t"])
        e = it.get("tone", emo.get(it["s"], "neutral"))
        tagged = text if text.lstrip().startswith("[") else (render.EMO_TAG.get(e, "") + " " + text).strip()
        p = "build/tts/el_" + hashlib.md5(f"el|{c['el_voice']}|eleven_v3|0.5|1|{tagged}".encode()).hexdigest() + ".mp3"
        yield it["s"], c, tagged, p


def main(ep_dir):
    fallback = set(open("build/tts/fallback.txt").read().split()) if os.path.exists("build/tts/fallback.txt") else set()
    have, missing = {}, []
    for f in sorted(glob.glob("episodes/*/part*.py")):
        d = os.path.dirname(f)
        for cid, c, tagged, p in items(f, d):
            ok = os.path.exists(p) and os.path.getsize(p) > 0
            if ok and p not in fallback:
                have.setdefault(c["el_voice"], []).append(p)
            if not ok and os.path.abspath(d) == os.path.abspath(ep_dir) and p not in [m[3] for m in missing]:
                missing.append((cid, c, tagged, p))
    print(len(missing), "fehlende Zeilen", flush=True)
    if not missing:
        return
    import torch
    import torchaudio
    from chatterbox.tts import ChatterboxTTS
    torch.set_num_threads(os.cpu_count() or 4)
    m = ChatterboxTTS.from_pretrained(device="cpu")
    os.makedirs("build/ref", exist_ok=True)
    log = open("build/tts/fallback.txt", "a")
    for cid, c, tagged, path in missing:
        plain = re.sub(r"\[[^\]]*\]", "", tagged).strip()
        plain = re.sub(r"\b([A-Z][A-Z']+)\b", lambda mm: mm.group(1).capitalize() if mm.group(1) != "I" else "I", plain)
        if c.get("robot"):
            tmp = path + ".edge.mp3"
            import asyncio
            asyncio.run(render._tts(plain, c["voice"], "+8%", "+20Hz", tmp))
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af",
                            "afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75,"
                            "aecho=0.8:0.6:12:0.3", "-b:a", "128k", path], check=True)
            os.remove(tmp)
        else:
            ref = f"build/ref/{c['el_voice']}.wav"
            if not os.path.exists(ref):
                src = have.get(c["el_voice"])
                if not src:
                    print("Keine Vorlage für", cid, "- übersprungen")
                    continue
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "concat:" + "|".join(src[:8]), "-ac", "1",
                                "-ar", "24000", "-t", "18", ref], check=True)
            hot = any(h in tagged.lower() for h in HOT)
            torch.manual_seed(0)
            w = m.generate(plain, audio_prompt_path=ref, exaggeration=0.8 if hot else 0.55, cfg_weight=0.35)
            tmp = path.replace(".mp3", ".wav")
            torchaudio.save(tmp, w, m.sr)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-b:a", "128k", path], check=True)
            os.remove(tmp)
        log.write(path + "\n")
        log.flush()
        print("ok", cid, plain, flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
