"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="open_MJ", s="J", t="Mia, he stole your project in front of the CEO! Do something!", e={"J": "angry", "M": "calm"},
         p={"J": "point", "M": "cross"}),
    dict(s="M", t="Oh, I will. On Friday.", e={"M": "smug"}, cam="med", say="[calm, knowing] Oh, I will. On Friday."),
    dict(shot="open_J", s="J", t="Why Friday?", e={"J": "confused"}, p={"J": "shrug"}),
    dict(shot="open_M", s="M", t="Because that's when Brad has to explain pages two to twenty four.", e={"M": "smug"}, gap=0.4),
    dict(shot="blank_BO", s="B", t="Welcome, everyone. Page two. The supplier switch.", e={"B": "smug", "O": "neutral"},
         p={"B": "point", "O": "cross"}, look={"B": "up"}, sfx=[("ding", 0.0)]),
    dict(shot="blank_O", s="O", t="Your slide says question mark, question mark, question mark. Ask Mia.", e={"O": "confused"},
         look={"O": "up"}),
    dict(shot="blank_B", s="B", t="That's a placeholder. For suspense.", e={"B": "worried"}, p={"B": "shrug"},
         say="[nervous] That's a placeholder. For... suspense."),
    dict(shot="blank_O", s="O", t="Fine. Walk me through the cost model, then.", e={"O": "annoyed"}, p={"O": "cross"}, look={"O": None}),
    dict(shot="blank_B", s="B", t="The cost model is, uh, locked. By its owner.", e={"B": "worried"}, look={"B": "up"},
         say="[panicking] The cost model is, uh... locked. By its owner."),
    dict(shot="blank_O", s="O", t="By its owner? I thought you were the owner, Brad.", e={"O": "annoyed"}, cam="med"),
    dict(shot="blank_BMO", s="M", t="Mr. Okafor, may I?", e={"M": "calm", "B": "worried", "O": "neutral"}, p={"M": "explain", "B": "idle", "O": "idle"}),
    dict(s="B", t="She's just going to talk about fonts.", e={"B": "smug"}, p={"B": "cross"}, say="[dismissive] She's just going to talk about fonts."),
    dict(shot="history_M", s="M", t="Here's the version history of the file.", e={"M": "smug"}, p={"M": "point"}, look={"M": "up"},
         sfx=[("ding", 0.0)]),
    dict(s="M", t="Created by me, Tuesday, two oh seven a.m. Edited forty six times.", e={"M": "calm"}),
    dict(s="M", t="Brad viewed it once. At five oh three p.m. Then he copied it.", e={"M": "smug"}, cam="med"),
    dict(shot="history_B", s="B", t="That's, uh, a glitch.", e={"B": "shocked"}, p={"B": "head"}, punch=True,
         say="[sweating] That's, uh... a glitch."),
    dict(shot="history_O", s="O", t="Brad. Who exactly came up with this idea?", e={"O": "angry"}, p={"O": "point"}, cam="close",
         say="[slow, cold] Brad. Who exactly came up with this idea?", gap=0.8),
]
