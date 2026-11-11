"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="lobby_V_phone", s="V", t="Noah! Buddy! How's the free time treating you?", e={"V": "happy", "N": "calm"},
         p={"V": "phone", "N": "lap_phone"}, prop={"V": "phone", "N": "phone"},
         say="[fake cheerful] Noah! Buddy! How's the free time treating you?"),
    dict(shot="home_N", s="N", t="It's been one day, Victor. It's great.", e={"N": "smug"}, cam="med",
         say="[relaxed] It's been one day, Victor. It's great."),
    dict(shot="lobby_V_phone", s="V", t="Quick question. Kevin may have unplugged the beige box.", e={"V": "worried"}),
    dict(shot="home_N", s="N", t="The one with the sticker that says do not touch?", e={"N": "smug"}),
    dict(shot="lobby_V_phone", s="V", t="That's the one.", e={"V": "sad"}, say="[defeated] That's the one."),
    dict(shot="home_N", s="N", t="I can fix it in five minutes. My consulting fee is five thousand dollars.", e={"N": "calm"},
         p={"N": "lap_explain"}),
    dict(shot="lobby_V_phone", s="V", t="Five thousand? To type a password?", e={"V": "shocked"}, punch=True,
         say="[outraged] Five THOUSAND? To type a password?"),
    dict(shot="home_N", s="N", t="Typing it costs one dollar. Knowing it costs four thousand nine hundred ninety nine.",
         e={"N": "smug"}, p={"N": "lap_phone"}, cam="close",
         say="[dryly] Typing it costs one dollar. Knowing it costs four thousand nine hundred ninety nine."),
    dict(shot="lobby_VD_phone", s="D", t="Give me the phone, Victor.", e={"D": "annoyed", "V": "worried"}, p={"D": "stop", "V": "idle"},
         prop={"V": None}),
    dict(s="D", t="Noah, it's Diana. Your fee is approved. And I want you back. Head of IT. Double your old salary.",
         p={"D": "phone"}, prop={"D": "phone"}, e={"D": "happy"}),
    dict(shot="home_N", s="N", t="Deal. Give me ten seconds.", e={"N": "happy"}, say="[satisfied] Deal. Give me ten seconds.", gap=0.5),
    dict(shot="ok_VD", beat=1.3, sfx=[("ding", 0.2)], e={"V": "shocked", "D": "happy"}, p={"V": "idle", "D": "idle"},
         prop={"D": None}),
    dict(s="D", t="Doors are open. Website's back. That man is worth every cent.", e={"D": "happy"}, p={"D": "explain"}),
    dict(s="D", t="Oh, and Victor. Starting Monday, you report to Noah.", e={"D": "smug"}, p={"D": "cross"}, cam="med"),
    dict(s="V", t="Report to the IT guy?", e={"V": "shocked"}, p={"V": "head"}, punch=True,
         say="[horrified] Report to the IT GUY?", gap=0.4),
    dict(shot="ok_NV", s="N", t="The IT guy who runs the company, Victor.", e={"N": "smug", "V": "sad"}, p={"N": "hips", "V": "idle"},
         say="[calm, confident] The IT guy who runs the company, Victor."),
    dict(shot="ok_NK", s="K", t="So where can I plug in my gaming monitor?", e={"K": "worried", "N": "calm"}, p={"K": "shrug", "N": "idle"},
         say="[sheepish] So... where can I plug in my gaming monitor?"),
    dict(s="N", t="Anywhere you want, Kevin. Except there.", e={"N": "smug"}, p={"N": "point"}, cam="med",
         say="[deadpan] Anywhere you want, Kevin. Except there.", gap=0.8),
]
