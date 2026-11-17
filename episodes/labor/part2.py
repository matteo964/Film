"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="meet_T", s="T", t="Doug. Read the screen behind you.", e={"T": "angry", "D": "confused"}, p={"T": "point"}, look={"T": "up"},
         say="[cold, slow] Doug. Read the screen behind you."),
    dict(shot="meet_D", s="D", t="Our values. Family first.", e={"D": "worried"}, look={"D": "up"}, say="[reading, uneasy] Our values... Family first."),
    dict(shot="meet_T", s="T", t="That's our company slogan. I chose your firm because I thought you shared it.", e={"T": "annoyed"}, look={"T": None}),
    dict(s="T", t="And you just fired a man for going to the birth of his child.", e={"T": "angry"}, cam="med"),
    dict(shot="meet_D", s="D", t="It's a figure of speech! Family first, business second, I mean, business first!", e={"D": "worried"}, p={"D": "shrug"},
         look={"D": None}, say="[panicking] It's a figure of speech! Family first, business second... I mean, business first!", gap=0.4),
    dict(shot="hall_E", s="E", t="Room twelve. Room twelve. Hang on, Mia. I'm coming.", e={"E": "worried"}, p={"E": "panic"},
         say="[out of breath, running] Room twelve. Room twelve. Hang on, Mia. I'm coming."),
    dict(shot="bed_EW", s="W", t="Ethan! You made it!", e={"W": "happy", "E": "happy"}, p={"W": "lap", "E": "chest"}, say="[exhausted, relieved] Ethan! You made it!"),
    dict(s="E", t="Of course I made it. Nothing was going to stop me.", e={"E": "happy"}, p={"E": "pray"}),
    dict(s="W", t="What about your big meeting?", e={"W": "worried"}),
    dict(s="E", t="I might not have a job anymore. But that's a problem for Monday.", e={"E": "calm"}, p={"E": "shrug"}, sfx=[("ding", 3.4)]),
    dict(shot="fired", s="E", t="Leave equals you're fired. Return your laptop Monday.", e={"E": "annoyed"},
         say="[reading, sighing] 'Leave equals you're fired. Return your laptop Monday.'"),
    dict(shot="bed_EW", s="W", t="Your boss fired you for this?", e={"W": "angry"}),
    dict(s="E", t="He did. And I'd do it again. Every single time.", e={"E": "happy"}, p={"E": "pray"}),
    dict(shot="meet_DT", s="T", t="Doug, we won't be signing today. Or any day.", e={"T": "angry", "D": "shocked"}, p={"T": "cross", "D": "idle"}),
    dict(s="D", t="Wait! Please! What can I do?", e={"D": "worried"}, p={"D": "pray"}, say="[desperate] Wait! Please! What can I do?"),
    dict(shot="meet_T", s="T", t="Tell me which hospital Ethan is at. I'd like to meet the only person at your company who understood our values.",
         e={"T": "smug"}, p={"T": "phone"}, prop={"T": "phone"}, cam="close", gap=0.8),
]
