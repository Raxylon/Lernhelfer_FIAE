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

def modul51():

    lerninhalte = [
        "IT-Services sind essenziell für die Funktionstüchtigkeit von Unternehmen. Die IT-Abteilungen stellen dabei nicht\n\
        nur die Technik bereit, sondern bieten eine Vielzahl an Services für interne und externe Kunden.",
        "Servicearten umfassen unter anderem Vor-Ort-Service, IT-Betreuung, IT-Management, IT-Outsourcing, IT-Vertrieb und\n\
        User-Help-Desk. Virtuelle Services, Cloud-Hosting und IT-Infrastrukturen sind stark wachsende Segmente.",
        "Mit zunehmender Digitalisierung steigen die Anforderungen an IT-Services. Unternehmen lagern oft Server und Rechenzentren\n\
         aus und schließen Service- und Wartungsverträge mit externen Dienstleistern ab.",
        "Ein Beispiel ist das Systemhaus JIKU IT-Solutions, das über 200 Unternehmen betreut. Es bietet Informationen über\n\
        Services per Flyer, Webseiten, Blogs, E-Books und Chat.",
        "Servicequalität hängt von Verfügbarkeit, Zuverlässigkeit und Einhaltung rechtlicher Vorgaben (z. B. DSGVO) ab. Externe\n\
        Zertifizierungen und Assessments dienen als Nachweise.",
        "Der IT-Service-Lifecycle beschreibt den gesamten Lebenszyklus eines IT-Services – von Planung, Roll-out, Betrieb\n\
        bis zur Ablösung. Zu den Phasen gehören: Analyse, Planung, Konfiguration, Wartung, Schulung, Entsorgung usw.",
        "Services unterscheiden sich durch Art der Verwendung, Ort, Prozessphase, beteiligte Objekte und Systeme, sowie\n\
        Dringlichkeit, Ressourcen und Komplexität.",
        "Definitionen: BSI – Kombination aus Objekten und Prozessen; FitSM® – Mittel zur Lieferung von Mehrwert; ITIL 4 –\n\
        Förderung gewünschter Ergebnisse ohne Kosten- und Risikoverwaltung.",
        "Services entstehen aus gemeinsamer Wertschöpfung zwischen Anbieter, Partnern und Kunden.",
        "Mitarbeitende müssen flexibel neue Services entwickeln, reflektieren und verändern (Change-Management).",
        "Serviceketten: Services sind voneinander abhängig und durch mehrere Teams entlang der Prozesskette konzipiert.",
        "Servicearten im IT-Bereich: z.B. IT-Vertrieb, Break/Fix, On-Site, Swap, DIY, Cloud-Services, Chatbots, Managed Services,\n\
        Garantieleistungen, Helpdesk, Wartung, Reparatur, IT-Einweisung, Training, Beratung usw.",
        "Serviceverfügbarkeit wird z.B. als 24/7 oder 12/5 angegeben.",
        "IT-Service-Management (ITSM): Planung, Bereitstellung, Betrieb und Steuerung von IT-Services durch Provider.",
        "Serviceportfolio & Servicekatalog: Übersicht über alle Services, Beschreibung gemäß SMART, Verantwortung zugewiesen.",
        "Service-Level-Management: Kundenanforderungen werden priorisiert, Services geplant und vertraglich geregelt.",
        "KPIs: Schlüsselmetriken wie Verfügbarkeit oder Ausfälle messen Servicequalität.",
        "SOA: Modularisierte IT-Architektur, wiederverwendbare Module, definiert Interaktionen über Beschreibungssprachen.",
        "Cloud-Plattformen: IaaS (Infrastruktur), FaaS (Funktionen), PaaS (Plattformen), SaaS (Software).",
        "Der IMAC/R/D-Lebenszyklus beschreibt die typischen IT-Servicephasen über den gesamten Lebenszyklus hinweg:",
        "Install (Installation): Konfiguration und Aufbau bzw. Einrichtung der IT-Arbeitsplätze (z.B. Büro, Homeoffice, unterwegs).\n\
        Dazu gehören Bereitstellung und Einrichtung von Hardware, Software, Zubehör und IT-Dienstleistungen.",
        "Move (Umzug): Bereitstellung, Verpackung und Transport von Geräten, Umzug der IT-Ausstattung, Neuinstallation am Zielort,\n\
        Anpassung der Konfiguration sowie Verwaltung der Benutzerrechte.",
        "Add (Ergänzung): Installation und Konfiguration zusätzlicher Komponenten (Hardware, Software, Rechte) entsprechend den\n\
        Anforderungen und Lizenzbedingungen.",
        "Change (Änderung): Anpassung bestehender Installationen durch Updates, Upgrades, Neuinstallationen, Änderungen von\n\
        Benutzerrechten oder Sicherheitsrichtlinien.",
        "Remove (Entfernung): Vorbereitung und Sicherung zu entfernender Hard-/Software, Datenlöschung, Abbau und fachgerechter Ausbau\n\
        der Systeme.",
        "Dispose (Entsorgung): Rückführung, Entsorgung oder Wiederaufbereitung (z. B. Refurbishing, Recycling, Remarketing) der\n\
        Hardware gemäß ökologischer und rechtlicher Vorgaben."
    ]

    fragen = [
        {
            "frage": "Welche Aussage über IT-Abteilungen trifft zu?",
            "optionen": [
                "Sie verkaufen hauptsächlich Hardware.",
                "Sie betreuen ausschließlich externe Kunden.",
                "Sie stellen IT-Services für interne und externe Kunden bereit.",
                "Sie bieten keine Serviceverträge an."
            ],
            "antwort": "Sie stellen IT-Services für interne und externe Kunden bereit."
        },
        {
            "frage": "Welche Servicearten zählen typischerweise zum IT-Portfolio?",
            "optionen": [
                "IT-Betreuung",
                "Buchhaltung",
                "IT-Outsourcing",
                "Vor-Ort-Service"
            ],
            "antwort": ["IT-Betreuung", "IT-Outsourcing", "Vor-Ort-Service"]
        },
        {
            "frage": "Was ist Ziel der IT-Abteilung hinsichtlich der Kundenzufriedenheit?",
            "optionen": [
                "Minimierung von Services",
                "Maximale Verfügbarkeit und Zuverlässigkeit",
                "Reduktion von Kommunikationskanälen",
                "Konzentration auf Hardwareverkauf"
            ],
            "antwort": "Maximale Verfügbarkeit und Zuverlässigkeit"
        },
        {
            "frage": "Welche rechtlichen und qualitativen Anforderungen gelten für IT-Services?",
            "optionen": [
                "Nur ISO 9001 ist relevant",
                "Keine spezifischen Vorgaben",
                "Datenschutzgesetze wie die DSGVO und Qualitätsstandards",
                "ITIL ist gesetzlich vorgeschrieben"
            ],
            "antwort": "Datenschutzgesetze wie die DSGVO und Qualitätsstandards"
        },
        {
            "frage": "Was beschreibt der IT-Service-Lifecycle?",
            "optionen": [
                "Softwareentwicklung",
                "Lebenszyklus eines IT-Service von Planung bis Entsorgung",
                "IT-Finanzplanung",
                "Personalentwicklung"
            ],
            "antwort": "Lebenszyklus eines IT-Service von Planung bis Entsorgung"
        },
        {
            "frage": "Was versteht man unter Cloud-Services?",
            "optionen": [
                "Reparatur von Hardware",
                "IT-Dienste über das Internet, z. B. Speicher oder Rechenleistung",
                "Hotline-Support",
                "Nur Online-Schulungen"
            ],
            "antwort": "IT-Dienste über das Internet, z. B. Speicher oder Rechenleistung"
        },
        {
            "frage": "Welche Kommunikationswege nutzen IT-Dienstleister zur Kundeninformation?",
            "optionen": [
                "Blogs",
                "Brieftauben",
                "E-Books",
                "Flyer"
            ],
            "antwort": ["Blogs", "E-Books", "Flyer"]
        },
        {
            "frage": "Was sind typische Aufgaben im Betrieb von IT-Services?",
            "optionen": [
                "Konfiguration, Wartung, Lizenzverwaltung",
                "Produktentwicklung",
                "Personalakquise",
                "Steuerberatung"
            ],
            "antwort": "Konfiguration, Wartung, Lizenzverwaltung"
        },
        {
            "frage": "Was sind zentrale Merkmale von ITIL 4 und ITSM?",
            "optionen": [
                "Kundenmanagement durch IT",
                "Gemeinsame Wertschöpfung & Planung/Steuerung von IT-Services",
                "Kostenlosigkeit von Services",
                "Verzicht auf interne Prozesse"
            ],
            "antwort": "Gemeinsame Wertschöpfung & Planung/Steuerung von IT-Services"
        },
        {
            "frage": "Was ist ein Helpdesk-Service?",
            "optionen": [
                "Persönliche Schulung",
                "Telefonverkauf",
                "Online-Support über ein zentrales System",
                "Gerätetausch vor Ort"
            ],
            "antwort": "Online-Support über ein zentrales System"
        },
        {
            "frage": "Was versteht man unter einem Managed Service?",
            "optionen": [
                "Spontaner Service ohne Vertrag",
                "Dauerhafte Betreuung mit SLA",
                "Selbstverwaltung durch Kunden",
                "Einmaliger Vor-Ort-Service"
            ],
            "antwort": "Dauerhafte Betreuung mit SLA"
        },
        {
            "frage": "Welche Arten von Cloud-Diensten gibt es?",
            "optionen": [
                "IaaS",
                "PaaS",
                "SaaS",
                "Kaas"
            ],
            "antwort": ["IaaS", "PaaS", "SaaS"]
        },
        {
            "frage": "Welche Aufgaben umfasst der IMAC/R/D-Zyklus in IT-Services?",
            "optionen": [
                "Install: Einrichtung von IT-Arbeitsplätzen",
                "Move: Verpacken, Transport, Neuinstallation",
                "Add: Erweiterung durch neue Komponenten",
                "Dispose: Recycling und Datenvernichtung"
            ],
            "antwort": [
                "Install: Einrichtung von IT-Arbeitsplätzen",
                "Move: Verpacken, Transport, Neuinstallation",
                "Add: Erweiterung durch neue Komponenten",
                "Dispose: Recycling und Datenvernichtung"
            ]
        },
        {
            "frage": "Welche Aufgaben fallen in die Phase „Change“ im IMAC/R/D-Zyklus?",
            "optionen": [
                "Software- und Sicherheitsupdates",
                "Hardwareeinkauf",
                "Benutzerrechte löschen",
                "Rückgabe von Altgeräten"
            ],
            "antwort": "Software- und Sicherheitsupdates"
        },
        {
            "frage": "Welche Bedeutung hat ein Servicekatalog im IT-Service?",
            "optionen": [
                "Er ersetzt Backup-Konzepte",
                "Er regelt Kundenverträge",
                "Er dokumentiert Richtlinien und Zuständigkeiten",
                "Er listet IT-Produkte für Shops"
            ],
            "antwort": "Er dokumentiert Richtlinien und Zuständigkeiten"
        }
    ]
    modul_lernen_und_testen("5.1 Servicearten und Serviceanforderungen im IT-Bereich beschreiben", lerninhalte, fragen)





#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)
#        modul_lernen_und_testen(modulname, lerninhalte, fragen)