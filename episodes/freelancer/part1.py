"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_GZ", s="Z", t="Here it is, Mr. Grant. Your new website. Finished and ready for launch.",
         e={"Z": "happy", "G": "neutral"}, p={"Z": "tablet", "G": "desk"}, prop={"Z": "tablet"}),
    dict(s="G", t="Wow. That looks fantastic. The investors are going to love this.", e={"G": "happy"},
         p={"G": ["desk_explain", "desk"]}),
    dict(s="Z", t="Great. Then I'll send you the final invoice. Four thousand eight hundred dollars.",
         e={"Z": "calm"}, p={"Z": "explain"}, prop={"Z": None}),
    dict(s="G", t="Four thousand? For a website?", e={"G": "shocked"}, p={"G": "desk_lean"}, punch=True),
    dict(s="Z", t="That's the price we agreed on. It's in the contract.", e={"Z": "neutral"}, p={"Z": "hips"}),
    dict(s="G", t="Yeah, about that. My nephew Tyler says he could've built this in a weekend.",
         e={"G": "smug"}, p={"G": ["desk_explain", "desk"]}),
    dict(s="Z", t="Then why didn't he?", e={"Z": "smug"}, cam="med"),
    dict(s="G", t="Look, I'm doing you a favor here. Think of the exposure.", e={"G": "happy"},
         p={"G": "desk_point"}, say="[cheerfully] Look, I'm doing you a favor here. Think of the EXPOSURE."),
    dict(s="G", t="I'll put your name in the footer. Tiny letters. Very classy.", p={"G": ["desk_explain", "desk"]}),
    dict(s="Z", t="Exposure doesn't pay my rent.", e={"Z": "annoyed"}, p={"Z": "cross"}),
    dict(s="G", t="Neither does arguing with me. We're not paying.", e={"G": "smug"}, p={"G": "desk_lean"}, cam="med"),
    dict(s="Z", t="You did read the contract, right?", e={"Z": "calm"}),
    dict(s="G", t="Contracts are for people who can afford lawyers.", e={"G": "smug"},
         say="[laughs] Contracts are for people who can afford LAWYERS."),
    dict(s="Z", t="Section seven. The website stays my property until the final invoice is paid.",
         e={"Z": "neutral"}, p={"Z": "explain2"}),
    dict(s="G", t="Then sue me.", e={"G": "smug"}, p={"G": "desk_point"}),
    dict(s="Z", t="Oh, I won't need to.", e={"Z": "smug"}, cam="close", say="[mischievously] Oh, I won't need to."),
    dict(s="G", t="What's that supposed to mean?", e={"G": "confused"}, p={"G": "desk"}, gap=0.3),

    dict(shot="office_GZT", s="T", t="Uncle Greg! I copied all her files. We totally don't need her anymore.",
         e={"T": "happy", "Z": "neutral"}, p={"T": "explain", "Z": "cross"}, look={"Z": "away"}),
    dict(s="G", t="See? Tyler's got it covered. He's very good with computers.", e={"G": "happy"},
         p={"G": "desk_point"}),
    dict(s="Z", t="You copied the files. Did you copy the domain too?", e={"Z": "calm"}, look={"Z": None}),
    dict(s="T", t="The what?", e={"T": "confused"}, p={"T": "shrug"}),
    dict(s="Z", t="The domain. The hosting account. The thing that makes the website actually work.",
         p={"Z": ["explain", "cross"]}),
    dict(s="T", t="Uh, yeah. Totally. I copied that too.", e={"T": "worried"}, p={"T": "head"}),
    dict(s="G", t="Goodbye, Zoe. The launch is Friday at ten. With or without you.", e={"G": "annoyed"},
         p={"G": "desk_point"}),
    dict(s="Z", t="Friday at ten. Got it.", e={"Z": "smug"}, p={"Z": "idle"}, gap=0.5),

    dict(shot="apt", beat=1.0, e={"Z": "calm"}, p={"Z": "type"}, prop={"Z": "laptop"}),
    dict(s="Z", t="Invoice number ten forty two. Due Friday, ten a.m.", p={"Z": ["type", "type2"]},
         look={"Z": "down"}),
    dict(s="Z", t="Payment reminder set.", e={"Z": "smug"}, p={"Z": ["type2", "type"]}),
    dict(s="Z", t="And if it's not paid by then?", look={"Z": "front"}, e={"Z": "neutral"}, cam="med"),
    dict(s="Z", t="Well. Let's just say the investors will get a very memorable launch.",
         e={"Z": "smug"}, cam="close", say="[mischievously] Well. Let's just say the investors will get a very memorable launch.",
         gap=0.8),
]
