"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_RC", s="R", t="Chloe. Tell me. What exactly do you do all day?", e={"R": "annoyed", "C": "neutral"},
         p={"R": "desk", "C": "idle"}),
    dict(s="C", t="I run our social media. I grew our account to two million followers.", e={"C": "happy"},
         p={"C": "explain"}),
    dict(s="R", t="You make little dancing videos on your phone.", e={"R": "smug"}, p={"R": "desk_explain"},
         say="[mockingly] You make little dancing videos on your phone."),
    dict(s="C", t="Those little videos doubled our sales this year.", e={"C": "annoyed"}, p={"C": "hips"}),
    dict(s="R", t="My grandson says anybody can make videos. So I'm letting you go.", e={"R": "smug"},
         p={"R": "desk_point"}, cam="med"),
    dict(s="C", t="You're firing me? We just signed the biggest sponsorship deal in company history!",
         e={"C": "shocked"}, p={"C": "chest"}, punch=True),
    dict(s="R", t="Exactly. And now I don't have to pay you to film it. I'll make the videos myself.",
         e={"R": "happy"}, p={"R": ["desk_explain", "desk"]}),
    dict(s="C", t="You? You don't even know how to turn on the front camera.", e={"C": "smug"}, p={"C": "cross"},
         say="[laughs] You? You don't even know how to turn on the front camera."),
    dict(s="R", t="How hard can it be? You point the phone, and you dance.", e={"R": "smug"}, p={"R": "desk_lean"},
         cam="med"),
    dict(s="C", t="Have you read the Sprinto contract?", e={"C": "calm"}),
    dict(s="R", t="Contracts are boring. That's why I have lawyers.", e={"R": "annoyed"}, p={"R": "desk"}),
    dict(s="C", t="Page four. You might want to read it.", e={"C": "smug"}, p={"C": "explain2"}, cam="close",
         say="[knowingly] Page four. You might want to read it."),
    dict(s="R", t="Just leave the password on my desk.", e={"R": "annoyed"}, p={"R": "desk_point"}),
    dict(s="C", t="It's on a sticky note. Good luck with the algorithm.", e={"C": "smug"}, p={"C": "idle"}),
    dict(s="R", t="I don't need luck. I have charisma.", e={"R": "smug"}, p={"R": "desk_lean"},
         say="[proudly] I don't need luck. I have CHARISMA."),
    dict(s="C", t="Sure you do, Rick.", e={"C": "smug"}, say="[sarcastically] Sure you do, Rick.", gap=0.5),

    dict(shot="home", beat=1.0, e={"C": "calm"}, p={"C": "lap_phone"}, prop={"C": "phone"}),
    dict(s="C", t="Okay. Phone's recording.", e={"C": "neutral"}, look={"C": "front"}),
    dict(s="C", t="Hi everyone. So, funny story. I just got fired for making my company go viral.",
         e={"C": "smug"}, cam="med", say="[dryly] Hi everyone. So, funny story. I just got fired for making my company go viral."),
    dict(s="C", t="Apparently my boss is going to make the videos himself now.", e={"C": "happy"},
         say="[trying not to laugh] Apparently my boss is going to make the videos himself now."),
    dict(s="C", t="Two million followers. Let's see how long they stay without me.", e={"C": "smug"}, cam="close",
         say="[mischievously] Two million followers. Let's see how long they stay without me.", gap=0.8),
]
