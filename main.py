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
        with json_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Die Datei {json_path} wurde nicht gefunden.") from e
    except JSONDecodeError as e:
        raise ValueError(f"Die Datei {json_path} enthält ungültiges JSON.") from e
    
daten = lade_lernmodule(JSON_PATH)

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
        self._clear(self.frame_module)
        self._show_only(self.frame_module)

        ttk.Label(
            self.frame_module,
            text=f"Lernfeld {self.current_lf_code} - {self.current_lf_titel}",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 10))

        sf = ScrollableFrame(self.frame_module)
        sf.pack(fill="both", expand=True)

        module_info = ermittle_module_fuer_lernfeld(self.daten, self.current_lf_code or "00", skip_lm01=True)

        if not module_info:
            ttk.Label(sf.inner, text="Keine Module (lmXX) gefunden.").pack(anchor="w", pady=(0, 10))
        else:
            for lm_key, lm_titel in module_info:
                ttk.Button(
                    sf.inner,
                    text=f"{lm_key} - {lm_titel}",
                    command=lambda k=lm_key, t=lm_titel: self._on_modul_click(k, t)
                ).pack(fill="x", pady=4)

        ttk.Button(self.frame_module, text="Zurück", command=self._zeige_lernfelder).pack(anchor="w", pady=(12, 0))

    def _on_modul_click(self, lm_key: str, lm_titel: str) -> None:
        self.current_lm_key = lm_key
        self.current_lm_titel = lm_titel
        self._zeige_actions()

    # -------------------- View 3: Aktionen (Lernen/Test/Zurück) --------------------
    def _zeige_actions(self) -> None:
        self._clear(self.frame_actions)
        self._show_only(self.frame_actions)

        ttk.Label(
            self.frame_actions,
            text=f"{self.current_lf_code} - {self.current_lf_titel}\n{self.current_lm_key} - {self.current_lm_titel}",
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(0, 12))

        btn_row = ttk.Frame(self.frame_actions)
        btn_row.pack(anchor="w", fill="x")

        ttk.Button(btn_row, text="Lernen", command=self._start_lernen).pack(side="left", padx=(0, 8))
        ttk.Button(btn_row, text="Test", command=self._start_test).pack(side="left", padx=(0, 8))
        ttk.Button(btn_row, text="Zurück", command=self._zeige_module).pack(side="left")

    def _start_lernen(self) -> None:
        # Hier später: Modul laden + Lernmodus starten
        messagebox.showinfo("Lernen", f"Starte Lernen: {self.current_lm_key} - {self.current_lm_titel}")

    def _start_test(self) -> None:
        # Hier später: Testmodus starten
        messagebox.showinfo("Test", f"Starte Test: {self.current_lm_key} - {self.current_lm_titel}")


# ==============================================================================
def main():
    daten = lade_lernmodule(JSON_PATH)

    root = tk.Tk()
    root.title("Lernfelder / Module")

    app = LernApp(root, daten)

    root.mainloop()


if __name__ == "__main__":
    main()
