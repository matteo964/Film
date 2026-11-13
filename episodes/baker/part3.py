"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="collapse_V", s="V", t="Then where is it, Howard?", e={"V": "smug", "H": "worried", "R": "calm"}, p={"V": "cross"},
         cam="close", say="[cold] Then where is it, Howard?"),
    dict(shot="collapse_H", s="H", t="Okay. Okay. I'm calling her.", e={"H": "worried"}, p={"H": "phone"}, prop={"H": "phone"},
         say="[panicked] Okay. Okay. I'm calling her."),
    dict(s="H", t="Rosa! Hi! It's Howard. Is that beautiful cake still available?", e={"H": "happy"},
         say="[fake cheerful] Rosa! Hi! It's Howard. Is that beautiful cake still available?"),
    dict(shot="bakery_R", s="R", t="Let me guess. Chad's cake didn't make it.", e={"R": "smug"}, p={"R": "phone"}, prop={"R": "phone"}, cam="med"),
    dict(shot="collapse_H", s="H", t="It collapsed. In front of three hundred people.", e={"H": "sad"}, say="[defeated] It collapsed. In front of three hundred people."),
    dict(shot="bakery_R", s="R", t="I can be there in twenty minutes. It's thirty eight hundred now.", e={"R": "calm"}),
    dict(shot="collapse_H", s="H", t="Thirty eight hundred? It was twenty eight!", e={"H": "shocked"}, punch=True,
         say="[outraged] Thirty-eight hundred? It was twenty-eight!"),
    dict(shot="bakery_R", s="R", t="Rush delivery fee. And an emergency frosting fee. Apparently frosting doesn't fix everything.",
         e={"R": "smug"}, say="[dryly] Rush delivery fee. And an emergency frosting fee. Apparently frosting doesn't fix everything."),
    dict(shot="collapse_HV", s="V", t="Give me the phone, Howard.", e={"V": "annoyed", "H": "worried"}, p={"V": "stop", "H": "idle"},
         prop={"H": None}),
    dict(s="V", t="Miss Rosa, Eleanor Vance here. I'll pay the thirty eight hundred myself. Please hurry.", p={"V": "phone"},
         prop={"V": "phone"}, e={"V": "neutral"}),
    dict(shot="bakery_R", s="R", t="On my way.", e={"R": "happy"}, say="[cheerful] On my way.", gap=0.5),
    dict(shot="real_VR", beat=1.4, sfx=[("ding", 0.2)], e={"V": "happy", "R": "happy"}, p={"V": "idle", "R": "explain"},
         prop={"V": None, "R": None}, look={"V": "down"}),
    dict(s="V", t="Now that is a cake. Who made this masterpiece?", e={"V": "happy"}, look={"V": None}, p={"V": "explain"}),
    dict(s="R", t="Rosa Delgado. Freelance baker.", e={"R": "happy"}, p={"R": "chest"}),
    dict(s="V", t="I have forty two hotels, Miss Delgado. I want you for every single one of our events.", e={"V": "happy"}, cam="med"),
    dict(shot="real_HC", s="C", t="Can I be your assistant? I'm great with frosting.", e={"C": "happy", "H": "annoyed"}, p={"C": "pray", "H": "cross"},
         say="[hopeful] Can I be your assistant? I'm great with frosting."),
    dict(s="H", t="No, Chad.", e={"H": "angry"}, say="[firmly] No, Chad."),
    dict(shot="real_HR", s="H", t="Rosa, can I at least get a discount for all that exposure?", e={"H": "worried", "R": "smug"},
         p={"H": "pray", "R": "cross"}),
    dict(s="R", t="Think of the exposure, Howard. Three hundred VIPs just saw your cake collapse.", e={"R": "smug"}, cam="close",
         say="[sweetly] Think of the exposure, Howard. Three hundred VIPs just saw your cake collapse.", gap=0.8),
]
