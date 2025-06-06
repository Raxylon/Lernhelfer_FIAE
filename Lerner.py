# Lernfeld8.py – enthält modul1, modul2, modul3
# modul1 = Projektmanagement
# modul2 = Datenquellen
# modul3 = Agile Vorgehensmodelle

from Lernfeld8 import (modul1, modul2, modul3, modul4, modul5, modul6, modul7, modul8, modul9, modul10, modul11, modul12, modul13, modul14)
from Lernfeld8 import (modul15, modul16, modul17, modul18, modul19, modul20, modul21)

def auswahl_lernfeld():
    print("\nWähle ein Lernfeld:")
   # print("1. Lernfeld 1")
   # print("2. Lernfeld 2")
    #print("3. Lernfeld 3")
   # print("4. Lernfeld 4")
   # print("5. Lernfeld 5")
   # print("6. Lernfeld 6")
   # print("7. Lernfeld 7")
    print("8. Lernfeld 8")  # Nur dieses ist aktuell implementiert
    print("0. Beenden")
    return input("Deine Wahl: ")


def auswahl_modul(modul_liste):
    print("\nWähle ein Modul:")
    for i, modul in enumerate(modul_liste, 1):
        print(f"{i}. {modul}")
    print("0. Zurück")
    return input("Deine Wahl: ")


def main():
    # Nur Lernfeld 8 hat Module, alle anderen sind Platzhalter
    module_dict = {
        "8": [
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
    }

    while True:
        lernfeld_wahl = auswahl_lernfeld()

        if lernfeld_wahl == "0":
            print("Auf Wiedersehen, Meister des Wissens.")
            break

        if lernfeld_wahl not in module_dict:
            print("Dieses Lernfeld ist noch nicht implementiert. Bitte wähle Lernfeld 8.")
            continue

        # Modulwahl innerhalb von Lernfeld 8
        while True:
            modul_wahl = auswahl_modul(module_dict[lernfeld_wahl])
            if modul_wahl == "0":
                break

            if not modul_wahl.isdigit():
                print("Bitte gib eine gültige Zahl ein.")
                continue

            modul_index = int(modul_wahl)
            if not 1 <= modul_index <= len(module_dict[lernfeld_wahl]):
                print("Modulauswahl ungültig. Versuche es erneut.")
                continue

            # Modul-Funktion aufrufen
            if lernfeld_wahl == "8":
                if modul_index == 1:
                    modul1()
                elif modul_index == 2:
                    modul2()
                elif modul_index == 3:
                    modul3()
                elif modul_index == 4:
                    modul4()
                elif modul_index == 5:
                    modul5()
                elif modul_index == 6:
                    modul6()
                elif modul_index == 7:
                    modul7()
                elif modul_index == 8:
                    modul8()
                elif modul_index == 9:
                    modul9()
                elif modul_index == 10:
                    modul10()
                elif modul_index == 11:
                    modul11()
                elif modul_index == 12:
                    modul12()
                elif modul_index == 13:
                    modul13()
                elif modul_index == 14:
                    modul14()
                elif modul_index == 15:
                    modul15()
                elif modul_index == 16:
                    modul16()
                elif modul_index == 17:
                    modul17()
                elif modul_index == 18:
                    modul18()
                elif modul_index == 19:
                    modul19()
                elif modul_index == 20:
                    modul20()
                elif modul_index == 21:
                    modul21()
                else:
                    print("Modul existiert, aber ist noch nicht implementiert.")

if __name__ == "__main__":
    main()
