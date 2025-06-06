import json


with open("lernmodule.json", "r", encoding="utf-8") as f:
    Text1 = json.load(f)

#print(Text1["modul20"]["lerninhalt"])

for eintrag in Text1["modul20"]["lerninhalt"]:
    print(eintrag)
    input("Drücke Enter für den nächsten Eintrag...\n")


