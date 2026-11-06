"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="stage_site_GL", s="G", t="Mrs. Chen, thank you for coming. Today, Grant and Company enters the future.",
         e={"G": "happy", "L": "neutral"}, p={"G": "explain2", "L": "cross"}),
    dict(s="L", t="I'm impressed, Greg. Who designed the website?", e={"L": "happy"}, p={"L": "explain"}),
    dict(s="G", t="Oh, that was all us. Totally in house.", e={"G": "smug"}, p={"G": "chest"}),
    dict(s="L", t="Really? It looks very professional.", e={"L": "neutral"}, p={"L": "idle"}),
    dict(s="G", t="Well, we only hire the best. And we pay them very fairly.", e={"G": "happy"},
         p={"G": ["explain", "chest"]}, cam="med"),
    dict(shot="stage_site_GT", s="T", t="Uncle Greg, it's almost ten. Should I make the site go live?",
         e={"T": "neutral"}, p={"T": "tablet", "G": "idle"}, prop={"T": "tablet"}),
    dict(s="G", t="Yes! Do it. Let's give them a show.", e={"G": "happy"}, p={"G": "point"}),
    dict(shot="stage_site_GL", s="G", t="Ladies and gentlemen. Our brand new website!", p={"G": "panic"},
         say="[excited] Ladies and gentlemen. Our brand new website!", gap=0.6),

    dict(shot="stage_down_GL", beat=1.4, sfx=[("alarm", 0.0)], e={"G": "shocked", "L": "confused"},
         p={"G": "idle", "L": "cross"}),
    dict(s="L", t="Website suspended? Invoice unpaid?", e={"L": "confused"}, cam="med"),
    dict(s="G", t="That's, uh, that's just a little technical glitch.", e={"G": "worried"}, p={"G": "shrug"}),
    dict(s="L", t="It says the amount due is four thousand eight hundred dollars.", e={"L": "annoyed"}),
    dict(shot="stage_down_GT", s="G", t="Tyler! Fix it! Right now!", e={"G": "angry", "T": "worried"},
         p={"G": "point"}, say="[angry whisper] Tyler! Fix it! Right NOW!"),
    dict(s="T", t="I'm trying! But I can't log in to the hosting account.", p={"T": "tablet"}),
    dict(s="G", t="You said you copied everything!", p={"G": "explain2"}),
    dict(s="T", t="I copied the files. Not the domain.", e={"T": "sad"}),
    dict(s="G", t="So who owns the domain?", e={"G": "worried"}),
    dict(s="T", t="According to this, Zoe Parker.", e={"T": "worried"}, look={"T": "down"}),
    dict(shot="stage_down_GL", s="L", t="Greg. You don't even own your own website?", e={"L": "angry"},
         p={"L": "hips"}, cam="med", look={"T": None}),
    dict(s="G", t="Technically, it's a gray area.", e={"G": "worried"}, p={"G": "facepalm"}),
    dict(s="L", t="Then I suggest you call Ms. Parker. Right now.", e={"L": "annoyed"}, p={"L": "point"}),
    dict(s="L", t="Or my investment walks out that door with me.", p={"L": "cross"}),
    dict(shot="stage_down_G", s="G", t="Okay. Okay. I'm calling her.", e={"G": "sad"}, p={"G": "phone"},
         prop={"G": "phone"}, say="[sighs] Okay. Okay. I'm calling her."),
    dict(s="G", t="Zoe! Hey! It's Greg. How's my favorite web designer doing?", e={"G": "happy"},
         say="[nervously cheerful] Zoe! Hey! It's Greg. How's my favorite web designer doing?",
         cam="close", gap=0.8),
]
