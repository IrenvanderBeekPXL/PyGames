# TODO
# voeg een functie toe om een kaart van het bordje te vervangen door een kaart die meegegeven wordt als parameter
# De index wordt ook meegegeven als parameter en de vorige kaart moet gereturnt worden

from secrets import randbelow

def hide():
    input("Press enter to hide")
    for i in range(2000):
        print("\n")
    input("Press enter to continue")

kaarten_stapel = []
for i in range(60):
    kaarten_stapel.append(i + 1)

def shuffle(bordjes):
    for i in bordjes:
        for j in range(10):
            i.append(kaarten_stapel[randbelow(len(kaarten_stapel))])

def is_gewonnen(bordje):
    vorige = 0
    for i in bordje:
        if i <= vorige:
            return False
    return True
