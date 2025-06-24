import json

with open("lernmodule.json", "r", encoding="utf-8") as f:
    daten = json.load(f)
while True:
    try:
        while True:

                lf_names = daten["Lernfelder"]
                #print("Lernfelder: ", lf_names.keys)
                lernfeld_wahl = input("Wähle ein Lernfeld!\n08 - Daten systemübergreifend bereitstellen\n09 - Netzwerke und Dienste bereitstellen\nWelche Zahl darf es sein?\n-> ")
                lernfeld = lf_names[f"lernmoduleLF{lernfeld_wahl}"]
                #print("Lernmodule: ", lernfeld)
                # Thema-Liste über alle Module zusammensetzen
                thema_list = []
                thema_modul_map = {}  # Thema -> Modul
                for modul in lernfeld.values():
                    for thema in modul.keys():
                        thema_list.append(thema)
                        thema_modul_map[thema] = modul

                # Themen anzeigen
                print("\n📚 Verfügbare Themen:")
                for i, t in enumerate(thema_list, 1):
                    print(f"{i}. {t}")

                thema_index = int(input("Welches Thema willst du sehen?\n(Zahl) -> "))
                thema_name = thema_list[thema_index - 1]
                thema = thema_modul_map[thema_name][thema_name]
                fragen = thema["fragen"]

                while True:
                    auswahl = input("1 - Lernen\n2 - Test\n0 - Zurück\n-> ")
                    if auswahl == "0":
                        break
                    elif auswahl == "1":
                        print("\n📘 Lerninhalt:")
                        for absatz in thema["lerninhalt"]:
                            print("-", absatz)
                            input("enter...")
                    elif auswahl == "2":
                        punkte = 0
                        gesamt = len(fragen)
                        for absatz in fragen:
                            print(absatz["frage"])
                            for opt in absatz["optionen"]:
                                print(opt)
                            antwort = input("Deine Antwort (Buchstabe, bei mehreren bitte Komma getrennt): ").lower().replace(" ", "")
                            if isinstance(absatz["antwort"], list):
                                richtige_antworten = set(absatz["antwort"])
                                eingabe_antworten = set(antwort.split(","))
                                if eingabe_antworten == richtige_antworten:
                                    print("Richtig!")
                                    punkte += 1
                                else:
                                    print(f"Falsch! Richtige Antworten: {', '.join(richtige_antworten)}")
                            else:
                                if antwort == absatz["antwort"]:
                                    print("Richtig!")
                                    punkte += 1
                                else:
                                    print(f"Falsch! Richtige Antwort: {absatz['antwort']}")
                            print()

                        print(f"🧪 Test abgeschlossen. Du hast {punkte} von {gesamt} Fragen richtig beantwortet.")

                inp = input("enter - continue\n0 - break\n-> ")
                if inp != "0":
                    continue
                else:
                    break

    except Exception as e:
        print(f"Fehler: {e}")
        a = input("weiter...1: ")
        if a != "1":
            break
        else:
            continue
