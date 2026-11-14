"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="L", t="Wait. Tyler makes how much?", e={"L": "shocked"}, sfx=[("whoosh", 0.1)],
         say="[stunned whisper] Wait... Tyler makes HOW much?"),
    dict(s="L", t="A hundred and twelve thousand. He started three weeks ago.", say="[disbelief] A hundred and twelve thousand. He started three weeks ago."),
    dict(s="L", t="I trained him. Last month. I've been here eight years.", say="[hurt, quiet] I trained him. Last month. I've been here eight years."),
    dict(s="L", t="And I make sixty one.", say="[angry whisper] And I make sixty-one.", gap=0.4),
    dict(shot="printer_LR", s="R", t="Lena? You okay? You look like you saw a ghost.", e={"R": "worried", "L": "angry"},
         p={"R": "explain", "L": "paper"}, prop={"L": "paper:$112K"}),
    dict(s="L", t="Raj. How much do you make?", e={"L": "neutral"}, say="[serious] Raj. How much do you make?"),
    dict(s="R", t="Sixty four. Why?", e={"R": "confused"}, p={"R": "shrug"}),
    dict(s="R", t="I asked for a raise last year. Darren said there was no budget.", e={"R": "annoyed"}, p={"R": "cross"}),
    dict(s="L", t="Funny. He found a hundred and twelve thousand for Tyler.", e={"L": "angry"}, say="[bitter] Funny. He found a hundred and twelve thousand for Tyler."),
    dict(s="L", t="Because the new guy makes almost double.", e={"L": "angry"}, p={"L": "point"}, cam="med", gap=0.4),
    dict(shot="office_DL", s="L", t="Darren, why does Tyler make fifty thousand more than me? I trained him.", e={"L": "angry", "D": "annoyed"},
         p={"L": "paper", "D": "desk"}),
    dict(shot="office_D", s="D", t="Where did you get that? Salaries are strictly confidential.", e={"D": "angry"}, p={"D": "desk_point"}),
    dict(shot="office_L", s="L", t="It was on the printer. Now answer the question.", e={"L": "annoyed"}, prop={"L": None}, p={"L": "cross"}),
    dict(shot="office_D", s="D", t="Tyler negotiated. You didn't. And you're already at the top of your pay band.", e={"D": "smug"},
         p={"D": "desk_explain"}),
    dict(s="D", t="One more word about salaries, and you're fired. Discussing pay is against company policy.", e={"D": "angry"},
         p={"D": "desk_lean"}, cam="med", say="[threatening] One more word about salaries, and you're fired. Discussing pay is against company policy."),
    dict(shot="office_L", s="L", t="Actually, Darren, it's illegal to stop us from talking about our pay.", e={"L": "smug"}, p={"L": "explain"}),
    dict(shot="office_D", s="D", t="Nobody in this office is going to talk about their salary.", e={"D": "smug"}, p={"D": "desk"},
         say="[confident] Nobody in this office is going to talk about their salary."),
    dict(shot="wb1_L", s="L", t="Then I'll go first. Who's next?", e={"L": "smug"}, p={"L": "write"}, prop={"L": "chalk"}, cam="close",
         say="[calm, defiant] Then I'll go first. Who's next?", gap=0.8),
]
