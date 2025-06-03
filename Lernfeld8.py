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

    def lernen():
        print("\nLERNMODUS - Lernfeld 8, Modul 1: Projektmanagement-Grundlagen\n")
        for abschnitt in lerninhalte:
            print("- " + abschnitt)
            input("\nDrücke Enter, um weiterzulernen...")

    def test():
        print("\nTESTMODUS - Lernfeld 8, Modul 1: Projektmanagement-Grundlagen\n")

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
        print("\nLernfeld 8 - Modul 1: Projektmanagement-Grundlagen")
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
