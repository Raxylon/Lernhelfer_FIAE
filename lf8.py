import json

def anzeigen_lerninhalt(inhalte):
    print(f"\n📚 Lerninhalte:\n")
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
                print("✅ Richtig."); punkte += 1
            else:
                print(f"❌ Falsch. Richtig wäre: {', '.join(richtige)}")
        else:
            if antwort == richtige:
                print("✅ Richtig."); punkte += 1
            else:
                print(f"❌ Falsch. Richtig wäre: {richtige}")
    print(f"\n🏁 Ergebnis: {punkte} von {len(fragen)} Punkten.")

def lade_module():
    try:
        with open("lernmodule.json", "r", encoding="utf-8") as f:
            return json.load(f).get("lernmoduleLF8", {})
    except Exception as e:
        print("❗ Fehler beim Laden der Datei:", e)
        return {}

def menu():
    # Lädt die Lernmodule aus der JSON-Datei in ein Dictionary
    module = lade_module()

    # Extrahiert die Schlüssel der Module (z.B. "lm01", "lm02") als Liste
    keys = list(module.keys())

    # Gibt das Hauptmenü im Terminal aus
    print("\n=== 📘 Lernfeld 8 – Hauptmenü ===")

    # Iteriert über jedes Modul, nummeriert sie ab 1 und zeigt sie im Format "1 – Modul Thema"
    for i, k in enumerate(keys, 1):
        # Holt den ersten Schlüssel (z.B. "Projektmanagement") aus dem Modul (z.B. "lm01")
        themen_key = next(iter(module[k]))  # Annahme: Der erste Key ist der Themenname
        # Gibt die Zeile im Menü aus, z.B. "1 – Modul LM01.Projektmanagement"
        print(f"{i} – Modul {themen_key}")

    # Option zum Beenden des Programms
    print("0 – Beenden")

    # Fragt den Nutzer nach seiner Auswahl und speichert diese als String
    wahl = input("Auswahl: ").strip()

    # Wenn der Benutzer "0" eingibt, wird die Funktion beendet (zurück zum Aufrufer oder Programmende)
    if wahl == "0": return

    try:
        # Wandelt die Eingabe in eine Zahl um und ermittelt den entsprechenden Modulschlüssel
        key = keys[int(wahl) - 1]

        # Ruft die Funktion zum Anzeigen der Lerninhalte auf und übergibt die Inhalte dieses Moduls
        anzeigen_lerninhalt(module[key]["lerninhalt"])

        # Ruft die Funktion zum Durchführen des Fragen-Quiz auf
        durchlauf_fragen(module[key]["fragen"])

    except Exception as e:
        # Gibt bei einem Fehler (z.B. ungültiger Index oder Tippfehler) eine Fehlermeldung aus
        print("❌ Fehler:", e)


if __name__ == "__main__":
    menu()

