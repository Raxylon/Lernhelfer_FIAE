import importlib

lernfelder = [
    "lf01","lf02","lf03","lf04","lf05","lf06","lf07","lf8","lf09","lf10","lf11","lf12"]

def auswahl_lernfeld():
    print("\nWähle ein Lernfeld:")
    for i, feld in enumerate(lernfelder, 1):
        print(f"{i}. {feld.upper()}")
    print("0. Beenden")
    wahl = input("Deine Wahl: ").strip()
    return wahl

def main():
    while True:
        wahl = auswahl_lernfeld()
        if wahl == "0":
            print("Auf Wiedersehen, Meister des Wissens.")
            break
        if not wahl.isdigit() or not (1 <= int(wahl) <= len(lernfelder)):
            print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
            continue
        modul_name = lernfelder[int(wahl)-1]
        try:
            modul = importlib.import_module(modul_name)
            # Erwartet, dass in jeder lfXX.py ein menu() definiert ist
            modul.menu()
        except ModuleNotFoundError:
            print(f"Modul '{modul_name}' nicht gefunden.")
        except AttributeError:
            print(f"Modul '{modul_name}' hat keine Funktion 'menu()'.")
        except Exception as e:
            print(f"Fehler beim Ausführen von '{modul_name}': {e}")

if __name__ == "__main__":
    main()
