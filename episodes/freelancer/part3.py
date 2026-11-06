"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    # Überlappung mit dem Ende von Teil 2
    dict(shot="stage_down_G", s="G", t="Zoe! Hey! It's Greg. How's my favorite web designer doing?",
         e={"G": "happy", "Z": "calm"}, p={"G": "phone", "Z": "lap_phone"}, prop={"G": "phone", "Z": "phone"},
         say="[nervously cheerful] Zoe! Hey! It's Greg. How's my favorite web designer doing?"),
    dict(shot="apt", s="Z", t="Let me guess. Your website is down.", e={"Z": "smug"}, cam="med"),
    dict(shot="stage_down_G", s="G", t="Ha. Funny story. Yeah. Could you maybe turn it back on?",
         e={"G": "worried"}, say="[nervous laugh] Ha. Funny story. Yeah. Could you maybe turn it back on?"),
    dict(shot="apt", s="Z", t="Sure. As soon as invoice ten forty two is paid.", e={"Z": "calm"}),
    dict(shot="stage_down_G", s="G", t="Come on, Zoe. Think of the exposure.", e={"G": "happy"}),
    dict(shot="apt", s="Z", t="Exposure? Greg, a whole room of investors is looking at my name right now.",
         e={"Z": "smug"}, say="[laughs] Exposure? Greg, a whole room of investors is looking at my name right now."),
    dict(s="Z", t="I think I've got enough exposure.", e={"Z": "smug"}, cam="close"),
    dict(shot="stage_down_G", s="G", t="Fine. Fine! I'll pay the forty eight hundred.", e={"G": "angry"}),
    dict(shot="apt", s="Z", t="It's ninety six hundred now.", e={"Z": "calm"}),
    dict(shot="stage_down_G", s="G", t="Ninety six hundred?", e={"G": "shocked"}, punch=True,
         say="[shocked] NINETY SIX hundred?"),
    dict(shot="apt", s="Z", t="Late fee, rush fee, and a weekend fee. Tyler said it only takes a weekend.",
         e={"Z": "smug"}),
    dict(shot="stage_down_GL", s="L", t="Give me the phone, Greg.", e={"L": "annoyed", "G": "worried"},
         p={"L": "stop"}, prop={"G": None}, look={"G": None}),
    dict(s="L", t="Ms. Parker, this is Linda Chen. Send me the invoice. I'll pay it personally.",
         p={"L": "phone"}, prop={"L": "phone"}, e={"L": "neutral"}),
    dict(shot="apt", s="Z", t="Thank you, Mrs. Chen. It's in your inbox.", e={"Z": "happy"}),
    dict(shot="stage_down_GL", s="L", t="And paid.", e={"L": "calm"}, p={"L": "phone"}),
    dict(shot="apt", s="Z", t="Then the website is back online in three. Two. One.", e={"Z": "smug"},
         p={"Z": "lap_phone"}, gap=0.3),
    dict(shot="stage_back_GL", beat=1.2, sfx=[("ding", 0.0)], e={"G": "happy", "L": "neutral"},
         p={"G": "panic", "L": "idle"}, prop={"L": None}),
    dict(s="G", t="It's back! See? I told you it was just a little glitch.", e={"G": "happy"}, p={"G": "chest"},
         say="[relieved] It's back! See? I told you it was just a little glitch."),
    dict(s="L", t="Greg, you almost lost my investment over a four thousand dollar invoice.", e={"L": "angry"},
         p={"L": "point"}, cam="med"),
    dict(s="G", t="In my defense, she was very expensive.", e={"G": "worried"}, p={"G": "shrug"}),
    dict(s="L", t="She was worth every cent. Here's my condition.", e={"L": "annoyed"}, p={"L": "cross"}),
    dict(s="L", t="Ms. Parker builds the rest of the platform. And you don't touch the budget.",
         p={"L": ["explain", "cross"]}),
    dict(s="G", t="Fine.", e={"G": "sad"}, p={"G": "idle"}, say="[defeated] Fine."),
    dict(shot="stage_back_LT", s="T", t="Um, can I at least keep my job?", e={"T": "worried", "L": "neutral"},
         p={"T": "chest", "L": "idle"}, prop={"T": None}),
    dict(s="L", t="What exactly is your job?", e={"L": "confused"}, p={"L": "hips"}),
    dict(s="T", t="Copying files?", e={"T": "confused"}, p={"T": "shrug"}, say="[unsure] Copying files?"),
    dict(shot="apt", s="Z", t="Oh, and Greg? I'm keeping my name in the footer.", e={"Z": "smug"},
         p={"Z": "lap_phone"}, cam="med"),
    dict(s="Z", t="Think of the exposure.", e={"Z": "happy"}, cam="close",
         say="[playfully] Think of the exposure.", gap=0.8),
]
