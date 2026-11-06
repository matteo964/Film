"""Erzeugt fehlende ElevenLabs-Zeilen lokal mit Chatterbox (Stimmvorlage = vorhandene EL-Zeilen der Figur)."""
import sys, os, re, hashlib, importlib.util, subprocess, functools
import numpy as np
sys.path.insert(0, 'engine')
ep_dir = sys.argv[1]
sys.path.insert(0, ep_dir)
import render
import tqdm
tqdm.tqdm.__init__ = functools.partialmethod(tqdm.tqdm.__init__, disable=True)

def key_for(c, it, emo):
    text = it.get("say", it["t"]); e = it.get("tone", emo.get(it["s"], "neutral"))
    tagged = text if text.lstrip().startswith("[") else (render.EMO_TAG.get(e, "") + " " + text).strip()
    return tagged, f"build/tts/el_" + hashlib.md5(f"el|{c['el_voice']}|eleven_v3|0.5|1|{tagged}".encode()).hexdigest() + ".mp3"

have, missing = {}, []
for f in sorted(os.listdir(ep_dir)):
    if not f.startswith("part"): continue
    spec = importlib.util.spec_from_file_location("ep", os.path.join(ep_dir, f)); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    emo = {}
    for it in ep.SCRIPT:
        emo.update(it.get("e", {}))
        if "t" not in it or "beat" in it: continue
        c = ep.CHARS[it["s"]]; tagged, path = key_for(c, it, emo)
        if os.path.exists(path) and os.path.getsize(path) > 0: have.setdefault(it["s"], []).append(path)
        else: missing.append((it["s"], tagged, path))
print(len(missing), "fehlende Zeilen")
if not missing: sys.exit()
import torch, torchaudio
from chatterbox.tts import ChatterboxTTS
torch.set_num_threads(4)
m = ChatterboxTTS.from_pretrained(device="cpu")
os.makedirs("build/ref", exist_ok=True)
log = open("build/tts/fallback.txt", "a")
for cid, tagged, path in missing:
    ref = f"build/ref/{cid}.wav"
    if not os.path.exists(ref):
        lst = "|".join(have[cid][:6])
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"concat:{lst}", "-ac", "1", "-ar", "24000", "-t", "15", ref], check=True)
    plain = re.sub(r"\[[^\]]*\]", "", tagged).strip()
    plain = re.sub(r"\b([A-Z][A-Z']+)\b", lambda mm: mm.group(1).capitalize() if mm.group(1) not in ("I", "OK") else mm.group(1), plain)
    excited = any(w in tagged for w in ("excited", "outraged", "shouting", "cheerfully", "playfully"))
    torch.manual_seed(0)
    w = m.generate(plain, audio_prompt_path=ref, exaggeration=0.75 if excited else 0.55, cfg_weight=0.4)
    tmp = path.replace(".mp3", ".wav"); torchaudio.save(tmp, w, m.sr)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-b:a", "128k", path], check=True); os.remove(tmp)
    log.write(path + "\n"); print("ok", cid, plain, flush=True)
