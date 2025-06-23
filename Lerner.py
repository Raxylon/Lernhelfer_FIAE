# Lernfeld8.py – enthält modul1, modul2, modul3
# modul1 = Projektmanagement
# modul2 = Datenquellen
# modul3 = Agile Vorgehensmodelle
import coding_module, Lernfeld5, Lernfeld8
#from coding_module import (modulc1)


modulnamen = [f"modul{i}" for i in range(81,832)]
modulnamenc = [f"modulc{i}" for i in range(1,32)]

#m_namen_code =
module = {name: getattr(Lernfeld8, name)for name in modulnamen if hasattr(Lernfeld8, name)}
module_coding = {name: getattr(coding_module, name) for name in modulnamenc if hasattr(coding_module, name)}

module_dict = {
        "8": [
            "8.1 - Kundenaufträge im Rahmen von Softwareprojekten",
            "8.1.2 - Softwareprojekte mithilfe von agilen Vorgehensmodellen umsetzen",
            "8.1.2.1-3 - Scrum, Kanban, Burndown chard",
            "8.2.1 - Die Qualität von Daten beschreiben",
            "8.2.2 - Daten aus Datenquellen abrufen ",
            "8.2.3 - Heterogene Datenquellen",
            "8.3.1 - Programmierparadigmen unterscheiden",
            "8.3.2 - Das objektorientiertes Programmierparadigma beschreiben",
            "8.3.3 - Die Modellierungssprache UML verwenden",
            "8.3.4 - Anwendungsfalldiagramme beschreiben und anwenden",
            "8.3.5 - Klassendiagramme beschreiben und anwenden",
            "8.3.6 - Aktivitätsdiagramm beschreiben und anwenden",
            "8.3.7 - Sicherheitsrelevante Aspekte bei der Softwareplanung",
            "8.4.1 - Benutzerschnittstellen unter softwareergonomischen Gesichtspunkten planen",
            "8.4.2 - Eine Oberfläche für eine Benutzerschnittstelle entwerfen",
            "8.5.1 - Java beschreiben und eine Entwicklungsumgebung auswählen",
            "8.5.2 - Grundlegende Sprachelemente beschreiben und Konsolenanwendungen implementieren",
            "8.5.3 - Das objektorientierte Programmierparadigma in Java umsetzen",
            "8.5.4 - Grafische Benutzerschnittstellen in Java entwickeln",
            "8.6.  - Anwendungen in Python implementieren",
            "8.6.2 - Grafische Benutzerschnittstellen in Python entwickeln",
            "8.7.1 - Datenbanklösungen bedarfsgerecht entwickeln",
            "8.7.2 - Den Prozess des Designs relationaler Datenbanken beschreiben",
            "8.7.3 - Relationale Datenmodelle normalisieren",
            "8.7.4 - Das Basiswissen über SQL erweitern und anwenden",
            "8.7.5 - Eine MySQL-Datenbank mit Java ansprechen",
            "8.7.6 - NoSQL-Datenbanken und deren Datenmodelle unterscheiden",
            "8.7.7 - Die NoSQL-Datenbank 'MongoDB' mit Python ansprechen ",
            "8.7.8 - Cloud-basierte Datenbanklösungen unterscheiden",
            "8.8   - Software testen und dokumentieren",
            "8.8.2 - Testdatengeneratoren verwenden",
            "8.8.3 - Projektabnahmen"
        ],
        "c": [
            "Tkinter"
        ]
    }
l_auswahl=None

def auswahl_lernfeld():
    global l_auswahl
    print("\nWähle ein Lernfeld:")
   # print("1. Lernfeld 1")
   # print("2. Lernfeld 2")
    #print("3. Lernfeld 3")
   # print("4. Lernfeld 4")
   # print("5. Lernfeld 5")
   # print("6. Lernfeld 6")
   # print("7. Lernfeld 7")
    print("8. Lernfeld 8")  # Nur dieses ist aktuell implementiert
    print("C. Coding")
    print("0. Beenden")
    l_auswahl = input("Deine Wahl: ").strip().lower()
    return l_auswahl

def auswahl_modul(modul_liste):
    print("\nWähle ein Modul:")
    for i, modul in enumerate(modul_liste, 1):
        print(f"{i}. {modul}")
    print("0. Zurück")
    return input("Deine Wahl: ").strip()

def aufruf_modul(modul_index, l_auswahl):
    #if lernfeld == "8":
    #    i="8"
    modul_key = f"modul{l_auswahl}{modul_index}"
    funktion = module_coding.get(modul_key) if l_auswahl == "c" else module.get(modul_key)
    print(modul_key)
    """elif lernfeld == "c":
        modul_key = f"modulc{modul_index}"
        funktion = module_coding.get(modul_key)
    else:
        funktion = None"""

    if callable(funktion):
        funktion()
    else:
        print(f"Modul {modul_key} ist nicht implementiert oder nicht aufrufbar.")

def main():
    # Nur Lernfeld 8 hat Module, alle anderen sind Platzhalter


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
            aufruf_modul(modul_index, lernfeld_wahl)



if __name__ == "__main__":
    main()

""" if lernfeld_wahl == "8":
                if modul_index == 1:
                    module["modul1"]()
                elif modul_index == 2:
                    module["modul2"]()
                elif modul_index == 3:
                    module["modul3"]()
                elif modul_index == 4:
                    module["modul4"]()
                elif modul_index == 5:
                    module["modul5"]()
                elif modul_index == 6:
                    module["modul6"]()
                elif modul_index == 7:
                    module["modul7"]()
                elif modul_index == 8:
                    module["modul8"]()
                elif modul_index == 9:
                    module["modul9"]()
                elif modul_index == 10:
                    module["modul10"]()
                elif modul_index == 11:
                    module["modul11"]()
                elif modul_index == 12:
                    module["modul12"]()
                elif modul_index == 13:
                    module["modul13"]()
                elif modul_index == 14:
                    module["modul14"]()
                elif modul_index == 15:
                    module["modul15"]()
                elif modul_index == 16:
                    module["modul16"]()
                elif modul_index == 17:
                    module["modul17"]()
                elif modul_index == 18:
                    module["modul18"]()
                elif modul_index == 19:
                    module["modul19"]()
                elif modul_index == 20:
                    module["modul20"]()
                elif modul_index == 21:
                    module["modul21"]()
                elif modul_index == 22:
                    module["modul22"]()
                elif modul_index == 23:
                    module["modul23"]()
                elif modul_index == 24:
                    module["modul24"]()
                elif modul_index == 25:
                    module["modul25"]()
                elif modul_index == 26:
                    module["modul26"]()
                elif modul_index == 27:
                    module["modul27"]()
                elif modul_index == 28:
                    module["modul28"]()
                elif modul_index == 29:
                    module["modul29"]()
                elif modul_index == 30:
                    module["modul30"]()
                elif modul_index == 31:
                    module["modul31"]()
                elif modul_index == 32:
                    module["modul32"]()
                else:
                    print("Modul existiert, aber ist noch nicht implementiert.")

            elif lernfeld_wahl.lower() == "c":
                #if modul_wahl == "1":
                #    modulc1()
                elif modul_index == 1:
                    module["modulc1"]()
                else:
                    print("Modul existiert, aber ist noch nicht implementiert.")"""
