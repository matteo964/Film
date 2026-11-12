"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="photo_R", s="R", t="Ladies and gentlemen! Please enjoy a slideshow of my beautiful daughter's wedding!",
         e={"R": "happy"}, p={"R": "explain2"}, say="[proud, loud] Ladies and gentlemen! Please enjoy a slideshow of my beautiful daughter's wedding!"),
    dict(shot="watermark_RJE", beat=1.4, sfx=[("ding", 0.0)], e={"R": "happy", "J": "neutral", "E": "happy"},
         p={"R": "idle", "J": "idle", "E": "idle"}, look={"R": "up", "J": "up", "E": "up"}),
    dict(s="E", t="Dad? Why does every photo say unpaid preview?", e={"E": "shocked"}, look={"E": None}, p={"E": "chest"}),
    dict(s="R", t="That's, uh, just a filter. Very trendy.", e={"R": "worried"}, p={"R": "shrug"}, look={"R": None},
         say="[nervous] That's, uh... just a filter. Very trendy."),
    dict(shot="watermark_E", s="E", t="It says invoice number two oh seven. Three thousand five hundred dollars due.", e={"E": "angry"},
         look={"E": "up"}),
    dict(shot="watermark_RJE", s="E", t="Dad, two hundred people are staring at us.", e={"E": "worried"}, p={"E": "idle"}, look={"E": None}),
    dict(s="R", t="Smile, sweetheart. It's your big day.", e={"R": "worried"}, p={"R": "shrug"},
         say="[forced smile] Smile, sweetheart. It's your big day."),
    dict(shot="watermark_R", s="R", t="Jake! Switch to your photos! Quickly!", e={"R": "angry"}, p={"R": "point"},
         say="[urgent whisper] Jake! Switch to your photos! Quickly!"),
    dict(shot="nephew_J", s="J", t="Got it, Uncle Rich. My photos are amazing.", e={"J": "happy"}, p={"J": "chest"}, sfx=[("ding", 0.0)],
         say="[proud] Got it, Uncle Rich. My photos are amazing."),
    dict(shot="nephew_RJE", beat=1.2, e={"R": "shocked", "E": "shocked", "J": "happy"}, look={"R": "up", "E": "up", "J": "up"}),
    dict(s="E", t="Is that a thumb? Is that your thumb in my wedding photo?", e={"E": "angry"}, look={"E": None}, p={"E": "point"},
         say="[horrified] Is that a thumb? Is that your THUMB in my wedding photo?"),
    dict(s="J", t="It's artistic. And the blurry ones are action shots.", e={"J": "worried"}, p={"J": "shrug"}, look={"J": None}),
    dict(shot="nephew_E", s="E", t="Every single picture is blurry!", e={"E": "angry"}, p={"E": "panic"}, punch=True,
         say="[upset] Every single picture is blurry!"),
    dict(shot="nephew_RES", s="S", t="Excuse me. I'm a wedding planner. Those first photos were stunning. Who's the photographer?",
         e={"S": "neutral", "R": "worried", "E": "sad"}, p={"S": "explain", "R": "idle", "E": "idle"}),
    dict(s="R", t="Nobody important.", e={"R": "worried"}, say="[mumbling] Nobody important."),
    dict(shot="nephew_E", s="E", t="Dad. Look at me. Did you not pay the photographer?", e={"E": "angry"}, p={"E": "cross"}, cam="close",
         say="[slow, furious] Dad. Look at me. Did you not pay the photographer?", gap=0.8),
]
