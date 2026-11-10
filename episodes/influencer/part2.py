"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="menu_BJ", s="B", t="Go ahead. I'm still live.", e={"B": "smug", "J": "calm"}, p={"B": "film", "J": "cross"},
         prop={"B": "phone"}, say="[smugly] Go ahead. I'm still live."),
    dict(s="J", t="Perfect.", e={"J": "smug"}, cam="close", say="[sweetly] Perfect.", gap=0.4),
    dict(shot="cctv_BFJ", s="F", t="Okay. Camera three. Table six. Twelve forty one.", e={"F": "neutral", "B": "smug"},
         p={"F": "explain"}, look={"F": "up", "B": "up", "J": "up"}, sfx=[("ding", 0.0)]),
    dict(s="J", t="Watch her right hand.", e={"J": "calm"}),
    dict(s="F", t="Wait. Is she pulling a hair out of her own head?", e={"F": "shocked"}, p={"F": "point"}, punch=True),
    dict(shot="cctv2_BFJ", s="J", t="And putting it right on her plate.", e={"J": "smug", "B": "shocked"},
         p={"J": "point"}, sfx=[("ding", 0.0)]),
    dict(s="B", t="That's fake! That's AI!", e={"B": "worried"}, p={"B": "stop"}, look={"B": None},
         say="[panicking] That's fake! That's AI!"),
    dict(s="J", t="It's a security camera from two thousand twelve. It can barely do color.", e={"J": "smug"},
         look={"J": None}, say="[dryly] It's a security camera from two thousand twelve. It can barely do color."),
    dict(s="F", t="You planted a hair in your own food to get my waitress fired?", e={"F": "angry"}, p={"F": "point"},
         look={"F": None}),
    dict(s="B", t="It's called content!", e={"B": "annoyed"}, p={"B": "shrug"}, say="[defensive] It's called CONTENT!"),
    dict(s="J", t="And forty eight thousand people just watched you do it. Live.", e={"J": "smug"}, p={"J": "cross"}),
    dict(shot="cctv2_B_live", s="B", t="Guys, don't believe that video. They edited it!", e={"B": "worried"}, p={"B": "film"},
         look={"B": "front"}, say="[desperate, to her phone] Guys, don't believe that video. They edited it!"),
    dict(s="B", t="Why is everyone unfollowing me?", e={"B": "shocked"}, look={"B": "down"}, cam="med",
         say="[shocked] Why is everyone unfollowing me?"),
    dict(shot="cctv2_BFJ", s="F", t="Ma'am, your meal is no longer on the house. That'll be eighty four fifty.",
         e={"F": "annoyed"}, p={"F": "cross"}, look={"B": None}),
    dict(s="B", t="You'll be hearing from my lawyer!", e={"B": "angry"}, p={"B": "point"}, prop={"B": None},
         say="[furious] You'll be hearing from my lawyer!"),
    dict(s="J", t="Great. Because someone else wants to talk to you too.", e={"J": "smug"}, p={"J": "idle"}, gap=0.4),
    dict(shot="cctv2_OBJ", s="O", t="Ma'am. Officer Davis. Are you Brittany Hayes?", e={"O": "neutral", "B": "worried"},
         p={"O": "idle", "B": "idle"}),
    dict(s="B", t="Maybe. Why?", e={"B": "worried"}, p={"B": "shrug"}, say="[nervously] Maybe. Why?"),
    dict(s="O", t="We've had five reports this month. Same woman, same hair, five different restaurants.", e={"O": "annoyed"},
         p={"O": "explain"}),
    dict(s="O", t="And this diner just sent us the video.", e={"O": "neutral"}, p={"O": "point"}, cam="med"),
    dict(s="B", t="Wait. Am I being arrested?", e={"B": "shocked"}, p={"B": "chest"}, cam="close", punch=True,
         say="[terrified] Wait... am I being arrested?", gap=0.8),
]
