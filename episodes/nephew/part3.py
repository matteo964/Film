"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="fail_M", s="M", t="Okay. Okay. I'm calling her.", e={"M": "worried", "E": "calm"}, p={"M": "phone", "E": "lap_phone"},
         prop={"M": "phone", "E": "phone"}, say="[panicked] Okay. Okay. I'm calling her."),
    dict(s="M", t="Emma! How's my favorite employee doing?", e={"M": "happy"}, say="[fake cheerful] Emma! How's my favorite employee doing?"),
    dict(shot="living_E", s="E", t="Hi Mark. I thought Tyler was your favorite.", e={"E": "smug"}, cam="med",
         say="[dryly] Hi Mark. I thought Tyler was your favorite."),
    dict(shot="fail_M", s="M", t="About that. Mrs. Henderson would like you back on the account.", e={"M": "worried"},
         say="[nervous laugh] About that... Mrs. Henderson would like you back on the account."),
    dict(shot="living_E", s="E", t="I'm meeting Brightline tomorrow morning.", e={"E": "calm"}),
    dict(shot="fail_M", s="M", t="Don't! Please. What do you want?", e={"M": "shocked"}, punch=True, say="[desperate] Don't! Please. What do you want?"),
    dict(shot="living_E", s="E", t="The team lead title. The raise you promised me two years ago.", e={"E": "neutral"}, p={"E": "lap_explain"}),
    dict(s="E", t="And Tyler goes back to being an intern.", e={"E": "smug"}, p={"E": "lap_phone"}, cam="med"),
    dict(shot="fail_M", s="M", t="An intern? He's my nephew!", e={"M": "angry"}, say="[outraged] An intern? He's my NEPHEW!"),
    dict(shot="living_E", s="E", t="Family first, right? Then he can start from the bottom. Like family.", e={"E": "smug"},
         say="[sweetly] Family first, right? Then he can start from the bottom. Like family."),
    dict(shot="fail_MH", s="H", t="Give me that phone, Mark.", e={"H": "annoyed", "M": "worried"}, p={"H": "stop", "M": "idle"},
         prop={"M": None}),
    dict(s="H", t="Emma, it's Margaret Henderson. I'll renew today. Three years. If you lead the account.",
         p={"H": "phone"}, prop={"H": "phone"}, e={"H": "happy"}),
    dict(shot="living_E", s="E", t="Then we have a deal, Mrs. Henderson.", e={"E": "happy"}, say="[warmly] Then we have a deal, Mrs. Henderson."),
    dict(shot="signed_MH", beat=1.2, sfx=[("ding", 0.0)], e={"M": "happy", "H": "happy"}, p={"M": "idle", "H": "idle"},
         prop={"H": None}, look={"M": "up", "H": "up"}),
    dict(shot="signed_M", s="M", t="Fine. Emma is team lead. With the raise.", e={"M": "sad"}, look={"M": None},
         say="[defeated] Fine. Emma is team lead. With the raise."),
    dict(shot="signed_T", s="T", t="Wait. So I'm an intern now?", e={"T": "shocked"}, p={"T": "chest"}, punch=True,
         say="[shocked] Wait. So I'm an INTERN now?", gap=0.4),
    dict(shot="open_ET", s="E", t="Welcome to the team, Tyler. First lesson. It's Mrs. Henderson. Not bro.",
         e={"E": "smug", "T": "sad"}, p={"E": "explain", "T": "idle"}, prop={"E": None},
         say="[confident] Welcome to the team, Tyler. First lesson. It's Mrs. Henderson. Not bro."),
    dict(s="T", t="Yes, ma'am.", e={"T": "sad"}, say="[humbled] Yes, ma'am."),
    dict(s="E", t="See? Turns out you can teach leadership. It just takes six years.", e={"E": "happy"}, p={"E": "hips"}, cam="med",
         say="[playfully] See? Turns out you CAN teach leadership. It just takes six years.", gap=0.8),
]
