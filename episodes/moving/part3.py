"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="house_P", s="P", t="Craig. Is this your house?", e={"P": "angry", "C": "worried", "R": "smug", "K": "smug"}, p={"P": "point"},
         say="[slow, cold] Craig. Is this... your house?"),
    dict(shot="house_CP", s="C", t="Technically? Yes. But we're bonding! Look how bonded they are!", e={"C": "worried"}, p={"C": "explain"},
         say="[desperate] Technically? Yes. But we're bonding! Look how bonded they are!"),
    dict(shot="house_PRK", s="P", t="Rosa, Kai. How did Craig describe today?", e={"P": "neutral", "R": "calm", "K": "smug"}, p={"P": "explain"}),
    dict(s="R", t="Mandatory. Unpaid. Bring gloves. Trust exercises with a piano.", e={"R": "smug"}, p={"R": "explain"}),
    dict(s="K", t="He called it paid in culture.", e={"K": "smug"}, p={"K": "shrug"}, say="[dry] He called it 'paid in culture.'"),
    dict(shot="house_P", s="P", t="Paid in culture. Then let's pay them properly.", e={"P": "smug"}, p={"P": "cross"}),
    dict(s="P", t="Everyone gets paid double for today. And Monday off. Craig's budget.", e={"P": "happy"}, p={"P": "point"}, cam="med"),
    dict(shot="house_CP", s="C", t="My budget? But I'm the manager!", e={"C": "shocked"}, p={"C": "chest"}, punch=True,
         say="[outraged] MY budget? But I'm the manager!"),
    dict(s="P", t="Not of a moving company, Craig. You used your team as free movers. That's over.", e={"P": "angry"}, p={"P": "point"}),
    dict(shot="house_PRK", s="P", t="Rosa, I'd like you to run the team from Monday. Tuesday, actually.", e={"P": "happy", "R": "happy"}, p={"P": "explain"},
         say="[warm] Rosa, I'd like you to run the team from Monday. Tuesday, actually."),
    dict(s="R", t="I'd love that. Thank you, Mr. Patel.", e={"R": "happy"}, p={"R": "chest"}),
    dict(s="P", t="Now, who wants pizza? It's on me.", e={"P": "happy"}, p={"P": "shrug"}, say="[cheerful] Now, who wants pizza? It's on me.", gap=0.4),
    dict(shot="end", s="C", t="Hey! Can someone help me with this couch?", e={"C": "worried", "R": "smug"}, p={"R": "mug"}, prop={"R": "mug"},
         say="[straining, desperate] Hey! Can someone help me with this couch?"),
    dict(s="R", t="Sorry, Craig. We're on break. Lift with your legs.", e={"R": "smug"}, cam="med",
         say="[sweetly, sipping] Sorry, Craig. We're on break. Lift with your legs.", gap=0.8),
]
