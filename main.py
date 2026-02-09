import json
from json import JSONDecodeError
from pathlib import Path

import tkinter as tk
from tkinter import messagebox, ttk

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

#------------------------------------------------------------------------------------------------

def ermittle_lernfelder(daten: dict) -> list[tuple[str, str]]:
    """Ermittelt die Lernfelder aus den geladenen Daten."""
    lernfelder = daten.get("Lernfelder", {})
    ergebnis: list[tuple[str, str]] = []

    for lf_key, lf_dict in lernfelder.items():
        # Die Lernfeld-ID ist der Schlüssel (lf_key) und der Name ist im Dictionary (lf_dict) unter "Name" zu finden.
        lf_code = lf_key.removeprefix("lernmoduleLF")  # Entfernt das Präfix "lernmoduleLF" von der ID
        lm01 = lf_dict.get("lm01", {})
        titel = next(iter(lm01.keys()), f"Lernfeld {lf_code}")  #Nimmt den ersten Schlüssel aus lm01 als Titel, oder einen Standardtitel
        ergebnis.append((lf_code, titel))
    ergebnis.sort(key=lambda x: x[0])  # Sortiert die Lernfelder nach der ID
    return ergebnis

#------------------------------------------------------------------------------------------------
