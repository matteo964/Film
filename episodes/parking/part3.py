"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="empty_RS", s="S", t="Rex? Why is your car leaving without you?", e={"S": "confused", "R": "shocked", "A": "calm"},
         p={"S": "point", "R": "idle"}, say="[confused, polite] Rex? Why is your car leaving without you?"),
    dict(s="R", t="Valet service. Very exclusive. Shall we go inside?", e={"R": "worried"}, p={"R": "shrug"},
         say="[nervous laugh] Valet service. Very exclusive. Shall we go inside?", gap=0.4),
    dict(shot="lobby_RSA", s="S", t="So. Show me the plan you promised.", e={"S": "neutral", "R": "worried", "A": "calm"}, p={"S": "cross", "R": "idle", "A": "idle"}),
    dict(s="R", t="The plan is, uh, in a laptop. Which is currently in a truck. On the highway.", e={"R": "worried"}, p={"R": "explain"},
         say="[sweating] The plan is, uh... in a laptop. Which is currently in a truck. On the highway."),
    dict(shot="lobby_S", s="S", t="I flew here from Tokyo, Rex.", e={"S": "annoyed"}, say="[cold] I flew here from Tokyo, Rex."),
    dict(shot="lobby_R", s="R", t="Ava! You built that plan with me. You must have a copy!", e={"R": "worried"}, p={"R": "pray"},
         say="[desperate whisper] Ava! You built that plan with me. You must have a copy!"),
    dict(shot="lobby_A", s="A", t="With you? I built it alone, Rex. You added your name on the last slide.", e={"A": "smug"}, p={"A": "cross"}),
    dict(s="A", t="But yes. I have a copy.", e={"A": "smug"}, p={"A": "tablet"}, prop={"A": "tablet"}, cam="med"),
    dict(shot="lobby_SA", s="A", t="Mrs. Sato, I'm Ava. I designed this plan. Let me walk you through it.", e={"A": "happy", "S": "neutral"},
         p={"A": "explain", "S": "idle"}),
    dict(s="S", t="Finally. Someone who's prepared.", e={"S": "happy"}, p={"S": "chest"}, say="[relieved] Finally. Someone who's prepared.", gap=0.4),
    dict(s="S", t="Ava, this is excellent. We'll sign. But only if you lead our account.", e={"S": "happy"}, p={"S": "point"}, prop={"A": None}),
    dict(shot="lobby_R", s="R", t="She can't lead the account. I'm the boss!", e={"R": "angry"}, p={"R": "chest"},
         say="[outraged] She can't lead the account. I'M the boss!"),
    dict(shot="lobby_S", s="S", t="A boss who can't find his own presentation? I'll call your CEO about that.", e={"S": "smug"}, p={"S": "phone"},
         prop={"S": "phone"}, cam="med"),
    dict(shot="empty_RA", s="R", t="Ava. Could you at least give me a ride to the tow yard?", e={"R": "sad", "A": "smug"}, p={"R": "pray", "A": "cross"},
         say="[defeated] Ava... could you at least give me a ride to the tow yard?"),
    dict(s="A", t="Sure, Rex. My car's parked right by the entrance.", e={"A": "smug"}, p={"A": "point"}, look={"A": "away"}, cam="close",
         say="[sweetly] Sure, Rex. My car's parked right by the entrance.", gap=0.8),
]
