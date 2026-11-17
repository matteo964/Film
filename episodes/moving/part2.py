"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="house_C", s="C", t="The CEO is coming here? Now?", e={"C": "shocked", "R": "smug", "K": "smug"}, p={"C": "head"}, punch=True,
         say="[panicking] The CEO is coming HERE? Now?"),
    dict(s="C", t="Okay. Okay. Everybody act like this is team building. Hide the boxes. Cover the truck!", e={"C": "worried"}, p={"C": "panic"},
         say="[frantic] Okay. Okay. Everybody act like this is team building. Hide the boxes. Cover the truck!"),
    dict(shot="house_CR", s="R", t="So now you admit it's not team building?", e={"R": "smug", "C": "worried"}, p={"R": "cross", "C": "idle"}),
    dict(s="C", t="It is team building! Building my team's ability to move furniture!", e={"C": "worried"}, p={"C": "explain"},
         say="[desperate] It IS team building! Building my team's ability to... move furniture!", gap=0.4),
    dict(shot="carry", s="K", t="This couch weighs more than my car.", e={"K": "worried"}, say="[straining] This couch weighs more than my car."),
    dict(s="R", t="Just keep smiling, Kai. The CEO is almost here.", e={"R": "smug"}, say="[strained, sarcastic] Just keep smiling, Kai. The CEO is almost here.",
         gap=0.4),
    dict(shot="house_K", s="K", t="Craig, should we also hide your name on the mailbox?", e={"K": "smug"}, p={"K": "point"}),
    dict(shot="house_C", s="C", t="No time! Just smile and look bonded!", e={"C": "worried"}, p={"C": "panic"}),
    dict(shot="house_CP", s="P", t="Craig! Love the energy! What's today's exercise?", e={"P": "happy", "C": "worried"}, p={"P": "explain", "C": "idle"},
         say="[enthusiastic] Craig! Love the energy! What's today's exercise?"),
    dict(s="C", t="Mr. Patel! It's called, uh, the box relay. Builds trust. And core strength.", e={"C": "worried"}, p={"C": "shrug"},
         say="[nervous] Mr. Patel! It's called, uh... the box relay. Builds trust. And core strength."),
    dict(s="P", t="Interesting. And whose house is this? The mailbox says C. Dunn.", e={"P": "confused"}, p={"P": "point"}, look={"P": "away"}),
    dict(s="C", t="Coincidence! Very common name.", e={"C": "worried"}, say="[squeaky] Coincidence! Very common name."),
    dict(shot="house_CPM", s="M", t="Craig, sweetie! The movers put your bed in the wrong room again!", e={"M": "happy", "C": "shocked", "P": "smug"},
         p={"M": "explain", "C": "idle", "P": "cross"}, say="[sweet, loud] Craig, sweetie! The movers put your bed in the wrong room again!"),
    dict(s="P", t="The movers?", e={"P": "smug"}, p={"P": "cross"}, look={"P": "away"}),
    dict(shot="house_P", s="P", t="Craig. Is this your house?", e={"P": "angry"}, p={"P": "point"}, cam="close",
         say="[slow, cold] Craig. Is this... your house?", gap=0.8),
]
