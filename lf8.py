import json  # Importiert das JSON-Modul zum Laden und Verarbeiten von JSON-Dateien

# Funktion zeigt die Lerninhalte im Terminal an
def anzeigen_lerninhalt(inhalte):
    print(f"\n📚 Lerninhalte:\n")  # Überschrift
    for punkt in inhalte:  # Schleife über alle Inhalte (Liste von Stichpunkten)
        print("–", punkt)  # Gibt jeden Punkt aus
        input("Weiter mit Enter...")  # Wartet auf Benutzereingabe für nächsten Punkt

# Funktion führt ein Fragenset als Quiz durch
def durchlauf_fragen(fragen):
    punkte = 0  # Punktestand initialisieren
    for nr, frage in enumerate(fragen, 1):  # Schleife über alle Fragen mit Nummerierung ab 1
        print(f"\nFrage {nr}: {frage['frage']}")  # Gibt die Frage aus
        for option in frage["optionen"]:  # Gibt alle Antwortoptionen aus
            print(option)
        antwort = input("Deine Antwort (z.B. a oder a c d): ").lower().strip()  # Benutzerantwort in Kleinbuchstaben
        richtige = frage["antwort"]  # Holt die richtige(n) Antwort(en)

        # Wenn es sich um eine Mehrfachantwort (Liste) handelt:
        if isinstance(richtige, list):
            gegeben = sorted(antwort.replace(",", " ").split())  # Benutzerantwort in Liste umwandeln, sortiert
            if gegeben == sorted(richtige):  # Antwort vergleichen
                print("✅ Richtig."); punkte += 1  # Punkt bei richtiger Antwort
            else:
                print(f"❌ Falsch. Richtig wäre: {', '.join(richtige)}")  # Korrekte Antwort anzeigen
        else:
            if antwort == richtige:  # Bei einfacher Antwort
                print("✅ Richtig."); punkte += 1
            else:
                print(f"❌ Falsch. Richtig wäre: {richtige}")

    # Am Ende: Punktestand anzeigen
    print(f"\n🏁 Ergebnis: {punkte} von {len(fragen)} Punkten.")

# Funktion lädt die JSON-Datei und extrahiert die Lernmodule für LF8
def lade_module():
    try:
        with open("lernmodule.json", "r", encoding="utf-8") as f:  # Datei öffnen
            return json.load(f).get("lernmoduleLF8", {})  # 'lernmoduleLF8'-Bereich extrahieren
    except Exception as e:  # Fehler beim Laden
        print("❗ Fehler beim Laden der Datei:", e)
        return {}

# Hauptmenü-Funktion
def menu():
    while True:
        module = lade_module()
        keys = list(module.keys())

        print("\n=== 📘 Lernfeld 8 – Hauptmenü ===")
        for i, k in enumerate(keys, 1):
            themen_key = next(iter(module[k]))
            print(f"{i} – Modul {themen_key}")
        print("0 – Beenden")

        wahl = input("Auswahl: ").strip()
        if wahl == "0":
            break

        try:
            index = int(wahl) - 1
            if not (0 <= index < len(keys)):
                print("❌ Ungültige Auswahl.")
                continue

            key = keys[index]
            themen_key = next(iter(module[key]))
            inhalt = module[key][themen_key]
            print(inhalt)
            print(themen_key)
            print(key)
            while True:
                auswahl = input("Was darf es sein?\n1. Lernen\n2. Test\n0. Zurück\n→ ").strip()
                if auswahl == "1":
                    anzeigen_lerninhalt(inhalt["lerninhalt"])
                elif auswahl == "2":
                    durchlauf_fragen(inhalt["fragen"])
                elif auswahl == "0":
                    break
                else:
                    print("❌ Ungültige Eingabe.")

        except ValueError:
            print("❌ Bitte nur Zahlen eingeben.")


# Einstiegspunkt des Programms
if __name__ == "__main__":
    menu()  # Startet das Menü beim Ausführen der Datei
