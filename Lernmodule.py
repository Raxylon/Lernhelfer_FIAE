class LernModul:
    def __init__(self, titel):
        self.titel = titel
        self.inhalte = []  # Liste von (Überschrift, Text)
        self.fragen = []   # Liste von (Frage, Antwortmöglichkeiten, Index der richtigen Antwort)

    def inhalt_hinzufuegen(self, ueberschrift, text):
        self.inhalte.append((ueberschrift, text))

    def frage_hinzufuegen(self, frage, antworten, richtige_antwort):
        self.fragen.append((frage, antworten, richtige_antwort))



def erstelle_agiles_manifest_modul():
    agil_modul = LernModul("Agiles Manifest")

    agil_modul.inhalt_hinzufuegen(
        "Grundlagen des Agilen Manifests",
        ("Das Agile Manifest ist ein Bekenntnis zu Werten und Prinzipien, "
         "die in der agilen Softwareentwicklung den Wandel erleichtern und "
         "den Menschen ins Zentrum stellen. "
         "Es beruht auf vier zentralen Werten:\n"
         "1. Individuen und Interaktionen mehr als Prozesse und Werkzeuge\n"
         "2. Funktionierende Software mehr als umfassende Dokumentation\n"
         "3. Zusammenarbeit mit dem Kunden mehr als Vertragsverhandlung\n"
         "4. Reagieren auf Veränderung mehr als Befolgen eines Plans\n"
         "\nDiese Werte sind nicht ablehnend gegenüber dem, was rechts steht, "
         "sondern betonen, was wertvoller ist.\n"
         "Dazu kommen 12 Prinzipien, die die Umsetzung begleiten.")
    )

    agil_modul.frage_hinzufuegen(
        "Wie viele Werte nennt das Agile Manifest?",
        ["Zwei", "Vier", "Sechs", "Acht"],
        1
    )
    agil_modul.frage_hinzufuegen(
        "Welcher Wert steht im Agilen Manifest an erster Stelle?",
        ["Individuen und Interaktionen", "Prozesse und Werkzeuge",
         "Dokumentation", "Vertragsverhandlung"],
        0
    )
    agil_modul.frage_hinzufuegen(
        "Was wird im Agilen Manifest höher bewertet als Vertragsverhandlung?",
        ["Kundenkommunikation", "Planung", "Vertragsbruch", "Zusammenarbeit mit dem Kunden"],
        3
    )
    agil_modul.frage_hinzufuegen(
        "Was ist laut Agilem Manifest wichtiger als Befolgen eines Plans?",
        ["Reagieren auf Veränderung", "Vertragsabschluss", "Festhalten an Prozessen", "Dokumentation"],
        0
    )

    return agil_modul
