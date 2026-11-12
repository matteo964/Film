"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_RL", s="L", t="Mr. Whitmore, the wedding photos are edited. Four hundred images. Here's the final invoice.",
         e={"L": "happy", "R": "neutral"}, p={"L": "paper", "R": "desk"}, prop={"L": "paper:$3,500"}),
    dict(shot="office_R", s="R", t="Three thousand five hundred dollars? For pictures?", e={"R": "shocked"}, p={"R": "desk_lean"},
         punch=True, say="[scoffing] Three thousand five hundred dollars? For PICTURES?"),
    dict(shot="office_L", s="L", t="That's the price we agreed on. It's in the contract you signed.", e={"L": "calm"}, prop={"L": None},
         p={"L": "hips"}),
    dict(shot="office_R", s="R", t="My nephew Jake has a very good camera. He took photos too. For free.", e={"R": "smug"},
         p={"R": "desk_explain"}),
    dict(shot="office_L", s="L", t="Then why did you hire me?", e={"L": "smug"}, p={"L": "cross"}),
    dict(shot="office_R", s="R", t="Because my wife insisted.", e={"R": "annoyed"}, p={"R": "desk"},
         say="[grumbling] Because my wife insisted."),
    dict(shot="office_L", s="L", t="Smart woman.", e={"L": "smug"}, say="[dryly] Smart woman."),
    dict(shot="office_R", s="R", t="Look. I'm doing you a favor. Two hundred very rich guests will see your work.", e={"R": "happy"},
         p={"R": "desk_point"}),
    dict(s="R", t="Think of the exposure.", e={"R": "smug"}, cam="med", say="[smugly] Think of the EXPOSURE."),
    dict(shot="office_L", s="L", t="Exposure doesn't pay for my camera.", e={"L": "annoyed"}),
    dict(shot="office_R", s="R", t="Well, I'm not paying. Send me the photos for the slideshow tonight.", e={"R": "annoyed"}, p={"R": "desk"}),
    dict(shot="office_L", s="L", t="Did you read section four of the contract?", e={"L": "calm"}, p={"L": "explain"}),
    dict(shot="office_R", s="R", t="I'm a busy man. I don't read contracts.", e={"R": "smug"}, p={"R": "desk_lean"},
         say="[laughs] I'm a busy man. I don't read contracts."),
    dict(shot="office_L", s="L", t="Until the invoice is paid, you get preview images. With a watermark.", e={"L": "smug"}, p={"L": "explain2"}),
    dict(shot="office_R", s="R", t="A tiny little watermark? Nobody will even notice.", e={"R": "smug"}, p={"R": "desk_explain"},
         say="[dismissive] A tiny little watermark? Nobody will even notice."),
    dict(shot="office_L", s="L", t="Oh. They'll notice.", e={"L": "smug"}, cam="close", say="[mischievously] Oh... they'll notice.", gap=0.4),
    dict(shot="home_L", s="L", t="Previews are uploaded. Watermark size. Hmm.", e={"L": "calm"}, p={"L": "type"}, prop={"L": "laptop"},
         look={"L": "down"}, say="[to herself] Previews are uploaded. Watermark size... hmm."),
    dict(s="L", t="Let's go with extra large.", e={"L": "smug"}, look={"L": "front"}, cam="close",
         say="[playful] Let's go with... extra large.", gap=0.8),
]
