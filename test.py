# Lerner.py – Einstiegspunkt

from lf8 import (
   #modul1, modul2, modul1, modul1, modul1, modul1, modul1, modul1, modul1, modul1,
    modul20
)

# Liste der Modul-Funktionen, Reihenfolge muss zum Anzeige-Text passen!
modul_funktionen = [
     modul20
]

modul_namen = [
    "Projektmanagement",
    "Datenquellen",
    "Agile Vorgehensmodelle",
    "Scrum, Kanban, Burndown chard",
    "Datenqualität",
    "Datenquelle",
    "Heterogene Datenquellen",
    "Programmierparadigmen unterscheiden",
    "objektorientierte Programmierung",
    "unified modeling language",
    "Anwendungsfalldiagramme beschreiben und anwenden",
    "Klassendiagramme",
    "Aktivitätsdiagramm beschreiben und anwenden",
    "Sicherheitsrelevante Aspekte bei der Softwareplanung",
    "Benutzerschnittstellen unter softwareergonomischen Gesichtspunkten planen",
    "Eine Oberfläche für eine Benutzerschnittstelle entwerfen",
    "Java beschreiben und eine Entwicklungsumgebung auswählen",
    "Grundlegende Sprachelemente beschreiben und Konsolenanwendungen implementieren",
    "Das objektorientierte Programmierparadigma in Java umsetzen",
    "Grafische Benutzerschnittstellen in Java entwickeln",
    "Anwendungen in Python implementieren"
]
lernfeld = ["Lernfeld 01", "Lernfeld 02", "Lernfeld 03", "Lernfeld 04", "Lernfeld 05", "Lernfeld 06",
             "Lernfeld 07", "Lernfeld 08", "Lernfeld 09", "Lernfeld 10", "Lernfeld 11", "Lernfeld 12"
            ]

def auswahl_lernfeld(lernfeld_liste):
    print("\nWähle ein Lernfeld:")
    for i, feld in enumerate(lernfeld_liste,1):
        print(f"{i}.{feld}")

    print("0. Beenden")
    return input("Deine Wahl: ")

def auswahl_modul(modul_liste):
    print("\nWähle ein Modul:")
    for i, modul in enumerate(modul_liste, 1):
        print(f"{i}. {modul}")
    print("0. Zurück")
    return input("Deine Wahl: ")

def main():
    while True:
        lernfeld_wahl = auswahl_lernfeld(lernfeld)

        if lernfeld_wahl == "0":
            print("Auf Wiedersehen, Meister des Wissens.")
            break

        if not lernfeld_wahl.isdigit():
            print("bist du dumm? Eine gültige Zahl!!!")
            continue
        index = int(lernfeld_wahl) - 1
        if 0 <= index < len(lernfeld):
            try:
                lernfeld[index] ()
            except Exception as e:
                print(f"Fehler beim Ausführen des Lernfeldes: {e}")
            else:
                print("Ungültige Auswahl. Bitte versuche es erneut.")

            #8continue

        while True:
            modul_wahl = auswahl_modul(modul_namen)
            if modul_wahl == "0":
                break

            if not modul_wahl.isdigit():
                print("Bitte gib eine gültige Zahl ein.")
                continue

            index = int(modul_wahl) - 1
            if 0 <= index < len(modul_funktionen):
                try:
                    modul_funktionen[index]()
                except Exception as e:
                    print(f"Fehler beim Ausführen des Moduls: {e}")
            else:
                print("Ungültige Auswahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
