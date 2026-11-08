import sys, os, re, glob, functools, subprocess
sys.path.insert(0,'engine'); sys.path.insert(0,'.')
import tqdm; tqdm.tqdm.__init__ = functools.partialmethod(tqdm.tqdm.__init__, disable=True)
import render, torch, torchaudio
from engine.fallback_chatterbox import items
from chatterbox.tts import ChatterboxTTS
fb=set(open('build/tts/fallback.txt').read().split())
todo=[]
for f in sorted(glob.glob(f'{sys.argv[1]}/part*.py')):
    for cid,c,tagged,p in items(f,sys.argv[1]):
        if p in fb and not c.get("robot"):
            sc,_=render._check(render.trim_norm(render._decode(p)),tagged)
            if sc<0.75: todo.append((cid,c,tagged,p))
print(len(todo),"zu reparieren",flush=True)
m=ChatterboxTTS.from_pretrained(device="cpu")
for cid,c,tagged,p in todo:
    plain=re.sub(r"\[[^\]]*\]","",tagged).strip()
    best=None
    for seed in range(1,9):
        torch.manual_seed(seed)
        w=m.generate(plain,audio_prompt_path=f"build/ref/{c['el_voice']}.wav",exaggeration=0.5,cfg_weight=0.5)
        a=w.squeeze().numpy()
        import numpy as np
        a24=np.interp(np.arange(0,len(a),m.sr/24000),np.arange(len(a)),a).astype(np.float32)
        sc,h=render._check(render.trim_norm(a24),tagged)
        if best is None or sc>best[0]: best=(sc,w,h)
        if sc>=0.99: break
    tmp=p.replace(".mp3",".wav"); torchaudio.save(tmp,best[1],m.sr)
    subprocess.run(["ffmpeg","-v","error","-y","-i",tmp,"-b:a","128k",p],check=True); os.remove(tmp)
    print(f"{cid} {best[0]:.2f} '{best[2].strip()}' für '{plain}'",flush=True)
