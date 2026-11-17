"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="R", t="Hey! Hey! That's my car! Put it down!", e={"R": "shocked"}, sfx=[("clunk", 0.2), ("alarm", 0.6)],
         say="[screaming, running] Hey! HEY! That's my car! Put it DOWN!"),
    dict(s="A", t="Should've read the sign, Rex.", e={"A": "smug"}, say="[calm, satisfied] Should've read the sign, Rex.", gap=0.3),
    dict(shot="earlier", beat=1.4, sfx=[("whoosh", 0.0)]),
    dict(shot="lot_AB", s="B", t="Employee of the year! And you get your own parking spot right by the entrance. Congrats, Ava!",
         e={"B": "happy", "A": "happy"}, p={"B": "explain", "A": "chest"}),
    dict(s="A", t="Six years of early mornings. Finally worth it.", e={"A": "happy"}, say="[proud] Six years of early mornings. Finally worth it."),
    dict(s="B", t="Uh, Ava? Whose red car is that? In your spot?", e={"B": "confused"}, p={"B": "point"}, look={"B": "away"}),
    dict(shot="lot_AR", s="R", t="Mine. Problem?", e={"R": "smug", "A": "annoyed"}, p={"R": "cross", "A": "idle"}, look={"B": None}),
    dict(s="A", t="Rex, that's my reserved spot. It says employee of the year.", e={"A": "annoyed"}, p={"A": "point"}),
    dict(s="R", t="I'm the boss. Every spot in this parking lot is my spot.", e={"R": "smug"}, p={"R": "chest"},
         say="[arrogant] I'm the boss. Every spot in this parking lot is MY spot."),
    dict(s="A", t="Then why not use the boss spot?", e={"A": "smug"}),
    dict(s="R", t="Too far from the coffee machine.", e={"R": "smug"}, p={"R": "shrug"}, say="[shrugging] Too far from the coffee machine.", gap=0.4),
    dict(shot="rain_A", s="A", t="Day eight. He's in my spot again. And I'm parking at the very back. In the rain.", e={"A": "angry"},
         p={"A": "cross"}, sfx=[("whoosh", 0.0)]),
    dict(shot="lot_R", s="R", t="Nice weather, Ava! Good thing I'm parked right by the door.", e={"R": "happy"}, p={"R": "mug"}, prop={"R": "mug"},
         say="[mocking, cheerful] Nice weather, Ava! Good thing I'm parked right by the door."),
    dict(shot="rain_A", s="A", t="Day nine. Day ten. Day eleven. Same red car. Same smug face.", e={"A": "angry"}, p={"A": "hips"}),
    dict(shot="lot_AR", s="A", t="Rex, the sign says violators get towed.", e={"A": "annoyed", "R": "smug"}, p={"A": "point"}, look={"A": "away"}),
    dict(s="R", t="Nobody tows the boss.", e={"R": "smug"}, p={"R": "cross"}, cam="med", say="[laughs] Nobody tows the boss."),
    dict(shot="lot_A_phone", s="A", t="Hi, Big Mike's Towing? I'd like to report an unauthorized vehicle.", e={"A": "smug"}, p={"A": "phone"},
         prop={"A": "phone"}, cam="close", look={"R": None}, say="[sweetly] Hi, Big Mike's Towing? I'd like to report an unauthorized vehicle.", gap=0.8),
]
