import json
from json import JSONDecodeError
import textwrap
import tkinter.font as tkfont

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

def lade_lerninhalt(daten: dict, lf_code: str, lm_key: str) -> list[str]:
    """
    Holt den Lerninhalt (Liste von Absätzen) aus der JSON.

    Beispiel-Pfad:
    daten["Lernfelder"]["lernmoduleLF01"]["lm02"]["<Modultitel>"]["lerninhalt"]
    """
    lf_id = f"lernmoduleLF{lf_code}"

    try:
        lf_dict = daten["Lernfelder"][lf_id]
    except KeyError as e:
        raise KeyError(f"Lernfeld {lf_code} ({lf_id}) nicht gefunden.") from e

    try:
        lm_dict = lf_dict[lm_key]  # z.B. {"1.1.1 - ...": {"lerninhalt": [...], "fragen":[...]}}
    except KeyError as e:
        raise KeyError(f"Modul {lm_key} in Lernfeld {lf_code} nicht gefunden.") from e

    modul_titel_key = next(iter(lm_dict.keys()), None)
    if not modul_titel_key:
        raise ValueError(f"Modul {lm_key} hat keinen Titel-Key in der JSON-Struktur.")

    payload = lm_dict.get(modul_titel_key, {})
    lerninhalt = payload.get("lerninhalt", [])

    if not isinstance(lerninhalt, list):
        raise TypeError(f"lerninhalt ist nicht vom Typ list (gefunden: {type(lerninhalt).__name__}).")

    return lerninhalt
#---------------------------------------------------------------------------------

def lade_fragen(daten: dict, lf_code: str, lm_key: str) -> list[dict]:
    """
    Holt die Fragen (Liste von dicts) aus der JSON.

    Pfad:
    daten["Lernfelder"]["lernmoduleLFxx"][lm_key]["<Modultitel>"]["fragen"]
    """
    lf_id = f"lernmoduleLF{lf_code}"

    try:
        lf_dict = daten["Lernfelder"][lf_id]
    except KeyError as e:
        raise KeyError(f"Lernfeld {lf_code} ({lf_id}) nicht gefunden.") from e

    try:
        lm_dict = lf_dict[lm_key]
    except KeyError as e:
        raise KeyError(f"Modul {lm_key} in Lernfeld {lf_code} nicht gefunden.") from e

    modul_titel_key = next(iter(lm_dict.keys()), None)
    if not modul_titel_key:
        raise ValueError(f"Modul {lm_key} hat keinen Titel-Key in der JSON-Struktur.")

    payload = lm_dict.get(modul_titel_key, {})
    fragen = payload.get("fragen", [])

    if not isinstance(fragen, list):
        raise TypeError(f"fragen ist nicht vom Typ list (gefunden: {type(fragen).__name__}).")

    return fragen

#---------------------------------------------------------------------------------

def baue_suchindex(daten: dict) -> list[dict]:
    """
    Erstellt eine Liste durchsuchbarer Einträge.
    Eintrag-Form:
      - type: "LF" oder "LM"
      - lf_code, lf_titel
      - (optional) lm_key, lm_titel
      - search: lower-case Suchtext
    """
    index: list[dict] = []

    lernfelder = daten.get("Lernfelder", {})
    for lf_key, lf_dict in lernfelder.items():
        lf_code = lf_key.removeprefix("lernmoduleLF")

        # Lernfeld-Titel aus lm01
        lm01 = lf_dict.get("lm01", {})
        lf_titel_roh = next(iter(lm01.keys()), f"Lernfeld {lf_code}")
        lf_titel = clean_titel(lf_titel_roh)

        # Lernfeld-Eintrag
        lf_search = f"{lf_code} {lf_titel}".lower()
        index.append({
            "type": "LF",
            "lf_code": lf_code,
            "lf_titel": lf_titel,
            "search": lf_search
        })

        # Module dieses Lernfelds
        for lm_key, lm_dict in lf_dict.items():
            if not lm_key.startswith("lm"):
                continue

            modul_titel_key = next(iter((lm_dict or {}).keys()), lm_key.upper())
            lm_titel = clean_titel(modul_titel_key)

            payload = (lm_dict or {}).get(modul_titel_key, {}) if isinstance(lm_dict, dict) else {}
            lerninhalt = payload.get("lerninhalt", [])
            fragen = payload.get("fragen", [])

            # Viel Suchtext: Titel + Inhalte + Fragen (damit Stichwörter im Text auch treffen)
            textteile: list[str] = [lf_code, lf_titel, lm_key, lm_titel]

            if isinstance(lerninhalt, list):
                textteile.extend(str(x) for x in lerninhalt)

            if isinstance(fragen, list):
                for q in fragen:
                    if isinstance(q, dict):
                        textteile.append(str(q.get("frage", "")))
                        opt = q.get("optionen", [])
                        if isinstance(opt, list):
                            textteile.extend(str(o) for o in opt)

            lm_search = " ".join(textteile).lower()

            index.append({
                "type": "LM",
                "lf_code": lf_code,
                "lf_titel": lf_titel,
                "lm_key": lm_key,
                "lm_titel": lm_titel,
                "search": lm_search
            })

    return index


def suche_im_index(index: list[dict], query: str) -> list[dict]:
    q = query.strip().lower()
    if not q:
        return []
    # AND-Suche über alle Wörter
    terms = [t for t in re.findall(r"\w+", q) if t]
    if not terms:
        return []
    return [item for item in index if all(t in item["search"] for t in terms)]

#---------------------------------------------------------------------------------


def _justify_line_mono(line: str, width: int) -> str:
    """Blocksatz für eine einzelne Zeile (Monospace)."""
    words = line.split()
    if len(words) <= 1:
        return line

    total_chars = sum(len(w) for w in words)
    gaps = len(words) - 1
    spaces_total = width - total_chars
    if spaces_total <= gaps:  # zu wenig Platz -> normal
        return " ".join(words)

    base, extra = divmod(spaces_total, gaps)
    out = []
    for i, w in enumerate(words[:-1]):
        out.append(w)
        out.append(" " * (base + (1 if i < extra else 0)))
    out.append(words[-1])
    return "".join(out)


def _format_blocksatz(text: str, width: int) -> str:
    """Blocksatz-Formatierung (Monospace), absatzweise. Letzte Zeile je Absatz bleibt links."""
    # Absätze trennen
    paras = [p.strip() for p in text.strip().split("\n\n") if p.strip()]
    out_paras = []

    for p in paras:
        # Wenn der Absatz schon Zeilenumbrüche (z.B. Listen) enthält, behandeln wir jede Zeile separat
        lines_in = p.splitlines() if "\n" in p else [p]
        rebuilt = []

        for raw_line in lines_in:
            raw_line = raw_line.strip()
            if not raw_line:
                rebuilt.append("")
                continue

            # Listen/Code-artige Zeilen nicht “kaputt-justifizieren”
            if raw_line.startswith(("-", "*", "•")) or raw_line[:2].isdigit() or raw_line.endswith(":"):
                wrapped = textwrap.wrap(raw_line, width=width, break_long_words=False, break_on_hyphens=False)
                rebuilt.extend(wrapped)
                continue

            wrapped = textwrap.wrap(raw_line, width=width, break_long_words=False, break_on_hyphens=False)
            if not wrapped:
                continue

            for wline in wrapped[:-1]:
                rebuilt.append(_justify_line_mono(wline, width))
            rebuilt.append(wrapped[-1])  # letzte Zeile links

        out_paras.append("\n".join(rebuilt).rstrip())

    return "\n\n".join(out_paras).strip()


class LerninhaltViewer(tk.Toplevel):
    def __init__(self, parent: tk.Tk, titel: str, abschnitte: list[str], blocksatz: bool = True):
        super().__init__(parent)
        self.title(titel)
        self.geometry("900x600")

        self.abschnitte = abschnitte or ["(Kein Lerninhalt vorhanden)"]
        self.idx = 0
        self.blocksatz = blocksatz

        self.frame = ttk.Frame(self, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Kopfzeile (Index/Progress)
        self.lbl_progress = ttk.Label(self.frame, font=("Segoe UI", 11, "bold"))
        self.lbl_progress.pack(anchor="w", pady=(0, 8))

        # Text + Scrollbar
        text_frame = ttk.Frame(self.frame)
        text_frame.pack(fill="both", expand=True)

        self.scroll_y = ttk.Scrollbar(text_frame, orient="vertical")
        self.scroll_y.pack(side="right", fill="y")

        # Monospace hilft beim Blocksatz
        self.text_font = tkfont.Font(family="Courier New" if self.blocksatz else "Segoe UI", size=11)

        self.text = tk.Text(
            text_frame,
            wrap="word" if not self.blocksatz else "none",  # Blocksatz: wir setzen Zeilenumbrüche selbst
            yscrollcommand=self.scroll_y.set,
            font=self.text_font
        )
        self.text.pack(side="left", fill="both", expand=True)
        self.scroll_y.config(command=self.text.yview)

        # Optional: X-Scroll nur bei Blocksatz (falls ein Wort mal länger ist)
        self.scroll_x = None
        if self.blocksatz:
            self.scroll_x = ttk.Scrollbar(self.frame, orient="horizontal", command=self.text.xview)
            self.text.configure(xscrollcommand=self.scroll_x.set)
            self.scroll_x.pack(fill="x", pady=(6, 0))

        # Navigation
        nav = ttk.Frame(self.frame)
        nav.pack(anchor="e", fill="x", pady=(10, 0))

        self.btn_prev = ttk.Button(nav, text="◀ Zurück", command=self.prev)
        self.btn_prev.pack(side="left")

        self.btn_next = ttk.Button(nav, text="Weiter ▶", command=self.next)
        self.btn_next.pack(side="left", padx=(8, 0))

        ttk.Button(nav, text="Schließen", command=self.destroy).pack(side="right")

        # Reflow bei Resize (nur wenn Blocksatz aktiv)
        self._reflow_job = None
        if self.blocksatz:
            self.bind("<Configure>", self._on_resize)

        self.render()

    def _calc_width_chars(self) -> int:
        # Breite in Zeichen, grob aus Pixelbreite und Font-Metrik
        self.update_idletasks()
        px = max(200, self.text.winfo_width() - 20)
        char_px = max(6, self.text_font.measure("0"))
        return max(40, int(px / char_px))

    def _on_resize(self, _event=None):
        if self._reflow_job is not None:
            self.after_cancel(self._reflow_job)
        self._reflow_job = self.after(120, self.render)  # leicht gedrosselt

    def render(self):
        self._reflow_job = None

        total = len(self.abschnitte)
        self.lbl_progress.config(text=f"Abschnitt {self.idx + 1} / {total}")

        raw = self.abschnitte[self.idx].strip()

        if self.blocksatz:
            width_chars = self._calc_width_chars()
            content = _format_blocksatz(raw, width_chars)
        else:
            content = raw

        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("end", content)
        self.text.config(state="disabled")

        self.btn_prev.config(state=("disabled" if self.idx == 0 else "normal"))
        self.btn_next.config(text=("Fertig" if self.idx == total - 1 else "Weiter ▶"))

    def next(self):
        if self.idx >= len(self.abschnitte) - 1:
            self.destroy()
            return
        self.idx += 1
        self.render()
        self.text.yview_moveto(0.0)

    def prev(self):
        if self.idx <= 0:
            return
        self.idx -= 1
        self.render()
        self.text.yview_moveto(0.0)


def zeige_lerninhalt_fenster(parent: tk.Tk, titel: str, abschnitte: list[str], blocksatz: bool = True) -> None:
    LerninhaltViewer(parent, titel, abschnitte, blocksatz=blocksatz)

#---------------------------------------------------------------------------------

class TestViewer(tk.Toplevel):
    def __init__(self, parent: tk.Tk, titel: str, fragen: list[dict]):
        super().__init__(parent)
        self.title(titel)
        self.geometry("900x600")

        self.fragen = fragen or []
        self.idx = 0

        # Speichert Antworten stabil: idx -> {"sel": set[str], "correct": bool}
        self.results: dict[int, dict] = {}

        # Status der aktuellen Frage (für 2-Schritt: prüfen -> weiter)
        self.answered = False

        self.frame = ttk.Frame(self, padding=10)
        self.frame.pack(fill="both", expand=True)

        self.lbl_progress = ttk.Label(self.frame, font=("Segoe UI", 11, "bold"))
        self.lbl_progress.pack(anchor="w", pady=(0, 8))

        self.lbl_frage = ttk.Label(self.frame, wraplength=860, justify="left", font=("Segoe UI", 12))
        self.lbl_frage.pack(anchor="w", pady=(0, 10))

        self.lbl_feedback = ttk.Label(self.frame, wraplength=860, justify="left")
        self.lbl_feedback.pack(anchor="w", pady=(0, 10))

        self.opt_frame = ttk.Frame(self.frame)
        self.opt_frame.pack(fill="x", anchor="w")

        nav = ttk.Frame(self.frame)
        nav.pack(fill="x", pady=(14, 0))

        self.btn_prev = ttk.Button(nav, text="◀ Zurück", command=self.prev)
        self.btn_prev.pack(side="left")

        self.btn_edit = ttk.Button(nav, text="Antwort ändern", command=self.edit_answer)
        self.btn_edit.pack(side="left", padx=(8, 0))

        self.btn_next = ttk.Button(nav, text="Antwort prüfen", command=self.next)
        self.btn_next.pack(side="left", padx=(8, 0))

        ttk.Button(nav, text="Schließen", command=self.destroy).pack(side="right")

        # Auswahl-State
        self.var_single = tk.StringVar(value="")
        self.var_single.trace_add("write", lambda *_: self._maybe_enable_next())

        self.vars_multi: dict[str, tk.IntVar] = {}
        self.multi = False
        self.correct_set: set[str] = set()

        self.bind("<Return>", lambda _e: self.next())

        self.render()

    # ---------------- helpers ----------------
    def _score(self) -> int:
        return sum(1 for v in self.results.values() if v.get("correct") is True)
    
    def _show_result_and_close(self):
        total = len(self.fragen)
        punkte = self._score()
        prozent = int((punkte / total) * 100) if total else 0
        messagebox.showinfo("Ergebnis", f"Du hast {punkte} von {total} richtig. ({prozent}%)", parent=self)
        self.destroy()


    def _clear_options(self):
        for w in self.opt_frame.winfo_children():
            w.destroy()
        self.vars_multi.clear()
        self.var_single.set("")

    def _set_options_enabled(self, enabled: bool) -> None:
        for w in self.opt_frame.winfo_children():
            try:
                if isinstance(w, (ttk.Radiobutton, ttk.Checkbutton)):
                    w.state(["!disabled"] if enabled else ["disabled"])
            except Exception:
                pass

    def _selected_set(self) -> set[str]:
        if self.multi:
            return {k for k, v in self.vars_multi.items() if v.get() == 1}
        v = self.var_single.get().strip().lower()
        return {v} if v else set()

    def _maybe_enable_next(self):
        if self.answered:
            self.btn_next.config(state="normal")
            return
        sel = self._selected_set()
        self.btn_next.config(state=("normal" if sel else "disabled"))

    def _normalize(self, q: dict):
        frage_text = (q.get("frage") or "").strip()

        optionen = q.get("optionen") or []
        if not isinstance(optionen, list):
            optionen = []

        ans = q.get("antwort", "")
        letters = []
        if isinstance(ans, str):
            letters = re.findall(r"[a-zA-Z]", ans)
        elif isinstance(ans, list):
            for x in ans:
                if isinstance(x, str):
                    letters.extend(re.findall(r"[a-zA-Z]", x))
        correct_set = {c.lower() for c in letters}

        opts_norm: list[tuple[str, str]] = []
        for i, opt in enumerate(optionen):
            opt_str = str(opt).strip()
            m = re.match(r"^\s*([a-zA-Z])\)", opt_str)
            letter = (m.group(1).lower() if m else chr(ord("a") + i))
            opts_norm.append((letter, opt_str))

        multi = len(correct_set) > 1
        schwierigkeit = (q.get("schwierigkeit") or "").strip()
        return frage_text, opts_norm, correct_set, multi, schwierigkeit

    # ---------------- rendering ----------------
    def render(self):
        if not self.fragen:
            self.answered = False
            self.lbl_progress.config(text="Keine Fragen vorhanden.")
            self.lbl_frage.config(text="In diesem Modul wurden keine Testfragen gefunden.")
            self.lbl_feedback.config(text="")
            self._clear_options()
            self.btn_prev.config(state="disabled")
            self.btn_edit.config(state="disabled")
            self.btn_next.config(state="disabled")
            return

        total = len(self.fragen)
        q = self.fragen[self.idx]
        frage_text, opts_norm, correct_set, multi, schwierigkeit = self._normalize(q)

        self.correct_set = correct_set
        self.multi = multi

        # WICHTIG: Reset VOR _clear_options(), weil _clear_options var_single.set("") triggert (trace)
        self.answered = False

        punkte = self._score()
        prog = f"Frage {self.idx + 1} / {total}  •  Punkte: {punkte}"
        if schwierigkeit:
            prog += f"  •  {schwierigkeit}"
        self.lbl_progress.config(text=prog)

        self.lbl_frage.config(text=frage_text if frage_text else "(Fragetext fehlt)")
        self.lbl_feedback.config(text="")

        self._clear_options()

        # Optionen bauen
        if self.multi:
            ttk.Label(self.opt_frame, text="(Mehrfachauswahl möglich)").pack(anchor="w", pady=(0, 6))
            for letter, text in opts_norm:
                v = tk.IntVar(value=0)
                self.vars_multi[letter] = v
                ttk.Checkbutton(
                    self.opt_frame,
                    text=text,
                    variable=v,
                    command=self._maybe_enable_next
                ).pack(anchor="w", pady=2)
        else:
            for letter, text in opts_norm:
                ttk.Radiobutton(
                    self.opt_frame,
                    text=text,
                    value=letter,
                    variable=self.var_single
                ).pack(anchor="w", pady=2)

        # Navigation-Buttons
        self.btn_prev.config(state=("disabled" if self.idx == 0 else "normal"))

        # Falls diese Frage schon beantwortet wurde: wiederherstellen + sperren + Feedback zeigen
        if self.idx in self.results:
            saved_sel: set[str] = set(self.results[self.idx].get("sel", set()))
            saved_correct: bool = bool(self.results[self.idx].get("correct", False))

            # Auswahl setzen
            if self.multi:
                for k, v in self.vars_multi.items():
                    v.set(1 if k in saved_sel else 0)
            else:
                self.var_single.set(next(iter(saved_sel), ""))

            # Feedback setzen
            if saved_correct:
                self.lbl_feedback.config(text="✅ Richtig.")
            else:
                corr = ", ".join(sorted(self.correct_set)) if self.correct_set else "?"
                self.lbl_feedback.config(text=f"❌ Falsch. Richtig wäre: {corr}")

            self.answered = True
            self._set_options_enabled(False)

            if self.idx >= total - 1:
                self.btn_next.config(text="Ergebnis anzeigen")
            else:
                self.btn_next.config(text="Weiter ▶")

            self.btn_edit.config(state="normal")
            self.btn_next.config(state="normal")
        else:
            # Neue/unbeantwortete Frage
            self.btn_edit.config(state="disabled")
            self.btn_next.config(text="Antwort prüfen")
            self._set_options_enabled(True)
            self._maybe_enable_next()

    # ---------------- actions ----------------
    def edit_answer(self):
        # Antwort löschen (damit Score stimmt), dann entsperren
        if self.idx in self.results:
            del self.results[self.idx]
        self.answered = False
        self.lbl_feedback.config(text="")
        self._set_options_enabled(True)
        self.btn_edit.config(state="disabled")
        self.btn_next.config(text="Antwort prüfen")
        self._maybe_enable_next()

        # Progress aktualisieren (Punkte können sinken)
        total = len(self.fragen)
        punkte = self._score()
        self.lbl_progress.config(text=f"Frage {self.idx + 1} / {total}  •  Punkte: {punkte}")

    def next(self):
        if not self.fragen:
            return

        total = len(self.fragen)

        # Schritt 1: Prüfen
        if not self.answered:
            sel = self._selected_set()
            if not sel:
                self._maybe_enable_next()
                return

            correct = (sel == self.correct_set)

            # Speichern (und Score stabil halten)
            self.results[self.idx] = {"sel": set(sel), "correct": correct}

            if correct:
                self.lbl_feedback.config(text="✅ Richtig.")
            else:
                corr = ", ".join(sorted(self.correct_set)) if self.correct_set else "?"
                self.lbl_feedback.config(text=f"❌ Falsch. Richtig wäre: {corr}")

            self.answered = True
            self._set_options_enabled(False)

            # Buttontext
            if self.idx >= total - 1:
                self.btn_next.config(text="Ergebnis anzeigen")
            else:
                self.btn_next.config(text="Weiter ▶")

            self.btn_edit.config(state="normal")
            self.btn_next.config(state="normal")

            # Progress (Punkte) aktualisieren
            punkte = self._score()
            prog = f"Frage {self.idx + 1} / {total}  •  Punkte: {punkte}"
            self.lbl_progress.config(text=prog)

            return

        # Schritt 2: Weiter / Ergebnis
        if self.idx >= total - 1:
            self.after(0, self._show_result_and_close)  # sauber über den Eventloop
            return


        self.idx += 1
        self.render()

    def prev(self):
        if self.idx <= 0:
            return
        self.idx -= 1
        self.render()



def zeige_test_fenster(parent: tk.Tk, titel: str, fragen: list[dict]) -> None:
    TestViewer(parent, titel, fragen)

#---------------------------------------------------------------------------

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

        # ---- Suchleiste (bleibt immer sichtbar) ----
        self.search_index = baue_suchindex(self.daten)

        self.search_var = tk.StringVar()

        topbar = ttk.Frame(self.container)
        topbar.pack(fill="x", pady=(0, 8))

        ttk.Label(topbar, text="Suche:").pack(side="left")
        entry = ttk.Entry(topbar, textvariable=self.search_var)
        entry.pack(side="left", fill="x", expand=True, padx=(6, 6))
        entry.bind("<Return>", lambda _e: self._suche())

        ttk.Button(topbar, text="Suchen", command=self._suche).pack(side="left")
        ttk.Button(topbar, text="Leeren", command=self._clear_search).pack(side="left", padx=(6, 0))


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

    def _clear_search(self):
        self.search_var.set("")
        self._zeige_lernfelder()

    def _suche(self):
        query = self.search_var.get().strip()
        if not query:
            self._zeige_lernfelder()
            return
        self._zeige_suchergebnisse(query)

    def _zeige_suchergebnisse(self, query: str):
        self._clear(self.frame_lernfelder)
        self._show_only(self.frame_lernfelder)

        results = suche_im_index(self.search_index, query)
        lfs = [r for r in results if r.get("type") == "LF"]
        lms = [r for r in results if r.get("type") == "LM"]

        ttk.Label(
            self.frame_lernfelder,
            text=f"Suchergebnisse für: {query}",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", pady=(0, 6))

        ttk.Label(
            self.frame_lernfelder,
            text=f"Gefunden: {len(lfs)} Lernfelder, {len(lms)} Module",
        ).pack(anchor="w", pady=(0, 10))

        sf = ScrollableFrame(self.frame_lernfelder)
        sf.pack(fill="both", expand=True)

        if not results:
            ttk.Label(sf.inner, text="Keine Treffer.").pack(anchor="w")
            return

        if lfs:
            ttk.Label(sf.inner, text="Lernfelder", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 6))
            for r in lfs:
                ttk.Button(
                    sf.inner,
                    text=f"{r['lf_code']} - {r['lf_titel']}",
                    command=lambda rr=r: self._on_lernfeld_click(rr["lf_code"], rr["lf_titel"])
                ).pack(fill="x", pady=2)

        if lms:
            ttk.Label(sf.inner, text="Module", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(12, 6))
            for r in lms:
                ttk.Button(
                    sf.inner,
                    text=f"{r['lf_code']}/{r['lm_key']} - {r['lm_titel']}",
                    command=lambda rr=r: self._open_modul_from_search(rr)
                ).pack(fill="x", pady=2)

    def _open_modul_from_search(self, r: dict):
        # direkt zum Modul springen (Aktionen-Ansicht)
        self.current_lf_code = r["lf_code"]
        self.current_lf_titel = r["lf_titel"]
        self.current_lm_key = r["lm_key"]
        self.current_lm_titel = r["lm_titel"]
        self._zeige_actions()
    

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

        module_info = ermittle_module_fuer_lernfeld(self.daten, self.current_lf_code or "00", skip_lm01=False)   #ermittelt die Module-Informationen für das aktuell ausgewählte Lernfeld als Liste von (lm_key, titel), z.B. [("lm02", "Grundlagen der Elektrizität"), ("lm03", "Elektrische Größen und Einheiten"), ...]. skip_lm01=True, weil lm01 das Thema/Überschrift des Lernfeldes ist und nicht wirklich ein Modul.

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
        try:
            abschnitte = lade_lerninhalt(self.daten, self.current_lf_code, self.current_lm_key)
        except Exception as e:
            messagebox.showerror("Fehler", str(e))
            return

        titel = f"Lernen: {self.current_lf_code} / {self.current_lm_key}"
        zeige_lerninhalt_fenster(self.root, titel, abschnitte, blocksatz=True)

    def _start_test(self) -> None:
        try:
            fragen = lade_fragen(self.daten, self.current_lf_code, self.current_lm_key)
        except Exception as e:
            messagebox.showerror("Fehler", str(e))
            return

        titel = f"Test: {self.current_lf_code} / {self.current_lm_key}"
        zeige_test_fenster(self.root, titel, fragen)


# ==============================================================================
def main():
    daten = lade_lernmodule(JSON_PATH)      #lädt die Lernmodule-Daten aus der JSON-Datei, damit wir sie in der App verwenden können. Wenn die Datei fehlt oder ungültiges JSON enthält, wird eine Fehlermeldung angezeigt und die App wird nicht gestartet.

    root = tk.Tk()                          #erstellt das Hauptfenster der App, damit wir eine grafische Benutzeroberfläche haben, in der wir die Lernfelder, Module und Aktionen anzeigen können. Das Fenster wird später mit einem Titel versehen und die LernApp wird darin gestartet.
    root.title("Lernfelder / Module")       #setzt den Titel des Hauptfensters auf "Lernfelder / Module", damit der Nutzer sofort weiß, worum es in der App geht, wenn er sie öffnet.

    app = LernApp(root, daten)              #erstellt eine Instanz der LernApp-Klasse und übergibt ihr das Hauptfenster und die geladenen Daten, damit die App initialisiert wird und die Lernfelder-Ansicht direkt angezeigt wird, wenn die App startet.

    root.mainloop()                         #startet die Haupt-Event-Schleife der App, damit das Fenster angezeigt wird und auf Benutzerinteraktionen reagiert. Die App bleibt so lange geöffnet, bis der Nutzer das Fenster schließt.


if __name__ == "__main__":
    main()
