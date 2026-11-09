"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="profile_RJ", s="R", t="Jake! Grab the phone. We're going viral today.", e={"R": "happy", "J": "neutral"},
         p={"R": "point", "J": "film"}, prop={"J": "phone"}),
    dict(s="J", t="Sir, are you sure? Chloe usually plans these for a week.", e={"J": "worried"}),
    dict(s="R", t="Chloe is gone. Now we do it my way. Are we rolling?", e={"R": "smug"}, p={"R": "hips"}),
    dict(s="J", t="Rolling.", e={"J": "neutral"}, gap=0.3),
    dict(shot="profile_R", s="R", t="Hello young people! Buy coffee! It's lit! No cap!", e={"R": "happy"},
         p={"R": ["dance1", "dance2", "dance3", "dance2"]}, rate=0.35,
         say="[awkwardly enthusiastic] Hello young people! Buy coffee! It's lit! No cap!"),
    dict(s="R", t="Boom. Post it. That's how it's done.", e={"R": "smug"}, p={"R": "cross"}, gap=0.5),
    dict(shot="flop_RJ", beat=1.2, sfx=[("whoosh", 0.0)], e={"J": "worried", "R": "smug"}, look={"J": "up"}),
    dict(s="J", t="Uh, sir? It has twelve likes.", e={"J": "worried"}, look={"J": None}),
    dict(s="R", t="Twelve? Give it a minute. The algorithm needs time.", e={"R": "confused"}, p={"R": "shrug"}),
    dict(s="J", t="And three thousand comments. Who is this guy? Where is Chloe?", e={"J": "worried"},
         look={"J": "up"}, say="[reading awkwardly] And three thousand comments. Who is this guy? Where is Chloe?"),
    dict(s="J", t="My grandpa dances better.", look={"J": "up"}, say="[trying not to laugh] My grandpa dances better."),
    dict(s="R", t="Delete that one!", e={"R": "angry"}, p={"R": "point"}, look={"J": None},
         say="[angry] Delete that one!"),
    dict(s="J", t="We also lost seven hundred thousand followers.", e={"J": "shocked"}, punch=True),
    dict(s="R", t="Seven hundred thousand?", e={"R": "shocked"}, p={"R": "head"}, cam="med", gap=0.4),
    dict(shot="flop_RPJ", s="P", t="Rick. Grace Park from Sprinto. We saw your video.",
         e={"P": "annoyed", "R": "happy", "J": "worried"}, p={"P": "cross", "R": "idle", "J": "idle"}, prop={"J": None}),
    dict(s="R", t="Great, right? I'm a natural.", e={"R": "smug"}, p={"R": "chest"}),
    dict(s="P", t="Where is Chloe?", e={"P": "neutral"}),
    dict(s="R", t="Let her go. Cost cutting. Now you get me!", e={"R": "happy"}, p={"R": "shrug"}),
    dict(shot="flop_RP", s="P", t="Then we have a problem. Page four of our contract. The key talent clause.",
         e={"P": "annoyed"}, p={"P": "explain"}),
    dict(s="R", t="Key what?", e={"R": "confused"}, cam="med"),
    dict(s="P", t="Our campaign only runs with Chloe as creative lead. No Chloe, no campaign.", e={"P": "angry"},
         p={"P": "point"}),
    dict(s="P", t="And you return our two hundred thousand dollar advance. By Friday.", p={"P": "cross"}),
    dict(s="R", t="Two hundred thousand?", e={"R": "shocked"}, p={"R": "panic"}, punch=True,
         say="[panicking] Two HUNDRED thousand?"),
    dict(shot="chloe_RJ", s="J", t="Uh, sir? Chloe just posted a video. It has five million views.",
         e={"J": "shocked", "R": "shocked"}, p={"J": "point", "R": "idle"}, look={"J": "up", "R": "up"}),
    dict(s="J", t="And the top comment says, boycott Bean and Co until Chloe is back.", look={"J": "up"}),
    dict(s="R", t="Five million?", e={"R": "shocked"}, look={"R": None}, cam="close", punch=True,
         say="[stunned] Five... MILLION?", gap=0.8),
]
