import tkinter as tk
from tkinter import messagebox

fragen = [
    {
        "frage": "Was unterscheidet eine GUI grundlegend von einer Konsolenanwendung?",
        "optionen": ["a) Nur die Ausgabemethode", "b) Nur die Programmiersprache",
                     "c) Die Interaktion durch Oberflächenelemente", "d) Es gibt keinen Unterschied"],
        "antwort": "c"
    },
    {
        "frage": "Welche drei grundlegenden Elemente muss eine Java-GUI-Bibliothek bieten?",
        "optionen": ["a) Tabellen, SQL-Anbindung, Datenexport",
                     "b) Widgets, Ereignismodell, grafische Grundoperationen",
                     "c) Konsolenkommandos, Fenster, HTML",
                     "d) Netzwerktools, Compiler, Datenbanken"],
        "antwort": "b"
    },
    {
        "frage": "Welche Java-Bibliothek war die erste GUI-API?",
        "optionen": ["a) JavaFX", "b) Java2D", "c) Swing", "d) AWT"],
        "antwort": "d"
    },
    {
        "frage": "Wofür steht die Abkürzung JFC?",
        "optionen": ["a) Java Fast Compilation", "b) Java Foundation Classes",
                     "c) Java Function Core", "d) Java File Controller"],
        "antwort": "b"
    },
    {
        "frage": "Was bedeutet 'Pluggable Look and Feel'?",
        "optionen": ["a) Das Layout ist fest und unveränderbar",
                     "b) Komponenten können dynamisch zur Laufzeit verändert werden",
                     "c) Nur Buttons sind veränderbar", "d) Es betrifft nur den Hintergrund"],
        "antwort": "b"
    },
    {
        "frage": "Welche Klasse wird verwendet, um ein Fenster in Java zu erstellen?",
        "optionen": ["a) JFrame", "b) JWindow", "c) FrameMaker", "d) JavaPanel"],
        "antwort": "a"
    },
    {
        "frage": "Was bewirkt der Aufruf von System.exit(0) in einer GUI?",
        "optionen": ["a) Es öffnet ein neues Fenster", "b) Das Programm wird beendet",
                     "c) Es startet den Debugger", "d) Es wechselt zur Konsole"],
        "antwort": "b"
    },
    {
        "frage": "Welche Vorteile bieten GUI-Builder?",
        "optionen": ["a) Nur grafisch schönere Oberflächen",
                     "b) Automatische Codegenerierung und einfache Anordnung der Elemente",
                     "c) Schnellere Kompilierung", "d) Unterstützung von Datenbanken"],
        "antwort": "b"
    },
    {
        "frage": "Wie heißt der GUI-Builder für Eclipse?",
        "optionen": ["a) JavaMaker", "b) GUIForge", "c) WindowBuilder", "d) EclipseFX"],
        "antwort": "c"
    },
    {
        "frage": "Welche Technologien unterstützt die Accessibility-API in Java? (Mehrere Antworten möglich)",
        "optionen": ["a) Spracherkennung", "b) Lesegeräte für Blinde",
                     "c) Druckfunktion", "d) Bildschirmlupe"],
        "antwort": ["a", "b", "d"]
    },
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("GUI-Fragenspiel")
        self.fragen = fragen
        self.index = 0
        self.punkte = 0
        self.widgets = []

        self.frage_label = tk.Label(master, text="", font=("Arial", 14), wraplength=600, justify="left")
        self.frage_label.pack(pady=20)

        self.optionen_frame = tk.Frame(master)
        self.optionen_frame.pack()

        self.naechste_button = tk.Button(master, text="Weiter", command=self.weiter)
        self.naechste_button.pack(pady=10)

        self.zeige_frage()

    def zeige_frage(self):
        self.auswahl = []
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()

        frage_daten = self.fragen[self.index]
        self.frage_label.config(text=frage_daten["frage"])

        if isinstance(frage_daten["antwort"], list):  # Mehrfachantwort
            for i, opt in enumerate(frage_daten["optionen"]):
                var = tk.IntVar()
                cb = tk.Checkbutton(self.optionen_frame, text=opt, variable=var, anchor="w", justify="left")
                cb.pack(fill="x", padx=20, anchor="w")
                self.auswahl.append((opt[0], var))
                self.widgets.append(cb)
        else:  # Einzelantwort
            self.auswahl_var = tk.StringVar()
            for i, opt in enumerate(frage_daten["optionen"]):
                rb = tk.Radiobutton(self.optionen_frame, text=opt, variable=self.auswahl_var, value=opt[0],
                                    anchor="w", justify="left")
                rb.pack(fill="x", padx=20, anchor="w")
                self.widgets.append(rb)

    def weiter(self):
        frage_daten = self.fragen[self.index]
        korrekt = frage_daten["antwort"]
        richtige_antwort = ""
        richtig = False

        if isinstance(korrekt, list):  # Mehrfachantwort
            gewaehlt = [key for key, var in self.auswahl if var.get()]
            richtig = set(gewaehlt) == set(korrekt)
            richtige_antwort = ", ".join(korrekt)
        else:  # Einzelantwort
            gewaehlt = self.auswahl_var.get()
            richtig = gewaehlt == korrekt
            richtige_antwort = korrekt

        if richtig:
            self.punkte += 1
            msg = f"✔️ Richtig!\n\nDie Antwort war: {richtige_antwort}"
        else:
            msg = f"❌ Falsch.\n\nDie richtige Antwort ist: {richtige_antwort}"

        messagebox.showinfo("Ergebnis", msg)

        self.index += 1
        if self.index < len(self.fragen):
            self.zeige_frage()
        else:
            messagebox.showinfo("Fertig!", f"Dein Ergebnis: {self.punkte} von {len(self.fragen)} Punkten")
            self.master.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
