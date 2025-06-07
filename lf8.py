import json

def anzeigen_lerninhalt(inhalte):
    print("\n📚 Lerninhalte:\n")
    for punkt in inhalte:
        print("–", punkt)
        input("Weiter mit Enter...")

def durchlauf_fragen(fragen):
    punkte = 0
    for nr, frage in enumerate(fragen, 1):
        print(f"\nFrage {nr}: {frage['frage']}")
        for option in frage["optionen"]:
            print(option)
        antwort = input("Deine Antwort (z.B. a oder a c d): ").lower().strip()

        richtige = frage["antwort"]
        if isinstance(richtige, list):
            gegeben = sorted(antwort.replace(",", " ").split())
            if gegeben == sorted(richtige):
                print("✅ Richtig.")
                punkte += 1
            else:
                print(f"❌ Falsch. Richtig wäre: {', '.join(richtige)}")
        else:
            if antwort == richtige:
                print("✅ Richtig.")
                punkte += 1
            else:
                print(f"❌ Falsch. Richtig wäre: {richtige}")
    print(f"\n🏁 Ergebnis: {punkte} von {len(fragen)} Punkten.")

def modul20():
    try:
        with open("lernmodule.json", "r", encoding="utf-8") as f:
            module = json.load(f)
        daten = module["lm20"]

        anzeigen_lerninhalt(daten["lerninhalt"])

        """print("\n🔍 Starte Testphase:")
        durchlauf_fragen(daten["fragen"])"""
    except FileNotFoundError:
        print("❗ Die Datei 'lernmodule.json' wurde nicht gefunden.")
    except KeyError:
        print("❗ Modul 'lm20' ist nicht vorhanden oder fehlerhaft.")
    except Exception as e:
        print("❗ Ein Fehler ist aufgetreten:", e)

def menu():
    while True:
        print("\n=== Lernfeld 8 – Hauptmenü ===")
        print("1 – Lernen: GUI-Entwicklung in Java (Swing, JavaFX)")
        print("2 - Test ")
        print("0 – Beenden")
        wahl = input("Deine Auswahl: ").strip()

        if wahl == "1":
            modul20()
        elif wahl == "0":
            print("Auf Wiedersehen!")
            break
        else:
            print("❌ Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    menu()
