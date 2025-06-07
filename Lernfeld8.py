import json

def modul_lernen_und_testen2(modulname,modulnummer, lerninhalte, fragen):

    """def lerninhalt():
        with open("lernmodule.json", "r", encoding="utf-8") as f:
             lerninhalt1 = json.load(f)

        for eintrag in lerninhalt1["modul20"]["lerninhalt"]:
            print(eintrag["lerninhalt"])
            input("Drücke Enter für den nächsten Eintrag...\n")

    print(f"\nLERNMODUS - {modulname}\n")
    for abschnitt in lerninhalte:
        print("- " + abschnitt)
        input("\nDrücke Enter, um weiterzulernen...")
    return lerninhalt()

    lernen = lerninhalt()"""


    def lernen():
        try:
            with open("lernmodule.json", "r", encoding="utf-8") as f:
                daten = json.load(f)

            modul_key = f"modul{modulnummer}"

            if modul_key in daten and "lerninhalt" in daten[modul_key]:
                for eintrag in daten[modul_key]["lerninhalt"]:
                    print(eintrag["lerninhalt"])  # ACHTUNG: Key muss exakt so im JSON sein!
                    input("Drücke Enter für den nächsten Eintrag...\n")
            else:
                print(f"Modul {modulnummer} oder 'lerninhalt' nicht in JSON gefunden.")
        except FileNotFoundError:
            print("Datei 'lernmodule.json' wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Fehler beim Einlesen der JSON-Datei.")
        except KeyError as e:
            print(f"Fehlender Schlüssel in JSON: {e}")

    # Lernmodus: Inhalte anzeigen
    print(f"\nLERNMODUS - {modulname}\n")
    for abschnitt in lerninhalte:
        print("- " + abschnitt)
        input("\nDrücke Enter, um weiterzulernen...")

    # Lerneinträge aus Datei anzeigen
    lernen()

    def test():
        print(f"\nTESTMODUS - {modulname}\n")
        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print(f"\n{modulname}")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.") #es ist gerade zu spät zum denken
def modul_lernen_und_testen(modulname, lerninhalte, fragen):
    def lernen():
        print(f"\nLERNMODUS - {modulname}\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print(f"\nTESTMODUS - {modulname}\n")
        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print(f"\n{modulname}")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")
def modul1():
    lerninhalte = [
        "Projekte sind zeitlich begrenzt, haben ein klares Ziel und sind einmalig.\n\
        Projektmanagement umfasst Planung, Überwachung, Steuerung und Abschluss von Projekten.\n\
        Ein Projekt ist ein Balanceakt zwischen Umfang, Zeit und Kosten.\n\
        Projektphasen: Initiierung, Definition, Planung, Ausführung, Abschluss.",
        "Projektkontrolle läuft parallel zu anderen Phasen.\n\
        Im Projektabschluss werden Abschlussbericht erstellt und Ablauf evaluiert.\n\
        Risikoabschätzung und Finanzplanung sind Aufgaben des Projektmanagements."
    ]

    fragen = [
        {
            "frage": "Welche Aussage trifft zu? Ein Projekt...",
            "optionen": ["a) hat keine zeitliche Begrenzung.",
                        "b) ist einmalig und hat ein klares Ziel.",
                        "c) ist immer gleich lang.",
                        "d) ist ein Routinevorgang."],
            "antwort": "b"
        },
        {
            "frage": "Was ist Teil des Projektmanagements?",
            "optionen": ["a) Planung, Überwachung und Steuerung",
                        "b) Nur Planung",
                        "c) Nur Ausführung",
                        "d) Keine der genannten"],
            "antwort": "a"
        },
        {
            "frage": "Welche Phasen gehören zu einem Projekt? (Mehrere Antworten möglich)",
            "optionen": ["a) Initiierung",
                        "b) Planung",
                        "c) Ausführung",
                        "d) Nutzung"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Was gehört zur Projektabschlussphase?",
            "optionen": ["a) Risikoabschätzung",
                        "b) Erstellung eines Abschlussberichts",
                        "c) Teambildung",
                        "d) Evaluierung des Projektablaufs"],
            "antwort": ["b", "d"]
        },
        {
            "frage": "Welche Faktoren beeinflussen sich in einem Projekt gegenseitig?",
            "optionen": ["a) Zeit, Umfang, Kosten",
                        "b) Personal, Räume, Kosten",
                        "c) Technik, Ziel, Qualität",
                        "d) Nur Zeit und Personal"],
            "antwort": "a"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8: modul1 Projektmanagement",lerninhalte,fragen)

def modul2():
    lerninhalte = [
        "Datenquellen sind die verborgenen Quellen, aus denen das Wissen fließt.\n"
        "Sie treten hervor als interne Speicher wie Datenbanken, ERP-Systeme oder Logdateien,\n"
        "doch ebenso als externe Quellen wie APIs, öffentliche Datenportale und soziale Netzwerke.\n"
        "Daten existieren strukturiert (relationale Datenbanken), semi-strukturiert (XML, JSON)\n"
        "und unstrukturiert (Texte, Bilder), jede Form birgt ihre eigene Geheimnisse.\n"
        "Die Qualität der Datenquelle – ihre Aktualität, Genauigkeit, Zuverlässigkeit – bestimmt\n"
        "den Wert des Wissens, das aus ihr geboren wird.",
        "Man unterscheidet:\n"
        "- Primärdaten: direkt und frisch wie das erste Blut, gewonnen durch Umfragen oder Sensoren.\n"
        "- Sekundärdaten: bereits gesammelte Schätze aus Berichten, Marktforschung, Archiven.\n"
        "- Offene Daten (Open Data): frei zugänglich, lizenziert für die breite Welt.\n"
        "- Geschlossene Daten: bewacht und verborgen in den Tiefen des Unternehmens.",
        "Datenquellen sind oft heterogen, verschiedenartig wie Schatten und Licht,\n"
        "und müssen transformiert, vereinigt und gezähmt werden, um in Projekten zu dienen."
    ]

    fragen = [
        {
            "frage": "Nenne drei Arten von Datenquellen.",
            "optionen": ["a) Primärdaten", "b) Sekundärdaten", "c) Offene Daten", "d) Magische Daten"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Was sind strukturierte Datenquellen?",
            "optionen": [
                "a) Datenquellen mit festem Schema, wie relationale Datenbanken",
                "b) Texte und Bilder",
                "c) Soziale Medien",
                "d) Unbekannte Daten"
            ],
            "antwort": "a"
        },
        {
            "frage": "Nenne ein Beispiel für offene Datenquellen.",
            "optionen": [
                "a) Öffentliche APIs",
                "b) Unternehmensinterne Daten",
                "c) Private Briefe",
                "d) Geheimdokumente"
            ],
            "antwort": "a"
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 2: Datenquellen\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 2: Datenquellen\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 2: Datenquellen")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul3():
    lerninhalte = [
        "Agile Vorgehensmodelle ermöglichen flexible und kundennahe Softwareentwicklung.\n\
        Ziel ist es, schneller lauffähige Software zu liefern und Kunden frühzeitig einzubinden.\n\
        Das Agile Manifest (2001) formuliert vier zentrale Werte:",

        "1. Individuen und Interaktionen sind wichtiger als Prozesse und Werkzeuge.\n\
        2. Funktionierende Software ist wichtiger als umfassende Dokumentation.\n\
        3. Zusammenarbeit mit dem Kunden ist wichtiger als Vertragsverhandlungen.\n\
        4. Reagieren auf Veränderung ist wichtiger als das Befolgen eines Plans.",

        "Vorteile agiler Modelle:\n\
        - Höhere Kundenzufriedenheit durch frühes Feedback.\n\
        - Flexibilität bei Änderungen.\n\
        - Regelmäßige Zwischenversionen der Software.\n\
        - Selbstorganisierte Teams fördern Eigenverantwortung.",

        "Nachteile agiler Modelle:\n\
        - Hoher Kommunikationsaufwand durch viele Meetings.\n\
        - Kosten schwer kalkulierbar.\n\
        - Ständiger Kundenkontakt kann herausfordernd sein.\n\
        - Viele Tests können zeit- und kostenintensiv sein.",

        "Vergleich klassisch vs. agil:\n\
        Klassisch: feste Anforderungen, wenig Änderung, große Teams, hierarchisch.\n\
        Agil: Anforderungen entwickeln sich, kleine Teams, flache Hierarchie, iterative Entwicklung."
    ]

    fragen = [
        {
            "frage": "Was ist ein Ziel agiler Vorgehensmodelle?",
            "optionen": ["a) Möglichst wenig Kommunikation mit Kunden",
                         "b) Späte Auslieferung der Software",
                         "c) Frühe lauffähige Software und Kundenfeedback",
                         "d) Feste Abläufe und keine Änderungen"],
            "antwort": "c"
        },
        {
            "frage": "Was steht im Agilen Manifest im Vordergrund?",
            "optionen": ["a) Dokumentation vor funktionierender Software",
                         "b) Planung vor Änderungen",
                         "c) Werkzeuge vor Menschen",
                         "d) Individuen und Interaktionen vor Prozessen und Werkzeugen"],
            "antwort": "d"
        },
        {
            "frage": "Welche Aussage trifft NICHT auf agile Modelle zu?",
            "optionen": ["a) Viel Kommunikation über Stand-up-Meetings",
                         "b) Selbstorganisierte Teams",
                         "c) Hohe Kosten bei späteren Änderungen",
                         "d) Iterative Entwicklung"],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Nachteil agiler Modelle?",
            "optionen": ["a) Kundenkontakt fehlt völlig",
                         "b) Änderungen sind kaum möglich",
                         "c) Hoher Kommunikations- und Testaufwand",
                         "d) Keine frühzeitigen Ergebnisse"],
            "antwort": "c"
        },
        {
            "frage": "Was unterscheidet agile von klassischen Modellen? (Mehrere Antworten möglich)",
            "optionen": ["a) Klassisch: sequenziell, Agil: iterativ",
                         "b) Klassisch: große Teams, Agil: kleine Teams",
                         "c) Klassisch: frühe Ergebnisse, Agil: späte Ergebnisse",
                         "d) Klassisch: Anforderungen fest, Agil: Änderungen eingeplant"],
            "antwort": ["a", "b", "d"]
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 3: Agile Vorgehensmodelle\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 3: Agile Vorgehensmodelle\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 3: Agile Vorgehensmodelle")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul4():
    lerninhalte = [
        "Scrum ist ein agiles Rahmenwerk, ursprünglich für Softwareentwicklung,\n\
        heute breit genutzt in der Produktentwicklung. Es lebt vom Sprint,\n\
        einem festen Rhythmus von 2-4 Wochen, in denen ein fertiges Produktinkrement entsteht.",
        "Rollen in Scrum:\n\
        - Product Owner: Hüter der Anforderungen und des Product Backlogs, Stimme des Kunden.\n\
        - Scrum Master: Wächter des Prozesses, beseitigt Hindernisse und sorgt für Teamfluss.\n\
        - Entwicklungsteam: Selbstorganisierte Fachkräfte, gemeinsam verantwortlich für die Lieferung.",
        "Grundprinzipien von Scrum:\n\
        - Transparency (Transparenz): Alles ist offen und sichtbar.\n\
        - Inspection (Überprüfung): Regelmäßiges Prüfen von Fortschritt und Zusammenarbeit.\n\
        - Adaptation (Anpassung): Lernen aus Feedback, stete Verbesserung.",
        "Scrum-Zeremonien und Prozess:\n\
        - Sprint Planning: Ziele und Aufgaben werden festgelegt.\n\
        - Daily Scrum: Kurzes tägliches Meeting zur Abstimmung.\n\
        - Sprint Review: Vorstellung des Ergebnisses und Feedback.\n\
        - Sprint Retrospektive: Reflexion und Prozessoptimierung.",
        "Wichtige Artefakte:\n\
        - Product Backlog: Priorisierte Liste aller Anforderungen.\n\
        - Sprint Backlog: Aufgaben des aktuellen Sprints.\n\
        - Product Increment: Fertiges Ergebnis mit Mehrwert.\n\
        - Definition of Done: Kriterien für Abschluss.\n\
        - Impediment List: Liste von Hindernissen.",
        "Ergänzende Methoden:\n\
        - Kanban: Visualisierung des Workflows, flexible und kontinuierliche Lieferung.\n\
        - Extreme Programming (XP): Fokus auf technische Exzellenz, z.B. Pair Programming und TDD.",
        "Die agilen Werte sind das Herzstück:\n\
        - Individuen und Interaktionen über Prozesse und Werkzeuge\n\
        - Funktionierende Software über umfassende Dokumentation\n\
        - Zusammenarbeit mit dem Kunden über Vertragsverhandlungen\n\
        - Reagieren auf Veränderung über das Befolgen eines Plans"
    ]

    fragen = [
        {
            "frage": "Welche Rolle ist verantwortlich für das Product Backlog?",
            "optionen": ["a) Scrum Master", "b) Entwicklungsteam", "c) Product Owner", "d) Projektleiter"],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt am besten einen Sprint in Scrum?",
            "optionen": ["a) Ein tägliches Meeting", "b) Ein 2-4 Wochen langer Arbeitsabschnitt",
                         "c) Die gesamte Projektzeit", "d) Ein Prozess zur Fehlerbehebung"],
            "antwort": "b"
        },
        {
            "frage": "Welche Scrum-Zeremonie dient der Reflexion und Verbesserung des Teams?",
            "optionen": ["a) Sprint Review", "b) Sprint Retrospektive", "c) Daily Scrum", "d) Sprint Planning"],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage trifft zu? Das Entwicklungsteam...",
            "optionen": ["a) Hat feste Rollen verteilt",
                         "b) Ist selbstorganisiert und gemeinsam verantwortlich",
                         "c) Wird vom Scrum Master geleitet",
                         "d) Priorisiert die Anforderungen"],
            "antwort": "b"
        },
        {
            "frage": "Welche der folgenden Artefakte gehören zu Scrum? (Mehrere Antworten möglich)",
            "optionen": ["a) Product Backlog", "b) Sprint Backlog", "c) Gantt-Diagramm", "d) Product Increment"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was sind die agilen Werte? (Mehrere Antworten möglich)",
            "optionen": [
                "a) Individuen und Interaktionen über Prozesse und Werkzeuge",
                "b) Dokumentation über funktionierende Software",
                "c) Zusammenarbeit mit dem Kunden über Vertragsverhandlungen",
                "d) Reagieren auf Veränderung über das Befolgen eines Plans"
            ],
            "antwort": ["a", "c", "d"]
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 4: Scrum und agile Vorgehensmodelle\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 4: Scrum und agile Vorgehensmodelle\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 4: Scrum und agile Vorgehensmodelle")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul5():
    lerninhalte = [
        "Datenqualität beschreibt, wie gut Daten den Anforderungen der Nutzer entsprechen.\n\
        Gute Datenqualität ist notwendig für korrekte, zuverlässige und verständliche Informationen.\n\
        Qualitätskriterien sind unter anderem: Korrektheit, Vollständigkeit, Aktualität, Genauigkeit, Konsistenz, Redundanzfreiheit und Verständlichkeit.",
        "Schlechte Datenqualität zeigt sich durch widersprüchliche, fehlerhafte, unvollständige oder veraltete Werte.\n\
        Datenbereinigung beseitigt gefundene Fehler, z. B. durch Korrektur, Löschung oder Ergänzung.\n\
        Monitoring von Daten ist ein kontinuierlicher Prozess zur Qualitätssicherung.\n\
        Daten können sich durch Alterung verschlechtern – regelmäßige Pflege ist notwendig.",
        "Verständlichkeit hängt von der Zielgruppe ab.\n\
        Beispiel: Für Endkunden sollte z. B. ein Lieferdatum klar formuliert sein („Lieferung am 12.06.2025“).\n\
        Für IT-Fachkräfte können technische Formate wie ISO-Daten oder XML sinnvoll sein.",
        "Berechnungen zur Datenqualität sind möglich, z. B. zur Ermittlung der Aktualität:\n\
        Aktualität = (aktuelle + korrigierte Daten) / Gesamtdaten."
    ]

    fragen = [
        {
            "frage": "Welche Aussage trifft zu?",
            "optionen": [
                "a) Gute Informationen stammen meist aus qualitativ hochwertigen Daten.",
                "b) Im Handwerk spielt Datenqualität keine Rolle.",
                "c) Schlechte Datenqualität erkennt man an fehlerhaften und widersprüchlichen Werten.",
                "d) Korrektheit, Genauigkeit und Eindeutigkeit sind keine Qualitätskriterien."
            ],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Was bedeutet Konsistenz bei Daten?",
            "optionen": [
                "a) Widersprüche, die nicht weiter auffallen.",
                "b) Daten stimmen logisch und inhaltlich überein.",
                "c) Daten sind vollständig.",
                "d) Daten sind verständlich für Endnutzer."
            ],
            "antwort": "b"
        },
        {
            "frage": "Wann ist ein Datensatz vollständig?",
            "optionen": [
                "a) Wenn alle Attribute einen gültigen Wert haben.",
                "b) Wenn alle Felder leer sind.",
                "c) Wenn die wichtigsten Werte vorliegen.",
                "d) Wenn keine Redundanzen vorhanden sind."
            ],
            "antwort": "a"
        },
        {
            "frage": "Was beschreibt Redundanzfreiheit?",
            "optionen": [
                "a) Wenn gleiche Informationen mehrfach vorkommen.",
                "b) Wenn Daten sparsam und ohne Wiederholungen gespeichert sind.",
                "c) Wenn Daten besonders vollständig sind.",
                "d) Wenn Daten aktualisiert wurden."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was passiert bei der Datenbereinigung?",
            "optionen": [
                "a) Die Daten werden archiviert.",
                "b) Fehlerhafte Daten werden erkannt und entfernt oder korrigiert.",
                "c) Daten werden nur gelöscht.",
                "d) Neue Daten werden erzeugt."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage ist richtig zur Datenaktualität?",
            "optionen": [
                "a) Veraltete Daten bleiben unverändert im System.",
                "b) Die Korrektur veralteter Daten hat keinen Einfluss.",
                "c) Die Aktualität kann prozentual berechnet werden.",
                "d) Aktualität spielt nur bei Kundendaten eine Rolle."
            ],
            "antwort": "c"
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 5: Datenqualität\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 5: Datenqualität\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

        print("\nZUSATZFRAGE – Berechnungsaufgabe:")
        print("Es wurden 250.000 Kontaktdaten überprüft. 31.759 waren veraltet, davon 12.333 korrigiert.")
        print("Wie hoch ist die Aktualität nach der Korrektur?")

        eingabe = input("Deine Antwort in Prozent (nur Zahl, z.B. 92.23): ").replace(",", ".")
        try:
            wert = float(eingabe)
            if abs(wert - 92.23) < 0.1:
                print("Richtig! Aktualität ≈ 92,23%")
            else:
                print("Falsch! Die korrekte Antwort lautet ≈ 92,23%")
        except:
            print("Ungültige Eingabe – bitte nur eine Zahl eingeben.")

    while True:
        print("\nLernfeld 8 - Modul 5: Datenqualität")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul6():
    lerninhalte = [
        "Eine Datenquelle ist der Ursprung von Daten – also der Ort, an dem Daten entstehen oder gespeichert sind.\n\
        Primäre Datenquellen liefern Daten direkt vom Ursprung (z.B. Sensoren).\n\
        Sekundäre Datenquellen speichern Daten weiter (z.B. Datenbanken, Dateien).",

        "Typische Datenquellen sind:\n\
        – Datenbanken (z.B. MySQL)\n\
        – Dateien (z.B. CSV)\n\
        – Sensoren, Benutzer, Webseiten oder Apps.",

        "Open Data ist für alle frei zugänglich, maschinenlesbar und kostenlos nutzbar.\n\
        Closed Data ist eingeschränkt, oft kostenpflichtig und nur mit Berechtigung verfügbar.",

        "Ein Datenformat beschreibt die Struktur von Informationen in einer Datei.\n\
        Programme können Daten nur lesen, wenn sie das Format verstehen.",

        "Wichtige Datenformate:\n\
        – CSV: Trennzeichen-getrennt, einfach und weit verbreitet\n\
        – XML: Hierarchisch, selbst definierte Tags\n\
        – JSON: Schlüssel-Wert-Paare, kompakt und ideal für Webanwendungen",

        "Beispiele:\n\
        – CSV: Vorname;Nachname;PLZ;Ort\n\
        – XML: <Kunde><PLZ>12345</PLZ></Kunde>\n\
        – JSON: {\"Name\": \"Max\", \"PLZ\": \"12345\"}",

        "Datenübertragung erfolgt oft über Netzwerke.\n\
        Programme holen Daten automatisch oder Nutzer geben sie ein.",

        "Wichtige Übertragungsprotokolle:\n\
        – FTP: Dateien übertragen\n\
        – HTTP: Webdaten abrufen\n\
        – SFTP/FTPS: sichere Dateiübertragung\n\
        – SMB/NFS: Netzwerk-Dateizugriff zwischen Rechnern"
    ]

    fragen = [
        {
            "frage": "Was ist eine primäre Datenquelle?",
            "optionen": ["a) Eine Excel-Tabelle", "b) Eine Datenbank", "c) Ein Sensor", "d) Eine Webseite"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage beschreibt Open Data korrekt?",
            "optionen": ["a) Nur mit Anmeldung nutzbar", "b) Kostenlos, maschinenlesbar, offen",
                         "c) Nur als PDF vorhanden", "d) Kostenpflichtig"],
            "antwort": "b"
        },
        {
            "frage": "Welches Format nutzt geschweifte Klammern und Schlüssel-Wert-Paare?",
            "optionen": ["a) CSV", "b) XML", "c) JSON", "d) TXT"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage stimmt zu Datenformaten?",
            "optionen": ["a) Jedes Programm versteht jedes Format", "b) Formate sind nur bei Bildern wichtig",
                         "c) Formate bestimmen die Lesbarkeit durch Programme", "d) Dateiformate sind veraltet"],
            "antwort": "c"
        },
        {
            "frage": "Welche Protokolle übertragen Daten verschlüsselt? (Mehrere möglich)",
            "optionen": ["a) FTP", "b) HTTP", "c) SFTP", "d) FTPS"],
            "antwort": ["c", "d"]
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 5: Datenquellen, Formate & Übertragung\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 5: Datenquellen, Formate & Übertragung\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 5: Datenquellen, Formate & Übertragung")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul7():
    lerninhalte = [
        "🔹 Heterogene Datenquellen:\n\
        Unternehmen nutzen viele Datenquellen: intern (z.B. Datenbanken) und extern (z.B. Webservices).\n\
        Diese Quellen sind oft uneinheitlich – also *heterogen*. Beispiel: „Ort“ vs. „Location“. Beide meinen dasselbe, sind aber verschieden gespeichert.",

        "🔹 Formen der Heterogenität:\n\
        – Technisch: verschiedene Zugriffsmethoden (z.B. SQL, REST)\n\
        – Syntaktisch: unterschiedliche Darstellung (z.B. Datum als 20.03.2021 oder 2021-03-20)\n\
        – Modellbezogen: unterschiedliche Datenmodelle (z.B. relational vs. dokumentenbasiert)\n\
        – Strukturell: gleiche Daten, verschieden organisiert (z.B. Adressen direkt vs. als Tabelle)\n\
        – Semantisch: gleiche Bedeutung, andere Bezeichnung („Ort“ vs. „Location“)",

        "🔹 Ziel der Informationsintegration:\n\
        Daten aus verschiedenen Quellen in einer *einheitlichen Struktur* zusammenführen.\n\
        Herausforderung: Daten sind oft redundant – Redundanzen müssen erkannt und sinnvoll genutzt werden.",

        "🔹 Zwei Wege der Integration:\n\
        1. *Physische (materialisierte) Integration*: Daten werden zentral gespeichert (z.B. im Data Warehouse oder Data Lake)\n\
        ✔ Vorteile: gute Qualität, schnelle Auswertung\n\
        ✘ Nachteile: nicht immer aktuell, hoher Pflegeaufwand",

        "2. *Virtuelle (logische) Integration*: Daten bleiben am Ursprungsort, werden nur bei Abfrage zusammengeführt (z.B. durch Mediator-Systeme)\n\
        ✔ Vorteile: immer aktuell, flexibel\n\
        ✘ Nachteile: langsamere Abfragen, niedrigere Qualität",

        "🔹 Unterschied Data Warehouse vs. Data Lake:\n\
        – Data Warehouse: strukturierte, vorbereitete Daten für Analysen und Reporting\n\
        – Data Lake: große Mengen roher Daten, auch unstrukturiert – gut für Big Data & KI-Verfahren",

        "🟨 Merke zur Auswahl:\n\
        – Virtuelle Integration: wenn aktuelle Daten wichtig sind\n\
        – Physische Integration: wenn Qualität und Analysegeschwindigkeit im Fokus stehen"
    ]

    fragen = [
        {
            "frage": "Welche Aussage über heterogene Datenquellen ist korrekt?",
            "optionen": [
                "a) Heterogene Quellen enthalten immer gleich formatierte Daten.",
                "b) Heterogenität bedeutet Gleichartigkeit.",
                "c) Unternehmen nutzen oft sowohl interne als auch externe Datenquellen.",
                "d) Datenquellen sind nur dann heterogen, wenn sie aus dem Internet stammen."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Beispiel für semantische Heterogenität?",
            "optionen": [
                "a) 'Ort' in System A, 'Location' in System B",
                "b) '20.03.2021' vs. 'March 20, 2021'",
                "c) Datenbank vs. Textdatei",
                "d) REST vs. SQL"
            ],
            "antwort": "a"
        },
        {
            "frage": "Welche Aussagen treffen zu? (Mehrfachauswahl)",
            "optionen": [
                "a) Die Datenqualität ist bei physischer Integration meist höher.",
                "b) Virtuelle Integration ermöglicht aktuelle Datenzugriffe.",
                "c) Virtuelle Integration ist immer schneller.",
                "d) Physische Integration vermeidet jegliche Redundanz."
            ],
            "antwort": ["a", "b"]
        },
        {
            "frage": "Welche Unterschiede bestehen zwischen Data Warehouse und Data Lake? (Mehrfachauswahl)",
            "optionen": [
                "a) Data Warehouse speichert strukturierte Daten.",
                "b) Data Lakes speichern Daten stets aufbereitet.",
                "c) Data Lakes enthalten auch unstrukturierte Rohdaten.",
                "d) Nur Data Warehouses sind für KI geeignet."
            ],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Was versteht man unter Informationsintegration?",
            "optionen": [
                "a) Das Kombinieren von Daten aus mehreren Quellen in einer gemeinsamen Struktur.",
                "b) Die Speicherung von Daten nur in einer Cloud.",
                "c) Die Erstellung einer Datenbank ohne Redundanzen.",
                "d) Die Sicherung einzelner Systeme gegen Datenverlust."
            ],
            "antwort": "a"
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 5: Heterogene Datenquellen und Integration\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 5: Heterogene Datenquellen und Integration\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 5: Heterogene Datenquellen und Integration")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul8():
    lerninhalte = [
        "UML ist geeignet zur Planung objektorientierter Softwarelösungen.\n"
        "Anwendungsfall-, Klassendiagramme und Aktivitätsdiagramme helfen bei der Strukturierung und Visualisierung.\n"
        "Informationssicherheit muss bereits in der Planungsphase berücksichtigt werden.",

        "Ein Programmierparadigma ist ein grundlegender Ansatz, Programme zu strukturieren.\n"
        "Imperative Paradigmen beschreiben **wie** ein Problem gelöst wird – mit Anweisungen, Kontrollstrukturen.",

        "Strukturiertes Paradigma: nutzt keine Sprunganweisungen wie goto, modularisiert Programme.",
        "Prozedurales Paradigma: verwendet Funktionen/Prozeduren zur Wiederverwendung und Struktur.",

        "Deklarative Paradigmen beschreiben **was** ein Programm leisten soll – ohne konkrete Ablaufschritte.",
        "Funktionale Programmierung: basiert auf Funktionen, ohne Zustandsänderung – etwa Haskell.",
        "Logische Programmierung: basiert auf Fakten und Regeln, etwa in Prolog.",
        "Viele moderne Sprachen kombinieren mehrere Paradigmen – das erhöht Flexibilität, aber auch Komplexität."
    ]

    fragen = [
        {
            "frage": "Was beschreibt ein Programmierparadigma?",
            "optionen": [
                "a) Eine spezielle Programmiersprache",
                "b) Den Stil und Aufbau von Programmen",
                "c) Nur den Programmablaufplan",
                "d) Nur Sicherheitsregeln"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist typisch für das strukturierte Programmierparadigma?",
            "optionen": [
                "a) Viele Sprünge mit goto",
                "b) Nutzung von Prozeduren und Modulen",
                "c) Nutzung von Regeln und Fakten",
                "d) Nur grafische Programmierung"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage trifft auf deklarative Programmierung zu?",
            "optionen": [
                "a) Es wird exakt beschrieben, wie etwas gemacht wird",
                "b) Der Ablauf erfolgt über Zuweisungen und Kontrollstrukturen",
                "c) Sie beschreibt das Was, nicht das Wie",
                "d) Sie basiert auf grafischen Elementen"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Beispiel für funktionale Programmierung?",
            "optionen": [
                "a) Pascal",
                "b) Prolog",
                "c) C",
                "d) Haskell"
            ],
            "antwort": "d"
        },
        {
            "frage": "Was ist ein Merkmal logischer Programmierung?",
            "optionen": [
                "a) Prozeduren",
                "b) Schleifen",
                "c) Regeln und Fakten",
                "d) Klassen und Objekte"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussagen sind **richtig**? (Mehrfachauswahl – Kompetenzcheck)",
            "optionen": [
                "a) Prozedurale Programmierung ist ein imperatives Paradigma.",
                "b) Imperative Programmierung beschreibt den Lösungsweg mit Befehlen.",
                "c) Ein Programmierparadigma beschreibt Struktur und Stil von Programmen.",
                "d) C unterstützt strukturierte und prozedurale Programmierung.",
                "e) Verschiedene Paradigmen eignen sich unterschiedlich gut für bestimmte Probleme.",
                "f) Deklarative Programme beschreiben das Was, nicht das Wie.",
                "g) Deklarative Programme sind oft stark abstrahiert.",
                "h) Prolog ist eine funktionale Sprache.",
                "i) Funktionale Programme bestehen aus Funktionsaufrufen.",
                "j) C ist eine logische Sprache.",
                "k) Logische Programme bestehen aus Regeln und Fakten."
            ],
            "antwort": ["a", "b", "c", "d", "e", "f", "g", "i", "k"]
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 8: Objektorientierung & Paradigmen\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 8: Objektorientierung & Paradigmen\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 8: Objektorientierung & Paradigmen")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul9():
    lerninhalte = [
        "Die objektorientierte Programmierung (OOP) orientiert sich an Objekten der realen Welt.\n"
        "Sie basiert auf früheren Paradigmen wie strukturierter und prozeduraler Programmierung.\n"
        "Ziel ist eine anwendungsnahe Modellierung mit Konzepten wie Klassen, Vererbung und Polymorphie.",

        "Ein Objekt besitzt Eigenschaften (Zustand) und Methoden (Verhalten).\n"
        "Eine Klasse ist eine Vorlage für gleichartige Objekte.\n"
        "Beispiel: Klasse 'Wasserfahrzeug' mit Attributen wie Name, Tiefgang und Methoden wie schwimmen().",

        "Kapselung bedeutet, dass interne Daten eines Objekts verborgen werden.\n"
        "Zugriff auf Eigenschaften erfolgt nur über definierte Schnittstellen (Methoden).\n"
        "Zugriffsmodifizierer: public, protected, private.",

        "Vererbung erlaubt es, neue Klassen auf Basis vorhandener Klassen zu erstellen.\n"
        "Abgeleitete Klassen erben Eigenschaften und Methoden der Basisklasse und können erweitert werden.\n"
        "Mehrfachvererbung ist nicht in allen Sprachen unterstützt.",

        "Polymorphie erlaubt gleichnamige Methoden mit unterschiedlichem Verhalten in verschiedenen Klassen.\n"
        "Formen: Überladen (Methoden mit verschiedenen Parametern), Überschreiben (Methode neu implementiert).\n"
        "Dynamische Bindung entscheidet zur Laufzeit, welche Methode ausgeführt wird."
    ]

    fragen = [
        {
            "frage": "Was ist ein zentrales Ziel der objektorientierten Programmierung?",
            "optionen": [
                "a) Möglichst viele globale Variablen verwenden.",
                "b) Den Programmcode nicht strukturieren.",
                "c) Abbildung realer Objekte in Software durch Klassen und Objekte.",
                "d) Direktes Schreiben in Speicheradressen ermöglichen."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt eine Klasse?",
            "optionen": [
                "a) Ein konkretes Objekt.",
                "b) Eine Programmiersprache.",
                "c) Eine Vorlage für gleichartige Objekte.",
                "d) Eine Fehlerbehandlung."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was gehört zu einem Objekt?",
            "optionen": [
                "a) Nur Methoden.",
                "b) Nur Eigenschaften.",
                "c) Nur Datenbanken.",
                "d) Zustand und Verhalten (Eigenschaften und Methoden)."
            ],
            "antwort": "d"
        },
        {
            "frage": "Was bedeutet Kapselung?",
            "optionen": [
                "a) Methoden dürfen nicht aufgerufen werden.",
                "b) Eigenschaften werden vor direktem Zugriff geschützt.",
                "c) Die Klasse wird mehrfach verwendet.",
                "d) Objekte werden vererbt."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Zugriffsmodifizierer gibt es laut Lehrtext?",
            "optionen": ["a) static, final, new",
                         "b) public, protected, private",
                         "c) open, strict, flexible",
                         "d) inline, export, abstract"],
            "antwort": "b"
        },
        {
            "frage": "Was ist eine abgeleitete Klasse?",
            "optionen": [
                "a) Eine Klasse ohne Methoden.",
                "b) Eine Klasse, die aus einer Basisklasse entsteht und diese erweitert.",
                "c) Eine Kopie der Basisklasse.",
                "d) Eine fehlerhafte Klasse."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt Polymorphie am besten?",
            "optionen": [
                "a) Eine Methode kann nur in einer Klasse existieren.",
                "b) Objekte müssen identisch sein.",
                "c) Gleichnamige Methoden verhalten sich unterschiedlich in verschiedenen Klassen.",
                "d) Eine Methode wird nur einmal im Programm aufgerufen."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist keine Form von Polymorphie?",
            "optionen": [
                "a) Überladen von Methoden.",
                "b) Überschreiben von Methoden.",
                "c) Direktes Editieren von Attributen.",
                "d) Dynamische Bindung."
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Bedingungen gelten beim Überschreiben von Methoden?",
            "optionen": [
                "a) Methodenname, Parameter und Rückgabewert müssen identisch sein.",
                "b) Nur Methodenname muss identisch sein.",
                "c) Parameter dürfen unterschiedlich sein.",
                "d) Rückgabewert darf frei gewählt werden."
            ],
            "antwort": "a"
        },
        {
            "frage": "Warum ist Mehrfachvererbung problematisch?",
            "optionen": [
                "a) Weil sie zu einfache Strukturen erzeugt.",
                "b) Weil sie keine Vererbung erlaubt.",
                "c) Weil nicht alle objektorientierten Sprachen sie vollständig unterstützen.",
                "d) Weil Objekte dabei gelöscht werden."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist das Hauptziel der objektorientierten Programmierung (OOP)?",
            "optionen": [
                "a) Programme möglichst schnell ausführen",
                "b) Programme modularisieren und an Wirklichkeitsobjekte anlehnen",
                "c) Alle Daten sichtbar machen",
                "d) Möglichst viele Programmiersprachen einsetzen"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage beschreibt ein Objekt korrekt?",
            "optionen": [
                "a) Es ist ein Algorithmus.",
                "b) Es ist ein abstraktes Konzept ohne Zustand.",
                "c) Es besitzt Eigenschaften mit Werten und Methoden.",
                "d) Es ist immer privat."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist eine Klasse in der OOP?",
            "optionen": [
                "a) Eine spezielle Methode",
                "b) Eine Funktion zur Laufzeitbindung",
                "c) Ein Bauplan für gleichartige Objekte",
                "d) Ein Codeblock ohne Funktion"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was bedeutet Kapselung in der OOP?",
            "optionen": [
                "a) Objekte werden gelöscht",
                "b) Eigenschaften sind immer öffentlich",
                "c) Implementierungsdetails werden verborgen",
                "d) Methoden können nicht überschrieben werden"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was erlaubt Polymorphie?",
            "optionen": [
                "a) Methoden können mehrfach benannt werden, solange sie identisch sind",
                "b) Methoden gleichen Namens zeigen je nach Objekt unterschiedliches Verhalten",
                "c) Alle Eigenschaften werden mehrfach vererbt",
                "d) Alle Objekte sind gleich"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt dynamisches Binden?",
            "optionen": [
                "a) Methoden werden beim Kompilieren zugewiesen",
                "b) Methodenbindung geschieht zur Laufzeit",
                "c) Objekte werden zu Anfang gelöscht",
                "d) Objekte binden Daten zur Compilezeit"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was sind Voraussetzungen für das Überschreiben einer Methode?",
            "optionen": [
                "a) Anderer Methodenname, gleiche Parameter",
                "b) Gleicher Name, Parameter, Rückgabewert und keine restriktiveren Rechte",
                "c) Gleicher Name, unterschiedliche Rückgabetypen",
                "d) Beliebiger Name mit gleichem Zugriff"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage zur Vererbung ist richtig?",
            "optionen": [
                "a) Nur Eigenschaften, keine Methoden werden vererbt",
                "b) Nur Methoden, keine Eigenschaften werden vererbt",
                "c) Eigenschaften und Methoden der Basisklasse werden übernommen",
                "d) Vererbung gibt es nur in JavaScript"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Problem bei der Mehrfachvererbung?",
            "optionen": [
                "a) Sie ist nur in Python möglich",
                "b) Sie ist sehr leicht zu implementieren",
                "c) Sie wird nicht von allen Sprachen unterstützt",
                "d) Sie führt automatisch zu höherer Leistung"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welches Qualitätsziel wird u.a. durch OOP gefördert?",
            "optionen": [
                "a) Ineffizienz",
                "b) Änderbarkeit und Wiederverwendbarkeit",
                "c) Einmaligkeit des Codes",
                "d) Komplexität und Langsamkeit"
            ],
            "antwort": "b"
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 2: Objektorientiertes Programmierparadigma\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 2: Objektorientiertes Programmierparadigma\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 2: Objektorientiertes Programmierparadigma")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul10():
    lerninhalte = [
        "Sie sollen die Modellierungssprache UML kennenlernen, die einzelnen Diagrammtypen unterscheiden und das Anwendungsfalldiagramm,\n\
         das Klassendiagramm und das Aktivitätsdiagramm anwenden können.\n\
         Größere Softwareprojekte können nicht ohne Vorbereitung und Planung erfolgreich erstellt werden. Abstimmungsgespräche, sowohl zwischen\n\
         den einzelnen Projektmitgliedern als auch mit dem Kunden, sind notwendig. In der Regel werden für die Kommunikation und \n\
         Dokumentation Modellierungssprachen, z.B. das Struktogramm oder das ERM, verwendet. Diese vereinfachen die Kommunikation \n\
         und stellen Sachverhalte übersichtlich dar. Heutzutage wird dafür immer häufiger UML (Unified Modeling Language) genutzt.",

        "Unified Modeling Language (UML) ist eine Modellierungssprache zur Spezifikation, Visualisierung, Konstruktion und Dokumentation \n\
        von Modellen für Softwaresysteme, aber auch zur Darstellung von Geschäftsmodellen. UML bietet eine Vielzahl an Diagrammtypen, besonders \n\
        ausgerichtet auf den objektorientierten Ansatz. Seit 1998 gilt UML als Standard, die Object Management Group (OMG) verantwortet die Standardisierung.",

        "Die Notwendigkeit zur Planung von Softwaresystemen wurde schon in den 1970er-Jahren erkannt. Viele inkompatible\n\
         Modellierungssprachen entstanden. Anfang der 1990er Jahre vereinheitlichten Grady Booch, Ivar Jacobsen und Jim Rumbaugh\n\
         diese in UML. Führende Unternehmen unterstützten diese Entwicklung. Die erste UML-Version erschien 1997, UML 2.0 wurde 2005\n\
         fertiggestellt. Die aktuelle Version 2.5.1 umfasst fast 800 Seiten und wurde 2017 veröffentlicht.",

        "UML 2.5.1 umfasst 14 verschiedene Diagrammtypen, eingeteilt in Struktur- und Verhaltensdiagramme. Diagramme können Elemente\n\
         anderer Diagrammtypen enthalten, besonders zwischen den beiden großen Kategorien. Zur Erstellung werden meist Programme genutzt,\n\
         in Meetings aber oft handgezeichnete Skizzen. Der standardisierte Austausch erfolgt via XML Metadata Interchange (XMI).",

        "UML-Diagramme sind: Verhaltensdiagramme (Anwendungsfalldiagramm, Sequenzdiagramm, Aktivitätsdiagramm, Zeitverlaufsdiagramm,\n\
         Zustandsdiagramm, Kommunikationsdiagramm, Interaktionsübersichtsdiagramm) und Strukturdiagramme (Klassendiagramm, Objektdiagramm, \n\
         Komponentendiagramm, Verteilungsdiagramm, Paketdiagramm, Profildiagramm, Kompositionsstrukturdiagramm). Strukturdiagramme sind statisch\n\
         und beschreiben den Systemzustand, Verhaltensdiagramme dynamisch und beschreiben Abläufe.",

        "Klassendiagramm: Wichtigster UML-Diagrammtyp. Beschreibt Klassen und deren Beziehungen als Bauplan für Objekte.",

        "Objektdiagramm: Spezifizierung des Klassendiagramms, zeigt reale Objekte und deren Beziehungen zur Laufzeit. Ergänzt Klassendiagramme.",

        "Komponentendiagramm: Zeigt Organisation und Abhängigkeiten von Software-Komponenten, die über Klassen-Ebene hinausgehen.",

        "Verteilungsdiagramm: Beschreibt verteilte Systeme, zeigt Geräte und darauf ausgeführte Programme sowie deren Kommunikation.",

        "Paketdiagramm: Gruppiert Klassen zu Paketen, genutzt zur übersichtlichen Anordnung in Programmiersprachen wie Java oder C#.",

        "Profildiagramm: Metamodell-Ebene zur Definition von Stereotypen und Profilen, steht über allen anderen Diagrammen, selten genutzt.",

        "Kompositionsstrukturdiagramm: Beschreibt interne Struktur einer Komponente und deren Interaktionen mit anderen Komponenten.",

        "Anwendungsfalldiagramm: Zeigt Beziehungen zwischen Akteuren und deren Aktionen auf einem System. Verdeutlicht grundlegende\n Anwendungsszenarien. Neben Klassendiagramm eines der wichtigsten UML-Diagramme.",

        "Aktivitätsdiagramm: Beschreibt Verhalten von Klassen oder Komponenten durch Abläufe von Aktionen. Sehr flexibel in der Darstellung.",

        "Zustandsdiagramm: Modelliert Zustandswechsel, Zustandsübergänge und Ereignisse eines Systems. Auch Zustandsautomat genannt.",

        "Sequenzdiagramm: Fokussiert Interaktionen zwischen Objekten, insbesondere den Nachrichtenfluss und zeitlichen Ablauf. Beziehungen\n der Objekte sind nicht dargestellt.",

        "Zeitverlaufsdiagramm: Zeigt Zustandswechsel von Objekten über Zeiträume, z.B. Zeitabstände zwischen Aktionen.",

        "Kommunikationsdiagramm: Stellt Zusammenarbeit von Objekten und deren dynamisches Verhalten dar. Alternative zum Sequenzdiagramm\n mit Fokus auf Struktur der Nachrichten.",

        "Interaktionsübersichtsdiagramm: Vereint mehrere Verhaltensdiagramme, z.B. Aktivitäts- und Sequenzdiagramme, um deren Zusammenspiel\n abzubilden.",

        "Beispielhafte Ausgangssituation: Für Kundenauftrag der Automatik AG entwickelt Systemhaus JIKU Software zur Maschinenwartung und \nProduktionsdatenanalyse. Software unterstützt Wartungsmitarbeiter und Statistiker. Objektorientierter Ansatz mit UML-Modellierung wird in allen Phasen verwendet."
    ]

    fragen = [
        {
            "frage": "Was ist das Hauptziel von UML?",
            "optionen": [
                "a) Visuelle Gestaltung von Benutzeroberflächen.",
                "b) Spezifikation, Visualisierung und Dokumentation von Softwaresystemen.",
                "c) Erstellung von Datenbanken.",
                "d) Programmierung von Webanwendungen."
            ],
            "antwort": "b"
        },
        {
            "frage": "Wer ist verantwortlich für die Standardisierung von UML?",
            "optionen": [
                "a) Microsoft.",
                "b) Object Management Group (OMG).",
                "c) Oracle.",
                "d) International Organization for Standardization (ISO)."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche zwei Hauptkategorien von UML-Diagrammen gibt es?",
            "optionen": [
                "a) Flussdiagramme und Zustandsdiagramme.",
                "b) Strukturdiagramme und Verhaltensdiagramme.",
                "c) Datenflussdiagramme und Netzwerkdiagramme.",
                "d) Anwendungsdiagramme und Klassendiagramme."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welches UML-Diagramm beschreibt den Bauplan von Klassen und deren Beziehungen?",
            "optionen": [
                "a) Aktivitätsdiagramm.",
                "b) Anwendungsfalldiagramm.",
                "c) Klassendiagramm.",
                "d) Zustandsdiagramm."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt ein Objektdiagramm im Vergleich zum Klassendiagramm?",
            "optionen": [
                "a) Es beschreibt abstrakte Klassen.",
                "b) Es zeigt reale Objekte und deren Beziehungen zur Laufzeit.",
                "c) Es modelliert den zeitlichen Ablauf von Aktionen.",
                "d) Es gruppiert Klassen zu Paketen."
            ],
            "antwort": "b"
        },
        {
            "frage": "Wozu dient ein Aktivitätsdiagramm in UML?",
            "optionen": [
                "a) Zur Beschreibung des Verhaltens von Klassen oder Komponenten durch Ablauf von Aktionen.",
                "b) Zur Darstellung von Paketabhängigkeiten.",
                "c) Zur Dokumentation von Hardwarekomponenten.",
                "d) Zur Visualisierung von Zustandsübergängen."
            ],
            "antwort": "a"
        },
        {
            "frage": "Was zeigt ein Verteilungsdiagramm an?",
            "optionen": [
                "a) Die interne Struktur einer Klasse.",
                "b) Verteilung von Programmen auf Geräten und deren Kommunikation.",
                "c) Die zeitliche Abfolge von Nachrichten zwischen Objekten.",
                "d) Beziehungen zwischen Akteuren und Aktionen."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage ist richtig?",
            "optionen": [
                "a) UML wurde in den 1970er Jahren vereinheitlicht.",
                "b) UML ist ausschließlich für objektorientierte Programmierung nutzbar.",
                "c) UML 2.5.1 umfasst 14 verschiedene Diagrammtypen.",
                "d) UML wird nicht mehr weiterentwickelt."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt ein Zustandsdiagramm?",
            "optionen": [
                "a) Eine Abfolge von Aktionen im Zeitverlauf.",
                "b) Zustandswechsel und Ereignisse eines Systems.",
                "c) Beziehungen zwischen Softwarekomponenten.",
                "d) Die Organisation von Klassen in Paketen."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage zum Anwendungsfalldiagramm ist korrekt?",
            "optionen": [
                "a) Es zeigt interne Strukturen von Klassen.",
                "b) Es verdeutlicht grundlegende Anwendungsszenarien durch Beziehungen zwischen Akteuren und Aktionen.",
                "c) Es beschreibt den Nachrichtenfluss zwischen Objekten.",
                "d) Es gruppiert Klassen zu Komponenten."
            ],
            "antwort": "b"
        }
    ]

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 10: UML - Die Modellierungssprache\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 10: UML - Die Modellierungssprache\n")

        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")

            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 - Modul 2: Objektorientiertes Programmierparadigma")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul11():
    lerninhalte = [
        "Ein Anwendungsfalldiagramm stellt die Funktionalität eines Systems aus Sicht der Benutzer dar.\n\
Es beschreibt *was* ein System leisten soll – nicht *wie* es technisch umgesetzt wird.\n\
Ein Anwendungsfalldiagramm besteht aus einer Menge von Anwendungsfällen (Use Cases) und zeigt die Beziehungen zu Akteuren.",

        "Wichtige Notationselemente:\n\
- Systemgrenze: Rechteck, das alle Anwendungsfälle umfasst.\n\
- Akteur (Actor): Externer Benutzer oder System (Strichmännchen oder Rechteck).\n\
- Anwendungsfall: Aktion oder Funktionsgruppe für den Benutzer.\n\
- Assoziation: Linie zwischen Akteur und Anwendungsfall.\n\
- «include»: Unbedingte Einbindung eines Use Cases in einen anderen.\n\
- «extends»: Bedingte Erweiterung eines Use Cases.\n\
- Generalisierung/Spezialisierung: Beziehung zwischen allgemeinem und spezialisiertem Element (für Akteure oder Use Cases).",

        "Angaben außerhalb des Rechtecks gehören nicht zum System.\n\
Aber Schnittstellen zu externen Systemen (z. B. zur Bank) müssen vorhanden sein.\n\
Diese ergeben sich aus den Beziehungen zwischen Akteuren und Anwendungsfällen – z. B. Benutzeroberflächen.\n\
Oft werden mehrere Anwendungsfalldiagramme für komplexere Systeme verwendet.",

        "Beispiel: Wartungsmitarbeiter sollen Maschinen ein-/ausschalten können, Fehlerprotokolle einsehen,\n\
Wartungsprotokolle erstellen und alles drucken können. Statistiker sollen Produktionsdaten einsehen,\n\
analysieren und ebenfalls drucken können. Daten müssen aktualisiert werden.\n\
Das Anwendungsfalldiagramm zeigt dies als vereinfachtes Systemverhalten.",

        "Beispielaufgabe: Hotelzimmerreservierung. Akteure: Kunde, Bank (extern).\n\
Anwendungsfälle: Zimmer reservieren, Verfügbarkeit prüfen («include»), Zahlungsmethode eingeben,\n\
Kreditkarte prüfen («extends», wenn Kreditkarte gewählt wird)."
    ]

    fragen = [
        {
            "frage": "Was beschreibt ein Anwendungsfalldiagramm hauptsächlich?",
            "optionen": ["a) Den technischen Code eines Programms.",
                         "b) Die Nutzeroberfläche in grafischer Form.",
                         "c) Die Funktionalität aus Sicht des Benutzers.",
                         "d) Den Verlauf eines Datenbankzugriffs."],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage trifft NICHT zu einem Anwendungsfalldiagramm?",
            "optionen": ["a) Es zeigt, was das System leisten soll.",
                         "b) Es zeigt die technische Umsetzung.",
                         "c) Es zeigt Beziehungen zu Akteuren.",
                         "d) Es dient der Strukturierung von Use Cases."],
            "antwort": "b"
        },
        {
            "frage": "Was bedeutet das Notationselement «include»?",
            "optionen": ["a) Bedingte Erweiterung eines Use Cases.",
                         "b) Ein Akteur muss einbezogen werden.",
                         "c) Unbedingte Einbindung eines anderen Use Cases.",
                         "d) Technische Erweiterung der Benutzeroberfläche."],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zu Systemgrenzen ist korrekt?",
            "optionen": ["a) Nur Akteure befinden sich innerhalb der Systemgrenze.",
                         "b) Die Systemgrenze enthält alle Akteure und alle Programme.",
                         "c) Die Systemgrenze umfasst alle Anwendungsfälle des Systems.",
                         "d) Angaben außerhalb des Rechtecks müssen ignoriert werden."],
            "antwort": "c"
        },
        {
            "frage": "Welche Elemente sind *nicht* Teil eines Anwendungsfalldiagramms?",
            "optionen": ["a) Anwendungsfälle",
                         "b) Datenbanktabellen",
                         "c) Akteure",
                         "d) Assoziationen"],
            "antwort": "b"
        },
        {
            "frage": "Was stellt eine Generalisierung/Spezialisierung dar?",
            "optionen": ["a) Eine Verbindung zu einer Datenbank.",
                         "b) Eine technische Erweiterung des Systems.",
                         "c) Eine Beziehung zwischen allgemeinem und spezialisiertem Akteur oder Use Case.",
                         "d) Eine Alternative zu «include» und «extends»."],
            "antwort": "c"
        },
        {
            "frage": "Was bedeutet die Notation «extends»?",
            "optionen": ["a) Erweiterung durch ein technisches Modul.",
                         "b) Bedingte Erweiterung eines Anwendungsfalls.",
                         "c) Mehrere Systeme greifen gleichzeitig zu.",
                         "d) Unbedingte Wiederholung eines Use Cases."],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein Akteur in einem Anwendungsfalldiagramm?",
            "optionen": ["a) Eine interne Komponente des Systems.",
                         "b) Ein externer Benutzer oder System.",
                         "c) Eine Funktion innerhalb eines Anwendungsfalls.",
                         "d) Eine Datenbankverbindung."],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussagen zum Beispiel Wartungsprogramm sind korrekt? (Mehrere möglich)",
            "optionen": ["a) Wartungsmitarbeiter können Maschinen ein- und ausschalten.",
                         "b) Fehlerprotokolle können angezeigt werden.",
                         "c) Nur die Statistiker dürfen das System verwenden.",
                         "d) Statistiken können ausgedruckt werden."],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Use Cases enthält das Hotelreservierungssystem? (Mehrere möglich)",
            "optionen": ["a) Zimmer reservieren",
                         "b) Verfügbarkeit prüfen",
                         "c) Zahlungsmethode eingeben",
                         "d) Benutzerprofil erstellen"],
            "antwort": ["a", "b", "c"]
        }
    ]

    def lernen():
        print("\nLERNMODUS – Lernfeld 8, Modul 11: Anwendungsfalldiagramme\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS – Lernfeld 8, Modul 11: Anwendungsfalldiagramme\n")
        punkte = 0
        gesamt = len(fragen)

        for f in fragen:
            print(f["frage"])
            for opt in f["optionen"]:
                print(opt)
            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")
            if isinstance(f["antwort"], list):
                richtige_antworten = set(f["antwort"])
                eingabe_antworten = set(antwort.split(","))
                if eingabe_antworten == richtige_antworten:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
            else:
                if antwort == f["antwort"]:
                    print("Richtig!")
                    punkte += 1
                else:
                    print(f"Falsch! Richtige Antwort: {f['antwort']}")
            print()

        print(f"Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

    while True:
        print("\nLernfeld 8 – Modul 11: Anwendungsfalldiagramme")
        print("1. Lernen")
        print("2. Test")
        print("0. Zurück zum Hauptmenü")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            lernen()
        elif wahl == "2":
            test()
        elif wahl == "0":
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

def modul12():
    lerninhalte = [
        "Klassendiagramme bilden ein zentrales Element der UML. Eingesetzt werden sie vor allem bei der Analyse und beim\n\
         Entwurf eines Softwaresystems.\n\
Sie können unterschiedliche Detaillierungsgrade aufweisen und beschreiben grafisch die Beziehungen zwischen den Klassen einer Anwendung.\n\
Klassendiagramme geben eine statische Sichtweise auf die Anwendung wieder und zählen somit zu den Strukturdiagrammen.\n\
Moderne IDEs haben oft Editoren integriert, mit deren Hilfe sich Klassendiagramme erstellen lassen oder sie können über Extensions\n\
 um diese Funktionalität erweitert werden.",

        "(1) Notationselemente und Aufbau:\n\
Klasse: Rechteck – Darstellung der Klasse mit Namen, Eigenschaften und Methoden.\n\
Klassenname: Singular, Großbuchstabe – trennt Eigenschaften (Attribute) und Methoden (Funktionen) durch eine horizontale Linie.\n\
Klassendarstellung (Alternative): Nur Klassenname – Eigenschaften und Methoden werden oft weggelassen, um Beziehungen zwischen Klassen\n\
 zu modellieren.\n",
"Sichtbarkeit: + public, - private, # protected – beschreibt Zugriffsmodifier der OOP.\n\
Assoziation: Beziehung zwischen Klassen, keine Teil-Ganzes-Beziehung – gerichtete Assoziationen mit Pfeil.\n\
Aggregation: Teil-Ganzes-Beziehung, Teile existieren unabhängig – Verbindungslinie mit nicht ausgefüllter Raute am „Ganzes“-Ende.\n\
Komposition: Starke Teil-Ganzes-Beziehung, Teile existieren nur mit Ganzem – Verbindungslinie mit ausgefüllter Raute am „Ganzes“-Ende.\n\
Multiplizität: Anzahl Objekte in Beziehung – Angaben zu Anzahl der Objekte in Assoziationen, Aggregationen, Kompositionen.\n\
Vererbung: Linie mit dreieckiger, nicht ausgefüllter Pfeilspitze von Unterklasse zur Oberklasse; bei Interfaces Strichlinie\n\
 statt durchgehender Linie.",

        "Einzelne Klassen werden in der Regel mit allen Eigenschaften, Methoden und deren Sichtbarkeiten dargestellt.\n\
Eigenschaften enthalten Datentypen, Methoden die Übergabeparameter und den Rückgabetyp.\n\
Schlüsselwörter wie interface oder abstract können ergänzt werden.\n\
Beziehungen zwischen Klassenobjekten werden modelliert und mit den beschriebenen Notationen visualisiert.",

        "Beispiel Klassendarstellung:\n\
- haarfarbe: string  \n\
+ Person()  \n\
+ Person(string)  \n\
+ Person(string, double)  \n\
+ Person(string, double, string)",
"+ gehen(): void  \n\
+ essen(): void  \n\
+ schlafen(): void  \n\
Klassenname, Eigenschaften mit Datentypen, Methoden mit Parametern und Rückgabetyp sind sichtbar.",

        "(3) Beispielaufgabe Bahnunternehmen:\n\
Ein Zug wird für eine Fahrt aus verschiedenen Objekten zusammengesetzt: Ein Zug hat einen Triebwagen und ein bis zwanzig Waggons.\n\
Triebwagen sind Diesel-Loks oder E-Loks.\n\
Waggons sind Güterwaggons, Personenwaggons oder Speisewagen.\n\
Ein Personenwaggon besitzt bis zu zehn Abteile.\n\
Zug besteht aus Triebwagen und Waggons → Aggregation (Teile existieren unabhängig).\n",
"Diesel-Lok und E-Lok erben von Triebwagen.\n\
Waggon wird vererbt zu Güterwaggon, Personenwaggon, Speisewagen.\n\
Beziehung Personenwaggon – Abteil ist Komposition (Abteile existieren nur mit Personenwaggon).",

        "Kompetenzcheck - richtige Aussagen:\n\
a) Eine Klasse besteht aus Eigenschaften und Methoden.\n\
b) Für jede Eigenschaft und Methode wird eine Sichtbarkeit angegeben.\n\
c) Klassendiagramme zählen zu den Verhaltensdiagrammen.\n\
d) Die Amortisation beschreibt eine Beziehung zwischen Klassen.\n\
e) Die Komposition ist eine Teil-Ganzes-Beziehung.\n\
f) Bei Aggregation können die Teile auch ohne das Ganze existieren.\n\
g) Die Komposition wird durch eine ausgefüllte Raute dargestellt.",

        "Aufgaben:\n\
- Finden Sie jeweils zwei weitere Beispiele für Assoziation, Aggregation, Komposition und Vererbung und diskutieren Sie diese.\n\
- Erweitern Sie die Beispielaufgabe „Zug“ um Klassen „Fahrt“, „Fahrplan“ und „Bahnhof“ mit Bedingungen:\n\
  Eine Fahrt hat genau einen Zug.\n\
  Eine Fahrt umfasst mindestens zwei und maximal zehn Bahnhöfe.\n\
  Ein Fahrplan kann beliebig viele Fahrten enthalten (auch null).\n\
- Diskutieren Sie das Ergebnis im Klassenverband.\n\
- Erstellen Sie für die Klasse „Baum“ vier sinnvolle Eigenschaften und Methoden als vollständige UML-Klasse mit Datentypen\n\
    und Parametern."
    ]

    fragen = [
        {
            "frage": "Was beschreiben Klassendiagramme hauptsächlich?",
            "optionen": ["a) Dynamische Abläufe im System",
                         "b) Beziehungen zwischen Klassen und deren Struktur",
                         "c) Benutzerinteraktionen",
                         "d) Netzwerksicherheit"],
            "antwort": "b"
        },
        {
            "frage": "Wie wird eine Klasse im Klassendiagramm dargestellt?",
            "optionen": ["a) Kreis",
                         "b) Rechteck mit Name, Eigenschaften und Methoden",
                         "c) Raute",
                         "d) Linie"],
            "antwort": "b"
        },
        {
            "frage": "Welche Sichtbarkeitsmodifikatoren sind in UML üblich?",
            "optionen": ["a) + public, - private, # protected",
                         "b) * global, ! internal, ? optional",
                         "c) % visible, & hidden",
                         "d) $ static, @ instance"],
            "antwort": "a"
        },
        {
            "frage": "Was beschreibt eine Aggregation in einem Klassendiagramm?",
            "optionen": ["a) Eine starke Teil-Ganzes-Beziehung",
                         "b) Eine Teil-Ganzes-Beziehung, bei der Teile unabhängig existieren",
                         "c) Eine Vererbung von Klassen",
                         "d) Eine gerichtete Assoziation"],
            "antwort": "b"
        },
        {
            "frage": "Welche Form kennzeichnet eine Komposition?",
            "optionen": ["a) Verbindungslinie mit ausgefüllter Raute am Ganzes-Ende",
                         "b) Linie mit Pfeilspitze",
                         "c) Nicht ausgefüllte Raute",
                         "d) Doppellinie"],
            "antwort": "a"
        },
        {
            "frage": "Wie wird Vererbung in UML dargestellt?",
            "optionen": ["a) Linie mit ausgefüllter Raute",
                         "b) Linie mit dreieckiger, nicht ausgefüllter Pfeilspitze",
                         "c) Doppelpfeil",
                         "d) Linie mit Kreis"],
            "antwort": "b"
        },
        {
            "frage": "Was bedeutet Multiplizität in Klassendiagrammen?",
            "optionen": ["a) Anzahl Objekte in Beziehung",
                         "b) Sichtbarkeit der Klasse",
                         "c) Anzahl Methoden einer Klasse",
                         "d) Anzahl Attribute einer Klasse"],
            "antwort": "a"
        },
        {
            "frage": "Welche Klassen gehören zur Beispielaufgabe des Bahnunternehmens?",
            "optionen": ["a) Zug, Triebwagen, Waggon, Abteil",
                         "b) Auto, Fahrer, Straße",
                         "c) Computer, Monitor, Tastatur",
                         "d) Schiff, Hafen, Kapitän"],
            "antwort": "a"
        },
        {
            "frage": "Welche Beziehung besteht zwischen Personenwaggon und Abteil?",
            "optionen": ["a) Aggregation",
                         "b) Assoziation",
                         "c) Komposition",
                         "d) Vererbung"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage ist falsch?",
            "optionen": ["a) Eine Klasse besteht aus Eigenschaften und Methoden.",
                         "b) Klassendiagramme zählen zu den Strukturdiagrammen.",
                         "c) Die Amortisation beschreibt eine Beziehung zwischen Klassen.",
                         "d) Die Komposition wird durch eine ausgefüllte Raute dargestellt."],
            "antwort": "c"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.3.3 - Klassendiagramme",lerninhalte,fragen)

def modul13():
    lerninhalte = [
        "Sie sollen sich grundlegende Kenntnisse über die Notationselemente und den Aufbau von Aktivitätsdiagrammen erarbeiten und auf\n\
konkrete Aufgaben anwenden können.\n\
Während Diagramme wie das Klassendiagramm eine statische Sicht auf das System abbilden, kann mithilfe vom Aktivitätsdiagramm eine\n\
dynamische Sicht bzw. das Verhalten des Systems modelliert werden.\n\
Das Aktivitätsdiagramm beschreibt den Ablauf von Aktionen und verwendet wenige Symbole für sehr umfangreiche Darstellungsmöglichkeiten.\n\
Es kann hinsichtlich seiner Darstellungsweise und seiner Aussagen mit einem Programmablaufplan verglichen werden. Aktivitätsdiagramme\n\
werden in vielen Phasen der Softwareentwicklung verwendet: in der Analysephase zur Beschreibung von Geschäftsprozessen und Tätigkeiten,\n\
 in der Entwurfsphase zur Darstellung des Algorithmus, in der Testphase zur Entwicklung von Testszenarien sowie zur Dokumentation.",
        "(1) Notationselemente und Aufbau\n\
- Startknoten: markiert den Beginn eines Ablaufes.\n\
- Endknoten: markiert das Ende eines Ablaufes.\n\
- Ablaufende: markiert das Ende eines Zweiges.\n\
- Aktion: beschreibt das Verhalten, welches eine Veränderung herbeiführt.\n\
- Kante: dient zur Angabe des Kontrollflusses.\n\
- Verzweigung: je nach Bedingung wird ein anderer Zweig ausgeführt.\n",
"- Zusammenführung: verschiedene Zweige führen zu gemeinsamer Aktion.\n\
- Aufspaltung: mehrere Aktionen werden parallel begonnen.\n\
- Synchronisation: mehrere Aktionen führen zurück in einen Ablauf.\n\
- Aktivität: kann Ein- und Ausgabeparameter besitzen und in Partitionen unterteilt werden.",
        "(2) Umsetzung eines Aktivitätsdiagramms: Algorithmus zur Durchschnittsproduktion\n\
- Initialisierung von Variablen\n\
- Schleife summiert Werte aus Liste produktionsdaten\n\
- Prüfung auf Division durch Null\n\
- Berechnung des Durchschnitts.",
        "(3) Beispiel Restaurantbesuch\n\
- Beteiligte: Gast, Bedienung, Koch\n\
- Aktionen werden Partitionen zugeordnet\n\
- Bezahlung ist ein interaktiver Prozess (parallel)\n\
- Gastaktionen: betreten, setzen, auswählen, essen, bezahlen, verlassen\n\
- Bedienung: Bestellung aufnehmen, servieren, Bezahlung entgegennehmen\n\
- Koch: Essen zubereiten"
    ]

    fragen = [
        {
            "frage": "Welche Sicht auf ein System liefert ein Aktivitätsdiagramm?",
            "optionen": ["a) Eine rein statische", "b) Eine dynamische", "c) Eine physikalische", "d) Keine"],
            "antwort": "b"
        },
        {
            "frage": "In welcher Phase wird ein Aktivitätsdiagramm zur Beschreibung von Geschäftsprozessen eingesetzt?",
            "optionen": ["a) Analysephase", "b) Testphase", "c) Betriebsphase", "d) Wartungsphase"],
            "antwort": "a"
        },
        {
            "frage": "Was beschreibt ein 'Startknoten' im Aktivitätsdiagramm?",
            "optionen": ["a) Das Ende eines Ablaufs", "b) Den Startpunkt eines Algorithmus", "c) Eine Verzweigung", "d) Eine Aktion mit Parameter"],
            "antwort": "b"
        },
        {
            "frage": "Was ist die Aufgabe der 'Kante' im Aktivitätsdiagramm?",
            "optionen": ["a) Darstellung von Partitionen", "b) Symbol für Startknoten", "c) Angabe des Kontrollflusses", "d) Darstellung von Rückmeldungen"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zur Aufspaltung ist korrekt?",
            "optionen": ["a) Aktionen werden nacheinander ausgeführt", "b) Aktionen beginnen parallel", "c) Es handelt sich um eine Bedingung", "d) Nur für Endknoten verwendbar"],
            "antwort": "b"
        },
        {
            "frage": "Welche Notation wird verwendet, wenn nach mehreren parallelen Aktionen eine gemeinsame Aktion folgt?",
            "optionen": ["a) Aufspaltung", "b) Endknoten", "c) Synchronisation", "d) Partition"],
            "antwort": "c"
        },
        {
            "frage": "Welche Rolle spielt die Partitionierung im Aktivitätsdiagramm?",
            "optionen": ["a) Steuerung des Kontrollflusses", "b) Darstellung paralleler Abläufe", "c) Zuweisung von Aktionen an Beteiligte", "d) Darstellung von Bedingungsausgängen"],
            "antwort": "c"
        },
        {
            "frage": "Welche Sicherheitsüberlegung wird im Beispiel der Durchschnittsberechnung behandelt?",
            "optionen": ["a) Zugriffskontrolle", "b) Schleifenabbruch", "c) Division durch null", "d) Passwortschutz"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aktionen gehören im Beispiel Restaurantbesuch zur Bedienung?",
            "optionen": ["a) Bestellung aufnehmen, Essen zubereiten", "b) Bestellung aufnehmen, Essen servieren, Bezahlung entgegennehmen", "c) Essen servieren, Restaurant verlassen", "d) Restaurant betreten, Bestellung aufnehmen"],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt die Zusammenführung im Aktivitätsdiagramm?",
            "optionen": ["a) Gleichzeitiger Beginn mehrerer Aktionen", "b) Übergang zu Endknoten", "c) Zusammenführen mehrerer Alternativen", "d) Start eines Prozesses"],
            "antwort": "c"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8 - 3.3.6 - Aktivitätsdiagramm beschreiben und anwenden", lerninhalte, fragen)

def modul14():
    lerninhalte = [
        "Die Gefährdung von Daten und Software nimmt im Rahmen der Digitalisierung immer mehr zu,\n\
besonders wenn diese über das Internet zugänglich sind. Besonders kritisch wird es, wenn sensible Daten\n\
oder geschäftsrelevante Software gezielt angegriffen werden. Security by Design bedeutet, dass Software\n\
von Grund auf sicher konzipiert wird. Privacy by Design verlangt Datenschutz während des gesamten\n\
Engineering-Prozesses gemäß DSGVO.",

        "Sechs Sicherheitsprinzipien: Minimalprinzip, Separierung von Berechtigungen, vollständige\n\
Zugriffsüberwachung, mehrere Sicherheitsebenen, sicherer Ausfall, benutzerfreundliche Sicherheit.\n\
Sicherheitsmaßnahmen müssen Zugriffskontrolle, Authentifizierung, Datenvalidierung,\n\
Fehlerbehandlung, Protokollierung und Kryptographie umfassen.",

        "Design- und Umsetzungshinweise: MVC-Pattern zur Trennung von Datenverarbeitung und -darstellung,\n\
Validierung der Daten vor Verarbeitung, sichere Übertragung (HTTPS), sichere Benutzerverwaltung,\n\
geschützte SOAP/REST-Schnittstellen (Whitelist), Unit-Tests, Verhinderung von SQL-Injections,\n\
Protokollierung sicherheitsrelevanter Ereignisse.",

        "Beispielhafte Umsetzung im Scrum-Prozess: Sicherheitsaspekte ermitteln (z.B. User Story, Risikobewertung)\n\
und Maßnahmen planen (z.B. datenschutzfreundliche Voreinstellungen)."
    ]

    fragen = [
        {
            "frage": "Was beschreibt 'Security by Design'?",
            "optionen": ["a) Sicherheit wird nachträglich eingebaut",
                         "b) Software wird von Anfang an sicher konzipiert",
                         "c) Datenschutz wird vollständig ignoriert",
                         "d) Nur die Benutzeroberfläche wird abgesichert"],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein Ziel von 'Privacy by Design'?",
            "optionen": ["a) Datenschutz nur am Ende der Entwicklung",
                         "b) Datensicherung durch externe Dienstleister",
                         "c) Datenschutz während des gesamten Engineering-Prozesses",
                         "d) Benutzerfreundlichkeit durch einfache Passwörter"],
            "antwort": "c"
        },
        {
            "frage": "Welche Sicherheitsprinzipien gehören zu den sechs Kernprinzipien? (Mehrere Antworten möglich)",
            "optionen": ["a) Sicherer Ausfall",
                         "b) Vollständige Zugriffsüberwachung",
                         "c) Offenlegung des Quellcodes",
                         "d) Benutzerfreundliche Sicherheit"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was beschreibt das Minimalprinzip?",
            "optionen": ["a) Jeder darf alles ändern",
                         "b) Nur notwendige Berechtigungen werden vergeben",
                         "c) Zugriff auf alle Daten zur Sicherheit",
                         "d) Sicherheit wird minimiert"],
            "antwort": "b"
        },
        {
            "frage": "Welche Maßnahmen gehören zur Softwarearchitektur? (Mehrere Antworten möglich)",
            "optionen": ["a) Zugriffskontrolle",
                         "b) Datenvalidierung",
                         "c) Wetterdatenintegration",
                         "d) Fehlerbehandlung"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was ist ein Vorteil des mehrschichtigen Sicherheitsmodells?",
            "optionen": ["a) Weniger Sicherheitsprüfungen notwendig",
                         "b) Schutz durch äußere Schichten bei Lücken in inneren",
                         "c) Schnellere Ausführung der Software",
                         "d) Keine Fehlerprotokolle mehr nötig"],
            "antwort": "b"
        },
        {
            "frage": "Welche Umsetzungsmöglichkeiten verhindern SQL-Injections?",
            "optionen": ["a) Nutzung von Framework-Schutzmechanismen",
                         "b) Selbst geschriebene SQL-Parser",
                         "c) Keine Überprüfung der Eingaben",
                         "d) SQL-Kommandos in JavaScript verlagern"],
            "antwort": "a"
        },
        {
            "frage": "Was gehört zu einer sicheren Benutzerverwaltung?",
            "optionen": ["a) Hartecodierte Passwörter",
                         "b) Standardverfahren der Frameworks nutzen",
                         "c) Vollzugriff für alle User",
                         "d) Nur manuelle Logins erlauben"],
            "antwort": "b"
        },
        {
            "frage": "Welche Maßnahmen erhöhen die Sicherheit bei REST/SOAP-Schnittstellen? (Mehrere Antworten möglich)",
            "optionen": ["a) Filtern der Eingabedaten",
                         "b) Whitelisting zulässiger Werte",
                         "c) Verschlüsselung auf Bit-Ebene selbst schreiben",
                         "d) Nutzung von Framework-Filtern"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Ereignisse sollten protokolliert werden? (Mehrere Antworten möglich)",
            "optionen": ["a) Fehlerhafte Anmeldeversuche",
                         "b) Änderungen an Berechtigungen",
                         "c) Wetterverlauf des Tages",
                         "d) Administratoraktivitäten"],
            "antwort": ["a", "b", "d"]
        }
    ]

    modul_lernen_und_testen("Lernfeld 8 - 3.3.7 Sicherheitsrelevante Aspekte bei der Softwareplanung", lerninhalte, fragen)

def modul15():
    lerninhalte = [
        "Softwareergonomie befasst sich mit der Anpassung von Software an Benutzerbedürfnisse.\n\
        Die Benutzerschnittstelle ist das Bindeglied zwischen Mensch und Computer.\n\
        Interaktionsformen reichen von alphanumerischen Oberflächen bis zu virtueller Realität.\n\
        Erkenntnisse aus Psychologie, Arbeitswissenschaft und Design fließen in die Gestaltung ein.",
        "Begriffe wie Benutzerfreundlichkeit, Bedienbarkeit, Usability beschreiben die Qualität der Interaktion.\n\
        Eine hohe Usability steigert Produktivität, reduziert Stress und Ermüdung.\n\
        Ergonomische Anforderungen sind in ISO 9241-110:2020 definiert – u.a. Steuerbarkeit, Erwartungskonformität, Robustheit gegen Fehler.",
        "User Experience (UX) beschreibt Wahrnehmung und Reaktion während der Nutzung.\n\
        UX Design analysiert, gestaltet und optimiert Benutzererlebnisse.\n\
        Bestandteile: visuelles Design, Informationsarchitektur, Interaktionsdesign, Usability, Zugänglichkeit.",
        "Corporate Design (Teil der Corporate Identity) schafft ein konsistentes Erscheinungsbild.\n\
        Ziel: Wiedererkennung, Kundenbindung, positives Unternehmensbild.",
        "Barrierefreiheit ermöglicht Nutzung durch Menschen mit Einschränkungen.\n\
        Umsetzung z.B. durch Tab-Navigation, Skalierbarkeit, Alternativtexte.\n\
        Betriebssysteme bieten unterstützende Funktionen wie Vorlesesoftware oder Braille-Display-Unterstützung."
    ]

    fragen = [
        {
            "frage": "Was ist das Ziel der Softwareergonomie?",
            "optionen": ["a) Die Entwicklung neuer Hardwarekomponenten.",
                         "b) Die Anpassung der Software an technische Systeme.",
                         "c) Die Anpassung der Software an Benutzerbedürfnisse.",
                         "d) Die Erhöhung der Programmiergeschwindigkeit."],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt der Begriff 'Usability'?",
            "optionen": ["a) Die Ästhetik einer Benutzeroberfläche.",
                         "b) Die Gebrauchstauglichkeit in einem bestimmten Nutzungskontext.",
                         "c) Die Geschwindigkeit der Datenverarbeitung.",
                         "d) Die Anzahl der Nutzerinteraktionen pro Minute."],
            "antwort": "b"
        },
        {
            "frage": "Welche Disziplinen beeinflussen die Gestaltung benutzerfreundlicher Software? (Mehrere Antworten möglich)",
            "optionen": ["a) Psychologie", "b) Arbeitswissenschaft", "c) Medizin", "d) Design"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was gehört zur ISO 9241-110:2020? (Mehrere Antworten möglich)",
            "optionen": ["a) Steuerbarkeit", "b) Energieeffizienz", "c) Erwartungskonformität", "d) Erlernbarkeit"],
            "antwort": ["a", "c", "d"]
        },
        {
            "frage": "Was beschreibt der Begriff 'User Experience (UX)'?",
            "optionen": ["a) Nur die visuelle Gestaltung eines Produkts.",
                         "b) Die Ladegeschwindigkeit von Software.",
                         "c) Die subjektive Wahrnehmung und Reaktion eines Nutzers.",
                         "d) Die Fehlerfreiheit eines Programms."],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage trifft zu UX Design zu?",
            "optionen": ["a) Es bezieht sich ausschließlich auf Farbgestaltung.",
                         "b) Es analysiert und optimiert das Nutzungserlebnis.",
                         "c) Es ersetzt das Corporate Design.",
                         "d) Es konzentriert sich auf Hardwarebedienung."],
            "antwort": "b"
        },
        {
            "frage": "Was ist Bestandteil des UX Designs? (Mehrere Antworten möglich)",
            "optionen": ["a) Visuelles Design", "b) Informationsarchitektur", "c) Interaktionsdesign", "d) Datenbankdesign"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Welche Merkmale sind Teil des Corporate Designs?",
            "optionen": ["a) Wiedererkennungswert und Kundenbindung",
                         "b) Höhere Downloadrate im Appstore",
                         "c) Optimierte Compilerleistung",
                         "d) Integration neuer Hardware"],
            "antwort": "a"
        },
        {
            "frage": "Was zählt zu barrierefreien Softwaremerkmalen? (Mehrere Antworten möglich)",
            "optionen": ["a) Alternativtexte für Bilder", "b) Bildschirmtastatur", "c) Tab-Navigation", "d) Einfache Codebasis"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Warum ist Barrierefreiheit wichtig?",
            "optionen": ["a) Sie senkt die Serverlast.",
                         "b) Sie ermöglicht auch Menschen mit Einschränkungen die Nutzung.",
                         "c) Sie erhöht den Stromverbrauch der Software.",
                         "d) Sie ersetzt alle Designprinzipien."],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8 - 3.4 - Benutzerschnittstellen unter softwareergonomischen Gesichtspunkten planen", lerninhalte, fragen)

def modul16():
    lerninhalte = [
        "Bevor mit der Umsetzung eines User Interfaces begonnen wird, sollten grafische Entwürfe erstellt werden:\n\
        Sketches, Wireframes, Mockups, Prototypen.\n\
        Diese dienen zur Planung der Benutzerführung, Kommunikation im Team und Präsentation beim Kunden.",
        "Sketch: Erste, grobe Skizze – Fokus auf Ideenfindung, nicht Ästhetik.\n\
        Wireframe: Konzeptioneller Entwurf – statisch oder dynamisch, ohne Farben, Bilder oder Texte.\n\
        Mockup: Detaillierte Visualisierung mit Farben, Typografie, Bildern – noch ohne finale Funktionalität.\n\
        Prototyp: Funktionierendes Modell, Interaktionen testbar, aber noch kein fertiges Produkt.\n\
        Tools: Balsamiq, Axure, Adobe XD, UXPin, Omnigraffle."
    ]

    fragen = [
        {
            "frage": "Was ist der Zweck von Sketches, Wireframes und Mockups?",
            "optionen": ["a) Die finale Software direkt zu implementieren",
                         "b) Ideen visuell vorzubereiten und Benutzerführung zu planen",
                         "c) Nur Entwickler zu schulen",
                         "d) Hardwarekomponenten zu planen"],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein Sketch?",
            "optionen": ["a) Ein detailliertes, farbiges Modell",
                         "b) Eine funktionierende Anwendung",
                         "c) Eine grobe Skizze zur Ideenfindung",
                         "d) Ein HTML-Prototyp"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage trifft auf ein Wireframe zu?",
            "optionen": ["a) Es enthält alle Funktionen der späteren App",
                         "b) Es ist rein dekorativ",
                         "c) Es stellt Struktur und Anordnung der Oberfläche dar",
                         "d) Es ist immer interaktiv"],
            "antwort": "c"
        },
        {
            "frage": "Was unterscheidet ein statisches von einem dynamischen Wireframe?",
            "optionen": ["a) Statische sind farbig, dynamische nicht",
                         "b) Dynamische verknüpfen mehrere Oberflächen",
                         "c) Statische enthalten Code, dynamische nicht",
                         "d) Es gibt keinen Unterschied"],
            "antwort": "b"
        },
        {
            "frage": "Welche Elemente fehlen in einem klassischen Wireframe? (Mehrere Antworten möglich)",
            "optionen": ["a) Farben",
                         "b) Texte",
                         "c) Bilder",
                         "d) Platzhalter"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Welche Tools können zur Erstellung von Wireframes genutzt werden?",
            "optionen": ["a) Adobe XD, Balsamiq, Axure",
                         "b) Microsoft Word",
                         "c) Excel und PowerPoint",
                         "d) JavaScript und Node.js"],
            "antwort": "a"
        },
        {
            "frage": "Was ist ein Mockup?",
            "optionen": ["a) Eine finale Version der Benutzeroberfläche",
                         "b) Eine textbasierte Struktur",
                         "c) Ein visuell detailliertes, aber noch nicht funktionales Modell",
                         "d) Ein Server-Layout"],
            "antwort": "c"
        },
        {
            "frage": "Was zeigt ein Mockup zusätzlich zum Wireframe? (Mehrere Antworten möglich)",
            "optionen": ["a) Farben",
                         "b) Schriftarten",
                         "c) Interaktive Funktionen",
                         "d) Bilder"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Aussage trifft auf einen Prototyp zu?",
            "optionen": ["a) Ein endgültiges Produkt",
                         "b) Ein grafischer Entwurf ohne Funktion",
                         "c) Ein testbares, funktionierendes Modell",
                         "d) Eine Papierskizze"],
            "antwort": "c"
        },
        {
            "frage": "Welche Reihenfolge ist bei der GUI-Entwicklung typisch?",
            "optionen": ["a) Prototyp → Mockup → Wireframe → Sketch",
                         "b) Sketch → Wireframe → Mockup → Prototyp",
                         "c) Wireframe → Prototyp → Sketch → Mockup",
                         "d) Mockup → Prototyp → Sketch → Wireframe"],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.3.4.2 Eine Oberfläche für eine Benutzerschnittstelle entwerfen", lerninhalte, fragen)

def modul17():
    lerninhalte = [
        "Java ist eine moderne, populäre und einfach zu erlernende objektorientierte Programmiersprache.",
        "Java wird seit 1995 (entwickelt von SUN, ab 2010 weitergeführt von Oracle) genutzt und ist in der Praxis weit verbreitet.",
        "Java steht für Qualität, Modularität und Plattformunabhängigkeit. Es ist zentral in der Open-Source-Community verankert.",
        "Java-Programme bestehen aus kleinen, zuverlässigen Moduleinheiten.",
        "Java nutzt das JDK (Java Development Kit) für Entwicklung und das JRE (Java Runtime Environment) zur Ausführung.",
        "Die JRE umfasst die JVM (Java Virtual Machine) zur Interpretation von Bytecode sowie die Java-API als Bibliothek.",
        "Java-Programme werden zuerst in .java-Dateien geschrieben, dann vom Compiler in Bytecode (.class) übersetzt.",
        "Die JVM interpretiert diesen Bytecode zur Laufzeit, weshalb Java auf vielen Plattformen läuft.",
        "Beliebte Java-IDEs sind: Eclipse, IntelliJ, NetBeans, BlueJ und VSCode – jede mit spezifischen Stärken.",
        "Eclipse ist quelloffen, erweiterbar (z.B. durch GUI-Builder), läuft auf Windows, Linux und MacOS und wird im Lehrbuch verwendet.",
    ]

    fragen = [
        {
            "frage": "Wofür steht Java im Kontext der IT?",
            "optionen": [
                "a) Für eine Hardwareplattform",
                "b) Für eine objektorientierte Programmiersprache und IT-Philosophie",
                "c) Für ein Betriebssystem",
                "d) Für einen JavaScript-Dialekt"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was gehört zu den Kernkomponenten der Java-Technologie?",
            "optionen": [
                "a) JDK und JRE",
                "b) JavaScript und Python",
                "c) Windows und Linux",
                "d) HTML und CSS"
            ],
            "antwort": "a"
        },
        {
            "frage": "Welche Aussagen über Java sind korrekt? (Mehrere Antworten möglich)",
            "optionen": [
                "a) Java wurde von SUN entwickelt.",
                "b) Java wird seit 2010 von Microsoft gepflegt.",
                "c) Java ist Bestandteil der Open-Source-Community.",
                "d) Java wurde nie kommerziell genutzt."
            ],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Wie lautet die Dateiendung von Java-Quelltextdateien?",
            "optionen": [
                "a) .exe",
                "b) .js",
                "c) .java",
                "d) .class"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was passiert nach der Kompilierung eines Java-Programms?",
            "optionen": [
                "a) Es wird direkt in Maschinencode übersetzt.",
                "b) Es entsteht Bytecode (.class), der von der JVM interpretiert wird.",
                "c) Der Quelltext wird gelöscht.",
                "d) Die IDE wandelt es in HTML um."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Rolle spielt die JVM?",
            "optionen": [
                "a) Sie ist ein Compiler für JavaScript.",
                "b) Sie interpretiert den Java-Bytecode zur Laufzeit.",
                "c) Sie ist eine Hardware-Komponente.",
                "d) Sie wird nur bei GUI-Anwendungen benötigt."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage über Eclipse ist korrekt?",
            "optionen": [
                "a) Eclipse ist nur für Windows verfügbar.",
                "b) Eclipse ist kommerziell und nicht erweiterbar.",
                "c) Eclipse basiert auf Java und unterstützt viele Programmiersprachen durch Plug-ins.",
                "d) Eclipse wird ausschließlich für Python verwendet."
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche IDE ist speziell für den Ausbildungsbereich konzipiert?",
            "optionen": [
                "a) Eclipse",
                "b) IntelliJ Ultimate",
                "c) NetBeans",
                "d) BlueJ"
            ],
            "antwort": "d"
        },
        {
            "frage": "Welche Funktion erfüllt die Java-API?",
            "optionen": [
                "a) Sie übersetzt Quellcode in Bytecode.",
                "b) Sie ist eine Sammlung vorgefertigter Softwarebausteine.",
                "c) Sie ist ein Betriebssystem.",
                "d) Sie ist ein JavaScript-Editor."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage über IntelliJ ist korrekt?",
            "optionen": [
                "a) Es gibt nur eine kostenpflichtige Version.",
                "b) Es wird ausschließlich für JavaScript verwendet.",
                "c) Die Community Edition reicht für Java SE aus.",
                "d) Es läuft nur unter Windows."
            ],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.3.5.1 Java beschreiben und eine Entwicklungsumgebung auswählen ", lerninhalte, fragen)

def modul18():
    lerninhalte = [
        "Sie lernen grundlegende Sprachelemente von Java kennen und entwickeln einfache Konsolenanwendungen.",
        "Es wird eine kurze Einführung in die grundlegenden Sprachelemente von Java gegeben – darunter Operatoren, Kontrollstrukturen,\n\
         Felder und Zufallszahlen.",
        "Die Umsetzung erfolgt in der Entwicklungsumgebung Eclipse, die auf einfache Weise Java-Projekte erstellen und ausführen lässt.",
        "Java ist case-sensitive, d.h., es wird zwischen Groß- und Kleinschreibung unterschieden (z.B. 'auto' ≠ 'Auto').",
        "Syntaxfehler entstehen häufig durch fehlende oder falsch gesetzte Semikolons oder geschweifte Klammern.",
        "Anweisungsblöcke in Java werden durch geschweifte Klammern gekennzeichnet und können beliebig verschachtelt sein.",
        "Bezeichner sind eindeutige Namen für Variablen, Klassen und Methoden und dürfen nur alphanumerische Zeichen und Unterstriche enthalten.",
        "Ein Bezeichner muss mit einem Buchstaben oder einem Unterstrich beginnen. Einzelne Unterstriche sind nicht erlaubt.",
        "Schlüsselwörter in Java sind reservierte Begriffe mit besonderer Bedeutung und dürfen nicht als Bezeichner verwendet werden\n\
        (z.B. public, class, void usw.).",
        "Kommentare in Java ermöglichen Notizen im Quelltext – entweder einzeilig mit // oder mehrzeilig mit /* */.",
        "Der Datentyp einer Variablen oder Konstanten bestimmt deren Wertebereich, Speichergröße sowie zulässige Operationen.",
        "Zur Ausgabe in Java werden System.out.print und System.out.println verwendet.\n"
        "Zeichenketten werden in Anführungszeichen geschrieben, Variablen werden durch '+' verbunden.\n"
        "Beispiel: System.out.print(\"Text\"); oder System.out.println(\"Text\" + variable);",

        "Zur Konsoleneingabe nutzt man die Scanner-Klasse aus dem Paket java.util.\n"
        "1. Import java.util.*;\n"
        "2. Erzeugen eines Scanner-Objekts: Scanner input = new Scanner(System.in);\n"
        "3. Einlesen mit input.nextLine(), input.nextInt() oder input.nextDouble();\n"
        "4. Am Ende: input.close();",

        "Kontrollstrukturen in Java ermöglichen Verzweigungen und Wiederholungen.\n"
        "Verzweigungen: if, if-else, switch.\n"
        "Schleifenarten: while (kopfgesteuert), do-while (fußgesteuert), for (zählschleife).",

        "Funktionen (Methoden) bestehen aus Rückgabetyp, Funktionsnamen, Parametern, Anweisungen und Rückgabe.\n"
        "Beispiel: static double berechneSumme(double x, double y) { return x + y; }\n"
        "Aufruf erfolgt z.B. in main: double s = berechneSumme(1.2, 3.4);",

        "Felder (Arrays) speichern mehrere Werte gleichen Typs.\n"
        "Index beginnt bei 0. Zugriff erfolgt über feld[0], feld[1], ...\n"
        "Beispiel: int[] feld = new int[5]; feld[0] = 20; feld[4] = 10;"
    ]

    fragen = [
        {
            "frage": "Welche Entwicklungsumgebung wird zur Erstellung einfacher Java-Konsolenanwendungen verwendet?",
            "optionen": ["a) Visual Studio", "b) Eclipse", "c) IntelliJ", "d) NetBeans"],
            "antwort": "b"
        },
        {
            "frage": "Was bedeutet 'case-sensitive' in Java?",
            "optionen": ["a) Groß- und Kleinschreibung sind gleichwertig", "b) Java ignoriert Großbuchstaben", "c) Es wird zwischen Groß- und Kleinschreibung unterschieden", "d) Nur Großbuchstaben sind erlaubt"],
            "antwort": "c"
        },
        {
            "frage": "Wodurch entstehen in Java häufig Syntaxfehler? (Mehrere Antworten möglich)",
            "optionen": ["a) Vergessene Semikolons", "b) Falsche Klammern", "c) Zu viele Leerzeichen", "d) Großbuchstaben"],
            "antwort": ["a", "b"]
        },
        {
            "frage": "Wie beginnt man in Eclipse die Erstellung eines Java-Projekts?",
            "optionen": ["a) File > New > Project", "b) File > New > Java Project", "c) Edit > New > Java Class", "d) Start > Java > New Project"],
            "antwort": "b"
        },
        {
            "frage": "Was ist die Hauptfunktion der Methode 'public static void main(String[] args)' in Java?",
            "optionen": ["a) Sie erstellt ein neues Objekt", "b) Sie initialisiert Variablen", "c) Sie dient als Einstiegspunkt für das Programm", "d) Sie importiert Bibliotheken"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussagen zu Bezeichnern in Java sind korrekt? (Mehrere Antworten möglich)",
            "optionen": ["a) Dürfen Leerzeichen enthalten", "b) Müssen mit Buchstaben oder Unterstrich beginnen", "c) Dürfen keine Sonderzeichen wie $ enthalten", "d) Ein einzelner Unterstrich ist erlaubt"],
            "antwort": ["b", "c"]
        },
        {
            "frage": "Welche dieser Wörter sind in Java reservierte Schlüsselwörter? (Mehrere Antworten möglich)",
            "optionen": ["a) void", "b) auto", "c) class", "d) print"],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Wie kennzeichnet man einen einzeiligen Kommentar in Java?",
            "optionen": ["a) /* */", "b) <!-- -->", "c) //", "d) ##"],
            "antwort": "c"
        },
        {
            "frage": "Wozu dienen geschweifte Klammern in Java?",
            "optionen": ["a) Um Text farbig darzustellen", "b) Um Kommentare zu kennzeichnen", "c) Um Anweisungsblöcke zu definieren", "d) Zur Importierung von Bibliotheken"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage trifft auf den Datentyp einer Variablen zu?",
            "optionen": ["a) Er hat keinen Einfluss auf die Operationen", "b) Er legt den Speicherort fest", "c) Er bestimmt Wertebereich und zulässige Operationen", "d) Er ist beliebig wählbar und hat keine Wirkung"],
            "antwort": "c"
        },
        {
            "frage": "Welche Methode erzeugt einen Zeilenumbruch bei der Ausgabe?",
            "optionen": ["a) System.out.print", "b) System.out.write", "c) System.out.println",
                         "d) System.write.print"],
            "antwort": "c"
        },
        {
            "frage": "Wie verbindet man in Java eine Zeichenkette mit einer Variable in der Ausgabe?",
            "optionen": ["a) Durch ein Komma", "b) Mit '+'", "c) Mit '&'", "d) Mit '#'"],
            "antwort": "b"
        },
        {
            "frage": "Was ist notwendig, um in Java über die Konsole Eingaben zu tätigen?",
            "optionen": ["a) Scanner-Klasse und System.in", "b) System.out.write", "c) input.getText()",
                         "d) Console.read()"],
            "antwort": "a"
        },
        {
            "frage": "Welche Methode wird verwendet, um eine Kommazahl einzulesen?",
            "optionen": ["a) input.next()", "b) input.readDouble()", "c) input.nextDouble()", "d) input.getFloat()"],
            "antwort": "c"
        },
        {
            "frage": "Was ist eine zweiseitige Verzweigung in Java?",
            "optionen": ["a) if", "b) if-else", "c) switch", "d) while"],
            "antwort": "b"
        },
        {
            "frage": "Welche Schleife ist fußgesteuert?",
            "optionen": ["a) for", "b) while", "c) do-while", "d) if"],
            "antwort": "c"
        },
        {
            "frage": "Wie lautet der Rückgabetyp einer Methode, die nichts zurückgibt?",
            "optionen": ["a) void", "b) null", "c) empty", "d) returnless"],
            "antwort": "a"
        },
        {
            "frage": "Welche der folgenden Anweisungen deklariert eine Funktion mit zwei Parametern vom Typ double?",
            "optionen": ["a) double f(x, y) { ... }", "b) static double berechneSumme(double x, double y) { ... }",
                         "c) void berechne(double) { ... }", "d) public void berechneSumme() { ... }"],
            "antwort": "b"
        },
        {
            "frage": "Welchen Index hat das erste Element eines Arrays in Java?",
            "optionen": ["a) 1", "b) -1", "c) 0", "d) beliebig"],
            "antwort": "c"
        },
        {
            "frage": "Wie kann man in einem Array mit fünf Elementen den Wert 10 dem letzten Element zuweisen?",
            "optionen": ["a) feld[5] = 10;", "b) feld[4] = 10;", "c) feld[0] = 10;", "d) feld[10] = 10;"],
            "antwort": "b"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.3.5.2 Grundlegende Sprachelemente beschreiben und Konsolenanwendungen implementieren", lerninhalte, fragen)

def modul19():
   lerninhalte = [
       "Die objektorientierte Programmierung in Java basiert auf den vier Grundkonzepten: Abstraktion, Kapselung, Vererbung und Polymorphie.\n"
       "Java unterstützt diese Konzepte vollständig, jedoch ist Mehrfachvererbung nur über Interfaces möglich.\n"
       "Für die Umsetzung einer Software für ein Luftfahrtunternehmen wurde ein UML-Modell entworfen und in Java umgesetzt."
       ,
       "Eine Klasse beginnt mit dem Schlüsselwort 'class'. Eigenschaften und Methoden werden innerhalb von geschweiften Klammern definiert.\n"
       "Zugriffsmodifier legen die Sichtbarkeit von Klassenbestandteilen fest: public, protected, private.\n"
       "Getter und Setter ermöglichen den kontrollierten Zugriff auf private Eigenschaften (Kapselung).\n"
       "Ein Konstruktor wird beim Erzeugen eines Objekts aufgerufen und dient der Initialisierung.\n"
       "Ein Destruktor wird beim Zerstören eines Objekts aufgerufen, ist in Java jedoch nicht notwendig wegen des Garbage Collectors.\n"
       "Objekte werden mit dem Schlüsselwort 'new' erzeugt.",
       "Vererbung ist ein grundlegendes Prinzip der objektorientierten Programmierung (OOP).",
       "Es gibt Einfach- und Mehrfachvererbung. Java unterstützt direkt nur Einfachvererbung mit dem Schlüsselwort 'extends'.",
       "Mehrfachvererbung kann in Java nur indirekt durch Interfaces realisiert werden.",
       "Vererbte Methoden können genutzt werden, wenn sie public sind. Auf private Attribute kann nicht direkt zugegriffen werden.",
       "Mit 'protected' wird der Zugriff auf Attribute für Unterklassen ermöglicht.",
       "Methoden wie 'getDaten()' können in abgeleiteten Klassen überschrieben werden.",
       "Eine abstrakte Klasse kann abstrakte Methoden enthalten und nicht instanziiert werden.",
       "Abstrakte Methoden besitzen nur eine Methodensignatur, aber keinen Methodenrumpf.",
       "Interfaces enthalten ausschließlich abstrakte Methoden und Konstanten.",
       "Eine Klasse kann mehrere Interfaces implementieren, aber nur von einer abstrakten Klasse erben."
   ]

   fragen = [
       {
           "frage": "Welche vier Grundkonzepte liegen der objektorientierten Programmierung zugrunde?",
           "optionen": ["a) Schleifen, Bedingungen, Klassen, Arrays",
                        "b) Abstraktion, Kapselung, Vererbung, Polymorphie",
                        "c) Public, Private, Methoden, Objekte",
                        "d) Konstruktor, Destruktor, Getter, Setter"],
           "antwort": "b"
       },
       {
           "frage": "Wie wird Mehrfachvererbung in Java umgesetzt?",
           "optionen": ["a) Durch Vererbung von mehreren Klassen",
                        "b) Sie ist in Java nicht möglich",
                        "c) Durch Interfaces",
                        "d) Durch Getter und Setter"],
           "antwort": "c"
       },
       {
           "frage": "Welches Schlüsselwort wird in Java verwendet, um eine Klasse zu definieren?",
           "optionen": ["a) object",
                        "b) class",
                        "c) new",
                        "d) define"],
           "antwort": "b"
       },
       {
           "frage": "Was beschreibt die Kapselung in der OOP?",
           "optionen": ["a) Das Erben von Eigenschaften",
                        "b) Das Verdecken von Methoden",
                        "c) Den kontrollierten Zugriff auf Eigenschaften",
                        "d) Das Ausblenden von Objekten"],
           "antwort": "c"
       },
       {
           "frage": "Wozu dienen Getter und Setter?",
           "optionen": ["a) Zur Initialisierung von Objekten",
                        "b) Zum Zugriff auf öffentliche Eigenschaften",
                        "c) Zur Kontrolle des Zugriffs auf private Eigenschaften",
                        "d) Zur Löschung von Objekten"],
           "antwort": "c"
       },
       {
           "frage": "Welche Zugriffsmodifizierer gibt es in Java? (Mehrere Antworten möglich)",
           "optionen": ["a) public",
                        "b) default",
                        "c) private",
                        "d) protected"],
           "antwort": ["a", "c", "d"]
       },
       {
           "frage": "Was passiert, wenn kein Zugriffsmodifizierer angegeben wird?",
           "optionen": ["a) Die Eigenschaft ist public",
                        "b) Die Eigenschaft ist private",
                        "c) Die Eigenschaft ist nur im selben Paket sichtbar (package-private)",
                        "d) Die Eigenschaft ist automatisch final"],
           "antwort": "c"
       },
       {
           "frage": "Was ist ein Konstruktor?",
           "optionen": ["a) Eine Methode zur Zerstörung eines Objekts",
                        "b) Eine Methode zur Initialisierung eines Objekts",
                        "c) Ein Interface",
                        "d) Ein Zugriffsmodifizierer"],
           "antwort": "b"
       },
       {
           "frage": "Warum sind Destruktoren in Java meist nicht nötig?",
           "optionen": ["a) Weil Java keine Destruktoren kennt",
                        "b) Weil der Garbage Collector automatisch Speicher freigibt",
                        "c) Weil Destruktoren illegal sind",
                        "d) Weil Java persistent ist"],
           "antwort": "b"
       },
       {
           "frage": "Wie erzeugt man ein Objekt in Java?",
           "optionen": ["a) new Klasse();",
                        "b) create Klasse();",
                        "c) Objekt Klasse = new Objekt();",
                        "d) instance Klasse();"],
           "antwort": "a"
       },
       {
           "frage": "Was ist ein wesentliches Merkmal der Vererbung in der OOP?",
           "optionen": [
               "a) Vererbung erlaubt beliebig viele Instanzen.",
               "b) Neue Klassen können auf Basis bestehender Klassen erstellt werden.",
               "c) Vererbung ersetzt die Kapselung.",
               "d) Vererbung ist in Java nicht erlaubt."],
           "antwort": "b"
       },
       {
           "frage": "Welche Vererbungsform unterstützt Java direkt?",
           "optionen": [
               "a) Mehrfachvererbung",
               "b) Dreifachvererbung",
               "c) Einfachvererbung",
               "d) Keine"],
           "antwort": "c"
       },
       {
           "frage": "Wie wird Vererbung in Java realisiert?",
           "optionen": [
               "a) implements",
               "b) inherits",
               "c) uses",
               "d) extends"],
           "antwort": "d"
       },
       {
           "frage": "Welche Zugriffsmodifizierer erlauben Vererbung auf Attribute in Unterklassen?",
           "optionen": [
               "a) private",
               "b) static",
               "c) protected",
               "d) final"],
           "antwort": "c"
       },
       {
           "frage": "Warum kann auf private Attribute einer Oberklasse nicht direkt zugegriffen werden?",
           "optionen": [
               "a) Weil private Methoden vorrang haben.",
               "b) Weil sie nur über Getter/Setter verfügbar sind.",
               "c) Weil Java keine Vererbung unterstützt.",
               "d) Weil nur static aufrufbar ist."],
           "antwort": "b"
       },
       {
           "frage": "Was beschreibt eine abstrakte Methode?",
           "optionen": [
               "a) Eine Methode mit vollständiger Implementierung.",
               "b) Eine Methode, die in jeder Klasse gleich ist.",
               "c) Eine Methode ohne Methodenrumpf.",
               "d) Eine Methode mit doppelter Sichtbarkeit."],
           "antwort": "c"
       },
       {
           "frage": "Was ist ein zentrales Merkmal einer abstrakten Klasse?",
           "optionen": [
               "a) Sie darf Instanzen erzeugen.",
               "b) Sie muss final sein.",
               "c) Sie kann abstrakte und konkrete Methoden enthalten.",
               "d) Sie besteht nur aus Interfaces."],
           "antwort": "c"
       },
       {
           "frage": "Was passiert, wenn eine Klasse nicht alle Methoden eines Interfaces implementiert?",
           "optionen": [
               "a) Die Klasse bleibt unverändert.",
               "b) Die Klasse muss als abstrakt deklariert werden.",
               "c) Das Interface wird automatisch angepasst.",
               "d) Die Klasse wird gelöscht."],
           "antwort": "b"
       },
       {
           "frage": "Was unterscheidet ein Interface von einer abstrakten Klasse? (Mehrfachantwort) ",
           "optionen": [
               "a) In Interfaces sind alle Methoden abstrakt.",
               "b) Interfaces dürfen keine Konstanten enthalten.",
               "c) Interfaces haben immer public Sichtbarkeit.",
               "d) Abstrakte Klassen dürfen mehrere Interfaces erben."],
           "antwort": ["a", "c"]
       },
       {
           "frage": "Was gilt für Java hinsichtlich Mehrfachvererbung?",
           "optionen": [
               "a) Java unterstützt sie direkt.",
               "b) Java unterstützt sie über Interfaces.",
               "c) Java erlaubt sie über Mehrfachkonstruktoren.",
               "d) Java nutzt private Klassen dafür."],
           "antwort": "b"
       }
   ]
   modul_lernen_und_testen("Lernfeld 8.3.5.3 Das objektorientierte Programmierparadigma in Java umsetzen", lerninhalte, fragen)

def modul20():
    with open("lernmodule.json", "r", encoding="utf-8") as f:
        lerninhalte = json.load(f)
        for i in lerninhalte["lm20"]["lerninhalt"]:
            print(i)
            input("Enter...\n")
        """("Grafische Benutzeroberflächen (GUIs) in Java ermöglichen eine komplexere Interaktion als Konsolenanwendungen.",
        "GUI-Programmierung erfordert Planung und ist aufwändiger hinsichtlich Benutzerfreundlichkeit und Oberflächendesign.",
        "Java bietet zur GUI-Erstellung spezielle Bibliotheken: AWT, Swing (JFC), JavaFX.",
        "Swing ist plattformunabhängig, vollständig in Java implementiert und enthält zahlreiche GUI-Komponenten.",
        "Jede grafische Bibliothek benötigt: Widgets (Fenster, Buttons etc.), ein Ereignismodell und grafische\n\
         Grundoperationen (Farben, Linien, Fonts).",
        "Swing erlaubt 'Pluggable Look and Feel' – das UI kann zur Laufzeit geändert werden.",
        "Swing unterstützt Accessibility für barrierefreien Zugang (z.B. Screenreader, Lupe, Spracherkennung).",
        "Die Java2D API erlaubt das Zeichnen und Darstellen von Objekten auf dem Bildschirm.",
        "JFrame ist eine Swing-Klasse zur Erstellung von Fenstern. Beispielcode zeigt: Fenstergröße, Position, Sichtbarkeit.",
        "GUI-Elemente (z.B. Buttons) können Ereignisse auslösen, z.B. Programm beenden mit ActionListener.",
        "GUI-Builder wie WindowBuilder erleichtern die Oberflächengestaltung per Drag and Drop und automatischer Code-Generierung.",
        "WindowBuilder kann über den Eclipse Marketplace installiert und verwendet werden.")"""


    fragen = [
        {
            "frage": "Was unterscheidet eine GUI grundlegend von einer Konsolenanwendung?",
            "optionen": [
                "a) Nur die Ausgabemethode",
                "b) Nur die Programmiersprache",
                "c) Die Interaktion durch Oberflächenelemente",
                "d) Es gibt keinen Unterschied"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche drei grundlegenden Elemente muss eine Java-GUI-Bibliothek bieten?",
            "optionen": [
                "a) Tabellen, SQL-Anbindung, Datenexport",
                "b) Widgets, Ereignismodell, grafische Grundoperationen",
                "c) Konsolenkommandos, Fenster, HTML",
                "d) Netzwerktools, Compiler, Datenbanken"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Java-Bibliothek war die erste GUI-API?",
            "optionen": [
                "a) JavaFX",
                "b) Java2D",
                "c) Swing",
                "d) AWT"
            ],
            "antwort": "d"
        },
        {
            "frage": "Wofür steht die Abkürzung JFC?",
            "optionen": [
                "a) Java Fast Compilation",
                "b) Java Foundation Classes",
                "c) Java Function Core",
                "d) Java File Controller"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was bedeutet 'Pluggable Look and Feel'?",
            "optionen": [
                "a) Das Layout ist fest und unveränderbar",
                "b) Komponenten können dynamisch zur Laufzeit verändert werden",
                "c) Nur Buttons sind veränderbar",
                "d) Es betrifft nur den Hintergrund"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Klasse wird verwendet, um ein Fenster in Java zu erstellen?",
            "optionen": [
                "a) JFrame",
                "b) JWindow",
                "c) FrameMaker",
                "d) JavaPanel"
            ],
            "antwort": "a"
        },
        {
            "frage": "Was bewirkt der Aufruf von System.exit(0) in einer GUI?",
            "optionen": [
                "a) Es öffnet ein neues Fenster",
                "b) Das Programm wird beendet",
                "c) Es startet den Debugger",
                "d) Es wechselt zur Konsole"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Vorteile bieten GUI-Builder?",
            "optionen": [
                "a) Nur grafisch schönere Oberflächen",
                "b) Automatische Codegenerierung und einfache Anordnung der Elemente",
                "c) Schnellere Kompilierung",
                "d) Unterstützung von Datenbanken"
            ],
            "antwort": "b"
        },
        {
            "frage": "Wie heißt der GUI-Builder für Eclipse?",
            "optionen": [
                "a) JavaMaker",
                "b) GUIForge",
                "c) WindowBuilder",
                "d) EclipseFX"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Technologien unterstützt die Accessibility-API in Java? (Mehrere Antworten möglich)",
            "optionen": [
                "a) Spracherkennung",
                "b) Lesegeräte für Blinde",
                "c) Druckfunktion",
                "d) Bildschirmlupe"
            ],
            "antwort": ["a", "b", "d"]
        }
    ]

    modul_lernen_und_testen2("Lernfeld 8.3.5.4 Grafische Benutzerschnittstellen in Java entwickeln", lerninhalte, fragen)

def modul21():
    lerninhalte = [
        "Ziel: Erweiterung der Kenntnisse über objektorientierte Programmierung (OOP) und grafische Benutzeroberflächen in Python.\n\
        Voraussetzung: Grundkenntnisse in Python und Entwicklungsumgebung (z.B. PyCharm).",
        "OOP-Konzepte: Abstraktion, Kapselung, Vererbung, Polymorphie.\n\
        Python unterstützt OOP nur teilweise (z.B. kein vollständiges Methoden-Overloading).",
        "Zugriffsmodifier in Python:\n\
        - public: ohne Präfix, uneingeschränkter Zugriff (Standard in Python)\n\
        - protected: mit einem Unterstrich (_) – nur konventionell geschützt\n\
        - private: mit doppeltem Unterstrich (__) – Zugriff nur innerhalb der Klasse.",
        "Kapselung wird über Getter und Setter erreicht, um Eigenschaften geschützt zu lesen/setzen.\n\
        Änderungen an Schnittstellen wirken sich nicht auf den restlichen Code aus.",
        "Konstruktor: Methode __init__, wird beim Erzeugen des Objekts automatisch aufgerufen.\n\
        Initialisiert Attribute und speichert Anfangswerte.\n\
        Destruktor: Methode __del__, wird beim Löschen eines Objekts aufgerufen (z.B. zum Speichern von Daten).",
        "Python-Klassen bestehen aus Attributen, Methoden und ggf. Konstruktor/Destruktor.\n\
        Beispielklasse: Musikinstrument mit Attributen modell, hersteller, preis sowie Getter/Setter und Methode get_daten().",
        "Objekterzeugung: bezeichner = Klassenname(parameterliste).\n\
        Nach Erzeugung kann auf Attribute über Getter/Setter zugegriffen werden.\n\
        Beispiel aus Hauptprogramm zeigt konkrete Initialisierung und Nutzung."
    ]

    fragen = [
        {
            "frage": "Welche Programmiersprache wird im Kapitel verwendet?",
            "optionen": ["a) Java", "b) C++", "c) Python", "d) JavaScript"],
            "antwort": "c"
        },
        {
            "frage": "Welche Konzepte gehören zur objektorientierten Programmierung?",
            "optionen": ["a) Wiederholung, Reihenfolge, Selektion, Vererbung",
                         "b) Abstraktion, Kapselung, Vererbung, Polymorphie",
                         "c) Funktionen, Bedingungen, Schleifen, Klassen",
                         "d) Modularität, Effizienz, Kompilierung, Parallelität"],
            "antwort": "b"
        },
        {
            "frage": "Welche Sichtbarkeitsstufen unterstützt Python offiziell?",
            "optionen": ["a) Nur public", "b) Nur private", "c) public, protected, private", "d) Keine"],
            "antwort": "c"
        },
        {
            "frage": "Woran erkennt man ein protected-Attribut in Python?",
            "optionen": ["a) Kein Unterstrich", "b) Ein Unterstrich (_) vor dem Namen",
                         "c) Zwei Unterstriche (__)", "d) Stern (*) vor dem Namen"],
            "antwort": "b"
        },
        {
            "frage": "Was ist die Aufgabe eines Getters?",
            "optionen": ["a) Zum Initialisieren des Objekts",
                         "b) Zum Zuweisen eines Werts",
                         "c) Zum Löschen eines Objekts",
                         "d) Zum Auslesen eines Attributwerts"],
            "antwort": "d"
        },
        {
            "frage": "Was ist korrekt über Konstruktoren in Python?",
            "optionen": ["a) Es kann mehrere pro Klasse geben",
                         "b) Sie heißen immer __init__",
                         "c) Sie heißen init() ohne Unterstriche",
                         "d) Konstruktoren sind optional und selten genutzt"],
            "antwort": "b"
        },
        {
            "frage": "Wann wird ein Destruktor aufgerufen?",
            "optionen": ["a) Beim Start des Programms",
                         "b) Beim Anlegen einer Klasse",
                         "c) Beim Löschen eines Objekts",
                         "d) Beim Beenden eines Methodenblocks"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zur Kapselung ist korrekt?",
            "optionen": ["a) Attribute werden immer direkt angesprochen",
                         "b) Getter und Setter ermöglichen kontrollierten Zugriff",
                         "c) Nur Methoden sind gekapselt",
                         "d) Es gibt keine Kapselung in Python"],
            "antwort": "b"
        },
        {
            "frage": "Wie sieht die Syntax zum Erzeugen eines Objekts aus?",
            "optionen": ["a) Klasse = Objekt(Parameter)",
                         "b) bezeichner: Klasse(Parameter)",
                         "c) bezeichner = Klassenname(Parameter)",
                         "d) class Parameter = Objekt"],
            "antwort": "c"
        },
        {
            "frage": "Was enthält die Methode get_daten() der Klasse Musikinstrument?",
            "optionen": ["a) Ein Konstruktor",
                         "b) Die Rückgabe von Modell, Hersteller und Preis",
                         "c) Eine Datenbankverbindung",
                         "d) Nur einen Preisvergleich"],
            "antwort": "b"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.3.6 Anwendungen in Python implementieren", lerninhalte, fragen)
#


