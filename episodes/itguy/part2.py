"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="lobby_V", s="V", t="Why is my badge not working?", e={"V": "annoyed"}, p={"V": "point"},
         say="[irritated] Why is my badge not working?"),
    dict(s="V", t="Access denied? I'm the boss!", e={"V": "angry"}, p={"V": "panic"}, punch=True, sfx=[("ding", 0.0)],
         say="[outraged] Access DENIED? I'm the boss!"),
    dict(shot="lobby_VD", s="D", t="Victor. Why is my entire company standing on the sidewalk?", e={"D": "angry", "V": "worried"},
         p={"D": "cross", "V": "idle"}),
    dict(s="V", t="Diana! Just a tiny glitch. Nothing to worry about.", e={"V": "worried"}, p={"V": "shrug"},
         say="[nervous] Diana! Just a tiny glitch. Nothing to worry about."),
    dict(shot="lobby_D", s="D", t="The website is down too. Customers can't place a single order.", e={"D": "angry"}, p={"D": "phone"},
         prop={"D": "phone"}),
    dict(shot="lobby_VD", s="V", t="At least the coffee machine works, right?", e={"V": "worried"}, p={"V": "shrug"}, prop={"D": None},
         say="[hopeful] At least the coffee machine works, right?"),
    dict(s="D", t="It's a smart coffee machine, Victor. It's connected to the server too.", e={"D": "annoyed"}, p={"D": "cross"}),
    dict(s="V", t="Why is the coffee connected to the server?", e={"V": "shocked"}, p={"V": "panic"},
         say="[baffled] Why is the COFFEE connected to the server?"),
    dict(shot="lobby_K", s="V", t="Kevin? Is that you in there?", e={"V": "confused"}, p={"V": "point"}, look={"V": "away"}),
    dict(s="K", t="I came in early to impress you. Now I'm locked in!", e={"K": "worried"},
         say="[muffled, panicking] I came in early to impress you. Now I'm locked IN!"),
    dict(s="V", t="Then fix it!", e={"V": "angry"}, p={"V": "stop"}, say="[shouting] Then FIX it!"),
    dict(s="K", t="I plugged the box back in. But now it wants a password. Sixty four characters.", e={"K": "worried"},
         say="[muffled, desperate] I plugged the box back in. But now it wants a password. Sixty four characters."),
    dict(shot="lobby_VD_phone", s="D", t="Who has that password?", e={"D": "neutral", "V": "worried"}, p={"D": "cross", "V": "idle"},
         prop={"D": None}),
    dict(shot="lobby_K", s="K", t="The screen says, please contact Noah.", e={"K": "sad"}, look={"V": "away"},
         say="[muffled, sheepish] The screen says... please contact Noah."),
    dict(shot="lobby_D", s="D", t="Noah? Our IT lead? Where is Noah?", e={"D": "confused"}, p={"D": "shrug"}, cam="med"),
    dict(shot="lobby_V", s="V", t="He's no longer with us. I replaced him. Smart business.", e={"V": "worried"}, p={"V": "chest"},
         look={"V": None}),
    dict(shot="lobby_D", s="D", t="You fired the man who built our entire system. To save fifty thousand dollars.", e={"D": "angry"},
         p={"D": "point"}),
    dict(s="D", t="We're losing that much every hour the website is down.", e={"D": "angry"}, cam="close",
         say="[furious] We're losing that much every HOUR the website is down."),
    dict(shot="lobby_V", s="V", t="Funny story.", e={"V": "worried"}, p={"V": "shrug"}, cam="close",
         say="[nervous laugh] Funny story...", gap=0.8),
]
