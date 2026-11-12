"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="history_O", s="O", t="Brad. Who exactly came up with this idea?", e={"O": "angry", "B": "worried", "M": "calm"},
         p={"O": "point", "B": "idle", "M": "idle"}, cam="close", say="[slow, cold] Brad. Who exactly came up with this idea?"),
    dict(shot="history_B", s="B", t="It was a team effort! We're all a family here!", e={"B": "worried"}, p={"B": "shrug"},
         say="[desperate] It was a team effort! We're all a family here!"),
    dict(shot="history_O", s="O", t="You said you had a breakthrough at two a.m.", e={"O": "annoyed"}, p={"O": "cross"}),
    dict(shot="history_O_phone", s="O", t="At two oh four a.m., you posted this. No days off. Grinding.", e={"O": "smug"},
         p={"O": "phone"}, prop={"O": "phone"}, say="[dryly] At two oh four a.m., you posted this. No days off. Grinding."),
    dict(shot="history_B", s="B", t="I was grinding ideas. In my head.", e={"B": "worried"}, say="[weakly] I was grinding... ideas. In my head."),
    dict(shot="history_O", s="O", t="At the gym.", e={"O": "smug"}, prop={"O": None}, p={"O": "cross"}, say="[deadpan] At the gym.", gap=0.4),
    dict(shot="pitch_MO", s="O", t="Mia. Please. Walk us through the real plan.", e={"O": "neutral", "M": "happy"}, p={"O": "explain", "M": "idle"}),
    dict(s="M", t="Of course. We switch three suppliers and merge two warehouses. That alone saves one point eight million.",
         e={"M": "happy"}, p={"M": "point"}, look={"M": "up"}),
    dict(s="M", t="The cost model on page eleven covers the rest. It's unlocked now.", e={"M": "smug"}, look={"M": None}),
    dict(shot="pitch_O", s="O", t="That's the best plan I've seen in ten years.", e={"O": "happy"}, say="[genuinely impressed] That's the best plan I've seen in ten years."),
    dict(shot="approved_MO", beat=1.2, sfx=[("ding", 0.2)], e={"M": "happy", "O": "happy"}, p={"M": "idle", "O": "idle"},
         look={"M": "up", "O": "up"}),
    dict(s="O", t="Mia, you're leading Lighthouse. And you're our new head of operations.", e={"O": "happy"}, look={"O": None, "M": None},
         p={"O": "explain"}),
    dict(s="M", t="Thank you, Mr. Okafor. I won't let you down.", e={"M": "happy"}, p={"M": "chest"}),
    dict(shot="approved_M", s="M", t="And Brad? Next time you copy a file, check the version history first.", e={"M": "smug"},
         p={"M": "point"}, say="[dryly] And Brad? Next time you copy a file, check the version history first."),
    dict(shot="approved_B", s="B", t="And what about me?", e={"B": "worried"}, p={"B": "chest"}),
    dict(shot="approved_O", s="O", t="You'll be on Mia's team, Brad.", e={"O": "smug"}, p={"O": "point"}),
    dict(shot="approved_B", s="B", t="Doing what?", e={"B": "confused"}, p={"B": "shrug"}),
    dict(shot="approved_B", s="B", t="Can I at least keep my parking spot?", e={"B": "sad"}, p={"B": "pray"},
         say="[pleading] Can I at least keep my parking spot?"),
    dict(shot="approved_O", s="O", t="That's Mia's parking spot now.", e={"O": "smug"}, p={"O": "cross"}),
    dict(shot="approved_M", s="M", t="Don't worry, Brad. You can help with the fonts.", e={"M": "smug"}, p={"M": "hips"}, cam="close",
         say="[sweetly] Don't worry, Brad. You can help with the fonts.", gap=0.8),
]
