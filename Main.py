# lernreise.py
def warte():
    input("\n(Drücke Enter, um fortzufahren...)")


def frage_mit_feedback(frage, richtige_antwort, erklaerung):
    while True:
        antwort = input(frage + "\n> ").strip().lower()
        if antwort == richtige_antwort:
            print("✅ Richtig!\n")
            break
        else:
            print(f"❌ Falsch. {erklaerung}\nVersuch es noch einmal.\n")


def station_1_agiles_manifest():
    print("📘 Station 1: Agiles Manifest der Softwareentwicklung")
    print("""
Das Agile Manifest ist ein Leitbild für moderne Softwareentwicklung.
Es wurde 2001 von 17 Entwickler*innen formuliert.

Die 4 Leitsätze:
1. Individuen & Interaktionen > Prozesse & Werkzeuge
2. Funktionierende Software > umfassende Dokumentation
3. Zusammenarbeit mit dem Kunden > Vertragsverhandlung
4. Reagieren auf Veränderung > Befolgen eines Plans

Dazu kommen 12 Prinzipien, z. B.:
– Frühzeitige, kontinuierliche Auslieferung
– Tägliche Zusammenarbeit mit der Fachseite
– Nachhaltiges Tempo
– Technische Exzellenz & gutes Design
""")
    warte()
    frage_mit_feedback(
        "Was steht im Zentrum des agilen Manifests?\n"
        "a) Prozesse\nb) Individuen\nc) Verträge\nd) Werkzeuge",
        "b",
        "Individuen und Interaktionen sind zentral."
    )


def station_2_scrum():
    print("📘 Station 2: Scrum (Framework)")
    print("""
Scrum ist ein agiles Rahmenwerk.

🔹 Rollen:
– Product Owner (PO): priorisiert Product Backlog
– Scrum Master: schützt das Team, moderiert
– Entwicklungsteam: selbstorganisiert, interdisziplinär

🔹 Artefakte:
– Product Backlog: Liste aller Anforderungen
– Sprint Backlog: Aufgaben des aktuellen Sprints
– Inkrement: fertige Produktfunktion

🔹 Ereignisse:
– Sprint: feste Zeitspanne (1–4 Wochen)
– Planning, Daily, Review, Retrospektive
""")
    warte()
    frage_mit_feedback(
        "Wer verantwortet das Product Backlog?\n"
        "a) Scrum Master\nb) Projektleiter\nc) Product Owner\nd) Entwicklerteam",
        "c",
        "Nur der Product Owner priorisiert das Product Backlog."
    )


def station_3_datenqualitaet():
    print("📘 Station 3: Datenqualität")
    print("""
Gute Datenqualität bedeutet:
– Genauigkeit
– Vollständigkeit
– Konsistenz
– Aktualität
– Eindeutigkeit
– Relevanz

Verbesserung durch:
– Validierung
– Bereinigung
– Redundanzvermeidung
– Standards
""")
    warte()
    frage_mit_feedback(
        "Was ist KEIN Kriterium guter Datenqualität?\n"
        "a) Konsistenz\nb) Farbe\nc) Vollständigkeit\nd) Relevanz",
        "b",
        "Farbe ist kein Datenqualitätsmerkmal."
    )


def station_4_datenquellen():
    print("📘 Station 4: Datenquellen & -arten")
    print("""
Datenquellen:
– Manuell (z. B. Eingabeformulare)
– Automatisch (Sensoren, APIs)
– Intern (z. B. ERP-Systeme)
– Extern (z. B. Statistiken, Wetterdaten)

Open Data: frei nutzbar, oft öffentlich (z. B. OpenStreetMap)  
Closed Data: geschützt, z. B. Kundendatenbank
""")
    warte()
    frage_mit_feedback(
        "Welche Aussage trifft auf Open Data zu?\n"
        "a) Passwortgeschützt\nb) Nur intern nutzbar\nc) Öffentlich frei nutzbar\nd) Vertraulich",
        "c",
        "Open Data ist öffentlich und ohne Einschränkungen nutzbar."
    )


def station_5_dateiformate():
    print("📘 Station 5: Dateiformate – XML, CSV, JSON")
    print("""
🔹 XML: hierarchisch, mit Tags (<name>Inhalt</name>)
🔹 CSV: Tabellenform, durch Komma getrennt
🔹 JSON: leicht lesbar, strukturierte Daten mit Schlüssel-Wert-Paaren

Einsatz:
– XML: Konfiguration, Dokumente
– CSV: Tabellen, Excel-Import/Export
– JSON: APIs, Webdaten
""")
    warte()
    frage_mit_feedback(
        "Wofür steht CSV?\n"
        "a) Coded Structured Values\nb) Comma Separated Values\n"
        "c) Character Syntax Vector\nd) Column String Values",
        "b",
        "CSV steht für Comma Separated Values."
    )


def station_6_heterogene_quellen():
    print("📘 Station 6: Heterogene Datenquellen")
    print("""
Heterogen bedeutet:
– Unterschiedliche Formate (z. B. XML, JSON, SQL)
– Unterschiedliche Quellen (z. B. lokal, Web, Datenbank)
– Unterschiedliche Strukturen

Integration über:
– ETL-Prozesse (Extract – Transform – Load)
– Datenstandards
– APIs
""")
    warte()
    frage_mit_feedback(
        "Was ist ein typisches Problem bei heterogenen Quellen?\n"
        "a) Gleiches Format\nb) Konsistenz\nc) Unterschiedliche Formate\nd) Geschwindigkeit",
        "c",
        "Unterschiedliche Formate erschweren die Integration."
    )


def station_7_data_warehouse_lake():
    print("📘 Station 7: Data Warehouse vs. Data Lake")
    print("""
Data Warehouse:
– Strukturiert, relational
– Analytisch (z. B. Berichte)
– Datenmodell vorab definiert

Data Lake:
– Rohdaten, auch unstrukturiert
– Flexibel, günstig speicherbar
– Für Big Data und KI geeignet
""")
    warte()
    frage_mit_feedback(
        "Was trifft auf ein Data Warehouse zu?\n"
        "a) Speicherung unstrukturierter Rohdaten\nb) Relationale Struktur\n"
        "c) Keine Analyse möglich\nd) Nur Bilddateien",
        "b",
        "Warehouses speichern strukturierte Daten für Analysen."
    )


def station_8_anwendungsfall():
    print("📘 Station 8: Anwendungsfalldiagramm")
    print("""
UML-Diagramm zur Darstellung von:
– Akteuren (Nutzer, Systeme)
– Anwendungsfällen (z. B. „Einloggen“, „Daten eingeben“)
– Beziehungen (Assoziationen)

Ziel: Überblick über Funktionen aus Benutzersicht
""")
    warte()
    frage_mit_feedback(
        "Was zeigt ein Anwendungsfalldiagramm NICHT?\n"
        "a) Interne Abläufe\nb) Nutzeraktionen\nc) Systemgrenzen\nd) Akteure",
        "a",
        "Interne Abläufe gehören z. B. ins Aktivitätsdiagramm, nicht ins Anwendungsfalldiagramm."
    )


def station_9_aktivitaetsdiagramm():
    print("📘 Station 9: Aktivitätsdiagramm")
    print("""
Zeigt Abläufe (Workflows):
– Startpunkt, Aktionen, Entscheidungen, Endpunkt
– Mit Kontrollflüssen (Pfeile)
– Unterstützt Parallelität (Fork/Join)

Nützlich für Prozessmodellierung.
""")
    warte()
    frage_mit_feedback(
        "Was zeigt ein Aktivitätsdiagramm?\n"
        "a) Datenbanken\nb) Klassenvererbung\nc) Abläufe\nd) Rollenverteilung",
        "c",
        "Abläufe, Entscheidungen und Aktionen sind der Fokus von Aktivitätsdiagrammen."
    )


def lernreise():
    print("🧠 Willkommen, Raxylon. Deine Lernreise beginnt.")
    station_1_agiles_manifest()
    station_2_scrum()
    station_3_datenqualitaet()
    station_4_datenquellen()
    station_5_dateiformate()
    station_6_heterogene_quellen()
    station_7_data_warehouse_lake()
    station_8_anwendungsfall()
    station_9_aktivitaetsdiagramm()
    print("🎓 Lernreise abgeschlossen. Wiederhole jederzeit oder vertiefe einzelne Stationen.")


if __name__ == "__main__":
    lernreise()
