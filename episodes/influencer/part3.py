"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="cctv2_OBJ", s="B", t="Wait. Am I being arrested?", e={"B": "shocked", "O": "neutral", "J": "calm"},
         p={"B": "chest", "O": "idle", "J": "cross"}, cam="close", punch=True, say="[terrified] Wait... am I being arrested?"),
    dict(s="O", t="Leaving without paying five times is theft of services. So, yes. Unless you pay every restaurant back today.",
         e={"O": "annoyed"}, p={"O": "explain"}),
    dict(s="B", t="Every restaurant? That's like two thousand dollars!", e={"B": "worried"}, p={"B": "panic"},
         say="[panicking] Every restaurant? That's like two THOUSAND dollars!"),
    dict(s="O", t="Two thousand three hundred and twelve. Plus a fine.", e={"O": "smug"}, cam="med"),
    dict(shot="cctv2_B", s="B", t="Hello? Hi, it's Brittany. About our sponsorship deal.", e={"B": "worried"},
         p={"B": "phone"}, prop={"B": "phone"}, say="[nervous] Hello? Hi, it's Brittany. About our sponsorship deal..."),
    dict(s="B", t="What do you mean, you saw the video? Hello? Hello?", e={"B": "shocked"}, cam="med",
         say="[devastated] What do you mean, you saw the video? Hello? Hello?"),
    dict(shot="cctv2_BJ", s="B", t="Okay. Okay. Jess, right? What if I give you a shoutout? Two million followers. Think of the exposure.",
         e={"B": "happy", "J": "calm"}, p={"B": "explain", "J": "cross"}, prop={"B": None},
         say="[fake sweet] Okay. Okay. Jess, right? What if I give you a shoutout? Two million followers. Think of the exposure."),
    dict(s="J", t="I don't need exposure, Brittany. You're the one who just got exposed.", e={"J": "smug"}, cam="med",
         say="[dryly] I don't need exposure, Brittany. You're the one who just got EXPOSED."),
    dict(shot="cctv2_OB", s="O", t="Let's go, ma'am. You can pay at the station.", e={"O": "neutral", "B": "sad"},
         p={"O": "point", "B": "idle"}),
    dict(s="B", t="Can I at least get a to go box?", e={"B": "sad"}, say="[sadly] Can I at least get a to-go box?"),
    dict(shot="cctv2_BJ", s="J", t="Sure. That'll be eighty four fifty. Plus tip.", e={"J": "smug"}, p={"J": "paper"},
         prop={"J": "paper:$84.50"}, say="[sweetly] Sure. That'll be eighty four fifty. Plus tip.", gap=0.5),
    dict(shot="viral_FJ", s="F", t="Jess. I owe you an apology. I chose a stranger's followers over my best employee.",
         e={"F": "sad", "J": "neutral"}, p={"F": "pray", "J": "idle"}, prop={"J": None}),
    dict(s="J", t="You suspended me for doing my job, Frank.", e={"J": "annoyed"}, p={"J": "cross"}),
    dict(s="F", t="I know. Our video of her has twelve million views. We're booked out for three months.", e={"F": "happy"},
         p={"F": "point"}, look={"F": "up"}),
    dict(s="F", t="So I'd like to make you shift manager. With a raise.", e={"F": "happy"}, look={"F": None}, p={"F": "explain"}),
    dict(s="J", t="Shift manager?", e={"J": "shocked"}, punch=True),
    dict(s="F", t="And one new rule. Nobody gets a free meal for having followers.", e={"F": "smug"}, cam="med"),
    dict(s="J", t="Deal. Now, table six needs their check.", e={"J": "happy"}, p={"J": "hips"}, cam="close",
         say="[happily] Deal. Now, table six needs their check.", gap=0.8),
]
