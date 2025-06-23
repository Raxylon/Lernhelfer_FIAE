


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

def modul81():
    lerninhalte = [
        "In der Zeit von Big Data und exponentiellem Datenwachstum ist es wichtig,\n\
        die anfallenden Daten entsprechend zu verarbeiten, zu speichern und\n\
        anschließend für das Unternehmen sinnvoll zu nutzen. Dazu müssen die\n\
        verfügbaren Daten und die dazugehörigen Quellen zunächst analysiert und\n\
        hinsichtlich ihrer Qualität und Verfügbarkeit bewertet werden. Im Anschluss\n\
        daran werden Softwarelösungen entwickelt, welche diese Daten aus den\n\
        verschiedenen Quellen zusammenführen und für eine weitere Analyse\n\
        systemübergreifend bereitstellen.",

        "Viele Unternehmen nutzen noch klassische Konzepte zur Datenverarbeitung,\n\
        insbesondere bei moderat wachsenden, strukturierten Datenmengen. Diese\n\
        Konzepte stoßen bei großen, unstrukturierten Datenmengen schnell an ihre\n\
        Grenzen. Daher setzen immer mehr Unternehmen auf moderne, agile Ansätze wie\n\
        cloudbasierte NoSQL-Datenbanklösungen oder agile Vorgehensmodelle (z. B. Scrum).",

        "Zur Sicherstellung der Softwarequalität wird verstärkt auf objektorientierte\n\
        Programmiersprachen wie Java oder Python gesetzt. Auch die Modellierungssprache\n\
        UML spielt bei der Planung von Softwarelösungen eine große Rolle. Ebenso gewinnt\n\
        die ergonomische Gestaltung von Benutzerschnittstellen an Bedeutung.",

        "Alle diese Themen sind Bestandteil des Lernfelds und orientieren sich an der\n\
        Ausbildungsverordnung und am Rahmenlehrplan der neuen IT-Berufe.\n\
        Beispielhafte Softwareprojekte: Entwicklung einer Lernsoftware („SMART“),\n\
        Musik-Store-Erweiterung, Jachthafen-App, Tool „Statistika“, Luftfahrt-Software,\n\
        Cloud-Migration von ASTRA, Webauftritt, Projektverwaltungssoftware,\n\
        Maschinenwartung mit Datenauswertung.",

        "Softwareprojekte können Neu- oder Anpassungsentwicklungen sein und sowohl intern\n\
        als auch extern beauftragt werden. Die Projektdefinition hängt nicht vom Thema\n\
        oder der Komplexität ab.",

        "Projektmanagement ist die Planung, Überwachung, Steuerung und der Abschluss\n\
        eines Projekts. Projekte durchlaufen Phasen: Initiierung, Definition,\n\
        Planung, Ausführung, Abschluss. Die Projektkontrolle erfolgt über alle Phasen.",

        "Jedes Projekt ist ein Balanceakt zwischen Umfang, Zeit und Kosten. Eine Änderung\n\
        eines Faktors beeinflusst die anderen. Projektmanagement stammt ursprünglich aus\n\
        dem Ingenieurwesen und wurde fachübergreifend weiterentwickelt.",

        "Bearbeitung von Kundenaufträgen im Rahmen von Softwareprojekten gewinnt an\n\
        Bedeutung. Anteil am BIP: 2007 = 2 %, 2020 = 15 %, Tendenz steigend.",

        "Ziel: Entwicklung einer Software zur Aufbereitung, Auswertung und Bereitstellung\n\
        von Daten aus verschiedenen Quellen nach Kundenwunsch.",

        "Arbeit in Projekten unterscheidet sich wesentlich von Routineaufgaben.\n\
        Projekte sind einmalige Vorhaben mit klar definiertem Ziel und begrenzter Dauer."
    ]

    fragen = [
        {
            "frage": "Was ist bei der Verarbeitung großer Datenmengen besonders wichtig?",
            "optionen": ["a) Speicherung auf CDs", "b) Analyse und Bewertung der Datenqualität",
                         "c) Manuelle Dateneingabe", "d) Nutzung lokaler Textdateien"],
            "antwort": "b"
        },
        {
            "frage": "Wofür stoßen klassische Datenkonzepte an ihre Grenzen?",
            "optionen": ["a) Bei strukturierten Daten", "b) Bei kleinen Datenmengen",
                         "c) Bei großen, unstrukturierten Datenmengen", "d) Bei der Programmierung mit Python"],
            "antwort": "c"
        },
        {
            "frage": "Welche Technologien gewinnen in modernen Softwareprojekten an Bedeutung?",
            "optionen": ["a) Disketten und Faxgeräte", "b) NoSQL und agile Modelle",
                         "c) Monolithische Architekturen", "d) Tabellenkalkulationen"],
            "antwort": "b"
        },
        {
            "frage": "Warum wurde der Entwickler beim Bäcker rausgeworfen?",
            "optionen": [
                "a) Weil er den Quellcode des Rezeptes wollte",
                "b) Weil er das Brot mit `sudo` schneiden wollte",
                "c) Weil er meinte: 'Dieses Brötchen kompiliert nicht!'",
                "d) Weil er nach dem `Master-Brot` fragte"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Vorteil objektorientierter Programmiersprachen in Softwareprojekten?",
            "optionen": ["a) Sie arbeiten ohne Daten", "b) Sie reduzieren Softwarequalität",
                         "c) Sie unterstützen eine strukturierte Entwicklung", "d) Sie ersetzen Projektmanagement"],
            "antwort": "c"
        },
        {
            "frage": "Was ist UML?",
            "optionen": ["a) Eine Programmiersprache", "b) Ein Datenbanksystem",
                         "c) Eine Modellierungssprache zur Softwareplanung", "d) Ein Betriebssystem"],
            "antwort": "c"
        },
        {
            "frage": "Was zeigen die Projektbeispiele im Lernfeld?",
            "optionen": ["a) Nur Schulprojekte", "b) Eine Bandbreite realer Softwareentwicklungen",
                         "c) Nur Cloudlösungen", "d) Ausschließlich Apps"],
            "antwort": "b"
        },
        {
            "frage": "Was trifft auf Softwareprojekte zu?",
            "optionen": ["a) Nur interne Entwicklung", "b) Immer identischer Ablauf",
                         "c) Neu- oder Anpassungsentwicklung, intern oder extern",
                         "d) Keine Projektplanung notwendig"],
            "antwort": "c"
        },
        {
            "frage": "Wie entwickelt sich der Beitrag der Projektarbeit zum BIP?",
            "optionen": ["a) Sinkt stark", "b) Bleibt bei 2 %",
                         "c) Stieg von 2 % (2007) auf 15 % (2020)", "d) Ist irrelevant"],
            "antwort": "c"
        },
        {
            "frage": "Was ist unter Projektmanagement zu verstehen?",
            "optionen": ["a) Nur Softwareentwicklung",
                         "b) Planung, Überwachung, Steuerung und Abschluss eines Projekts",
                         "c) Nur Projektabschluss", "d) Nur Dokumentation"],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt ein Projekt im Vergleich zur Routinearbeit?",
            "optionen": ["a) Wiederholende Aufgaben ohne Ziel", "b) Einmaligkeit und klares Zielbild",
                         "c) Offener Zeitrahmen", "d) Permanente Wartung"],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8: modul1 Projektmanagement",lerninhalte,fragen)

def modul82():
    lerninhalte = [
        "Ein erfolgreiches Softwareprojekt wird im geplanten Zeitrahmen, innerhalb der definierten Kosten und in gewünschter Qualität abgeschlossen.",
        "Klassische Vorgehensmodelle (z.B. Wasserfallmodell, V-Modell) bestehen aus streng sequenziellen Phasen mit klaren Meilensteinen.",
        "Bei klassischen Modellen sind Änderungen unerwünscht, da sie aufwendig sind – dies kann zu unpassenden Ergebnissen führen.",
        "Agile Modelle wie Scrum und DevOps setzen auf Flexibilität, frühe nutzbare Software und enge Kundeneinbindung.",
        "Das Agile Manifest (2001) formuliert vier Leitsätze: Interaktion > Prozesse, Software > Dokumentation, Zusammenarbeit > Verträge, Reaktion > Plan.",
        "Agile Projekte liefern kontinuierlich Zwischenergebnisse und fördern hohe Kundenzufriedenheit.",
        "Nachteile agiler Modelle: hoher Zeitaufwand durch Meetings, intensive Tests, schwer kalkulierbare Kosten, ständiger Kundenkontakt.",
        "Vergleich: Klassisch = starre Anforderungen, große Teams, Hierarchie, viel Dokumentation – Agil = flexible Anforderungen, kleine Teams, Selbstorganisation.",
        "Aufwandsschätzungen: klassisch durch Projektleiter, agil gemeinsam im Team.",
        "Scrum ist das meistgenutzte agile Vorgehensmodell in deutschen Unternehmen."
    ]

    fragen = [
        {
            "frage": "Wodurch zeichnet sich ein erfolgreiches Softwareprojekt aus?",
            "optionen": [
                "a) Durch möglichst viele Funktionen",
                "b) Durch Einsatz modernster Technologien",
                "c) Durch Einhaltung von Zeit, Kosten und Qualität",
                "d) Durch eine große Anzahl an Teammitgliedern"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage beschreibt klassische Vorgehensmodelle am besten?",
            "optionen": [
                "a) Sie sind besonders flexibel.",
                "b) Änderungen sind während des Projekts einfach und günstig.",
                "c) Sie basieren auf klar getrennten Projektphasen mit Meilensteinen.",
                "d) Sie setzen auf kleine, selbstorganisierte Teams."
            ],
            "antwort": "c"
        },
        {
            "frage": "Wie viele DAUs braucht man, um eine Glühbirne zu wechseln?",
            "optionen": [
                "a) Einen – aber nur, wenn der Helpdesk vorher die Lampe neu startet.",
                "b) Keinen – das ist ein Hardwareproblem, kein Benutzerfehler.",
                "c) Drei – einer ruft an, einer hält die Birne, und einer dreht den Stuhl.",
                "d) Zehn – neun halten ein Meeting, einer beschwert sich über die IT."
            ],
            "antwort": "c"
        },
        {
            "frage": "Warum gelten klassische Modelle als schwerfällig?",
            "optionen": [
                "a) Weil sie agilen Methoden ähneln.",
                "b) Weil sie viele Entwickler benötigen.",
                "c) Weil sie zu viel Kundenfeedback einfordern.",
                "d) Weil sie Änderungen im Projektablauf kaum zulassen."
            ],
            "antwort": "d"
        },
        {
            "frage": "Welches Ziel verfolgen agile Vorgehensmodelle?",
            "optionen": [
                "a) Möglichst detaillierte Dokumentation",
                "b) Frühe Auslieferung nutzbarer Software",
                "c) Einhaltung starrer Phasen",
                "d) Minimierung der Kundeneinbindung"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welcher der folgenden Werte gehört NICHT zu den Leitsätzen des Agilen Manifests?",
            "optionen": [
                "a) Funktionierende Software ist wichtiger als umfassende Dokumentation.",
                "b) Individuen und Interaktionen sind wichtiger als Prozesse und Werkzeuge.",
                "c) Vertragsverhandlungen sind wichtiger als Zusammenarbeit mit dem Kunden.",
                "d) Reaktion auf Veränderung ist wichtiger als das Befolgen eines Plans."
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Nachteile können bei agilen Vorgehensmodellen auftreten? (Mehrfachantwort möglich)",
            "optionen": [
                "a) Viele Meetings senken die Programmierzeit.",
                "b) Kosten sind schwer kalkulierbar.",
                "c) Späte Änderungen sind extrem teuer.",
                "d) Ständiger Kundenkontakt kann problematisch sein."
            ],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was ist ein zentraler Unterschied zwischen klassischen und agilen Modellen?",
            "optionen": [
                "a) Klassische Modelle liefern häufige Zwischenergebnisse.",
                "b) Agile Modelle vermeiden direkte Kommunikation.",
                "c) Klassische Modelle sind iterativ.",
                "d) Agile Modelle arbeiten oft mit kleinen, selbstorganisierten Teams."
            ],
            "antwort": "d"
        },
        {
            "frage": "Wie erfolgt die Aufwandsschätzung in agilen Teams typischerweise?",
            "optionen": [
                "a) Durch externe Berater",
                "b) Durch das gesamte Team",
                "c) Durch den Kunden",
                "d) Durch den Projektleiter alleine"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage über Kundenbeteiligung in agilen Projekten trifft zu?",
            "optionen": [
                "a) Der Kunde wird erst am Projektende einbezogen.",
                "b) Der Kunde erhält regelmäßig Zwischenergebnisse.",
                "c) Der Kunde hat nur bei Vertragsabschluss Einfluss.",
                "d) Agile Projekte meiden Kundenfeedback bewusst."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welches Vorgehensmodell wird in deutschen Unternehmen am häufigsten verwendet?",
            "optionen": [
                "a) Wasserfallmodell",
                "b) V-Modell",
                "c) Scrum",
                "d) Kanban"
            ],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Datenquellen?", lerninhalte, fragen)

def modul83():
    lerninhalte = [
        "Scrum ist ein agiles Vorgehensmodell im Projektmanagement, ursprünglich für die Softwareentwicklung konzipiert.\n\
        Es ist heute das am weitesten verbreitete Modell in der Produktentwicklung, trotz einfacher Theorie schwer in der Praxis.\n\
        Drei zentrale Rollen in Scrum: Product Owner, Scrum Master, Entwicklungsteam.",
        "Product Owner: Formuliert Anforderungen, pflegt das Product Backlog, priorisiert Aufgaben, vertritt Kundeninteressen.\n\
        Scrum Master: Sichert Einhaltung von Scrum-Praktiken, moderiert, organisiert Ressourcen, beseitigt Hindernisse.\n\
        Entwicklungsteam: 3–9 Mitglieder, organisiert sich selbst, trägt gemeinsam Verantwortung, möglichst flexibel in Aufgaben.",
        "Scrum beruht auf drei Grundsätzen: Transparency, Inspection, Adaption.\n\
        Transparency: Alle Informationen müssen offen zugänglich und dokumentiert sein.\n\
        Inspection: Regelmäßige Überprüfung von Artefakten und Zusammenarbeit.\n\
        Adaption: Erkenntnisse führen zu Anpassung von Plänen und Prozessen.",
        "Scrum-Prozess läuft in Zyklen (Sprints), beginnend mit einer Idee und endend mit einem funktionierenden Produkt.\n\
        Sprints sind feste Intervalle mit Ziel eines Zwischenergebnisses.\n\
        Projektbeginn mit Kick-off-Meeting, Erstellung von Story-Cards.",
        "Product Backlog: Vom Product Owner gepflegte Liste aller Anforderungen, basiert auf Story-Cards.\n\
        Sprint Planning: Planung in zwei Teilen – Auswahl der Anforderungen und Aufteilung in Tasks.\n\
        Sprint Backlog: Enthält alle geplanten Tasks, inkl. Definition of Done, wird visuell dargestellt.",
        "Tägliches Daily Scrum: 15-Minuten-Meeting zur Tagesplanung und Problemerkennung.\n\
        Scrum Master stellt Zeitrahmen (Timebox) sicher, nimmt aber nicht aktiv teil.\n\
        Fortschritt wird im Sprint-Burn-Down-Chart festgehalten.",
        "Impediment List: Dokumentiert aktuelle Hindernisse im Projekt (z. B. Kommunikation, Logistik).\n\
        Scrum Master ergreift Maßnahmen zur Beseitigung dieser Hindernisse.",
        "Sprint Review: Am Ende eines Sprints Vorstellung der Arbeitsergebnisse vor Stakeholdern.\n\
        Feedback wird eingeholt, Product Backlog bei Bedarf angepasst.",
        "Sprint Retrospektive: Analyse des Sprints zur Verbesserung der Zusammenarbeit.\n\
        Ziel: Verbesserung der Prozessqualität zur Erhöhung der Produktqualität.\n\
        Anpassung der Definition of Done.",
        "Scrum ist ein iterativer Prozess: Nach jedem Sprint startet der nächste Zyklus.",
        "Kanban ist eine agile Projektmanagementmethode, bei der eine Gesamtaufgabe in einzelne Schritte zerlegt und diese einzeln abgearbeitet werden.\n\
                Ziel ist eine Reduktion von Risiken, kürzere Bearbeitungszeiten und bessere Qualität.\n\
                Ursprünglich in den 1950er-Jahren von Taiichi Ōno bei Toyota für die Produktionssteuerung entwickelt.\n\
                2007 übertrug David Anderson die Prinzipien auf die Softwareentwicklung.",

        "Ein Kanban-Board visualisiert den Bearbeitungsstand von Aufgaben – typischerweise in drei Spalten: To Do, In Progress/Doing, Done.\n\
        Aufgaben wandern je nach Status zwischen den Spalten.\n\
        Kanban-Boards können physisch (z.B. Whiteboard mit Haftnotizen) oder digital geführt werden.\n\
        Der Workflow sieht vor, dass Teammitglieder Aufgaben selbstständig auswählen und bearbeiten.",

        "Vorteile von Kanban: Übersicht über Fortschritt und Probleme, schnelle Bearbeitung, geringer Managementaufwand, vielseitig einsetzbar, gute Kombinierbarkeit mit anderen Methoden.\n\
        Nachteile: Hohe Anforderungen an Teamkompetenz, nur bedingt geeignet für große Projekte oder starres Zeitmanagement.",

        "Im Vergleich zu Serum: Kanban ist flexibler, hat wenige feste Regeln, keine festen Rollen und Iterationen sind optional.\n\
        Serum hingegen hat ein komplexes Regelwerk, feste Rollen (Product Owner, Serum Master, Team), sowie vorgeschriebene Iterationen und Priorisierung.\n\
        Kanban eignet sich auch für Routineaufgaben, während Serum nur für Projekte ab drei Personen geeignet ist.",

        "Obwohl beide Methoden Gemeinsamkeiten wie agile Arbeitsweise, transparente Prozesse und Aufgabenverteilung aus einem Backlog aufweisen, bleibt Serum das umfassendere Modell.\n\
        Kanban lässt sich leicht auf die visuelle Darstellung von Aufgabenmanagement reduzieren und flexibel mit anderen Methoden kombinieren."
    ]

    fragen = [
        {
            "frage": "Welche der folgenden Aussagen über Scrum trifft zu?",
            "optionen": ["a) Scrum ist ein klassisches Wasserfallmodell.",
                         "b) Scrum eignet sich nur für Softwareentwicklung.",
                         "c) Scrum basiert auf festen Sprints und iterativen Zyklen.",
                         "d) Scrum ersetzt alle Projektrollen durch eine zentrale Figur."],
            "antwort": "c"
        },
        {
            "frage": "Welche Aufgaben hat der Product Owner? (Mehrere Antworten möglich)",
            "optionen": ["a) Pflegt das Product Backlog.",
                         "b) Moderiert Daily Scrum.",
                         "c) Priorisiert Anforderungen.",
                         "d) Ist Teil des Entwicklungsteams."],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Was ist KEINE Aufgabe des Scrum Masters?",
            "optionen": ["a) Sicherstellung der Einhaltung von Scrum-Regeln.",
                         "b) Beseitigung von Hindernissen.",
                         "c) Pflege des Product Backlogs.",
                         "d) Moderation der Retrospektive."],
            "antwort": "c"
        },
        {
            "frage": "Wie groß ist ein typisches Scrum-Entwicklungsteam?",
            "optionen": ["a) 1–3 Mitglieder", "b) 3–9 Mitglieder", "c) 10–15 Mitglieder", "d) Über 20 Mitglieder"],
            "antwort": "b"
        },
        {
            "frage": "Welche drei Grundsätze bilden das Fundament von Scrum?",
            "optionen": ["a) Kontrolle, Struktur, Planung",
                         "b) Transparenz, Überprüfung, Anpassung",
                         "c) Dokumentation, Planung, Erfolg",
                         "d) Offenheit, Sicherheit, Innovation"],
            "antwort": "b"
        },
        {
            "frage": "Was ist der Unterschied zwischen einem Entwickler und einem DAU?",
            "optionen": [
                "a) Der Entwickler liest die Fehlermeldung, der DAU klickt sie weg.",
                "b) Der DAU programmiert nur in Word.",
                "c) Entwickler rebooten den Rechner – DAUs rebooten den Router.",
                "d) Es gibt keinen – beide googeln die Lösung."
            ],
            "antwort": "a"
        },
        {
            "frage": "Was ist ein Sprint Backlog?",
            "optionen": ["a) Eine Liste aller Projektbeteiligten.",
                         "b) Das visuelle Board für Anforderungen des ganzen Projekts.",
                         "c) Der Arbeitsplan eines Sprints mit einzelnen Tasks.",
                         "d) Eine Liste über zukünftige Kundenwünsche."],
            "antwort": "c"
        },
        {
            "frage": "Wann gilt ein Task in Scrum als erledigt?",
            "optionen": ["a) Wenn der Entwickler ihn abgibt.",
                         "b) Sobald das Daily Scrum endet.",
                         "c) Nach Abnahme durch den Product Owner gemäß Definition of Done.",
                         "d) Sobald alle Teammitglieder zustimmen."],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zum Daily Scrum trifft zu?",
            "optionen": ["a) Es dauert 30 Minuten.",
                         "b) Es findet wöchentlich statt.",
                         "c) Es wird vom Product Owner moderiert.",
                         "d) Es dient der täglichen Abstimmung im Team."],
            "antwort": "d"
        },
        {
            "frage": "Wozu dient die Sprint Retrospektive?",
            "optionen": ["a) Um das Produkt an den Kunden zu übergeben.",
                         "b) Um Aufgaben für den nächsten Sprint zu definieren.",
                         "c) Um das Team und den Prozess zu reflektieren.",
                         "d) Um das Burn-Down-Chart auszuwerten."],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt das Product Backlog am besten?",
            "optionen": ["a) Liste aller erledigten Aufgaben.",
                         "b) Zentrale Sammlung aller Anforderungen, gepflegt vom Product Owner.",
                         "c) Dokumentation des Projektabschlusses.",
                         "d) Interne Notizen des Scrum Masters."],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein zentrales Ziel der Kanban-Methode?",
            "optionen": ["a) Feste Rollen im Projektteam",
                         "b) Umfangreiche Dokumentation",
                         "c) Reduktion von Risiken und bessere Qualität",
                         "d) Lange Planungsphasen"],
            "antwort": "c"
        },
        {
            "frage": "Wie ist ein klassisches Kanban-Board typischerweise aufgebaut?",
            "optionen": ["a) Zwei Spalten: Offen – Erledigt",
                         "b) Drei Spalten: To Do – In Progress – Done",
                         "c) Vier Spalten: Plan – Test – Release – Review",
                         "d) Eine Liste aller Aufgaben ohne Status"],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage zu Kanban trifft zu?",
            "optionen": ["a) Kanban kennt feste Rollen wie Product Owner",
                         "b) Aufgaben werden zentral vom Projektleiter zugewiesen",
                         "c) Kanban ist nur für Softwareentwicklung geeignet",
                         "d) Kanban erlaubt eine flexible Anpassung der Spaltenanzahl"],
            "antwort": "d"
        },
        {
            "frage": "Welche Gemeinsamkeit haben Kanban und Serum?",
            "optionen": ["a) Beide erfordern ein großes Team",
                         "b) Beide setzen auf transparente Prozesse und Backlogs",
                         "c) Beide haben strenge Regeln und Rollen",
                         "d) Beide nutzen ausschließlich digitale Boards"],
            "antwort": "b"
        },
        {
            "frage": "Welche Nachteile hat Kanban laut Text? (Mehrere Antworten möglich)",
            "optionen": ["a) Hoher Managementaufwand",
                         "b) Schwierige Umsetzbarkeit bei großen Projekten",
                         "c) Schlechte Kombinierbarkeit mit anderen Methoden",
                         "d) Höhere Anforderungen an fachliche Fähigkeiten bei Ausfall von Teammitgliedern"],
            "antwort": ["b", "d"]
        }
    ]

    modul_lernen_und_testen("Agile Vorgehensmodelle", lerninhalte, fragen)

def modul84():
    lerninhalte = [
        "In Unternehmen entstehen große Datenmengen aus verschiedenen heterogenen Quellen, z.B. Kundenkommunikation, Maschinensensoren oder finanziellen Transaktionen.\n"
        "Die Integration dieser vielfältigen Datenquellen ohne zentralen Zugriffspunkt ist eine große Herausforderung.\n"
        "Datenqualität ist die Eignung von Daten für eine datenverarbeitende Anwendung und beeinflusst die Qualität der daraus gewonnenen Informationen.\n"
        "Schlechte Datenqualität zeigt sich durch Fehler, Dubletten, fehlende Werte, falsche Formate oder Widersprüche.\n"
        "Datenqualität ist entscheidend für den geschäftlichen Erfolg; schlechte Qualität verursacht erhebliche Kosten.\n"
        "Qualitätskriterien für Daten sind Vollständigkeit, Eindeutigkeit, Korrektheit, Aktualität, Genauigkeit, Konsistenz, Redundanzfreiheit, Relevanz, Einheitlichkeit, Zuverlässigkeit, Verständlichkeit und Zugänglichkeit.\n"
        "Diese Kriterien werden in Prozent angegeben und sind je nach Nutzer und Anwendungsfall unterschiedlich wichtig.\n"
        "Beispiele verdeutlichen die Bedeutung und Messbarkeit der Qualitätskriterien, z.B. Dubletten, falsche Formate, veraltete Daten oder widersprüchliche Werte.\n"
        "Es ist wichtig, die Qualitätskriterien auf die Kundenanforderungen abzustimmen und diese bei der Softwareentwicklung zu berücksichtigen.\n"
        "Eine fundierte Analyse der Datenqualität sollte anhand festgelegter Kriterien erfolgen, um Fehlentscheidungen zu vermeiden."
    ]

    fragen = [
        {
            "frage": "Woher stammen die Daten, die in Unternehmen ausgewertet werden?",
            "optionen": ["a) Nur aus Kundenkommunikation",
                         "b) Aus verschiedenen heterogenen Quellen wie Kundenkommunikation, Sensordaten und finanziellen Transaktionen",
                         "c) Nur aus Maschinensensoren",
                         "d) Aus einem zentralen Zugriffspunkt"],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt die Datenqualität?",
            "optionen": ["a) Die Menge der Daten",
                         "b) Die Eignung der Daten für die jeweilige datenverarbeitende Anwendung",
                         "c) Nur die Aktualität der Daten",
                         "d) Die Anzahl der Datenquellen"],
            "antwort": "b"
        },
        {
            "frage": "Welche Probleme weisen Daten mit schlechter Qualität auf?",
            "optionen": ["a) Datenfehler und Dubletten",
                         "b) Fehlende Werte und falsche Formatierungen",
                         "c) Widersprüche in den Daten",
                         "d) Alle genannten Probleme"],
            "antwort": "d"
        },
        {
            "frage": "Warum ist Datenqualität für Unternehmen wichtig?",
            "optionen": ["a) Sie verursacht keine Kosten",
                         "b) Sie beeinflusst den geschäftlichen Erfolg und schlechte Datenqualität verursacht erhebliche Kosten",
                         "c) Sie ist nur in der Industrie relevant",
                         "d) Sie wird nur von Nachrichtendiensten benötigt"],
            "antwort": "b"
        },
        {
            "frage": "Welche der folgenden Kriterien gehören zu den Qualitätskriterien für Daten?",
            "optionen": ["a) Vollständigkeit, Eindeutigkeit, Korrektheit",
                         "b) Geschwindigkeit, Volumen, Visualisierung",
                         "c) Design, Benutzerfreundlichkeit, Performance",
                         "d) Hardware, Software, Netzwerk"],
            "antwort": "a"
        },
        {
            "frage": "Was ist der Unterschied zwischen Debugging und Detektivarbeit?",
            "optionen": [
                "a) Beim Debugging ist der Täter immer man selbst.",
                "b) Detektive haben keine Syntaxfehler.",
                "c) Beim Debugging kann man Coffee statt Fingerabdrücke verwenden.",
                "d) Es gibt keinen – beide verfolgen Spuren."
            ],
            "antwort": "a"
        },
        {
            "frage": "Wie werden die Qualitätskriterien meist angegeben?",
            "optionen": ["a) Als absolute Zahlen",
                         "b) Als Prozentwerte",
                         "c) Als freie Texte",
                         "d) Als binäre Werte (wahr/falsch)"],
            "antwort": "b"
        },
        {
            "frage": "Was bedeutet das Qualitätskriterium 'Vollständigkeit'?",
            "optionen": ["a) Alle Datenwerte sind vorhanden und gültig",
                         "b) Die Daten sind aktuell",
                         "c) Die Daten sind eindeutig",
                         "d) Die Daten sind korrekt formatiert"],
            "antwort": "a"
        },
        {
            "frage": "Warum sollte die Auswahl der Qualitätskriterien an Kundenanforderungen ausgerichtet sein?",
            "optionen": ["a) Weil nicht alle Kriterien für jede Anwendung gleich wichtig sind",
                         "b) Weil alle Kriterien immer gleichzeitig erfüllt sein müssen",
                         "c) Weil Kunden keine Ahnung von Datenqualität haben",
                         "d) Weil nur ein Kriterium ausgewählt werden darf"],
            "antwort": "a"
        },
        {
            "frage": "Welche Auswirkungen hat eine schlechte Datenqualität laut dem Text?",
            "optionen": ["a) Erhöhte Kosten und Zeitaufwand",
                         "b) Schnellere Verarbeitung",
                         "c) Verbesserte Kundenbindung",
                         "d) Keine Auswirkungen"],
            "antwort": "a"
        },
        {
            "frage": "Was ist der wichtigste Grund, eine genaue Analyse der Datenqualität vorzunehmen?",
            "optionen": ["a) Um Kosten zu sparen",
                         "b) Um Fehlentscheidungen durch schlechte Daten zu vermeiden",
                         "c) Um mehr Daten zu generieren",
                         "d) Um das Netzwerk zu optimieren"],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("SCRUM", lerninhalte, fragen)

def modul85():
    lerninhalte = [
        "Programme beziehen ihre Daten häufig aus externen Datenquellen. Diese können Datenbanken, Benutzer-Eingaben oder Echtzeitübertragungen von Maschinen sein. \n\
        Eine Datenquelle ist der Ursprung oder Speicherort von Daten: primär (Ursprung) oder sekundär (Speicherort).\n\
        Beispiele: Datenbanken, Dateien, Maschinen, Videokonferenzen.\n\
        Durch IoT und Big Data nimmt Vielfalt und Menge der Datenquellen stetig zu.\n\
        Datenquellen können offen (Open Data) oder geschlossen (Closed Data) sein.",

        "Open Data sind frei nutzbare Daten, evtl. mit Einschränkungen wie Urhebernennung oder Share-alike.\n\
        Sie ermöglichen neue Anwendungen und Innovationen.\n\
        Quellen: Berlin Open Data, Open.NRW, Statistisches Bundesamt, NASA, Wikipedia, usw.\n\
        Closed Data unterliegen Zugangsbeschränkungen, Rechten oder hohen Kosten.\n\
        Der Übergang ist fließend.\n\
        Pro und Kontra Open Data: + öffentlich finanziert = öffentlich zugänglich, + Innovationspotenzial, - Datenschutzbedenken, - Qualitätszweifel, - Missbrauchsgefahr.",

        "Datenformate definieren Struktur und Inhalt gespeicherter Daten.\n\
        Für Datenaustausch sind einfache, universelle Formate nötig, um Kompatibilität zu gewährleisten.\n\
        CSV: Textbasiertes Format mit Trennzeichen (Komma, Semikolon, etc.), sehr weit verbreitet, einfach lesbar.\n\
        JSON und XML sind Alternativen für komplexere Strukturen.\n\
        XML: Hierarchisch, mit selbstdefinierbaren Tags, Parameter in Attributen.\n\
        CSV enthält Spaltennamen und Listendaten, keine Hierarchie.\n\
        XML nutzt verschachtelte Tags zur Darstellung von Struktur."
    ]

    fragen = [
        {
            "frage": "Was ist eine primäre Datenquelle?",
            "optionen": ["a) Eine bearbeitete Kopie von Daten.",
                         "b) Der ursprüngliche Entstehungsort von Daten.",
                         "c) Eine Backup-Datei.",
                         "d) Eine Videokonferenzaufnahme."],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage zu Open Data ist korrekt?",
            "optionen": ["a) Sie dürfen nie verändert werden.",
                         "b) Sie sind kostenpflichtig.",
                         "c) Sie dürfen frei genutzt werden, evtl. mit Einschränkungen.",
                         "d) Sie stammen nur aus der EU."],
            "antwort": "c"
        },
        {
            "frage": "Welche Beispiele gehören zu Open Data Quellen? (Mehrere Antworten möglich)",
            "optionen": ["a) NASA",
                         "b) DBpedia",
                         "c) Google Public Data Explorer",
                         "d) Private Firmendatenbanken"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Was ist ein wesentliches Merkmal von Closed Data?",
            "optionen": ["a) Immer in analoger Form vorhanden.",
                         "b) Vollständig öffentlich zugänglich.",
                         "c) Zugangsbeschränkungen und Nutzungsrechte.",
                         "d) Werden kostenlos bereitgestellt."],
            "antwort": "c"
        },
        {
            "frage": "Welcher Kritikpunkt wird häufig GEGEN Open Data genannt?",
            "optionen": ["a) Innovationsförderung",
                         "b) Verbesserung des Wettbewerbs",
                         "c) Datenschutzbedenken",
                         "d) Öffentliche Kontrolle"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zu Datenformaten ist korrekt?",
            "optionen": ["a) Alle Formate sind untereinander kompatibel.",
                         "b) Ein Datenformat beschreibt Struktur und Interpretation der Daten.",
                         "c) Datenformate enthalten nur Metadaten.",
                         "d) CSV-Dateien nutzen ausschließlich Tabs als Trennzeichen."],
            "antwort": "b"
        },
        {
            "frage": "Was sagt ein Sysadmin morgens als Erstes?",
            "optionen": [
                "a) 'Wo ist mein Passwortzettel?'",
                "b) 'Ich reboot mal mein Leben.'",
                "c) 'sudo kaffee now –force'",
                "d) 'Ping Kaffee –t'"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein typisches Merkmal von CSV-Dateien?",
            "optionen": ["a) Hierarchische Datenstruktur mit Tags.",
                         "b) Binäres Datenformat.",
                         "c) Nutzung von Trennzeichen für Listendaten.",
                         "d) Nutzung von JSON-Tags."],
            "antwort": "c"
        },
        {
            "frage": "Was unterscheidet XML von CSV?",
            "optionen": ["a) XML verwendet Trennzeichen statt Tags.",
                         "b) CSV ist nur in HTML nutzbar.",
                         "c) XML erlaubt verschachtelte Daten durch Tags.",
                         "d) Beide sind gleich strukturiert."],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Vorteil von universellen Datenformaten wie CSV?",
            "optionen": ["a) Bessere Verschlüsselung",
                         "b) Ermöglichen Datenaustausch zwischen inkompatiblen Programmen.",
                         "c) Speicherung großer Binärdaten",
                         "d) Nutzung von HTML"],
            "antwort": "b"
        },
        {
            "frage": "Welche Datenquelle liefert typischerweise Echtzeitdaten?",
            "optionen": ["a) Archiv-CD-ROM",
                         "b) Maschinen im IoT",
                         "c) Wikipedia",
                         "d) CSV-Dateien auf USB-Stick"],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("Datenquellen", lerninhalte, fragen)

def modul86():
    lerninhalte = [
        "Unternehmen beziehen ihre Daten aus einer Vielzahl interner und externer Datenquellen. Diese Quellen sind oft\n\
        heterogen – d.h. uneinheitlich in Struktur, Format, Bedeutung oder Technologie.",
        "Heterogenität kann sich in folgenden Formen äußern:\n\
        - Technisch: Unterschiedliche Zugriffsschnittstellen (z.B. SQL, XPath)\n\
        - Syntaktisch: Verschiedene Speicherformate (z.B. 20.03.2021 vs. 2021-03-20)\n\
        - Datenmodell: Unterschiedliche Modellarten (z.B. relational vs. dokumentenbasiert)\n\
        - Strukturell: Unterschiedliche Speicherstrukturen trotz gleichem Modell\n\
        - Semantisch: Unterschiedliche Bedeutungen für gleiche Inhalte (z.B. Ort vs. Location)",
        "Ziel ist die Informationsintegration – also das Zusammenführen von Daten aus unterschiedlichen Quellen zu einer einheitlichen Struktur.\n\
        Dabei müssen Redundanzen erkannt, ggf. entfernt oder zur Verifikation genutzt werden.",
        "Integrationsarten:\n\
        - Materialisierte/physische Integration: Daten werden zentral gespeichert (z.B. im Data Warehouse oder Data Lake)\n\
        - Virtuelle/logische Integration: Daten bleiben dezentral, werden erst zur Laufzeit verbunden (z.B. in föderierten Datenbanksystemen)",
        "Materialisierte Integration – Vorteile:\n\
        - Schnellere Verfügbarkeit\n\
        - Höhere Datenqualität\n\
        Nachteile:\n\
        - Daten evtl. veraltet\n\
        - hoher Pflegeaufwand (Hardware, Quellenänderungen)",
        "Virtuelle Integration – Vorteile:\n\
        - Immer aktuelle Daten\n\
        - Flexibles Hinzufügen/Entfernen von Quellen\n\
        Nachteile:\n\
        - Langsame Abfrage\n\
        - Geringere Datenqualität",
        "Data Warehouse: zentrale, strukturierte Datenbank zur Analyse großer Datenmengen. Daten werden vorher aufbereitet\n\
        und transformiert (Data Warehousing).",
        "Data Lake: flexible Analyseplattform für große Mengen unstrukturierter Daten (Big Data). Sehr hohe Speicherkapazität,\n\
        nutzt moderne Analyseverfahren.",
        "Data Lakes sind besonders geeignet für vielfältige, große und unstrukturierte Daten. Data Warehouses hingegen für\n\
        strukturierte Datenanalysen.",
        "Beide Lösungen sind aufwendig, mitunter nicht aktuell. Datenvirtualisierung kann hier helfen – da die Daten am Ursprungsort\n\
        verbleiben, bleiben sie synchron."
    ]

    fragen = [
        {
            "frage": "Was bedeutet der Begriff 'heterogen' im Kontext von Datenquellen?",
            "optionen": ["a) Gleichförmig", "b) Uneinheitlich", "c) Zentralisiert", "d) Verschlüsselt"],
            "antwort": "b"
        },
        {
            "frage": "Welche Formen der Heterogenität gibt es? (Mehrere Antworten möglich)",
            "optionen": ["a) Technisch", "b) Physikalisch", "c) Semantisch", "d) Strukturell"],
            "antwort": ["a", "c", "d"]
        },
        {
            "frage": "Was ist Informationsintegration?",
            "optionen": ["a) Die Auswertung von einheitlichen Datenmodellen",
                         "b) Die Speicherung von Daten in lokalen Quellen",
                         "c) Die Vereinheitlichung heterogener Datenstrukturen",
                         "d) Das Mining von Big-Data-Systemen"],
            "antwort": "c"
        },
        {
            "frage": "Welche Vorteile bietet die physische Integration? (Mehrere Antworten möglich)",
            "optionen": ["a) Immer aktuelle Daten", "b) Schnellere Verfügbarkeit", "c) Höhere Datenqualität",
                         "d) Flexibles Quellmanagement"],
            "antwort": ["b", "c"]
        },
        {
            "frage": "Ein Nachteil der virtuellen Integration ist...",
            "optionen": ["a) langsame Abfragen", "b) veraltete Daten", "c) hoher Hardwarebedarf",
                         "d) geringer Speicherbedarf"],
            "antwort": "a"
        },
        {
            "frage": "Wo verbleiben die Daten bei virtueller Integration?",
            "optionen": ["a) In einer Cloud", "b) In einer zentralen Datenbank", "c) In den ursprünglichen Quellen",
                         "d) In einem Data Lake"],
            "antwort": "c"
        },
        {
            "frage": "Was kennzeichnet ein Data Warehouse? (Mehrere Antworten möglich)",
            "optionen": ["a) Nutzung unstrukturierter Daten", "b) Zentrale Datenhaltung", "c) Striktes Datenmodell",
                         "d) Fokus auf Analyse großer Datenmengen"],
            "antwort": ["b", "c", "d"]
        },
        {
            "frage": "Ein Data Lake ist besonders geeignet für...",
            "optionen": ["a) Kleine strukturierte Datenmengen",
                         "b) Realtime-Transaktionen",
                         "c) Unstrukturierte Big-Data-Datenmengen",
                         "d) Datenbank-Backups"],
            "antwort": "c"
        },
        {
            "frage": "Warum kann Datenvirtualisierung hilfreich sein?",
            "optionen": ["a) Weil sie Daten redundant speichert",
                         "b) Weil sie physische Hardware ersetzt",
                         "c) Weil Daten synchron mit Originaldaten bleiben",
                         "d) Weil sie Daten verschlüsselt"],
            "antwort": "c"
        },
        {
            "frage": "Was ist das Backup-Mantra jedes Admins?",
            "optionen": [
                "a) 'Ich vertraue meinem RAID 0.'",
                "b) 'Ein Backup ist kein Backup.'",
                "c) 'Festplatten leben ewig.'",
                "d) 'Speichern heißt vergessen.'"
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage trifft auf Redundanz bei Informationsintegration zu?",
            "optionen": ["a) Redundanz muss immer vollständig vermieden werden",
                         "b) Redundante Daten können zur Verifikation genutzt werden",
                         "c) Redundanz ist bei homogener Struktur unvermeidbar",
                         "d) Redundanz erhöht die Zugriffsgeschwindigkeit"],
            "antwort": "b"
        }
    ]

    modul_lernen_und_testen("Heterogene Datenquellen", lerninhalte, fragen)

def modul87():
    lerninhalte = [
        "8.3 Objektorientierte Softwarelösungen unter Beachtung der Informationssicherheit planen.\n\
        Mithilfe von UML-Diagrammen werden objektorientierte Anwendungen geplant und sicherheitsrelevante Aspekte berücksichtigt.\n\
        UML-Anwendungsfall- und Klassendiagramme sind besonders geeignet für Planung und Dokumentation.\n\
        UML-Aktivitätsdiagramme ersetzen oft den veralteten Programmablaufplan (PAP) zur Abbildung von Algorithmen und Prozessen.\n\
        Sicherheitsaspekte in der Softwareplanung werden häufig vernachlässigt, obwohl Kundenerwartungen hoch sind.",

        "3.3.1 Programmierparadigmen unterscheiden.\n\
        Programme bestehen aus Befehlen und Speicheradressen.\n\
        Programmierparadigmen sind Konzepte, die den Aufbau und die Ausführung von Programmen definieren und den Programmierstil beeinflussen.\n\
        Es gibt kein ‚richtig‘ oder ‚falsch‘, nur passendere oder weniger passende Paradigmen für bestimmte Probleme.\n\
        Moderne Programmiersprachen unterstützen oft mehrere Paradigmen.",

        "Imperative Programmierparadigmen beschreiben präzise die Reihenfolge der Abarbeitung von Befehlen mit Kontrollstrukturen wie Verzweigungen und Schleifen.\n\
        Dazu gehören strukturiertes, prozedurales und objektorientiertes Programmierparadigma.\n\
        Strukturiertes Programmieren verzichtet auf Sprunganweisungen (Goto) zugunsten von Kontrollstrukturen und verlangt Zerlegung in Teilprogramme.\n\
        Beispiele: C, Pascal.",

        "Prozedurales Programmierparadigma baut auf strukturiertem Programmieren auf, um Quelltexte wiederverwendbar und übersichtlich zu machen.\n\
        Programme werden in Prozeduren oder Funktionen aufgeteilt, um Redundanzen zu vermeiden.\n\
        Beispiele: C, FORTRAN, COBOL, Pascal.",

        "Objektorientiertes Programmierparadigma ist eine Weiterentwicklung anderer Paradigmen und heute Standard in vielen Bereichen der Softwareentwicklung.\n\
        Es wird in Abschnitt 8.3.2 vertiefend erläutert.",

        "Deklarative Programmierparadigmen beschreiben nur das gewünschte Ergebnis, nicht die Umsetzung.\n\
        Dadurch ist Quelltext kurz, präzise, aber oft schwerer verständlich.\n\
        Trennung von Ausführungslogik und Programmentwicklung erleichtert Wartung und Optimierung.\n\
        Wichtige Arten sind funktionales und logisches Programmierparadigma.",

        "Funktionales Programmierparadigma besteht aus einer Reihe von Funktionsaufrufen ohne Wertzuweisungen.\n\
        Eingesetzt u.a. in KI und Compilerbau.\n\
        Beispiele: Lisp, Haskell, F#.",

        "Logisches Programmierparadigma beruht auf mathematischer Logik mit Fakten und Regeln.\n\
        Beispiel: Prolog.\n\
        Programm antwortet auf Anfragen durch Anwendung von Regeln auf Fakten.",

        "Deklarative Programmierung ist ungewohnt für Menschen, da sie Lösungszustände beschreibt, nicht den Weg.\n\
        In der Praxis werden meist Mischformen aus deklarativen und imperativen Paradigmen genutzt.\n\
        Dies erhöht aber die Fehleranfälligkeit und kann die Lesbarkeit des Codes beeinträchtigen."
    ]

    fragen = [
        {
            "frage": "Was ist ein Vorteil von UML-Aktivitätsdiagrammen gegenüber Programmablaufplänen (PAP)?",
            "optionen": [
                "a) Sie sind veraltet und werden kaum genutzt.",
                "b) Sie können Algorithmen und Prozesse moderner und anschaulicher abbilden.",
                "c) Sie sind nur für Sicherheitsaspekte relevant.",
                "d) Sie sind ausschließlich für Hardwareplanung geeignet."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt ein Programmierparadigma grundsätzlich?",
            "optionen": [
                "a) Die Art der Programmiersprache.",
                "b) Das grundlegende Konzept für Aufbau und Ausführung von Programmen.",
                "c) Die Hardware, auf der das Programm läuft.",
                "d) Die grafische Oberfläche einer Anwendung."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Paradigmen gehören zu den imperativen Programmierparadigmen?",
            "optionen": [
                "a) Funktionale und logische Programmierung",
                "b) Strukturiertes, prozedurales und objektorientiertes Programmieren",
                "c) Deklarative und imperative Programmierung",
                "d) Keine der genannten"
            ],
            "antwort": "b"
        },
        {
            "frage": "Woran erkennt man einen Entwickler auf der Party?",
            "optionen": [
                "a) Am Hoodie und den Augenringen.",
                "b) Er fragt nach dem WLAN-Passwort vor dem Namen.",
                "c) Er bringt GitHub statt Bier mit.",
                "d) Er fragt: 'Wo ist das Production Environment?'"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein Merkmal des strukturierten Programmierparadigmas?",
            "optionen": [
                "a) Verzicht auf Sprunganweisungen (Goto) zugunsten von Kontrollstrukturen.",
                "b) Verwendung von unstrukturiertem Code.",
                "c) Keine Verwendung von Funktionen oder Prozeduren.",
                "d) Fokus auf deklarative Logik."
            ],
            "antwort": "a"
        },
        {
            "frage": "Welchen Zweck verfolgt das prozedurale Programmierparadigma?",
            "optionen": [
                "a) Programme sollen möglichst lang und komplex sein.",
                "b) Quelltexte wiederverwendbar und übersichtlich machen durch Aufteilung in Prozeduren oder Funktionen.",
                "c) Programmierung ohne Kontrollstrukturen.",
                "d) Nur für künstliche Intelligenz geeignet."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist charakteristisch für das objektorientierte Programmierparadigma?",
            "optionen": [
                "a) Es ist eine veraltete Methode.",
                "b) Es ist eine Weiterentwicklung anderer Paradigmen und heute Standard in vielen Bereichen.",
                "c) Es wird nur für kleine Programme genutzt.",
                "d) Es beschreibt nur deklarative Programmierung."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was beschreibt das deklarative Programmierparadigma?",
            "optionen": [
                "a) Die genaue Reihenfolge der Abarbeitung von Befehlen.",
                "b) Nur das gewünschte Ergebnis, nicht wie es erreicht wird.",
                "c) Nur imperative Befehle.",
                "d) Die Hardware des Computers."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche zwei Paradigmen sind die wichtigsten Arten der deklarativen Programmierung?",
            "optionen": [
                "a) Strukturiert und prozedural",
                "b) Funktional und logisch",
                "c) Objektorientiert und strukturiert",
                "d) Imperativ und prozedural"
            ],
            "antwort": "b"
        },
        {
            "frage": "Wofür wird das funktionale Programmierparadigma oft eingesetzt?",
            "optionen": [
                "a) Für Webdesign.",
                "b) Für künstliche Intelligenz und Compilerbau.",
                "c) Nur für einfache Skripte.",
                "d) Für Datenbankverwaltung."
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist eine Herausforderung bei der Verwendung von Mischformen aus deklarativen und imperativen Paradigmen?",
            "optionen": [
                "a) Erhöhte Fehleranfälligkeit und beeinträchtigte Lesbarkeit des Codes.",
                "b) Weniger Funktionen im Programm.",
                "c) Kein Einsatz von Kontrollstrukturen möglich.",
                "d) Keine Vorteile gegenüber reinem imperativen Programmieren."
            ],
            "antwort": "a"
        }
    ]

    modul_lernen_und_testen("8.3.1 - Programmierparadigmen unterscheiden", lerninhalte, fragen)

def modul88():
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
        "Dynamische Bindung entscheidet zur Laufzeit, welche Methode ausgeführt wird.",

        "Datenquellen können über verschiedene Netzwerkprotokolle angesprochen werden: FTP, HTTP, NFS, SMB.",
        "Für verschlüsselte Übertragungen kommen SFTP oder FTPS zum Einsatz (siehe auch Lernfeld 3 und 9).",
        "APIs ermöglichen Zugriff auf Datenquellen mit mehr Anpassungsmöglichkeiten und Zugriffsmethoden.",
        "Zugriff auf Datenquellen im Internet kann über WebDAV, SOAP oder REST erfolgen.",
        "SOAP ist ein standardisiertes, protokollbasiertes Netzwerkprotokoll auf XML-Basis mit hoher Komplexität.",
        "SOAP bietet integrierte Standards wie ACID, Sicherheit, Konsistenz und ist geeignet für Unternehmenslösungen.",
        "SOAP-Nachrichten basieren auf XML, können über HTTP, SMTP, TCP übertragen werden.",
        "WSDL ist eine Beschreibungssprache für Webservices auf XML-Basis und vereinfacht die SOAP-Nutzung.",
        "REST ist eine moderne, leichtgewichtige Alternative zu SOAP, nutzt HTTP-Methoden: GET, POST, PUT, DELETE.",
        "REST eignet sich für IoT, mobile Anwendungen, Cloud-Anbieter (z. B. AWS, Azure) und ist zukunftsorientiert.",
        "REST folgt sechs Prinzipien: Client-Server-Modell, Zustandslosigkeit, Caching, einheitliche Schnittstelle, Layered System, Code-on-Demand.",
        "REST erfordert kein XML, ist einfacher zu implementieren, aber bietet weniger standardisierte Sicherheit als SOAP."
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
            "frage": "Was ist der Unterschied zwischen einem Entwickler und einem Magier?",
            "optionen": [
                "a) Der Entwickler kann Bugs beschwören.",
                "b) Der Magier kennt seine Zaubersprüche.",
                "c) Der Entwickler muss alles dreimal erklären.",
                "d) Beim Entwickler funktioniert's nur auf seinem Gerät."
            ],
            "antwort": "d"
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
        },
        {
            "frage": "Welche der folgenden Protokolle ermöglichen den Zugriff auf externe Datenquellen?",
            "optionen": ["a) FTP, HTTP, SMB", "b) WSDL, REST, SMTP", "c) JSON, XML, SOAP", "d) ACID, NFS, XML"],
            "antwort": "a"
        },
        {
            "frage": "Was ist ein Vorteil von REST gegenüber SOAP?",
            "optionen": ["a) Höhere Sicherheit", "b) Komplexere Transaktionskontrolle",
                         "c) Weniger Ressourcenverbrauch und einfachere Anwendung", "d) Pflicht zur XML-Nutzung"],
            "antwort": "c"
        },
        {
            "frage": "Welche Prinzipien sollte ein REST-Service aufweisen? (Mehrfachantwort möglich)",
            "optionen": ["a) Caching", "b) Zustandslosigkeit", "c) Code-on-Demand", "d) Stateful Session Management"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Welche Aussage zu SOAP ist korrekt?",
            "optionen": ["a) SOAP nutzt JSON als Standardformat", "b) SOAP ist ein leichtgewichtiges Protokoll",
                         "c) SOAP basiert auf XML-Nachrichten", "d) SOAP wird ausschließlich über HTTP verwendet"],
            "antwort": "c"
        },
        {
            "frage": "Wofür steht die Abkürzung WSDL?",
            "optionen": ["a) Web Server Description Language", "b) Web Services Description Language",
                         "c) Wide Service Data Layer", "d) Web Storage Definition Layout"],
            "antwort": "b"
        },
        {
            "frage": "Welche HTTP-Methoden werden typischerweise in REST verwendet? (Mehrfachantwort möglich)",
            "optionen": ["a) GET", "b) POST", "c) DELETE", "d) FETCH"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Warum wird SOAP trotz seiner Komplexität noch eingesetzt?",
            "optionen": ["a) Es ist einfacher zu erlernen", "b) Es ist älter und unterstützt veraltete Systeme",
                         "c) Es benötigt kein XML", "d) Es ersetzt REST vollständig"],
            "antwort": "b"
        },
        {
            "frage": "Welche Vorteile bietet WSDL bei der Nutzung von SOAP?",
            "optionen": ["a) Es ersetzt XML vollständig", "b) Es ermöglicht die Verwendung von JSON",
                         "c) Es beschreibt Webservices ohne direktes XML-Coding", "d) Es ist ein Ersatz für REST"],
            "antwort": "c"
        },
        {
            "frage": "Was beschreibt das ACID-Prinzip in Bezug auf SOAP? (Mehrfachantwort möglich)",
            "optionen": ["a) Atomizität", "b) Konsistenz", "c) Isolation", "d) Dauerhaftigkeit"],
            "antwort": ["a", "b", "c", "d"]
        },
        {
            "frage": "Welcher REST-API-Aufruf erstellt eine neue Ressource?",
            "optionen": ["a) GET", "b) POST", "c) PUT", "d) DELETE"],
            "antwort": "b"
        },
        {
            "frage": "Was bewirkt die HTTP-Methode DELETE in einer REST-API?",
            "optionen": ["a) Ruft eine Ressource ab", "b) Aktualisiert eine Ressource", "c) Löscht eine Ressource",
                         "d) Erstellt eine Ressource"],
            "antwort": "c"
        },
        {
            "frage": "Welche Rolle spielt XML bei SOAP?",
            "optionen": ["a) Keine", "b) XML ist optional", "c) SOAP basiert vollständig auf XML",
                         "d) XML wird nur bei REST verwendet"],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Objektorientierte Programmierung", lerninhalte, fragen)

def modul89():
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

    modul_lernen_und_testen("Unified Modeling Language", lerninhalte, fragen)

def modul810():
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
            "frage": "Warum gehen Entwickler selten raus?",
            "optionen": [
                "a) Draußen gibt’s kein Stack Overflow.",
                "b) Weil draußen kein Dark Mode ist.",
                "c) Weil draußen keine Semikolons gebraucht werden.",
                "d) Weil draußen die Variable 'Wetter' unbestimmt ist."
            ],
            "antwort": "b"
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

    modul_lernen_und_testen("Das Anwendungsfalldiagramm", lerninhalte, fragen)

def modul811():
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
            "frage": "Was bedeutet 'Works on my machine' wirklich?",
            "optionen": [
                "a) Ich hab's kaputtgeliebt.",
                "b) Ich habe keine Ahnung, warum es funktioniert.",
                "c) Es liegt an dir, nicht an mir.",
                "d) Ich hab keine Lust mehr."
            ],
            "antwort": "c"
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

def modul812():
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

def modul813():
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
            "frage": "Was sagt der Server, wenn er gestresst ist?",
            "optionen": [
                "a) 503 Service Unavailable.",
                "b) Ich brauch mehr Kaffee.",
                "c) Kernel Panic!",
                "d) Ich bin raus – Ctrl + Alt + Goodbye."
            ],
            "antwort": "a"
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

def modul814():
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
            "frage": "Wie nennt man einen DAU mit Adminrechten?",
            "optionen": [
                "a) Apokalypso.",
                "b) Root des Bösen.",
                "c) Sicherheitslücke mit Tastatur.",
                "d) Ein Bug mit Bonusrechten."
            ],
            "antwort": "c"
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

def modul815():
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
            "frage": "Was passiert, wenn man einen ITler um 3 Uhr nachts anruft?",
            "optionen": [
                "a) Er rebootet aus Reflex.",
                "b) Er sagt 'Hast du es neu gestartet?'",
                "c) Er flüstert '127.0.0.1...'",
                "d) Bluescreen der Seele."
            ],
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

def modul816():
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
            "frage": "Warum haben Programmierer keine Angst vor Geistern?",
            "optionen": [
                "a) Sie kennen alle Hintergrundprozesse.",
                "b) Sie debuggen sogar Spuk.",
                "c) Sie sehen schlimmere Dinge im Code.",
                "d) Geister brauchen keine Ports."
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

def modul817():
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
            "frage": "Was ist der Lieblingssport eines Informatikers?",
            "optionen": [
                "a) Java-Run",
                "b) Ping-Pong",
                "c) Datenjogging",
                "d) SQL-Slalom"
            ],
            "antwort": "b"
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

def modul818():
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
           "frage": "Wieso ist ein IT-Sicherheitsexperte schlecht beim Flirten?",
           "optionen": [
               "a) Er blockt alles.",
               "b) Er vertraut niemandem.",
               "c) Er fragt zuerst nach Zwei-Faktor-Authentifizierung.",
               "d) Er hat Angst vor Datenverlust."
           ],
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

def modul819():
    lerninhalte =[
        "Grafische Benutzeroberflächen (GUIs) in Java ermöglichen eine komplexere Interaktion als Konsolenanwendungen.",
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
        "WindowBuilder kann über den Eclipse Marketplace installiert und verwendet werden."]


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
            "frage": "Was trinkt ein Programmierer im Sommer?",
            "optionen": [
                "a) Iced Java",
                "b) PHP-Schorle",
                "c) HTML-Tonic",
                "d) Coldbrew-Loop"
            ],
            "antwort": "a"
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

    modul_lernen_und_testen("Lernfeld 8.3.5.4 Grafische Benutzerschnittstellen in Java entwickeln", lerninhalte, fragen)

def modul820():
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
            "frage": "Was macht ein DAU, wenn die Maus nicht funktioniert?",
            "optionen": [
                "a) Er streichelt sie.",
                "b) Er ruft die IT an.",
                "c) Er tauscht die Batterien im Bildschirm.",
                "d) Er klickt lauter."
            ],
            "antwort": "d"
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

def modul821():
    lerninhalte = [
            "Grafische Benutzeroberflächen (GUIs) unterscheiden sich von Konsolenanwendungen durch ihre Interaktionsmöglichkeiten.\n\
            GUIs bieten viele Oberflächenelemente (Widgets) und ermöglichen benutzerfreundliche Eingaben und Ausgaben.\n\
            Das Entwerfen benutzerfreundlicher Oberflächen ist aufwendig und erfordert Planung.",

            "Zur Erstellung von GUIs in Python benötigt man Toolkits wie Tkinter, PyQt oder PyObject.\n\
            Tkinter ist in der Standardbibliothek enthalten und muss nicht extra installiert werden.\n\
            PyQt ist ein Binding für das Qt-Toolkit, PyObject für Gtk – beide müssen zusätzlich installiert werden.",

            "Grundstruktur eines GUI-Programms in Tkinter:\n\
            - Import des tkinter-Moduls\n\
            - Erstellen eines Fensters mit tkinter.Tk()\n\
            - Setzen von Eigenschaften wie Titel und Größe\n\
            - Hinzufügen von Widgets wie Button, Label, Entry\n\
            - mainloop() hält das Fenster offen und verarbeitet Ereignisse.",

            "Ein Button wird mit ttk.Button erstellt und über .place() positioniert.\n\
            Ein Beispiel ist ein Fenster mit einem Button „Beenden“, der mit einer Methode verknüpft ist.\n\
            Die Methode zerstört das Fenster mit frmMain.destroy().",

            "Beispielaufgabe: Ein GUI-Programm berechnet Tankkosten basierend auf Menge und Preis.\n\
            - Eingabe: Litermenge und Preis pro Liter\n\
            - Algorithmus: kosten = menge * preis\n\
            - Ausgabe: Ergebnis in einem Eingabefeld anzeigen\n\
            Fehler werden mit messagebox.showwarning behandelt."
        ]

    fragen = [
            {
                "frage": "Was ist ein Hauptunterschied zwischen GUI und Konsolenanwendung?",
                "optionen": ["a) GUIs können keine Eingaben verarbeiten.",
                             "b) GUIs benötigen keinen Code.",
                             "c) GUIs bieten vielfältigere Interaktionsmöglichkeiten.",
                             "d) Konsolenanwendungen sind grafisch komplexer."],
                "antwort": "c"
            },
            {
                "frage": "Welches Toolkit ist in Python bereits enthalten und muss nicht installiert werden?",
                "optionen": ["a) PyQt", "b) PyObject", "c) Gtk", "d) Tkinter"],
                "antwort": "d"
            },
            {
                "frage": "Welche Aussage über PyQt ist korrekt?",
                "optionen": ["a) Es basiert auf Gtk.",
                             "b) Es ist ein Binding für Qt und muss installiert werden.",
                             "c) Es ist Bestandteil von Python.",
                             "d) Es ersetzt tkinter."],
                "antwort": "b"
            },
            {
                "frage": "Was ist die Funktion von frmMain.mainloop() im Tkinter-Programm?",
                "optionen": ["a) Es beendet das Fenster.",
                             "b) Es definiert die Fenstergröße.",
                             "c) Es hält das Fenster offen und verarbeitet Ereignisse.",
                             "d) Es erstellt alle Widgets."],
                "antwort": "c"
            },
            {
                "frage": "Was passiert, wenn der Button mit dem Befehl frmMain.destroy() verknüpft ist?",
                "optionen": ["a) Das Programm wird gespeichert.",
                             "b) Das Hauptfenster wird geschlossen.",
                             "c) Ein neues Fenster öffnet sich.",
                             "d) Ein Fehler wird ausgegeben."],
                "antwort": "b"
            },
            {
                "frage": "Was muss für ein Binding wie PyQt oder PyObject zusätzlich geschehen?",
                "optionen": ["a) Es wird automatisch geladen.",
                             "b) Es muss programmiert werden.",
                             "c) Es muss extra installiert werden.",
                             "d) Es ist in tkinter enthalten."],
                "antwort": "c"
            },
            {
                "frage": "Warum hassen Entwickler Meetings?",
                "optionen": [
                    "a) Kein Debug-Modus.",
                    "b) Keine Escape-Taste.",
                    "c) Kein Return möglich.",
                    "d) Alles ohne Syntax."
                ],
                "antwort": "b"
            },
            {
                "frage": "Welche Widgets werden im Tankkosten-Beispiel verwendet? (Mehrere Antworten möglich)",
                "optionen": ["a) Label", "b) Entry", "c) Combobox", "d) Button"],
                "antwort": ["a", "b", "d"]
            },
            {
                "frage": "Was berechnet die Methode btnCalc_click() im Beispielprogramm?",
                "optionen": ["a) Das Durchschnittsgewicht",
                             "b) Die Summe zweier Zahlen",
                             "c) Die Tankkosten anhand Menge und Preis",
                             "d) Die Fenstergröße"],
                "antwort": "c"
            },
            {
                "frage": "Wie wird ein Button in Tkinter erzeugt?",
                "optionen": ["a) button = Button.create()",
                             "b) btn = ttk.Button(frm, text='...', command=...)",
                             "c) Button = new Window()",
                             "d) window.create_button(...)"],
                "antwort": "b"
            },
            {
                "frage": "Was geschieht, wenn bei der Berechnung ein Fehler auftritt?",
                "optionen": ["a) Das Programm stürzt ab.",
                             "b) Es passiert nichts.",
                             "c) Eine Warnung wird über messagebox angezeigt.",
                             "d) Der Button verschwindet."],
                "antwort": "c"
            }
        ]

    modul_lernen_und_testen("Lernfeld 8.6.2 Grafische Benutzerschnittstellen in Python entwickeln", lerninhalte, fragen)

def modul822():
    lerninhalte = [
        "Zur Entwicklung bedarfsgerechter Datenbanklösungen muss das Wissen über Datenbanken und SQL erweitert werden.\n\
        Es stehen verschiedene Datenmodelle und Datenbankmanagementsysteme zur Verfügung, die sorgfältig ausgewählt werden müssen.",

        "Datenarten: strukturierte, semistrukturierte und unstrukturierte Daten.\n\
        Früher lag der Fokus auf strukturierten Daten, heute wächst der Anteil unstrukturierter Daten stark an –\n\
        z.B. durch IoT, KI, 5G, Edge Computing, neue Geschäftsmodelle.",

        "Big Data beschreibt große, komplexe, sich schnell ändernde Datenmengen.\n\
        Die 5 Vs von Big Data: Volume (Menge), Variety (Vielfalt), Velocity (Verarbeitungsgeschwindigkeit),\n\
        Veracity (Vertrauenswürdigkeit), Value (Mehrwert).",

        "Relationale Datenbanken speichern strukturierte Daten in Tabellen, erfordern feste Schemata, skalieren vertikal,\n\
        unterstützen ACID-Regeln und verwenden SQL.\n\
        Bekannte Systeme: MySQL, PostgreSQL, Oracle, MS-SQL. Einsatz bei stabiler Struktur und ACID-Pflicht.",

        "NoSQL-Datenbanken unterstützen strukturierte, semi- und unstrukturierte Daten, skalieren horizontal,\n\
        nutzen BASE statt ACID und haben keine einheitliche Abfragesprache.\n\
        Modelle: Dokumenten-, Graph- oder Key-Value-Datenbanken. Beispiele: MongoDB, Apache HBase, Amazon DB.",

        "Relationale Datenbanken setzen auf vertikale Skalierung (ein Server), NoSQL auf horizontale (mehrere Server).\n\
        NoSQL eignet sich besonders bei stark wachsender Datenmenge oder flexibler Struktur."
    ]

    fragen = [
        {
            "frage": "Was ist Ziel der Entwicklung bedarfsgerechter Datenbanklösungen?",
            "optionen": ["a) Reduktion von Datenmengen", "b) Vereinfachung von Hardware",
                         "c) Systemübergreifende Datenbereitstellung", "d) Vermeidung von Internetzugriffen"],
            "antwort": "c"
        },
        {
            "frage": "Welche der folgenden Aussagen trifft auf unstrukturierte Daten zu? (Mehrere Antworten möglich)",
            "optionen": ["a) Können Fotos oder Audiodateien sein", "b) Werden in Spalten gespeichert",
                         "c) Müssen vor Speicherung konvertiert werden", "d) Kommen häufig bei Big Data vor"],
            "antwort": ["a", "d"]
        },
        {
            "frage": "Was beschreibt der Begriff Big Data?",
            "optionen": ["a) Kleine Datenmengen mit hohem Mehrwert",
                         "b) Große, komplexe und dynamische Datenmengen",
                         "c) Daten aus relationalen Systemen",
                         "d) Eine SQL-Datenbank"],
            "antwort": "b"
        },
        {
            "frage": "Was ist schlimmer als ein Bug?",
            "optionen": [
                "a) Ein Feature.",
                "b) Ein Nutzer mit Feedback.",
                "c) Ein Bug, der intermittent ist.",
                "d) Zwei Bugs, die sich gegenseitig triggern."
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Eigenschaften zählen zu den 5 Vs von Big Data? (Mehrere Antworten möglich)",
            "optionen": ["a) Value", "b) Velocity", "c) Validation", "d) Veracity"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Technologien fördern das Datenwachstum? (Mehrere Antworten möglich)",
            "optionen": ["a) Internet of Things", "b) SQL-Abfragen", "c) Künstliche Intelligenz", "d) Edge Computing"],
            "antwort": ["a", "c", "d"]
        },
        {
            "frage": "Was trifft auf relationale Datenbanken zu?",
            "optionen": ["a) Unterstützen BASE-Modell", "b) Skalieren horizontal",
                         "c) Speichern Daten in Tabellen", "d) Nutzen Graphmodelle"],
            "antwort": "c"
        },
        {
            "frage": "Welche Abfragesprache wird typischerweise in relationalen Datenbanken verwendet?",
            "optionen": ["a) MongoQL", "b) SQL", "c) NoScript", "d) XML"],
            "antwort": "b"
        },
        {
            "frage": "Welche Vorteile bieten NoSQL-Datenbanken? (Mehrere Antworten möglich)",
            "optionen": ["a) Flexibilität für verschiedene Datenarten",
                         "b) Unterstützung aller ACID-Regeln",
                         "c) Horizontale Skalierbarkeit",
                         "d) Einheitliche Abfragesprache"],
            "antwort": ["a", "c"]
        },
        {
            "frage": "Was beschreibt das BASE-Modell in NoSQL-Datenbanken?",
            "optionen": ["a) Binary Access, Shared Environment",
                         "b) Basically Available, Soft State, Eventually Consistent",
                         "c) Basic System Architecture Evaluation",
                         "d) Balanced Availability State Execution"],
            "antwort": "b"
        },
        {
            "frage": "Wann sind relationale Datenbanken vorzuziehen?",
            "optionen": ["a) Wenn die Datenstruktur häufig wechselt",
                         "b) Wenn große Datenmengen flexibel verarbeitet werden sollen",
                         "c) Wenn ACID-Unterstützung notwendig ist",
                         "d) Wenn keine feste Struktur vorhanden ist"],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.7.1 Datenbanklösungen bedarfsgerecht entwickeln", lerninhalte, fragen)

def modul823():
    lerninhalte = [
        "Relationale Datenbanken sind zentrale Werkzeuge für Unternehmen und Behörden zur Speicherung, Verwaltung und Auswertung\n\
        großer Datenmengen. Ihre Qualität ist entscheidend, weshalb sie sorgfältig entworfen und umgesetzt werden müssen.\n\
        Der Designprozess relationaler Datenbanken umfasst typischerweise vier Phasen: Analyse, konzeptionelle Phase, logische\n\
        Phase und Implementationsphase. Man unterscheidet zwischen DBMS-unabhängigen und DBMS-abhängigen Phasen.",
        "1. Analysephase: In dieser Phase werden die Anforderungen des Kunden durch eine Anforderungsanalyse ermittelt und\n\
        strukturiert. Das Ergebnis ist eine informelle Beschreibung des zu lösenden Problems.",
        "2. Konzeptionelle Phase: Ziel ist eine formalisierte Beschreibung des Sachverhalts. Am bekanntesten ist das\n\
        Entity-Relationship-Modell (ER-Modell), das Entitätstypen, Attribute, Beziehungen und Kardinalitäten (z.B. 1:1, 1:n, m:n)\n\
        beschreibt.",
        "3. Logische Phase: Das konzeptionelle Modell wird in ein relationales Datenmodell überführt. Zuerst wird das ER-Modell\n\
        in ein relationales Modell umgesetzt, dann wird dieses Modell durch Normalisierung optimiert.",
        "4. Implementationsphase: Das logische Modell wird mithilfe von SQL in ein konkretes Datenbankschema überführt. Es werden\n\
        Tabellen mit Primär- (PK) und Fremdschlüsseln (FK), Datentypen und Wertebereichen definiert.\n\
        Beispiel: CREATE TABLE Hersteller (HNr INTEGER, Name VARCHAR(50), PRIMARY KEY(HNr)).",
        "Bei einfachen Datenstrukturen kann man konzeptionelle und logische Phase zusammenfassen, sollte dies jedoch sorgfältig\n\
        abwägen, da spätere Änderungen in relationalen Datenbanken aufwendig sind. Ein schlechtes logisches Design führt langfristig\n\
        zu Problemen – auch wenn es kurzzeitig durch leistungsfähige Hardware kompensiert werden kann.",
        "Beispiel – Buchverleih einer Bibliothek:\nAnalysephase: Die Datenbank soll Kundendaten (Kundennummer, Name, Adresse,\n\
        Telefonnummer), Buchdaten (Titel, ISBN, Auflage, Verlag, Nummer, Anschaffungsdatum) und Verleihvorgänge (Buch, Kunde,\n\
        Ausleih- und Rückgabedatum) verwalten.\nKonzeptionelle Phase: Erstellung eines ER-Modells mit den genannten Entitäten\n\
        und Beziehungen.\nLogische Phase: Ableitung eines relationalen Modells (noch nicht normalisiert), mit Tabellen für Kunde,\n\
        Buch und Verleihvorgang sowie Primär- und Fremdschlüsseln.",
        "Die Normalisierung des relationalen Modells folgt im nächsten Abschnitt und wird hier noch nicht behandelt."
    ]

    fragen = [
        {
            "frage": "Warum sind relationale Datenbanken für Unternehmen und Behörden wichtig?",
            "optionen": ["a) Sie ersetzen Mitarbeiter vollständig.",
                         "b) Sie ermöglichen die Verwaltung großer Datenmengen.",
                         "c) Sie können nicht verändert werden.",
                         "d) Sie sind immer kostenlos."],
            "antwort": "b"
        },
        {
            "frage": "Welche vier Phasen umfasst der Designprozess relationaler Datenbanken?",
            "optionen": ["a) Planung, Ausführung, Abschluss, Bewertung",
                         "b) Analyse, Entwicklung, Kontrolle, Test",
                         "c) Analyse, konzeptionelle Phase, logische Phase, Implementationsphase",
                         "d) Definition, Design, Ausführung, Analyse"],
            "antwort": "c"
        },
        {
            "frage": "Was ist das Ziel der Analysephase?",
            "optionen": ["a) Erstellung eines SQL-Skripts",
                         "b) Auswertung von Nutzerdaten",
                         "c) Erstellung eines informellen Problemberichts durch Anforderungsanalyse",
                         "d) Berechnung von Speicherbedarf"],
            "antwort": "c"
        },
        {
            "frage": "Was wird typischerweise in der konzeptionellen Phase verwendet?",
            "optionen": ["a) JSON-Modell",
                         "b) ER-Modell",
                         "c) Python-Modul",
                         "d) Tabellenkalkulation"],
            "antwort": "b"
        },
        {
            "frage": "Wie nennt man ein WLAN ohne Passwort?",
            "optionen": [
                "a) Freie Liebe.",
                "b) Honeypot.",
                "c) Router-Roulette.",
                "d) Ein offenes Geständnis."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Elemente enthält ein ER-Modell?",
            "optionen": ["a) Nur Tabellen",
                         "b) Beziehungen, Entitätstypen, Attribute, Kardinalitäten",
                         "c) Nur Attribute",
                         "d) Nur Beziehungen"],
            "antwort": "b"
        },
        {
            "frage": "Was ist das Ziel der logischen Phase?",
            "optionen": ["a) Die Hardwarekonfiguration zu bestimmen",
                         "b) Das ER-Modell direkt in Code zu übersetzen",
                         "c) Das ER-Modell in ein relationales Modell zu überführen und zu normalisieren",
                         "d) Die SQL-Befehle zu testen"],
            "antwort": "c"
        },
        {
            "frage": "Was passiert in der Implementationsphase?",
            "optionen": ["a) Es wird ein Betriebssystem installiert",
                         "b) Das relationale Modell wird mit SQL als Datenbankschema umgesetzt",
                         "c) Kundenkontakte werden gespeichert",
                         "d) Benutzeroberflächen werden erstellt"],
            "antwort": "b"
        },
        {
            "frage": "Was sollte beachtet werden, wenn man konzeptionelle und logische Phase zusammenfasst?",
            "optionen": ["a) Es spart auf jeden Fall Zeit und ist immer zu empfehlen.",
                         "b) Änderungen sind später einfach vorzunehmen.",
                         "c) Änderungen an relationalen Datenbanken sind später sehr aufwendig.",
                         "d) Die Implementationsphase wird überflüssig."],
            "antwort": "c"
        },
        {
            "frage": "Was kann ein schlechtes logisches Design kurzfristig kompensieren?",
            "optionen": ["a) Gute Beziehungen",
                         "b) Leistungsfähige Hardware",
                         "c) Kleine Datenmengen",
                         "d) Gute Nutzerführung"],
            "antwort": "b"
        },
        {
            "frage": "Welche Informationen sollen in der Bibliotheksdatenbank gespeichert werden?",
            "optionen": ["a) Nur Ausleihdaten",
                         "b) Kundenname, Ausleihdatum, Rückgabeort",
                         "c) Kundendaten, Buchdaten, Verleihvorgänge",
                         "d) Rechnungsdaten und Mahnungen"],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.7.2 Den Prozess des Designs relationaler Datenbanken beschreiben", lerninhalte, fragen)

def modul824():
    lerninhalte = [
        "Normalisierung ist ein Verfahren zur Reduzierung von Datenredundanz und zur Erhöhung der Datenkonsistenz in relationalen\n\
        Datenbankmodellen.",
        "Ziel ist es, Tabellenstrukturen zu optimieren, sodass sie bestimmten Normalformen (NF) entsprechen. Üblich sind 1. bis\n\
        3. NF, höhere NF werden selten angewendet.",
        "Erste Normalform (1. NF): Alle Attribute enthalten nur atomare (einfache) Werte. Mehrwertige oder strukturierte Felder\n\
        müssen aufgeteilt werden.",
        "Zweite Normalform (2. NF): Die Tabelle befindet sich in der 1. NF und alle Nichtschlüsselattribute sind vom gesamten\n\
        Primärschlüssel funktional abhängig. Teilschlüsselabhängigkeiten werden eliminiert.",
        "Dritte Normalform (3. NF): Zusätzlich zur 2. NF dürfen keine transitiven Abhängigkeiten zwischen Nichtschlüsselattributen\n\
        bestehen.",
        "Beispiel zur 1. NF: Die Tabelle 'Bestellung' wird aufgeteilt, sodass aus 'Bestellpositionen' eigene Spalten für Pos, Anzahl,\n\
        Bezeichnung, ANr entstehen. Primärschlüssel wird aus BestellNr und Pos gebildet.",
        "Beispiel zur 2. NF: Datum, KNr, Name werden aus der Tabelle 'Bestellungen' ausgelagert, da sie nur von BestellNr abhängen,\n\
        nicht vom gesamten zusammengesetzten Schlüssel (BestellNr, Pos).",
        "Beispiel zur 3. NF: KNr und Name sowie ANr und Bezeichnung werden jeweils in eigene Tabellen ausgelagert (Kunde, Artikel),\n\
        um transitive Abhängigkeiten zu vermeiden.",
        "Durch die 3. NF entstehen vier verknüpfte Tabellen: Bestellung, BestellPosition, Kunde und Artikel. Redundanzen werden so\n\
        effektiv reduziert.",
        "Weitere Normalformen (4. NF, 5. NF) existieren, sind jedoch in der Praxis selten. Nachteile der Normalisierung sind u.a.\n\
        erhöhter Aufwand bei Abfragen durch mehr Tabellen und Joins."
    ]

    fragen = [
        {
            "frage": "Was ist das Hauptziel der Normalisierung in relationalen Datenbanken?",
            "optionen": ["a) Erhöhung der Datenmenge",
                         "b) Reduzierung der Komplexität durch mehr Tabellen",
                         "c) Reduzierung von Redundanz und Erhöhung der Konsistenz",
                         "d) Verbesserung der Benutzeroberfläche"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage trifft auf die erste Normalform (1. NF) zu?",
            "optionen": ["a) Alle Spalten müssen Fremdschlüssel sein",
                         "b) Es dürfen keine Zahlen in den Attributen vorkommen",
                         "c) Alle Werte müssen atomar sein",
                         "d) Alle Attribute müssen Texte enthalten"],
            "antwort": "c"
        },
        {
            "frage": "Was passiert bei der Überführung einer Tabelle in die 1. NF?",
            "optionen": ["a) Mehrere Tabellen werden zusammengeführt",
                         "b) Alle Attribute werden zu einem einzigen kombiniert",
                         "c) Aufzählungen und mehrwertige Felder werden aufgeteilt",
                         "d) Alle Spalten werden gelöscht"],
            "antwort": "c"
        },
        {
            "frage": "Wann befindet sich eine Tabelle in der zweiten Normalform (2. NF)?",
            "optionen": ["a) Wenn sie die 3. NF erfüllt",
                         "b) Wenn alle Nichtschlüsselattribute vom gesamten Primärschlüssel abhängen",
                         "c) Wenn sie keine Spalten enthält",
                         "d) Wenn sie keine Fremdschlüssel enthält"],
            "antwort": "b"
        },
        {
            "frage": "Welche Spalten wurden im Beispiel bei der 2. NF ausgelagert?",
            "optionen": ["a) BestellNr und Pos",
                         "b) Datum, KNr, Name",
                         "c) Anzahl und Bezeichnung",
                         "d) Kunde und Artikel"],
            "antwort": "b"
        },
        {
            "frage": "Welche Bedingung gilt für die dritte Normalform (3. NF)?",
            "optionen": ["a) Alle Attribute müssen Fremdschlüssel sein",
                         "b) Keine Spalte darf leer sein",
                         "c) Keine transitive Abhängigkeit darf bestehen",
                         "d) Alle Tabellen müssen zusammengeführt werden"],
            "antwort": "c"
        },
        {
            "frage": "Welche Abhängigkeit besteht in der Tabelle 'Bestellung', die eine Verletzung der 3. NF darstellt?",
            "optionen": ["a) BestellNr → Datum",
                         "b) KNr → Name",
                         "c) ANr → Anzahl",
                         "d) Pos → BestellNr"],
            "antwort": "b"
        },
        {
            "frage": "Welche Aussage trifft auf die dritte Normalform zu?",
            "optionen": ["a) Sie beseitigt teilschlüsselabhängige Attribute",
                         "b) Sie wird vor der ersten Normalform angewendet",
                         "c) Sie beseitigt redundante Fremdschlüssel",
                         "d) Sie beseitigt transitive Abhängigkeiten"],
            "antwort": "d"
        },
        {
            "frage": "Wie werden die Tabellen nach der Überführung in die 3. NF miteinander verbunden?",
            "optionen": ["a) Durch numerische Reihenfolge",
                         "b) Durch 1:n-Beziehungen über Schlüssel",
                         "c) Durch die Anzahl der Felder",
                         "d) Durch Spaltennamen"],
            "antwort": "b"
        },
        {
            "frage": "Welche Nachteile können bei zu starker Normalisierung entstehen?",
            "optionen": ["a) Datenverlust",
                         "b) Schlechtere Performance durch komplexere Abfragen",
                         "c) Mehr Redundanzen",
                         "d) Fehlende Primärschlüssel"],
            "antwort": "b"
        },
        {
            "frage": "Warum benutzen Hacker Linux?",
            "optionen": [
                "a) Weil sie es können.",
                "b) Weil sudo wie 'abrakadabra' ist.",
                "c) Weil Windows fragt: 'Sind Sie sicher?'",
                "d) Weil die Kommandozeile sexy ist."
            ],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.7.3 Relationale Datenmodelle normalisieren ", lerninhalte, fragen)

def modul825():
    lerninhalte = [
        "Erweiterung des SQL-Basiswissens um neue Anweisungen.\n\
        Zentrale Anweisungen: CREATE/DROP DATABASE, CREATE/ALTER/DROP TABLE,\n\
        INSERT, UPDATE, DELETE sowie SELECT mit Aggregatfunktionen und Operatoren.\n\
        Abfragen über mehrere Tabellen können klassisch (FROM/WHERE) oder modern (JOIN) umgesetzt werden.",

        "Klassische Mehrtabellenabfrage: Tabellen in FROM-Klausel, Verknüpfung über WHERE.\n\
        Moderne Methode: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN in FROM-Klausel mit ON-Bedingung.\n\
        Unterschiedliche JOIN-Arten liefern unterschiedliche Ergebnismengen.\n\
        LEFT JOIN zeigt z.B. alle Einträge der linken Tabelle – auch ohne passende Gegenstücke in rechter Tabelle.",

        "Mit UNION (bzw. UNION ALL) lassen sich Ergebnismengen kombinieren.\n\
        Voraussetzung: gleiche Anzahl an Spalten mit gleichem Datentyp.\n\
        UNION entfernt doppelte Werte, UNION ALL nicht.\n\
        Beispiel: SELECT O.Name FROM Ort UNION SELECT L.Name FROM Land;",

        "Unterabfragen (Subqueries) liefern Werte, die in übergeordneter SQL-Anweisung verwendet werden.\n\
        Können einen oder mehrere Werte zurückgeben.\n\
        Bei Einzelwertvergleichen: Vergleichsoperatoren (=, <, >, etc.), oft in Verbindung mit Aggregatfunktionen (AVG, MAX, etc.).\n\
        Mehrwertige Unterabfragen benötigen Mengenoperatoren: IN, EXISTS, ALL, ANY.",

        "Beispiel Einzelwert-Unterabfrage:\n\
        SELECT O.Name, O.Einwohner FROM Ort O WHERE O.Einwohner > (SELECT AVG(O.Einwohner) FROM Ort O)\n\
        Beispiel mehrwertige Unterabfrage mit IN:\n\
        DELETE FROM Ort O WHERE O.LandID = (SELECT L.LandID FROM Land L WHERE L.Name = 'Malta')"
    ]

    fragen = [
        {
            "frage": "Welche Anweisung wird zum Erstellen einer Datenbank verwendet?",
            "optionen": ["a) CREATE DATABASE", "b) NEW DATABASE", "c) INIT DATABASE", "d) MAKE DATABASE"],
            "antwort": "a"
        },
        {
            "frage": "Welche SQL-Befehle dienen dem Bearbeiten von Tabellen?",
            "optionen": ["a) CREATE, ALTER, DROP", "b) SELECT, INSERT, UPDATE", "c) JOIN, UNION, GROUP",
                         "d) OPEN, MODIFY, DELETE"],
            "antwort": "a"
        },
        {
            "frage": "Welche JOIN-Art liefert alle Werte der linken Tabelle, auch wenn keine Übereinstimmung in der rechten besteht?",
            "optionen": ["a) INNER JOIN", "b) LEFT JOIN", "c) RIGHT JOIN", "d) FULL JOIN"],
            "antwort": "b"
        },
        {
            "frage": "Welche Bedingung muss für eine UNION erfüllt sein?",
            "optionen": ["a) Tabellen müssen gleich heißen", "b) Spaltennamen müssen identisch sein",
                         "c) Gleiche Anzahl und Typ der Spalten", "d) Nur Primärschlüssel dürfen verwendet werden"],
            "antwort": "c"
        },
        {
            "frage": "Welche Funktion wird verwendet, um den Durchschnitt einer Spalte zu berechnen?",
            "optionen": ["a) AVG()", "b) SUM()", "c) COUNT()", "d) MEAN()"],
            "antwort": "a"
        },
        {
            "frage": "Was bewirkt der Befehl „UNION ALL“ im Vergleich zu „UNION“?",
            "optionen": ["a) Nur eindeutige Werte anzeigen", "b) Auch doppelte Werte anzeigen",
                         "c) Alle Zeilen aus der ersten Tabelle anzeigen", "d) Nur NULL-Werte ausschließen"],
            "antwort": "b"
        },
        {
            "frage": "Wie lautet die klassische Variante, um Länder aus Europa auszugeben?",
            "optionen": ["a) SELECT L.Name FROM Land WHERE Kontinent = 'Europa';",
                         "b) SELECT Name FROM Land JOIN Kontinent WHERE K = 'Europa';",
                         "c) SELECT L.Name, K.Bezeichnung FROM Land L, Kontinent K WHERE L.KontinentID = K.KontinentID AND K.Bezeichnung = 'Europa';",
                         "d) SELECT Europa FROM Land, Kontinent;"],
            "antwort": "c"
        },
        {
            "frage": "Wie beginnt eine Unterabfrage, die in einer WHERE-Klausel eingebettet ist?",
            "optionen": ["a) WITH SELECT ...", "b) START SELECT ...", "c) WHERE SELECT ...", "d) (SELECT ...)"],
            "antwort": "d"
        },
        {
            "frage": "Welche Operatoren benötigt man bei Unterabfragen mit mehreren Werten?",
            "optionen": ["a) +, -, *", "b) IS, LIKE", "c) IN, EXISTS, ANY, ALL", "d) HAVING, JOIN"],
            "antwort": "c"
        },
        {
            "frage": "Was trifft auf JOINs zu?",
            "optionen": ["a) JOINs funktionieren nur mit einer Tabelle",
                         "b) JOINs erlauben das Kombinieren mehrerer Tabellen über Schlüsselbeziehungen",
                         "c) JOINs werden nur bei INSERT verwendet",
                         "d) JOINs ignorieren NULL-Werte vollständig"],
            "antwort": "b"
        },
        {
            "frage": "Was gibt folgender SQL-Befehl zurück? SELECT O.Name, K.Bezeichnung FROM Ort O INNER JOIN Land L ON O.LandID = L.LandID INNER JOIN Kontinent K ON L.KontinentID = K.KontinentID WHERE K.Bezeichnung = 'Europa' AND O.Name LIKE 'B%';",
            "optionen": ["a) Orte weltweit mit beliebigem Anfangsbuchstaben",
                         "b) Länder in Europa",
                         "c) Orte in Europa, deren Name mit B beginnt",
                         "d) Kontinente mit Ort-IDs"],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Beispiel für eine Unterabfrage mit Aggregatfunktion?",
            "optionen": ["a) SELECT MAX(Ort) FROM Einwohner;",
                         "b) DELETE * FROM Ort WHERE Einwohner > ALL;",
                         "c) SELECT O.Name FROM Ort O WHERE O.Einwohner > (SELECT AVG(O.Einwohner) FROM Ort O);",
                         "d) AVG(SELECT Einwohner FROM Ort);"],
            "antwort": "c"
        },
        {
            "frage": "Wofür steht das Schlüsselwort EXISTS?",
            "optionen": ["a) Überprüft, ob eine Tabelle existiert",
                         "b) Führt nur INSERT aus",
                         "c) Prüft, ob ein oder mehrere Ergebnisse in der Unterabfrage existieren",
                         "d) Wird mit GROUP BY kombiniert"],
            "antwort": "c"
        },
        {
            "frage": "Was macht dieser SQL-Befehl? DELETE FROM Ort O WHERE O.LandID = (SELECT L.LandID FROM Land L WHERE L.Name = 'Malta')",
            "optionen": ["a) Löscht alle Länder außer Malta",
                         "b) Löscht alle Orte, die in Malta liegen",
                         "c) Fügt Orte in Malta hinzu",
                         "d) Ändert den Namen von Malta"],
            "antwort": "b"
        },
        {
            "frage": "Was macht die Funktion COUNT()?",
            "optionen": ["a) Summiert alle Werte", "b) Zählt NULL-Werte", "c) Zählt Einträge in einer Spalte",
                         "d) Berechnet Durchschnitt"],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage ist korrekt bezüglich FULL JOIN?",
            "optionen": ["a) Zeigt nur die Werte der rechten Tabelle",
                         "b) Zeigt alle Werte beider Tabellen – auch ohne Verknüpfung",
                         "c) Ist identisch mit INNER JOIN",
                         "d) Muss mit DELETE kombiniert werden"],
            "antwort": "b"
        },
        {
            "frage": "Wie unterscheidet sich LEFT JOIN von INNER JOIN?",
            "optionen": ["a) LEFT JOIN benötigt kein ON",
                         "b) LEFT JOIN zeigt auch Einträge der linken Tabelle ohne Partner in der rechten",
                         "c) Es gibt keinen Unterschied",
                         "d) LEFT JOIN kann nur mit GROUP BY verwendet werden"],
            "antwort": "b"
        },
        {
            "frage": "Welche Einschränkung besteht bei UNION?",
            "optionen": ["a) Tabellen müssen gleich benannt sein",
                         "b) Es dürfen keine JOINs verwendet werden",
                         "c) Spalten müssen in Anzahl und Datentyp übereinstimmen",
                         "d) Nur auf Primärschlüssel anwendbar"],
            "antwort": "c"
        },
        {
            "frage": "Was gibt SELECT MIN(Einwohner) FROM Ort; zurück?",
            "optionen": ["a) Den Namen des kleinsten Orts", "b) Die ID des größten Orts",
                         "c) Die Einwohnerzahl des kleinsten Orts", "d) NULL"],
            "antwort": "c"
        },
        {
            "frage": "Wozu dient der LIKE-Operator in SQL?",
            "optionen": ["a) Zum Verknüpfen von Tabellen", "b) Für Mustervergleiche in Zeichenketten",
                         "c) Für mathematische Berechnungen", "d) Für Aggregatfunktionen"],
            "antwort": "b"
        },
        {
            "frage": "Wie testet man, ob ein ITler Single ist?",
            "optionen": [
                "a) Man fragt ihn nach seinem IDE.",
                "b) Man schaut auf seine Bildschirmzeit.",
                "c) Man fragt: 'Was ist Wochenende?'",
                "d) Man entfernt das Internet."
            ],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.7.4 Das Basiswissen über SQL erweitern und anwenden", lerninhalte, fragen)

def modul826():
    lerninhalte = [
        "MySQL ist ein relationales Datenbankmanagementsystem (RDBMS), das SQL verwendet und besonders für seine Performance\n\
        und Plattformvielfalt bekannt ist. Es wurde 1994 von MySQLAB entwickelt und gehört seit 2010 zu Oracle.",
        "MySQL arbeitet nach dem Client-Server-Prinzip mit einem MySQL-Server und einem oder mehreren Clients. Es besitzt keine\n\
        eigene GUI, weshalb externe Lösungen notwendig sind.",
        "Die aktuelle MySQL-Version kann unter https://dev.mysql.com/downloads/ heruntergeladen werden.",
        "Java kann über JDBC mit einer MySQL-Datenbank kommunizieren. Dazu muss die Treiberklasse geladen und eine Verbindung\n\
        mit 'DriverManager.getConnection(...)' hergestellt werden.",
        "Ein Java-Programm kann SQL-Anweisungen wie CREATE, INSERT, UPDATE, DELETE, SELECT, DROP über ein Statement-Objekt an MySQL senden.",
        "Das Beispielprojekt zeigt eine Verbindung zu 'Ortverwaltung', mit SQL-Anweisungen zur Tabellenerstellung und Datenabfrage\n\
        per ResultSet.",
        "Fehlerbehandlung erfolgt durch try-catch-Blöcke mit Auswertung der SQLException (Message, SQLState, VendorError).",
        "Die Auswertung eines ResultSets erfolgt in einer while-Schleife über 'rs.next()'. Zugriff auf Spalten erfolgt über\n\
        'getString()', 'getInt()' etc."
    ]

    fragen = [
        {"frage": "Was ist MySQL?",
         "optionen": ["a) Eine Programmiersprache",
                      "b) Ein Betriebssystem",
                      "c) Ein relationales Datenbankmanagementsystem",
                      "d) Ein Grafikprogramm"],
         "antwort": "c"},

        {"frage": "Wer entwickelte MySQL ursprünglich?",
         "optionen": ["a) Microsoft",
                      "b) Oracle",
                      "c) MySQLAB",
                      "d) IBM"],
         "antwort": "c"},

        {"frage": "Seit wann gehört MySQL zu Oracle?",
         "optionen": ["a) 2005",
                      "b) 2010",
                      "c) 2015",
                      "d) 2000"],
         "antwort": "b"},

        {"frage": "Was benötigt man, um eine MySQL-Datenbank mit Java anzusprechen?",
         "optionen": ["a) Nur die Klasse Main",
                      "b) Eine GUI",
                      "c) JDBC-Treiber und eine Verbindung",
                      "d) HTML und CSS"],
         "antwort": "c"},

        {"frage": "Welche SQL-Anweisung erzeugt eine Tabelle?",
         "optionen": ["a) SELECT",
                      "b) INSERT",
                      "c) CREATE TABLE",
                      "d) DELETE"],
         "antwort": "c"},
        {
            "frage": "Was ist das Gegenteil von Plug & Play?",
            "optionen": [
                "a) Plug & Pray.",
                "b) Boot & Schrei.",
                "c) Code & Wut.",
                "d) Stack & Overflow."
            ],
            "antwort": "a"
        },

        {"frage": "Wie lautet der Standard-Port von MySQL?",
         "optionen": ["a) 80",
                      "b) 443",
                      "c) 3306",
                      "d) 21"],
         "antwort": "c"},

        {"frage": "Wie wird ein SQL-Befehl in Java ausgeführt?",
         "optionen": ["a) con.insert()",
                      "b) sqlStatement.executeUpdate(sql)",
                      "c) rs.execute(sql)",
                      "d) Driver.run(sql)"],
         "antwort": "b"},

        {"frage": "Was liefert ein SELECT-Befehl in Java zurück?",
         "optionen": ["a) String",
                      "b) ResultSet",
                      "c) Boolean",
                      "d) Connection"],
         "antwort": "b"},

        {"frage": "Welche Methode liest eine Zeichenkette aus einem ResultSet?",
         "optionen": ["a) rs.readString()",
                      "b) rs.getText()",
                      "c) rs.getString()",
                      "d) rs.fetch()"],
         "antwort": "c"},

        {"frage": "Was macht die Methode rs.next()?",
         "optionen": ["a) Gibt das letzte Element zurück",
                      "b) Startet die Verbindung",
                      "c) Iteriert über die Zeilen eines ResultSets",
                      "d) Führt SQL aus"],
         "antwort": "c"},

        {"frage": "Was passiert bei einem SQLException-Fehler?",
         "optionen": ["a) Das Programm fährt fort ohne Meldung",
                      "b) Es wird eine neue Datenbank erstellt",
                      "c) Die Exception muss abgefangen und behandelt werden",
                      "d) Die Verbindung wird sofort gelöscht"],
         "antwort": "c"},

        {"frage": "Wie lautet der Befehl zum Laden der Treiberklasse?",
         "optionen": ["a) LoadDriver()",
                      "b) DriverManager.load()",
                      "c) Class.forName(...)",
                      "d) ImportDriver()"],
         "antwort": "c"},

        {"frage": "Was enthält das Statement: 'DriverManager.getConnection(...)'?",
         "optionen": ["a) Die SQL-Abfrage",
                      "b) Die JDBC-Verbindungsdaten",
                      "c) Das GUI-Fenster",
                      "d) Das ResultSet"],
         "antwort": "b"},

        {"frage": "Welche Methoden zum Schließen einer Verbindung werden verwendet?",
         "optionen": ["a) con.end() und statement.stop()",
                      "b) con.close() und sqlStatement.close()",
                      "c) statement.delete() und con.destroy()",
                      "d) rs.quit()"],
         "antwort": "b"},

        {"frage": "Wie erkennt man, dass eine Verbindung erfolgreich war?",
         "optionen": ["a) Es erscheint ein GUI-Fenster",
                      "b) Die Konsole gibt eine Bestätigung aus",
                      "c) Es wird ein Fehler geworfen",
                      "d) Die Tabelle wird automatisch erstellt"],
         "antwort": "b"},

        {"frage": "Was passiert in der Methode 'updateDB(String sql)'?",
         "optionen": ["a) Ein SQL-Statement wird ausgewertet",
                      "b) Eine Tabelle wird automatisch angezeigt",
                      "c) SQL-Anweisungen wie INSERT, DELETE werden ausgeführt",
                      "d) Daten werden exportiert"],
         "antwort": "c"},

        {"frage": "Wie erfolgt der Zugriff auf Daten im ResultSet?",
         "optionen": ["a) Über getField()",
                      "b) Über getColumn()",
                      "c) Über getString() und getInt() je nach Datentyp",
                      "d) Direkt aus dem Statement"],
         "antwort": "c"},

        {"frage": "Welche Datenbankname wird im Beispiel verwendet?",
         "optionen": ["a) KontinentDB",
                      "b) Ortverwaltung",
                      "c) myDB",
                      "d) GeoDaten"],
         "antwort": "b"},

        {"frage": "Welche Klasse enthält die Datenbankverbindung im Beispiel?",
         "optionen": ["a) Program",
                      "b) JDBCConnection",
                      "c) MySQLConnection",
                      "d) SQLHandler"],
         "antwort": "c"},

        {"frage": "Welche Tabelle wird im Hauptprogramm erstellt?",
         "optionen": ["a) Land",
                      "b) Ort",
                      "c) Kontinent",
                      "d) Verwaltung"],
         "antwort": "c"}
    ]

    modul_lernen_und_testen("Lernfeld 8.7.5 Eine MySQL-Datenbank mit Java ansprechen ", lerninhalte, fragen)

def modul827():
    lerninhalte = [
        "NoSQL-Datenbanken (Not only SQL) ergänzen relationale Datenbanken, besonders bei unstrukturierten oder unbekannten Daten\n\
        – z.B. in Big-Data-Anwendungen.\n\
        Sie verwenden keine Tabellen mit festen Spalten und Zeilen, sondern organisieren Daten mit flexiblen Modellen.\n\
        Die vier Haupttypen von NoSQL-Datenbanken sind: dokumentenorientiert, graphbasiert, spaltenbasiert und Key-Value-orientiert.",

        "Dokumentenorientierte Datenbanken speichern Daten in Dokumenten, oft im JSON-Format.\n\
        Jedes Dokument kann unterschiedlich aufgebaut sein und besitzt einen eindeutigen Identifikator.\n\
        Besonders geeignet für Content-Management-Systeme, Blogs oder dynamische Webanwendungen.\n\
        Beispiele: CouchDB, Firestore, DocumentDB.\n\
        Vorteil: einfache Erweiterbarkeit, keine feste Struktur notwendig.\n\
        Nachteil: schwer bei stark verknüpften Daten.",

        "Graphdatenbanken bestehen aus Knoten (Datenpunkte), Kanten (Beziehungen) und deren Eigenschaften.\n\
        Verwendet für stark vernetzte Informationen, z. B. soziale Netzwerke oder Betrugserkennung.\n\
        Beziehungen besitzen Richtung und Typ und können eigene Attribute haben.\n\
        Beispiele: Neo4j, OrientDB, Neptune.\n\
        Vorteil: performanter bei komplexen Beziehungen.\n\
        Nachteil: komplexere Datenmodellierung nötig.",

        "Key-Value-Datenbanken speichern Daten als Schlüssel-Wert-Paare.\n\
        Der Key ist eindeutig und wird extern gespeichert – nicht im Datensatz selbst.\n\
        Ähnlich dokumentenbasiert, aber ohne strukturierte Felder.\n\
        Sehr performant bei Zugriffen über Schlüssel, hohe horizontale Skalierbarkeit.\n\
        Nachteile: eingeschränkte Abfragefunktionalität, keine komplexen Beziehungen möglich."
    ]

    fragen = [
        {
            "frage": "Was bedeutet NoSQL?",
            "optionen": ["a) Nur SQL", "b) Keine SQL-Abfragen erlaubt", "c) Not only SQL",
                         "d) Neuer organisierter SQL"],
            "antwort": "c"
        },
        {
            "frage": "Was macht ein Entwickler beim Psychologen?",
            "optionen": [
                "a) Einen Core-Dump.",
                "b) Einen Bugreport.",
                "c) Ein Git-Reset.",
                "d) Ein Ticket aufmachen."
            ],
            "antwort": "a"
        },
        {
            "frage": "Welche Aussage beschreibt dokumentenorientierte Datenbanken korrekt?",
            "optionen": [
                "a) Sie nutzen Tabellen mit festen Schemata",
                "b) Alle Dokumente müssen gleich aufgebaut sein",
                "c) Sie nutzen flexible Dokumente im JSON-Format",
                "d) Sie speichern Daten nur in XML-Dateien"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Vorteil von Key-Value-Datenbanken?",
            "optionen": [
                "a) Relationale Abfragen sind effizienter",
                "b) Daten lassen sich in mehreren Tabellen verknüpfen",
                "c) Sehr schnelle Zugriffe über eindeutige Schlüssel",
                "d) Sie speichern Daten in Baumstrukturen"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage zu Graphdatenbanken ist falsch?",
            "optionen": [
                "a) Sie speichern Daten als Knoten und Kanten",
                "b) Sie sind optimal für komplexe Beziehungen",
                "c) Jede Kante kann eigene Attribute besitzen",
                "d) Sie nutzen SQL zur Modellierung von Beziehungen"
            ],
            "antwort": "d"
        },
        {
            "frage": "Wofür eignen sich dokumentenorientierte Datenbanken besonders?",
            "optionen": [
                "a) Für komplexe mathematische Berechnungen",
                "b) Für Webinhalte und Blogs",
                "c) Für einfache Schlüssel-Wert-Relationen",
                "d) Für massive tabellarische Massendaten"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was trifft auf Key-Value-Datenbanken zu?",
            "optionen": [
                "a) Schlüssel sind optional",
                "b) Werte enthalten nur Ganzzahlen",
                "c) Hohe Skalierbarkeit durch horizontale Verteilung",
                "d) Komplexe JOINs werden bevorzugt"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche NoSQL-Kategorie nutzt Knoten und Kanten zur Modellierung?",
            "optionen": ["a) Dokumentenorientiert", "b) Key-Value", "c) Spaltenorientiert", "d) Graphbasiert"],
            "antwort": "d"
        },
        {
            "frage": "Was ist ein Nachteil von Key-Value-Datenbanken?",
            "optionen": [
                "a) Kein schneller Zugriff auf Schlüssel",
                "b) Komplizierter Aufbau der Knoten",
                "c) Eingeschränkte Suchfunktionen",
                "d) Kein horizontaler Betrieb möglich"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was unterscheidet eine dokumentenorientierte DB von einer relationalen?",
            "optionen": [
                "a) Strukturlose Dokumente mit variablen Attributen",
                "b) Tabellen mit festem Schema",
                "c) Abfragen über mehrere Fremdschlüssel",
                "d) Daten nur als Text gespeichert"
            ],
            "antwort": "a"
        },
        {
            "frage": "Welches Datenformat wird häufig in dokumentenbasierten Datenbanken genutzt?",
            "optionen": ["a) CSV", "b) XML", "c) JSON", "d) YAML"],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfeld 8.7.6 NoSQL-Datenbanken und deren Datenmodelle unterscheiden", lerninhalte, fragen)

def modul828():
    lerninhalte = [
        "MongoDB ist ein dokumentbasiertes NoSQL-Datenbankmanagementsystem, das oft in der modernen Anwendungsentwicklung und in der Cloud eingesetzt wird.\n\
Es ist Open-Source und auf Windows, MacOS und Linux verfügbar. Die verwalteten Dokumente sind im JSON-ähnlichen Format.\n\
Eine Datenbank in MongoDB enthält Collections – Gruppen von Dokumenten, vergleichbar mit Tabellen in relationalen Datenbanken.\n\
Einzelne Dokumente können mit `insert_one(...)`, mehrere mit `insert_many(...)` eingefügt werden.\n\
Die `find_one(...)`-Funktion gibt genau ein Dokument zurück, während `find(...)` mehrere Dokumente liefert, die typischerweise mit einer Schleife ausgegeben werden.\n\
Zur Verwendung in Python muss das Paket `pymongo` installiert werden, z. B. mit `python -m pip install pymongo`.\n\
Der Zugriff erfolgt über das `MongoClient`-Objekt, das eine Verbindung zur Datenbank herstellt.\n\
Beispiel für Datenbankzugriff:\n\
`from pymongo import MongoClient`\n\
`db = MongoClient('mongodb://localhost:27017/')['artikelverwaltung_db']`\n\
`collection = db['artikel']`\n\
Einfügen einzelner Dokumente:\n\
`collection.insert_one({...})`\n\
Mehrere Dokumente:\n\
`collection.insert_many([{...}, {...}])`\n\
Daten abfragen:\n\
`collection.find_one({''artikel_nr'': ''1234''})`\n\
    `for d in collection.find({''hersteller'': ''Möbel GmbH''}): print(d)`"
    ]

    fragen = [
        {
            "frage": "Was ist MongoDB?",
            "optionen": [
                "a) Eine relationale Datenbank",
                "b) Eine dokumentbasierte NoSQL-Datenbank",
                "c) Ein Dateisystem",
                "d) Eine Tabellenkalkulation"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was muss installiert sein, um MongoDB mit Python zu nutzen?",
            "optionen": [
                "a) sqlite3",
                "b) mongoengine",
                "c) pymongo",
                "d) mysql-connector"
            ],
            "antwort": "c"
        },
        {
            "frage": "Warum war der Server traurig?",
            "optionen": [
                "a) Weil er niemanden pingen konnte.",
                "b) Weil alle Ports geschlossen waren.",
                "c) Weil der Loadbalancer unfair war.",
                "d) Weil er sich entkabelt fühlte."
            ],
            "antwort": "a"
        },
        {
            "frage": "Welche Aussage zur Funktion `insert_one(...)` trifft zu?",
            "optionen": [
                "a) Fügt mehrere Dokumente ein",
                "b) Löscht ein Dokument",
                "c) Fügt ein einzelnes Dokument in eine Collection ein",
                "d) Ruft ein Dokument ab"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Funktion wird verwendet, um mehrere Dokumente gleichzeitig zu speichern?",
            "optionen": [
                "a) insert_many(...)",
                "b) insert_all(...)",
                "c) write_many(...)",
                "d) store_many(...)"
            ],
            "antwort": "a"
        },
        {
            "frage": "Welche dieser Aussagen ist korrekt?",
            "optionen": [
                "a) `find(...)` gibt nur ein Dokument zurück",
                "b) `find_one(...)` liefert eine Liste",
                "c) `find(...)` kann mehrere Dokumente liefern",
                "d) `insert_one(...)` wird für mehrere Datensätze verwendet"
            ],
            "antwort": "c"
        },
        {
            "frage": "Wie stellt man eine Verbindung zu MongoDB her?",
            "optionen": [
                "a) MongoDB.connect(...)",
                "b) MongoClient('mongodb://localhost:27017/')",
                "c) mongo.open('localhost')",
                "d) connect_mongo('localhost')"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist eine Collection in MongoDB?",
            "optionen": [
                "a) Eine SQL-Tabelle",
                "b) Ein Dateiverzeichnis",
                "c) Eine Gruppe von Dokumenten",
                "d) Ein Modul zur Verschlüsselung"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Ausgabe erzeugt der folgende Code?\n`print(collection.find_one({\"artikel_nr\": \"1234\"}))`",
            "optionen": [
                "a) Fügt einen Artikel mit Nummer 1234 ein",
                "b) Löscht Artikel 1234",
                "c) Gibt das Dokument mit Artikelnummer 1234 aus",
                "d) Listet alle Artikel mit dieser Nummer"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welcher Befehl installiert pymongo korrekt?",
            "optionen": [
                "a) install pymongo",
                "b) pip install pymongo",
                "c) python install pymongo",
                "d) python -m pip install pymongo"
            ],
            "antwort": "d"
        },
        {
            "frage": "Was wird mit `for d in collection.find(...)` erreicht?",
            "optionen": [
                "a) Alle Dokumente werden bearbeitet",
                "b) Nur das erste Dokument wird gelöscht",
                "c) Ein einzelnes Dokument wird angezeigt",
                "d) Die Datenbank wird initialisiert"
            ],
            "antwort": "a"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.7.7 Die NoSQL-Datenbank 'MongoDB' mit Python ansprechen ", lerninhalte, fragen)

def modul829():
    lerninhalte = [
        "Cloud-Datenbanken sind ein wachsender Bereich im Cloud-Markt und werden als Database as a Service (DBaaS) angeboten.\n\
        Es gibt universelle und spezialisierte Angebote, inklusive relationaler und NoSQL-Datenbanken.\n\
        Das DBaaS-Modell umfasst Betrieb, Wartung, Administration sowie Sicherung, Skalierung und Sicherheit der Datenbank.\n\
        Vorteile sind Flexibilität, schnelle Markteinführung, geringe Risiken durch Hochverfügbarkeit und SLAs sowie niedrigere\n\
        Kosten durch Pay-per-Use und dynamische Skalierung.",

        "Es gibt vier Modelle des Cloud-Datenbankmanagements:\n\
        - Selbstverwaltete: maximale Kontrolle, hohe Verantwortung für DBAs\n\
        - Automatisierte: APIs, voller Zugriff, eingeschränkte SLAs\n\
        - Verwaltete: kein Serverzugriff, eingeschränkte Konfigurierbarkeit\n\
        - Autonome: KI-basierte Automatisierung aller Verwaltungsaufgaben, inklusive Sicherheit, Backups, Optimierung.\n\
        Autonome Datenbanken erkennen Hardwarefehler und skalieren Leistung/Kapazität automatisch.",

        "Anbieter-Vergleich:\n\
        - Amazon: Relationale DBs (SQL Server, Oracle, MySQL, PostgreSQL, Aurora), NoSQL (DynamoDB, DocumentDB), Graph (Neptune),\n\
          Data Warehouse (Redshift).\n\
          Unterstützt Migration durch AWS DMS und Schema Conversion Tool (für Views, Stored Procedures, Embedded SQL).\n\
        - Microsoft: Relationale DBs (Azure SQL, MySQL, PostgreSQL, MariaDB), NoSQL (Cosmos DB, Azure Table Storage, Redis),\n\
          SQL Data Warehouse.\n\
          Migration über Azure Database Migration Service."
    ]

    fragen = [
        {
            "frage": "Was ist DBaaS?",
            "optionen": ["a) Ein lokales Datenbankmodell", "b) Eine Serverhardware",
                         "c) Eine Datenbanknutzung als Cloud-Service", "d) Eine Datenbanksoftware zum Kauf"],
            "antwort": "c"
        },
        {
            "frage": "Welche Datenbanktypen sind typischerweise im Cloud-Bereich vertreten?",
            "optionen": ["a) Nur relationale", "b) Nur NoSQL", "c) Relationale und NoSQL", "d) Nur Graphdatenbanken"],
            "antwort": "c"
        },
        {
            "frage": "Wie erkennt man einen Praktikanten im Rechenzentrum?",
            "optionen": [
                "a) Er fragt, wo der WLAN-Stick steckt.",
                "b) Er föhnt die Lüfter trocken.",
                "c) Er tippt direkt auf dem Servergehäuse.",
                "d) Er löscht das BIOS zur 'Entrümpelung'."
            ],
            "antwort": "a"
        },
        {
            "frage": "Was tut ein Programmierer, wenn er sich verliebt?",
            "optionen": [
                "a) Er pushed zu viel.",
                "b) Er forked Beziehungen.",
                "c) Er bekommt Merge-Konflikte.",
                "d) Er verliert seine Branch-Kontrolle."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was gehört *nicht* zu den Vorteilen von Cloud-Datenbanken?",
            "optionen": ["a) Schnelle Bereitstellung", "b) Hohe Einmalkosten", "c) Pay-per-Use", "d) Skalierbarkeit"],
            "antwort": "b"
        },
        {
            "frage": "Welche Aufgaben übernimmt ein Anbieter beim DBaaS-Modell? (Mehrere Antworten möglich)",
            "optionen": ["a) Wartung", "b) Datensicherung", "c) Serverinstallation durch Kunden",
                         "d) Hochverfügbarkeit"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Aussage zur selbstverwalteten Cloud-Datenbank stimmt?",
            "optionen": ["a) Keine manuelle Verwaltung nötig", "b) Nur eingeschränkte Kontrolle",
                         "c) Höchste Flexibilität und Verantwortung beim Kunden",
                         "d) Vollautomatisiert durch Anbieter"],
            "antwort": "c"
        },
        {
            "frage": "Was ist ein Merkmal autonomer Cloud-Datenbanken?",
            "optionen": ["a) Keine Nutzung von Machine Learning", "b) Volle manuelle Kontrolle erforderlich",
                         "c) Automatisierte Verwaltung durch KI", "d) Keine Skalierung möglich"],
            "antwort": "c"
        },
        {
            "frage": "Welche Datenbankprodukte bietet Amazon an? (Mehrere Antworten möglich)",
            "optionen": ["a) DynamoDB", "b) Redshift", "c) Oracle", "d) Cosmos DB"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Wofür dient das AWS Schema Conversion Tool?",
            "optionen": ["a) Um Datenbanken zu sichern", "b) Um Server zu skalieren",
                         "c) Um Datenbankschema zu konvertieren", "d) Um SQL-Anfragen zu löschen"],
            "antwort": "c"
        },
        {
            "frage": "Welche Services zählen zu Microsofts DBaaS-Angeboten? (Mehrere Antworten möglich)",
            "optionen": ["a) Cosmos DB", "b) MariaDB", "c) Azure Table Storage", "d) Neptune"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Welche Rolle spielt Machine Learning in autonomen Datenbanken?",
            "optionen": ["a) Keine", "b) Unterstützt die Migration",
                         "c) Ermöglicht Automatisierung von Verwaltungstätigkeiten", "d) Nur zur Datensicherung"],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("Lernfelder 8.7.8 Cloud-basierte Datenbanklösungen unterscheiden", lerninhalte, fragen)

def modul830():
    lerninhalte = [
        "Beim Testen von Software kommen verschiedene Testverfahren zum Einsatz.\n"
        "Diese lassen sich in zwei Hauptarten einteilen: Black-Box-Tests und White-Box-Tests.\n"
        "White-Box-Tests sind strukturorientiert, da der Quellcode bekannt ist. Ziel ist eine möglichst hohe Testabdeckung.\n"
        "Sie müssen häufig angepasst werden, wenn sich der Quellcode ändert.\n"
        "Black-Box-Tests sind spezifikationsorientiert. Es wird geprüft, ob die Software die Anforderungen erfüllt – unabhängig vom Quellcode.\n"
        "Testdaten werden auf Basis der Anforderungsspezifikation abgeleitet, nicht aus dem Quellcode.\n"
        "Typische Teststufen: Unittest, Integrationstest, Systemtest.",

        "Zentrale Methoden zur Auswahl von Testdaten:\n"
        "– Äquivalenzklassenbildung: Eingabe- und Ausgabewerte werden in gültige und ungültige Klassen unterteilt.\n"
        "   Ziel: hohe Testabdeckung mit wenigen, repräsentativen Testfällen.\n"
        "– Grenzwertanalyse: Ergänzt die Äquivalenzklassenmethode. Fehler treten oft an Klassengrenzen auf (z.B. <= vs. <).\n"
        "   Es werden Testdaten an den Rändern der Klassen gewählt.",

        "Beispiel (beide Verfahren):\n"
        "Eine Methode `bool isTemperatureOk(double temp)` gibt True zurück, wenn die Temperatur ≤ 30 °C ist, sonst False.\n"
        "Äquivalenzklassen: 1. ≤ 30, 2. > 30. Mögliche Werte: [-1, 28, 3.89], [32, 101.33, 40].\n"
        "Grenzwerte: 30.00 → True, 30.01 → False.\n"
        "Funktion soll nur Werte mit zwei Nachkommastellen akzeptieren. Absolute Nullpunktgrenzen werden ignoriert.",

        "Entscheidungstabellen helfen bei der Ableitung von Testfällen – insbesondere bei einfacher Logik.\n"
        "Jede Spalte der Tabelle bildet einen Testfall ab. Komplexe Logik kann schnell unübersichtlich werden.\n"
        "Beispiel (Entscheidungstabelle):\n"
        "Sensor 1 sendet Signal = JA, Sensor 2 = NEIN ⇒ Alarm auslösen.",

        "Zur Dokumentation von Tests gehören unter anderem: Testprotokolle, Testfallbeschreibungen, Fehlerberichte und das Abnahmeprotokoll.\n"
        "Das Abnahmeprotokoll dokumentiert die formale Abnahme der Software durch den Auftraggeber."
    ]

    fragen = [
        {
            "frage": "Was zeichnet Black-Box-Tests aus?",
            "optionen": [
                "a) Der Quellcode wird analysiert.",
                "b) Die Testdaten basieren auf der Programmlogik.",
                "c) Es werden nur interne Abläufe getestet.",
                "d) Sie basieren auf der Anforderungsspezifikation."
            ],
            "antwort": "d"
        },
        {
            "frage": "Welche Aussage trifft auf White-Box-Tests zu?",
            "optionen": [
                "a) Sie sind unabhängig vom Quellcode.",
                "b) Sie müssen bei Codeänderungen nicht angepasst werden.",
                "c) Sie sind strukturorientiert und analysieren die Programmlogik.",
                "d) Sie testen ausschließlich die Benutzeroberfläche."
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Testdaten liefert die Äquivalenzklassenbildung?",
            "optionen": [
                "a) Nur ungültige Werte.",
                "b) Werte aus der Programmlogik.",
                "c) Repräsentative Werte aus gültigen und ungültigen Klassen.",
                "d) Nur Extremwerte."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was ist der Nachteil von White-Box-Tests?",
            "optionen": [
                "a) Keine Testabdeckung erreichbar.",
                "b) Muss bei jeder Änderung im Quellcode überprüft und angepasst werden.",
                "c) Sind unzuverlässig bei Systemtests.",
                "d) Benötigen keine Testdaten."
            ],
            "antwort": "b"
        },
        {
            "frage": "Wie funktioniert die Grenzwertanalyse?",
            "optionen": [
                "a) Durch Auswahl zufälliger Werte.",
                "b) Durch Testdaten an den Rändern von Äquivalenzklassen.",
                "c) Durch Vergleich von Codeblöcken.",
                "d) Durch Simulation von Systemabstürzen."
            ],
            "antwort": "b"
        },
        {
            "frage": "Welche Temperatur würde bei isTemperatureOk(temp) den Rückgabewert False erzeugen?",
            "optionen": [
                "a) 29.99",
                "b) 30.00",
                "c) 30.01",
                "d) -1"
            ],
            "antwort": "c"
        },
        {
            "frage": "Was trifft auf Entscheidungstabellen zu?",
            "optionen": [
                "a) Jede Zeile bildet einen Testfall.",
                "b) Sie sind ausschließlich für grafische Benutzeroberflächen geeignet.",
                "c) Sie sind ideal für komplexe Logik.",
                "d) Jede Spalte bildet einen Testfall ab."
            ],
            "antwort": "d"
        },
        {
            "frage": "Was passiert, wenn man 'rm -rf /' als Root ausführt?",
            "optionen": [
                "a) Ein Moment der Stille.",
                "b) Ein tiefer Blick in die Leere.",
                "c) Erleuchtung.",
                "d) Man wird Buddha mit Adminrechten."
            ],
            "antwort": "a"
        },
        {
            "frage": "Welches Verfahren eignet sich besonders zur Generierung von Testdaten an Schnittstellen?",
            "optionen": [
                "a) White-Box-Test",
                "b) Black-Box-Test",
                "c) Debugging",
                "d) Code-Review"
            ],
            "antwort": "b"
        },
        {
            "frage": "Was ist das Ziel eines Abnahmeprotokolls?",
            "optionen": [
                "a) Die Testumgebung zu beschreiben.",
                "b) Fehlerberichte zu speichern.",
                "c) Die formale Abnahme durch den Kunden zu dokumentieren.",
                "d) Logfiles zu archivieren."
            ],
            "antwort": "c"
        },
        {
            "frage": "Was gilt für die Methode isTemperatureOk(temp)? (Mehrfachantwort)",
            "optionen": [
                "a) Gibt True zurück, wenn temp ≤ 30.",
                "b) Temp = 30.00 ergibt True.",
                "c) Testwert 30.01 ergibt True.",
                "d) Es wird nur ein Rückgabewert True/False geliefert."
            ],
            "antwort": ["a", "b", "d"]
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.8 Software testen und dokumentieren", lerninhalte, fragen)

def modul831():
    lerninhalte = [
        "Testdatengeneratoren erzeugen synthetische Daten für Softwaretests, z.B. für Last-, Leistungs- und Stresstests.",
        "Sie werden verwendet, wenn reale Testdaten fehlen oder nicht ausreichen. Auch sensible Daten können durch Dummydaten ersetzt werden.",
        "Ein Testdatengenerator erzeugt Daten automatisch – durch Generierung, Modifikation, Auswahl oder aus Wissensdatenbanken.",
        "Sie sind besonders relevant für Big-Data-Anwendungen aufgrund ihres Volumens und ihrer Geschwindigkeit.",
        "Es gibt vier Hauptkategorien: datenbankbasierte, codebasierte, schnittstellenbasierte und spezifikationsbasierte Generatoren.",
        "Mockaroo ist ein beliebter, kostenloser Online-Testdatengenerator mit über 100 Datentypen, unterstützt CSV, JSON, SQL, Excel.",
        "Beispieldatensätze bei Mockaroo umfassen Felder wie ID, Land, Ländercode, Währung, Währungscode und Zeitzone."
    ]

    fragen = [
        {
            "frage": "Wozu dienen Testdatengeneratoren?",
            "optionen": ["a) Zur Analyse von Programmcode", "b) Zum Erzeugen synthetischer Testdaten",
                         "c) Zum Verschlüsseln von Daten", "d) Zur Kompilierung von Quellcode"],
            "antwort": "b"
        },
        {
            "frage": "Wann kommen Testdatengeneratoren besonders häufig zum Einsatz?",
            "optionen": ["a) Bei Produktivsystemen", "b) Wenn reale Testdaten fehlen oder zu wenige vorhanden sind",
                         "c) In der Designphase", "d) Nur bei manuellen Tests"],
            "antwort": "b"
        },
        {
            "frage": "Welche Arten von Tests ermöglichen Testdatengeneratoren?",
            "optionen": ["a) Last-, Leistungs-, Stresstests", "b) Design- und Architekturanalyse", "c) UI-Tests",
                         "d) Debugging von Produktionssystemen"],
            "antwort": "a"
        },
        {
            "frage": "Was kann ein Testdatengenerator leisten? (Mehrere Antworten möglich)",
            "optionen": ["a) Daten generieren", "b) Daten verändern", "c) Wissen extrahieren", "d) Daten selektieren"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Was ist der natürliche Feind eines Entwicklers?",
            "optionen": [
                "a) Ein nicht reproduzierbarer Fehler.",
                "b) Ein Kunde mit 'nur einer kleinen Änderung'.",
                "c) Montagmorgen ohne Kaffee.",
                "d) Internet Explorer."
            ],
            "antwort": "d"
        },
        {
            "frage": "Welche Kategorie gehört nicht zu den vier Hauptarten von Testdatengeneratoren?",
            "optionen": ["a) Schnittstellenbasiert", "b) Datenbankbasiert", "c) Speicherbasiert", "d) Codebasiert"],
            "antwort": "c"
        },
        {
            "frage": "Was kennzeichnet schnittstellenbasierte Testdatengeneratoren?",
            "optionen": ["a) Sie basieren auf Codeanalysen",
                         "b) Sie analysieren Schnittstellenparameter und nutzen Äquivalenzklassenanalyse",
                         "c) Sie werten GUI-Elemente aus", "d) Sie erzeugen ausschließlich JSON-Daten"],
            "antwort": "b"
        },
        {
            "frage": "Welche Datenformate unterstützt Mockaroo? (Mehrere Antworten möglich)",
            "optionen": ["a) CSV", "b) XML", "c) JSON", "d) Excel"],
            "antwort": ["a", "c", "d"]
        },
        {
            "frage": "Welche Eigenschaften bietet Mockaroo?",
            "optionen": ["a) Über 100 Datentypen, realistische Werte", "b) Nur Textdaten", "c) Nur Zufallszahlen",
                         "d) Nur für PostgreSQL"],
            "antwort": "a"
        },
        {
            "frage": "Wie sieht ein typischer Testdatensatz bei Mockaroo aus? (Mehrere Antworten möglich)",
            "optionen": ["a) ID", "b) Ländercode", "c) Farbcode", "d) Zeitzone"],
            "antwort": ["a", "b", "d"]
        },
        {
            "frage": "Welche Faktoren spielen bei der Toolwahl für Testdatengeneratoren eine Rolle?",
            "optionen": ["a) Datenbankunterstützung", "b) Preis", "c) Formatvielfalt", "d) Farbschema"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Welche Rolle spielen Dummy-Daten in Testdatengeneratoren?",
            "optionen": ["a) Sie verschlüsseln sensible Daten",
                         "b) Sie ersetzen vertrauliche Daten zur Wahrung der Datensicherheit",
                         "c) Sie erhöhen die Datenmenge künstlich", "d) Sie formatieren Metadaten"],
            "antwort": "b"
        },
        {
            "frage": "Warum sind Testdatengeneratoren für Big-Data-Anwendungen wichtig?",
            "optionen": ["a) Weil sie mit wenig RAM auskommen", "b) Wegen schneller, massenhafter Datenerzeugung",
                         "c) Sie benötigen keine Datenbank", "d) Sie ersetzen Datenbanken"],
            "antwort": "b"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.8.2 Testdatengeneratoren verwenden", lerninhalte, fragen)

def modul832():
    lerninhalte = [
        "Die Abnahme ist der Vorgang, bei dem der Auftraggeber die erstellte Software prüft und erklärt, dass sie den vertraglich vereinbarten Anforderungen entspricht.\n\
        Sie ist gesetzlich vorgeschrieben, wenn ein Werkvertrag besteht. Grundlage sind Vertrag oder Pflichtenheft.\n\
        Abnahme nach DIN 69901-5:2009-1 ist die Bestätigung, dass der Auftragnehmer die Anforderungen erfüllt hat.\n\
        Sie hat wichtige rechtliche Folgen: Zahlungsanspruch, Beginn der Mängelverjährung, Übergang der Beweislast.",

        "Arten der Abnahme:\n\
        - Vertragliche Akzeptanz: Vollständigkeit und Qualität der Leistungen, gesetzliche Anforderungen.\n\
        - Benutzerakzeptanz: Funktionale und nichtfunktionale Anforderungen (z. B. Tests, Dokumentation).\n\
        - Betreiberakzeptanz: IT-Sicherheit, Revisionssicherheit, Admin-Handbücher.",

        "Das Abnahmeprotokoll dokumentiert Ort, Datum, Teilnehmer, geprüfte Eigenschaften, offene Punkte usw.\n\
        Es muss von Auftraggeber und Auftragnehmer (oder deren Vertretern) unterschrieben werden.\n\
        Standards wie PMBOK oder PRINCE2 geben keine strengen Vorgaben für Abnahmeprotokolle.\n\
        Eine Checkliste mit den Abnahmekriterien ist Mindestinhalt, empfohlen sind weitere Details.",

        "Beispielhafte Inhalte im Abnahmeprotokoll:\n\
        - Software & Version, Vertragsnummer\n\
        - Getestete Anforderungen mit Ergebnissen (funktional, nichtfunktional, technisch)\n\
        - Offene Punkte mit Terminen oder Verzicht\n\
        - Schlussbeurteilung und Freigabe durch beide Parteien.",

        "Beispiel (Auszug):\n\
        Software: Statistika Version 1.0\n\
        Funktionale Anforderung: Vier grafische Darstellungsmöglichkeiten – erfüllt\n\
        Nichtfunktionale Anforderung: Bedienungsanleitung – vorhanden\n\
        Technische Anforderung: Lauffähig unter Windows 10 und Linux – erfüllt\n\
        Offene Punkte: keine\n\
        Genehmigung durch beide Parteien – erforderlich"
    ]

    fragen = [
        {
            "frage": "Was ist eine Projektabnahme im rechtlichen Sinne?",
            "optionen": ["a) Eine optionale Projektbesprechung",
                         "b) Eine gesetzlich vorgeschriebene Leistung bei Werkverträgen",
                         "c) Ein freiwilliger Testlauf durch den Kunden",
                         "d) Eine zusätzliche Qualitätssicherung"],
            "antwort": "b"
        },
        {
            "frage": "Welche der folgenden Aussagen beschreibt die Abnahme nach DIN 69901-5:2009-1 korrekt?",
            "optionen": ["a) Die Abnahme ist ein Vertragsanhang",
                         "b) Die Abnahme ist eine schriftliche Stellungnahme des Projektteams",
                         "c) Die Abnahme bestätigt die Erfüllung der Anforderungen durch den Auftragnehmer",
                         "d) Die Abnahme ersetzt die Vertragsprüfung"],
            "antwort": "c"
        },
        {
            "frage": "Welche rechtlichen Folgen hat die Abnahme eines Softwareprodukts? (Mehrfachantwort möglich)",
            "optionen": ["a) Beginn der Verjährung von Mängelansprüchen",
                         "b) Anspruch auf Bonuszahlungen",
                         "c) Fälligkeit der Vergütung",
                         "d) Beweislast geht auf den Auftraggeber über"],
            "antwort": ["a", "c", "d"]
        },
        {
            "frage": "Was gehört zur Benutzerakzeptanz? (Mehrfachantwort möglich)",
            "optionen": ["a) Performance-Tests",
                         "b) Gesetzeskonformität der Leistung",
                         "c) Qualität der Admin-Handbücher",
                         "d) Verständlichkeit der Dokumentation"],
            "antwort": ["a", "d"]
        },
        {
            "frage": "Welche Inhalte sollte ein Abnahmeprotokoll mindestens enthalten?",
            "optionen": ["a) Firmenlogo des Auftraggebers",
                         "b) Checkliste mit Abnahmekriterien",
                         "c) Projektkostenaufstellung",
                         "d) Vertraulichkeitsvereinbarung"],
            "antwort": "b"
        },
        {
            "frage": "Wie nennt man einen Entwickler mit 4 Stunden Schlaf?",
            "optionen": [
                "a) Funktionierend.",
                "b) Legacy-Code mit Augenringen.",
                "c) Beta-Version seiner selbst.",
                "d) Schlaflos in /home"
            ],
            "antwort": "c"
        },
        {
            "frage": "Welche Aussage ist FALSCH?",
            "optionen": ["a) Ein Abnahmeprotokoll muss von Auftraggeber und Auftragnehmer unterschrieben werden.",
                         "b) PRINCE2 definiert das Abnahmeprotokoll im Detail.",
                         "c) Der PMBOK-Standard kennt kein Abnahmedokument.",
                         "d) Unternehmen entscheiden meist selbst über die Form des Protokolls."],
            "antwort": "b"
        },
        {
            "frage": "Was dokumentiert ein Abnahmeprotokoll NICHT zwingend?",
            "optionen": ["a) Genaue Softwareversion",
                         "b) Ergebnisse der Prüfung",
                         "c) Testmethoden und Benchmarks",
                         "d) Ort, Datum, Uhrzeit der Abnahme"],
            "antwort": "c"
        },
        {
            "frage": "Welche technische Anforderung wurde im Beispielprotokoll überprüft?",
            "optionen": ["a) Unterstützung von MacOS",
                         "b) Kompatibilität mit Linux und Windows 10",
                         "c) Internetzugang erforderlich",
                         "d) Schnittstellen zu Datenbanken"],
            "antwort": "b"
        },
        {
            "frage": "Welche Punkte können im Abnahmeprotokoll als 'offen' aufgeführt werden? (Mehrfachantwort möglich)",
            "optionen": ["a) Aufgaben, auf deren Erfüllung verzichtet wird",
                         "b) Nicht geprüfte Kriterien",
                         "c) Offene Mängel mit Fristsetzung",
                         "d) Kosten für Nachbesserung"],
            "antwort": ["a", "b", "c"]
        },
        {
            "frage": "Was folgt aus einer unterzeichneten Abnahmeerklärung?",
            "optionen": ["a) Der Auftragnehmer wird aus allen Verpflichtungen entlassen.",
                         "b) Die Software darf nicht mehr verändert werden.",
                         "c) Die Software gilt als vertragsgemäß erbracht.",
                         "d) Der Kunde verliert alle Rechte auf Nachbesserung."],
            "antwort": "c"
        }
    ]

    modul_lernen_und_testen("8.8.3 Projektabnahmen", lerninhalte, fragen)

#====================================================================================================================
#-----------------------Extra Module zum Coding----------------------------------------------------------------------
#====================================================================================================================


#modul_code_API()
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#    modul_lernen_und_testen(modulname, lerninhalte, fragen)
#