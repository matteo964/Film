"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="conf_DM", s="D", t="Okay, everything has to be perfect. The owner walks in at ten.",
         e={"D": "neutral", "M": "neutral"}, p={"D": ["explain", "hips"], "M": "idle"}),
    dict(s="M", t="The slides are ready. I worked on them all night.", e={"M": "happy"}, p={"M": "explain"}),
    dict(s="D", t="Great. I'll tell him I made them.", e={"D": "smug"}, p={"D": "cross"}),
    dict(s="M", t="You'll what?", e={"M": "shocked"}, p={"M": "chest"}, punch=True),
    dict(s="D", t="Relax. Interns don't get credit. That's how business works.", p={"D": "shrug"}, cam="med"),
    dict(s="M", t="But that's not fair.", e={"M": "sad"}, p={"M": "idle"}),
    dict(s="D", t="Neither is life. Now go get me a coffee.", e={"D": "annoyed"}, p={"D": "point"}, gap=0.35),

    dict(shot="conf_DW", s="D", t="Oh, you have got to be kidding me. What are you doing here?",
         e={"D": "angry", "W": "calm"}, p={"D": "hips", "W": "mop"}, prop={"W": "mop"}),
    dict(s="W", t="Good morning. I was told to be in this room at ten."),
    dict(s="D", t="By who? Your mop?", e={"D": "smug"}, p={"D": "point"}),
    dict(s="D", t="I told you to stay out of sight today.", e={"D": "angry"}, p={"D": ["explain", "hips"]}),
    dict(s="W", t="You did.", e={"W": "neutral"}),
    dict(s="D", t="Then why are you standing in my meeting room?", p={"D": "explain2"}),
    dict(s="W", t="Your meeting room?", e={"W": "smug"}, cam="med"),
    dict(s="D", t="Yes, my meeting room. In one hour, I'm the regional director.", e={"D": "smug"}, p={"D": "chest"}),
    dict(s="W", t="Did you wash the car yet?", e={"W": "calm"}),
    dict(s="D", t="I'm not talking about the car! Get out!", e={"D": "angry"}, p={"D": "point"}, punch=True),

    dict(shot="conf_DWM", s="M", t="Mr. Collins, maybe we should just let him...", e={"M": "worried"},
         p={"M": "explain"}, look={"M": None}),
    dict(s="D", t="Stay out of this!", e={"D": "angry"}, p={"D": "stop"}),
    dict(s="D", t="Walter, last chance. Leave, or I'm calling security.", p={"D": "point"}),
    dict(s="W", t="Go ahead. Call them.", e={"W": "calm"}, p={"W": "mop"}),
    dict(s="D", t="Unbelievable. Security! Get in here!", e={"D": "angry"}, p={"D": "panic"}, gap=0.35),

    dict(shot="conf_DG", s="G", t="Derek. What is all this shouting about?",
         e={"G": "annoyed", "D": "shocked"}, p={"G": "hips", "D": "idle"}),
    dict(s="D", t="Margaret! Thank God. This janitor refuses to leave the meeting room.",
         e={"D": "worried"}, p={"D": ["explain", "point"]}),
    dict(s="G", t="The janitor?", e={"G": "confused"}),
    dict(s="D", t="Yes! And the owner will be here any minute.", p={"D": "panic"}),
    dict(s="G", t="Derek, the owner is already here.", e={"G": "neutral"}, p={"G": "cross"}, cam="med"),
    dict(s="D", t="What? Where? I'll greet him personally.", e={"D": "happy"}, p={"D": "chest"}),
    dict(shot="conf_DGW", s="G", t="Good morning, Mr. Hayes.", e={"G": "happy", "W": "calm", "D": "happy"},
         p={"G": "idle", "W": "mop"}, gap=0.5),
    dict(s="D", t="Mister who?", e={"D": "shocked"}, p={"D": "idle"}, cam="close", punch=True, gap=0.8),
]
