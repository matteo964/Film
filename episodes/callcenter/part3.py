"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE, Look, WHITE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

G_HEADSET = Look(shirt=WHITE, tie=True, collar=True, headset=True)
SHOTS["queue_GM_end"] = dict(bg="queue", layers=[("char", "G", L, Y, 1.0, 1, dict(look=G_HEADSET)),
                                                 ("char", "M", R, Y, 1.0, -1)])
SHOTS["queue_G_end"] = dict(bg="queue", layers=[("char", "G", 540, Y, 1.05, 1, dict(look=G_HEADSET))])

SCRIPT = [
    dict(shot="recording_GKM", s="K", t="Linda Holt. Corporate Quality Assurance. I'm a mystery shopper.",
         e={"K": "smug", "G": "happy", "M": "calm"}, p={"K": "idle", "G": "chest", "M": "idle"}, cam="close",
         say="[calmly, professional] Linda Holt. Corporate Quality Assurance. I'm a mystery shopper."),
    dict(s="G", t="A mystery shopper?", e={"G": "shocked"}, p={"G": "head"}, punch=True, say="[stunned] A... mystery shopper?"),
    dict(shot="recording_GK", s="K", t="We test how managers treat their agents when a customer gets nasty.", e={"K": "neutral"},
         p={"K": "explain"}),
    dict(s="K", t="Devin. Put my report on the screen, please.", look={"K": "away"}),
    dict(shot="report_GK", s="K", t="Agent Maya. Calm, professional, followed policy. Ten out of ten.", e={"K": "happy", "G": "worried"},
         look={"K": "up", "G": "up"}, sfx=[("ding", 0.0)]),
    dict(s="K", t="Manager Gary. Didn't listen to the recording. Gave away twelve hundred dollars. Threatened to fire his best agent.",
         e={"K": "annoyed"}),
    dict(s="G", t="I can explain! The customer is always right!", e={"G": "worried"}, p={"G": "pray"}, look={"G": None},
         say="[desperately] I can explain! The customer is always right!"),
    dict(s="K", t="You told Maya nobody listens to recordings.", e={"K": "angry"}, look={"K": None}, p={"K": "point"}),
    dict(s="K", t="Corporate listens to every recording, Gary.", e={"K": "smug"}, cam="med",
         say="[coldly] Corporate listens to EVERY recording, Gary."),
    dict(s="G", t="So, what happens now?", e={"G": "sad"}, p={"G": "idle"}, say="[nervously] So... what happens now?"),
    dict(shot="report_GKM", s="K", t="Maya. Congratulations. You're the new team lead.", e={"K": "happy", "M": "shocked", "G": "shocked"},
         p={"K": "explain", "M": "idle"}),
    dict(s="M", t="Seriously? Thank you so much!", e={"M": "happy"}, p={"M": "panic"}, say="[excited] Seriously? Thank you so much!"),
    dict(shot="report_DM", s="D", t="Let's go, Maya! Team lead!", e={"D": "happy", "M": "happy"}, p={"D": "panic", "M": "idle"},
         say="[cheering] Let's go, Maya! Team lead!"),
    dict(shot="report_GK", s="G", t="And me?", e={"G": "worried"}, p={"G": "chest"}),
    dict(s="K", t="You're going back on the phones. Starting with the angry callers queue.", e={"K": "smug"},
         p={"K": "cross"}),
    dict(s="G", t="The angry callers queue?", e={"G": "shocked"}, p={"G": "head"}, punch=True,
         say="[horrified] The ANGRY callers queue?"),
    dict(s="K", t="Twelve calls waiting.", e={"K": "smug"}, say="[sweetly] Twelve calls waiting.", gap=0.4),
    dict(shot="queue_GM_end", s="M", t="Here you go, Gary. Line four is holding.", e={"M": "smug", "G": "sad"},
         p={"M": "explain", "G": "idle"}),
    dict(s="M", t="And remember. The customer is always right.", e={"M": "smug"}, cam="med",
         say="[playfully] And remember. The customer is ALWAYS right."),
    dict(shot="queue_G_end", s="G", t="Thank you for calling Customer Care, this is Gary.", e={"G": "sad"},
         say="[defeated] Thank you for calling Customer Care, this is Gary."),
    dict(s="K", t="Finally! I've been on hold for forty minutes! Your stupid company charged me twice!", fx="phone",
         e={"G": "shocked"}, p={"G": "head"}, cam="close",
         say="[shouting angrily] Finally! I've been on hold for forty minutes! Your stupid company charged me twice!", gap=0.8),
]
