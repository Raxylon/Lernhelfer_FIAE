

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

def modulc1():               #TKinter
    lerninhalte = [
        "Tkinter ist die Standard-GUI-Bibliothek in Python. Sie ermöglicht das Erstellen grafischer Benutzeroberflächen (GUIs) mit Fenstern, Buttons, Labels, Eingabefeldern und mehr.\n\
        Tkinter ist in der Python-Standardbibliothek enthalten und basiert auf dem Tk-GUI-Toolkit.",

        "Grundstruktur eines Tkinter-Programms:\n\
        ```python\n\
        import tkinter as tk\n\
        root = tk.Tk()\n\
        root.title(\"Fenstertitel\")\n\
        label = tk.Label(root, text=\"Hallo, Welt!\")\n\
        label.pack()\n\
        root.mainloop()\n\
        ```\n\
        \n\
        Der Code erzeugt ein einfaches Fenster mit einem Textlabel. `mainloop()` startet die GUI und hält sie aktiv.",

        "Häufig verwendete Widgets:\n\
        - `Label`: Zeigt Text an.\n\
        - `Button`: Führt eine Aktion aus.\n\
        - `Entry`: Einzeiliges Eingabefeld.\n\
        - `Text`: Mehrzeiliges Textfeld.\n\
        - `Frame`: Container für andere Widgets.\n\
        - `Checkbutton`, `Radiobutton`, `Listbox`, `Canvas` und mehr.",

        "Layout-Manager:\n\
        Tkinter bietet drei Layout-Manager:\n\
        - `pack()`: einfache Platzierung der Widgets (z.B. oben, unten).\n\
        - `grid()`: tabellarisches Layout mit Zeilen und Spalten.\n\
        - `place()`: absolute Positionierung (selten empfohlen).",

        "Ereignisbindung:\n\
        Mit `command=` oder `.bind()` können Aktionen an Buttons und Events gebunden werden.\n\
        Beispiel:\n\
        ```python\n\
        def klick():\n            print(\"Button wurde geklickt!\")\n\
        button = tk.Button(root, text=\"Klick mich!\", command=klick)\n\
        ```",

        "GUI-Debugging:\n\
        - Bei Problemen: `print()`-Ausgaben in Callbacks helfen.\n\
        - Nutze `.grid()` und `.pack()` nicht im selben Container.\n\
        - Fehlermeldungen im Terminal beachten.",

        "Mini-Projektidee:\n\
        Erstelle eine kleine GUI mit Eingabefeld, Button und Label. Beim Klick auf den Button soll der Text aus dem Entry im Label erscheinen.",

        "Expertenwissen:\n\
        - `StringVar()`, `IntVar()` usw. erlauben die Bindung von Variablen an Widgets.\n\
        - `after(ms, func)` ermöglicht wiederkehrende Aufgaben (Timer).\n\
        - Mit `Toplevel()` lassen sich neue Fenster erzeugen."
    ]

    fragen = [
        {
            "frage": "Was ist Tkinter in Python?",
            "optionen": ["a) Ein Webframework", "b) Ein Datenbankmodul", "c) Eine GUI-Bibliothek", "d) Ein Compiler"],
            "antwort": "c"
        },
        {
            "frage": "Was bewirkt `root.mainloop()` in einem Tkinter-Programm?",
            "optionen": ["a) Es beendet das Programm.", "b) Es startet die GUI-Ereignisschleife.", "c) Es importiert das Modul.", "d) Es schließt das Fenster."],
            "antwort": "b"
        },
        {
            "frage": "Welches Widget eignet sich für ein einzeiliges Eingabefeld?",
            "optionen": ["a) Label", "b) Text", "c) Entry", "d) Button"],
            "antwort": "c"
        },
        {
            "frage": "Welche Layout-Manager existieren in Tkinter?",
            "optionen": ["a) flex, grid, float", "b) pack, grid, place", "c) align, box, stack", "d) static, flow, border"],
            "antwort": "b"
        },
        {
            "frage": "Wie bindet man eine Funktion an einen Button?",
            "optionen": ["a) mit bind(command=...)", "b) über lambda root", "c) mit command=Funktion", "d) durch config(event)"],
            "antwort": "c"
        },
        {
            "frage": "Was passiert, wenn man `pack()` und `grid()` im selben Container verwendet?",
            "optionen": ["a) Das Layout wird präziser.", "b) Es gibt einen Fehler.", "c) Alles funktioniert wie gewohnt.", "d) Widgets werden transparent."],
            "antwort": "b"
        },
        {
            "frage": "Wozu dient `StringVar()` in Tkinter?",
            "optionen": ["a) Für Farben", "b) Zum Speichern von Bildern", "c) Für die Verbindung von Widgets mit Variablen", "d) Für Schleifen"],
            "antwort": "c"
        },
        {
            "frage": "Welche Methode erzeugt ein zweites Fenster in Tkinter?",
            "optionen": ["a) new()", "b) Toplevel()", "c) SubWindow()", "d) WindowPlus()"],
            "antwort": "b"
        },
        {
            "frage": "Welche Methode wird genutzt, um Widgets absolut zu positionieren?",
            "optionen": ["a) grid()", "b) layout()", "c) absolute()", "d) place()"],
            "antwort": "d"
        },
        {
            "frage": "Was bewirkt `after(ms, func)` in Tkinter?",
            "optionen": ["a) Startet eine neue GUI.", "b) Verhindert Eingaben.", "c) Führt eine Funktion nach einer Zeit aus.", "d) Löscht ein Widget."],
            "antwort": "c"
        }
    ]
    modul_lernen_und_testen("Coding - TKinter", lerninhalte, fragen)

def modul_code_API():
    lerninhalte = [
        "REST (Representational State Transfer) ist ein Architekturstil für verteilte Systeme, der meist in Webanwendungen verwendet wird.\n\
        REST basiert auf dem HTTP-Protokoll und verwendet standardisierte Methoden: GET, POST, PUT, DELETE.\n\
        RESTful APIs ermöglichen eine einfache Kommunikation zwischen Client und Server über URLs und HTTP-Operationen.\n\
        REST ist zustandslos, nutzt meist JSON für den Datenaustausch und ist leichtgewichtig im Vergleich zu SOAP.\n\
        Ein REST-Endpunkt (API) ist meist eine URL, die Daten bereitstellt oder entgegennimmt – z.B. /users/ oder /api/items.\n\
        Python verwendet häufig die `requests`-Bibliothek für REST-Aufrufe.",

        "Beispiel für eine GET-Anfrage in Python mit `requests`:\n\
        ```python\n\
        import requests\n\
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')\n\
        if response.status_code == 200:\n\
            data = response.json()\n\
            print(data['title'])\n\
        ```\n\
        Dieses Beispiel ruft ein Post-Objekt ab und gibt dessen Titel aus.\n\
        Weitere Methoden sind POST (zum Erstellen), PUT (zum Aktualisieren) und DELETE (zum Löschen).",

        "REST-Prinzipien:\n\
        • Client-Server-Modell: Klare Trennung von Frontend und Backend.\n\
        • Zustandslosigkeit: Jeder Request ist unabhängig, der Server speichert keinen Zustand.\n\
        • Caching: Serverantworten können zwischengespeichert werden.\n\
        • Einheitliche Schnittstelle: Ressourcen werden über definierte URLs angesprochen.\n\
        • Layered System: Aufrufe können durch mehrere Schichten gehen (z.B. Load Balancer).\n\
        • Code-On-Demand (optional): Server kann ausführbaren Code an Client schicken."
    ]

    fragen = [
        {
            "frage": "Was ist ein wesentliches Merkmal von REST?",
            "optionen": ["a) SOAP-Nachrichten", "b) Zustandslosigkeit", "c) XML-basierte Antwort",
                         "d) Nur PUT-Anfragen"],
            "antwort": "b"
        },
        {
            "frage": "Welche Methode wird in REST genutzt, um eine Ressource zu löschen?",
            "optionen": ["a) GET", "b) POST", "c) DELETE", "d) PATCH"],
            "antwort": "c"
        },
        {
            "frage": "Was bedeutet 'zustandslos' im Kontext von REST?",
            "optionen": ["a) Der Server speichert Sessions.",
                         "b) Jeder Request enthält alle notwendigen Informationen.",
                         "c) Der Client speichert Serverstatus.", "d) Nur GET-Anfragen sind erlaubt."],
            "antwort": "b"
        },
        {
            "frage": "Welche Bibliothek verwendet man typischerweise in Python für REST-Zugriffe?",
            "optionen": ["a) flask", "b) socket", "c) json", "d) requests"],
            "antwort": "d"
        },
        {
            "frage": "Was ist die Hauptaufgabe der `requests.get()`-Funktion in Python?",
            "optionen": ["a) Daten verschlüsseln", "b) Eine Datei hochladen", "c) Eine GET-Anfrage senden",
                         "d) Eine REST-API starten"],
            "antwort": "c"
        },
        {
            "frage": "Was gibt `response.json()` in Python zurück?",
            "optionen": ["a) Einen XML-String", "b) Eine HTML-Seite", "c) Ein Dictionary mit JSON-Daten",
                         "d) Einen REST-Client"],
            "antwort": "c"
        },
        {
            "frage": "Welche REST-Methode wird verwendet, um eine neue Ressource zu erstellen?",
            "optionen": ["a) GET", "b) POST", "c) PUT", "d) DELETE"],
            "antwort": "b"
        },
        {
            "frage": "Welche der folgenden Aussagen trifft auf REST zu?",
            "optionen": ["a) REST nutzt typischerweise SOAP für die Kommunikation.",
                         "b) REST benötigt zwingend XML.",
                         "c) REST ist schwergewichtig.",
                         "d) REST nutzt meist JSON und HTTP."],
            "antwort": "d"
        },
        {
            "frage": "Welche Aussage trifft auf das Prinzip der einheitlichen Schnittstelle zu?",
            "optionen": ["a) Alle Ressourcen haben identische Inhalte.",
                         "b) Ressourcen werden über definierte URLs angesprochen.",
                         "c) Alle Antworten enthalten HTML.",
                         "d) Jede Anfrage benötigt SSL."],
            "antwort": "b"
        },
        {
            "frage": "Was ist ein Beispiel für eine typische REST-URL?",
            "optionen": ["a) smtp://mailserver.com", "b) telnet://localhost", "c) /api/users/1",
                         "d) ftp://datenbank.local"],
            "antwort": "c"
        }
    ]
    modul_lernen_und_testen("Lernfeld 8.3.2 Zusatz: API - SOAP und REST", lerninhalte, fragen)