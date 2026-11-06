"""Part 1 – The janitor who secretly owns the company."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_DW", s="D", t="Hey! You. Janitor. Get over here.",
         e={"D": "annoyed", "W": "neutral"}, p={"D": "desk_point", "W": "mop"}, prop={"W": "mop"}),
    dict(s="W", t="Good morning, Mr. Collins. Is something wrong?", e={"W": "calm"}),
    dict(s="D", t="Yeah. I spilled my coffee. It's all over the floor. Clean it up.", p={"D": ["desk_explain", "desk"]}),
    dict(s="W", t="You know, there's a napkin right next to your hand.", e={"W": "neutral"}, look={"W": "down"}),
    dict(s="D", t="Napkins are for people who don't have a janitor.", e={"D": "smug"}, p={"D": "desk_lean"},
         look={"W": None}, cam="med"),
    dict(s="W", t="Of course.", p={"W": ["mop2", "mop"]}, e={"W": "calm"}),
    dict(s="D", t="And hurry up. Tomorrow is the biggest day of my career.", p={"D": ["desk_explain", "desk"]}, e={"D": "happy"}),
    dict(s="W", t="Oh? What's happening tomorrow?", p={"W": "mop"}, e={"W": "neutral"}),
    dict(s="D", t="The owner is finally visiting. First time anyone's seen him in twelve years.", e={"D": "smug"}),
    dict(s="D", t="He's picking the new regional director. And trust me, that's gonna be me.",
         p={"D": "desk_point"}, cam="med"),
    dict(s="W", t="Have you ever actually met the owner?", e={"W": "calm"}),
    dict(s="D", t="Nobody has. Some mystery billionaire who bought the company and disappeared.",
         p={"D": ["desk_explain", "desk"]}, e={"D": "neutral"}),
    dict(s="W", t="Maybe he's closer than you think.", e={"W": "smug"}, cam="close"),
    dict(s="D", t="Please. Guys like that don't hang around guys like you.", e={"D": "smug"}, p={"D": "desk_lean"}),
    dict(s="D", t="Which reminds me. Tomorrow, you stay out of sight.", p={"D": "desk_point"}, e={"D": "annoyed"}),
    dict(s="W", t="Out of sight?", e={"W": "confused"}),
    dict(s="D", t="Nobody wants to see a janitor when we're trying to impress a billionaire.",
         p={"D": ["desk_explain", "desk"]}, e={"D": "smug"}),
    dict(s="W", t="I see.", e={"W": "calm"}, gap=0.3),

    dict(shot="office_DWM", s="M", t="Excuse me, Mr. Collins. Here are the reports you asked for.",
         e={"M": "happy", "D": "annoyed"}, p={"M": "explain", "D": "desk"}),
    dict(s="D", t="Finally. Took you long enough.", p={"D": "desk_point"}),
    dict(s="M", t="Oh, Walter, let me help you with that.", look={"M": None}, e={"M": "happy"}, p={"M": "idle"}),
    dict(s="D", t="Don't. You're an intern, not a cleaning lady. Let the help do his job.",
         e={"D": "angry", "M": "worried"}, p={"D": "desk_point"}),
    dict(s="M", t="It's just a little coffee.", e={"M": "sad"}, p={"M": "shrug"}),
    dict(s="D", t="And that's exactly why you'll be an intern forever.", e={"D": "smug"}, p={"D": "desk"}),
    dict(shot="office_DW", s="D", t="Walter, when you're done, wash my car. The black one. Spot number one.",
         p={"D": ["desk_explain", "desk_point"]}),
    dict(s="W", t="Spot number one? I thought that was reserved for the owner.", e={"W": "neutral"}),
    dict(s="D", t="He's never here. Somebody should use it.", e={"D": "smug"}, p={"D": "desk_lean"}),
    dict(s="W", t="Interesting.", e={"W": "smug"}, cam="close"),
    dict(s="D", t="What's interesting?", e={"D": "confused"}),
    dict(s="W", t="Nothing. I'll make sure it's taken care of.", e={"W": "calm"}),
    dict(s="D", t="Good. Now get out. You're making my office smell like floor cleaner.",
         e={"D": "annoyed"}, p={"D": "desk_point"}, gap=0.5),

    # Abends im Penthouse
    dict(shot="penthouse", beat=1.2, prop={"W": "phone"}, p={"W": "lap_phone"}, e={"W": "calm"},
         sfx=[("ding", 0.2)]),
    dict(s="W", t="Margaret, it's me. Change of plans for tomorrow."),
    dict(s="G", t="Mr. Hayes? I thought you were doing your undercover week as a janitor."),
    dict(s="W", t="I was. But I think I've seen enough.", e={"W": "annoyed"}),
    dict(s="W", t="Tell the board I'll be at the meeting tomorrow.", e={"W": "calm"}, cam="med"),
    dict(s="G", t="Should I tell Derek Collins you're coming?"),
    dict(s="W", t="No. Let it be a surprise.", e={"W": "smug"}, cam="close", gap=0.8),
]
