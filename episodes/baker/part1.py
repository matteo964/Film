"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_HR", s="R", t="Mr. Hale, your anniversary cake is ready. Five tiers, gold leaf. Here's the final invoice.",
         e={"R": "happy", "H": "neutral"}, p={"R": "paper", "H": "desk"}, prop={"R": "paper:$2,800"}),
    dict(shot="office_H", s="H", t="Two thousand eight hundred dollars? For flour and sugar?", e={"H": "shocked"}, p={"H": "desk_lean"},
         punch=True, say="[scoffing] Two thousand eight hundred dollars? For flour and SUGAR?"),
    dict(shot="office_R", s="R", t="And three weeks of work. It's the price you agreed to.", e={"R": "calm"}, p={"R": "hips"}, prop={"R": None}),
    dict(shot="office_H", s="H", t="My assistant Chad bakes. He made amazing brownies last Christmas.", e={"H": "smug"}, p={"H": "desk_explain"}),
    dict(shot="office_R", s="R", t="Then why did you order a five tier cake from me?", e={"R": "smug"}, p={"R": "cross"}),
    dict(shot="office_H", s="H", t="Look. Three hundred VIPs will see your cake tonight. Investors. Press.", e={"H": "happy"},
         p={"H": "desk_point"}),
    dict(s="H", t="Think of the exposure.", e={"H": "smug"}, cam="med", say="[smugly] Think of the EXPOSURE."),
    dict(shot="office_R", s="R", t="Exposure doesn't pay for my butter.", e={"R": "annoyed"}),
    dict(shot="office_H", s="H", t="Well, I'm not paying. Just deliver the cake to the gala at eight.", e={"H": "annoyed"}, p={"H": "desk"}),
    dict(shot="office_R", s="R", t="Did you read the contract? The cake is delivered after full payment.", e={"R": "calm"}, p={"R": "explain"}),
    dict(shot="office_H", s="H", t="Then keep your fancy cake. Chad will bake a better one. For free.", e={"H": "smug"}, p={"H": "desk_lean"},
         say="[laughs] Then keep your fancy cake. Chad will bake a better one. For free."),
    dict(shot="office_R", s="R", t="By eight o'clock tonight? Good luck, Chad.", e={"R": "smug"}, cam="close",
         say="[amused] By eight o'clock tonight? Good luck, Chad.", gap=0.4),
    dict(shot="bakery_C", s="C", t="Okay. Five tiers. How hard can it be? I've watched like three baking videos.", e={"C": "happy"},
         p={"C": "hips"}, say="[confident] Okay. Five tiers. How hard can it be? I've watched like three baking videos."),
    dict(s="C", t="Does cake batter need eggs? Or is that just for pancakes?", e={"C": "confused"}, p={"C": "think"},
         say="[genuinely confused] Does cake batter need eggs? Or is that just for pancakes?"),
    dict(s="C", t="You know what? I'll just use extra frosting. Frosting fixes everything.", e={"C": "smug"}, p={"C": "point"}, cam="close",
         say="[proud] You know what? I'll just use extra frosting. Frosting fixes everything.", gap=0.8),
]
