import json
from json import JSONDecodeError
from pathlib import Path
import re

import tkinter as tk
from tkinter import messagebox, ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.vscroll = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vscroll.set)

        self.inner = ttk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")

        self.inner.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.vscroll.pack(side="right", fill="y")

        # Mausrad scrollt nur, wenn der Mauszeiger über dem Canvas ist
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)

    def _on_canvas_configure(self, event):
        # inner-Frame immer auf Canvas-Breite ziehen
        self.canvas.itemconfigure(self.window_id, width=event.width)

    def _bind_mousewheel(self, _event=None):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)     # Windows/macOS
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux) # Linux hoch
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux) # Linux runter

    def _unbind_mousewheel(self, _event=None):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-3, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(3, "units")

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "lernmodule.json"

#==================================================================================================

def lade_lernmodule(json_path: Path) -> dict:
    try:
        with json_path.open("r", encoding="utf-8") as f:    #öffnet die JSON-Datei im Lesemodus mit UTF-8 Encoding, damit wir die Lernmodule-Daten laden können. Wenn die Datei nicht gefunden wird, wird eine FileNotFoundError mit einer benutzerfreundlichen Fehlermeldung ausgelöst. Wenn die Datei ungültiges JSON enthält, wird eine ValueError mit einer benutzerfreundlichen Fehlermeldung ausgelöst.
            return json.load(f)                             #lädt die JSON-Daten aus der Datei und gibt sie als dict zurück, damit wir sie in der App verwenden können. Wenn die Datei ungültiges JSON enthält, wird eine JSONDecodeError ausgelöst, die wir abfangen und in eine ValueError mit einer benutzerfreundlichen Fehlermeldung umwandeln.
    except FileNotFoundError as e:                          #wenn die Datei nicht gefunden wird, z.B. weil sie fehlt oder der Pfad falsch ist, fangen wir die FileNotFoundError ab und werfen eine neue FileNotFoundError mit einer benutzerfreundlichen Fehlermeldung, damit der Nutzer weiß, dass die Datei fehlt und die App nicht gestartet werden kann.
        raise FileNotFoundError(f"Die Datei {json_path} wurde nicht gefunden.") from e  #wir verwenden "from e", damit die ursprüngliche Fehlermeldung (z.B. "No such file or directory") in der neuen Fehlermeldung enthalten ist, damit der Nutzer mehr Informationen über den Fehler bekommt.
    except JSONDecodeError as e:                                                        #wenn die Datei ungültiges JSON enthält, z.B. weil sie beschädigt ist oder nicht richtig formatiert ist, fangen wir die JSONDecodeError ab und werfen eine neue ValueError mit einer benutzerfreundlichen Fehlermeldung, damit der Nutzer weiß, dass die Datei ungültiges JSON enthält und die App nicht gestartet werden kann.
        raise ValueError(f"Die Datei {json_path} enthält ungültiges JSON.") from e      #wir verwenden "from e", damit die ursprüngliche Fehlermeldung (z.B. "Expecting value") in der neuen Fehlermeldung enthalten ist, damit der Nutzer mehr Informationen über den Fehler bekommt.
    
daten = lade_lernmodule(JSON_PATH)                          #lädt die Lernmodule-Daten aus der JSON-Datei, damit wir sie in der App verwenden können. Wenn die Datei fehlt oder ungültiges JSON enthält, wird eine Fehlermeldung angezeigt und die App wird nicht gestartet.

def clean_titel(titel_roh: str) -> str:                     
    # entfernt führende Nummern wie "1 - " oder "8.1 - " oder "9.0.0 - "
    return re.sub(r"^\s*\d+(?:\.\d+)*\s*-\s*", "", titel_roh).strip()   

#------------------------------------------------------------------------------------------------

def ermittle_lernfelder(daten: dict) -> list[tuple[str, str]]:  #erwartet dict, gibt Liste von (code, titel) zurück
    """Gibt Lernfelder als (lf_code, titel) zurück."""
    lernfelder = daten.get("Lernfelder", {})                    #stellt sicher, dass wir ein dict haben, auch wenn "Lernfelder" fehlt
    ergebnis: list[tuple[str, str]] = []                        #hier sammeln wir die (code, titel) Paare

    for lf_key, lf_dict in lernfelder.items():                  #z.B. lf_key = "lernmoduleLF01", lf_dict = { "lm01": { "1 - Titel": {...} } }
        lf_code = lf_key.removeprefix("lernmoduleLF")  # z.B. "01"
        lm01 = lf_dict.get("lm01", {})                          #holt das dict unter "lm01", z.B. { "1 - Titel": {...} }
        titel_roh = next(iter(lm01.keys()), f"Lernfeld {lf_code}") #holt den ersten Schlüssel aus lm01, z.B. "1 - Titel", oder falls lm01 leer ist, einen Fallback wie "Lernfeld 01"
        titel = clean_titel(titel_roh)                          #bereinigt den Titel, z.B. "1 - Titel" -> "Titel"
        ergebnis.append((lf_code, titel))                       #fügt das (code, titel) Paar zur Ergebnisliste hinzu

    ergebnis.sort(key=lambda x: int(x[0]))                      #sortiert die Ergebnisliste nach dem numerischen Wert des Codes, z.B. "01" -> 1, "02" -> 2
    return ergebnis                                             #gibt die sortierte Liste von (code, titel) zurück, z.B. [("01", "Titel1"), ("02", "Titel2"), ...]

#------------------------------------------------------------------------------------------------
def ermittle_module_fuer_lernfeld(daten: dict, lf_code: str, skip_lm01: bool = True) -> list[tuple[str, str]]: #erwartet dict, lf_code wie "01", gibt Liste von (lm_key, titel) zurück
    """
    Gibt Module eines Lernfelds als (lm_key, titel) zurück, z.B. ("lm02", "Grundlagen ...").
    skip_lm01=True, weil lm01 bei dir das Thema/Überschrift des Lernfeldes ist.
    """
    lf_key = f"lernmoduleLF{lf_code}"                           #z.B. "lernmoduleLF01"
    lf_dict = daten.get("Lernfelder", {}).get(lf_key, {})       #holt das dict für das Lernfeld, z.B. { "lm01": { "1 - Titel": {...} }, "lm02": { "1 - Titel": {...} }, ... }

    module: list[tuple[str, str]] = []                          #hier sammeln wir die (lm_key, titel) Paare der Module
    for key, mod_dict in lf_dict.items():                       #z.B. key = "lm01", mod_dict = { "1 - Titel": {...} }
        if not key.startswith("lm"):                            #nur Schlüssel betrachten, die mit "lm" beginnen, z.B. "lm01", "lm02", ... Alle anderen ignorieren (falls es welche gibt)
            continue
        if skip_lm01 and key == "lm01":                         #lm01 überspringen, weil es das Thema/Überschrift des Lernfeldes ist und nicht wirklich ein Modul,
            continue

        titel_roh = next(iter((mod_dict or {}).keys()), key.upper())#holt den ersten Schlüssel aus mod_dict, z.B. "1 - Titel", oder falls mod_dict leer oder None ist, einen Fallback wie "LM02" (key.upper())
        titel = clean_titel(titel_roh)                          #bereinigt den Titel, z.B. "1 - Titel" -> "Titel"
        module.append((key, titel))                             #fügt das (lm_key, titel) Paar zur Module-Liste hinzu, z.B. ("lm02", "Grundlagen ...")

    module.sort(key=lambda x: int(x[0][2:]))  # "lm02" -> 2     #sortiert die Module-Liste nach der numerischen Zahl im lm_key, z.B. "lm02" -> 2, "lm10" -> 10
    return module

#------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------

class LernApp:
    def __init__(self, root: tk.Tk, daten: dict):
        self.root = root                                        #speichert die Referenz auf das Hauptfenster
        self.daten = daten                                      #speichert die geladenen Daten aus der JSON-Datei                

        self.current_lf_code: str | None = None #speichert den aktuell ausgewählten Lernfeld-Code, z.B. "01"
        self.current_lf_titel: str | None = None    #speichert den Titel des aktuell ausgewählten Lernfelds, z.B. "Grundlagen der Elektrotechnik"
        self.current_lm_key: str | None = None  #speichert den aktuell ausgewählten Modul-Key, z.B. "lm02"
        self.current_lm_titel: str | None = None    #speichert den Titel des aktuell ausgewählten Moduls, z.B. "Grundlagen der Elektrizität"

        self.container = ttk.Frame(root, padding=10)    #Haupt-Container, in dem die verschiedenen Frames (Ansichten) angezeigt werden. Alle Frames werden hier hineingepackt, aber immer nur eines wird sichtbar sein.
        self.container.pack(fill="both", expand=True)   #Container füllt das Fenster und wächst mit ihm mit

        # Frames (Ansichten)
        self.frame_lernfelder = ttk.Frame(self.container)   #Frame für die Anzeige der Lernfelder
        self.frame_module = ttk.Frame(self.container)       #Frame für die Anzeige der Module eines Lernfelds
        self.frame_actions = ttk.Frame(self.container)      #Frame für die Anzeige der Aktionen (Lernen/Test/Zurück) eines Moduls

        self._zeige_lernfelder()                            #zeigt direkt die Lernfelder-Ansicht an, wenn die App startet

    def _clear(self, frame: ttk.Frame) -> None:             #entfernt alle Widgets aus einem Frame, damit wir ihn neu befüllen können
        for w in frame.winfo_children():                    #geht alle direkten Kind-Widgets des Frames durch
            w.destroy()                                     #zerstört jedes Widget, damit der Frame leer ist

    def _show_only(self, frame: ttk.Frame) -> None:         #zeigt nur den angegebenen Frame an und versteckt die anderen Frames, damit wir zwischen den Ansichten wechseln können
        for f in (self.frame_lernfelder, self.frame_module, self.frame_actions):    #geht alle Frames durch
            f.pack_forget()                                                         #versteckt jedes Frame, damit nur das gewünschte Frame sichtbar ist
        frame.pack(fill="both", expand=True)                        #zeigt das angegebene Frame an, damit es sichtbar ist

    # -------------------- View 1: Lernfelder --------------------

    def _zeige_lernfelder(self) -> None:                    #zeigt die Lernfelder-Ansicht an, in der alle Lernfelder als Buttons aufgelistet werden. Beim Klick auf ein Lernfeld wird die Module-Ansicht für dieses Lernfeld angezeigt.
        self._clear(self.frame_lernfelder)                  #leert den Lernfelder-Frame, damit wir ihn neu befüllen können, falls wir von einer anderen Ansicht zurückkommen
        self._show_only(self.frame_lernfelder)              #zeigt nur den Lernfelder-Frame an, damit er sichtbar ist und die anderen Frames versteckt sind

        ttk.Label(self.frame_lernfelder, text="Lernfelder", font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 10))   #Überschrift für die Lernfelder-Ansicht

        sf = ScrollableFrame(self.frame_lernfelder) #erstellt einen ScrollableFrame, damit wir eine scrollbare Liste von Lernfeldern haben, falls es viele gibt
        sf.pack(fill="both", expand=True)           #lässt den ScrollableFrame das gesamte Frame ausfüllen und mit ihm wachsen

        lernfelder_info = ermittle_lernfelder(self.daten)   #ermittelt die Lernfelder-Informationen als Liste von (code, titel), z.B. [("01", "Grundlagen der Elektrotechnik"), ("02", "Elektrische Energieverteilung"), ...]
        for code, titel in lernfelder_info:                 #   geht alle Lernfelder durch, z.B. code = "01", titel = "Grundlagen der Elektrotechnik"
            ttk.Button(                                     
                sf.inner,
                text=f"{code} - {titel}",
                command=lambda c=code, t=titel: self._on_lernfeld_click(c, t)
            ).pack(fill="x", pady=4)    #erstellt für jedes Lernfeld einen Button mit dem Text "code - titel", z.B. "01 - Grundlagen der Elektrotechnik". Beim Klick auf den Button wird die Funktion _on_lernfeld_click mit den entsprechenden code und titel als Argumente aufgerufen, damit wir die Module-Ansicht für dieses Lernfeld anzeigen können.

    def _on_lernfeld_click(self, code: str, titel: str) -> None:
        self.current_lf_code = code
        self.current_lf_titel = titel
        self._zeige_module()


    # -------------------- View 2: Module (lmXX) --------------------
    def _zeige_module(self) -> None:
        self._clear(self.frame_module)  #leert den Module-Frame, damit wir ihn neu befüllen können, falls wir von einer anderen Ansicht zurückkommen
        self._show_only(self.frame_module)  #zeigt nur den Module-Frame an, damit er sichtbar ist und die anderen Frames versteckt sind

        ttk.Label(
            self.frame_module,
            text=f"Lernfeld {self.current_lf_code} - {self.current_lf_titel}",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 10))    #Überschrift für die Module-Ansicht, zeigt den Code und Titel des aktuell ausgewählten Lernfelds an, z.B. "Lernfeld 01 - Grundlagen der Elektrotechnik"

        sf = ScrollableFrame(self.frame_module) #erstellt einen ScrollableFrame, damit wir eine scrollbare Liste von Modulen haben, falls es viele gibt
        sf.pack(fill="both", expand=True)       #lässt den ScrollableFrame das gesamte Frame ausfüllen und mit ihm wachsen

        module_info = ermittle_module_fuer_lernfeld(self.daten, self.current_lf_code or "00", skip_lm01=True)   #ermittelt die Module-Informationen für das aktuell ausgewählte Lernfeld als Liste von (lm_key, titel), z.B. [("lm02", "Grundlagen der Elektrizität"), ("lm03", "Elektrische Größen und Einheiten"), ...]. skip_lm01=True, weil lm01 das Thema/Überschrift des Lernfeldes ist und nicht wirklich ein Modul.

        if not module_info:                         #wenn keine Module gefunden wurden, z.B. weil das Lernfeld leer ist oder nur lm01 enthält, zeigen wir eine Info anstatt Buttons an
            ttk.Label(sf.inner, text="Keine Module (lmXX) gefunden.").pack(anchor="w", pady=(0, 10))    #zeigt eine Info an, dass keine Module gefunden wurden, damit der Nutzer weiß, dass es hier nichts zu lernen oder testen gibt
        else:
            for lm_key, lm_titel in module_info:    #   geht alle Module durch, z.B. lm_key = "lm02", lm_titel = "Grundlagen der Elektrizität"
                ttk.Button(
                    sf.inner,
                    text=f"{lm_key} - {lm_titel}",
                    command=lambda k=lm_key, t=lm_titel: self._on_modul_click(k, t)
                ).pack(fill="x", pady=4)                #erstellt für jedes Modul einen Button mit dem Text "lm_key - lm_titel", z.B. "lm02 - Grundlagen der Elektrizität". Beim Klick auf den Button wird die Funktion _on_modul_click mit den entsprechenden lm_key und lm_titel als Argumente aufgerufen, damit wir die Aktionen-Ansicht für dieses Modul anzeigen können.

        ttk.Button(self.frame_module, text="Zurück", command=self._zeige_lernfelder).pack(anchor="w", pady=(12, 0))   #erstellt einen Zurück-Button, der den Nutzer zurück zur Lernfelder-Ansicht bringt, damit er ein anderes Lernfeld auswählen kann

    def _on_modul_click(self, lm_key: str, lm_titel: str) -> None:  #wenn ein Modul-Button geklickt wird, speichern wir den lm_key und lm_titel des ausgewählten Moduls, damit wir sie in der Aktionen-Ansicht anzeigen können, und zeigen dann die Aktionen-Ansicht an
        self.current_lm_key = lm_key                                #speichert den lm_key des aktuell ausgewählten Moduls, z.B. "lm02", damit wir ihn in der Aktionen-Ansicht anzeigen können
        self.current_lm_titel = lm_titel                            #speichert den lm_titel des aktuell ausgewählten Moduls, z.B. "Grundlagen der Elektrizität", damit wir ihn in der Aktionen-Ansicht anzeigen können
        self._zeige_actions()                                       #zeigt die Aktionen-Ansicht an, damit der Nutzer die Optionen Lernen/Test/Zurück für das ausgewählte Modul sieht und auswählen kann

    # -------------------- View 3: Aktionen (Lernen/Test/Zurück) --------------------
    def _zeige_actions(self) -> None:                       #zeigt die Aktionen-Ansicht an, in der die Optionen Lernen/Test/Zurück für das aktuell ausgewählte Modul angezeigt werden. Beim Klick auf Lernen oder Test wird eine Info-Box angezeigt (später: Lernmodus/Testmodus starten). Beim Klick auf Zurück wird die Module-Ansicht für das aktuelle Lernfeld angezeigt.
        self._clear(self.frame_actions)                     #leert den Aktionen-Frame, damit wir ihn neu befüllen können, falls wir von einer anderen Ansicht zurückkommen
        self._show_only(self.frame_actions)                 #zeigt nur den Aktionen-Frame an, damit er sichtbar ist und die anderen Frames versteckt sind

        ttk.Label(
            self.frame_actions,
            text=f"{self.current_lf_code} - {self.current_lf_titel}\n{self.current_lm_key} - {self.current_lm_titel}",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 12))    #Überschrift für die Aktionen-Ansicht, zeigt den Code und Titel des aktuell ausgewählten Lernfelds und Moduls an, z.B. "01 - Grundlagen der Elektrotechnik\nlm02 - Grundlagen der Elektrizität"

        btn_row = ttk.Frame(self.frame_actions) #erstellt einen Frame für die Buttons, damit wir sie in einer Zeile anordnen können, damit die Aktionen-Buttons Lernen/Test/Zurück nebeneinander statt untereinander angezeigt werden
        btn_row.pack(anchor="w", fill="x")      #lässt den Button-Row-Frame die gesamte Breite ausfüllen, damit die Buttons sich gleichmäßig verteilen können

        ttk.Button(btn_row, text="Lernen", command=self._start_lernen).pack(side="left", padx=(0, 8))   #erstellt einen Lernen-Button, der die Funktion _start_lernen aufruft, wenn er geklickt wird, damit wir später den Lernmodus für das ausgewählte Modul starten können. Der Button wird links im Button-Row-Frame angeordnet und bekommt einen kleinen Abstand nach rechts (8 Pixel), damit er nicht direkt am nächsten Button klebt.
        ttk.Button(btn_row, text="Test", command=self._start_test).pack(side="left", padx=(0, 8))       #erstellt einen Test-Button, der die Funktion _start_test aufruft, wenn er geklickt wird, damit wir später den Testmodus für das ausgewählte Modul starten können. Der Button wird links im Button-Row-Frame angeordnet und bekommt einen kleinen Abstand nach rechts (8 Pixel), damit er nicht direkt am nächsten Button klebt.
        ttk.Button(btn_row, text="Zurück", command=self._zeige_module).pack(side="left")                #erstellt einen Zurück-Button, der die Funktion _zeige_module aufruft, wenn er geklickt wird, damit der Nutzer zurück zur Module-Ansicht für das aktuelle Lernfeld kommt. Der Button wird links im Button-Row-Frame angeordnet und bekommt keinen Abstand nach rechts, damit er direkt am nächsten Button klebt.

    def _start_lernen(self) -> None:
        # Hier später: Modul laden + Lernmodus starten
        messagebox.showinfo("Lernen", f"Starte Lernen: {self.current_lm_key} - {self.current_lm_titel}")    #zeigt eine Info-Box an, dass der Lernmodus für das aktuell ausgewählte Modul gestartet wird, damit der Nutzer eine Rückmeldung bekommt, dass seine Aktion erkannt wurde. Später soll hier der eigentliche Lernmodus gestartet werden, z.B. indem ein neues Fenster mit den Lerninhalten geöffnet wird.

    def _start_test(self) -> None:
        # Hier später: Testmodus starten
        messagebox.showinfo("Test", f"Starte Test: {self.current_lm_key} - {self.current_lm_titel}")        #zeigt eine Info-Box an, dass der Testmodus für das aktuell ausgewählte Modul gestartet wird, damit der Nutzer eine Rückmeldung bekommt, dass seine Aktion erkannt wurde. Später soll hier der eigentliche Testmodus gestartet werden, z.B. indem ein neues Fenster mit den Testfragen geöffnet wird.


# ==============================================================================
def main():
    daten = lade_lernmodule(JSON_PATH)      #lädt die Lernmodule-Daten aus der JSON-Datei, damit wir sie in der App verwenden können. Wenn die Datei fehlt oder ungültiges JSON enthält, wird eine Fehlermeldung angezeigt und die App wird nicht gestartet.

    root = tk.Tk()                          #erstellt das Hauptfenster der App, damit wir eine grafische Benutzeroberfläche haben, in der wir die Lernfelder, Module und Aktionen anzeigen können. Das Fenster wird später mit einem Titel versehen und die LernApp wird darin gestartet.
    root.title("Lernfelder / Module")       #setzt den Titel des Hauptfensters auf "Lernfelder / Module", damit der Nutzer sofort weiß, worum es in der App geht, wenn er sie öffnet.

    app = LernApp(root, daten)              #erstellt eine Instanz der LernApp-Klasse und übergibt ihr das Hauptfenster und die geladenen Daten, damit die App initialisiert wird und die Lernfelder-Ansicht direkt angezeigt wird, wenn die App startet.

    root.mainloop()                         #startet die Haupt-Event-Schleife der App, damit das Fenster angezeigt wird und auf Benutzerinteraktionen reagiert. Die App bleibt so lange geöffnet, bis der Nutzer das Fenster schließt.


if __name__ == "__main__":
    main()
