from lf08 import menu

lernfelder = [
    "lf01","lf02","lf03","lf04","lf05","lf06","lf07","lf08","lf09","lf10","lf11","lf12"]


def auswahl_lernfeld(): #rate doch mal

    for index, value in enumerate(lernfelder,1): # einmal liste durchnummeriere (enumerate), und mit name zeigen (value)
        print(f"{index}-{value.upper()}")

    #return x
    while True:
        for index, value in enumerate(lernfelder,1):  # einmal liste durchnummeriere (enumerate), und mit name zeigen (value)
            print(f"{index}-{value.upper()}")
        x = int(input("0 - zum verlassen \nWelches Lernfeld? Bitte eine Zahl von 1 - 12.\n-->"))
        if x == 0:
            print("Auf wiedersehen mein Fürst.")
            break

        elif x <= 7 or x >= 9:
            print("leider ist dieses Lernfeld noch nicht implementiert!")

        else:
            print("gut gmaht")
            menu()

auswahl_lernfeld()
