"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="none_H", s="H", t="Ladies and gentlemen. Twenty five years of Halcyon. Let's bring out the cake!", e={"H": "happy"},
         p={"H": "explain2"}, say="[proud, loud] Ladies and gentlemen! Twenty five years of Halcyon. Let's bring out the cake!"),
    dict(shot="chad_HC", s="C", t="Ta da! Three tiers. I ran out of time for the other two.", e={"C": "happy", "H": "shocked"},
         p={"C": "explain", "H": "idle"}, sfx=[("ding", 0.0)], say="[proud] Ta-da! Three tiers. I ran out of time for the other two."),
    dict(s="H", t="Why is it leaning?", e={"H": "worried"}, look={"H": "down"}),
    dict(s="C", t="That's a design choice. It's called modern.", e={"C": "smug"}, p={"C": "shrug"}),
    dict(shot="chad_V", s="V", t="Howard. It says happy fifty two.", e={"V": "confused"}, look={"V": "down"},
         say="[dry, British] Howard. It says happy fifty-two."),
    dict(shot="chad_HC", s="C", t="The numbers are artistic too.", e={"C": "worried"}, look={"H": None}),
    dict(s="H", t="Why is the top tier green?", e={"H": "angry"}, p={"H": "point"}),
    dict(s="C", t="I ran out of chocolate. So I used matcha. And a little spinach.", e={"C": "worried"}, p={"C": "shrug"},
         say="[sheepish] I ran out of chocolate. So I used matcha. And a little spinach."),
    dict(shot="collapse_HV", s="V", t="Is it moving?", e={"V": "shocked", "H": "shocked"}, look={"V": "down", "H": "down"},
         sfx=[("whoosh", 1.2), ("clunk", 2.6)], say="[alarmed] Is it... moving?", gap=2.4),
    dict(s="H", t="My cake!", e={"H": "shocked"}, p={"H": "panic"}, punch=True, say="[screaming] My CAKE!"),
    dict(shot="collapse_C", s="C", t="Okay. In my defense, frosting does not fix everything.", e={"C": "sad"}, p={"C": "shrug"},
         look={"C": "down"}, say="[defeated] Okay. In my defense... frosting does not fix everything."),
    dict(shot="collapse_V", s="V", t="I own the Grandview hotel chain. I was going to invest tonight.", e={"V": "annoyed"}, p={"V": "cross"}),
    dict(s="V", t="But if this is how you plan an anniversary, I'm not sure how you run a company.", e={"V": "angry"}, cam="med"),
    dict(shot="collapse_H", s="H", t="Wait! The real cake exists! It's amazing! Five tiers!", e={"H": "worried"}, p={"H": "stop"},
         say="[desperate] Wait! The real cake exists! It's amazing! Five tiers!"),
    dict(shot="collapse_V", s="V", t="Then where is it, Howard?", e={"V": "smug"}, cam="close", say="[cold] Then where is it, Howard?", gap=0.8),
]
