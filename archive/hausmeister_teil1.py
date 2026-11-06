"""POV: Dein Chef feuert den Hausmeister, der das ganze Gebäude am Laufen hält – Teil 1."""
import backgrounds as bg
from stickman import Look

HOOK = ["POV: Dein Chef feuert den Hausmeister,", "der das ganze Gebäude am Laufen hält"]
HOOK_UNTIL = None  # Teil 1: Hook bleibt das ganze Video stehen
GAP = 0.18

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)

CHARS = {
    "B": dict(name="Brandt", voice="de-DE-ConradNeural", rate="-6%", pitch="-3Hz",
              look=Look(shirt=CYAN, belt=True, moustache=True)),
    "K": dict(name="Kessler", voice="de-DE-KillianNeural", rate="+10%", pitch="+2Hz",
              look=Look(shirt=WHITE, tie=True, collar=True)),
    "W": dict(name="Wagner", voice="de-DE-KatjaNeural", rate="+6%",
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
}
K_SCARF = Look(shirt=WHITE, tie=True, collar=True, scarf=True)

BG = {
    "office": lambda: bg.office(False),
    "office_cold": lambda: bg.office(True),
    "cellar": bg.cellar,
    "corridor": bg.corridor,
}

SHOTS = {
    "office": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "K", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "B", 790, 1730, 1.0, -1),
    ]),
    "cellar": dict(bg="cellar", overlays=[bg.cellar_overlay], layers=[]),
    "office_cold": dict(bg="office_cold", overlays=[bg.snow_overlay], layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "K", 300, 1700, 1.0, 1, dict(hide_legs=True, shiver=1.0, look=K_SCARF)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "W", 790, 1730, 1.0, -1, dict(shiver=0.6)),
    ]),
    "corridor": dict(bg="corridor", overlays=[bg.corridor_overlay], layers=[
        ("char", "W", 290, 1730, 1.0, 1),
        ("char", "K", 790, 1730, 1.0, -1, dict(shiver=0.7, look=K_SCARF)),
    ]),
}

# e = Emotionen, p = Posen (Liste = Gesten wechseln beim Sprechen), cam = wide/med/close
SCRIPT = [
    dict(shot="office", s="B", t="Guten Morgen, Herr Kessler. Sie wollten mich sprechen?",
         e={"B": "neutral", "K": "smug"}, p={"B": "idle", "K": "desk"}),
    dict(s="K", t="Ja. Setzen Sie sich gar nicht erst hin. Das dauert nicht lange.", p={"K": ["desk", "desk_explain"]}),
    dict(s="K", t="Wir trennen uns von Ihnen. Mit sofortiger Wirkung.", cam="med", p={"K": "desk_point"}),
    dict(s="B", t="Wie bitte? Nach einunddreißig Jahren? Ohne jede Vorwarnung?", e={"B": "shocked"},
         p={"B": "chest"}, punch=True),
    dict(s="K", t="Das nennt sich Kostenoptimierung.", e={"K": "smug"}, p={"K": "desk"}),
    dict(s="K", t="Sie verdienen mehr als mancher Teamleiter. Und ehrlich gesagt sehe ich Sie nur Kaffee trinken und durch die Flure laufen.",
         p={"K": ["desk_explain", "desk"]}, e={"B": "worried"}),
    dict(s="B", t="Sie glauben, ich laufe nur durch die Flure?", e={"B": "annoyed"}, p={"B": "hips"}),
    dict(s="K", t="Ach, kommen Sie. Mal eine Glühbirne wechseln, mal eine Tür ölen. Das kann doch jeder.",
         p={"K": ["desk_explain", "desk"]}),
    dict(s="B", t="Natürlich. Mehr mache ich ja nicht.", e={"B": "calm"}),
    dict(s="K", t="Außerdem habe ich schon Ersatz. FixIt24. Handwerker per App, rund um die Uhr.",
         p={"K": ["desk_explain", "desk_point"]}, cam="med"),
    dict(s="K", t="Für ein Drittel Ihres Gehalts.", e={"K": "smug"}, p={"K": "desk"}),
    dict(s="B", t="Per App. Und die kennen sich mit unserer Heizungsanlage von neunzehnhundertsiebenundachtzig aus?",
         e={"B": "annoyed"}, p={"B": ["explain", "hips"]}),
    dict(s="K", t="Heizung ist Heizung. Wie schwer kann das schon sein?", p={"K": "desk_lean"}, e={"K": "smug"}),
    dict(s="B", t="Wenn Sie meinen.", e={"B": "calm"}, p={"B": "cross"}, cam="med"),
    dict(s="K", t="Ihr Wartungsplan liegt mir vor. Drei Seiten. Da steht alles drin.", p={"K": ["desk_explain", "desk"]}),
    dict(s="B", t="Drei Seiten. Richtig.", e={"B": "smug"}),
    dict(s="K", t="Sie sind ersetzbar, Herr Brandt.", cam="close", p={"K": "desk_point"}),
    dict(s="B", t="In Ordnung.", e={"B": "calm"}),
    dict(s="K", t="Das war's? Sie wollen nicht mal diskutieren?", e={"K": "confused"}, p={"K": "desk"}),
    dict(s="B", t="Würde es etwas ändern?", p={"B": "hips"}),
    dict(s="K", t="Nicht im Geringsten.", e={"K": "smug"}),
    dict(s="K", t="Wir sparen damit über vierzigtausend Euro im Jahr.", p={"K": ["desk_explain", "desk"]}, e={"K": "happy"}),
    dict(s="B", t="Na dann. Herzlichen Glückwunsch zu den Einsparungen.", e={"B": "smug"}, p={"B": "explain"}),
    dict(s="K", t="Soll das etwa sarkastisch sein?", e={"K": "annoyed"}, cam="med"),
    dict(s="B", t="Keineswegs. Ich wünsche Ihnen nur viel Glück.", e={"B": "calm"}, p={"B": "cross"}),
    dict(s="K", t="Geben Sie einfach Ihren Schlüsselbund ab.", p={"K": "desk_point"}, e={"K": "smug"}),
    dict(s="B", t="Bitte sehr. Siebenundvierzig Schlüssel.", p={"B": "keys"}, prop={"B": "keys"}, e={"B": "calm"},
         sfx=[("ding", 0.0)]),
    dict(s="K", t="Siebenundvierzig? Wofür um alles in der Welt braucht man siebenundvierzig Schlüssel?",
         e={"K": "shocked"}, p={"K": "desk_lean"}, punch=True),
    dict(s="B", t="Das steht bestimmt in der App.", e={"B": "smug"}),
    dict(s="K", t="Und erwarten Sie nicht, dass wir angekrochen kommen, wenn Sie arbeitslos sind.",
         e={"K": "angry"}, p={"K": "desk_point"}, prop={"B": None}),
    dict(s="B", t="Würde mir nicht im Traum einfallen.", e={"B": "calm"}, p={"B": "hips"}),
    dict(s="K", t="Endlich mal jemand, der was von Wirtschaft versteht.", e={"K": "happy"}, p={"K": "desk"}),
    dict(s="B", t="Ach, eine letzte Frage noch.", p={"B": "explain2"}, e={"B": "neutral"}),
    dict(s="B", t="Hat Ihnen jemand gesagt, was man jeden Morgen um sechs Uhr unten am Kessel machen muss?",
         cam="close", p={"B": "think"}),
    dict(s="K", t="Warum sollte mich das interessieren? Dafür haben wir jetzt die App.", e={"K": "annoyed"},
         p={"K": ["desk_explain", "desk"]}),
    dict(s="B", t="Richtig. Die App.", e={"B": "smug"}, p={"B": "cross"}),
    dict(s="K", t="Gibt es ein Problem?", e={"K": "confused"}),
    dict(s="B", t="Nein, nein. Sie haben ja alles, was Sie wollten.", e={"B": "calm"}, p={"B": "shrug"}),
    dict(s="K", t="Gut. Den Ausgang finden Sie ja.", e={"K": "smug"}, p={"K": "desk_point"}),
    dict(s="B", t="Keine Sorge. Ich kenne hier jeden Weg.", e={"B": "smug"}, p={"B": "idle"}, cam="med", gap=0.5),

    # Nächster Morgen: Heizungskeller – Kessel fällt aus
    dict(shot="cellar", beat=3.0, zoom=(1.0, 1.12), sfx=[("clunk", 0.6), ("hiss", 0.9)]),

    dict(shot="office_cold", s="K", t="Frau Doktor Wagner! Ich wollte Ihnen gerade erzählen, wie viel Geld ich der Firma gespart habe.",
         e={"K": "happy", "W": "angry"}, p={"K": ["desk_explain", "desk"], "W": "hips"}),
    dict(s="W", t="Herr Kessler, warum hat es im ganzen Gebäude neun Grad?", cam="med", p={"W": "point"}),
    dict(s="K", t="Neun Grad? Ach, das ist bestimmt nur ein kleiner technischer Fehler.", e={"K": "worried"},
         p={"K": "desk"}),
    dict(s="W", t="Und warum bekomme ich eine Mail, dass Herr Brandt keinen Zugang mehr hat?", p={"W": "cross"}),
    dict(s="K", t="Ach, das. Ich habe eine überflüssige Stelle gestrichen. Riesige Ersparnis.", e={"K": "smug"},
         p={"K": "desk_explain"}),
    dict(s="W", t="Und wer kümmert sich jetzt um die Heizung?", e={"W": "annoyed"}, p={"W": "hips"}),
    dict(s="K", t="FixIt24. Der Techniker ist schon gebucht. Alles unter Kontrolle.", e={"K": "happy"},
         p={"K": ["desk_explain", "desk"]}),
    dict(s="W", t="Und wann kommt er?", e={"W": "neutral"}),
    dict(s="K", t="Das Zeitfenster ist Donnerstag. Zwischen acht und achtzehn Uhr.", e={"K": "neutral"},
         p={"K": "desk"}, look={"K": "down"}),
    dict(s="W", t="Herr Kessler. Heute ist Montag.", e={"W": "angry"}, cam="close", look={"K": None}),
    dict(s="W", t="Die Investoren aus Tokio sind schon im Haus.", p={"W": "point"}, e={"K": "shocked"}, gap=0.5),

    # Flur: Aufzug steckt fest
    dict(shot="corridor", beat=1.6, sfx=[("alarm", 0.0)], e={"W": "shocked", "K": "worried"},
         p={"W": "phone", "K": "idle"}, prop={"W": "phone"}),
    dict(s="W", t="Herr Kessler, wir haben ein ernstes Problem.", e={"W": "worried"}),
    dict(s="K", t="Was denn jetzt noch?", e={"K": "worried"}, p={"K": "shrug"}),
    dict(s="W", t="Der Aufzug mit den Investoren ist gerade zwischen dem dritten und vierten Stock stecken geblieben.",
         cam="med", gap=0.3),
    dict(s="K", t="Oh nein.", e={"K": "shocked"}, p={"K": "panic"}, cam="close", punch=True, gap=0.8),
]
