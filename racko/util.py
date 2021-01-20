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
    try:
        vorige = 0
        for i in bordje:
            if i >= vorige:
                return False
        return True
    except IndexError:
        return False
 
def verander_kaart(index, volgende_kaart, bordje):
    bordje.insert(index, volgende_kaart)
    return bordje.pop(index + 1)

def hide(next_speler):
    for i in range(2000):
        print("\n")
    print("Speler", next_speler, "is aan de beurt")
    input("Druk op enter...")
