"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    # Überlappung mit dem Ende von Teil 2
    dict(shot="conf_DGW", s="G", t="Good morning, Mr. Hayes.", e={"G": "happy", "W": "calm", "D": "happy"},
         p={"G": "idle", "W": "mop", "D": "idle"}, prop={"W": "mop"}),
    dict(s="D", t="Mister who?", say="[confused] Mister... who?", e={"D": "shocked"}, cam="close", punch=True),
    dict(shot="conf_DW", s="W", t="Walter Hayes. I own this company.", e={"W": "calm"}, p={"W": "mop"}, cam="med"),
    dict(s="D", t="Ha. That's a good one. Margaret, tell him to stop.", say="[nervous laugh] Ha. That's a good one. Margaret, tell him to stop.", e={"D": "confused"}, p={"D": "shrug"}),
    dict(shot="conf_DG", s="G", t="He's not joking, Derek. Mr. Hayes has owned this company for twelve years.",
         e={"G": "annoyed"}, p={"G": "cross"}),
    dict(s="D", t="But he's the janitor!", say="[panicking] But he's the JANITOR!", e={"D": "shocked"}, p={"D": "panic"}, punch=True),
    dict(shot="conf_DW", s="W", t="One week every quarter, I work a different job in my own company.",
         e={"W": "neutral"}, p={"W": "mop"}),
    dict(s="W", t="You learn a lot about people when they think you're nobody.", e={"W": "calm"}),
    dict(s="W", t="And this week, I learned a lot about you.", e={"W": "annoyed"}, cam="med"),
    dict(s="D", t="Mr. Hayes, sir, I had no idea!", e={"D": "worried"}, p={"D": "pray"}),
    dict(s="W", t="That's exactly the point.", e={"W": "calm"}),
    dict(s="W", t="You made me clean up the coffee you spilled. Because napkins are for people without a janitor.",
         e={"W": "annoyed"}),
    dict(s="W", t="You parked in my spot. And you asked me to wash your car.", e={"W": "smug"}),
    dict(s="D", t="I can explain!", e={"D": "worried"}, p={"D": "stop"}),
    dict(shot="conf_DWM", s="W", t="You told this young woman she'd be an intern forever.",
         e={"W": "annoyed", "M": "sad", "D": "worried"}, p={"M": "idle", "D": "idle"}),
    dict(s="W", t="And you were about to present her work as your own.", look={"W": "away"}),
    dict(s="D", t="That's a misunderstanding!", p={"D": "shrug"}),
    dict(s="M", t="I worked on those slides until three in the morning.", e={"M": "annoyed"}, p={"M": "cross"}),
    dict(shot="conf_MW", s="W", t="I know. I was mopping the hallway outside your office.",
         e={"W": "calm", "M": "neutral"}, look={"W": None}),
    dict(shot="conf_DW", s="D", t="Sir, please. I've worked so hard for that director position.",
         e={"D": "sad"}, p={"D": "pray"}),
    dict(s="W", t="Don't worry. You're getting a new position. Starting today.", e={"W": "smug"}),
    dict(s="D", t="Really?", e={"D": "happy"}, p={"D": "chest"}),
    dict(s="W", t="Facility maintenance. Three months.", e={"W": "calm"}, cam="med"),
    dict(s="D", t="Maintenance? You mean janitor?", say="[horrified] Maintenance? You mean... JANITOR?", e={"D": "shocked"}, p={"D": "head"}),
    dict(s="W", t="It's called learning from the ground up.", say="[smugly] It's called learning from the ground up.", e={"W": "smug"}, p={"W": "keys"},
         prop={"W": None, "D": "mop"}, sfx=[("whoosh", 0.0)]),
    dict(s="D", t="And who gets the director job?", e={"D": "sad"}, p={"D": "mop"}),
    dict(shot="conf_GW", s="W", t="Margaret, prepare an offer for Mia. Full time. And she reports directly to me.",
         e={"W": "happy", "G": "happy"}, p={"W": "explain", "G": "idle"}),
    dict(s="G", t="With pleasure, Mr. Hayes.", p={"G": "chest"}),
    dict(shot="conf_MW", s="M", t="Wait, me? Thank you so much, Mr. Hayes!", e={"M": "happy"}, p={"M": "panic"}),
    dict(s="W", t="Thank you for being kind to a janitor. Most people aren't.", e={"W": "happy"}, p={"W": "idle"}),
    dict(shot="conf_DW", s="W", t="Oh, and Derek? Your car was towed from spot number one.", e={"W": "smug", "D": "sad"}),
    dict(s="D", t="Towed?", say="[shocked] TOWED?", e={"D": "shocked"}, cam="close", punch=True),
    dict(s="W", t="My car is parked there now. You know where the bucket is.", e={"W": "happy"}, p={"W": "hips"}, gap=0.8),
]
