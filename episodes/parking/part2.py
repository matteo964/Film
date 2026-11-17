"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="tow_AK", s="K", t="Big Mike. You called about a vehicle in a reserved spot?", e={"K": "neutral", "A": "smug"}, p={"K": "hips", "A": "idle"},
         say="[gruff] Big Mike. You called about a vehicle in a reserved spot?"),
    dict(s="A", t="That's my spot. Here's my parking permit. That red car isn't me.", e={"A": "calm"}, p={"A": "paper"}, prop={"A": "paper:PERMIT"}),
    dict(s="K", t="Sign says violators towed. Permit checks out. Say no more.", e={"K": "smug"}, p={"K": "point"}, look={"K": "away"}, prop={"A": None}),
    dict(shot="lobby_RA", s="R", t="Ava, why aren't you at your desk? The Sato Group arrives in twenty minutes.", e={"R": "annoyed", "A": "calm"},
         p={"R": "point", "A": "cross"}),
    dict(s="A", t="Just dealing with a parking issue.", e={"A": "smug"}, say="[innocent] Just dealing with a parking issue."),
    dict(s="R", t="Whatever. My presentation laptop is in my car. I'll grab it in a minute.", e={"R": "smug"}, p={"R": "shrug"}),
    dict(s="A", t="In your car. Okay.", e={"A": "smug"}, cam="med", say="[trying not to smile] In your car. Okay.", gap=0.4),
    dict(shot="towing", beat=2.6, sfx=[("clunk", 1.0), ("whoosh", 1.3)]),
    dict(shot="tow_RK", s="R", t="Hey! What are you doing? That's my car!", e={"R": "shocked", "K": "neutral"}, p={"R": "panic", "K": "cross"},
         say="[screaming] Hey! What are you DOING? That's my car!"),
    dict(s="K", t="Got a permit for this spot, pal?", e={"K": "smug"}),
    dict(s="R", t="I don't need a permit. I'm the boss!", e={"R": "angry"}, p={"R": "chest"}, say="[outraged] I don't need a permit. I'm the BOSS!"),
    dict(shot="tow_K", s="K", t="Sign doesn't say boss. Says employee of the year.", e={"K": "smug"}, p={"K": "point"}, look={"K": "away"},
         say="[deadpan] Sign doesn't say boss. Says employee of the year."),
    dict(shot="tow_R", s="R", t="My laptop is in the trunk! My whole presentation!", e={"R": "worried"}, p={"R": "head"}),
    dict(shot="tow_K", s="K", t="You can pick it up at the tow yard. Forty miles north. Opens Monday.", e={"K": "smug"}, cam="med",
         say="[cheerful] You can pick it up at the tow yard. Forty miles north. Opens Monday."),
    dict(shot="towing", beat=1.2, sfx=[("whoosh", 0.0)]),
    dict(shot="empty_RS", s="S", t="Rex? I'm Mrs. Sato. Why is your car leaving without you?", e={"S": "confused", "R": "shocked"},
         p={"S": "point", "R": "idle"}, cam="close", say="[confused, polite] Rex? I'm Mrs. Sato. Why is your car leaving without you?", gap=0.8),
]
