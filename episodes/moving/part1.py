"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="C", t="Lift with your legs, team! This is what synergy looks like!", e={"C": "smug", "R": "annoyed", "K": "annoyed"},
         say="[cheerful, lounging] Lift with your legs, team! This is what synergy looks like!"),
    dict(s="K", t="Rosa. Is this team building? Or are we moving his couch?", e={"K": "annoyed"}, say="[strained, whispering] Rosa. Is this team building... or are we moving his couch?"),
    dict(s="R", t="Look at the mailbox, Kai.", e={"R": "smug"}, say="[through gritted teeth] Look at the mailbox, Kai.", gap=0.3),
    dict(shot="earlier", beat=1.4, sfx=[("whoosh", 0.0)]),
    dict(shot="open_C", s="C", t="Great news, everyone! This Saturday, we have a mandatory team building event!", e={"C": "happy"}, p={"C": "explain2"},
         say="[enthusiastic] Great news, everyone! This Saturday, we have a MANDATORY team building event!"),
    dict(shot="open_RK", s="K", t="Saturday? Is it paid?", e={"K": "confused", "R": "annoyed"}, p={"K": "shrug", "R": "cross"}),
    dict(shot="open_C", s="C", t="It's paid in culture, Kai. Wear sneakers. Bring gloves. And be there at eight a.m. sharp.", e={"C": "smug"},
         p={"C": "point"}),
    dict(shot="open_RK", s="R", t="Gloves? What kind of team building needs gloves?", e={"R": "confused"}, p={"R": "shrug"}),
    dict(shot="open_C", s="C", t="The physical kind. Trust exercises. Heavy lifting. Very bonding.", e={"C": "smug"}, p={"C": "chest"},
         say="[vague, smug] The physical kind. Trust exercises. Heavy lifting. Very bonding.", gap=0.4),
    dict(shot="arrive_RK", s="K", t="This is the address? It's a house. With a moving truck.", e={"K": "confused", "R": "neutral"}, p={"K": "point"},
         look={"K": "away"}),
    dict(s="R", t="And a mailbox that says C. Dunn. As in Craig Dunn.", e={"R": "annoyed"}, p={"R": "point"}),
    dict(shot="house_C", s="C", t="Welcome, team! First exercise. The trust carry. Start with the couch. Then the piano.", e={"C": "happy"},
         p={"C": "point"}, say="[cheerful] Welcome, team! First exercise. The trust carry. Start with the couch. Then the piano."),
    dict(shot="house_R", s="R", t="Craig, is this your new house?", e={"R": "angry"}, p={"R": "cross"}),
    dict(shot="house_C", s="C", t="It's an offsite location. With a very homey vibe.", e={"C": "smug"}, p={"C": "shrug"}),
    dict(shot="house_K", s="K", t="Uh, Rosa? He just posted it on LinkedIn. Proud of my team at our offsite.", e={"K": "shocked"}, p={"K": "phone"},
         prop={"K": "phone"}, look={"K": "down"}),
    dict(s="K", t="And he tagged the CEO. Who just replied. Love this! On my way to join you!", e={"K": "smug"}, cam="close",
         say="[reading, grinning] And he tagged the CEO. Who just replied: 'Love this! On my way to join you!'", gap=0.8),
]
