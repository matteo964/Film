"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="D", t="Phones away, everyone. Nobody leaves this meeting until the deal is signed.", e={"D": "smug"},
         sfx=[("ding", 0.2), ("ding", 1.2), ("ding", 2.2), ("ding", 3.2)],
         say="[strict] Phones away, everyone. Nobody leaves this meeting until the deal is signed."),
    dict(s="E", t="My water just broke. Come now.", say="[reading, panicking whisper] 'My water just broke... COME NOW.'", gap=0.3),
    dict(shot="meet_DET", s="E", t="Doug. I'm sorry. My wife just went into labor. I have to go.", e={"E": "worried", "D": "annoyed", "T": "neutral"},
         p={"E": "phone", "D": "cross", "T": "idle"}, prop={"E": "phone"}),
    dict(s="D", t="Sit down, Ethan. We're in the middle of the biggest deal of the year.", e={"D": "annoyed"}, p={"D": "point"}),
    dict(shot="meet_E", s="E", t="Doug, she's having our baby. Right now.", e={"E": "shocked"}, p={"E": "chest"}, prop={"E": None},
         say="[desperate] Doug, she's having our BABY. Right now."),
    dict(shot="meet_D", s="D", t="Babies take hours. Sometimes days. This deal takes ninety minutes.", e={"D": "smug"}, p={"D": "explain"},
         say="[dismissive] Babies take hours. Sometimes days. This deal takes ninety minutes."),
    dict(s="D", t="Your wife will understand. Priorities, Ethan.", e={"D": "smug"}, p={"D": "shrug"}),
    dict(shot="meet_E", s="E", t="You're right. Priorities.", e={"E": "calm"}, p={"E": "idle"}, say="[quiet, decided] You're right. Priorities."),
    dict(shot="meet_D", s="D", t="Good man. Now sit down.", e={"D": "happy"}, p={"D": "point"}),
    dict(shot="meet_DE", s="E", t="I'm leaving.", e={"E": "angry", "D": "shocked"}, p={"E": "stop", "D": "idle"}, punch=True),
    dict(s="D", t="If you walk out that door, don't bother coming back on Monday!", e={"D": "angry"}, p={"D": "point"},
         say="[shouting] If you walk out that door, don't bother coming back on Monday!"),
    dict(s="E", t="Then I won't. My family comes first.", e={"E": "calm"}, p={"E": "idle"}, cam="med", gap=0.5),
    dict(shot="meet_DT", s="D", t="Sorry about that, Mrs. Tanaka. Some people just aren't committed.", e={"D": "smug", "T": "annoyed"},
         p={"D": "shrug", "T": "cross"}, say="[fake apologetic] Sorry about that, Mrs. Tanaka. Some people just aren't committed."),
    dict(shot="meet_T", s="T", t="Doug. Read the screen behind you.", e={"T": "angry"}, p={"T": "point"}, look={"T": "up"}, cam="close",
         say="[cold, slow] Doug. Read the screen behind you.", gap=0.8),
]
