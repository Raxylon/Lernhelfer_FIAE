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
        titel_roh = next(iter(lm01.keys()), f"Lernfeld {lf_code}")
        titel = clean_titel(titel_roh)
        ergebnis.append((lf_code, titel))

    ergebnis.sort(key=lambda x: int(x[0]))
    return ergebnis

#------------------------------------------------------------------------------------------------
def ermittle_module_fuer_lernfeld(daten: dict, lf_code: str, skip_lm01: bool = True) -> list[tuple[str, str]]:
    """
    Gibt Module eines Lernfelds als (lm_key, titel) zurück, z.B. ("lm02", "Grundlagen ...").
    skip_lm01=True, weil lm01 bei dir das Thema/Überschrift des Lernfeldes ist.
    """
    lf_key = f"lernmoduleLF{lf_code}"
    lf_dict = daten.get("Lernfelder", {}).get(lf_key, {})

    module: list[tuple[str, str]] = []
    for key, mod_dict in lf_dict.items():
        if not key.startswith("lm"):
            continue
        if skip_lm01 and key == "lm01":
            continue

        titel_roh = next(iter((mod_dict or {}).keys()), key.upper())
        titel = clean_titel(titel_roh)
        module.append((key, titel))

    module.sort(key=lambda x: int(x[0][2:]))  # "lm02" -> 2
    return module

#------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------

class LernApp:
    def __init__(self, root: tk.Tk, daten: dict):
        self.root = root
        self.daten = daten

        self.current_lf_code: str | None = None
        self.current_lf_titel: str | None = None
        self.current_lm_key: str | None = None
        self.current_lm_titel: str | None = None

        self.container = ttk.Frame(root, padding=10)
        self.container.pack(fill="both", expand=True)

        # Frames (Ansichten)
        self.frame_lernfelder = ttk.Frame(self.container)
        self.frame_module = ttk.Frame(self.container)
        self.frame_actions = ttk.Frame(self.container)

        self._zeige_lernfelder()

    def _clear(self, frame: ttk.Frame) -> None:
        for w in frame.winfo_children():
            w.destroy()

    def _show_only(self, frame: ttk.Frame) -> None:
        for f in (self.frame_lernfelder, self.frame_module, self.frame_actions):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    # -------------------- View 1: Lernfelder --------------------

    def _zeige_lernfelder(self) -> None:
        self._clear(self.frame_lernfelder)
        self._show_only(self.frame_lernfelder)

        ttk.Label(self.frame_lernfelder, text="Lernfelder", font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 10))

        sf = ScrollableFrame(self.frame_lernfelder)
        sf.pack(fill="both", expand=True)

        lernfelder_info = ermittle_lernfelder(self.daten)
        for code, titel in lernfelder_info:
            ttk.Button(
                sf.inner,
                text=f"{code} - {titel}",
                command=lambda c=code, t=titel: self._on_lernfeld_click(c, t)
            ).pack(fill="x", pady=4)

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
