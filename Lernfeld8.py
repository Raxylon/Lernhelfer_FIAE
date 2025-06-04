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
        Primäre Datenquellen liefern Daten direkt vom Ursprung (z. B. Sensoren).\n\
        Sekundäre Datenquellen speichern Daten weiter (z. B. Datenbanken, Dateien).",

        "Typische Datenquellen sind:\n\
        – Datenbanken (z. B. MySQL)\n\
        – Dateien (z. B. CSV)\n\
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
        Unternehmen nutzen viele Datenquellen: intern (z. B. Datenbanken) und extern (z. B. Webservices).\n\
        Diese Quellen sind oft uneinheitlich – also *heterogen*. Beispiel: „Ort“ vs. „Location“. Beide meinen dasselbe, sind aber verschieden gespeichert.",

        "🔹 Formen der Heterogenität:\n\
        – Technisch: verschiedene Zugriffsmethoden (z. B. SQL, REST)\n\
        – Syntaktisch: unterschiedliche Darstellung (z. B. Datum als 20.03.2021 oder 2021-03-20)\n\
        – Modellbezogen: unterschiedliche Datenmodelle (z. B. relational vs. dokumentenbasiert)\n\
        – Strukturell: gleiche Daten, verschieden organisiert (z. B. Adressen direkt vs. als Tabelle)\n\
        – Semantisch: gleiche Bedeutung, andere Bezeichnung („Ort“ vs. „Location“)",

        "🔹 Ziel der Informationsintegration:\n\
        Daten aus verschiedenen Quellen in einer *einheitlichen Struktur* zusammenführen.\n\
        Herausforderung: Daten sind oft redundant – Redundanzen müssen erkannt und sinnvoll genutzt werden.",

        "🔹 Zwei Wege der Integration:\n\
        1. *Physische (materialisierte) Integration*: Daten werden zentral gespeichert (z. B. im Data Warehouse oder Data Lake)\n\
        ✔ Vorteile: gute Qualität, schnelle Auswertung\n\
        ✘ Nachteile: nicht immer aktuell, hoher Pflegeaufwand",

        "2. *Virtuelle (logische) Integration*: Daten bleiben am Ursprungsort, werden nur bei Abfrage zusammengeführt (z. B. durch Mediator-Systeme)\n\
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

# Basierend auf dem bereitgestellten Lehrtext wurde ein neues Modul für das Lernprogramm erstellt,
# das dem Stil von modul1 folgt und zehn Fragen zur objektorientierten Programmierung enthält.

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
