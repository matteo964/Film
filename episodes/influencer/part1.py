"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="menu_BJ", s="J", t="Here's your check. Lobster pasta, wagyu burger, truffle fries and tiramisu.",
         e={"J": "happy", "B": "smug"}, p={"J": "paper", "B": "film"}, prop={"J": "paper:$84.50", "B": "phone"}),
    dict(s="B", t="Excuse me? There was a hair in my pasta.", e={"B": "annoyed"},
         say="[fake disgusted] Excuse me? There was a HAIR in my pasta."),
    dict(s="J", t="You finished the whole plate, ma'am.", e={"J": "confused"}, p={"J": "idle"}, prop={"J": None}),
    dict(s="B", t="Because I was traumatized! I'm not paying for this.", e={"B": "angry"},
         say="[dramatically] Because I was TRAUMATIZED! I'm not paying for this."),
    dict(shot="menu_B_live", s="B", t="Guys, you won't believe this. This disgusting diner served me hair.", e={"B": "sad"},
         p={"B": "film"}, look={"B": "front"}, say="[fake crying, to her phone] Guys, you won't believe this. This disgusting diner served me hair."),
    dict(s="B", t="Comment if you think the waitress should be fired.", e={"B": "smug"}, cam="med"),
    dict(shot="menu_BFJ", s="F", t="Is there a problem here?", e={"F": "worried", "B": "angry", "J": "calm"},
         p={"F": "idle", "J": "cross"}, look={"B": None}),
    dict(s="B", t="Your waitress served me hair, and she was rude about it. I have two million followers.",
         e={"B": "angry"}, p={"B": "point"}, prop={"B": None}),
    dict(s="F", t="Two million? Oh no. Ma'am, I am so sorry. Your meal is on the house.", e={"F": "worried"},
         p={"F": "pray"}, say="[panicking] Two million? Oh no. Ma'am, I am SO sorry. Your meal is on the house."),
    dict(s="B", t="And I want her fired. Right now. Or I post a review that ends this place.", e={"B": "smug"},
         p={"B": "cross"}, cam="med"),
    dict(s="F", t="Jess. Take off your apron. You're suspended.", e={"F": "annoyed", "J": "shocked"}, p={"F": "point"}),
    dict(s="J", t="Frank, she ate every bite. I didn't do anything.", e={"J": "annoyed"}, p={"J": "explain"}),
    dict(s="F", t="She has two million followers, Jess!", e={"F": "angry"}, p={"F": "shrug"},
         say="[stressed] She has two million followers, Jess!"),
    dict(s="J", t="And we have cameras.", e={"J": "smug"}, p={"J": "point"}, look={"J": "up"}, cam="close",
         say="[calmly] And we have cameras."),
    dict(s="B", t="Cameras? Whatever. My followers believe me, not some waitress.", e={"B": "smug"}, p={"B": "film"},
         prop={"B": "phone"}, look={"J": None}, say="[laughs] Cameras? Whatever. My followers believe ME, not some waitress."),
    dict(s="J", t="Frank, put camera three on the big screen.", e={"J": "calm"}, p={"J": "cross"}),
    dict(s="B", t="Go ahead. I'm still live.", e={"B": "smug"}, say="[smugly] Go ahead. I'm still live."),
    dict(s="J", t="Perfect.", e={"J": "smug"}, cam="close", say="[sweetly] Perfect.", gap=0.8),
]
