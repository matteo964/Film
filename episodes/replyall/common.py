"""Gemeinsame Besetzung/Sets: "Your boss accidentally hits Reply All"."""
import backgrounds as bgm
import backgrounds_v2 as B
import explainer_kit as K
import mailui as MU
from backgrounds import rgb
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss accidentally", "hits Reply All"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
MARTIN = Look(shirt=(0.45, 0.15, 0.20), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="sidepart", hair_color=(0.30, 0.20, 0.12),
              outfit="suit", tie_color=(0.15, 0.15, 0.20), shoes=True)
SOFIA = Look(shirt=(0.20, 0.55, 0.60), skin=(0.62, 0.45, 0.33), iris=(0.22, 0.14, 0.08), hair="curly", hair_color=(0.06, 0.05, 0.05),
             outfit="blouse", shoes=True, lashes=True)
BRENNAN = Look(shirt=(0.12, 0.14, 0.22), skin=SKIN, iris=(0.30, 0.45, 0.65), hair="updo", hair_color=(0.92, 0.90, 0.85),
               outfit="suit", tie_color=(0.70, 0.12, 0.20), shoes=True, lashes=True, glasses=True)
JAMAL = Look(shirt=(0.95, 0.75, 0.25), skin=(0.42, 0.29, 0.21), iris=(0.2, 0.12, 0.08), hair="spiky", hair_color=(0.06, 0.05, 0.05),
             outfit="hoodie", shoes=True)

CHARS = {
    "M": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB", look=MARTIN),   # Adam
    "S": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=SOFIA),                   # Jessica
    "B": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX", look=BRENNAN),            # Matilda
    "J": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=JAMAL),                # Will
    "K": dict(voice="en-US-SteffanNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=JAMAL),               # Liam (nur Telefon)
}

BODY = ("Greg,\nBetween us: the team-building retreat is just so I can pick who to lay off. "
        "And I'm presenting Sofia's Q3 project as mine in my promotion review.\nLOL. These people will believe anything.\n- Martin")
TO_GREG = "Greg Hall"
TO_ALL = "All Staff (312); Greg Hall"
SUBJ = "RE: Company Picnic Sign-up"


def lt():
    return bgm.CLOCK["lt"]


def sc_typing(cr, t):
    MU.compose(cr, TO_GREG, SUBJ, BODY, typed=lt() / 9.0)


def sc_replyall(cr, t):
    hover = lt() > 0.8
    MU.compose(cr, TO_ALL if lt() > 1.6 else TO_GREG, SUBJ, BODY, typed=1.0, hover_reply_all=hover)


def sc_send(cr, t):
    MU.compose(cr, TO_ALL, SUBJ, BODY, typed=1.0, highlight_to=True, sent=lt() > 1.2)


REPLIES_1 = [("Jamal Owens", "RE: RE: Company Picnic Sign-up", "...did you mean to send this to everyone?", False),
             ("Lisa (Accounting)", "RE: RE: Company Picnic Sign-up", "Lay off WHO?", True),
             ("Kevin (IT)", "RE: RE: Company Picnic Sign-up", "screenshot taken", False),
             ("Priya (Sales)", "RE: RE: Company Picnic Sign-up", "Sofia's project?? wow", True)]
REPLIES_2 = [("Martin Reed", "Please disregard previous email", "My account was hacked.", False),
             ("Tom (Design)", "RE: Please disregard", "hacked by who? your honesty?", True),
             ("Anna (HR)", "RE: Please disregard", "HR would like a word, Martin.", True),
             ("Dave (Ops)", "RE: RE: RE: Picnic", "please remove me from this list", False),
             ("Sofia Ramos", "RE: Q3 Project", "Attached: Q3_Plan_v1 – created by Sofia Ramos, Aug 2", True),
             ("Lisa (Accounting)", "RE: RE: RE: Picnic", "reply all is undefeated", False),
             ("Victoria Brennan (CEO)", "Martin.", "My office. Now.", True)]
REPLIES_END = [("Martin Reed", "Goodbye, team", "Greg, honestly this company never deserved me...", True),
               ("Jamal Owens", "RE: Goodbye, team", "HE DID IT AGAIN", True),
               ("Lisa (Accounting)", "RE: Goodbye, team", "legend", False)]


def sc_inbox1(cr, t):
    MU.inbox(cr, REPLIES_1, start=0.3, per=0.9)


def sc_recall(cr, t):
    MU.inbox(cr, REPLIES_1, start=-10)
    if lt() > 0.8:
        MU.dialog(cr, "RECALL FAILED", ["287 recipients have already", "read this message."])


def sc_inbox2(cr, t):
    MU.inbox(cr, REPLIES_2, start=0.2, per=1.1, counter_label=("replies", 21))


def sc_inbox_end(cr, t):
    MU.inbox(cr, REPLIES_END, start=0.4, per=1.0)


def ding_all(cr, t):
    l = lt()
    for k, (x, y) in enumerate(((200, 900), (520, 840), (860, 920))):
        if l > 0.4 + k * 0.35:
            K.label(cr, "ding!", x, y, 44, (1, 1, 1), (0.06, 0.42, 0.74, 0.9))


BG = {"office": B.boss_office, "open": B.open_office, "mail": K.BGS["dark"]}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, front=None, opts=None, after=None):
    d = dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))
    if after:
        d["front"] = after
    return d


def two(b, left, right, after=None):
    d = dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])
    if after:
        d["front"] = after
    return d


def martin_desk():
    return dict(bg="open", layers=[("char", "M", 330, Y1, S1, 1), ("fn", lambda cr: B.work_desk(cr, True))])


SHOTS = {
    "desk_M": martin_desk(),
    "mail_typing": dict(bg="mail", overlays=[sc_typing], layers=[]),
    "mail_replyall": dict(bg="mail", overlays=[sc_replyall], layers=[]),
    "mail_send": dict(bg="mail", overlays=[sc_send], layers=[]),
    "open_SJ": two("open", "J", "S", after=[ding_all]),
    "open_S": one("open", "S", 560, -1),
    "open_J": one("open", "J", 480, 1),
    "open_M": one("open", "M", 540, 1),
    "open_MS": two("open", "M", "S"),
    "open_SJ_plain": two("open", "J", "S"),
    "inbox1": dict(bg="mail", overlays=[sc_inbox1], layers=[]),
    "recall": dict(bg="mail", overlays=[sc_recall], layers=[]),
    "inbox2": dict(bg="mail", overlays=[sc_inbox2], layers=[]),
    "inbox_end": dict(bg="mail", overlays=[sc_inbox_end], layers=[]),
    "ceo_B": one("office", "B", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "ceo_M": one("office", "M", 600, -1),
    "ceo_S": one("office", "S", 600, -1),
    "ceo_BM": dict(bg="office", layers=[("char", "B", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                        ("char", "M", 820, 1760, 1.0, -1)]),
    "ceo_BMS": dict(bg="office", layers=[("char", "B", 230, 1720, 0.9, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                         ("char", "M", 640, 1760, 0.9, -1), ("char", "S", 900, 1760, 0.9, -1)]),
}
