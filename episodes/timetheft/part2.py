"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_T", s="T", t="Managers? Why would they track managers?", e={"T": "shocked", "N": "smug", "L": "neutral"}, p={"T": "desk_lean"},
         say="[panicking] Managers? Why would they track MANAGERS?"),
    dict(shot="office_N", s="N", t="WorkWatch doesn't lie, Trent. It sees everything.", e={"N": "smug"}, cam="med",
         say="[sweetly] WorkWatch doesn't lie, Trent. It sees everything.", gap=0.4),
    dict(shot="open_TL", s="T", t="Leo. Hypothetically. How would someone make WorkWatch think they're working?", e={"T": "worried", "L": "confused"},
         p={"T": "explain", "L": "idle"}, say="[whispering] Leo. Hypothetically. How would someone make WorkWatch think they're working?"),
    dict(s="L", t="Hypothetically? A mouse jiggler. It moves your mouse all day. Twenty bucks online.", e={"L": "smug"}, p={"L": "shrug"}),
    dict(shot="open_T", s="T", t="Interesting. No reason. Just curious.", e={"T": "smug"}, p={"T": "hips"}, say="[too casual] Interesting. No reason. Just curious.",
         gap=0.4),
    dict(shot="jiggle", s="L", t="Nora. Come look at Trent's desk.", e={"L": "confused"}, sfx=[("ding", 0.0)]),
    dict(shot="jiggle_NL", s="L", t="His chair has been empty since twelve thirty. But his mouse is still moving.", e={"L": "smug", "N": "neutral"},
         p={"L": "point", "N": "idle"}),
    dict(s="N", t="And his report says the letter A. Over and over.", e={"N": "smug"}, p={"N": "point"}, look={"N": "away"},
         say="[reading, amused] And his report says... the letter A. Over and over."),
    dict(s="L", t="He left a sticky note. Tee time. One p.m.", e={"L": "smug"}, say="[laughing] He left a sticky note. Tee time. One p.m."),
    dict(s="N", t="He's playing golf. On a Wednesday. While WorkWatch says he's one hundred percent active.", e={"N": "angry"}, p={"N": "cross"}),
    dict(shot="trent_dash", s="L", t="One hundred percent active. Not a single second idle.", e={"L": "smug"}, sfx=[("ding", 0.0)],
         say="[mocking] One hundred percent active. Not a single second idle."),
    dict(s="N", t="Friday is going to be very interesting.", e={"N": "smug"}, say="[quietly] Friday is going to be very interesting."),
    dict(shot="open_NL", s="L", t="Should we tell him the webcam takes a picture every five minutes?", e={"L": "smug", "N": "smug"}, p={"L": "explain", "N": "cross"}),
    dict(s="N", t="No. Let it be a surprise.", e={"N": "smug"}, cam="close", say="[mischievous] No. Let it be a surprise.", gap=0.8),
]
