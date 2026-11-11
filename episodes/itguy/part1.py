"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_V", s="V", t="Noah. Sit down. Let's talk numbers.", e={"V": "smug", "N": "neutral"},
         p={"V": "desk", "N": "idle"}),
    dict(shot="office_N", s="N", t="Sure. What's going on?", e={"N": "calm"}),
    dict(shot="office_V", s="V", t="You cost this company ninety thousand dollars a year.", p={"V": "desk_explain"}),
    dict(shot="office_N", s="N", t="I also keep this company online.", e={"N": "smug"}, p={"N": "cross"}),
    dict(shot="office_V", s="V", t="Not anymore. Meet Kevin. Kevin costs forty.", e={"V": "happy"}, p={"V": "desk_point"},
         say="[proudly] Not anymore. Meet Kevin. Kevin costs forty."),
    dict(shot="office_VNK", s="K", t="Sup.", e={"K": "happy", "N": "confused", "V": "smug"}, p={"K": "stop", "N": "idle"},
         say="[casual] Sup."),
    dict(s="N", t="You're replacing me with Kevin?", e={"N": "shocked"}, p={"N": "shrug"}, punch=True),
    dict(s="V", t="He has a certificate. Online. Took him one weekend.", e={"V": "smug"}, p={"V": "desk_explain"}),
    dict(shot="office_N", s="N", t="I built every single system in this building. The network, the doors, payroll. Everything.",
         e={"N": "annoyed"}, p={"N": "explain"}),
    dict(shot="office_V", s="V", t="And now Kevin runs them. For half the price. That's called smart business.", e={"V": "smug"},
         p={"V": "desk_lean"}),
    dict(shot="office_N", s="N", t="Does Kevin know about the server under my desk?", e={"N": "calm"}),
    dict(shot="office_V", s="V", t="That ugly beige box? I've wanted that junk gone for years.", e={"V": "annoyed"},
         say="[dismissive] That ugly beige box? I've wanted that junk gone for years."),
    dict(shot="office_N", s="N", t="That junk opens every door in this building. And runs the website.", e={"N": "smug"}),
    dict(shot="office_V", s="V", t="Then Kevin will figure it out. Badge on the desk, please.", e={"V": "smug"}, p={"V": "desk_point"}),
    dict(shot="office_VNK", s="N", t="Fine. One free tip, Kevin. The box with the sticker that says do not touch.",
         e={"N": "calm", "K": "neutral"}, p={"N": "explain"}),
    dict(s="N", t="Don't touch it.", e={"N": "smug"}, cam="med", say="[deadpan] Don't touch it."),
    dict(s="K", t="Got it, boss.", e={"K": "happy"}, p={"K": "explain"}),
    dict(s="V", t="He's not your boss anymore, Kevin.", e={"V": "annoyed"}, gap=0.4),
    dict(shot="it_K", s="K", t="Okay. New desk. New job. Now I just need a plug for my gaming monitor.", e={"K": "happy"},
         p={"K": "hips"}, say="[cheerful] Okay. New desk. New job. Now I just need a plug for my gaming monitor."),
    dict(s="K", t="This old box isn't doing anything anyway.", e={"K": "smug"}, p={"K": "point"}, look={"K": "down"}),
    dict(shot="it_K_unplug", s="K", t="There we go.", e={"K": "happy"}, p={"K": "point"}, look={"K": "down"},
         sfx=[("clunk", 1.0), ("alarm", 1.2)], say="[satisfied] There we go...", gap=0.2),
    dict(s="K", t="Wait. Why did the lights just go out?", e={"K": "shocked"}, p={"K": "panic"}, look={"K": "up"}, cam="close",
         say="[nervous] Wait... why did the lights just go out?", gap=0.8),
]
