"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="nephew_E", s="E", t="Dad. Look at me. Did you not pay the photographer?", e={"E": "angry", "R": "worried", "L": "calm"},
         p={"E": "cross", "R": "idle", "L": "lap_phone"}, prop={"L": "phone"}, cam="close",
         say="[slow, furious] Dad. Look at me. Did you not pay the photographer?"),
    dict(shot="nephew_R", s="R", t="Okay. Okay. I'm calling her.", e={"R": "worried"}, p={"R": "phone"}, prop={"R": "phone"},
         say="[panicked] Okay. Okay. I'm calling her."),
    dict(s="R", t="Lily! Hi! It's Richard. Funny story. Your watermark is a little big.", e={"R": "happy"},
         say="[fake cheerful] Lily! Hi! It's Richard. Funny story. Your watermark is a little big."),
    dict(shot="home_L", s="L", t="I told you they'd notice.", e={"L": "smug"}, p={"L": "lap_phone"}, cam="med"),
    dict(shot="nephew_R", s="R", t="Fine. I'll pay the thirty five hundred. Just remove it.", e={"R": "annoyed"}),
    dict(shot="home_L", s="L", t="It's forty five hundred now.", e={"L": "calm"}),
    dict(shot="nephew_R", s="R", t="Forty five hundred? Why?", e={"R": "shocked"}, punch=True, say="[outraged] Forty five HUNDRED? Why?"),
    dict(shot="home_L", s="L", t="Late fee. Rush fee. And a nephew fee for having to look at Jake's photos.", e={"L": "smug"},
         say="[dryly] Late fee. Rush fee. And a nephew fee, for having to look at Jake's photos."),
    dict(shot="nephew_RE", s="E", t="Give me the phone, Dad.", e={"E": "annoyed", "R": "worried"}, p={"E": "stop", "R": "idle"},
         prop={"R": None}),
    dict(s="E", t="Lily, it's Emily. I'm so sorry. I'm sending forty five hundred right now. From my own account.",
         p={"E": "phone"}, prop={"E": "phone"}, e={"E": "sad"}),
    dict(shot="home_L", s="L", t="Thank you, Emily. Congratulations. Check the screen.", e={"L": "happy"}, say="[warmly] Thank you, Emily. Congratulations. Check the screen.",
         gap=0.4),
    dict(shot="final_RES", beat=1.4, sfx=[("ding", 0.2)], e={"E": "happy", "R": "shocked", "S": "happy"},
         p={"E": "idle", "S": "idle"}, prop={"E": None}, look={"R": "up", "E": "up", "S": "up"}),
    dict(s="E", t="It's perfect. They're absolutely perfect.", e={"E": "happy"}, look={"E": None}, p={"E": "chest"},
         say="[emotional] It's perfect. They're absolutely perfect."),
    dict(s="S", t="I'm booking her for my next five weddings. That's real exposure.", e={"S": "happy"}, look={"S": None}, p={"S": "phone"},
         prop={"S": "phone"}),
    dict(shot="final_RJ", s="J", t="Uncle Rich, can I still take photos at the next wedding?", e={"J": "happy", "R": "annoyed"},
         p={"J": "camera_hold", "R": "cross"}, prop={"J": "camera"}, look={"R": None}),
    dict(s="R", t="No, Jake.", e={"R": "angry"}, say="[firmly] No, Jake."),
    dict(shot="final_R", s="R", t="Lily. Can I at least get a discount for all the exposure?", e={"R": "worried"}, p={"R": "phone"},
         prop={"R": "phone"}),
    dict(shot="home_L", s="L", t="Think of the exposure, Richard. Two hundred guests just saw who didn't pay.", e={"L": "smug"},
         cam="close", say="[sweetly] Think of the exposure, Richard. Two hundred guests just saw who didn't pay.", gap=0.8),
]
